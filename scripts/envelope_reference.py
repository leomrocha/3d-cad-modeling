"""Build and inspect a source-dimensioned axis-aligned reference envelope.

This creates a clearance/product-envelope reference volume, not detailed body
geometry. Inputs and source provenance are supplied by an external component
job. Supported units are millimetres and the local construction frame is XY
profile with +Z extrusion.
"""
import importlib
import math

from component_records import require_ready
from feature_checks import closed_body, vertex_extrema
from step_placements import identity_sat_vertices


def parameters(job):
    """Validate all source/job geometry values before any native write."""
    require_ready(job)
    if job['units'] != 'mm':
        raise ValueError('Envelope reference helper supports millimetres only')
    if job.get('geometry_role') != 'reference_envelope':
        raise ValueError('Explicit geometry_role=reference_envelope is required')
    if not isinstance(job.get('local_frame'), str) or not job['local_frame'].strip():
        raise ValueError('Explicit local_frame description is required')
    if not isinstance(job.get('geometry_name'), str) or not job['geometry_name'].strip():
        raise ValueError('Explicit readable geometry_name is required')
    axis_features = job.get('dimension_features')
    if not isinstance(axis_features, dict) or set(axis_features) != {'x', 'y', 'z'}:
        raise ValueError('dimension_features must map x, y and z to source feature names')
    names = list(axis_features.values())
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError('Each envelope axis needs a readable source feature name')
    if len(set(names)) != 3:
        raise ValueError('Envelope axes must use three distinct source features')
    by_name = {feature['name']: feature for feature in job['features']}
    dimensions = {}
    for axis, name in axis_features.items():
        if name not in by_name:
            raise ValueError('Missing required source feature for axis ' + axis)
        feature = by_name[name]
        value = feature.get('value')
        if feature.get('required') is not True:
            raise ValueError('Envelope dimension must be a required source feature: ' + name)
        if feature.get('unit') != job['units']:
            raise ValueError('Envelope dimension units must match job units: ' + name)
        if isinstance(value, bool) or not isinstance(value, (int, float)) \
                or not math.isfinite(value) or value <= 0:
            raise ValueError('Positive finite envelope dimension required: ' + name)
        dimensions[axis] = float(value)
    origin = job.get('origin')
    if not isinstance(origin, (list, tuple)) or len(origin) != 3 \
            or any(isinstance(v, bool) or not isinstance(v, (int, float))
                   or not math.isfinite(v) for v in origin):
        raise ValueError('Finite three-coordinate envelope origin required')
    tolerance = job.get('readback_tolerance', 1e-7)
    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)) \
            or not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Positive finite readback_tolerance required')
    return {'dimensions': dimensions, 'origin': [float(v) for v in origin],
            'tolerance': float(tolerance)}


def geometry(client):
    """Use the installed OCS Geometry adapter through its selection guard."""
    from rounded_tube import SelectionCheckedClient
    Geometry = importlib.import_module('cadtools.geometry').Geometry
    return Geometry(SelectionCheckedClient(client))


def build_envelope(client, job):
    """Create one explicitly named reference-envelope solid after full preflight."""
    p = parameters(job)
    dims, origin = p['dimensions'], p['origin']
    x, y, z = origin
    dx, dy, dz = dims['x'], dims['y'], dims['z']
    profile = [[x, y], [x + dx, y], [x + dx, y + dy], [x, y + dy]]
    g = geometry(client)
    solid = g.extrude(job['geometry_name'], profile, z, dz)
    g.metadata(job['geometry_name'] + ' source metadata', [solid], [
        job['part_name'], job['representation'],
        'Reference envelope; units ' + job['units'],
        'Local frame: ' + job['local_frame'],
        'Source job: ' + job['job_id'],
    ])
    return solid


def verify(features, job):
    """Compare native vertex extrema with source job envelope extents."""
    p = parameters(job)
    origin, dims = p['origin'], p['dimensions']
    expected = [[origin[i], origin[i] + dims[axis]]
                for i, axis in enumerate(('x', 'y', 'z'))]
    checks = [vertex_extrema('Source reference-envelope XYZ extrema', features,
                             expected, p['tolerance'])]
    if 'topology' in features:
        checks.append(closed_body('Reference envelope is one closed connected body',
                                  features))
    return {'result': 'PASS' if all(c['result'] == 'PASS' for c in checks) else 'FAIL',
            'method': 'native vertex extrema; closed-body topology when available',
            'numeric_tolerance_mm': p['tolerance'],
            'source_measurements': {axis: dims[axis] for axis in ('x', 'y', 'z')},
            'representation': job['representation'], 'checks': checks}


def inspect(client, handles, job):
    """Read one solid's SAT/SAB feature points and run the source-bound check."""
    if set(handles) != {'envelope'}:
        raise ValueError("Envelope inspection requires one handle named 'envelope'")
    response = client.read('records', collection='entities',
                           handles=[handles['envelope']], limit=1)
    records = response.get('records', [])
    if len(records) != 1:
        raise ValueError('Expected exactly one envelope solid record')
    acis = records[0]['properties']['acis_data']
    sat = acis.get('sat_data')
    if sat:
        features = {'points': identity_sat_vertices(sat)}
        encoding = 'SAT point records'
    else:
        sab = acis.get('sab_data')
        if not sab:
            raise ValueError('Native envelope SAT/SAB data is absent')
        from native_acis import sab_features
        features = sab_features(bytes(sab), allow_rigid=True)
        encoding = 'SAB native body graph'
    result = verify(features, job)
    result.update(document_id=response.get('document_id'),
                  revision=response.get('revision'),
                  geometry_revision=response.get('geometry_revision'),
                  handle=handles['envelope'], encoding=encoding, features=features)
    return response, result
