"""Bounded rational B-spline evaluation from exact binary64 inputs.

Local nonzero bases and the caller affine transform are evaluated in Decimal;
only final coordinates are rounded to float. Agreement at two precisions is a
numerical convergence observation, not an analytic error certificate.
"""
from bisect import bisect_right
from collections import Counter
from decimal import Decimal, localcontext
import math


def _number(x):
    if type(x) not in (int, float) or not math.isfinite(x):
        raise ValueError('Finite binary64 input required')
    return Decimal.from_float(float(x))


def _knots(values, degree, count):
    if type(degree) is not int or not 1 <= degree <= 25 or count <= degree:
        raise ValueError('Supported degree and sufficient controls required')
    result = [_number(v) for v in values]
    if len(result) != count + degree + 1 or result != sorted(result):
        raise ValueError('Ordered expanded knot vector required')
    if result[degree] >= result[count]:
        raise ValueError('Positive knot domain required')
    if any(count > degree + 1 for count in Counter(result).values()):
        raise ValueError('Knot multiplicity exceeds degree plus one')
    return result


def _basis(knots, degree, x):
    span = max(degree, min(len(knots)-degree-2, bisect_right(knots, x)-1))
    basis = [Decimal(1)] + [Decimal(0)]*degree
    left = [Decimal(0)]*(degree+1); right = left.copy()
    for j in range(1, degree+1):
        left[j] = x-knots[span+1-j]; right[j] = knots[span+j]-x
        saved = Decimal(0)
        for r in range(j):
            denominator = right[r+1]+left[j-r]
            if denominator == 0:
                raise ValueError('Unsupported zero basis denominator')
            value = basis[r]/denominator
            basis[r] = saved+right[r+1]*value; saved = left[j-r]*value
        basis[j] = saved
    return list(range(span-degree, span+1)), basis


def evaluate_rational_surface(surface, uv, *, transform, precisions,
                              parameter_bounds=((0, 1), (0, 1))):
    """Evaluate normalized UV with explicit precision pair and permitted bounds.

    Surface fields: control_points[u][v][xyz], weights[u][v], degree_u,
    degree_v, knots_u, knots_v (expanded). Weights must be positive. A caller
    may explicitly permit bounded polynomial extension beyond normalized [0,1].
    """
    if len(precisions) != 2 or any(type(p) is not int or not 32 <= p <= 500 for p in precisions) or precisions[0] >= precisions[1]:
        raise ValueError('Increasing precision pair from 32 to 500 digits required')
    points = surface['control_points']; weights = surface['weights']
    nu = len(points); nv = len(points[0]) if nu else 0
    if not nu or not nv or nu*nv > 100000 or any(len(row) != nv for row in points):
        raise ValueError('Bounded rectangular control grid required')
    if len(weights) != nu or any(len(row) != nv for row in weights):
        raise ValueError('Weight grid must match controls')
    p = []
    for row in points:
        column = []
        for xyz in row:
            if len(xyz) != 3: raise ValueError('Control point triple required')
            column.append([_number(x) for x in xyz])
        p.append(column)
    w = [[_number(x) for x in row] for row in weights]
    if any(x <= 0 for row in w for x in row): raise ValueError('Positive rational weights required')
    du, dv = surface['degree_u'], surface['degree_v']
    tu = _knots(surface['knots_u'], du, nu); tv = _knots(surface['knots_v'], dv, nv)
    if len(transform) != 4 or any(len(row) != 4 for row in transform) or list(transform[3]) != [0,0,0,1]:
        raise ValueError('Affine 4x4 transform required')
    matrix = [[_number(x) for x in row] for row in transform]
    if len(uv) != 2 or len(parameter_bounds) != 2 or any(len(b) != 2 for b in parameter_bounds):
        raise ValueError('UV pair and two bounded parameter intervals required')
    q = [_number(x) for x in uv]; bounds = [[_number(x) for x in b] for b in parameter_bounds]
    if any(a > b or not a <= x <= b for x,(a,b) in zip(q,bounds)):
        raise ValueError('UV lies outside caller-permitted bounds')
    values = []
    for precision in precisions:
        with localcontext() as context:
            context.prec = precision
            u = tu[du]+q[0]*(tu[nu]-tu[du]); v = tv[dv]+q[1]*(tv[nv]-tv[dv])
            iu, bu = _basis(tu,du,u); iv, bv = _basis(tv,dv,v)
            terms = [(i,j,a*b*w[i][j]) for i,a in zip(iu,bu) for j,b in zip(iv,bv)]
            denominator = sum(t for i,j,t in terms)
            if denominator <= 0: raise ValueError('Nonpositive rational denominator')
            xyz = [sum(t*p[i][j][c] for i,j,t in terms)/denominator for c in range(3)]
            values.append([sum(matrix[c][k]*xyz[k] for k in range(3))+matrix[c][3] for c in range(3)])
    rounded = [[float(x) for x in row] for row in values]
    if any(not math.isfinite(x) for row in rounded for x in row): raise ValueError('Final float64 overflow')
    with localcontext() as context:
        context.prec = precisions[-1]+10
        difference = max(abs(a-b) for a,b in zip(*values))
        rounding_error = sum((Decimal.from_float(x)-y)**2 for x,y in zip(rounded[-1],values[-1])).sqrt()
    return dict(result='PASS' if rounded[0] == rounded[1] else 'PRECISION_DISAGREEMENT',
                point=rounded[-1], reference=[str(x) for x in values[-1]], precisions=list(precisions),
                precision_difference=str(difference), rounding_error_norm=str(rounding_error),
                method='local rational basis; affine transform before final binary64 rounding',
                scope='two-precision numerical agreement on caller binary64 inputs')
