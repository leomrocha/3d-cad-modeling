"""Build and check the source-dimensioned Pixhawk 6C mechanical envelope.

The official retained drawing supplies the outer dimensions and mounting
threads. This recipe represents that interface as a rectangular clearance
envelope with nominal M2 thread cylinders; it does not claim the undimensioned
case bevels, connector windows, connector internals, or material construction.
Those require a separately sourced CAD file or a recorded drawing trace.
"""
import importlib
import math

from component_records import require_ready
from feature_checks import comparison, cylinder_pattern, vertex_extrema
from rounded_tube import SelectionCheckedClient


def parameters(job):
    """Read the pinned C052 source job without choosing absent geometry."""
    require_ready(job)
    if job['part_id'] != 'C052' or job['units'] != 'mm':
        raise ValueError('Pixhawk recipe requires C052 and millimetres')
    if 'Pixhawk 6C' not in job['part_name']:
        raise ValueError('C052 Pixhawk 6C identity required')
    values = {f['name']: f['value'] for f in job['features']}
    required = {
        'case length X', 'case width Y', 'case thickness Z',
        'mount hole X pitch', 'mount hole Y pitch',
        'mount thread nominal designation', 'mount thread depth',
    }
    names = [f['name'] for f in job['features']]
    if any(names.count(name) != 1 for name in required):
        raise ValueError('Each required C052 feature name must occur exactly once')
    if not required.issubset(values):
        raise ValueError('C052 source job lacks required case or mounting features')
    numeric = required - {'mount thread nominal designation'}
    if any(isinstance(values[n], bool) or not isinstance(values[n], (int, float))
           or not math.isfinite(values[n]) or values[n] <= 0 for n in numeric):
        raise ValueError('C052 dimensions and pitches must be positive finite values')
    if values['mount thread nominal designation'] != 'M2':
        raise ValueError('Only the source-dimensioned M2 mounting thread is supported')
    if values['mount thread depth'] >= values['case thickness Z']:
        raise ValueError('Mounting thread depth must be shallower than the case envelope')
    length, width, thickness = (values[n] for n in
                                ('case length X', 'case width Y', 'case thickness Z'))
    x_pitch, y_pitch = values['mount hole X pitch'], values['mount hole Y pitch']
    nominal_thread_radius = 1.0
    if x_pitch / 2 + nominal_thread_radius > length / 2 \
            or y_pitch / 2 + nominal_thread_radius > width / 2:
        raise ValueError('Nominal M2 thread reference lies outside the source envelope')
    construction = job.get('construction')
    if not isinstance(construction, dict) or 'construction_overrun_mm' not in construction:
        raise ValueError('Explicit construction_overrun_mm is required')
    overrun = construction['construction_overrun_mm']
    if isinstance(overrun, bool) or not isinstance(overrun, (float, int)) \
            or not math.isfinite(overrun) or overrun <= 0:
        raise ValueError('Positive finite construction_overrun_mm is required')
    if values['mount thread depth'] + overrun > thickness:
        raise ValueError('M2 reference cut overrun exceeds the sourced envelope thickness')
    values['construction_overrun_mm'] = overrun
    return values


def geometry(client):
    return importlib.import_module('cadtools.geometry').Geometry(SelectionCheckedClient(client))


def build_envelope(client, job):
    """Build the dimension envelope and four nominal M2 mounting references.

    The 2.0 mm cylinders are nominal thread references, not a modeled thread
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
    body = g.extrude('C052 Pixhawk 6C source-dimension envelope', profile, 0, thickness)
    x_pitch, y_pitch = p['mount hole X pitch'], p['mount hole Y pitch']
    overrun = p['construction_overrun_mm']
    cutters = [g.cylinder(f'C052 nominal M2 mounting thread {i}',
                          [sx * x_pitch / 2, sy * y_pitch / 2, -overrun],
                          1.0, p['mount thread depth'] + overrun)
               for i, (sx, sy) in enumerate(((-1, -1), (-1, 1), (1, -1), (1, 1)), 1)]
    solid = g.subtract('C052 source-dimension envelope with four M2 mounting references',
                       body, cutters)
    g.metadata('C052 source provenance', [solid], [
        job['part_name'],
        'Dimension envelope with four nominal M2 mounting-thread reference cylinders',
        job['frame'],
        'Manufacturer dimensions: 84.8 x 44 x 12.4 mm; hole pitch 60 x 32 mm; thread depth 6 mm',
        'Connector windows, bevels, case material and internal details are not represented by this envelope',
        'Source job: ' + job['job_id'],
    ])
    return solid


def verify(features, job, tolerance=1e-7):
    """Check native envelope extrema and M2 thread-reference locations."""
    p = parameters(job)
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Positive finite CAD readback tolerance required')
    case = features['case']
    checks = [vertex_extrema(
        'C052 case-envelope XYZ extrema', case,
        [[-p['case length X'] / 2, p['case length X'] / 2],
         [-p['case width Y'] / 2, p['case width Y'] / 2],
         [0, p['case thickness Z']]], tolerance)]
    expected = [[x, y] for x in (-p['mount hole X pitch'] / 2,
                                  p['mount hole X pitch'] / 2)
                        for y in (-p['mount hole Y pitch'] / 2,
                                   p['mount hole Y pitch'] / 2)]
    checks.append(cylinder_pattern('Four nominal M2 thread-reference axes', case,
                                   2.0, 2, expected, tolerance))
    bottoms = sorted([plane['origin'][:2] for plane in case['planes']
                      if abs(abs(plane['normal'][2]) - 1) <= tolerance
                      and abs(plane['origin'][2] - p['mount thread depth']) <= tolerance])
    checks.append(comparison('Four M2 blind-thread bottom planes', bottoms,
                             sorted(expected), tolerance,
                             method='native planar bottom faces at source thread depth'))
    if 'topology' in case:
        from feature_checks import closed_body
        checks.append(closed_body('C052 envelope is one closed connected body', case))
    return {
        'result': 'PASS' if all(check['result'] == 'PASS' for check in checks) else 'FAIL',
        'method': 'native surface equations, planar hole bottoms and vertex extrema',
        'numeric_tolerance_mm': tolerance,
        'source_dimensional_tolerances_mm': {
            'case length': 0.1, 'case width': 0.1, 'case thickness': 0.1,
            'mount hole pitches': 0.1,
        },
        'checks': checks,
        'scope': 'source-defined C052 dimension envelope and nominal M2 mounting references',
        'representation': 'rectangular clearance envelope; detailed outer case and connectors excluded',
    }


def inspect(client, handles, job):
    """Read actual OCS surface records and run independent source-bound checks."""
    from native_acis import sab_features
    from rounded_tube import sat_features

    if set(handles) != {'case'}:
        raise ValueError("C052 envelope inspection expects one named handle: 'case'")
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
