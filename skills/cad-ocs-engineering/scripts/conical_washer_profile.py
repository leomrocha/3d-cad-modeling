"""Construct and inspect source-bound straight-strip conical washers.

The caller supplies source dimensions, configuration identity, frame, placement
and tolerance in an external job.  This helper solves one shallow rectangular
strip section from its projected radial width, axial height and normal
thickness, then revolves that closed profile with the existing OCS adapter.
"""
import importlib
import math
from copy import deepcopy

from component_records import require_ready, resolve_source_locator
from feature_checks import closed_body
from source_metadata import compare_source_metadata

METADATA_APPLICATION = 'CADTOOLS_SOURCE'


def _finite(value, label):
    try:
        finite = math.isfinite(value)
    except (OverflowError, TypeError):
        finite = False
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not finite:
        raise ValueError(label + ' must be finite')
    return float(value)


def _runtime_job(job, root_map):
    """Resolve source feature paths on a runtime clone; leave stored job locators intact."""
    if not isinstance(job, dict):
        raise ValueError('External conical washer job must be an object')
    runtime = deepcopy(job)
    if not isinstance(runtime.get('features'), list):
        raise ValueError('External conical washer job needs a feature list')
    for feature in runtime['features']:
        if not isinstance(feature, dict) or feature.get('value') is None:
            continue
        try:
            feature['source'] = str(resolve_source_locator(feature.get('source'), root_map))
        except (TypeError, ValueError) as error:
            raise ValueError('Source feature locator cannot be resolved: '
                             + str(feature.get('name', '<unnamed>'))) from error
    return runtime


def _poly_value(coefficients, x):
    result = 0.0
    for value in reversed(coefficients):
        result = result * x + value
    return result


def _poly_roots_in_interval(coefficients, low, high):
    """Isolate all real roots of a degree-at-most-four polynomial in an interval."""
    coefficients = list(coefficients)
    scale = max((abs(value) for value in coefficients), default=0.0)
    if not math.isfinite(scale) or scale == 0:
        raise ValueError('Root polynomial must have finite nonzero coefficients')
    while len(coefficients) > 1 and abs(coefficients[-1]) <= scale * 1e-15:
        coefficients.pop()
    degree = len(coefficients) - 1
    zero_tolerance = scale * 2e-13
    if degree == 0:
        return []
    if degree == 1:
        root = -coefficients[0] / coefficients[1]
        return [root] if low <= root <= high else []

    derivative = [index * coefficients[index] for index in range(1, len(coefficients))]
    critical = _poly_roots_in_interval(derivative, low, high)
    divisions = [low] + [root for root in critical if low < root < high] + [high]
    divisions = sorted(set(divisions))
    roots = []
    for point in divisions:
        if abs(_poly_value(coefficients, point)) <= zero_tolerance:
            roots.append(point)
    for left, right in zip(divisions, divisions[1:]):
        f_left = _poly_value(coefficients, left)
        f_right = _poly_value(coefficients, right)
        if f_left == 0 or f_right == 0 or f_left * f_right > 0:
            continue
        a, b, fa = left, right, f_left
        for _ in range(100):
            middle = (a + b) / 2
            fm = _poly_value(coefficients, middle)
            if fm == 0 or b - a <= 2e-14 * max(1.0, abs(middle)):
                a = b = middle
                break
            if fa * fm <= 0:
                b = middle
            else:
                a, fa = middle, fm
        roots.append((a + b) / 2)
    unique = []
    for root in sorted(roots):
        if not unique or abs(root - unique[-1]) > 1e-10:
            unique.append(root)
    return unique


def _solve_strip(width, height, thickness, angle_interval_degrees):
    """Solve the unique physical strip solution on a declared shallow branch."""
    if not isinstance(angle_interval_degrees, (list, tuple)) or len(angle_interval_degrees) != 2:
        raise ValueError('Explicit two-value angle_interval_degrees is required')
    low_degrees = _finite(angle_interval_degrees[0], 'minimum profile angle')
    high_degrees = _finite(angle_interval_degrees[1], 'maximum profile angle')
    if not (0 <= low_degrees < high_degrees <= 45):
        raise ValueError('Supported conical profile branch is within 0..45 degrees')
    low, high = math.tan(math.radians(low_degrees)), math.tan(math.radians(high_degrees))

    # Squaring (H - w*q)/sqrt(1+q^2) = t*(1-q^2)/(1+q^2),
    # q=tan(alpha), yields this quartic. Candidate roots are checked in the
    # unsquared equation so the opposite-sign roots introduced by squaring fail.
    h2, w2, t2 = height * height, width * width, thickness * thickness
    coefficients = [h2 - t2, -2 * height * width,
                    w2 + h2 + 2 * t2, -2 * height * width, w2 - t2]
    candidates = []
    for tangent in _poly_roots_in_interval(coefficients, low, high):
        angle = math.atan(tangent)
        if not low_degrees < math.degrees(angle) < high_degrees:
            continue
        if height - width * tangent < -1e-11 * max(height, width):
            continue
        cosine, sine = math.cos(angle), math.sin(angle)
        denominator = math.cos(2 * angle)
        if denominator <= 0:
            continue
        length = (width * cosine - height * sine) / denominator
        if not math.isfinite(length) or length <= thickness:
            continue
        predicted_width = length * cosine + thickness * sine
        predicted_height = length * sine + thickness * cosine
        check_tol = 2e-9 * max(width, height, thickness)
        if (abs(predicted_width - width) > check_tol
                or abs(predicted_height - height) > check_tol):
            continue
        candidates.append((length, angle))
    if len(candidates) != 1:
        raise ValueError('Declared shallow branch must contain exactly one physical strip solution')
    return candidates[0]


def parameters(job, root_map=None):
    """Validate source features and derive the closed axial-radial profile."""
    job = _runtime_job(job, root_map)
    try:
        require_ready(job)
    except OverflowError as error:
        raise ValueError('Source dimensions must be finite representable numbers') from error
    if job.get('units') != 'mm':
        raise ValueError('Conical washer reference supports millimetres only')
    if job.get('geometry_role') != 'reference_conical_washer':
        raise ValueError('Explicit geometry_role=reference_conical_washer is required')
    for key in ('job_id', 'part_id', 'part_name', 'configuration', 'representation',
                'geometry_name', 'frame', 'local_frame', 'metadata_request_label'):
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError('Explicit nonempty ' + key + ' is required')
    if job.get('metadata_application') != METADATA_APPLICATION:
        raise ValueError('Geometry.metadata uses the fixed CADTOOLS_SOURCE application')
    feature_names = job.get('dimension_features')
    expected_dimensions = {'inside_diameter', 'outside_diameter', 'normal_thickness', 'free_height'}
    if not isinstance(feature_names, dict) or set(feature_names) != expected_dimensions:
        raise ValueError('dimension_features must bind inside_diameter, outside_diameter, normal_thickness and free_height')
    names = list(feature_names.values())
    if (any(not isinstance(name, str) or not name.strip() for name in names)
            or len(set(names)) != len(expected_dimensions)):
        raise ValueError('Four distinct readable source feature names are required')
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
    inside = dimensions['inside_diameter']
    outside = dimensions['outside_diameter']
    thickness = dimensions['normal_thickness']
    height = dimensions['free_height']
    if inside >= outside:
        raise ValueError('Inside diameter must be smaller than outside diameter')
    width = (outside - inside) / 2
    if not math.isfinite(width) or width <= 0:
        raise ValueError('Projected radial strip width collapses')
    if thickness >= width or thickness >= height:
        raise ValueError('Strip thickness must be smaller than radial width and axial height')
    length, angle = _solve_strip(width, height, thickness,
                                 job.get('angle_interval_degrees'))
    cosine, sine = math.cos(angle), math.sin(angle)

    center = job.get('center')
    if not isinstance(center, (list, tuple)) or len(center) != 2:
        raise ValueError('Explicit two-coordinate axis center is required')
    center = [_finite(value, 'axis center') for value in center]
    z_origin = _finite(job.get('z_origin'), 'z_origin')
    tolerance = _finite(job.get('readback_tolerance', 1e-7), 'readback_tolerance')
    angle_tolerance = _finite(job.get('readback_angle_tolerance_rad', 1e-7),
                              'readback_angle_tolerance_rad')
    if tolerance <= 0 or angle_tolerance <= 0:
        raise ValueError('Positive finite readback tolerances are required')

    inner_r, outer_r = inside / 2, outside / 2
    # Coordinates retain the source extrema: minimum radius at inner_r,
    # maximum radius at outer_r, and axial range [z_origin,z_origin+free height].
    profile = [
        [inner_r, length * sine],
        [inner_r + length * cosine, 0.0],
        [outer_r, thickness * cosine],
        [inner_r + thickness * sine, height],
    ]
    profile = [[_finite(point[0], 'profile radius'), _finite(point[1], 'profile height')]
               for point in profile]
    if any(point[0] <= 0 for point in profile):
        raise ValueError('Revolved washer profile must remain outside the axis')
    if any(first == second for first, second in zip(profile, profile[1:] + profile[:1])):
        raise ValueError('Conical washer profile vertices collapse numerically')
    if not math.isfinite(z_origin + height) or z_origin + height <= z_origin:
        raise ValueError('Washer axial placement collapses or overflows numerically')
    for center_value, extent, axis_name in ((center[0], outer_r, 'X'), (center[1], outer_r, 'Y')):
        low, high = center_value - extent, center_value + extent
        if (not math.isfinite(low) or not math.isfinite(high)
                or low >= center_value or high <= center_value):
            raise ValueError(axis_name + ' washer radius collapses at the requested centre')

    edges = [[b[0]-a[0], b[1]-a[1]]
             for a, b in zip(profile, profile[1:] + profile[:1])]
    edge_lengths = [math.hypot(*edge) for edge in edges]
    if not all(math.isfinite(value) and value > 0 for value in edge_lengths):
        raise ValueError('Washer profile edge length collapses or overflows')
    cross_products = [edges[i][0]*edges[(i+1)%4][1]
                      - edges[i][1]*edges[(i+1)%4][0] for i in range(4)]
    signed_area = sum(a[0]*b[1]-b[0]*a[1]
                      for a,b in zip(profile,profile[1:]+profile[:1])) / 2
    dot_products = [edges[i][0]*edges[(i+1)%4][0]
                    + edges[i][1]*edges[(i+1)%4][1] for i in range(4)]
    invariant_tolerance = 5e-10 * max(length*thickness, 1.0)
    if (signed_area <= 0 or abs(signed_area-length*thickness) > invariant_tolerance
            or any(value <= 0 for value in cross_products)
            or any(abs(value) > invariant_tolerance for value in dot_products)
            or abs(edge_lengths[0]-length) > invariant_tolerance
            or abs(edge_lengths[2]-length) > invariant_tolerance
            or abs(edge_lengths[1]-thickness) > invariant_tolerance
            or abs(edge_lengths[3]-thickness) > invariant_tolerance):
        raise ValueError('Washer profile must be closed, convex and positive with normal thickness t')
    if (abs(min(point[0] for point in profile)-inner_r) > invariant_tolerance
            or abs(max(point[0] for point in profile)-outer_r) > invariant_tolerance
            or abs(min(point[1] for point in profile)) > invariant_tolerance
            or abs(max(point[1] for point in profile)-height) > invariant_tolerance):
        raise ValueError('Washer profile lost a source diameter or free-height extent')

    extra = job.get('metadata', [])
    if not isinstance(extra, list) or any(not isinstance(v, str) or not v.strip() for v in extra):
        raise ValueError('metadata must be a list of nonempty strings')
    metadata = [job['part_id'], job['part_name'], 'Configuration: ' + job['configuration'],
                job['representation'], 'Units: mm', 'Frame: ' + job['local_frame'],
                'Source job: ' + job['job_id'],
                'Nominal free single-washer conical strip; no stack or installed direction represented',
                'Calculated strip length mm: ' + format(length, '.12g'),
                'Calculated inclination degrees: ' + format(math.degrees(angle), '.12g')] + extra
    return {'dimensions': dimensions, 'radial_width': width, 'strip_length': length,
            'inclination_radians': angle, 'inclination_degrees': math.degrees(angle),
            'center': center, 'z_origin': z_origin, 'z_end': z_origin + height,
            'profile': profile, 'tolerance': tolerance,
            'angle_tolerance_rad': angle_tolerance, 'metadata': metadata}


def geometry(client):
    """Create the existing guarded OCS Geometry adapter."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_conical_washer(client, job, root_map=None):
    """Revolve one validated closed strip section into a washer solid."""
    p = parameters(job, root_map)
    g = geometry(client)
    solid = g.revolve_z(job['geometry_name'] + ' closed conical section', p['profile'])
    displacement = [p['center'][0], p['center'][1], p['z_origin']]
    if displacement != [0.0, 0.0, 0.0]:
        g.move(job['geometry_name'] + ' local axis placement', [solid], displacement)
    g.metadata(job['metadata_request_label'], [solid], p['metadata'])
    return solid


def verify(features, job, root_map=None):
    """Check source profile vertices, four conical faces and one closed body."""
    p = parameters(job, root_map)
    dims = p['dimensions']
    points = features.get('points')
    if not isinstance(points, list) or len(points) < 4:
        raise ValueError('Native vertex observations for the conical profile are required')
    radial = []
    axial = []
    for point in points:
        if not isinstance(point, (list, tuple)) or len(point) != 3:
            raise ValueError('Native profile points must have three coordinates')
        x, y, z = [_finite(value, 'native vertex coordinate') for value in point]
        radial.append(_finite(math.hypot(x - p['center'][0], y - p['center'][1]),
                              'native radial distance'))
        axial.append(z)
    radial_extrema = [min(radial), max(radial)]
    axial_extrema = [min(axial), max(axial)]
    tol = p['tolerance']
    radius_check = {'check': 'Source inside and outside diameter radial extrema',
                    'observed_radii_mm': radial_extrema,
                    'expected_radii_mm': [dims['inside_diameter'] / 2,
                                          dims['outside_diameter'] / 2],
                    'numeric_tolerance_mm': tol,
                    'method': 'native profile vertex radial distances from the specified washer axis',
                    'result': 'PASS' if all(abs(a-b) <= tol for a,b in zip(
                        radial_extrema, [dims['inside_diameter']/2, dims['outside_diameter']/2])) else 'FAIL'}
    height_check = {'check': 'Source basic/reference free height',
                    'observed_axial_extrema_mm': axial_extrema,
                    'expected_axial_extrema_mm': [p['z_origin'], p['z_end']],
                    'numeric_tolerance_mm': tol,
                    'method': 'native profile vertex axial coordinate extrema',
                    'result': 'PASS' if all(abs(a-b) <= tol for a,b in zip(
                        axial_extrema, [p['z_origin'], p['z_end']])) else 'FAIL'}
    expected_profile = sorted((point[0], point[1] + p['z_origin']) for point in p['profile'])
    raw_profile = sorted(zip(radial, axial))
    observed_profile = []
    for candidate in raw_profile:
        if not any(abs(candidate[0]-seen[0]) <= tol
                   and abs(candidate[1]-seen[1]) <= tol for seen in observed_profile):
            observed_profile.append(candidate)
    profile_matches = []
    unmatched_observed = list(observed_profile)
    for expected in expected_profile:
        matches = [row for row in unmatched_observed
                   if abs(row[0] - expected[0]) <= tol
                   and abs(row[1] - expected[1]) <= tol]
        if len(matches) == 1:
            profile_matches.append({'expected_radius_z_mm': list(expected),
                                    'observed_radius_z_mm': list(matches[0])})
            unmatched_observed.remove(matches[0])
        else:
            profile_matches.append({'expected_radius_z_mm': list(expected),
                                    'matching_observed_vertices': len(matches)})
    profile_check = {'check': 'All four source-derived axial-radial section vertices are reproduced',
                     'observed_native_profile_vertex_count_raw': len(raw_profile),
                     'observed_native_profile_vertices_unique_within_tolerance': [list(row) for row in observed_profile],
                     'expected_profile_vertices': [list(row) for row in expected_profile],
                     'matched_vertices': profile_matches,
                     'unmatched_observed_vertices': [list(row) for row in unmatched_observed],
                     'numeric_tolerance_mm': tol,
                     'method': 'native seam-vertex radial distances about the specified axis and axial stations',
                     'result': 'PASS' if len(observed_profile) == 4 and not unmatched_observed
                     and all('observed_radius_z_mm' in row for row in profile_matches) else 'FAIL'}

    cones = features.get('cones')
    if not isinstance(cones, list) or len(cones) != 4:
        raise ValueError('Four native conical surface records are required')
    observed_angles = []
    unexpected_axes = []
    for cone in cones:
        axis = cone.get('axis', [])
        if len(axis) != 3:
            raise ValueError('Native cone axis must have three coordinates')
        axis = [_finite(v, 'native cone axis') for v in axis]
        if (abs(abs(axis[2]) - 1) > p['angle_tolerance_rad']
                or abs(axis[0]) > p['angle_tolerance_rad']
                or abs(axis[1]) > p['angle_tolerance_rad']):
            unexpected_axes.append(axis)
        sine = _finite(cone.get('sin_angle'), 'native cone sin_angle')
        cosine = _finite(cone.get('cos_angle'), 'native cone cos_angle')
        angle = math.atan2(abs(sine), abs(cosine))
        observed_angles.append(angle)
    expected_angles = sorted([p['inclination_radians'], p['inclination_radians'],
                              math.pi/2-p['inclination_radians'],
                              math.pi/2-p['inclination_radians']])
    angle_ok = len(observed_angles) == len(expected_angles) and all(
        abs(a-b) <= p['angle_tolerance_rad'] for a,b in
        zip(sorted(observed_angles), expected_angles))
    cone_check = {'check': 'Four conical surfaces follow the source-bound strip edge angles',
                  'observed_angles_rad': sorted(observed_angles),
                  'expected_angles_rad': expected_angles,
                  'unexpected_axes': unexpected_axes,
                  'numeric_angular_tolerance_rad': p['angle_tolerance_rad'],
                  'method': 'native SAB cone-surface axis and semi-angle records',
                  'result': 'PASS' if angle_ok and not unexpected_axes else 'FAIL'}
    extra = {name: features.get(name, []) for name in ('planes','cylinders','spheres','tori','ellipses')
             if features.get(name)}
    surface_check = {'check': 'Only the four expected conical surface families are present',
                     'observed_extra_surfaces': extra,
                     'expected_extra_surfaces': {},
                     'result': 'PASS' if not extra else 'FAIL'}
    topology_check = closed_body('One closed connected conical washer body', features)
    checks = [radius_check, height_check, profile_check, cone_check, surface_check, topology_check]
    return {'result': 'PASS' if all(row.get('result') == 'PASS' for row in checks) else 'FAIL',
            'method': 'source-bound radial and axial extrema, analytic cone surfaces and closed-body topology',
            'source_dimensions_mm': dims, 'calculated_strip_length_mm': p['strip_length'],
            'calculated_inclination_degrees': p['inclination_degrees'],
            'representation': job['representation'], 'local_frame': job['local_frame'],
            'scope': 'one nominal free washer; no installation stack or facing direction',
            'checks': checks}


def verify_metadata(record, handle, job, root_map=None):
    """Compare source identity, configuration, frame and scope metadata."""
    p = parameters(job, root_map)
    return compare_source_metadata(record, handle, METADATA_APPLICATION, p['metadata'])


def inspect(client, handle, job, root_map=None):
    """Inspect one reopened Solid3D and bind SAB checks to its document revision."""
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
        raise ValueError('Reopened conical washer record must be Solid3D')
    sab = record.get('properties', {}).get('acis_data', {}).get('sab_data')
    if not sab:
        raise ValueError('Reopened conical washer SAB geometry is required')
    from native_acis import sab_features
    features = sab_features(bytes(sab), allow_rigid=True, allow_cones=True, include_loops=False)
    geometry_check = verify(features, job, root_map)
    metadata_check = verify_metadata(record, handle, job, root_map)
    after = client.read('state')
    if (after.get('document_id') != document_id
            or after.get('geometry_revision') != geometry_revision
            or after.get('revision') != revision):
        raise ValueError('Document identity or revision changed during conical washer inspection')
    result = {'result': 'PASS' if geometry_check['result'] == 'PASS'
              and metadata_check['result'] == 'PASS' else 'FAIL',
              'document_id': document_id, 'document_revision': revision,
              'geometry_revision': geometry_revision, 'handle': handle,
              'geometry': geometry_check, 'metadata': metadata_check,
              'encoding': 'SAB analytic cone surfaces with connected closed-body topology',
              'features': features}
    return response, result, record
