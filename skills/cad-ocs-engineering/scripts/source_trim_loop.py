"""Prepare one sampled, simply connected source-face trim in a single UV chart."""
import math

from profile_reference import validate_profile


def _identifier(value):
    if type(value) not in (int, str) or value == '':
        raise ValueError('Source entity identifier required')
    return value


def _finite(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError('Finite numeric value required')
    return value


def _vector(value, size):
    if len(value) != size:
        raise ValueError(f'Expected {size} coordinates')
    return [_finite(component) for component in value]


def prepare_trim_loop(*, face_id, support_id, vertices, edges, traversal, inverse_uv,
                      evaluate_support, parameter_bounds, endpoint_limit_mm, inverse_limit_mm):
    """Bind ordered edge uses to corner IDs and compare two independent residuals.

    vertices maps IDs to source XYZ in mm. edges maps IDs to start/end vertex IDs,
    curve_id, same_sense and curve_samples (XYZ in increasing curve parameter).
    traversal gives ordered {edge_id, forward} uses, already in face-bound order.
    inverse_uv(xyz) supplies a candidate in the specified chart. evaluate_support(uv)
    returns a checked {result:'PASS', point:xyz} receipt in the same frame, such
    as evaluate_rational_surface. One loop per call; seams require their own chart.
    """
    _identifier(face_id)
    _identifier(support_id)
    limits = [_finite(x) for x in (endpoint_limit_mm, inverse_limit_mm)]
    if min(limits) < 0:
        raise ValueError('Residual limits must be nonnegative')
    bounds = [_vector(interval, 2) for interval in parameter_bounds]
    if len(bounds) != 2 or any(low >= high for low, high in bounds):
        raise ValueError('Two increasing UV intervals required')
    if not traversal:
        raise ValueError('Ordered edge traversal required')

    def project(xyz):
        uv = _vector(inverse_uv(xyz), 2)
        if any(not low <= q <= high for q, (low, high) in zip(uv, bounds)):
            raise ValueError('Inverse outside declared UV chart')
        receipt = evaluate_support(uv)
        if receipt['result'] != 'PASS':
            raise ValueError('Support evaluation failed')
        residual = math.dist(xyz, _vector(receipt['point'], 3))
        return uv, _finite(residual)

    oriented = []
    for use in traversal:
        edge_id = _identifier(use['edge_id'])
        edge = edges[edge_id]
        first, last = (_identifier(edge[key]) for key in ('start', 'end'))
        forward, sense = use['forward'], edge['same_sense']
        if type(forward) is not bool or type(sense) is not bool:
            raise ValueError('Explicit edge orientation and curve sense required')
        points = [_vector(point, 3) for point in edge['curve_samples']]
        if len(points) < 2:
            raise ValueError('Curve samples must include both endpoints')
        if not forward:
            first, last = last, first
        if forward != sense:
            points.reverse()
        oriented.append((edge_id, _identifier(edge['curve_id']), first, last, points))
    for i, (_, _, _, last, _) in enumerate(oriented):
        if last != oriented[(i + 1) % len(oriented)][2]:
            raise ValueError('Source vertex IDs do not form a closed ordered traversal')

    corners = {}
    polygon = []
    observations = []
    for edge_id, curve_id, first, last, points in oriented:
        endpoints = [_vector(vertices[key], 3) for key in (first, last)]
        endpoint_residuals = [_finite(math.dist(p, q))
                              for p, q in zip((points[0], points[-1]), endpoints)]
        if first not in corners:
            corners[first] = project(endpoints[0])
        uv, corner_residual = corners[first]
        polygon.append(uv)
        inverse_residuals = [corner_residual]
        for sample in points[1:-1]:
            uv, residual = project(sample)
            polygon.append(uv)
            inverse_residuals.append(residual)
        observations.append({'edge_id': edge_id, 'curve_id': curve_id,
                             'oriented_vertices': [first, last],
                             'endpoint_to_vertex_mm': endpoint_residuals,
                             'max_inverse_residual_mm': max(inverse_residuals)})
    validate_profile(polygon)
    endpoint_max = max(max(row['endpoint_to_vertex_mm']) for row in observations)
    inverse_max = max(row['max_inverse_residual_mm'] for row in observations)
    return {'result': 'PASS' if endpoint_max <= limits[0] and inverse_max <= limits[1] else 'FAIL',
            'face_id': face_id, 'support_id': support_id, 'uv_polygon': polygon,
            'edges': observations, 'endpoint_limit_mm': limits[0], 'inverse_limit_mm': limits[1],
            'max_endpoint_to_vertex_mm': endpoint_max, 'max_inverse_residual_mm': inverse_max,
            'scope': 'ordered source corners and sampled edge interiors on one support chart'}
