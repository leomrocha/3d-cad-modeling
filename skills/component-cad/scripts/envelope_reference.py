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
    envelope_scope = job.get('envelope_scope')
    if envelope_scope is not None and (
            not isinstance(envelope_scope, str) or not envelope_scope.strip()):
        raise ValueError('envelope_scope must be a nonempty string when supplied')
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
    axis_datums = job.get('axis_datums')
    if axis_datums is not None:
        if not isinstance(axis_datums, dict) or set(axis_datums) != {'x', 'y', 'z'}:
            raise ValueError('axis_datums must map x, y and z when supplied')
        normalized_datums = {}
        for axis in ('x', 'y', 'z'):
            datum = axis_datums[axis]
            if not isinstance(datum, dict) or set(datum) != {'feature', 'datum'}:
                raise ValueError('Each axis datum must contain exactly feature and datum')
            feature_name, description = datum['feature'], datum['datum']
            if not isinstance(feature_name, str) or not feature_name.strip() \
                    or feature_name != axis_features[axis]:
                raise ValueError('Axis datum feature must match dimension_features for ' + axis)
            if not isinstance(description, str) or not description.strip():
                raise ValueError('Axis datum description must be nonempty for ' + axis)
            normalized_datums[axis] = {'feature': feature_name, 'datum': description}
        axis_datums = normalized_datums
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
            'tolerance': float(tolerance), 'envelope_scope': envelope_scope,
            'axis_datums': axis_datums}


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
    metadata = [
        job['part_name'], job['representation'],
        'Reference envelope; units ' + job['units'],
        'Local frame: ' + job['local_frame'],
        'Source job: ' + job['job_id'],
    ]
    if p['envelope_scope'] is not None:
        metadata.append('Envelope scope: ' + p['envelope_scope'])
    if p['axis_datums'] is not None:
        for axis in ('x', 'y', 'z'):
            datum = p['axis_datums'][axis]
            metadata.append('Axis datum ' + axis.upper() + ' (source feature "'
                            + datum['feature'] + '"): ' + datum['datum'])
    g.metadata(job['geometry_name'] + ' source metadata', [solid], metadata)
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
    result = {'result': 'PASS' if all(c['result'] == 'PASS' for c in checks) else 'FAIL',
            'method': 'native vertex extrema; closed-body topology when available',
            'numeric_tolerance_mm': p['tolerance'],
            'source_measurements': {axis: dims[axis] for axis in ('x', 'y', 'z')},
            'representation': job['representation'], 'checks': checks}
    if p['envelope_scope'] is not None:
        result['envelope_scope'] = p['envelope_scope']
    if p['axis_datums'] is not None:
        result['axis_datums'] = p['axis_datums']
    return result


def inspect(client, handles, job):
    """Read one solid's SAT/SAB feature points and run the source-bound check."""
    if set(handles) != {'envelope'}:
        raise ValueError("Envelope inspection requires one handle named 'envelope'")
    expected_document = getattr(client, 'document_id', None)
    if expected_document is None:
        raise ValueError('Client must be bound to an explicit document_id')
    before = client.read('state')
    if before.get('document_id') != expected_document:
        raise ValueError('Active document differs from the bound client document')
    before_geometry_revision = before.get('geometry_revision')
    if before_geometry_revision is None:
        raise ValueError('Pre-read state has no geometry_revision')
    before_revision = before.get('revision')
    if before_revision is None:
        raise ValueError('Pre-read state has no document revision')
    response = client.read('records', collection='entities',
                           handles=[handles['envelope']], limit=1)
    records = response.get('records', [])
    if len(records) != 1:
        raise ValueError('Expected exactly one envelope solid record')
    record = records[0]
    if record.get('handle') != handles['envelope']:
        raise ValueError('Native record handle differs from requested envelope handle')
    if record.get('type') != 'Solid3D':
        raise ValueError('Native envelope record must have type Solid3D')
    if response.get('document_id') not in (None, expected_document):
        raise ValueError('Native record response belongs to a different document')
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
    after = client.read('state')
    if after.get('document_id') != expected_document:
        raise ValueError('Active document changed during envelope inspection')
    after_geometry_revision = after.get('geometry_revision')
    if after_geometry_revision != before_geometry_revision:
        raise ValueError('Geometry revision changed during envelope inspection')
    after_revision = after.get('revision')
    if after_revision != before_revision:
        raise ValueError('Document revision changed during envelope inspection')
    for label, source in (('record response', response), ('record', record)):
        response_document = source.get('document_id')
        if response_document not in (None, expected_document):
            raise ValueError(label + ' belongs to a different document')
        response_geometry_revision = source.get('geometry_revision')
        if response_geometry_revision not in (None, before_geometry_revision):
            raise ValueError(label + ' geometry_revision differs from active state')
    result = verify(features, job)
    result.update(document_id=expected_document,
                  document_revision=after_revision,
                  geometry_revision=after_geometry_revision,
                  handle=handles['envelope'], encoding=encoding, features=features)
    return response, result
