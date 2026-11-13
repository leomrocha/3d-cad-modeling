import hashlib
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import annular_job_runner as runner


class FakeSessionHelper:
    READ_OPS = {'state'}

    def __init__(self, initial_path=None):
        self.calls = []
        self.state = {
            'ok': True, 'document_id': 17, 'revision': 4, 'geometry_revision': 2,
            'command': None, 'modal': None,
            'documents': [{'id': 17, 'path': str(initial_path) if initial_path else None,
                           'dirty': False}],
        }

    def descriptors(self, session):
        self.calls.append(('descriptors', session))
        return [{'session_id': 'synthetic-session'}]

    def request(self, descriptor, payload, timeout):
        self.calls.append(('request', payload['op']))
        return dict(self.state)

    def execute_checked(self, *args, **kwargs):
        self.calls.append(('MUTATION',))
        raise AssertionError('Read-only preflight must not call execute_checked')


class AnnularJobRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'component_project'
        self.project.mkdir()
        self.source_dir = self.project / 'sources'
        self.source_dir.mkdir()
        self.job_dir = self.project / 'jobs' / 'annular'
        self.job_dir.mkdir(parents=True)
        self.output_dir = self.project / 'cad' / 'parts'
        self.output_dir.mkdir(parents=True)
        self.index = self.project / 'parts.json'
        self.index.write_text('{}', encoding='utf-8')
        self.work_index = self.project / 'component-work.json'
        self.work_index.write_text('{}', encoding='utf-8')
        self.cad_root = self.project / 'cad'
        self.project_root = self.project
        self.source = self.source_dir / 'source-a.txt'
        self.source.write_text('synthetic source observation', encoding='utf-8')
        self.digest = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.job_path = self.job_dir / 'source-job.json'
        self.job_path.write_text(json.dumps(self.job()), encoding='utf-8')
        self.output = self.output_dir / 'annular-reference.dwg'
        self.control = self.base / 'control.py'
        self.control.write_text('# test helper path', encoding='utf-8')
        self.cadtools = self.base / 'cadtools'
        (self.cadtools / 'cadtools').mkdir(parents=True)
        for name in ('runtime.py', 'geometry.py', 'verification.py'):
            (self.cadtools / 'cadtools' / name).write_text('', encoding='utf-8')
        self.helper = FakeSessionHelper()

    def job(self):
        names = {'bore_diameter': 'bore', 'outside_diameter': 'outside',
                 'thickness': 'thickness'}
        values = {'bore': 4.0, 'outside': 9.0, 'thickness': 1.25}
        return {
            'job_id': 'synthetic-annular-job', 'namespace': 'synthetic-annulus-test',
            'part_id': 'SAMPLE-PART-17', 'part_name': 'Sample annular part',
            'representation': 'Nominal annular reference',
            'geometry_role': 'reference_annulus', 'geometry_name': 'Sample annulus',
            'units': 'mm', 'frame': 'XY plane with +Z thickness',
            'local_frame': 'Center at origin; lower face at Z=0; axis +Z',
            'metadata_application': 'CADTOOLS_SOURCE',
            'metadata_request_label': 'Sample annulus source binding',
            'center': [0.0, 0.0], 'z_origin': 0.0,
            'construction': {'cutter_overrun_mm': 0.5},
            'readback_tolerance': 1e-7,
            'dimension_features': names,
            'features': [
                {'name': name, 'required': True, 'value': values[name], 'unit': 'mm',
                 'source': str(self.source), 'source_sha256': self.digest,
                 'source_location': 'synthetic drawing row ' + name,
                 'evidence_status': 'synthetic_test_fixture'}
                for name in names.values()
            ],
        }

    def args(self, **changes):
        values = dict(
            job=self.job_path, job_dir=self.job_dir,
            output='${PROJECT_ROOT}/cad/parts/annular-reference.dwg',
            index=self.index, work_index=self.work_index,
            cad_root=self.cad_root, project_root=self.project_root,
            cadtools_root=self.cadtools, control=self.control,
            session='synthetic-session', execution_model='synthetic-test-model',
            root=[f'PROJECT_ROOT={self.project}'], allow_write=False,
            configuration=None,
        )
        values.update(changes)
        return SimpleNamespace(**values)

    def fake_runtime_modules(self):
        package = types.ModuleType('cadtools')
        package.__path__ = []
        runtime = types.ModuleType('cadtools.runtime')
        runtime.load_helper = lambda path: self.helper
        geometry = types.ModuleType('cadtools.geometry')
        verification = types.ModuleType('cadtools.verification')
        return {'cadtools': package, 'cadtools.runtime': runtime,
                'cadtools.geometry': geometry, 'cadtools.verification': verification}

    def test_readonly_preflight_writes_record_without_native_mutation(self):
        with patch.dict(sys.modules, self.fake_runtime_modules()), \
                patch.object(runner, 'sab_reader_preflight', return_value={'result': 'PASS'}), \
                patch.object(runner, 'model_gate', return_value={
                    'part_id': 'SAMPLE-PART-17', 'action': 'NEW_MODEL_REQUIRED',
                    'models': [], 'candidates': []}):
            result = runner.run(self.args())
        self.assertEqual(result['mode'], 'READ_ONLY_PREFLIGHT')
        self.assertEqual(result['native_mutations'], 0)
        self.assertTrue((self.job_dir / 'native-preflight.json').is_file())
        self.assertNotIn(('MUTATION',), self.helper.calls)
        self.assertEqual([entry for entry in self.helper.calls if entry[0] == 'request'],
                         [('request', 'state')])

    def test_source_hash_change_blocks_before_session_discovery(self):
        self.source.write_text('changed source', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Source revision changed'):
            runner.resolve_job(self.job_path, {'PROJECT_ROOT': self.project})

    def test_source_change_after_preflight_is_detected_before_native_write(self):
        prepared = runner.resolve_job(self.job_path, {'PROJECT_ROOT': self.project})
        prepared.update(roots={'PROJECT_ROOT': self.project})
        self.source.write_text('changed after preflight', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'changed after preflight'):
            runner.verify_source_pins(prepared)

    def test_request_namespace_and_generated_labels_are_bounded(self):
        job = self.job()
        job['namespace'] = 'n' * 64
        job['geometry_name'] = 'g' * 70
        with self.assertRaisesRegex(ValueError, '128 UTF-8 bytes'):
            runner.validate_request_labels(job)

    def test_native_read_epoch_guard_rejects_changed_geometry_revision(self):
        client = SimpleNamespace(read=lambda op: {
            'document_id': 9, 'revision': 12, 'geometry_revision': 21})
        with self.assertRaisesRegex(RuntimeError, 'Geometry revision changed'):
            runner._verify_stable_state(client, 9, 12, 20)

    def test_point_persistence_preserves_sub_1e7_differences(self):
        check = runner._compare_point_sets([[5e-8, 0.0, 0.0]], [[0.0, 0.0, 0.0]], 1e-10)
        self.assertEqual(check['result'], 'FAIL')

    def test_point_persistence_matches_unordered_vertices_one_to_one(self):
        check = runner._compare_point_sets(
            [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            [[0.0, 0.0, 0.0], [1.0 + 2e-8, 0.0, 0.0]], 1e-7)
        self.assertEqual(check['result'], 'PASS')
        self.assertEqual(len(check['matches']), 2)

    def test_empty_sab_uses_valid_sat_pre_save_vertices(self):
        record = {'properties': {'acis_data': {'sab_data': [], 'sat_data': 'synthetic SAT'}}}
        with patch.dict(sys.modules, {
                'annular_reference': types.SimpleNamespace(verify=lambda features, job: {}),
                'native_acis': types.SimpleNamespace(sab_features=lambda *a, **k: self.fail('empty SAB decoded')),
                'step_placements': types.SimpleNamespace(
                    identity_sat_vertices=lambda sat: [[0.0, 0.0, 0.0]])}):
            result = runner._pre_save_geometry(record, self.job())
        self.assertEqual(result['format'], 'SAT')
        self.assertEqual(result['points'], [[0.0, 0.0, 0.0]])
        self.assertEqual(result['geometry_status'], 'OBSERVED')

    def test_empty_sab_without_sat_fails_before_save(self):
        record = {'properties': {'acis_data': {'sab_data': b'', 'sat_data': ''}}}
        with self.assertRaisesRegex(ValueError, 'neither nonempty SAB nor valid SAT'):
            runner._pre_save_geometry(record, self.job())

    def test_nonempty_sab_is_retained_before_decoder_access(self):
        order = []
        record = {'properties': {'acis_data': {'sab_data': b'abc', 'sat_data': ''}}}
        modules = {
            'annular_reference': types.SimpleNamespace(verify=lambda features, job: {'result': 'PASS'}),
            'native_acis': types.SimpleNamespace(
                sab_features=lambda raw, **kwargs: (order.append('decode') or {'points': [[0, 0, 0]]})),
            'step_placements': types.SimpleNamespace(identity_sat_vertices=lambda sat: []),
        }
        with patch.dict(sys.modules, modules):
            result = runner._pre_save_geometry(
                record, self.job(), lambda raw: (order.append('retain') or raw))
        self.assertEqual(order, ['retain', 'decode'])
        self.assertEqual(result['format'], 'SAB')

    def test_resume_requires_exact_readable_part_name(self):
        with self.assertRaisesRegex(ValueError, 'part_name differs'):
            runner._validate_resume_part_name(
                {'part_name': 'Selected source part'}, {'part_name': 'Different row'})
        runner._validate_resume_part_name(
            {'part_name': 'Selected source part'}, {'part_name': 'Selected source part'})

    def test_resume_checkpoint_rejects_any_save_intent_or_receipt(self):
        job = self.job()
        fixture = self.make_resume_checkpoint(job)
        with self.assertRaisesRegex(ValueError, 'save or reopen request already has an intent'):
            runner._resume_checkpoint(self.job_dir, job, fixture['source_job_sha256'],
                                      self.output, {'PROJECT_ROOT': self.project})

    def test_resume_checkpoint_requires_terminal_journal_responses(self):
        job = self.job()
        fixture = self.make_resume_checkpoint(job, save_intent=False)
        journal = self.job_dir / 'ocs-journal.jsonl'
        rows = [json.loads(line) for line in journal.read_text().splitlines()]
        for row in rows:
            if row.get('event') == 'response' \
                    and row.get('request_id') == job['namespace'] + ':capture-pre-save-viewport':
                row['response'] = {'status': 'running'}
        journal.write_text(''.join(json.dumps(row) + '\n' for row in rows), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'metadata and capture requests completed'):
            runner._resume_checkpoint(self.job_dir, job, fixture['source_job_sha256'],
                                      self.output, {'PROJECT_ROOT': self.project})

    def test_resume_preflight_checks_current_document_without_native_mutation(self):
        job = self.job()
        fixture = self.make_resume_checkpoint(job, save_intent=False)
        docs = [{'id': 1, 'path': None, 'dirty': False},
                {'id': 166, 'path': None, 'dirty': True}]
        self.helper.state.update({'document_id': 166, 'revision': 5,
                                  'geometry_revision': 99,
                                  'documents': docs, 'command': None, 'modal': None})
        modules = self.fake_runtime_modules()
        for name in ('native_acis', 'source_metadata', 'ocs_document_cleanup'):
            modules[name] = types.ModuleType(name)
        row = {'part_id': job['part_id'], 'part_name': job['part_name'],
               'configuration': None, 'action': 'NEW_MODEL_REQUIRED',
               'models': [], 'candidates': []}
        with patch.dict(sys.modules, modules), \
                patch.object(runner, 'sab_reader_preflight', return_value={'result': 'PASS'}), \
                patch.object(runner, 'model_gate', return_value=row):
            result, prepared = runner.prepare(self.args(allow_write=True, resume_pre_save=True))
        self.assertEqual(result['mode'], 'RESUME_PRE_SAVE')
        self.assertEqual(prepared['active_document_id'], 166)
        self.assertEqual(prepared['resume_checkpoint']['handle'], '7E')
        self.assertNotIn(('MUTATION',), self.helper.calls)
        original_failure = (self.job_dir / 'native-failure.json').read_bytes()
        original_body = (self.job_dir / 'pre-save-body.sab').read_bytes()
        self.assertEqual(original_body, b'')
        self.assertEqual((self.job_dir / 'native-failure.json').read_bytes(), original_failure)
        journal = self.job_dir / 'ocs-journal.jsonl'
        journal.write_text('', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'metadata and capture requests completed'):
            runner._resume_checkpoint(self.job_dir, job, fixture['source_job_sha256'],
                                      self.output, {'PROJECT_ROOT': self.project})

    def test_resume_execution_skips_new_build_and_capture_and_preserves_failure(self):
        job = self.job()
        self.make_resume_checkpoint(job, save_intent=False)
        state = {'ok': True, 'document_id': 166, 'revision': 5,
                 'geometry_revision': 99, 'command': None, 'modal': None,
                 'documents': [{'id': 1, 'path': None, 'dirty': False},
                               {'id': 166, 'path': None, 'dirty': True}]}
        self.helper.state.update(state)
        record = json.loads((self.job_dir / 'pre-save-entity-response.json').read_text())['records'][0]
        response = {'ok': True, 'document_id': 166, 'revision': 5,
                    'geometry_revision': 99, 'records': [record]}
        class ReadOnlyFakeClient:
            document_id = 166
            def __init__(self):
                self.calls = []
            def read(inner_self, op, **kwargs):
                inner_self.calls.append(('read', op))
                if op == 'state':
                    return dict(state)
                if op == 'records':
                    return response
                return {'ok': True}
            def mutate(inner_self, *args, **kwargs):
                inner_self.calls.append(('MUTATION', args, kwargs))
                raise AssertionError('Resume validation must not mutate before save_reopen')
        client = ReadOnlyFakeClient()
        modules = self.fake_runtime_modules()
        modules['cadtools.runtime'].Client = lambda *args, **kwargs: client
        modules['cadtools.runtime'].Journal = lambda *args, **kwargs: object()
        annular = types.ModuleType('annular_reference')
        annular.build_annulus = lambda *args, **kwargs: self.fail('resume rebuilt geometry')
        annular.inspect = lambda *args, **kwargs: self.fail('should stop at save_reopen')
        annular.verify = lambda *args, **kwargs: {}
        annular.verify_metadata = lambda *args, **kwargs: {'result': 'PASS'}
        annular.parameters = lambda job: {
            'dimensions': {'bore_diameter': 4.0, 'outside_diameter': 9.0, 'thickness': 1.25},
            'tolerance': 1e-7}
        modules['annular_reference'] = annular
        modules['native_acis'] = types.ModuleType('native_acis')
        modules['native_acis'].sab_features = lambda *args, **kwargs: self.fail('empty SAB decoded')
        modules['step_placements'] = types.ModuleType('step_placements')
        modules['step_placements'].identity_sat_vertices = lambda *args: [[0.0, 0.0, 0.0]]
        modules['source_metadata'] = types.ModuleType('source_metadata')
        modules['ocs_document_cleanup'] = types.ModuleType('ocs_document_cleanup')
        modules['cadtools.verification'].save_reopen = lambda *args, **kwargs: (_ for _ in ()).throw(
            RuntimeError('stop at existing save_reopen stage'))
        row = {'part_id': job['part_id'], 'part_name': job['part_name'],
               'configuration': None, 'action': 'NEW_MODEL_REQUIRED',
               'models': [], 'candidates': []}
        original_failure = (self.job_dir / 'native-failure.json').read_bytes()
        original_body = (self.job_dir / 'pre-save-body.sab').read_bytes()
        with patch.dict(sys.modules, modules), \
                patch.object(runner, 'sab_reader_preflight', return_value={'result': 'PASS'}), \
                patch.object(runner, 'model_gate', return_value=row), \
                patch.object(runner, 'RecoveringClient', side_effect=lambda item: item), \
                patch.object(runner, '_capture', side_effect=AssertionError('resume recaptured viewport')), \
                patch('envelope_job_runner.check_audit', return_value=None):
            _, prepared = runner.prepare(self.args(allow_write=True, resume_pre_save=True))
            with self.assertRaisesRegex(RuntimeError, 'stop at existing save_reopen stage'):
                runner.execute(prepared, self.args(allow_write=True, resume_pre_save=True))
        self.assertFalse(any(call[0] == 'MUTATION' for call in client.calls))
        self.assertEqual((self.job_dir / 'native-failure.json').read_bytes(), original_failure)
        self.assertEqual((self.job_dir / 'pre-save-body.sab').read_bytes(), original_body)
        self.assertTrue((self.job_dir / 'native-resume-failure.json').is_file())

    def make_resume_checkpoint(self, job, *, save_intent=True):
        namespace = job['namespace']
        construction_id, handle = 166, '7E'
        source_job_hash = runner.sha256(self.job_path)
        preflight = {'result': 'PASS', 'job_id': job['job_id'],
                     'request_namespace': namespace, 'source_job_sha256': source_job_hash,
                     'session_id': 'synthetic-session',
                     'active_documents_before': {
                         'document_id': 1, 'revision': 0, 'geometry_revision': 0,
                         'documents': [{'id': 1, 'path': None, 'dirty': False}]}}
        docs = [{'id': 1, 'path': None, 'dirty': False},
                {'id': construction_id, 'path': None, 'dirty': True}]
        state = {'document_id': construction_id, 'revision': 5,
                 'geometry_revision': 99, 'documents': docs}
        record = {'handle': handle, 'type': 'Solid3D', 'properties': {'acis_data': {
            'sab_data': [], 'sat_data': 'valid SAT fixture'}}}
        response = {'document_id': construction_id, 'revision': 5,
                    'geometry_revision': 99, 'records': [record]}
        failure = {'result': 'FAIL', 'stage': 'pre_save_records',
                   'part_id': job['part_id'], 'job_id': job['job_id'],
                   'error': 'Nonempty native SAB bytes required'}
        entries = {
            'native-preflight.json': preflight,
            'document-start.json': {'result': 'PASS', 'units': 'mm', 'INSUNITS': 4,
                                    'UCS': 'world', 'construction_document_id': construction_id,
                                    'construction_documents': docs},
            'native-handles.json': {'annulus': handle},
            'native-failure.json': failure,
            'pre-save-entity-response.json': response,
            'pre-save-read-states.json': {'before': state, 'after': state},
            'pre-save-body.json': {'status': 'CAPTURED_BEFORE_DECODER', 'bytes': 0,
                                   'sha256': hashlib.sha256(b'').hexdigest(),
                                   'handle': handle, 'document_id': construction_id,
                                   'geometry_revision': 99},
            'capture-pre-save.json': {'result': 'CAPTURED', 'geometry_revision': 99},
        }
        for name, value in entries.items():
            (self.job_dir / name).write_text(json.dumps(value), encoding='utf-8')
        (self.job_dir / 'pre-save-body.sab').write_bytes(b'')
        journal = [{'event': 'intent', 'request': {'request_id': namespace + ':capture-pre-save-viewport'}},
                   {'event': 'response', 'request_id': namespace + ':capture-pre-save-viewport',
                    'response': {'status': 'completed'}},
                   {'event': 'intent', 'request': {'request_id': namespace + ':' + job['metadata_request_label']}},
                   {'event': 'response', 'request_id': namespace + ':' + job['metadata_request_label'],
                    'response': {'ok': True, 'error': None, 'result': {'updated': 1}}}]
        if save_intent:
            journal.append({'event': 'intent', 'request': {'request_id': namespace + ':verified-save'}})
        (self.job_dir / 'ocs-journal.jsonl').write_text(
            ''.join(json.dumps(row) + '\n' for row in journal), encoding='utf-8')
        return {'source_job_sha256': source_job_hash}

    def test_model_gate_selects_exact_single_row_and_configuration(self):
        selected = {'part_id': 'SAMPLE-PART-17', 'configuration': 'variant-a',
                    'action': 'NEW_MODEL_REQUIRED', 'models': [], 'candidates': []}
        with patch('model_inventory.audit', return_value={'components': [selected]}) as audit:
            row = runner.model_gate(
                index_path=self.index, work_index=self.work_index,
                cad_root=self.cad_root, project_root=self.project_root,
                roots={'PROJECT_ROOT': str(self.project)},
                part_id='SAMPLE-PART-17', configuration='variant-a')
        self.assertEqual(row, selected)
        self.assertEqual(audit.call_args.kwargs['part_id'], 'SAMPLE-PART-17')
        self.assertEqual(audit.call_args.kwargs['configuration'], 'variant-a')

    def test_model_gate_keeps_other_configuration_and_dependency_rows_as_context(self):
        selected = {'part_id': 'SAMPLE-PART-17', 'configuration': 'variant-b',
                    'action': 'NEW_MODEL_REQUIRED', 'models': [], 'candidates': [],
                    'other_configuration_models': [{'configuration': 'variant-a',
                                                    'model': {'path': 'other.dwg'}}],
                    'dependency_models': [{'path': 'separate-input.dwg'}]}
        with patch('model_inventory.audit', return_value={'components': [selected]}):
            self.assertEqual(runner.model_gate(
                index_path=self.index, work_index=self.work_index,
                cad_root=self.cad_root, project_root=self.project_root,
                roots={'PROJECT_ROOT': str(self.project)},
                part_id='SAMPLE-PART-17', configuration='variant-b'), selected)

    def test_model_gate_rejects_existing_models_candidates_or_ambiguous_rows(self):
        base = {'part_id': 'SAMPLE-PART-17', 'action': 'NEW_MODEL_REQUIRED',
                'models': [], 'candidates': []}
        kwargs = dict(index_path=self.index, work_index=self.work_index,
                      cad_root=self.cad_root, project_root=self.project_root,
                      roots={'PROJECT_ROOT': str(self.project)},
                      part_id='SAMPLE-PART-17')
        for row in (
                {**base, 'action': 'SKIP_EXISTING_MODEL',
                 'models': [{'path': 'existing.dwg'}]},
                {**base, 'candidates': [{'path': 'candidate.dwg'}]}):
            with self.subTest(row=row), patch('model_inventory.audit',
                                              return_value={'components': [row]}):
                with self.assertRaises(FileExistsError):
                    runner.model_gate(**kwargs)
        with patch('model_inventory.audit', return_value={'components': [base, base]}):
            with self.assertRaisesRegex(ValueError, 'exactly one'):
                runner.model_gate(**kwargs)

    def test_existing_output_or_native_receipt_blocks_write_preflight(self):
        self.output.write_bytes(b'existing artifact')
        with self.assertRaises(FileExistsError):
            runner.check_write_targets(self.output, self.job_dir, True)
        self.output.unlink()
        (self.job_dir / 'ocs-journal.jsonl').write_text('{}\n', encoding='utf-8')
        with self.assertRaisesRegex(FileExistsError, 'receipts'):
            runner.check_write_targets(self.output, self.job_dir, True)

    def test_annular_specific_receipt_blocks_write_replay(self):
        (self.job_dir / 'reopened-entity-response.json').write_text('{}', encoding='utf-8')
        with self.assertRaisesRegex(FileExistsError, 'Annular write receipts prohibit replay'):
            runner._annular_write_gate(self.output, self.job_dir, True)

    def test_job_output_conflict_is_rejected(self):
        job = self.job()
        job['output_path'] = '${PROJECT_ROOT}/cad/parts/other.dwg'
        self.job_path.write_text(json.dumps(job), encoding='utf-8')
        with patch.dict(sys.modules, self.fake_runtime_modules()), \
                patch.object(runner, 'sab_reader_preflight', return_value={'result': 'PASS'}), \
                patch.object(runner, 'model_gate', return_value={
                    'part_id': 'SAMPLE-PART-17', 'action': 'NEW_MODEL_REQUIRED',
                    'models': [], 'candidates': []}):
            with self.assertRaisesRegex(ValueError, 'conflicts'):
                runner.prepare(self.args())
        self.assertEqual(self.helper.calls, [])

    def test_nonportable_existing_document_path_fails_preflight(self):
        self.helper.state['documents'][0]['path'] = str(self.base / 'outside-root.dwg')
        with patch.dict(sys.modules, self.fake_runtime_modules()), \
                patch.object(runner, 'sab_reader_preflight', return_value={'result': 'PASS'}), \
                patch.object(runner, 'model_gate', return_value={
                    'part_id': 'SAMPLE-PART-17', 'action': 'NEW_MODEL_REQUIRED',
                    'models': [], 'candidates': []}):
            with self.assertRaisesRegex(ValueError, 'outside caller-supplied'):
                runner.prepare(self.args())


if __name__ == '__main__':
    unittest.main()
