#!/usr/bin/env python3
"""Check supplied geometric measurements; does not query CAD or validate physical performance."""
import argparse
import json
import math
import sys


def number(value, label, nonnegative=False):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError(label + ' must be finite numeric data')
    if nonnegative and value < 0:
        raise ValueError(label + ' must be nonnegative')
    return float(value)


def vector(value, label):
    if not isinstance(value, list) or len(value) != 3:
        raise ValueError(label + ' must be a 3-vector')
    return tuple(number(v, label) for v in value)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.hypot(*a)


def normalized(a):
    length = norm(a)
    if length == 0 or not math.isfinite(length):
        raise ValueError('Axis/plane vector must be finite and nonzero')
    return tuple(v/length for v in a)


def run(data):
    if not isinstance(data, dict):
        raise ValueError('Contract must be an object')
    unit = data.get('length_unit')
    if not isinstance(unit, str) or not unit.strip():
        raise ValueError('An explicit length_unit is required')
    tol = data.get('tolerance', {})
    if not isinstance(tol, dict):
        raise ValueError('tolerance must be an object')
    lt = number(tol.get('length'), 'length tolerance', True)
    at = number(tol.get('angle_deg'), 'angle tolerance', True)
    if at >= 90:
        raise ValueError('Angular tolerance must be less than 90 degrees')
    observations = data.get('observations')
    checks = data.get('checks')
    if not isinstance(observations, dict) or not isinstance(checks, list) or not checks:
        raise ValueError('Named observations and nonempty checks are required')
    evidence = data.get('evidence')
    if not isinstance(evidence, dict) or evidence.get('kind') not in {
        'cad_measurement', 'declared_design', 'synthetic_fixture'}:
        raise ValueError('Evidence requires kind: cad_measurement, declared_design or synthetic_fixture')
    if not isinstance(evidence.get('source'), str) or not evidence['source'].strip():
        raise ValueError('Evidence requires a descriptive source string')
    if evidence['kind'] == 'cad_measurement':
        if any(type(evidence.get(k)) is not int for k in ('document_id', 'revision')):
            raise ValueError('CAD measurement evidence requires integer document_id and revision')
        if not isinstance(evidence.get('handles'), list) or not evidence['handles'] or any(
            not isinstance(h, str) or not h.strip() for h in evidence['handles']):
            raise ValueError('CAD measurement evidence requires nonempty source handles')

    def obj(key, kind):
        x = observations.get(key)
        if not isinstance(x, dict) or x.get('kind') != kind:
            raise ValueError(str(key) + ' must reference a ' + kind)
        origin = vector(x.get('origin'), str(key) + '.origin')
        if kind == 'point':
            return origin
        return origin, normalized(vector(x.get('direction' if kind == 'axis' else 'normal'), str(key)))

    results = []
    identities = set()
    for c in checks:
        if not isinstance(c, dict) or not isinstance(c.get('id'), str) or not c['id']:
            raise ValueError('Each check requires a nonempty id')
        if c['id'] in identities:
            raise ValueError('Duplicate check id: ' + c['id'])
        identities.add(c['id'])
        kind = c.get('kind')
        metrics = {}
        if kind in {'on_plane', 'before_plane'}:
            p = obj(c.get('point'), 'point')
            origin, n = obj(c.get('plane'), 'plane')
            distance = dot(sub(p, origin), n)
            if kind == 'on_plane':
                passed = abs(distance) <= lt
                metrics = {'absolute_distance': abs(distance), 'maximum_distance': lt}
            else:
                clearance = number(c.get('minimum_clearance'), 'minimum_clearance', True)
                passed = distance <= -clearance + lt
                metrics = {'signed_distance': distance, 'maximum_signed_distance': -clearance + lt,
                           'minimum_clearance': clearance, 'length_tolerance': lt}
        elif kind in {'parallel', 'perpendicular', 'coaxial', 'axes_intersect'}:
            p, u = obj(c.get('a'), 'axis')
            q, v = obj(c.get('b'), 'axis')
            sine = norm(cross(u, v))
            cosine = min(1.0, abs(dot(u, v)))
            angle = math.degrees(math.atan2(sine, cosine))
            metrics = {'unoriented_angle_deg': angle, 'angle_tolerance_deg': at}
            if kind == 'parallel':
                passed = angle <= at
            elif kind == 'perpendicular':
                passed = abs(90-angle) <= at
            elif kind == 'coaxial':
                # Transverse separation is meaningful only with the angular condition also checked.
                distance = norm(cross(sub(q, p), u))
                metrics.update({'origin_to_axis_distance': distance, 'length_tolerance': lt})
                passed = angle <= at and distance <= lt
            else:
                if sine == 0:
                    distance = norm(cross(sub(q, p), u))
                else:
                    distance = abs(dot(sub(q, p), cross(u, v))) / sine
                metrics.update({'infinite_axis_distance': distance, 'length_tolerance': lt})
                passed = distance <= lt
        else:
            raise ValueError('Unsupported check kind: ' + str(kind))
        if any(not math.isfinite(x) for x in metrics.values()):
            raise ValueError('Nonfinite calculated result')
        results.append({'id': c['id'], 'kind': kind, 'passed': passed, 'metrics': metrics})
    return {'all_passed': all(r['passed'] for r in results), 'length_unit': unit,
            'evidence': evidence, 'checks': results,
            'scope': 'Supplied coordinate measurements only; no OCS query, solid validation, gear-contact or physical-performance verdict'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract')
    args = parser.parse_args(argv)
    try:
        with open(args.contract, encoding='utf-8') as f:
            result = run(json.load(f))
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0 if result['all_passed'] else 1
    except (OSError, ValueError, TypeError, OverflowError) as e:
        print(json.dumps({'error': type(e).__name__, 'message': str(e)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
