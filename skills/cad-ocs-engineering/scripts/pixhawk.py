"""Source-bound rectangular mounting envelopes; legacy module name retained for callers."""
import importlib
import math
import re

from component_records import require_ready
from feature_checks import comparison, cylinder_pattern, vertex_extrema
from rounded_tube import SelectionCheckedClient


def parameters(job):
    """Read the pinned Mounting source job without choosing absent geometry."""
    require_ready(job)
    if job['units'] != 'mm':
        raise ValueError('Mounting envelope requires millimetres')
    values = {f['name']: f['value'] for f in job['features']}
    required = {
        'case length X', 'case width Y', 'case thickness Z',
        'mount hole X pitch', 'mount hole Y pitch',
        'mount thread nominal designation', 'mount thread depth',
    }
    names = [f['name'] for f in job['features']]
    if any(names.count(name) != 1 for name in required):
        raise ValueError('Each required Mounting feature name must occur exactly once')
    if not required.issubset(values):
        raise ValueError('Mounting source job lacks required case or mounting features')
    numeric = required - {'mount thread nominal designation'}
    if any(isinstance(values[n], bool) or not isinstance(values[n], (int, float))
           or not math.isfinite(values[n]) or values[n] <= 0 for n in numeric):
        raise ValueError('Mounting dimensions and pitches must be positive finite values')
    match=re.fullmatch(r'M([0-9]+(?:\.[0-9]+)?)',values['mount thread nominal designation'])
    if not match or float(match[1])<=0:raise ValueError('Nominal metric diameter designation required')
    values['nominal_thread_diameter']=float(match[1])
    if values['mount thread depth'] >= values['case thickness Z']:
        raise ValueError('Mounting thread depth must be shallower than the case envelope')
    length, width, thickness = (values[n] for n in
                                ('case length X', 'case width Y', 'case thickness Z'))
    x_pitch, y_pitch = values['mount hole X pitch'], values['mount hole Y pitch']
    nominal_thread_radius = values['nominal_thread_diameter']/2
    if x_pitch / 2 + nominal_thread_radius > length / 2 \
            or y_pitch / 2 + nominal_thread_radius > width / 2:
        raise ValueError('Nominal metric thread reference lies outside the source envelope')
    construction = job.get('construction')
    if not isinstance(construction, dict) or 'construction_overrun_mm' not in construction:
        raise ValueError('Explicit construction_overrun_mm is required')
    overrun = construction['construction_overrun_mm']
    if isinstance(overrun, bool) or not isinstance(overrun, (float, int)) \
            or not math.isfinite(overrun) or overrun <= 0:
        raise ValueError('Positive finite construction_overrun_mm is required')
    if values['mount thread depth'] + overrun > thickness:
        raise ValueError('metric reference cut overrun exceeds the sourced envelope thickness')
    values['construction_overrun_mm'] = overrun
    return values


def geometry(client):
    return importlib.import_module('cadtools.geometry').Geometry(SelectionCheckedClient(client))


def build_envelope(client, job):
    """Build the dimension envelope and four nominal metric mounting references.

    The source-designation cylinders are nominal thread references, not a modeled thread
    profile or a manufacturing tap-drill diameter. The case envelope is not
    the detailed exterior housing surface.
    """
    p = parameters(job)
    g = geometry(client)
    length, width, thickness = (p[n] for n in
                                ('case length X', 'case width Y', 'case thickness Z'))
    half_x, half_y = length / 2, width / 2
    profile = [[-half_x, -half_y], [half_x, -half_y],
               [half_x, half_y], [-half_x, half_y]]
    body = g.extrude('Mounting source-dimension envelope', profile, 0, thickness)
    x_pitch, y_pitch = p['mount hole X pitch'], p['mount hole Y pitch']
    overrun = p['construction_overrun_mm']
    cutters = [g.cylinder(f'Mounting nominal metric mounting thread {i}',
                          [sx * x_pitch / 2, sy * y_pitch / 2, -overrun],
                          p['nominal_thread_diameter']/2, p['mount thread depth'] + overrun)
               for i, (sx, sy) in enumerate(((-1, -1), (-1, 1), (1, -1), (1, 1)), 1)]
    solid = g.subtract('Mounting source-dimension envelope with four metric mounting references',
                       body, cutters)
    g.metadata('Mounting source provenance', [solid], [
        job['part_name'],
        'Dimension envelope with four nominal metric mounting-thread reference cylinders',
        job['frame'],
        'Envelope XYZ mm '+str([length,width,thickness])+'; mounting pitch mm '+str([x_pitch,y_pitch])+'; depth mm '+str(p['mount thread depth']),
        'Connector windows, bevels, case material and internal details are not represented by this envelope',
        'Source job: ' + job['job_id'],
    ])
    return solid


def verify(features, job, tolerance=1e-7):
    """Check native envelope extrema and metric thread-reference locations."""
    p = parameters(job)
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Positive finite CAD readback tolerance required')
    case = features['case']
    checks = [vertex_extrema(
        'Mounting case-envelope XYZ extrema', case,
        [[-p['case length X'] / 2, p['case length X'] / 2],
         [-p['case width Y'] / 2, p['case width Y'] / 2],
         [0, p['case thickness Z']]], tolerance)]
    expected = [[x, y] for x in (-p['mount hole X pitch'] / 2,
                                  p['mount hole X pitch'] / 2)
                        for y in (-p['mount hole Y pitch'] / 2,
                                   p['mount hole Y pitch'] / 2)]
    checks.append(cylinder_pattern('Four nominal metric thread-reference axes', case,
                                   p['nominal_thread_diameter'], 2, expected, tolerance))
    bottoms = sorted([plane['origin'][:2] for plane in case['planes']
                      if abs(abs(plane['normal'][2]) - 1) <= tolerance
                      and abs(plane['origin'][2] - p['mount thread depth']) <= tolerance])
    checks.append(comparison('Four metric blind-thread bottom planes', bottoms,
                             sorted(expected), tolerance,
                             method='native planar bottom faces at source thread depth'))
    if 'topology' in case:
        from feature_checks import closed_body
        checks.append(closed_body('Mounting envelope is one closed connected body', case))
    return {
        'result': 'PASS' if all(check['result'] == 'PASS' for check in checks) else 'FAIL',
        'method': 'native surface equations, planar hole bottoms and vertex extrema',
        'numeric_tolerance_mm': tolerance,
        'source_dimensional_tolerances_mm': job.get('source_dimensional_tolerances_mm',{}),
        'checks': checks,
        'scope': 'source-defined Mounting dimension envelope and nominal metric mounting references',
        'representation': 'rectangular clearance envelope; detailed outer case and connectors excluded',
    }


def inspect(client, handles, job):
    """Read actual OCS surface records and run independent source-bound checks."""
    from native_acis import sab_features
    from rounded_tube import sat_features

    if set(handles) != {'case'}:
        raise ValueError("Mounting envelope inspection expects one named handle: 'case'")
    records = client.read('records', collection='entities', handles=list(handles.values()),
                          limit=len(handles))
    by_handle = {record['handle']: record for record in records['records']}
    record = by_handle[handles['case']]
    acis = record['properties']['acis_data']
    parsed = sat_features(acis['sat_data']) if acis['sat_data'] else sab_features(
        bytes(acis['sab_data']))
    result = verify({'case': parsed}, job)
    result.update(document_id=records.get('document_id'),
                  revision=records.get('revision'),
                  geometry_revision=records.get('geometry_revision'),
                  handles=handles)
    return records, result
