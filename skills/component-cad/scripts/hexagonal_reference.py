"""Construct and verify a source-bound regular hexagonal prism reference.

Inputs, source limits, placement frame and metadata come from an external
component job. The optional bore is a geometric through-bore only when the
caller supplies a pinned diameter feature. Thread designations alone remain
axis metadata and do not select a bore diameter.
"""

import importlib
import math

from component_records import require_ready
from feature_checks import closed_body, comparison
from source_metadata import compare_source_metadata

METADATA_APPLICATION = 'CADTOOLS_SOURCE'


def _finite(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name + ' must be a finite number')
    try:
        value = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(name + ' must be a finite number') from error
    if not math.isfinite(value):
        raise ValueError(name + ' must be a finite number')
    return value


def _vector(value, name):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(name + ' must contain three finite coordinates')
    return [_finite(x, name) for x in value]


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def _norm(value):
    return math.sqrt(_dot(value, value))


def _unit(value, name):
    vector = _vector(value, name)
    length = _norm(vector)
    if not math.isfinite(length) or abs(length - 1.0) > 1e-9:
        raise ValueError(name + ' must be a unit vector')
    return vector


def regular_hexagon_points(across_flats_mm, center=(0.0, 0.0), rotation_degrees=0.0):
    """Return six XY vertices for a regular hexagon with the supplied AF."""
    across_flats = _finite(across_flats_mm, 'across_flats_mm')
    if across_flats <= 0:
        raise ValueError('across_flats_mm must be positive')
    if not isinstance(center, (list, tuple)) or len(center) != 2:
        raise ValueError('center must contain two finite coordinates')
    cx, cy = (_finite(value, 'center') for value in center)
    angle = math.radians(_finite(rotation_degrees, 'rotation_degrees'))
    radius = across_flats / math.sqrt(3.0)
    if not math.isfinite(radius) or radius <= 0:
        raise ValueError('across_flats_mm collapses or overflows the vertex radius')
    points = [[cx + radius * math.cos(angle + math.tau * i / 6.0),
               cy + radius * math.sin(angle + math.tau * i / 6.0)]
              for i in range(6)]
    if any(not math.isfinite(value) for point in points for value in point):
        raise ValueError('Hexagon coordinates overflow')
    if len({tuple(point) for point in points}) != 6:
        raise ValueError('Hexagon vertices collapse at the supplied centre and scale')
    return points


def _dimension(job, feature_name, label):
    by_name = {feature['name']: feature for feature in job['features']}
    feature = by_name.get(feature_name)
    if feature is None or feature.get('required') is not True:
        raise ValueError(label + ' must bind one required source feature')
    if feature.get('unit') != 'mm':
        raise ValueError(label + ' source feature must use mm')
    value = _finite(feature.get('value'), label)
    if value <= 0:
        raise ValueError(label + ' must be positive')
    return value, feature


def _metadata(job, p):
    lines = [job['part_id'], job['part_name'], job['representation'],
             'Geometry role: source-bound regular hexagonal prism reference',
             'Units: mm', 'Source job: ' + job['job_id'],
             'Frame: origin is the lower axial face centre; axis is + local Z',
             'Across-flats source value: %.12g mm (%s)' %
             (p['across_flats_mm'], p['across_flats_feature']),
             'Axial height source value: %.12g mm (%s)' %
             (p['height_mm'], p['height_feature'])]
    if p['bore_diameter_mm'] is not None:
        lines.append('Through-bore source value: %.12g mm (%s)' %
                     (p['bore_diameter_mm'], p['bore_feature']))
    else:
        lines.append('No bore solid represented; source thread/axis information remains metadata')
    lines.extend(job.get('metadata', []))
    for source in job.get('source_files', []):
        lines.append('Source: %s SHA-256 %s' %
                     (source['locator'], source['sha256']))
    return lines


def parameters(job):
    """Validate source readiness, dimensions, metadata and arbitrary frame."""
    ready = require_ready(job)
    for key in ('job_id', 'part_id', 'part_name', 'representation',
                'geometry_name', 'metadata_request_label', 'frame',
                'local_frame', 'geometry_role', 'units'):
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError(key + ' must be a nonempty string')
    if job['units'] != 'mm':
        raise ValueError('Hexagonal reference supports millimetres only')
    if job['geometry_role'] != 'reference_hexagonal_prism':
        raise ValueError('Explicit geometry_role=reference_hexagonal_prism is required')
    if job.get('metadata_application') != METADATA_APPLICATION:
        raise ValueError('Geometry.metadata uses the fixed CADTOOLS_SOURCE application')
    dimension_features = job.get('dimension_features')
    if not isinstance(dimension_features, dict) or set(dimension_features) not in (
            {'across_flats', 'height'}, {'across_flats', 'height', 'bore_diameter'}):
        raise ValueError('dimension_features must bind AF and height, with optional bore diameter')
    if any(not isinstance(value, str) or not value.strip()
           for value in dimension_features.values()):
        raise ValueError('dimension feature names must be nonempty strings')
    if len(set(dimension_features.values())) != len(dimension_features):
        raise ValueError('Each geometric dimension must bind a distinct source feature')
    af_name, height_name = dimension_features['across_flats'], dimension_features['height']
    af, af_feature = _dimension(job, af_name, 'across_flats_mm')
    height, height_feature = _dimension(job, height_name, 'height_mm')
    bore = None
    bore_feature = None
    bore_name = dimension_features.get('bore_diameter')
    construction = job.get('construction', {})
    if bore_name is not None:
        bore, bore_feature = _dimension(job, bore_name, 'bore_diameter_mm')
        if bore >= af:
            raise ValueError('bore_diameter_mm must be less than across_flats_mm')
        bore_radius = bore / 2.0
        if not math.isfinite(bore_radius) or bore_radius <= 0:
            raise ValueError('bore diameter collapses or overflows its constructed radius')
        overrun = _finite(construction.get('cutter_overrun_mm'), 'cutter_overrun_mm')
        if overrun <= 0:
            raise ValueError('cutter_overrun_mm must be positive when a bore is constructed')
        cutter_height = height + 2.0 * overrun
        if not math.isfinite(cutter_height) or cutter_height <= height:
            raise ValueError('bore cutter height overflows or loses its end overrun')
    else:
        if 'cutter_overrun_mm' in construction:
            raise ValueError('cutter overrun is valid only when a bore is constructed')
        overrun = None
        bore_radius = None
    frame = job.get('placement')
    if not isinstance(frame, dict) or set(frame) != {'origin', 'axis', 'radial_x'}:
        raise ValueError('placement must provide exactly origin, axis and radial_x')
    origin = _vector(frame['origin'], 'placement.origin')
    axis = _unit(frame['axis'], 'placement.axis')
    radial_x = _unit(frame['radial_x'], 'placement.radial_x')
    if abs(_dot(axis, radial_x)) > 1e-9:
        raise ValueError('placement.radial_x must be perpendicular to placement.axis')
    radial_y = _cross(axis, radial_x)
    if abs(_norm(radial_y) - 1.0) > 1e-9:
        raise ValueError('placement frame must be right-handed and orthonormal')
    end = [origin[i] + height * axis[i] for i in range(3)]
    if any(not math.isfinite(value) for value in end) or end == origin:
        raise ValueError('placement origin plus height collapses or overflows')
    points = regular_hexagon_points(af)
    world_points = [[origin[i] + point[0] * radial_x[i] + point[1] * radial_y[i]
                     for i in range(3)] for point in points]
    if any(not math.isfinite(value) for point in world_points for value in point):
        raise ValueError('placed hexagonal vertices overflow')
    if len({tuple(point) for point in world_points}) != 6:
        raise ValueError('placed hexagonal vertices collapse at the supplied origin and scale')
    # Existing OCS rotate supports cardinal-axis rotations; compose Z-Y-Z to
    # orient the local prism axis and its in-plane radial X direction.
    phi = math.atan2(axis[1], axis[0]) if abs(axis[0]) + abs(axis[1]) > 1e-15 else 0.0
    theta = math.acos(max(-1.0, min(1.0, axis[2])))
    intermediate_x = [math.cos(phi) * math.cos(theta),
                      math.sin(phi) * math.cos(theta), -math.sin(theta)]
    intermediate_y = [-math.sin(phi), math.cos(phi), 0.0]
    gamma = math.atan2(_dot(radial_x, intermediate_y),
                       _dot(radial_x, intermediate_x))
    tolerance = _finite(job.get('readback_tolerance_mm', 1e-7), 'readback_tolerance_mm')
    if tolerance <= 0:
        raise ValueError('readback_tolerance_mm must be positive')
    source_files = job.get('source_files')
    if not isinstance(source_files, list) or not source_files:
        raise ValueError('source_files must contain at least one pinned source')
    pinned = {(row['path'], row['sha256']) for row in ready['source_observations']}
    for index, source in enumerate(source_files):
        if not isinstance(source, dict) or not all(
                isinstance(source.get(k), str) and source[k].strip()
                for k in ('path', 'sha256', 'locator')):
            raise ValueError('source_files[%d] needs runtime path, portable locator and sha256' % index)
        if (source['path'], source['sha256']) not in pinned:
            raise ValueError('source_files[%d] must be pinned by a required dimension feature' % index)
    metadata = job.get('metadata', [])
    if not isinstance(metadata, list) or any(not isinstance(x, str) or not x.strip()
                                             for x in metadata):
        raise ValueError('metadata must be a list of nonempty strings')
    p = {'across_flats_mm': af, 'height_mm': height,
         'across_flats_feature': af_name, 'height_feature': height_name,
         'bore_diameter_mm': bore, 'bore_feature': bore_name,
         'bore_radius_mm': bore_radius,
         'cutter_overrun_mm': overrun, 'origin': origin, 'axis': axis,
         'radial_x': radial_x, 'radial_y': radial_y, 'end': end,
         'profile_points': points, 'world_points': world_points,
         'rotation_degrees': {'Z_initial': math.degrees(gamma),
                              'Y_axis_tilt': math.degrees(theta),
                              'Z_axis_azimuth': math.degrees(phi)},
         'tolerance': tolerance, 'metadata': None}
    p['metadata'] = _metadata(job, p)
    return p


def geometry(client):
    """Use the installed guarded Geometry adapter."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_hexagonal_reference(client, job):
    """Build one oriented hexagonal prism, with an optional sourced bore."""
    p = parameters(job)
    g = geometry(client)
    prism = g.extrude(job['geometry_name'] + ' hexagonal prism', p['profile_points'],
                      0.0, p['height_mm'])
    solid = prism
    if p['bore_diameter_mm'] is not None:
        overrun = p['cutter_overrun_mm']
        cutter = g.cylinder(job['geometry_name'] + ' through-bore cutter',
                            [0.0, 0.0, -overrun], p['bore_radius_mm'],
                            p['height_mm'] + 2.0 * overrun)
        solid = g.subtract(job['geometry_name'] + ' bored hexagonal solid', prism, [cutter])
    rotations = p['rotation_degrees']
    for axis_name in ('Z_initial', 'Y_axis_tilt', 'Z_axis_azimuth'):
        degrees = rotations[axis_name]
        if abs(degrees) > 1e-12:
            axis = axis_name[0]
            g.rotate(job['geometry_name'] + ' orient ' + axis_name, [solid], axis, degrees)
    if any(abs(value) > 0 for value in p['origin']):
        g.move(job['geometry_name'] + ' place origin', [solid], p['origin'])
    g.metadata(job['metadata_request_label'], [solid], p['metadata'])
    return solid


def verify(features, job):
    """Check six AF planes, both axial stations, optional bore and topology."""
    p = parameters(job)
    tol, af = p['tolerance'], p['across_flats_mm']
    axis, origin = p['axis'], p['origin']
    planes = features.get('planes')
    if not isinstance(planes, list):
        raise ValueError('Native planar surface inventory is required')

    # Deduplicate coplanar patches by their local unit normal and signed offset.
    unique_planes = []
    for plane in planes:
        normal = _unit(plane.get('normal'), 'native plane normal')
        plane_origin = _vector(plane.get('origin'), 'native plane origin')
        local_normal = [_dot(normal, p['radial_x']), _dot(normal, p['radial_y']),
                        _dot(normal, axis)]
        offset = _dot([plane_origin[i] - origin[i] for i in range(3)], normal)
        first = next((value for value in local_normal if abs(value) > tol), 1.0)
        if first < 0:
            local_normal = [-value for value in local_normal]
            offset = -offset
        if not any(_norm([local_normal[i] - old['normal'][i] for i in range(3)]) <= tol
                   and abs(offset - old['offset']) <= tol for old in unique_planes):
            unique_planes.append({'normal': local_normal, 'offset': offset})

    expected_planes = []
    points = p['profile_points']
    for index, a in enumerate(points):
        b = points[(index + 1) % 6]
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = math.hypot(dx, dy)
        local_normal = [dy / length, -dx / length, 0.0]
        offset = _dot(local_normal, [(a[0] + b[0]) / 2.0,
                                     (a[1] + b[1]) / 2.0])
        first = next(value for value in local_normal if abs(value) > tol)
        if first < 0:
            local_normal = [-value for value in local_normal]
            offset = -offset
        expected_planes.append({'normal': local_normal, 'offset': offset})
    expected_planes += [{'normal': [0.0, 0.0, 1.0], 'offset': 0.0},
                        {'normal': [0.0, 0.0, 1.0], 'offset': p['height_mm']}]
    unmatched = list(unique_planes)
    plane_matches = []
    for expected in expected_planes:
        hit = next((i for i, observed in enumerate(unmatched)
                    if _norm([observed['normal'][k] - expected['normal'][k]
                              for k in range(3)]) <= tol
                    and abs(observed['offset'] - expected['offset']) <= tol), None)
        plane_matches.append(hit is not None)
        if hit is not None:
            unmatched.pop(hit)
    plane_check = {'check': 'All unique planar surfaces match six side planes and two axial caps',
                   'observed_unique_plane_count': len(unique_planes),
                   'expected_unique_plane_count': 8,
                   'expected_surface_matches': plane_matches,
                   'unexpected_unique_planes': unmatched,
                   'method': 'native analytic plane equations; coincident patches deduplicated in the supplied component frame',
                   'result': 'PASS' if all(plane_matches) and not unmatched
                   and len(unique_planes) == len(expected_planes) else 'FAIL'}
    side_check = {'check': 'Six regular-hex side planes at source AF/2',
                  'source_across_flats_mm': af,
                  'observed_side_offsets_mm': sorted(
                      item['offset'] for item in unique_planes
                      if abs(item['normal'][2]) <= tol),
                  'expected_side_plane_count': 6,
                  'method': 'all deduplicated native side-plane equations against six source-profile edge planes',
                  'result': 'PASS' if all(plane_matches[:6]) else 'FAIL'}
    cap_planes = [item for item in unique_planes
                  if abs(item['normal'][0]) <= tol and abs(item['normal'][1]) <= tol]
    stations = sorted(item['offset'] for item in cap_planes)
    axial_check = comparison('Lower and upper axial face stations', stations,
                             [0.0, p['height_mm']], tol,
                             method='all deduplicated native cap planes projected onto supplied axis')
    checks = [side_check, plane_check, axial_check]

    cylinders = features.get('cylinders', [])
    if not isinstance(cylinders, list):
        raise ValueError('Native analytic cylinder inventory must be a list')
    unique_cylinders = []
    for cylinder in cylinders:
        cyl_axis = _unit(cylinder.get('axis'), 'native cylinder axis')
        cyl_origin = _vector(cylinder.get('origin'), 'native cylinder origin')
        radius = _finite(cylinder.get('radius'), 'native cylinder radius')
        if radius <= 0:
            raise ValueError('Native cylinder radius must be positive')
        if _dot(cyl_axis, axis) < 0:
            cyl_axis = [-value for value in cyl_axis]
        displacement = [cyl_origin[i] - origin[i] for i in range(3)]
        center_offset = [_dot(displacement, p['radial_x']),
                         _dot(displacement, p['radial_y'])]
        candidate = {'axis': cyl_axis, 'center_offset': center_offset,
                     'radius': radius}
        if not any(_norm([candidate['axis'][i] - old['axis'][i] for i in range(3)]) <= tol
                   and _norm([candidate['center_offset'][i] - old['center_offset'][i]
                              for i in range(2)]) <= tol
                   and abs(candidate['radius'] - old['radius']) <= tol
                   for old in unique_cylinders):
            unique_cylinders.append(candidate)
    expected_cylinders = [] if p['bore_diameter_mm'] is None else [
        {'axis': axis, 'center_offset': [0.0, 0.0], 'radius': p['bore_radius_mm']}]
    cylinder_matches = []
    unmatched_cylinders = list(unique_cylinders)
    for expected in expected_cylinders:
        hit = next((i for i, observed in enumerate(unmatched_cylinders)
                    if _norm([observed['axis'][k] - expected['axis'][k]
                              for k in range(3)]) <= tol
                    and _norm([observed['center_offset'][k] - expected['center_offset'][k]
                               for k in range(2)]) <= tol
                    and abs(observed['radius'] - expected['radius']) <= tol), None)
        cylinder_matches.append(hit is not None)
        if hit is not None:
            unmatched_cylinders.pop(hit)
    cylinder_check = {'check': 'All unique cylinders match the optional sourced coaxial bore',
                      'observed_unique_cylinder_count': len(unique_cylinders),
                      'expected_unique_cylinder_count': len(expected_cylinders),
                      'expected_surface_matches': cylinder_matches,
                      'unexpected_unique_cylinders': unmatched_cylinders,
                      'method': 'native analytic cylinder axes, centreline offsets and radii; coincident patches deduplicated',
                      'result': 'PASS' if all(cylinder_matches) and not unmatched_cylinders
                      and len(unique_cylinders) == len(expected_cylinders) else 'FAIL'}
    checks.append(cylinder_check)
    other_surfaces = {name: features.get(name, []) for name in ('cones', 'spheres')
                      if features.get(name)}
    checks.append({'check': 'No additional conical or spherical surfaces',
                   'observed': other_surfaces, 'expected': {},
                   'method': 'native analytic surface inventory',
                   'result': 'PASS' if not other_surfaces else 'FAIL'})

    if p['bore_diameter_mm'] is not None:
        loop_faces = features.get('planar_face_loops')
        if not isinstance(loop_faces, list):
            raise ValueError('SAB planar-face loops are required for a through-bore check')
        loop_observations = {}
        for station_name, station in (('lower', 0.0), ('upper', p['height_mm'])):
            matches = []
            for face in loop_faces:
                normal = face.get('normal', [])
                face_origin = face.get('origin', [])
                if len(normal) != 3 or len(face_origin) != 3:
                    raise ValueError('SAB planar-face loop records need a normal and origin')
                if abs(abs(_dot(normal, axis)) - 1.0) <= tol \
                        and abs(_dot([face_origin[i] - origin[i] for i in range(3)], axis)
                                - station) <= tol:
                    loops = face.get('loops')
                    if not isinstance(loops, list) or any(
                            not isinstance(loop.get('edge_count'), int)
                            or loop['edge_count'] <= 0 for loop in loops):
                        raise ValueError('SAB cap boundary loops must contain closed edge cycles')
                    matches.append(len(loops))
            loop_observations[station_name] = matches
        loops_pass = all(any(count >= 2 for count in loop_observations[name])
                         for name in ('lower', 'upper'))
        checks.append({'check': 'Through-bore has an inner boundary loop at both cap stations',
                       'observed_boundary_loop_counts_by_face': loop_observations,
                       'expected': 'at least one cap face with two or more loops at each end',
                       'method': 'SAB include_loops planar face boundary cycles at lower and upper stations',
                       'result': 'PASS' if loops_pass else 'FAIL'})
    checks.append(closed_body('One closed connected hexagonal body', features))
    return {'result': 'PASS' if all(check['result'] == 'PASS' for check in checks) else 'FAIL',
            'method': 'native plane equations, axial stations, optional analytic bore and closed-body topology',
            'numeric_tolerance_mm': tol,
            'source_measurements_mm': {'across_flats': af, 'height': p['height_mm'],
                                       'bore_diameter': p['bore_diameter_mm']},
            'frame': {'origin': origin, 'axis': axis, 'radial_x': p['radial_x']},
            'checks': checks}


def inspect(client, handles, job):
    """Read the native SAB and source metadata for one constructed solid."""
    if set(handles) != {'body'}:
        raise ValueError("Hexagonal reference inspection needs a 'body' handle")
    expected_document = getattr(client, 'document_id', None)
    if expected_document is None:
        raise ValueError('Client must be bound to an explicit document_id')
    before = client.read('state')
    if before.get('document_id') != expected_document:
        raise ValueError('Active document differs from the bound Client document')
    before_revision = before.get('revision')
    before_geometry_revision = before.get('geometry_revision')
    if before_revision is None or before_geometry_revision is None:
        raise ValueError('Active state must include document and geometry revisions')
    records = client.read('records', collection='entities', handles=[handles['body']], limit=1)
    if records.get('document_id') != expected_document:
        raise ValueError('Native record response belongs to a different document')
    if records.get('revision') != before_revision \
            or records.get('geometry_revision') != before_geometry_revision:
        raise ValueError('Native record response differs from the active document geometry epoch')
    rows = records.get('records', [])
    if len(rows) != 1 or rows[0].get('handle') != handles['body'] \
            or rows[0].get('type') != 'Solid3D':
        raise ValueError('Expected one Solid3D record for the requested body handle')
    acis = rows[0]['properties']['acis_data']
    sab = acis.get('sab_data')
    if not sab:
        raise ValueError('Hexagonal reference inspection requires saved/native SAB body data')
    from native_acis import sab_features
    features = sab_features(bytes(sab), allow_rigid=True, include_loops=True)
    check = verify(features, job)
    metadata = compare_source_metadata(rows[0], handles['body'], METADATA_APPLICATION,
                                       parameters(job)['metadata'])
    after = client.read('state')
    if after.get('document_id') != expected_document:
        raise ValueError('Active document changed during hexagonal reference inspection')
    if after.get('revision') != before_revision \
            or after.get('geometry_revision') != before_geometry_revision:
        raise ValueError('Document or geometry revision changed during hexagonal reference inspection')
    result = {'result': 'PASS' if check['result'] == metadata['result'] == 'PASS' else 'FAIL',
              'document_id': expected_document,
              'revision': after['revision'],
              'geometry_revision': after['geometry_revision'],
              'handle': handles['body'], 'geometry': check,
              'source_metadata': metadata, 'features': features}
    return records, result


def verify_metadata(record, handle, job):
    """Compare source identity and dimension-limit strings on the native body."""
    return compare_source_metadata(record, handle, METADATA_APPLICATION,
                                   parameters(job)['metadata'])
