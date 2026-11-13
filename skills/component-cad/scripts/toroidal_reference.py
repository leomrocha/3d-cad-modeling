"""Construct and inspect source-bound circular-section torus references.

All source dimensions, identity, metadata and local placement come from an
external job. The native construction route revolves a closed circular
section using the existing OCS Geometry adapter.
"""
import importlib
import math

from component_records import require_ready
from feature_checks import closed_body
from source_metadata import compare_source_metadata

METADATA_APPLICATION = 'CADTOOLS_SOURCE'


def _finite(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) \
            or not math.isfinite(value):
        raise ValueError(label + ' must be finite')
    return float(value)


def parameters(job):
    """Validate source bindings and derive the nominal torus radii."""
    require_ready(job)
    if job.get('units') != 'mm':
        raise ValueError('Toroidal reference helper supports millimetres only')
    if job.get('geometry_role') != 'reference_torus':
        raise ValueError('Explicit geometry_role=reference_torus is required')
    for key in ('job_id', 'part_id', 'part_name', 'representation',
                'geometry_name', 'frame', 'local_frame', 'metadata_request_label'):
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError('Explicit nonempty ' + key + ' is required')
    if job.get('metadata_application') != METADATA_APPLICATION:
        raise ValueError('Geometry.metadata uses the fixed CADTOOLS_SOURCE application')

    feature_names = job.get('dimension_features')
    if not isinstance(feature_names, dict) or set(feature_names) != {
            'inside_diameter', 'section_diameter'}:
        raise ValueError('dimension_features must bind inside_diameter and section_diameter')
    names = list(feature_names.values())
    if any(not isinstance(name, str) or not name.strip() for name in names) \
            or len(set(names)) != 2:
        raise ValueError('Two distinct readable source feature names are required')
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

    if job.get('axis') != [0, 0, 1]:
        raise ValueError('The supported local torus axis is explicitly +Z')
    center = job.get('center')
    if not isinstance(center, (list, tuple)) or len(center) != 3:
        raise ValueError('Explicit three-coordinate torus center is required')
    center = [_finite(value, 'center coordinate') for value in center]
    tolerance = _finite(job.get('readback_tolerance', 1e-7), 'readback_tolerance')
    if tolerance <= 0:
        raise ValueError('Positive readback_tolerance is required')

    inside = dimensions['inside_diameter']
    section = dimensions['section_diameter']
    minor_radius = section / 2
    major_radius = inside / 2 + minor_radius
    if (not math.isfinite(minor_radius) or minor_radius <= 0
            or not math.isfinite(major_radius) or major_radius <= minor_radius
            or major_radius - minor_radius <= tolerance
            or major_radius + minor_radius <= major_radius
            or major_radius - minor_radius >= major_radius):
        raise ValueError('Torus radii collapse or are not a finite ring-shaped section')

    # These four points and equal quarter-circle bulges form a true circle in
    # the revolve profile; no polygonal approximation of the section is used.
    profile = [[major_radius + minor_radius, 0.0],
               [major_radius, minor_radius],
               [major_radius - minor_radius, 0.0],
               [major_radius, -minor_radius]]
    for first, second in zip(profile, profile[1:] + profile[:1]):
        if first == second:
            raise ValueError('Toroidal profile vertices collapse numerically')
    bounds = [[center[0] - major_radius - minor_radius,
               center[0] + major_radius + minor_radius],
              [center[1] - major_radius - minor_radius,
               center[1] + major_radius + minor_radius],
              [center[2] - minor_radius, center[2] + minor_radius]]
    for i, (low, high) in enumerate(bounds):
        if not math.isfinite(low) or not math.isfinite(high) or low >= high:
            raise ValueError('Torus ' + 'XYZ'[i] + ' bounds collapse or overflow numerically')
        if low == center[i] or high == center[i]:
            raise ValueError('Torus ' + 'XYZ'[i] + ' bounds lose radius at the requested centre')

    metadata = job.get('metadata', [])
    if not isinstance(metadata, list) or any(
            not isinstance(value, str) or not value.strip() for value in metadata):
        raise ValueError('metadata must be a list of nonempty strings')
    source_lines = [job['part_id'], job['part_name'], job['representation'],
                    'Units: mm', 'Frame: ' + job['local_frame'],
                    'Source job: ' + job['job_id'],
                    'Nominal circular-section torus; no installed compression or groove represented']
    return {
        'dimensions': dimensions,
        'center': center,
        'axis': [0.0, 0.0, 1.0],
        'major_radius': major_radius,
        'minor_radius': minor_radius,
        'centerline_diameter': 2 * major_radius,
        'profile_points': profile,
        'quarter_arc_bulge': math.tan(math.pi / 8),
        'tolerance': tolerance,
        'metadata': source_lines + metadata,
    }


def geometry(client):
    """Create the existing guarded OCS Geometry adapter."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_torus(client, job):
    """Build one full torus by revolving an exact circular LWPOLYLINE profile."""
    p = parameters(job)
    g = geometry(client)
    bulges = {index: p['quarter_arc_bulge'] for index in range(4)}
    solid = g.revolve_z(job['geometry_name'] + ' circular section',
                        p['profile_points'], bulges=bulges)
    if p['center'] != [0.0, 0.0, 0.0]:
        g.move(job['geometry_name'] + ' local centre', [solid], p['center'])
    g.metadata(job['metadata_request_label'], [solid], p['metadata'])
    return solid


def verify(features, job):
    """Compare all observed torus surfaces and closed-body topology to the job."""
    p = parameters(job)
    rows = features.get('tori')
    if not isinstance(rows, list) or not rows:
        raise ValueError('Native analytic torus surface observations are required')
    tolerance = p['tolerance']
    unexpected = []
    matching = []
    for row in rows:
        center = row.get('center', [])
        axis = row.get('axis', [])
        if len(center) != 3 or len(axis) != 3:
            raise ValueError('Native torus center and axis need three coordinates')
        center = [_finite(value, 'native torus center') for value in center]
        axis = [_finite(value, 'native torus axis') for value in axis]
        major = _finite(row.get('major_radius'), 'native torus major radius')
        minor = _finite(row.get('minor_radius'), 'native torus minor radius')
        axis_ok = (abs(abs(axis[2]) - 1.0) <= tolerance
                   and abs(axis[0]) <= tolerance and abs(axis[1]) <= tolerance)
        radii_ok = (abs(major - p['major_radius']) <= tolerance
                    and abs(minor - p['minor_radius']) <= tolerance)
        center_ok = all(abs(a - b) <= tolerance for a, b in zip(center, p['center']))
        if center_ok and axis_ok and radii_ok:
            matching.append(row)
        else:
            unexpected.append({'center': center, 'axis': axis,
                               'major_radius': major, 'minor_radius': minor})

    expected_surface_names = {'tori'}
    extra_surfaces = {name: features.get(name, []) for name in
                      ('planes', 'cylinders', 'cones', 'spheres', 'ellipses')
                      if features.get(name)}
    topology = features.get('topology')
    if not isinstance(topology, dict):
        raise ValueError('Native closed-body topology observations are required')
    topology_check = closed_body('One closed connected toroidal body', features)
    checks = [
        {'check': 'Torus major/minor radii, centre and local +Z axis',
         'observed_matching_surfaces': len(matching),
         'observed_unexpected_surfaces': unexpected,
         'expected': {'center': p['center'], 'axis': p['axis'],
                      'major_radius_mm': p['major_radius'],
                      'minor_radius_mm': p['minor_radius']},
         'numeric_tolerance_mm': tolerance,
         'method': 'native analytic torus-surface records; all surface patches checked',
         'result': 'PASS' if len(matching) == len(rows) and not unexpected else 'FAIL'},
        {'check': 'Only toroidal analytic surfaces are present',
         'observed': extra_surfaces,
         'expected': {},
         'result': 'PASS' if not extra_surfaces else 'FAIL'},
        topology_check,
    ]
    return {
        'result': 'PASS' if all(check.get('result') == 'PASS' for check in checks) else 'FAIL',
        'method': 'native analytic torus radii/axis/centre and connected closed-body topology',
        'numeric_tolerance_mm': tolerance,
        'source_dimensions_mm': p['dimensions'],
        'derived_major_radius_mm': p['major_radius'],
        'derived_minor_radius_mm': p['minor_radius'],
        'local_frame': job['local_frame'],
        'representation': job['representation'],
        'scope': 'nominal torus; compound, tolerances, installation compression and groove excluded',
        'checks': checks,
    }


def verify_metadata(record, handle, job):
    """Compare source identity, frame and scope strings on the native record."""
    p = parameters(job)
    return compare_source_metadata(record, handle, METADATA_APPLICATION, p['metadata'])


def inspect(client, handle, job):
    """Inspect one reopened Solid3D against source metadata and analytic SAB surfaces."""
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
        raise ValueError('Reopened torus record must be Solid3D')
    if response.get('document_id') not in (None, document_id):
        raise ValueError('Native record response belongs to a different document')
    sab = record.get('properties', {}).get('acis_data', {}).get('sab_data')
    if not sab:
        raise ValueError('Reopened torus SAB geometry is required')
    from native_acis import sab_features
    # Root owns the generic SAB reader extension for analytic torus surfaces.
    features = sab_features(bytes(sab), include_loops=False, allow_tori=True)
    geometry_check = verify(features, job)
    metadata_check = verify_metadata(record, handle, job)
    after = client.read('state')
    if (after.get('document_id') != document_id
            or after.get('geometry_revision') != geometry_revision
            or after.get('revision') != revision):
        raise ValueError('Document identity or revision changed during torus inspection')
    result = {'result': 'PASS' if geometry_check['result'] == 'PASS'
              and metadata_check['result'] == 'PASS' else 'FAIL',
              'document_id': document_id, 'document_revision': revision,
              'geometry_revision': geometry_revision, 'handle': handle,
              'geometry': geometry_check, 'metadata': metadata_check,
              'encoding': 'SAB native body graph with analytic torus surface records',
              'features': features}
    return response, result, record
