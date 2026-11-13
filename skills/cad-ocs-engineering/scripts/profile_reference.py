"""Build and inspect a source-traced polygon extruded as a reference volume.

Component values and source records come from the caller's external job. This
helper preserves the supplied straight-segment outline and extrusion depth; it
does not infer source dimensions or claim detailed product geometry.
"""

import importlib
import math

from component_records import require_ready
from feature_checks import closed_body, vertex_extrema
from step_placements import identity_sat_vertices


SUPPORTED_REFERENCE_ROLES = {
    'source_traced_projected_profile_reference',
    'source_view_projected_clearance_reference',
    'source_traced_packaging_clearance_reference',
}


def _finite_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name + " must be a finite number")
    try:
        if not math.isfinite(value):
            raise ValueError(name + " must be a finite number")
        converted = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError(name + " must be a finite number") from error
    if not math.isfinite(converted):
        raise ValueError(name + " must be a finite number")
    return converted


def _point2(value, name):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(name + " must contain two finite coordinates")
    return [_finite_number(value[0], name), _finite_number(value[1], name)]


def _cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _on_segment(a, b, p, eps):
    return (min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps
            and min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps)


def _segments_intersect(a, b, c, d, eps):
    o1, o2, o3, o4 = (_cross(a, b, c), _cross(a, b, d),
                      _cross(c, d, a), _cross(c, d, b))
    if ((o1 > eps and o2 < -eps) or (o1 < -eps and o2 > eps)) \
            and ((o3 > eps and o4 < -eps) or (o3 < -eps and o4 > eps)):
        return True
    return ((abs(o1) <= eps and _on_segment(a, b, c, eps))
            or (abs(o2) <= eps and _on_segment(a, b, d, eps))
            or (abs(o3) <= eps and _on_segment(c, d, a, eps))
            or (abs(o4) <= eps and _on_segment(c, d, b, eps)))


def validate_profile(points):
    """Validate one closed simple polygon of straight segments."""
    if not isinstance(points, (list, tuple)) or len(points) < 3:
        raise ValueError("profile_points must contain at least three points")
    polygon = [_point2(point, f"profile_points[{index}]")
               for index, point in enumerate(points)]
    if any(a == b for a, b in zip(polygon, polygon[1:])) or polygon[0] == polygon[-1]:
        raise ValueError("profile_points must omit consecutive and closing duplicate points")
    if len({tuple(point) for point in polygon}) != len(polygon):
        raise ValueError("profile_points must not repeat or retrace a vertex")

    min_x = min(point[0] for point in polygon)
    min_y = min(point[1] for point in polygon)
    max_span = max(max(point[0] for point in polygon) - min_x,
                   max(point[1] for point in polygon) - min_y)
    if not math.isfinite(max_span) or max_span <= 0:
        raise ValueError("profile_points must span a finite nonzero area")
    scaled = [[(point[0] - min_x) / max_span,
               (point[1] - min_y) / max_span] for point in polygon]
    area2 = 0.0
    for index, point in enumerate(scaled):
        following = scaled[(index + 1) % len(scaled)]
        term = point[0] * following[1] - following[0] * point[1]
        area2 += term
        if not math.isfinite(area2):
            raise ValueError("profile area calculation overflowed")
    if area2 == 0:
        raise ValueError("profile_points must have nonzero area")

    eps = 1e-12
    count = len(scaled)
    for i in range(count):
        a, b = scaled[i], scaled[(i + 1) % count]
        for j in range(i + 1, count):
            if j == i or j == (i + 1) % count or (j + 1) % count == i:
                continue
            c, d = scaled[j], scaled[(j + 1) % count]
            if _segments_intersect(a, b, c, d, eps):
                raise ValueError("profile_points must not cross, touch or retrace nonadjacent edges")
    return polygon


def parameters(job):
    """Validate source readiness and every construction value before writes."""
    ready = require_ready(job)
    pinned_sources = {(row['path'], row['sha256'])
                      for row in ready['source_observations']}
    for key in ("job_id", "part_id", "part_name", "representation", "geometry_role",
                "geometry_name", "units", "frame", "local_frame", "geometry_scope"):
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError(key + " must be a nonempty string")
    if job["units"] != "mm":
        raise ValueError("profile reference helper supports millimetres only")
    if job['geometry_role'] not in SUPPORTED_REFERENCE_ROLES:
        raise ValueError('geometry_role must identify a supported projected profile reference')
    if not isinstance(job.get("origin"), (list, tuple)) or len(job["origin"]) != 3:
        raise ValueError("origin must contain three finite coordinates")
    origin = [_finite_number(value, "origin") for value in job["origin"]]
    profile = validate_profile(job.get("profile_points_2d"))
    depth = _finite_number(job.get("depth_mm"), "depth_mm")
    if depth <= 0:
        raise ValueError("depth_mm must be positive")
    far_z = origin[2] + depth
    if not math.isfinite(far_z):
        raise ValueError("origin plus depth overflows the construction coordinate")
    if far_z <= origin[2]:
        raise ValueError("positive extrusion depth is lost at the supplied z origin")

    translated = []
    for index, point in enumerate(profile):
        xy = [point[0] + origin[0], point[1] + origin[1]]
        if any(not math.isfinite(value) for value in xy):
            raise ValueError(f"profile_points_2d[{index}] plus origin overflows")
        translated.append(xy)
    validate_profile(translated)
    tolerance = _finite_number(job.get("readback_tolerance_mm", 1e-7),
                               "readback_tolerance_mm")
    if tolerance <= 0:
        raise ValueError("readback_tolerance_mm must be positive")
    depth_feature = job.get("depth_feature_name")
    features = {feature["name"]: feature for feature in job["features"]}
    if not isinstance(depth_feature, str) or depth_feature not in features:
        raise ValueError("depth_feature_name must identify a source-ready feature")
    if features[depth_feature].get('required') is not True:
        raise ValueError('depth_feature_name must identify a required source feature')
    source_depth = _finite_number(features[depth_feature].get("value"), 'depth feature value')
    if source_depth != depth \
            or features[depth_feature].get("unit") != "mm":
        raise ValueError("depth_mm must equal its pinned source feature value in mm")
    source_files = job.get("source_files")
    if not isinstance(source_files, list) or not source_files:
        raise ValueError("source_files must contain at least one pinned original or derived source")
    required_pinned = {(row['path'], row['sha256']) for feature in job['features']
                       if feature.get('required') is True and feature.get('value') is not None
                       for row in ready['source_observations'] if row['feature'] == feature['name']}
    if not any((source.get('path'), source.get('sha256')) in required_pinned
               for source in source_files if isinstance(source, dict)):
        raise ValueError('at least one source file must be pinned by a required source feature')
    for index, source in enumerate(source_files):
        if not isinstance(source, dict):
            raise ValueError(f"source_files[{index}] must be an object")
        if any(not isinstance(source.get(key), str) or not source[key].strip()
               for key in ("path", "sha256")):
            raise ValueError(f"source_files[{index}] needs path and sha256")
        if (source['path'], source['sha256']) not in pinned_sources:
            raise ValueError(f"source_files[{index}] must be pinned by a required job feature")
        if (source['path'], source['sha256']) not in required_pinned:
            raise ValueError(f"source_files[{index}] must be pinned by a required feature")
    extent_features = job.get('profile_extent_features')
    extent_bounds = job.get('profile_extent_bounds_mm')
    if not isinstance(extent_features, dict) or set(extent_features) != {'x', 'y'}:
        raise ValueError('profile_extent_features must map both x and y to required source features')
    if not isinstance(extent_bounds, dict) or set(extent_bounds) != {'x', 'y'}:
        raise ValueError('profile_extent_bounds_mm must give explicit bounds for x and y')
    profile_extents = [max(point[axis] for point in profile) - min(point[axis] for point in profile)
                       for axis in (0, 1)]
    for axis_name, axis_index in (('x', 0), ('y', 1)):
        feature_name = extent_features[axis_name]
        if not isinstance(feature_name, str) or feature_name not in features:
            raise ValueError(f'profile extent {axis_name} must identify a required source feature')
        feature = features[feature_name]
        if feature.get('required') is not True or feature.get('unit') != 'mm' \
                or isinstance(feature.get('value'), bool) or not isinstance(feature.get('value'), (int, float)):
            raise ValueError(f'profile extent {axis_name} needs a required numeric source feature in mm')
        bounds = extent_bounds[axis_name]
        if not isinstance(bounds, (list, tuple)) or len(bounds) != 2:
            raise ValueError(f'profile extent bounds {axis_name} must contain lower and upper mm values')
        lower, upper = (_finite_number(value, f'profile_extent_bounds_mm.{axis_name}')
                        for value in bounds)
        if lower < 0 or upper < lower:
            raise ValueError(f'profile extent bounds {axis_name} must be ordered and nonnegative')
        source_value = _finite_number(feature['value'], f'profile extent source value {axis_name}')
        if source_value <= 0:
            raise ValueError(f'profile extent source value {axis_name} must be positive')
        if not lower <= source_value <= upper:
            raise ValueError(f'profile extent bounds {axis_name} do not contain its source feature value')
        basis = job.get('profile_extent_basis', {}).get(axis_name) \
            if isinstance(job.get('profile_extent_basis'), dict) else None
        if not isinstance(basis, str) or not basis.strip():
            raise ValueError(f'profile_extent_basis.{axis_name} must describe the source-bound interval')
        if not lower <= profile_extents[axis_index] <= upper:
            raise ValueError(f'profile {axis_name} extent {profile_extents[axis_index]:g} mm is outside '
                             f'the source-bound interval [{lower:g}, {upper:g}] mm')
    scope = job["geometry_scope"].strip()
    return {'origin': origin, 'profile': profile, 'translated_profile': translated,
            'depth': depth, 'far_z': far_z, 'tolerance': tolerance,
            'depth_feature': depth_feature, 'scope': scope,
            'profile_extents': dict(zip(('x', 'y'), profile_extents)),
            'profile_extent_features': extent_features,
            'profile_extent_bounds_mm': extent_bounds}


def geometry(client):
    """Use the installed Geometry adapter with the established selection guard."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_profile_reference(client, job):
    """Create one source-traced profile extrusion after full input preflight."""
    p = parameters(job)
    g = geometry(client)
    solid = g.extrude(job['geometry_name'], p['translated_profile'],
                      p['origin'][2], p['depth'])
    metadata = [
        job['part_name'], job['representation'],
        'Geometry role: ' + job['geometry_role'],
        'Units: mm; local frame: ' + job['local_frame'],
        'Source job: ' + job['job_id'],
        'Geometry scope: ' + p['scope'],
        'Extrusion depth source feature: ' + p['depth_feature'],
    ]
    for source in job.get('source_files', []):
        metadata.append('Source file: ' + source['path'] + ' SHA-256 ' + source['sha256'])
    g.metadata(job['geometry_name'] + ' source metadata', [solid], metadata)
    return solid


def _expected_vertices(parameters_):
    origin, depth = parameters_['origin'], parameters_['depth']
    z0, z1 = origin[2], parameters_['far_z']
    return [[point[0] + origin[0], point[1] + origin[1], z]
            for point in parameters_['profile'] for z in (z0, z1)]


def _point_set_comparison(actual, expected, tolerance):
    def unique(points):
        result = []
        for point in points:
            if not isinstance(point, (list, tuple)) or len(point) != 3:
                raise ValueError("native and expected point records must be 3D")
            values = [_finite_number(value, "point coordinate") for value in point]
            duplicate = False
            for old in result:
                differences = [abs(a - b) for a, b in zip(values, old)]
                if any(not math.isfinite(value) for value in differences):
                    raise ValueError("native point comparison overflowed")
                if max(differences) <= tolerance:
                    duplicate = True
                    break
            if not duplicate:
                result.append(values)
        return result

    actual_points, expected_points = unique(actual), unique(expected)
    if not actual_points or not expected_points:
        raise ValueError("native and expected extruded profile vertices must be nonempty")

    def contains(point, points):
        for candidate in points:
            differences = [abs(a - b) for a, b in zip(point, candidate)]
            if any(not math.isfinite(value) for value in differences):
                raise ValueError("native point comparison overflowed")
            if max(differences) <= tolerance:
                return True
        return False

    missing = [point for point in expected_points if not contains(point, actual_points)]
    extra = [point for point in actual_points if not contains(point, expected_points)]
    result = {'check': 'Native vertices reproduce the supplied extruded polygon',
              'method': 'bidirectional 3D point-set comparison after tolerance-based deduplication',
              'numeric_tolerance_mm': tolerance,
              'expected_unique_vertices': len(expected_points),
              'observed_unique_vertices': len(actual_points),
              'missing_expected_vertices': missing,
              'unexpected_native_vertices': extra,
              'result': 'PASS' if not missing and not extra else 'FAIL'}
    return result


def verify(features, job):
    """Check native output bounds and polygon vertices against supplied input."""
    p = parameters(job)
    origin = p['origin']
    points = p['translated_profile']
    expected_bounds = [
        [min(point[0] for point in points), max(point[0] for point in points)],
        [min(point[1] for point in points), max(point[1] for point in points)],
        [origin[2], p['far_z']],
    ]
    checks = [vertex_extrema('Native profile-reference XYZ extrema', features,
                             expected_bounds, p['tolerance']),
              _point_set_comparison(features['points'], _expected_vertices(p), p['tolerance'])]
    if 'topology' in features:
        checks.append(closed_body('Reference extrusion is one closed connected body', features))
    return {'result': 'PASS' if all(row['result'] == 'PASS' for row in checks) else 'FAIL',
            'method': 'native vertex extrema, exact supplied profile endpoint set and closed-body topology when available',
            'numeric_tolerance_mm': p['tolerance'],
            'representation': job['representation'],
            'geometry_role': job['geometry_role'],
            'geometry_scope': p['scope'],
            'source_dimension_expectations': [
                {'name': feature['name'], 'value': feature.get('value'),
                 'unit': feature.get('unit'), 'evidence_status': feature.get('evidence_status'),
                 'source_location': feature.get('source_location')}
                for feature in job['features'] if feature.get('source_dimension_expectation') is True],
            'source_bound_profile_extent_checks': [
                {'axis': axis, 'source_feature': p['profile_extent_features'][axis],
                 'source_value_mm': next(feature['value'] for feature in job['features']
                                          if feature['name'] == p['profile_extent_features'][axis]),
                 'source_comparison_bounds_mm': p['profile_extent_bounds_mm'][axis],
                 'observed_profile_extent_mm': p['profile_extents'][axis],
                 'basis': job.get('profile_extent_basis', {}).get(axis), 'result': 'PASS'}
                for axis in ('x', 'y')],
            'output_bounds_expected_from_profile_and_depth': expected_bounds,
            'checks': checks}


def inspect(client, handles, job):
    """Read one named solid and bind measurements to stable native revisions."""
    if set(handles) != {'solid'}:
        raise ValueError("profile-reference inspection requires one handle named 'solid'")
    expected_document = getattr(client, 'document_id', None)
    if expected_document is None:
        raise ValueError('Client must be bound to an explicit document_id')
    before = client.read('state')
    if before.get('document_id') != expected_document:
        raise ValueError('Active document differs from the bound client document')
    before_geometry_revision = before.get('geometry_revision')
    before_revision = before.get('revision')
    if before_geometry_revision is None or before_revision is None:
        raise ValueError('Pre-read state lacks document or geometry revision')
    response = client.read('records', collection='entities', handles=[handles['solid']], limit=1)
    records = response.get('records', [])
    if len(records) != 1:
        raise ValueError('Expected exactly one profile-reference solid record')
    record = records[0]
    if record.get('handle') != handles['solid']:
        raise ValueError('Native record handle differs from requested solid handle')
    if record.get('type') != 'Solid3D':
        raise ValueError('Native profile-reference record must have type Solid3D')
    if response.get('document_id') not in (None, expected_document):
        raise ValueError('Native record response belongs to a different document')
    if response.get('geometry_revision') not in (None, before_geometry_revision):
        raise ValueError('Native record response geometry_revision differs from active state')
    if response.get('revision') not in (None, before_revision):
        raise ValueError('Native record response revision differs from active state')
    if record.get('document_id') not in (None, expected_document):
        raise ValueError('Native record belongs to a different document')
    if record.get('geometry_revision') not in (None, before_geometry_revision):
        raise ValueError('Native record geometry_revision differs from active state')
    if record.get('revision') not in (None, before_revision):
        raise ValueError('Native record revision differs from active state')
    acis = record.get('properties', {}).get('acis_data', {})
    sat = acis.get('sat_data')
    if sat:
        features = {'points': identity_sat_vertices(sat)}
        encoding = 'SAT point records'
    else:
        sab = acis.get('sab_data')
        if not sab:
            raise ValueError('Native profile-reference SAT/SAB data is absent')
        from native_acis import sab_features
        features = sab_features(bytes(sab), allow_rigid=True)
        encoding = 'SAB native body graph'
    after = client.read('state')
    if after.get('document_id') != expected_document:
        raise ValueError('Active document changed during profile-reference inspection')
    if after.get('geometry_revision') != before_geometry_revision:
        raise ValueError('Geometry revision changed during profile-reference inspection')
    if after.get('revision') != before_revision:
        raise ValueError('Document revision changed during profile-reference inspection')
    result = verify(features, job)
    result.update(document_id=expected_document, document_revision=before_revision,
                  geometry_revision=before_geometry_revision, handle=handles['solid'],
                  encoding=encoding, features=features)
    return response, result
