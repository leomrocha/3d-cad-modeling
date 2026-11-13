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
        if not separator or name not in {'FERME_ROOT', 'MODELING_ROOT'}:
            raise ValueError('--root accepts FERME_ROOT=ABSOLUTE_PATH or MODELING_ROOT=ABSOLUTE_PATH')
        path = Path(value)
        if not path.is_absolute() or name in roots:
            raise ValueError('Each named root must be an explicit unique absolute path')
        roots[name] = path.resolve()
    if set(roots) != {'FERME_ROOT', 'MODELING_ROOT'}:
        raise ValueError('Supply both FERME_ROOT and MODELING_ROOT roots')
    return roots


def resolve_locator(locator, roots):
    value = str(locator)
    match = re.match(r'^\$\{([A-Za-z_][A-Za-z0-9_]*)\}/(.*)$', value)
    if match:
        name, suffix = match.groups()
        if name not in roots:
            raise ValueError('Missing caller-supplied path root: ' + name)
        return (roots[name] / suffix).resolve()
    path = Path(value)
    if not path.is_absolute():
        path = roots['FERME_ROOT'] / path
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
    for feature in runtime_job['features']:
        if not isinstance(feature, dict) or not feature.get('source'):
            raise ValueError('Each job feature requires a source locator')
        feature['source'] = str(resolve_locator(feature['source'], roots))
    runtime_job['_portable_features'] = portable_features
    from component_records import require_ready
    from envelope_reference import parameters
    readiness = require_ready(runtime_job)
    parameters_value = parameters(runtime_job)
    return runtime_job, parameters_value, portableize(readiness, roots)


def expected_metadata(job):
    lines = ['Part ID: ' + job['part_id'], job['part_name'], job['representation'],
             'Reference envelope; units ' + job['units'],
             'Local frame: ' + job['local_frame'],
             'Source job: ' + job['job_id']]
    if job.get('envelope_scope'):
        lines.append('Envelope scope: ' + job['envelope_scope'])
    for feature in job.get('_portable_features', job['features']):
        lines.extend([
            'Source feature: ' + feature['name'] + ' = ' +
            format(feature['value'], '.12g') + ' ' + feature['unit'],
            'Source: ' + feature['source'] + ' SHA-256 ' + feature['source_sha256'],
            'Source location: ' + feature['source_location'],
        ])
    return lines


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
    output = resolve_locator(args.output, roots)
    write_gate = check_write_targets(output, job_dir, args.allow_write)

    modeling_root = roots['MODELING_ROOT']
    sys.path[:0] = [str(modeling_root / 'scripts'), str(args.cadtools_root.resolve())]
    job, params, readiness = resolve_runtime_job(job_path, roots)
    if job.get('output_path'):
        job_output = resolve_locator(job['output_path'], roots)
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
    prior_id = prior['document_id']
    documents_before = {row['id']: {'path': row.get('path'), 'dirty': row.get('dirty')}
                        for row in prior.get('documents', [])}
    preflight = {
        'result': 'PASS', 'part_id': job['part_id'], 'part_name': job['part_name'],
        'mode': write_gate['mode'], 'source_readiness': readiness,
        'source_dimensions_mm': params['dimensions'], 'origin_mm': params['origin'],
        'geometry_scope': job.get('envelope_scope'), 'sab_reader_preflight': sab,
        'session_id': descriptor['session_id'],
        'active_document_before': portableize(prior, roots),
        'output_path': source_locator(output, roots),
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
    for identity, old in documents_before.items():
        row = next((item for item in state.get('documents', [])
                    if item.get('id') == identity), None)
        if row is None or row.get('path') != old['path'] or row.get('dirty') != old['dirty']:
            raise RuntimeError('An existing document changed or disappeared during setup')
    client.document_id = state['document_id']
    empty = client.read('audit', target_format='dwg', target_version='2018')
    if empty.get('manifest', {}).get('total') != 0:
        raise RuntimeError('New document is not empty')
    client.mutate('set-millimetre-insunits', 'sysvar', set={'INSUNITS': 4})
    client.mutate('set-world-ucs', 'run', cmd='UCS W')
    handle = build_envelope(client, job)
    from envelope_reference import geometry
    metadata_lines = expected_metadata(job)
    geometry(client).metadata(job['geometry_name'] + ' source metadata',
                              [handle], metadata_lines)
    records, geometry_check = inspect(client, {'envelope': handle}, job)
    metadata_check = compare_source_metadata(records['records'][0], str(handle),
                                             'CADTOOLS_SOURCE', metadata_lines)
    if geometry_check['result'] != 'PASS' or metadata_check['result'] != 'PASS':
        raise RuntimeError('Pre-save geometry or source-metadata check failed')
    audit = client.read('audit', target_format='dwg', target_version='2018')
    if audit.get('manifest', {}).get('total') != 1:
        raise RuntimeError('Pre-save audit did not find exactly one native solid')
    write_json(job_dir / 'native-handles.json', {'envelope': handle})
    write_json(job_dir / 'pre-save-records.json', portableize(records, roots))
    write_json(job_dir / 'pre-save-feature-checks.json', portableize(geometry_check, roots))
    write_json(job_dir / 'pre-save-source-metadata-check.json', portableize(metadata_check, roots))

    persisted = save_reopen(client, str(output), {'3D Solid': 1})
    reopened_records, reopened_geometry = inspect(client, {'envelope': handle}, job)
    reopened_metadata = compare_source_metadata(reopened_records['records'][0], str(handle),
                                                'CADTOOLS_SOURCE', metadata_lines)
    if reopened_geometry['result'] != 'PASS' or reopened_metadata['result'] != 'PASS':
        raise RuntimeError('Reopened geometry or source-metadata check failed')
    result = {
        'state': 'REFERENCE_DONE', 'part_id': job['part_id'],
        'part_name': job['part_name'], 'representation': job['representation'],
        'geometry_role': job['geometry_role'], 'envelope_scope': job.get('envelope_scope'),
        'dimensions_mm': params['dimensions'], 'origin_mm': params['origin'],
        'local_frame': job['local_frame'], 'native_handle': handle,
        'document_id': reopened_geometry['document_id'],
        'document_revision': reopened_geometry['document_revision'],
        'geometry_revision': reopened_geometry['geometry_revision'],
        'pre_save_geometry': geometry_check, 'pre_save_metadata': metadata_check,
        'reopened_geometry': reopened_geometry,
        'reopened_metadata': reopened_metadata, 'save_reopen': portableize(persisted, roots),
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
