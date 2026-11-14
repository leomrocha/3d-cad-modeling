"""Parameterized nominal regular-hex-head and axial-shaft screw reference.

The caller supplies all dimensions, source locators, metadata and frame. This
module constructs no thread helix, chamfer, bevel, fillet or component-specific
geometry. It is an offline draft; it performs no OCS session discovery.
"""
import copy
import math
from pathlib import Path
import re

from component_records import require_ready
from hexagonal_reference import parameters as hex_parameters
from hexagonal_reference import build_hexagonal_reference
from source_metadata import compare_source_metadata

METADATA_APPLICATION = 'CADTOOLS_SOURCE'
GEOMETRY_ROLE = 'reference_hex_head_axial_shaft'


def _finite(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(label + ' must be a finite number')
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(label + ' must be a finite number') from error
    if not math.isfinite(result):
        raise ValueError(label + ' must be a finite number')
    return result


def _vec(value, label):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError(label + ' must contain three finite values')
    return [_finite(item, label) for item in value]


def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def _cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def _norm(v):
    return math.sqrt(_dot(v, v))


def _unit(v, label):
    result = _vec(v, label)
    length = _norm(result)
    if not math.isfinite(length) or abs(length - 1.0) > 1e-9:
        raise ValueError(label + ' must be a unit vector')
    return result


def _resolve(locator, roots):
    if not isinstance(locator, str):
        raise ValueError('Source locator must be text')
    match = re.fullmatch(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}/(.+)', locator)
    if match:
        name, suffix = match.groups()
        if name not in roots:
            raise ValueError('Missing caller-supplied source root: ' + name)
        root = Path(roots[name])
        if not root.is_absolute():
            raise ValueError('Configured source root must be absolute: ' + name)
        path = (root / suffix).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError as error:
            raise ValueError('Source locator escapes its configured root') from error
        return path
    path = Path(locator)
    if not path.is_absolute():
        raise ValueError('Source path must be absolute or use a named root')
    return path.resolve()


def _runtime_job(job, roots):
    result = copy.deepcopy(job)
    for feature in result.get('features', []):
        if isinstance(feature, dict) and isinstance(feature.get('source'), str):
            feature['source'] = str(_resolve(feature['source'], roots))
    for source in result.get('source_files', []):
        if isinstance(source, dict) and isinstance(source.get('path'), str):
            source['path'] = str(_resolve(source['path'], roots))
    return result


def parameters(job, root_map=None):
    """Validate readiness, source-pinned dimensions, frame and construction envelope."""
    roots = root_map or {}
    runtime = _runtime_job(job, roots)
    ready = require_ready(runtime)
    required = ('job_id', 'part_id', 'part_name', 'representation', 'geometry_name',
                'metadata_request_label', 'frame', 'local_frame', 'geometry_role', 'units')
    for key in required:
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError(key + ' must be a nonempty string')
    if job['geometry_role'] != GEOMETRY_ROLE or job['units'] != 'mm':
        raise ValueError('Explicit nominal screw-reference role and mm units are required')
    if job.get('metadata_application') != METADATA_APPLICATION:
        raise ValueError('Geometry metadata application must be CADTOOLS_SOURCE')
    mapping = job.get('dimension_features')
    names = {'head_across_flats', 'head_height', 'shaft_diameter', 'under_head_length'}
    if not isinstance(mapping, dict) or set(mapping) != names:
        raise ValueError('dimension_features must bind AF, head height, shaft diameter and under-head length')
    if any(not isinstance(value, str) or not value.strip() for value in mapping.values()) \
            or len(set(mapping.values())) != 4:
        raise ValueError('Each dimension must bind a distinct readable source feature')
    features = {f.get('name'): f for f in runtime['features']}
    values, source_features = {}, {}
    for key, feature_name in mapping.items():
        feature = features.get(feature_name)
        if feature is None or feature.get('required') is not True or feature.get('unit') != 'mm':
            raise ValueError(key + ' must bind a required source-pinned mm feature')
        value = _finite(feature.get('value'), key)
        if value <= 0:
            raise ValueError(key + ' must be positive')
        values[key] = value
        source_features[key] = feature
    af = values['head_across_flats']
    head_height = values['head_height']
    shaft_diameter = values['shaft_diameter']
    length = values['under_head_length']
    shaft_radius = shaft_diameter / 2.0
    if not math.isfinite(shaft_radius) or shaft_radius <= 0 or shaft_radius >= af / 2.0:
        raise ValueError('Shaft radius must remain positive and inside the hex head inradius')
    # Force all constructed dimensions to retain distinct representable stations.
    if not math.isfinite(head_height + length) or head_height + length <= head_height:
        raise ValueError('Head and shaft axial extent overflows or collapses')
    tol = _finite(job.get('readback_tolerance_mm', 1e-7), 'readback_tolerance_mm')
    if tol <= 0:
        raise ValueError('readback_tolerance_mm must be positive')

    placement = job.get('placement')
    if not isinstance(placement, dict) or set(placement) != {'under_head_origin', 'axis', 'radial_x'}:
        raise ValueError('placement must bind under_head_origin, axis and radial_x')
    origin = _vec(placement['under_head_origin'], 'under_head_origin')
    axis = _unit(placement['axis'], 'axis')
    radial_x = _unit(placement['radial_x'], 'radial_x')
    if abs(_dot(axis, radial_x)) > 1e-9:
        raise ValueError('radial_x must be perpendicular to axis')
    radial_y = _cross(axis, radial_x)
    if abs(_norm(radial_y) - 1.0) > 1e-9:
        raise ValueError('placement must be right-handed and orthonormal')
    tip = [origin[i] + length * axis[i] for i in range(3)]
    head_base = [origin[i] - head_height * axis[i] for i in range(3)]
    if any(not math.isfinite(x) for x in tip + head_base) or tip == origin or head_base == origin:
        raise ValueError('Axial stations overflow or collapse')
    rotations = _rotation_sequence(axis, radial_x)
    source_files = job.get('source_files')
    if not isinstance(source_files, list) or not source_files:
        raise ValueError('source_files must contain pinned source records')
    pinned = {(x['path'], x['sha256']) for x in ready['source_observations']}
    for i, source in enumerate(source_files):
        if not isinstance(source, dict) or not all(
                isinstance(source.get(k), str) and source[k].strip()
                for k in ('path', 'sha256', 'locator')):
            raise ValueError('source_files[%d] needs runtime path, sha256 and portable locator' % i)
        resolved_path = str(_resolve(source['path'], roots))
        if (resolved_path, source['sha256']) not in pinned:
            raise ValueError('source_files[%d] is not pinned by a required source feature' % i)
    metadata = job.get('metadata')
    if not isinstance(metadata, list) or any(not isinstance(x, str) or not x.strip() for x in metadata):
        raise ValueError('metadata must be a list of nonempty strings')
    p = {'values': values, 'features': source_features, 'origin': origin,
         'axis': axis, 'radial_x': radial_x, 'radial_y': radial_y,
         'head_base': head_base, 'tip': tip, 'shaft_radius': shaft_radius,
         'rotation_degrees': rotations, 'tolerance': tol, 'source_files': source_files}
    p['metadata_lines'] = _metadata_lines(job, p)

    # Validate the exact head-builder subjob now, before the caller creates Geometry.
    p['head_job'] = _head_job(job, runtime, p)
    hex_parameters(p['head_job'])
    return p


def _rotation_sequence(axis, radial_x):
    phi = math.atan2(axis[1], axis[0]) if abs(axis[0]) + abs(axis[1]) > 1e-15 else 0.0
    theta = math.acos(max(-1.0, min(1.0, axis[2])))
    ix = [math.cos(phi)*math.cos(theta), math.sin(phi)*math.cos(theta), -math.sin(theta)]
    iy = [-math.sin(phi), math.cos(phi), 0.0]
    gamma = math.atan2(_dot(radial_x, iy), _dot(radial_x, ix))
    return {'Z_initial': math.degrees(gamma), 'Y_axis_tilt': math.degrees(theta),
            'Z_axis_azimuth': math.degrees(phi)}


def _head_job(job, runtime, p):
    out = copy.deepcopy(runtime)
    out.update({'geometry_role': 'reference_hexagonal_prism',
                'geometry_name': job['geometry_name'] + ' head',
                'metadata_request_label': job['metadata_request_label'] + '-head',
                'metadata_application': METADATA_APPLICATION,
                'dimension_features': {'across_flats': job['dimension_features']['head_across_flats'],
                                       'height': job['dimension_features']['head_height']},
                'placement': {'origin': p['head_base'], 'axis': p['axis'], 'radial_x': p['radial_x']},
                'source_files': [{'path':s['path'], 'locator':original['locator'],
                                 'sha256':s['sha256']}
                                for s, original in zip(runtime['source_files'], job['source_files'])],
                'metadata': ['Head is the regular-hex nominal reference prism; no bevel or fillet is represented.']})
    # Make feature source paths match the runtime source rows used by source readiness.
    out['features'] = runtime['features']
    return out


def _metadata_lines(job, p):
    v = p['values']
    lines = [job['part_id'], job['part_name'], job['representation'],
             'Geometry role: nominal regular hexagonal head joined to a cylindrical shaft reference',
             'Units: mm', 'Source job: ' + job['job_id'], 'World frame: ' + job['frame'],
             'Local frame: ' + job['local_frame'],
             'Head across flats: %.12g mm; source feature %s' %
             (v['head_across_flats'], job['dimension_features']['head_across_flats']),
             'Head height: %.12g mm; source feature %s' %
             (v['head_height'], job['dimension_features']['head_height']),
             'Nominal shaft diameter: %.12g mm; source feature %s' %
             (v['shaft_diameter'], job['dimension_features']['shaft_diameter']),
             'Under-head length: %.12g mm; source feature %s' %
             (v['under_head_length'], job['dimension_features']['under_head_length']),
             'Shaft is a nominal thread-envelope cylinder; no helical thread is represented.',
             'Head flats orientation is a construction convention; no seller orientation is claimed.']
    lines.extend(job['metadata'])
    lines.extend('Source: %s SHA-256 %s' % (s['locator'], s['sha256']) for s in p['source_files'])
    return lines


def geometry(client):
    from rounded_tube import SelectionCheckedClient
    from cadtools.geometry import Geometry
    return Geometry(SelectionCheckedClient(client))


def build_hex_screw_reference(client, job, root_map=None):
    """Construct one head, one cylinder, one union; call only after native grant."""
    p = parameters(job, root_map)
    head = build_hexagonal_reference(client, p['head_job'])
    g = geometry(client)
    shaft = g.cylinder(job['geometry_name'] + ' nominal shaft', [0.0, 0.0, 0.0],
                       p['shaft_radius'], p['values']['under_head_length'])
    for axis_name in ('Z_initial', 'Y_axis_tilt', 'Z_axis_azimuth'):
        degrees = p['rotation_degrees'][axis_name]
        if abs(degrees) > 1e-12:
            g.rotate(job['geometry_name'] + ' shaft orient ' + axis_name, [shaft],
                     axis_name[0], degrees)
    if any(abs(x) > 0 for x in p['origin']):
        g.move(job['geometry_name'] + ' shaft place under-head datum', [shaft], p['origin'])
    body = g.combine(job['geometry_name'] + ' joined head and shaft', [head, shaft])
    g.metadata(job['metadata_request_label'], [body], p['metadata_lines'])
    return {'body': body}, p


def _plane_signature(plane):
    normal = _unit(plane.get('normal'), 'plane normal')
    origin = _vec(plane.get('origin'), 'plane origin')
    return normal, origin


def _plane_match(actual, expected, tol):
    an, ao = actual
    en, eo = expected
    dot = _dot(an, en)
    return abs(abs(dot)-1.0) <= tol and abs(_dot(ao, en)-_dot(eo, en)) <= tol


def verify(features, job, root_map=None):
    """Verify unique analytic surface identities, axial planes and closure."""
    p = parameters(job, root_map)
    tol = p['tolerance']
    # Hex helper's profile orientation: regular_hexagon_points(AF) in local XY.
    af = p['values']['head_across_flats']
    radius = af / math.sqrt(3.0)
    points = [[radius*math.cos(math.tau*i/6.0), radius*math.sin(math.tau*i/6.0)]
              for i in range(6)]
    expected_planes = []
    for i, a in enumerate(points):
        b = points[(i+1) % 6]
        dx, dy = b[0]-a[0], b[1]-a[1]
        nlocal = [dy/math.hypot(dx,dy), -dx/math.hypot(dx,dy), 0.0]
        normal = [nlocal[0]*p['radial_x'][j] + nlocal[1]*p['radial_y'][j]
                  for j in range(3)]
        midpoint = [(a[0]+b[0])/2.0, (a[1]+b[1])/2.0]
        plane_point = [p['head_base'][j] + midpoint[0]*p['radial_x'][j]
                       + midpoint[1]*p['radial_y'][j] for j in range(3)]
        expected_planes.append((normal, plane_point))
    for station in (p['head_base'], p['tip']):
        expected_planes.append((p['axis'], station))

    planes = features.get('planes')
    if not isinstance(planes, list):
        raise ValueError('Native analytic plane inventory is required')
    unique_planes = []
    for row in planes:
        signature = _plane_signature(row)
        if not any(_plane_match(signature, prior, tol) for prior in unique_planes):
            unique_planes.append(signature)
    unmatched = list(unique_planes)
    plane_matches = []
    for expected in expected_planes:
        found = next((i for i, row in enumerate(unmatched) if _plane_match(row, expected, tol)), None)
        plane_matches.append(found is not None)
        if found is not None:
            unmatched.pop(found)

    cylinders = features.get('cylinders')
    if not isinstance(cylinders, list):
        raise ValueError('Native analytic cylinder inventory is required')
    unique_cylinders = []
    for row in cylinders:
        axis = _unit(row.get('axis'), 'cylinder axis')
        origin = _vec(row.get('origin'), 'cylinder origin')
        radius_obs = _finite(row.get('radius'), 'cylinder radius')
        if radius_obs <= 0:
            raise ValueError('Cylinder radius must be positive')
        if _dot(axis, p['axis']) < 0:
            axis = [-x for x in axis]
        delta = [origin[i]-p['origin'][i] for i in range(3)]
        center = [delta[i]-_dot(delta,p['axis'])*p['axis'][i] for i in range(3)]
        candidate = (axis, center, radius_obs)
        if not any(_norm([axis[i]-old[0][i] for i in range(3)]) <= tol
                   and _norm([center[i]-old[1][i] for i in range(3)]) <= tol
                   and abs(radius_obs-old[2]) <= tol for old in unique_cylinders):
            unique_cylinders.append(candidate)
    cylinder_ok = (len(unique_cylinders) == 1
                   and _norm([unique_cylinders[0][0][i]-p['axis'][i] for i in range(3)]) <= tol
                   and _norm(unique_cylinders[0][1]) <= tol
                   and abs(unique_cylinders[0][2]-p['shaft_radius']) <= tol)
    unexpected = {name: features.get(name, []) for name in ('cones','spheres','tori')
                  if features.get(name)}
    points_obs = features.get('points')
    if not isinstance(points_obs, list) or not points_obs:
        raise ValueError('Native vertex-point inventory is required')
    axial = [_dot([_finite(x,'point coordinate') for x in point], p['axis'])
             for point in points_obs]
    expected_min = _dot(p['head_base'], p['axis'])
    expected_max = _dot(p['tip'], p['axis'])
    extrema_ok = abs(min(axial)-expected_min) <= tol and abs(max(axial)-expected_max) <= tol
    closure = features.get('topology', {})
    closed = (closure.get('bodies') == 1 and closure.get('lumps') == 1
              and closure.get('shells') == 1
              and closure.get('reciprocal_closed_partners') == 1)
    checks = [
        {'check':'six unique hex side planes and two axial end planes','result':'PASS' if all(plane_matches) and not unmatched and len(unique_planes)==8 else 'FAIL','matches':plane_matches,'unexpected_unique_planes':len(unmatched),'observed_unique_planes':len(unique_planes)},
        {'check':'one coaxial nominal-radius shaft cylinder','result':'PASS' if cylinder_ok else 'FAIL','observed_unique_cylinders':len(unique_cylinders),'expected_radius_mm':p['shaft_radius']},
        {'check':'no additional cone, sphere or torus surfaces','result':'PASS' if not unexpected else 'FAIL','unexpected':unexpected},
        {'check':'axial vertex extrema equal head top and shaft tip stations','result':'PASS' if extrema_ok else 'FAIL','observed_min_max_mm':[min(axial),max(axial)],'expected_min_max_mm':[expected_min,expected_max]},
        {'check':'one closed connected solid','result':'PASS' if closed else 'FAIL','observed_topology':closure}
    ]
    return {'result':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',
            'method':'unique native analytic plane/cylinder identities, axial vertex extrema and solid topology',
            'tolerance_mm':tol,'checks':checks}


def inspect(client, handles, job, root_map=None):
    """Read one same-document Solid3D and bind evidence to a stable epoch."""
    if set(handles) != {'body'}:
        raise ValueError("Inspection requires exactly one 'body' handle")
    document_id = getattr(client, 'document_id', None)
    if document_id is None:
        raise ValueError('Client must be bound to a document id')
    before = client.read('state')
    epoch = (before.get('document_id'), before.get('revision'), before.get('geometry_revision'))
    if epoch[0] != document_id or epoch[1] is None or epoch[2] is None:
        raise ValueError('Pre-read state is not bound to a complete document epoch')
    records = client.read('records', collection='entities', handles=[handles['body']], limit=1)
    if (records.get('document_id'), records.get('revision'), records.get('geometry_revision')) != epoch:
        raise ValueError('Entity read differs from the bound document epoch')
    rows = records.get('records', [])
    if len(rows) != 1 or rows[0].get('handle') != handles['body'] or rows[0].get('type') != 'Solid3D':
        raise ValueError('Expected one native Solid3D record')
    acis = rows[0].get('properties', {}).get('acis_data', {})
    sab = acis.get('sab_data')
    if not sab:
        raise ValueError('Reopened reference requires SAB body bytes')
    from native_acis import sab_features
    features = sab_features(bytes(sab), allow_rigid=True, include_loops=True)
    geometry_result = verify(features, job, root_map)
    metadata = verify_metadata(rows[0], handles['body'], job, root_map)
    after = client.read('state')
    if (after.get('document_id'), after.get('revision'), after.get('geometry_revision')) != epoch:
        raise ValueError('Inspection changed or lost the bound document epoch')
    result = {'result':'PASS' if geometry_result['result']==metadata['result']=='PASS' else 'FAIL',
              'document_id':document_id,'revision':epoch[1],'geometry_revision':epoch[2],
              'handle':handles['body'],'geometry':geometry_result,'metadata':metadata}
    return records, result


def verify_metadata(record, handle, job, root_map=None):
    return compare_source_metadata(record, handle, METADATA_APPLICATION,
                                   parameters(job, root_map)['metadata_lines'])
