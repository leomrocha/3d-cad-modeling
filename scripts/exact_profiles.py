"""Compare complete source Line/Arc/clamped-NURBS loops in a caller's planar frame.

Coordinates and length_tolerance use caller-declared length units. Knot and
weight tolerances are dimensionless. This checks representation preservation;
material nesting and kernel acceptance require separate evidence.
"""
import math
from cadtools.geometry import finite, vector


def _positive(value):
    if finite(value) <= 0:
        raise ValueError('Positive tolerance required')
    return value


def normalized_knots(knots):
    values = [finite(v) for v in knots]
    if len(values) < 2 or values[-1] <= values[0] or any(a > b for a, b in zip(values, values[1:])):
        raise ValueError('Nondecreasing knots with nonzero domain required')
    return [(v-values[0])/(values[-1]-values[0]) for v in values]


def validate_edge(edge):
    kind = edge['kind']
    if kind in ('Line', 'Arc'):
        a, b = vector(edge['start'], 2), vector(edge['end'], 2)
        if kind == 'Line' and a == b:
            raise ValueError('Collapsed Line needs a separate source binding')
        if kind == 'Arc':
            c = vector(edge['center'], 2); sweep = finite(edge['sweep'])
            radius = math.dist(a, c)
            if radius <= 0 or not 0 < abs(sweep) <= 2*math.pi:
                raise ValueError('Nonzero exact circular arc required')
            end = [c[0]+(a[0]-c[0])*math.cos(sweep)-(a[1]-c[1])*math.sin(sweep),
                   c[1]+(a[0]-c[0])*math.sin(sweep)+(a[1]-c[1])*math.cos(sweep)]
            # Input consistency is checked by the caller's numerical tolerance below.
            return a, b, math.dist(end, b)
        return a, b, 0.
    if kind != 'NURBS':
        raise ValueError('Exact Line, Arc or NURBS required; sampled fallback rejected')
    degree = edge['degree']; points = [vector(p, 2) for p in edge['control_points']]
    weights = [finite(w) for w in edge['weights']]; knots = normalized_knots(edge['knots'])
    if (type(degree) is not int or degree < 1 or len(points) <= degree
            or len(weights) != len(points) or any(w <= 0 for w in weights)
            or len(knots) != len(points)+degree+1 or edge.get('periodic') is not False
            or edge.get('fit_points') != []):
        raise ValueError('Complete nonperiodic control net, positive weights and no fit fallback required')
    if knots[:degree+1] != [0.]*(degree+1) or knots[-degree-1:] != [1.]*(degree+1):
        raise ValueError('Clamped NURBS required by this endpoint adapter')
    if any(knots.count(k) > degree for k in set(knots) - {0., 1.}):
        raise ValueError('Interior knot multiplicity exceeds degree')
    return points[0], points[-1], 0.


def reversed_edge(edge):
    validate_edge(edge)
    result = dict(edge)
    if edge['kind'] == 'NURBS':
        result.update(control_points=list(reversed(edge['control_points'])),
                      weights=list(reversed(edge['weights'])),
                      knots=[1-v for v in reversed(normalized_knots(edge['knots']))])
    else:
        result.update(start=edge['end'], end=edge['start'])
        if edge['kind'] == 'Arc': result['sweep'] = -edge['sweep']
    return result


def edge_equal(source, observed, *, length_tolerance, parameter_tolerance):
    lt, pt = _positive(length_tolerance), _positive(parameter_tolerance)
    for e in (source, observed):
        if validate_edge(e)[2] > lt:
            raise ValueError('Arc endpoint contradicts center and sweep')
    if source['kind'] != observed['kind']: return False
    def points(a, b):
        return len(a) == len(b) and all(math.dist(x, y) <= lt for x, y in zip(a, b))
    if source['kind'] == 'NURBS':
        a, b = normalized_knots(source['knots']), normalized_knots(observed['knots'])
        return (source['degree'] == observed['degree']
                and points(source['control_points'], observed['control_points'])
                and len(a) == len(b) and all(abs(x-y) <= pt for x, y in zip(a, b))
                and all(abs(x-y) <= pt for x, y in zip(source['weights'], observed['weights'])))
    match = points([source['start'], source['end']], [observed['start'], observed['end']])
    if source['kind'] == 'Arc':
        match = match and math.dist(source['center'], observed['center']) <= lt and abs(source['sweep']-observed['sweep']) <= pt
    return match


def compare_loops(source, observed, *, length_tolerance, parameter_tolerance):
    """Require a unique bijection of whole cyclic loops; allow whole-loop reversal.

    Each loop is {role: caller-classified material boundary role, edges: [...] }.
    Matching complete ordered loops prevents same-count edge regrouping passes.
    """
    lt = _positive(length_tolerance); _positive(parameter_tolerance)
    for loops in (source, observed):
        if not loops: raise ValueError('Nonempty loop set required')
        for loop in loops:
            edges = loop['edges']
            if not edges or not isinstance(loop.get('role'), str) or not loop['role']:
                raise ValueError('Explicit boundary role and complete edges required')
            ends = [validate_edge(e) for e in edges]
            if any(v[2] > lt for v in ends) or any(math.dist(a[1], b[0]) > lt for a, b in zip(ends, ends[1:]+ends[:1])):
                raise ValueError('Loop is open or has inconsistent arc endpoints')
    bindings = []
    for i, loop in enumerate(source):
        hits = []
        for j, other in enumerate(observed):
            if loop['role'] != other['role'] or len(loop['edges']) != len(other['edges']): continue
            for reverse in (False, True):
                edges = other['edges'] if not reverse else [reversed_edge(e) for e in reversed(other['edges'])]
                for shift in range(len(edges)):
                    ordered = edges[shift:]+edges[:shift]
                    if all(edge_equal(a,b,length_tolerance=lt,parameter_tolerance=parameter_tolerance) for a,b in zip(loop['edges'],ordered)):
                        hits.append(dict(source_loop=i, observed_loop=j, reversed=reverse, cyclic_shift=shift))
        if len(hits) != 1:
            return dict(result='FAIL', reason='Missing or ambiguous ordered loop match', source_loop=i, candidates=hits)
        bindings.append(hits[0])
    passed = len(source) == len(observed) and len({v['observed_loop'] for v in bindings}) == len(observed)
    return dict(result='PASS' if passed else 'FAIL', bindings=bindings, method='complete ordered curves, control nets, knots and roles')


def signed_extrusion(normal, displacement, *, angular_tolerance):
    """Compute signed height from an observed Region normal and source displacement."""
    tolerance = _positive(angular_tolerance)
    n, d = vector(normal), vector(displacement)
    norm = math.sqrt(sum(x*x for x in n)); depth = math.sqrt(sum(x*x for x in d))
    if norm == 0 or depth == 0: raise ValueError('Nonzero normal and source displacement required')
    n = [x/norm for x in n]; projection = sum(a*b for a,b in zip(n,d))
    if math.dist(d,[projection*x for x in n])/depth > tolerance:
        raise ValueError('Source displacement is not parallel to Region normal')
    return projection
