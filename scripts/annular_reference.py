"""Build and check a source-bound annular solid reference.

The external job supplies all dimensions, source bindings, metadata and local
placement. The helper constructs a plain annulus from two cylinders and a
subtraction; it does not add edge radii, chamfers, material, fit or assembly
placement.
"""
import importlib
import math

from component_records import require_ready
from feature_checks import closed_body, comparison, cylinder_pattern
from source_metadata import compare_source_metadata

METADATA_APPLICATION = 'CADTOOLS_SOURCE'


def _finite(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) \
            or not math.isfinite(value):
        raise ValueError(label + ' must be finite')
    return float(value)


def parameters(job):
    """Validate source readiness and every native construction input."""
    require_ready(job)
    if job.get('units') != 'mm':
        raise ValueError('Annular reference helper supports millimetres only')
    if job.get('geometry_role') != 'reference_annulus':
        raise ValueError('Explicit geometry_role=reference_annulus is required')
    for key in ('part_id', 'part_name', 'representation', 'geometry_name',
                'frame', 'local_frame', 'job_id', 'metadata_request_label'):
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError('Explicit nonempty ' + key + ' is required')
    if job.get('metadata_application') != METADATA_APPLICATION:
        raise ValueError('Geometry.metadata uses the fixed CADTOOLS_SOURCE application')
    feature_names = job.get('dimension_features')
    if not isinstance(feature_names, dict) or set(feature_names) != {
            'bore_diameter', 'outside_diameter', 'thickness'}:
        raise ValueError('dimension_features must bind bore_diameter, outside_diameter and thickness')
    if any(not isinstance(name, str) or not name.strip()
           for name in feature_names.values()) or len(set(feature_names.values())) != 3:
        raise ValueError('Three distinct readable source feature names are required')
    by_name = {feature['name']: feature for feature in job['features']}
    dimensions = {}
    for dimension, name in feature_names.items():
        feature = by_name.get(name)
        if feature is None or feature.get('required') is not True:
            raise ValueError('Required source feature is missing: ' + name)
        if feature.get('unit') != 'mm':
            raise ValueError('Source feature must use mm: ' + name)
        dimensions[dimension] = _finite(feature.get('value'), name + ' value')
        if dimensions[dimension] <= 0:
            raise ValueError('Positive source dimension required: ' + name)
    if dimensions['bore_diameter'] >= dimensions['outside_diameter']:
        raise ValueError('Bore diameter must be smaller than outside diameter')
    center = job.get('center')
    if not isinstance(center, (list, tuple)) or len(center) != 2:
        raise ValueError('Explicit two-coordinate local XY center is required')
    center = [_finite(value, 'center coordinate') for value in center]
    z_origin = _finite(job.get('z_origin'), 'z_origin')
    overrun = _finite(job.get('construction', {}).get('cutter_overrun_mm'),
                      'cutter_overrun_mm')
    if overrun <= 0:
        raise ValueError('Positive cutter_overrun_mm is required')
    far_z = z_origin + dimensions['thickness']
    cut_start, cut_end = z_origin - overrun, far_z + overrun
    bore_radius = dimensions['bore_diameter'] / 2
    outside_radius = dimensions['outside_diameter'] / 2
    cutter_height = cut_end - cut_start
    if not math.isfinite(far_z) or far_z <= z_origin \
            or not math.isfinite(cut_start) or cut_start >= z_origin \
            or not math.isfinite(cut_end) or cut_end <= far_z \
            or not math.isfinite(bore_radius) or bore_radius <= 0 \
            or not math.isfinite(outside_radius) or outside_radius <= 0 \
            or not math.isfinite(cutter_height) or cutter_height <= 0:
        raise ValueError('Annular placement or cutter overrun collapses or overflows numerically')
    for coordinate, extent, label in (
            (center[0], outside_radius, 'X'),
            (center[1], outside_radius, 'Y')):
        lo, hi = coordinate - extent, coordinate + extent
        if not math.isfinite(lo) or not math.isfinite(hi) or lo >= coordinate or hi <= coordinate:
            raise ValueError('Annular ' + label + ' bounds collapse or overflow numerically')
    tolerance = _finite(job.get('readback_tolerance', 1e-7), 'readback_tolerance')
    if tolerance <= 0:
        raise ValueError('Positive readback_tolerance is required')
    if dimensions['outside_diameter'] - dimensions['bore_diameter'] <= 2 * tolerance:
        raise ValueError('Bore and outside cylinder diameters must be numerically distinguishable')
    extra_metadata = job.get('metadata', [])
    if not isinstance(extra_metadata, list) or any(
            not isinstance(value, str) or not value.strip() for value in extra_metadata):
        raise ValueError('metadata must be a list of nonempty strings')
    metadata = [job['part_id'], job['part_name'], job['representation'],
                'Units: mm', 'Frame: ' + job['local_frame'], 'Source job: ' + job['job_id'],
                'Nominal annulus; no edge radius or chamfer represented'] + extra_metadata
    return {'dimensions': dimensions, 'center': center, 'z_origin': z_origin,
            'far_z': far_z, 'cut_start': cut_start, 'cut_end': cut_end,
            'cutter_height': cutter_height, 'overrun': overrun,
            'tolerance': tolerance, 'metadata': metadata}


def geometry(client):
    """Create the existing guarded OCS Geometry adapter."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_annulus(client, job):
    """Create one annular reference solid after full read-only preflight."""
    p = parameters(job)
    dims, center = p['dimensions'], p['center']
    x, y = center
    g = geometry(client)
    outer = g.cylinder(job['geometry_name'] + ' outside cylinder',
                       [x, y, p['z_origin']], dims['outside_diameter'] / 2,
                       dims['thickness'])
    bore = g.cylinder(job['geometry_name'] + ' through-bore cutter',
                      [x, y, p['cut_start']], dims['bore_diameter'] / 2,
                      p['cutter_height'])
    solid = g.subtract(job['geometry_name'] + ' annular solid', outer, [bore])
    g.metadata(job['metadata_request_label'], [solid], p['metadata'])
    return solid


def verify(features, job):
    """Check analytic cylinders, end planes, annular loops and body topology."""
    p = parameters(job)
    d, center, tolerance = p['dimensions'], p['center'], p['tolerance']
    cylinders = features.get('cylinders')
    if not isinstance(cylinders, list) or not cylinders:
        raise ValueError('Native cylinder surface observations are required')
    allowed_diameters = (d['outside_diameter'], d['bore_diameter'])
    unexpected_cylinders = []
    observed_families = set()
    for cylinder in cylinders:
        axis = cylinder.get('axis', [])
        origin = cylinder.get('origin', [])
        if len(axis) != 3 or len(origin) != 3:
            raise ValueError('Native cylinder axis and origin records must be three-dimensional')
        axis = [_finite(value, 'native cylinder axis') for value in axis]
        origin = [_finite(value, 'native cylinder origin') for value in origin]
        radius = _finite(cylinder.get('radius'), 'native cylinder radius')
        if radius <= 0:
            raise ValueError('Native cylinder radius must be positive')
        diameter = 2 * radius
        family = next((expected for expected in allowed_diameters
                       if abs(diameter - expected) <= tolerance), None)
        if (family is None or abs(abs(axis[2]) - 1) > tolerance
                or abs(axis[0]) > tolerance or abs(axis[1]) > tolerance
                or abs(origin[0] - center[0]) > tolerance
                or abs(origin[1] - center[1]) > tolerance):
            unexpected_cylinders.append({'diameter': diameter,
                                         'axis': axis, 'origin': origin})
        else:
            observed_families.add(family)
    checks = [
        cylinder_pattern('Outside cylindrical surface diameter and axis', features,
                         d['outside_diameter'], 2, [center], tolerance),
        cylinder_pattern('Through-bore cylindrical surface diameter and axis', features,
                         d['bore_diameter'], 2, [center], tolerance),
    ]
    checks.append({'check': 'Only the expected concentric bore and outside cylinders are present',
                   'observed_unexpected_surfaces': unexpected_cylinders,
                   'observed_diameter_families_mm': sorted(observed_families),
                   'expected_diameter_families_mm': sorted(allowed_diameters),
                   'method': 'all native analytic cylinder records against the two source-bound radii and common axis',
                   'result': 'PASS' if not unexpected_cylinders
                   and set(allowed_diameters) == observed_families else 'FAIL'})
    noncylindrical = {name: features.get(name, []) for name in ('cones', 'spheres')
                      if features.get(name)}
    checks.append({'check': 'No additional conical or spherical surfaces',
                   'observed': noncylindrical, 'expected': {},
                   'method': 'native analytic surface inventory',
                   'result': 'PASS' if not noncylindrical else 'FAIL'})
    planes = features.get('planes')
    if not isinstance(planes, list) or not planes:
        raise ValueError('Native planar end-face observations are required')
    z_values = []
    unexpected_planes = []
    for plane in planes:
        normal = plane.get('normal', [])
        origin = plane.get('origin', [])
        if len(normal) != 3 or len(origin) != 3:
            raise ValueError('Native plane normal and origin records must be three-dimensional')
        normal = [_finite(value, 'native plane normal') for value in normal]
        origin = [_finite(value, 'native plane origin') for value in origin]
        station = origin[2]
        if (abs(abs(normal[2]) - 1) > tolerance or abs(normal[0]) > tolerance
                or abs(normal[1]) > tolerance
                or min(abs(station - p['z_origin']), abs(station - p['far_z'])) > tolerance):
            unexpected_planes.append({'origin': origin, 'normal': normal})
        z_values.append(station)
    z_faces = []
    for station in sorted(z_values):
        if not z_faces or abs(station - z_faces[-1]) > tolerance:
            z_faces.append(station)
    checks.append(comparison('Annulus flat end-face stations', z_faces,
                             [p['z_origin'], p['far_z']], tolerance))
    checks.append({'check': 'Only planes parallel to the annular end faces are present',
                   'observed_unexpected_surfaces': unexpected_planes,
                   'method': 'all native analytic plane records against lower and upper end-face stations',
                   'result': 'PASS' if not unexpected_planes else 'FAIL'})
    face_loops = features.get('planar_face_loops')
    if not isinstance(face_loops, list):
        raise ValueError('Native planar_face_loops observations are required to confirm the through-bore')
    end_loop_counts = {}
    for label, station in (('lower', p['z_origin']), ('upper', p['far_z'])):
        matching = [face for face in face_loops
                    if abs(abs(face['normal'][2]) - 1) <= tolerance
                    and abs(face['normal'][0]) <= tolerance
                    and abs(face['normal'][1]) <= tolerance
                    and abs(face['origin'][2] - station) <= tolerance]
        valid = [face for face in matching if len(face.get('loops', [])) >= 2
                 and all(loop.get('edge_count', 0) > 0 for loop in face['loops'])]
        end_loop_counts[label] = {'faces_at_station': len(matching),
                                  'annular_faces_with_multiple_closed_boundary_loops': len(valid)}
    checks.append({'check': 'Through-bore is open at both annular end faces',
                   'observed': end_loop_counts,
                   'expected': {'lower': 'at least one face with two or more closed loops',
                                'upper': 'at least one face with two or more closed loops'},
                   'method': 'native planar face boundary loops at both end stations',
                   'result': 'PASS' if all(value['annular_faces_with_multiple_closed_boundary_loops']
                                           >= 1 for value in end_loop_counts.values()) else 'FAIL'})
    checks.append(closed_body('One closed connected annular body', features))
    return {'result': 'PASS' if all(check['result'] == 'PASS' for check in checks) else 'FAIL',
            'method': 'native analytic cylinder axes/radii, planar end stations, boundary loops and closed-body topology',
            'numeric_tolerance_mm': tolerance,
            'source_measurements_mm': d,
            'local_frame': job['local_frame'],
            'representation': job['representation'],
            'scope': 'nominal annular solid; edge radii, chamfers, material and fit excluded',
            'checks': checks}


def verify_metadata(record, handle, job):
    """Compare the entity's stored identity, frame and scope strings."""
    p = parameters(job)
    return compare_source_metadata(record, handle, METADATA_APPLICATION, p['metadata'])


def inspect(client, handle, job):
    """Read one reopened Solid3D and require saved SAB geometry and metadata."""
    if not isinstance(handle, str) or not handle.strip():
        raise ValueError('Explicit native solid handle is required')
    document_id = getattr(client, 'document_id', None)
    if document_id is None:
        raise ValueError('Client must be bound to an explicit document_id')
    before = client.read('state')
    if before.get('document_id') != document_id:
        raise ValueError('Active document differs from the bound client document')
    geometry_revision, revision = before.get('geometry_revision'), before.get('revision')
    if geometry_revision is None or revision is None:
        raise ValueError('Active OCS state lacks document or geometry revision')
    response = client.read('records', collection='entities', handles=[handle], limit=1)
    records = response.get('records', [])
    if len(records) != 1 or records[0].get('handle') != handle:
        raise ValueError('Expected exactly one native record with the requested handle')
    record = records[0]
    for label, source in (('record response', response), ('record', record)):
        observed_document = source.get('document_id')
        if observed_document not in (None, document_id):
            raise ValueError(label + ' belongs to a different document')
        observed_geometry_revision = source.get('geometry_revision')
        if observed_geometry_revision not in (None, geometry_revision):
            raise ValueError(label + ' geometry_revision differs from active state')
    if record.get('type') != 'Solid3D':
        raise ValueError('Reopened annulus record must be Solid3D')
    if response.get('document_id') not in (None, document_id):
        raise ValueError('Native record response belongs to a different document')
    acis = record.get('properties', {}).get('acis_data', {})
    sab = acis.get('sab_data')
    if not sab:
        raise ValueError('Reopened annulus SAB geometry is required')
    from native_acis import sab_features
    features = sab_features(bytes(sab), include_loops=True)
    geometry_check = verify(features, job)
    metadata_check = verify_metadata(record, handle, job)
    after = client.read('state')
    if (after.get('document_id') != document_id
            or after.get('geometry_revision') != geometry_revision
            or after.get('revision') != revision):
        raise ValueError('Document identity or revision changed during annulus inspection')
    result = {'result': 'PASS' if geometry_check['result'] == 'PASS'
              and metadata_check['result'] == 'PASS' else 'FAIL',
              'document_id': document_id, 'document_revision': revision,
              'geometry_revision': geometry_revision, 'handle': handle,
              'geometry': geometry_check, 'metadata': metadata_check,
              'encoding': 'SAB native body graph with planar boundary loops',
              'features': features}
    return response, result, record
