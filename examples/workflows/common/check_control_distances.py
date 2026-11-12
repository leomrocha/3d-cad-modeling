#!/usr/bin/env python3
"""Compare source-backed reference lengths with exported model point coordinates.

This helper checks supplied numbers. It does not read a CAD document or estimate
camera/scan alignment. The caller exports points from the revision being checked.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path

UNIT_TO_M = {'m': 1.0, 'cm': 0.01, 'mm': 0.001}


def number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label}: require a finite number')
    return float(value)


def unit_factor(unit):
    if unit not in UNIT_TO_M:
        raise ValueError(f'Unsupported length unit {unit!r}; use m, cm or mm')
    return UNIT_TO_M[unit]


def compare_distances(references, model, require_check_controls=False):
    scale = unit_factor(model['length_unit'])
    points = {}
    for item in model['points']:
        name = item['id']
        if not isinstance(name, str) or not name or name in points:
            raise ValueError('Point IDs must be unique nonempty strings')
        if len(item['xyz']) != 3:
            raise ValueError(f'{name}: require three coordinates')
        points[name] = tuple(number(v, name) * scale for v in item['xyz'])
    rows = []
    ids = set()
    for control in references['distances']:
        name = control['id']
        if not isinstance(name, str) or not name or name in ids:
            raise ValueError('Distance IDs must be unique nonempty strings')
        ids.add(name)
        role = control['role']
        if role not in {'fit', 'check'}:
            raise ValueError(f'{name}: role must be fit or check')
        if not isinstance(control['source'], str) or not control['source'].strip():
            raise ValueError(f'{name}: source is required')
        a, b = control['from'], control['to']
        if a == b or a not in points or b not in points:
            raise ValueError(f'{name}: require two distinct existing point IDs')
        expected = number(control['value'], name) * unit_factor(control['unit'])
        if expected <= 0:
            raise ValueError(f'{name}: reference length must be positive')
        actual = math.dist(points[a], points[b])
        residual = actual - expected
        rows.append({'id': name, 'role': role, 'source': control['source'],
                     'from': a, 'to': b, 'reference_m': expected,
                     'model_m': actual, 'signed_residual_mm': residual * 1000.0,
                     'relative_residual': residual / expected})
    if not rows:
        raise ValueError('At least one reference distance is required')
    if require_check_controls and not any(r['role'] == 'check' for r in rows):
        raise ValueError('At least one control labelled check is required')
    groups = {}
    for role in ['fit', 'check']:
        values = [r['signed_residual_mm'] for r in rows if r['role'] == role]
        if values:
            groups[role] = {'count': len(values),
                            'mean_absolute_residual_mm': sum(abs(v) for v in values) / len(values),
                            'maximum_absolute_residual_mm': max(abs(v) for v in values)}
    return {'model_revision': model['model_revision'], 'coordinate_frame': model['coordinate_frame'],
            'distances': rows, 'groups': groups,
            'meaning': 'Residuals of supplied lengths at the named model revision. Control independence is established by capture provenance.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--references', type=Path, required=True)
    parser.add_argument('--model-points', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--require-check-controls', action='store_true')
    args = parser.parse_args()
    if args.out.resolve() in {args.references.resolve(), args.model_points.resolve()}:
        parser.error('Output must preserve both input files')
    try:
        ref_bytes = args.references.read_bytes()
        model_bytes = args.model_points.read_bytes()
        report = compare_distances(json.loads(ref_bytes), json.loads(model_bytes), args.require_check_controls)
        report['inputs'] = [
            {'path': str(args.references.resolve()), 'sha256': hashlib.sha256(ref_bytes).hexdigest()},
            {'path': str(args.model_points.resolve()), 'sha256': hashlib.sha256(model_bytes).hexdigest()},
        ]
        args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    except (KeyError, ValueError, OSError, TypeError) as error:
        parser.exit(2, f'{error}\n')


if __name__ == '__main__':
    main()
