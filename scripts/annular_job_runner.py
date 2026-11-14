#!/usr/bin/env python3
"""Run a caller-supplied, source-bound annular reference job.

The JSON job supplies all part identity, dimensions, source claims and frame
data. Paths, model indexes, OCS session and execution-model identity are
explicit caller inputs. The default command performs preflight only; native
mutations require ``--allow-write``.
"""
import argparse
import base64
import copy
import hashlib
import importlib
import json
import math
from pathlib import Path
import sys

from envelope_job_runner import (
    RecoveringClient, check_audit, check_write_targets, cleanup_completed_envelope,
    document_snapshot, parse_roots, portableize, resolve_locator, sab_reader_preflight,
    sha256, source_locator, validate_save_receipt, write_json,
)


def resolve_job(job_path, roots):
    """Pin all feature sources and validate annular inputs before OCS access."""
    from component_records import readiness
    from annular_reference import parameters

    path = Path(job_path).resolve()
    original = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(original, dict):
        raise ValueError('External annular job must be a JSON object')
    namespace = original.get('namespace')
    if not isinstance(namespace, str) or not namespace.strip() \
            or len(namespace.encode('utf-8')) > 64:
        raise ValueError('External annular job requires a 1..64 byte request namespace')
    part_id = original.get('part_id')
    if not isinstance(part_id, str) or not part_id.strip():
        raise ValueError('External annular job requires a readable part_id')
    runtime = copy.deepcopy(original)
    portable_features = copy.deepcopy(original.get('features'))
    if not isinstance(runtime.get('features'), list) or not runtime['features']:
        raise ValueError('External annular job requires source-pinned feature records')
    resolved_sources = []
    for index, feature in enumerate(runtime['features']):
        if not isinstance(feature, dict) or not isinstance(feature.get('source'), str):
            raise ValueError('Every annular source feature needs an explicit source locator')
        resolved = resolve_locator(feature['source'], roots, path.parent)
        if not resolved.is_file():
            raise FileNotFoundError('Pinned feature source is missing: ' + str(resolved))
        feature['source'] = str(resolved)
        portable_features[index]['source'] = source_locator(resolved, roots)
        resolved_sources.append(source_locator(resolved, roots))
    runtime['_portable_features'] = portable_features
    readiness_result = readiness(runtime)
    if readiness_result.get('state') != 'SOURCE_READY':
        raise ValueError('Annular construction requires SOURCE_READY; observed '
                         + str(readiness_result.get('state')))
    params = parameters(runtime)
    validate_request_labels(runtime)
    return {
        'job': runtime,
        'readiness': readiness_result,
        'parameters': params,
        'resolved_sources': sorted(set(resolved_sources)),
        'source_job_sha256': sha256(path),
        'source_job_locator': source_locator(path, roots),
    }


def verify_source_pins(prepared):
    """Recheck the source-job and feature hashes immediately before native writes."""
    job = prepared['job']
    source_job = resolve_locator(prepared['source_job_locator'], prepared['roots'])
    if sha256(source_job) != prepared['source_job_sha256']:
        raise ValueError('Source-job JSON changed after preflight')
    for feature in job['features']:
        source = Path(feature['source'])
        if sha256(source) != feature['source_sha256']:
            raise ValueError('Pinned feature source changed after preflight: ' + str(source))


def validate_request_labels(job):
    """Check generated annular mutation identities before creating a document."""
    namespace = job['namespace']
    labels = [
        'create-isolated-document', 'units-millimetres', 'world-ucs',
        'capture-pre-save-viewport', job['metadata_request_label'],
        job['geometry_name'] + ' outside cylinder',
        job['geometry_name'] + ' through-bore cutter',
    ]
    subtraction = job['geometry_name'] + ' annular solid'
    labels.extend(subtraction + '-' + suffix for suffix in (
        'clear', 'start', 'base', 'base-pick', 'base-end', 'tools', 'tools-pick', 'end'))
    labels.extend(('verified-save', 'reopen'))
    too_long = [label for label in labels
                if len((namespace + ':' + label).encode('utf-8')) > 128]
    if too_long:
        raise ValueError('Namespace and generated annular labels exceed 128 UTF-8 bytes: '
                         + ', '.join(too_long))
    return labels


def model_gate(*, index_path, work_index, cad_root, project_root, roots,
               part_id, configuration=None):
    """Require exactly one fresh inventory row with no reusable model/candidate."""
    from model_inventory import audit

    result = audit(index_path, work_index, cad_root, project_root, roots,
                   configuration=configuration, part_id=part_id)
    rows = [row for row in result.get('components', []) if row.get('part_id') == part_id]
    if len(rows) != 1:
        raise ValueError('Live model inventory must return exactly one selected part row')
    row = rows[0]
    if configuration is not None and row.get('configuration') != configuration:
        raise ValueError('Live model inventory returned a different configuration scope')
    if row.get('action') != 'NEW_MODEL_REQUIRED' or row.get('models') or row.get('candidates'):
        raise FileExistsError('Selected-scope model inventory requires reuse/review')
    return row


def _json_safe(value):
    if isinstance(value, (bytes, bytearray, memoryview)):
        raw = bytes(value)
        return {'__binary_encoding__': 'base64',
                'data': base64.b64encode(raw).decode('ascii'),
                'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json_safe(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Native response contains a non-finite number')
    return value


def write_raw_response(path, response):
    Path(path).write_text(json.dumps(_json_safe(response), indent=2,
                                     ensure_ascii=False, allow_nan=False) + '\n',
                          encoding='utf-8')


def _sab_bytes(value):
    if isinstance(value, (bytes, bytearray, memoryview)):
        return bytes(value)
    if isinstance(value, list) and all(type(item) is int and 0 <= item <= 255 for item in value):
        return bytes(value)
    raise TypeError('Native response uses an unsupported SAB byte representation')


def _nonempty_sab_bytes(acis):
    """Return meaningful SAB bytes, or None when the native payload is empty."""
    value = acis.get('sab_data')
    if value is None:
        return None
    raw = _sab_bytes(value)
    return raw if raw else None


def _pre_save_geometry(record, job, retain_sab=None):
    """Retain nonempty SAB bytes before decoding; otherwise use SAT vertices."""
    from annular_reference import verify
    from native_acis import sab_features
    from step_placements import identity_sat_vertices

    acis = record.get('properties', {}).get('acis_data', {})
    raw_sab = _nonempty_sab_bytes(acis)
    if raw_sab is not None:
        if retain_sab is None:
            raise RuntimeError('Nonempty SAB must be retained before decoder access')
        retained = retain_sab(raw_sab)
        if isinstance(retained, tuple):
            retained, receipt = retained
        else:
            receipt = None
        if retained != raw_sab:
            raise ValueError('Retained SAB bytes differ from the native response')
        features = sab_features(retained, include_loops=True)
        geometry = verify(features, job)
        return {
            'format': 'SAB', 'raw_sab': retained, 'sab_receipt': receipt,
            'points': features.get('points'), 'geometry': geometry,
            'geometry_status': geometry.get('result'),
        }
    sat = acis.get('sat_data')
    if isinstance(sat, str) and sat.strip():
        points = identity_sat_vertices(sat)
        _canonical_points(points)
        return {
            'format': 'SAT', 'raw_sab': None, 'points': points,
            'geometry': {'result': 'OBSERVED',
                         'method': 'pre-save SAT vertices; analytic annular checks require reopened SAB',
                         'point_count': len(points)},
            'geometry_status': 'OBSERVED',
        }
    raise ValueError('Pre-save record contains neither nonempty SAB nor valid SAT geometry')


def _validate_resume_part_name(job, selected):
    if selected.get('part_name') != job.get('part_name'):
        raise ValueError('Live selected-row part_name differs from the source-job part_name')


def _check_selected_row(paths, args, roots, part_id, configuration):
    gate = model_gate(index_path=paths['index'], work_index=paths['work_index'],
                      cad_root=paths['cad_root'], project_root=paths['project_root'],
                      roots={name: str(path) for name, path in roots.items()},
                      part_id=part_id, configuration=configuration)
    return gate


def _annular_write_gate(output, job_dir, allow_write):
    result = check_write_targets(output, job_dir, allow_write)
    receipts = (
        'ocs-journal.jsonl', 'action-occurrences.jsonl', 'native-handles.json',
        'document-start.json', 'pre-save-entity-response.json',
        'pre-save-read-states.json', 'pre-save-body.sab', 'pre-save-body.json',
        'pre-save-checks.json', 'capture-pre-save.json', 'pre-save-viewport.png',
        'save-reopen.json', 'reopened-entity-response.json', 'reopened-read-states.json',
        'reopened-body.sab', 'reopened-body.json', 'reopened-checks.json',
        'persistence-check.json', 'document-cleanup.json', 'result.json',
        'native-failure.json',
    )
    existing = [name for name in receipts if (Path(job_dir) / name).exists()]
    if allow_write and existing:
        raise FileExistsError('Annular write receipts prohibit replay: ' + ', '.join(existing))
    result['existing_write_receipts'] = sorted(set(result['existing_write_receipts'] + existing))
    return result


def _read_json(path, label):
    try:
        value = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(label + ' is absent or invalid JSON') from error
    if not isinstance(value, dict):
        raise ValueError(label + ' must be a JSON object')
    return value


def _resume_checkpoint(job_dir, job, source_job_sha256, output, roots):
    """Validate a failed pre-save checkpoint without changing its evidence."""
    job_dir = Path(job_dir)
    required = {
        'native-preflight.json': 'preflight', 'document-start.json': 'document_start',
        'native-handles.json': 'handles', 'native-failure.json': 'failure',
        'pre-save-entity-response.json': 'response',
        'pre-save-read-states.json': 'read_states', 'pre-save-body.json': 'body_receipt',
        'capture-pre-save.json': 'capture',
    }
    records = {key: _read_json(job_dir / filename, filename)
               for filename, key in required.items()}
    if Path(output).exists():
        raise FileExistsError('Resume requires the output path to remain absent')
    forbidden = (
        'pre-save-checks.json', 'save-reopen.json', 'reopened-entity-response.json',
        'reopened-read-states.json', 'reopened-body.sab', 'reopened-body.json',
        'reopened-checks.json', 'persistence-check.json', 'document-cleanup.json',
        'result.json', 'action-occurrences.jsonl', 'resume-current-entity-response.json',
        'resume-current-read-states.json', 'resume-preflight.json',
        'native-resume-failure.json',
    )
    present = [name for name in forbidden if (job_dir / name).exists()]
    if present:
        raise FileExistsError('Resume is prohibited by downstream receipts: ' + ', '.join(present))

    failure = records['failure']
    if failure.get('result') != 'FAIL' or failure.get('stage') != 'pre_save_records' \
            or failure.get('part_id') != job.get('part_id') \
            or failure.get('job_id') != job.get('job_id') \
            or 'Nonempty native SAB bytes required' not in str(failure.get('error', '')):
        raise ValueError('Resume requires the recorded empty-SAB pre_save_records failure for this job')
    preflight = records['preflight']
    if preflight.get('result') != 'PASS' or preflight.get('job_id') != job.get('job_id') \
            or preflight.get('request_namespace') != job.get('namespace') \
            or preflight.get('source_job_sha256') != source_job_sha256:
        raise ValueError('Retained write preflight does not match the current source job')

    start = records['document_start']
    construction_id = start.get('construction_document_id')
    handle = records['handles'].get('annulus')
    if start.get('result') != 'PASS' or start.get('units') != 'mm' \
            or start.get('INSUNITS') != 4 or start.get('UCS') != 'world' \
            or type(construction_id) is not int or handle is None:
        raise ValueError('Retained document-start or native-handle proof is incomplete')
    if not any(row.get('id') == construction_id
               for row in start.get('construction_documents', []) if isinstance(row, dict)):
        raise ValueError('Owned construction document is absent from its start receipt')

    response = records['response']
    rows = response.get('records')
    if response.get('document_id') != construction_id or not isinstance(rows, list) \
            or len(rows) != 1 or rows[0].get('handle') != handle \
            or rows[0].get('type') != 'Solid3D':
        raise ValueError('Retained pre-save entity response does not identify the owned annulus')
    read_states = records['read_states']
    before, after = read_states.get('before'), read_states.get('after')
    if not isinstance(before, dict) or not isinstance(after, dict) \
            or before.get('document_id') != construction_id \
            or after.get('document_id') != construction_id \
            or before.get('revision') != after.get('revision') \
            or before.get('geometry_revision') != after.get('geometry_revision') \
            or after.get('geometry_revision') is None:
        raise ValueError('Retained entity read lacks a stable document and geometry epoch')
    if response.get('revision') != after.get('revision') \
            or response.get('geometry_revision') != after.get('geometry_revision'):
        raise ValueError('Retained entity response differs from its read-state epoch')
    body = records['body_receipt']
    empty_sha = hashlib.sha256(b'').hexdigest()
    body_path = job_dir / 'pre-save-body.sab'
    if body.get('bytes') != 0 or body.get('sha256') != empty_sha \
            or body.get('status') != 'CAPTURED_BEFORE_DECODER' \
            or body.get('handle') != handle or not body_path.is_file() \
            or body_path.stat().st_size != 0 or body.get('document_id') != construction_id \
            or body.get('geometry_revision') != after.get('geometry_revision'):
        raise ValueError('Retained empty-SAB receipt does not match the recorded failure')
    acis = rows[0].get('properties', {}).get('acis_data', {})
    if _nonempty_sab_bytes(acis) is not None or not isinstance(acis.get('sat_data'), str) \
            or not acis['sat_data'].strip():
        raise ValueError('Resume checkpoint is not the empty-SAB, valid-SAT case')

    capture = records['capture']
    if capture.get('result') != 'CAPTURED' \
            or capture.get('geometry_revision') != after.get('geometry_revision'):
        raise ValueError('Retained capture receipt does not match the pre-save geometry epoch')
    journal_path = job_dir / 'ocs-journal.jsonl'
    if not journal_path.is_file():
        raise ValueError('Resume requires the original OCS journal')
    intents = set()
    responses = set()
    journal_lines = journal_path.read_text(encoding='utf-8').splitlines()
    for line_number, line in enumerate(journal_lines, 1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError('Original OCS journal has invalid JSON at line ' + str(line_number)) from error
        request_id = event.get('request_id')
        if request_id is None:
            request_id = event.get('request', {}).get('request_id')
        if event.get('event') == 'intent' and isinstance(request_id, str):
            intents.add(request_id)
        if event.get('event') == 'response' and isinstance(request_id, str):
            payload = event.get('response', {})
            terminal = payload.get('status') == 'completed' or (
                payload.get('ok') is True and payload.get('error') is None
                and 'result' in payload)
            if terminal:
                responses.add(request_id)
    pending_ids = {job['namespace'] + ':verified-save', job['namespace'] + ':reopen'}
    if intents & pending_ids:
        raise ValueError('A save or reopen request already has an intent; use same-ID recovery review')
    capture_id = job['namespace'] + ':capture-pre-save-viewport'
    metadata_id = job['namespace'] + ':' + job['metadata_request_label']
    if capture_id not in intents or capture_id not in responses \
            or metadata_id not in intents or metadata_id not in responses:
        raise ValueError('Original journal does not prove metadata and capture requests completed')
    if job_dir.joinpath('pre-save-checks.json').exists():
        raise FileExistsError('Pre-save checks already exist; resume is limited to the failed stage')
    return {
        **records, 'construction_document_id': construction_id, 'handle': handle,
        'construction_revision': after.get('revision'),
        'geometry_revision': after.get('geometry_revision'),
        'journal_intents': sorted(intents), 'roots': roots,
    }


def _annular_resume_write_gate(output, job_dir, job, allow_resume_preflight=False):
    """Permit only the saved pre-save checkpoint's single downstream continuation."""
    if Path(output).exists():
        raise FileExistsError('Resume output already exists; inspect the saved artifact')
    receipts = (
        'save-reopen.json', 'reopened-entity-response.json', 'reopened-read-states.json',
        'reopened-body.sab', 'reopened-body.json', 'reopened-checks.json',
        'persistence-check.json', 'document-cleanup.json', 'result.json',
        'action-occurrences.jsonl', 'native-resume-failure.json',
    )
    existing = [name for name in receipts if (Path(job_dir) / name).exists()]
    if not allow_resume_preflight and (Path(job_dir) / 'resume-preflight.json').exists():
        existing.append('resume-preflight.json')
    if existing:
        raise FileExistsError('Resume receipts prohibit another continuation: ' + ', '.join(existing))
    journal = Path(job_dir) / 'ocs-journal.jsonl'
    for line_number, line in enumerate(journal.read_text(encoding='utf-8').splitlines(), 1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError('Original OCS journal has invalid JSON at line ' + str(line_number)) from error
        request = event.get('request', {})
        request_id = event.get('request_id') or request.get('request_id')
        if event.get('event') == 'intent' and request_id in {
                job['namespace'] + ':verified-save', job['namespace'] + ':reopen'}:
            raise ValueError('A save or reopen intent already exists; continuation must use reviewed recovery')


def _assert_resume_live_state(state, checkpoint, expected_snapshot):
    if state.get('ok') is not True \
            or state.get('document_id') != checkpoint['construction_document_id'] \
            or state.get('revision') != checkpoint['construction_revision'] \
            or state.get('geometry_revision') != checkpoint['geometry_revision'] \
            or state.get('command') or state.get('modal'):
        raise RuntimeError('Live OCS state differs from the retained pre-save document epoch')

    live = document_snapshot(state, checkpoint['roots'])
    if live.get('documents') != expected_snapshot.get('documents'):
        raise RuntimeError('Live OCS document paths or dirty states differ from the retained epoch')


def _record_geometry_fingerprint(record):
    acis = record.get('properties', {}).get('acis_data', {})
    return {
        'handle': record.get('handle'), 'type': record.get('type'),
        'sat_data': acis.get('sat_data'), 'sab_data': _nonempty_sab_bytes(acis),
    }


def prepare_resume(args):
    """Read-only gate for continuing one retained pre-save failure in place."""
    if not args.allow_write:
        raise ValueError('--resume-pre-save requires --allow-write')
    job_path = Path(args.job).resolve()
    job_dir = Path(args.job_dir).resolve()
    roots = parse_roots(args.root)
    output = resolve_locator(args.output, roots, job_path.parent)
    source_locator(job_dir, roots)
    prepared = resolve_job(job_path, roots)
    job = prepared['job']
    if job.get('output_path'):
        declared = resolve_locator(job['output_path'], roots, job_path.parent)
        if declared != output:
            raise ValueError('--output conflicts with the external job output_path')
    paths = {
        'index': Path(args.index).resolve(), 'work_index': Path(args.work_index).resolve(),
        'cad_root': Path(args.cad_root).resolve(), 'project_root': Path(args.project_root).resolve(),
    }
    for label, path in paths.items():
        if label in ('index', 'work_index') and not path.is_file():
            raise FileNotFoundError('Model-gate ' + label + ' file is absent')
        if label in ('cad_root', 'project_root') and not path.is_dir():
            raise FileNotFoundError('Model-gate ' + label + ' directory is absent')
        source_locator(path, roots)
    configuration = job.get('configuration')
    override = getattr(args, 'configuration', None)
    if override is not None:
        if configuration not in (None, override):
            raise ValueError('CLI configuration conflicts with source-job configuration')
        configuration = override
    prepared['configuration'] = configuration
    selected = _check_selected_row(paths, args, roots, job['part_id'], configuration)
    _validate_resume_part_name(job, selected)
    if not isinstance(args.execution_model, str) or not args.execution_model.strip():
        raise ValueError('Actual execution-model identity is required')
    if not isinstance(args.session, str) or not args.session.strip():
        raise ValueError('Exact OCS session name is required for resume')
    control, cadtools_root = Path(args.control).resolve(), Path(args.cadtools_root).resolve()
    if not control.is_file():
        raise FileNotFoundError('Explicit OCS control helper is absent')
    if not (cadtools_root / 'cadtools/runtime.py').is_file() \
            or not (cadtools_root / 'cadtools/verification.py').is_file():
        raise FileNotFoundError('--cadtools-root must contain cadtools/runtime.py and verification.py')

    checkpoint = _resume_checkpoint(job_dir, job, prepared['source_job_sha256'], output, roots)
    prior = _read_json(job_dir / 'native-preflight.json', 'native-preflight.json')
    sab = sab_reader_preflight()
    scripts_root = Path(__file__).resolve().parent
    for candidate in (scripts_root, cadtools_root):
        if str(candidate) not in sys.path:
            sys.path.insert(0, str(candidate))
    for module in ('cadtools.runtime', 'cadtools.geometry', 'cadtools.verification',
                   'native_acis', 'source_metadata', 'ocs_document_cleanup'):
        importlib.import_module(module)
    from cadtools.runtime import load_helper
    helper = load_helper(control)
    descriptors = helper.descriptors(session=args.session)
    if len(descriptors) != 1:
        raise RuntimeError('Expected exactly one selected OCS session')
    descriptor = descriptors[0]
    state = helper.request(descriptor, {'op': 'state'}, 30)
    if state.get('ok') is not True or state.get('document_id') != checkpoint['construction_document_id'] \
            or state.get('revision') != checkpoint['construction_revision'] \
            or state.get('geometry_revision') != checkpoint['geometry_revision'] \
            or state.get('command') or state.get('modal'):
        raise RuntimeError('Live OCS state differs from the retained pre-save document epoch')
    expected_documents = checkpoint['read_states']['after'].get('documents')
    if not isinstance(expected_documents, list) or not isinstance(state.get('documents'), list):
        raise ValueError('Resume requires retained and live document inventories')
    current_snapshot = document_snapshot(state, roots)
    if current_snapshot.get('documents') != expected_documents:
        raise RuntimeError('Live OCS document paths or dirty states differ from the retained epoch')
    if descriptor.get('session_id') != prior.get('session_id'):
        raise RuntimeError('Selected OCS session differs from the retained write preflight')

    original_documents = prior.get('active_documents_before')
    if not isinstance(original_documents, dict) or not isinstance(original_documents.get('documents'), list):
        raise ValueError('Original pre-build document snapshot is absent')
    occurrence_id = job['namespace'] + ':annular-save-reopen'
    result = {
        'result': 'PASS', 'mode': 'RESUME_PRE_SAVE', 'part_id': job['part_id'],
        'part_name': job['part_name'], 'job_id': job['job_id'],
        'request_namespace': job['namespace'], 'source_job': prepared['source_job_locator'],
        'source_job_sha256': prepared['source_job_sha256'],
        'source_readiness': portableize(prepared['readiness'], roots),
        'source_dimensions_mm': prepared['parameters']['dimensions'],
        'frame': job['local_frame'], 'representation': job['representation'],
        'source_locators': prepared['resolved_sources'],
        'model_gate': portableize(selected, roots), 'output_path': source_locator(output, roots),
        'resume_document_id': checkpoint['construction_document_id'],
        'resume_handle': checkpoint['handle'],
        'resume_geometry_revision': checkpoint['geometry_revision'],
        'failure_stage': 'pre_save_records', 'sab_reader': sab,
        'session_id': descriptor['session_id'], 'active_documents_before': document_snapshot(state, roots),
        'native_mutations': 0,
    }
    return result, {
        **prepared, 'roots': roots, 'output': output, 'job_dir': job_dir,
        'paths': paths, 'model_gate': selected, 'descriptor': descriptor,
        'helper': helper, 'documents_before': original_documents,
        'active_documents_before': document_snapshot(state, roots),
        'active_document_id': checkpoint['construction_document_id'],
        'resume_checkpoint': checkpoint, 'resume_preflight': result,
        'occurrence_id': occurrence_id, 'resume_pre_save': True,
    }


def prepare(args):
    """Read-only source, output, model-inventory, reader and OCS preflight."""
    if getattr(args, 'resume_pre_save', False):
        return prepare_resume(args)
    job_path = Path(args.job).resolve()
    job_dir = Path(args.job_dir).resolve()
    roots = parse_roots(args.root)
    output = resolve_locator(args.output, roots, job_path.parent)
    source_locator(job_dir, roots)
    write_gate = _annular_write_gate(output, job_dir, args.allow_write)
    prepared = resolve_job(job_path, roots)
    job = prepared['job']
    if job.get('output_path'):
        declared_output = resolve_locator(job['output_path'], roots, job_path.parent)
        if declared_output != output:
            raise ValueError('--output conflicts with the external job output_path')
    if job.get('job_id') is None:
        raise ValueError('External annular job needs a readable job_id')

    paths = {
        'index': Path(args.index).resolve(),
        'work_index': Path(args.work_index).resolve(),
        'cad_root': Path(args.cad_root).resolve(),
        'project_root': Path(args.project_root).resolve(),
    }
    for label, path in paths.items():
        if label in ('index', 'work_index') and not path.is_file():
            raise FileNotFoundError('Model-gate ' + label + ' file is absent')
        if label in ('cad_root', 'project_root') and not path.is_dir():
            raise FileNotFoundError('Model-gate ' + label + ' directory is absent')
        source_locator(path, roots)
    configuration = job.get('configuration')
    override = getattr(args, 'configuration', None)
    if override is not None:
        if not isinstance(override, str) or not override.strip():
            raise ValueError('Configuration scope must be a nonempty string')
        if configuration not in (None, override):
            raise ValueError('CLI configuration conflicts with source-job configuration')
        configuration = override
    prepared['configuration'] = configuration
    if configuration is not None and (not isinstance(configuration, str) or not configuration.strip()):
        raise ValueError('Job configuration must be a nonempty string when present')
    selected = _check_selected_row(paths, args, roots, job['part_id'], configuration)

    occurrence_id = job['namespace'] + ':annular-save-reopen'
    occurrence_path = job_dir / 'action-occurrences.jsonl'
    if args.allow_write and occurrence_path.is_file():
        for line in occurrence_path.read_text(encoding='utf-8').splitlines():
            if json.loads(line).get('occurrence_id') == occurrence_id:
                raise FileExistsError('Native occurrence already exists; inspect its receipts')

    control = Path(args.control).resolve()
    cadtools_root = Path(args.cadtools_root).resolve()
    if not control.is_file():
        raise FileNotFoundError('Explicit OCS control helper is absent')
    if not (cadtools_root / 'cadtools/runtime.py').is_file() \
            or not (cadtools_root / 'cadtools/verification.py').is_file():
        raise FileNotFoundError('--cadtools-root must contain cadtools/runtime.py and verification.py')
    if not isinstance(args.session, str) or not args.session.strip():
        raise ValueError('Exact OCS session name is required for preflight')
    if not isinstance(args.execution_model, str) or not args.execution_model.strip():
        raise ValueError('Actual execution-model identity is required')

    # The saved-body reader is imported before loading/discovering OCS.
    sab = sab_reader_preflight()
    scripts_root = Path(__file__).resolve().parent
    for candidate in (scripts_root, cadtools_root):
        if str(candidate) not in sys.path:
            sys.path.insert(0, str(candidate))
    importlib.import_module('cadtools.runtime')
    importlib.import_module('cadtools.geometry')
    importlib.import_module('cadtools.verification')
    importlib.import_module('native_acis')
    importlib.import_module('source_metadata')
    importlib.import_module('ocs_document_cleanup')

    from cadtools.runtime import load_helper
    helper = load_helper(control)
    descriptors = helper.descriptors(session=args.session)
    if len(descriptors) != 1:
        raise RuntimeError('Expected exactly one selected OCS session')
    descriptor = descriptors[0]
    state = helper.request(descriptor, {'op': 'state'}, 30)
    if state.get('ok') is not True or state.get('document_id') is None:
        raise RuntimeError('OCS session state is unreadable')
    if state.get('command') or state.get('modal'):
        raise RuntimeError('OCS command/modal state must be clear')
    snapshot = document_snapshot(state, roots)
    for row in snapshot['documents']:
        if row.get('path'):
            source_locator(resolve_locator(row['path'], roots), roots)
    result = {
        'result': 'PASS',
        'mode': write_gate['mode'],
        'part_id': job['part_id'], 'part_name': job['part_name'],
        'job_id': job['job_id'], 'request_namespace': job['namespace'],
        'source_job': prepared['source_job_locator'],
        'source_job_sha256': prepared['source_job_sha256'],
        'source_readiness': portableize(prepared['readiness'], roots),
        'source_dimensions_mm': prepared['parameters']['dimensions'],
        'frame': job['local_frame'], 'representation': job['representation'],
        'source_locators': prepared['resolved_sources'],
        'model_gate': portableize(selected, roots),
        'output_path': source_locator(output, roots),
        'existing_write_receipts': write_gate['existing_write_receipts'],
        'sab_reader': sab,
        'session_id': descriptor['session_id'],
        'active_documents_before': snapshot,
        'execution_model': args.execution_model,
        'native_mutations': 0,
    }
    return result, {
        **prepared, 'roots': roots, 'output': output, 'job_dir': job_dir,
        'paths': paths, 'model_gate': selected, 'descriptor': descriptor,
        'helper': helper, 'documents_before': snapshot,
        'occurrence_id': occurrence_id,
    }


def _verify_stable_state(client, expected_document, expected_revision=None,
                         expected_geometry_revision=None):
    state = client.read('state')
    if state.get('document_id') != expected_document:
        raise RuntimeError('Active document identity changed during native read')
    if expected_revision is not None and state.get('revision') != expected_revision:
        raise RuntimeError('Document revision changed during native read')
    if expected_geometry_revision is not None \
            and state.get('geometry_revision') != expected_geometry_revision:
        raise RuntimeError('Geometry revision changed during native read')
    return state


def _entity_response(client, handle, response_path, state_path, roots):
    before = client.read('state')
    response = client.read('records', collection='entities', handles=[handle], limit=1)
    after = client.read('state')
    write_raw_response(response_path, response)
    write_json(state_path, portableize({'before': before, 'after': after}, roots))
    if before.get('document_id') != client.document_id \
            or after.get('document_id') != client.document_id \
            or before.get('revision') is None or before.get('geometry_revision') is None \
            or after.get('revision') != before.get('revision') \
            or after.get('geometry_revision') != before.get('geometry_revision'):
        raise RuntimeError('Entity read was not bracketed by a stable document/revision epoch')
    if response.get('document_id') not in (None, client.document_id) \
            or response.get('revision') not in (None, after.get('revision')) \
            or response.get('geometry_revision') not in (None, after.get('geometry_revision')):
        raise RuntimeError('Entity response identity/revision differs from bracket states')
    rows = response.get('records', [])
    if len(rows) != 1 or rows[0].get('handle') != handle or rows[0].get('type') != 'Solid3D':
        raise RuntimeError('Expected exactly one Solid3D record for the annular handle')
    return response, rows[0], after


def _retain_sab(record, path, receipt_path, response, roots):
    acis = record.get('properties', {}).get('acis_data', {})
    raw = _nonempty_sab_bytes(acis)
    if raw is None:
        raise RuntimeError('Nonempty native SAB bytes required')
    Path(path).write_bytes(raw)
    descriptor = {
        'status': 'CAPTURED_BEFORE_DECODER', 'path': source_locator(path, roots),
        'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'handle': record.get('handle'), 'document_id': response.get('document_id'),
        'revision': response.get('revision'),
        'geometry_revision': response.get('geometry_revision'),
    }
    write_json(receipt_path, descriptor)
    return raw, descriptor


def _canonical_points(points):
    if not isinstance(points, list) or not points:
        raise ValueError('Native vertex observations are required for persistence comparison')
    canonical = []
    for point in points:
        if not isinstance(point, (list, tuple)) or len(point) != 3:
            raise ValueError('Native vertex observations must contain three coordinates')
        row = []
        for value in point:
            if isinstance(value, bool) or not isinstance(value, (int, float)) \
                    or not math.isfinite(value):
                raise ValueError('Native vertex observations must be finite numbers')
            row.append(float(value))
        canonical.append(tuple(row))
    return sorted(canonical)


def _compare_point_sets(actual, expected, tolerance):
    """Match native vertices one-to-one within the job's numerical tolerance."""
    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)) \
            or not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Positive finite annular point tolerance is required')
    observed = _canonical_points(actual)
    targets = _canonical_points(expected)
    if len(observed) != len(targets):
        return {'check': 'Pre-save to reopened native annular vertices',
                'result': 'FAIL', 'expected_count': len(targets),
                'observed_count': len(observed), 'numeric_tolerance_mm': tolerance,
                'method': 'one-to-one native vertex matching by coordinate tolerance'}
    unmatched = list(targets)
    matches = []
    for point in observed:
        options = [
            (max(abs(a - b) for a, b in zip(point, target)), index, target)
            for index, target in enumerate(unmatched)
        ]
        deviation, index, target = min(options, key=lambda row: (row[0], row[1]))
        if deviation > tolerance:
            return {'check': 'Pre-save to reopened native annular vertices',
                    'result': 'FAIL', 'unmatched_observation': point,
                    'nearest_expected': target,
                    'maximum_coordinate_deviation_mm': deviation,
                    'numeric_tolerance_mm': tolerance,
                    'method': 'one-to-one native vertex matching by coordinate tolerance'}
        matches.append({'observed': point, 'expected': target,
                        'maximum_coordinate_deviation_mm': deviation})
        unmatched.pop(index)
    return {'check': 'Pre-save to reopened native annular vertices',
            'result': 'PASS', 'matches': matches,
            'numeric_tolerance_mm': tolerance,
            'method': 'one-to-one native vertex matching by maximum coordinate deviation'}


def _capture(client, job_dir, roots, namespace):
    before = client.read('state')
    if before.get('document_id') != client.document_id or before.get('geometry_revision') is None:
        raise RuntimeError('Capture requires the owned document and a geometry revision')
    image = job_dir / 'pre-save-viewport.png'
    response = client.mutate('capture-pre-save-viewport', 'capture',
                             path=str(image), scope='viewport')
    after = client.read('state')
    if after.get('document_id') != client.document_id \
            or after.get('geometry_revision') != before.get('geometry_revision'):
        raise RuntimeError('Viewport capture changed the geometry epoch')
    if not image.is_file() or image.stat().st_size <= 0:
        raise RuntimeError('Viewport capture did not produce a nonempty image')
    evidence = {'result': 'CAPTURED', 'scope': 'viewport',
                'path': source_locator(image, roots), 'bytes': image.stat().st_size,
                'sha256': sha256(image), 'request_namespace': namespace,
                'geometry_revision': after['geometry_revision'],
                'identity_review': 'NOT_ASSESSED', 'response': _json_safe(response)}
    write_json(job_dir / 'capture-pre-save.json', evidence)
    return evidence


def execute(prepared, args):
    """Build once, retain raw native evidence, save/reopen, verify and clean up."""
    from cadtools.runtime import Client, Journal, load_helper
    from cadtools.verification import save_reopen
    from envelope_job_runner import check_audit
    from annular_reference import build_annulus, inspect, verify, verify_metadata
    from native_acis import sab_features
    from step_placements import identity_sat_vertices

    job = prepared['job']
    params = prepared['parameters']
    roots, job_dir, output = prepared['roots'], prepared['job_dir'], prepared['output']
    helper, descriptor = prepared['helper'], prepared['descriptor']
    before_snapshot = prepared['documents_before']
    initial_docs = {row['id']: (row.get('path'), row.get('dirty'))
                    for row in before_snapshot['documents']}
    prior_id = prepared.get('active_document_id', before_snapshot['document_id'])
    client = RecoveringClient(Client(
        helper, descriptor, prior_id, job['namespace'],
        Journal(job_dir / 'ocs-journal.jsonl'), allow_write=True, timeout=60))
    stage = 'resume_pre_save_validation' if prepared.get('resume_pre_save') \
        else 'create_isolated_document'
    try:
        verify_source_pins(prepared)
        if prepared.get('resume_pre_save'):
            checkpoint = prepared['resume_checkpoint']
            construction_id, handle = checkpoint['construction_document_id'], checkpoint['handle']
            _annular_resume_write_gate(output, job_dir, job, allow_resume_preflight=True)
            state = client.read('state')
            _assert_resume_live_state(state, checkpoint, prepared['active_documents_before'])
            stage = 'resume_pre_save_record'
            pre_response, pre_record, pre_state = _entity_response(
                client, handle, job_dir / 'resume-current-entity-response.json',
                job_dir / 'resume-current-read-states.json', roots)
            original_record = checkpoint['response']['records'][0]
            if _record_geometry_fingerprint(pre_record) != _record_geometry_fingerprint(original_record):
                raise RuntimeError('Live pre-save geometry or metadata differs from retained failure evidence')
            capture = checkpoint['capture']
        else:
            _annular_write_gate(output, job_dir, True)
            fresh_gate = model_gate(
                index_path=prepared['paths']['index'],
                work_index=prepared['paths']['work_index'],
                cad_root=prepared['paths']['cad_root'],
                project_root=prepared['paths']['project_root'],
                roots={name: str(path) for name, path in roots.items()},
                part_id=job['part_id'], configuration=prepared['configuration'])
            if fresh_gate.get('action') != 'NEW_MODEL_REQUIRED':
                raise FileExistsError('Fresh model inventory no longer permits an annular construction')
            client.mutate('create-isolated-document', 'new')
            state = helper.request(descriptor, {'op': 'state'}, 30)
            construction_id = state.get('document_id')
            if state.get('ok') is not True or construction_id is None or construction_id == prior_id:
                raise RuntimeError('Isolated annular document identity was not confirmed')
            new_snapshot = document_snapshot(state, roots)
            documents_after = {row['id']: (row.get('path'), row.get('dirty'))
                               for row in new_snapshot['documents']}
            if set(documents_after) != set(initial_docs) | {construction_id} \
                    or any(documents_after.get(key) != value for key, value in initial_docs.items()):
                raise RuntimeError('Existing documents changed during isolated-document creation')
            client.document_id = construction_id
            check_audit(client.read('audit', target_format='dwg', target_version='2018'), 0)
            client.mutate('units-millimetres', 'sysvar', set={'INSUNITS': 4})
            client.mutate('world-ucs', 'run', cmd='UCS W')
            write_json(job_dir / 'document-start.json', portableize({
                'result': 'PASS', 'previous_documents': before_snapshot['documents'],
                'construction_document_id': construction_id,
                'construction_documents': new_snapshot['documents'],
                'units': 'mm', 'INSUNITS': 4, 'UCS': 'world'}, roots))

            stage = 'construct_annulus'
            handle = build_annulus(client, job)
            write_json(job_dir / 'native-handles.json', {'annulus': handle})
            construction_state = client.read('state')
            if construction_state.get('document_id') != construction_id:
                raise RuntimeError('Active document changed during annular construction')

            stage = 'capture_before_save'
            capture = _capture(client, job_dir, roots, job['namespace'])

            stage = 'pre_save_records'
            pre_response, pre_record, pre_state = _entity_response(
                client, handle, job_dir / 'pre-save-entity-response.json',
                job_dir / 'pre-save-read-states.json', roots)
        pre_metadata = verify_metadata(pre_record, str(handle), job)
        if pre_metadata.get('result') != 'PASS':
            raise RuntimeError('Pre-save source metadata check failed')
        retained_sab = {}
        def retain_pre_save_sab(raw):
            saved, receipt = _retain_sab(
                pre_record, job_dir / 'pre-save-body.sab',
                job_dir / 'pre-save-body.json', pre_response, roots)
            retained_sab['receipt'] = receipt
            return saved

        geometry = _pre_save_geometry(pre_record, job, retain_pre_save_sab)
        if geometry['format'] == 'SAB':
            pre_sab_receipt = geometry.get('sab_receipt') or retained_sab.get('receipt')
            pre_points = geometry['points']
            pre_geometry = geometry['geometry']
            pre_geometry_status = geometry['geometry_status']
        else:
            pre_points = geometry['points']
            pre_sab_receipt = None
            pre_geometry = geometry['geometry']
            pre_geometry_status = 'OBSERVED'
        if pre_geometry_status not in ('PASS', 'OBSERVED'):
            raise RuntimeError('Pre-save analytic annular checks failed')
        check_audit(client.read('audit', target_format='dwg', target_version='2018'),
                    1, {'3D Solid': 1})
        pre_check = {
            'result': 'PASS', 'document_id': construction_id,
            'document_revision': pre_state['revision'],
            'geometry_revision': pre_state['geometry_revision'],
            'handle': handle, 'record_type': pre_record['type'],
            'metadata': pre_metadata, 'geometry': pre_geometry,
            'sab_receipt': pre_sab_receipt,
        }
        write_json(job_dir / 'pre-save-checks.json', portableize(pre_check, roots))

        stage = 'save_reopen'
        if prepared.get('resume_pre_save'):
            verify_source_pins(prepared)
            _annular_resume_write_gate(output, job_dir, job, allow_resume_preflight=True)
            current_state = _verify_stable_state(
                client, construction_id, pre_check['document_revision'],
                pre_check['geometry_revision'])
            _assert_resume_live_state(
                current_state, prepared['resume_checkpoint'],
                prepared['active_documents_before'])
        persisted = save_reopen(client, str(output), {'3D Solid': 1})
        # Retain the exact receipt immediately, before validation or entity decoding.
        write_json(job_dir / 'save-reopen.json', portableize(persisted, roots))
        persistence_receipt = validate_save_receipt(persisted, output, {'3D Solid': 1})

        stage = 'reopened_raw_record'
        post_response, post_record, post_state = _entity_response(
            client, handle, job_dir / 'reopened-entity-response.json',
            job_dir / 'reopened-read-states.json', roots)
        raw_sab, raw_receipt = _retain_sab(
            post_record, job_dir / 'reopened-body.sab',
            job_dir / 'reopened-body.json', post_response, roots)

        stage = 'reopened_analytic_checks'
        _, reopened_check, reopened_record = inspect(client, str(handle), job)
        if reopened_check.get('result') != 'PASS':
            raise RuntimeError('Reopened annular geometry or metadata check failed')
        if reopened_record.get('handle') != handle:
            raise RuntimeError('Reopened record handle differs from the constructed annulus')
        point_check = _compare_point_sets(
            reopened_check['features']['points'], pre_points, params['tolerance'])
        if point_check.get('result') != 'PASS':
            raise RuntimeError('Pre-save and reopened native point sets differ')
        final_state = _verify_stable_state(client, reopened_check['document_id'],
                                           reopened_check['document_revision'],
                                           reopened_check['geometry_revision'])
        if reopened_check['document_id'] == construction_id:
            raise RuntimeError('Save/reopen did not produce a distinct reopened document identity')
        all_docs = {row['id']: (row.get('path'), row.get('dirty'))
                    for row in final_state.get('documents', [])}
        if set(all_docs) != set(initial_docs) | {construction_id, reopened_check['document_id']} \
                or any(all_docs.get(key) != value for key, value in initial_docs.items()):
            raise RuntimeError('Existing documents changed during save/reopen')

        write_json(job_dir / 'reopened-checks.json', portableize(reopened_check, roots))
        write_json(job_dir / 'persistence-check.json', portableize(point_check, roots))
        digest = sha256(output)
        if prepared.get('resume_pre_save'):
            construction_row = next((row for row in prepared['active_documents_before']['documents']
                                     if row['id'] == construction_id), None)
        else:
            construction_row = next((row for row in new_snapshot['documents']
                                     if row['id'] == construction_id), None)
        if construction_row is None:
            raise RuntimeError('Owned construction document path snapshot is absent')
        stage = 'close_owned_documents'
        cleanup = cleanup_completed_envelope(
            helper=helper, descriptor=descriptor, client=client,
            namespace=job['namespace'], output=output, saved_sha256=digest,
            pre_save_geometry={'document_id': construction_id,
                               'document_revision': pre_check['document_revision'],
                               'geometry_revision': pre_check['geometry_revision']},
            reopened_geometry={key: reopened_check[key]
                               for key in ('document_id', 'document_revision', 'geometry_revision')},
            construction_path=construction_row.get('path'))
        write_json(job_dir / 'document-cleanup.json', portableize(cleanup, roots))

        result = {
            'status': 'DONE' if cleanup.get('status') == 'DONE' else 'NEEDS_FOLLOWUP',
            'part_id': job['part_id'], 'part_name': job['part_name'],
            'job_id': job['job_id'], 'execution_model': args.execution_model,
            'representation': job['representation'], 'geometry_role': job['geometry_role'],
            'units': job['units'], 'frame': job['local_frame'],
            'source_job': prepared['source_job_locator'],
            'source_job_sha256': prepared['source_job_sha256'],
            'source_readiness': prepared['readiness']['state'],
            'source_dimensions_mm': params['dimensions'],
            'native_model': source_locator(output, roots),
            'native_model_sha256': digest, 'native_model_bytes': output.stat().st_size,
            'native_handle': handle, 'construction_document_id': construction_id,
            'reopened_document_id': reopened_check['document_id'],
            'pre_save_checks': pre_check, 'reopened_checks': reopened_check,
            'pre_save_to_reopened_persistence': point_check,
            'save_reopen': persisted, 'persistence_receipt': persistence_receipt,
            'reopened_raw_sab': raw_receipt, 'capture': capture,
            'cleanup': cleanup,
        }
        write_json(job_dir / 'result.json', portableize(result, roots))
        _append_occurrence(prepared, args, result)
        return portableize(result, roots)
    except Exception as error:
        failure = {'result': 'FAIL', 'stage': stage, 'part_id': job['part_id'],
                   'part_name': job['part_name'], 'job_id': job['job_id'],
                   'execution_model': args.execution_model,
                   'error_type': type(error).__name__, 'error': str(error),
                   'journal': source_locator(job_dir / 'ocs-journal.jsonl', roots)}
        failure_path = 'native-resume-failure.json' if prepared.get('resume_pre_save') \
            else 'native-failure.json'
        write_json(job_dir / failure_path, portableize(failure, roots))
        raise


def _append_occurrence(prepared, args, result):
    from component_records import append_occurrence
    job, roots, job_dir = prepared['job'], prepared['roots'], prepared['job_dir']
    occurrence = {
        'occurrence_id': prepared['occurrence_id'], 'job_id': job['job_id'],
        'part_id': job['part_id'], 'part_name': job['part_name'],
        'action_id': 'build-source-bound-annular-reference',
        'action_name': 'Build, verify, save, reopen and close one source-bound annular reference',
        'inputs': sorted(set([prepared['source_job_locator'], *prepared['resolved_sources']])),
        'outputs': [source_locator(prepared['output'], roots),
                    source_locator(job_dir / 'pre-save-checks.json', roots),
                    source_locator(job_dir / 'reopened-checks.json', roots),
                    source_locator(job_dir / 'save-reopen.json', roots)],
        'prerequisites': ['Source readiness and source hashes pass',
                          'Model inventory requires a new model for the selected scope',
                          'Saved-body reader preimports pass',
                          'Explicit native-write flag and selected idle OCS session'],
        'software': ['OpenCADStudio through guarded cadtools Client/Journal',
                     'annular_reference.build_annulus and inspect',
                     'cadtools.verification.save_reopen',
                     'envelope_job_runner recovery and cleanup utilities'],
        'agent': args.execution_model, 'representation': job['representation'],
        'units': job['units'], 'frame': job['local_frame'],
        'preserved': ['Existing OCS documents and their recorded path/dirty state',
                      'Pinned source files and source-job bytes'],
        'changed_or_inferred': ['Constructed the nominal annular solid from pinned source dimensions',
                                'Applied the explicit job frame and millimetre document units'],
        'alternatives': job.get('alternatives', []),
        'downstream': job.get('downstream', []),
        'checks': {'pre_save': result['pre_save_checks'],
                   'reopened': result['reopened_checks'],
                   'persistence': result['pre_save_to_reopened_persistence'],
                   'save_reopen': result['persistence_receipt'],
                   'cleanup': result['cleanup'],
                   'native_model_sha256': result['native_model_sha256']},
        'result': 'PASS' if result['status'] == 'DONE' else 'UNKNOWN',
        'evidence': [source_locator(job_dir / 'result.json', roots),
                     source_locator(job_dir / 'pre-save-checks.json', roots),
                     source_locator(job_dir / 'reopened-checks.json', roots)],
    }
    append_occurrence(job_dir / 'action-occurrences.jsonl', occurrence)


def run(args):
    result, prepared = prepare(args)
    job_dir = prepared['job_dir']
    preflight_name = 'resume-preflight.json' if prepared.get('resume_pre_save') \
        else 'native-preflight.json'
    write_json(job_dir / preflight_name, portableize(result, prepared['roots']))
    if not args.allow_write:
        return result
    native_result = execute(prepared, args)
    write_json(job_dir / 'result.json', native_result)
    return native_result


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--job', required=True, type=Path)
    cli.add_argument('--job-dir', required=True, type=Path)
    cli.add_argument('--output', required=True,
                     help='Absolute path or ${ROOT_NAME}/relative/path')
    cli.add_argument('--index', required=True, type=Path,
                     help='Component input index used by model_inventory')
    cli.add_argument('--work-index', required=True, type=Path,
                     help='Component work index used by model_inventory')
    cli.add_argument('--cad-root', required=True, type=Path)
    cli.add_argument('--project-root', required=True, type=Path)
    cli.add_argument('--cadtools-root', required=True, type=Path)
    cli.add_argument('--control', required=True, type=Path)
    cli.add_argument('--session', required=True)
    cli.add_argument('--execution-model', required=True)
    cli.add_argument('--configuration',
                     help='Optional source-job configuration scope override')
    cli.add_argument('--root', action='append', default=[], metavar='NAME=ABSOLUTE_PATH')
    cli.add_argument('--allow-write', action='store_true',
                     help='Permit one guarded native build after every preflight passes')
    cli.add_argument('--resume-pre-save', action='store_true',
                     help='Continue only a retained empty-SAB failure at pre_save_records')
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        print(json.dumps(run(args), indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(json.dumps({'result': 'FAIL', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
