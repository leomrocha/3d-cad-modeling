#!/usr/bin/env python3
"""Run an external source-bound envelope job through guarded OCS APIs.

All component identity, source values, output path and request namespace come
from the external job or explicit CLI arguments. Default execution performs a
read-only preflight; native writes require --allow-write.
"""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, ensure_ascii=False,
                                     allow_nan=False) + '\n', encoding='utf-8')


def parse_roots(entries):
    roots = {}
    for entry in entries:
        name, separator, value = entry.partition('=')
        if not separator or not re.fullmatch(r'[A-Z][A-Z0-9_]*', name):
            raise ValueError('--root requires NAME=ABSOLUTE_PATH with an uppercase root name')
        path = Path(value)
        if not path.is_absolute() or name in roots:
            raise ValueError('Each named root must be an explicit unique absolute path')
        roots[name] = path.resolve()
    if not roots:
        raise ValueError('At least one caller-supplied named root is required')
    return roots


def resolve_locator(locator, roots, base_dir=None):
    value = str(locator)
    match = re.match(r'^\$\{([A-Za-z_][A-Za-z0-9_]*)\}/(.*)$', value)
    if match:
        name, suffix = match.groups()
        if name not in roots:
            raise ValueError('Missing caller-supplied path root: ' + name)
        return (roots[name] / suffix).resolve()
    path = Path(value)
    if not path.is_absolute():
        if base_dir is None:
            raise ValueError('Relative path requires an explicit external-job base directory')
        path = Path(base_dir) / path
    return path.resolve()


def portableize(value, roots):
    if isinstance(value, dict):
        return {key: portableize(item, roots) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [portableize(item, roots) for item in value]
    if isinstance(value, str) and value.startswith('/'):
        path = Path(value)
        for name, root in roots.items():
            try:
                return '${' + name + '}/' + path.resolve().relative_to(root).as_posix()
            except ValueError:
                continue
    return value


def source_locator(path, roots):
    resolved = Path(path).resolve()
    for name, root in roots.items():
        try:
            return '${' + name + '}/' + resolved.relative_to(root).as_posix()
        except ValueError:
            continue
    raise ValueError('Path is outside caller-supplied named roots')


def check_write_targets(output, job_dir, allow_write):
    """Reject overwrite and replay conditions before any native request."""
    output = Path(output).resolve()
    job_dir = Path(job_dir).resolve()
    if output.exists():
        raise FileExistsError('Output exists; inspect the existing model instead of overwriting')
    if not output.parent.is_dir():
        raise FileNotFoundError('Output parent directory must already exist')
    if not job_dir.is_dir():
        raise FileNotFoundError('External job directory must already exist')
    if output.suffix.lower() != '.dwg':
        raise ValueError('Native envelope output must use .dwg')
    receipts = ('ocs-journal.jsonl', 'native-handles.json', 'result.json',
                'document-start.json', 'pre-save-feature-checks.json',
                'pre-save-source-metadata-check.json', 'save-reopen.json',
                'reopened-feature-checks.json', 'native-failure.json',
                'source-check-errors.json')
    present = [name for name in receipts if (job_dir / name).exists()]
    for path in job_dir.rglob('*.json'):
        name = path.name.casefold()
        if any(token in name for token in ('failure', 'error')) and path.relative_to(job_dir).as_posix() not in present:
            present.append(path.relative_to(job_dir).as_posix())
        if 'source' in name and any(token in name for token in ('check', 'feature')):
            try:
                record = json.loads(path.read_text(encoding='utf-8'))
            except (OSError, ValueError) as error:
                raise ValueError('Existing source-check record is unreadable; preserve and inspect it') from error
            if _has_failed_check(record):
                present.append(path.relative_to(job_dir).as_posix() + ' with a failed source check')
    prior_preflight = job_dir / 'native-preflight.json'
    if prior_preflight.is_file():
        try:
            previous = json.loads(prior_preflight.read_text(encoding='utf-8'))
        except (OSError, ValueError) as error:
            raise ValueError('Existing native preflight record is unreadable; preserve and inspect it') from error
        if previous.get('result') != 'PASS':
            present.append('native-preflight.json with non-PASS result')
    if allow_write and present:
        raise FileExistsError('Existing write receipts prohibit replay: ' + ', '.join(present))
    return {'mode': 'WRITE_AUTHORIZED' if allow_write else 'READ_ONLY_PREFLIGHT',
            'output': str(output), 'existing_write_receipts': present}


def _has_failed_check(value):
    if isinstance(value, dict):
        for key in ('result', 'status'):
            if isinstance(value.get(key), str) and value[key].upper() in {'FAIL', 'FAILED', 'ERROR'}:
                return True
        return any(_has_failed_check(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_has_failed_check(item) for item in value)
    return False


def resolve_runtime_job(job_path, roots):
    """Resolve source locators into a runtime clone while retaining portable inputs."""
    job_path = Path(job_path).resolve()
    job = json.loads(job_path.read_text(encoding='utf-8'))
    if not isinstance(job.get('namespace'), str) or not job['namespace'].strip():
        raise ValueError('External envelope job requires a nonempty request namespace')
    if not isinstance(job.get('part_id'), str) or not job['part_id'].strip():
        raise ValueError('External envelope job requires a readable part_id')
    if len(job['namespace'].encode('utf-8')) > 64:
        raise ValueError('External envelope request namespace must be at most 64 UTF-8 bytes')
    portable_features = copy.deepcopy(job.get('features'))
    if not isinstance(portable_features, list) or not portable_features:
        raise ValueError('External envelope job requires source-pinned features')
    runtime_job = copy.deepcopy(job)
    resolved_sources = []
    for index, feature in enumerate(runtime_job['features']):
        if not isinstance(feature, dict) or not feature.get('source'):
            raise ValueError('Each job feature requires a source locator')
        feature['source'] = str(resolve_locator(feature['source'], roots, job_path.parent))
        portable_locator = source_locator(feature['source'], roots)
        resolved_sources.append(portable_locator)
        portable_features[index]['source'] = portable_locator
    runtime_job['_portable_features'] = portable_features
    runtime_job['_resolved_source_locators'] = sorted(set(resolved_sources))
    from component_records import require_ready
    from envelope_reference import parameters
    readiness = require_ready(runtime_job)
    parameters_value = parameters(runtime_job)
    return runtime_job, parameters_value, portableize(readiness, roots)


def expected_metadata(job):
    required_strings = ('part_id', 'part_name', 'representation', 'units',
                        'local_frame', 'job_id')
    for key in required_strings:
        if not isinstance(job.get(key), str) or not job[key].strip():
            raise ValueError('Metadata needs a nonempty string ' + key)
    lines = ['Part ID: ' + job['part_id'], job['part_name'], job['representation'],
             'Reference envelope; units ' + job['units'],
             'Local frame: ' + job['local_frame'],
             'Source job: ' + job['job_id']]
    if job.get('envelope_scope'):
        if not isinstance(job['envelope_scope'], str):
            raise ValueError('envelope_scope must be a string')
        lines.append('Envelope scope: ' + job['envelope_scope'])
    for feature in job.get('_portable_features', job['features']):
        if not isinstance(feature.get('name'), str) or not feature['name'].strip():
            raise ValueError('Each metadata source feature needs a name')
        value = feature.get('value')
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            value_text = format(value, '.12g')
        else:
            value_text = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True)
        unit = feature.get('unit')
        lines.append('Source feature: ' + feature['name'] + ' = ' + value_text +
                     ((' ' + unit) if isinstance(unit, str) and unit else ''))
        if feature.get('source') and feature.get('source_sha256'):
            lines.append('Source: ' + feature['source'] + ' SHA-256 ' + feature['source_sha256'])
        if feature.get('source_location'):
            lines.append('Source location: ' + feature['source_location'])
    return lines


def document_snapshot(state, roots):
    """Keep only identity and preservation fields from the OCS session state."""
    if not isinstance(state.get('documents'), list):
        raise ValueError('OCS state needs an explicit documents list')
    documents = []
    for row in state['documents']:
        if not isinstance(row, dict) or row.get('id') is None:
            raise ValueError('Each open document needs an identity')
        documents.append({'id': row['id'], 'path': portableize(row.get('path'), roots),
                          'dirty': row.get('dirty')})
    if len({row['id'] for row in documents}) != len(documents):
        raise ValueError('OCS document identities must be unique')
    return {
        'document_id': state.get('document_id'),
        'revision': state.get('revision'),
        'geometry_revision': state.get('geometry_revision'),
        'command': state.get('command'), 'modal': state.get('modal'),
        'documents': documents,
    }


def check_audit(audit, expected_total, expected_by_type=None):
    """Check the entity count and reject reported audit errors or unknowns."""
    if not isinstance(audit, dict) or audit.get('ok') is not True:
        raise ValueError('Native audit did not report success')
    manifest = audit.get('manifest')
    summary = audit.get('summary')
    if summary != {'errors': 0, 'warnings': 0}:
        raise ValueError('Native audit must report zero errors and warnings')
    for label, record in (('audit', audit), ('manifest', manifest)):
        if not isinstance(record, dict):
            continue
        for field in ('errors', 'unknown', 'unknown_entities', 'dropped', 'dropped_entities'):
            value = record.get(field)
            if value not in (None, False, 0, [], {}):
                raise ValueError('Native ' + label + ' reports ' + field)
    if not isinstance(manifest, dict) or manifest.get('total') != expected_total:
        raise ValueError('Native audit entity count differs from expected total')
    by_type = manifest.get('by_type')
    if expected_by_type is not None and by_type != expected_by_type:
        raise ValueError('Native audit entity types differ from expected types')
    return {'result': 'PASS', 'total': expected_total, 'by_type': by_type}


def validate_save_receipt(receipt, output, expected_by_type):
    """Validate the real save/reopen return and every reported dropped count."""
    if not isinstance(receipt, dict) or receipt.get('result') != 'PASS' \
            or receipt.get('stage') != 'reopened':
        raise ValueError('save_reopen did not return a reopened PASS receipt')
    saved = receipt.get('save')
    reopened_audit = receipt.get('reopened_audit')
    if not isinstance(saved, dict) or not isinstance(reopened_audit, dict):
        raise ValueError('save_reopen receipt needs saved result and reopened audit')
    if saved.get('verified') is not True:
        raise ValueError('Saved file is not marked verified')
    if saved.get('ok') is False or saved.get('status') in {'failed', 'rejected', 'error'}:
        raise ValueError('Saved-file result reports failure')
    if saved.get('target_format') not in (None, 'dwg'):
        raise ValueError('Saved-file target format differs from DWG')
    dropped = []

    def collect(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key == 'dropped_on_save':
                    dropped.append(item)
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)

    collect({'save': saved, 'reopened_audit': reopened_audit})
    if not dropped or any(value != 0 for value in dropped):
        raise ValueError('Save result must report zero dropped entities at every location')
    file_hash = sha256(output)
    if saved.get('sha256') != file_hash or receipt.get('sha256', file_hash) != file_hash:
        raise ValueError('save_reopen file hash differs from the output file')
    if saved.get('bytes') is not None and saved['bytes'] != Path(output).stat().st_size:
        raise ValueError('save_reopen byte count differs from the output file')
    saved_manifest = saved.get('manifest')
    if not isinstance(saved_manifest, dict) or saved_manifest.get('by_type') != expected_by_type:
        raise ValueError('Saved entity manifest differs from expected type counts')
    check_audit(reopened_audit, sum(expected_by_type.values()), expected_by_type)
    if reopened_audit['manifest'] != saved_manifest:
        raise ValueError('Reopened manifest differs from saved manifest')
    if isinstance(saved.get('audit'), dict):
        check_audit(saved['audit'], sum(expected_by_type.values()), expected_by_type)
    return {'result': 'PASS', 'sha256': file_hash, 'bytes': Path(output).stat().st_size,
            'dropped_on_save_observations': dropped}


def sab_reader_preflight():
    """Import saved-body readers in this process before any OCS write."""
    try:
        import ezdxf
        from ezdxf.acis.sab import parse_sab, SabDataLoader  # noqa: F401
    except ImportError as error:
        raise RuntimeError(
            'Saved-body reader preflight failed before OCS writes: import '
            'ezdxf.acis.sab.parse_sab and SabDataLoader in this interpreter.') from error
    return {'result': 'PASS',
            'checks': ['ezdxf.acis.sab.parse_sab import',
                       'ezdxf.acis.sab.SabDataLoader import'],
            'ezdxf_version': getattr(ezdxf, '__version__', 'UNKNOWN')}


class RecoveringClient:
    """Proxy that recovers the original request identity after uncertainty."""

    def __init__(self, client):
        object.__setattr__(self, '_client', client)

    def __getattr__(self, name):
        return getattr(self._client, name)

    def __setattr__(self, name, value):
        if name == '_client':
            object.__setattr__(self, name, value)
        else:
            setattr(self._client, name, value)

    def mutate(self, label, operation, allow_wait=False, **fields):
        from cadtools.runtime import Uncertain
        try:
            return self._client.mutate(label, operation, allow_wait=allow_wait, **fields)
        except Uncertain:
            return self._client.recover(self._client.namespace + ':' + label,
                                        allow_wait=allow_wait)


def run(args):
    job_dir = args.job_dir.resolve()
    job_path = args.job.resolve()
    roots = parse_roots(args.root)
    if args.modeling_root_name not in roots:
        raise ValueError('--modeling-root-name must refer to a caller-supplied root')
    output = resolve_locator(args.output, roots, job_path.parent)
    write_gate = check_write_targets(output, job_dir, args.allow_write)

    modeling_root = roots[args.modeling_root_name]
    sys.path[:0] = [str(modeling_root / 'scripts'), str(args.cadtools_root.resolve())]
    job, params, readiness = resolve_runtime_job(job_path, roots)
    metadata_lines = expected_metadata(job)
    job_locator = source_locator(job_path, roots)
    job_dir_locator = source_locator(job_dir, roots)
    progress_path = job_dir / 'progress.json'
    progress_snapshot = None
    if progress_path.is_file():
        progress_snapshot = json.loads(progress_path.read_text(encoding='utf-8'))
        if not isinstance(progress_snapshot, dict):
            raise ValueError('Existing progress.json must contain an object')
        json.dumps(progress_snapshot, ensure_ascii=False, allow_nan=False)
    occurrence_id = job['namespace'] + ':native-envelope-save-reopen'
    occurrence_path = job_dir / 'action-occurrences.jsonl'
    if args.allow_write and occurrence_path.is_file():
        for line in occurrence_path.read_text(encoding='utf-8').splitlines():
            if json.loads(line).get('occurrence_id') == occurrence_id:
                raise FileExistsError('Native action occurrence already exists; inspect existing receipts')
    if job.get('output_path'):
        job_output = resolve_locator(job['output_path'], roots, job_path.parent)
        if output != job_output:
            raise ValueError('--output conflicts with the external job output_path')

    # Check saved-body readers before OCS helper loading or session discovery.
    sab = sab_reader_preflight()
    cadtools_root = args.cadtools_root.resolve()
    if not (cadtools_root / 'cadtools/runtime.py').is_file() \
            or not (cadtools_root / 'cadtools/verification.py').is_file():
        raise FileNotFoundError('--cadtools-root must contain cadtools/runtime.py and verification.py')
    from cadtools.runtime import Client, Journal, load_helper
    from cadtools.verification import save_reopen
    from envelope_reference import build_envelope, inspect
    from source_metadata import compare_source_metadata

    control = args.control.resolve()
    helper = load_helper(control)
    descriptors = helper.descriptors(session=args.session)
    if len(descriptors) != 1:
        raise RuntimeError('Expected exactly one selected OCS session')
    descriptor = descriptors[0]
    prior = helper.request(descriptor, {'op': 'state'}, 30)
    if not prior.get('ok') or prior.get('document_id') is None:
        raise RuntimeError('Could not read OCS session state')
    if prior.get('command') or prior.get('modal'):
        raise RuntimeError('Active OCS command/modal state must be clear')
    before_snapshot = document_snapshot(prior, roots)
    prior_id = before_snapshot['document_id']
    documents_before = {row['id']: {'path': row.get('path'), 'dirty': row.get('dirty')}
                        for row in before_snapshot['documents']}
    preflight = {
        'result': 'PASS', 'part_id': job['part_id'], 'part_name': job['part_name'],
        'mode': write_gate['mode'], 'source_readiness': readiness,
        'source_dimensions_mm': params['dimensions'], 'origin_mm': params['origin'],
        'geometry_scope': job.get('envelope_scope'), 'sab_reader_preflight': sab,
        'session_id': descriptor['session_id'],
        'active_document_before': before_snapshot,
        'output_path': source_locator(output, roots),
        'executing_model': args.execution_model,
        'source_resolution': 'Runtime feature paths resolve from the explicit root map; stored inputs and metadata keep portable locators.',
    }
    write_json(job_dir / 'native-preflight.json', preflight)
    if not args.allow_write:
        return preflight

    journal_path = job_dir / 'ocs-journal.jsonl'
    client = RecoveringClient(Client(helper, descriptor, prior_id, job['namespace'],
                                      Journal(journal_path), allow_write=True, timeout=60))
    created = client.mutate('create-isolated-document', 'new')
    state = helper.request(descriptor, {'op': 'state'}, 30)
    if not state.get('ok') or state.get('document_id') in (None, prior_id):
        raise RuntimeError('Isolated native document did not become active')
    state_snapshot = document_snapshot(state, roots)
    for identity, old in documents_before.items():
        row = next((item for item in state_snapshot.get('documents', [])
                    if item.get('id') == identity), None)
        if row is None or row.get('path') != old['path'] or row.get('dirty') != old['dirty']:
            raise RuntimeError('An existing document changed or disappeared during setup')
    client.document_id = state['document_id']
    empty = client.read('audit', target_format='dwg', target_version='2018')
    check_audit(empty, 0)
    client.mutate('set-millimetre-insunits', 'sysvar', set={'INSUNITS': 4})
    client.mutate('set-world-ucs', 'run', cmd='UCS W')
    handle = build_envelope(client, job)
    from envelope_reference import geometry
    geometry(client).metadata(job['geometry_name'] + ' complete source binding',
                              [handle], metadata_lines)
    records, geometry_check = inspect(client, {'envelope': handle}, job)
    metadata_check = compare_source_metadata(records['records'][0], str(handle),
                                             'CADTOOLS_SOURCE', metadata_lines)
    if geometry_check['result'] != 'PASS' or metadata_check['result'] != 'PASS':
        raise RuntimeError('Pre-save geometry or source-metadata check failed')
    audit = client.read('audit', target_format='dwg', target_version='2018')
    check_audit(audit, 1, {'3D Solid': 1})
    write_json(job_dir / 'native-handles.json', {'envelope': handle})
    write_json(job_dir / 'pre-save-records.json', portableize(records, roots))
    write_json(job_dir / 'pre-save-feature-checks.json', portableize(geometry_check, roots))
    write_json(job_dir / 'pre-save-source-metadata-check.json', portableize(metadata_check, roots))

    persisted = save_reopen(client, str(output), {'3D Solid': 1})
    persistence_check = validate_save_receipt(persisted, output, {'3D Solid': 1})
    reopened_records, reopened_geometry = inspect(client, {'envelope': handle}, job)
    reopened_metadata = compare_source_metadata(reopened_records['records'][0], str(handle),
                                                'CADTOOLS_SOURCE', metadata_lines)
    if reopened_geometry['result'] != 'PASS' or reopened_metadata['result'] != 'PASS':
        raise RuntimeError('Reopened geometry or source-metadata check failed')
    result = {
        'state': 'REFERENCE_DONE', 'part_id': job['part_id'],
        'part_name': job['part_name'], 'representation': job['representation'],
        'geometry_role': job['geometry_role'], 'envelope_scope': job.get('envelope_scope'),
        'executing_model': args.execution_model,
        'dimensions_mm': params['dimensions'], 'origin_mm': params['origin'],
        'local_frame': job['local_frame'], 'native_handle': handle,
        'document_id': reopened_geometry['document_id'],
        'document_revision': reopened_geometry['document_revision'],
        'geometry_revision': reopened_geometry['geometry_revision'],
        'pre_save_geometry': geometry_check, 'pre_save_metadata': metadata_check,
        'reopened_geometry': reopened_geometry,
        'reopened_metadata': reopened_metadata, 'save_reopen': portableize(persisted, roots),
        'persistence_check': persistence_check,
        'native_model': source_locator(output, roots),
        'native_model_sha256': sha256(output), 'native_model_bytes': output.stat().st_size,
        'helper_sha256': sha256(Path(__file__)),
        'envelope_helper_sha256': sha256(modeling_root / 'scripts/envelope_reference.py'),
    }
    write_json(job_dir / 'reopened-records.json', portableize(reopened_records, roots))
    write_json(job_dir / 'reopened-feature-checks.json', portableize(reopened_geometry, roots))
    write_json(job_dir / 'reopened-source-metadata-check.json', portableize(reopened_metadata, roots))
    write_json(job_dir / 'save-reopen.json', portableize(persisted, roots))
    write_json(job_dir / 'result.json', portableize(result, roots))
    from component_records import append_occurrence
    source_inputs = [job_locator, *job['_resolved_source_locators']]
    occurrence = {
        'occurrence_id': occurrence_id, 'job_id': job['job_id'],
        'part_id': job['part_id'], 'part_name': job['part_name'],
        'action_id': 'build-source-bound-reference-envelope',
        'action_name': 'Build, verify, save and reopen one source-bound reference envelope',
        'inputs': sorted(set(source_inputs)),
        'outputs': [source_locator(output, roots),
                    source_locator(job_dir / 'pre-save-feature-checks.json', roots),
                    source_locator(job_dir / 'reopened-feature-checks.json', roots),
                    source_locator(job_dir / 'save-reopen.json', roots)],
        'prerequisites': ['Source readiness and source hashes pass',
                          'SAB reader imports pass in the execution interpreter',
                          'Explicit native-write authorization and selected OCS session'],
        'software': ['OpenCADStudio through guarded cadtools Client/Journal',
                     'scripts/envelope_reference.py', 'scripts/source_metadata.py',
                     'cadtools.verification.save_reopen'],
        'agent': args.execution_model,
        'representation': job['representation'], 'units': job['units'],
        'frame': job['local_frame'],
        'preserved': ['Existing open OCS documents',
                      'External source originals and their recorded hashes',
                      'External job and portable source locators'],
        'changed_or_inferred': ['Created one axis-aligned reference envelope from the external job source dimensions',
                                'Used the external job origin and local frame conventions'],
        'alternatives': job.get('alternatives',
                                ['Detailed component geometry requires a separate source-backed construction job']),
        'downstream': job.get('downstream', []),
        'checks': {'pre_save_geometry': geometry_check,
                   'pre_save_source_metadata': metadata_check,
                   'reopened_geometry': reopened_geometry,
                   'reopened_source_metadata': reopened_metadata,
                   'persistence_check': persistence_check,
                   'save_reopen': portableize(persisted, roots),
                   'native_model_sha256': result['native_model_sha256']},
        'result': 'PASS',
        'evidence': [source_locator(job_dir / 'result.json', roots),
                     job_locator,
                     source_locator(job_dir / 'pre-save-feature-checks.json', roots),
                     source_locator(job_dir / 'reopened-feature-checks.json', roots)],
    }
    append_occurrence(occurrence_path, occurrence)
    if progress_snapshot is not None:
        progress = progress_snapshot
        progress.update({
            'status': 'REFERENCE_DONE', 'stage': 'NATIVE_BUILD_SAVED_AND_REOPENED_PASS',
            'native_model_created': True,
            'native_model': source_locator(output, roots),
            'result_path': source_locator(job_dir / 'result.json', roots),
            'native_action_occurrence': occurrence_id,
            'native_model_sha256': result['native_model_sha256'],
        })
        write_json(progress_path, progress)
    return portableize(result, roots)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--job', required=True, type=Path)
    parser.add_argument('--job-dir', required=True, type=Path)
    parser.add_argument('--output', required=True)
    parser.add_argument('--session', required=True)
    parser.add_argument('--control', required=True, type=Path)
    parser.add_argument('--cadtools-root', required=True, type=Path,
                        help='Explicit directory containing cadtools/runtime.py')
    parser.add_argument('--modeling-root-name', required=True,
                        help='Caller-supplied root name containing reusable scripts')
    parser.add_argument('--execution-model', required=True,
                        help='Actual execution-model identity supplied by the caller')
    parser.add_argument('--root', action='append', default=[], metavar='NAME=ABSOLUTE_PATH')
    parser.add_argument('--allow-write', action='store_true')
    args = parser.parse_args(argv)
    try:
        print(json.dumps(run(args), indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(json.dumps({'result': 'FAIL', 'error': str(error)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
