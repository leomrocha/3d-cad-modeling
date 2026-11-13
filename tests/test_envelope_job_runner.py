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
import envelope_job_runner as runner


class FakeHelper:
    READ_OPS = {'audit'}

    def __init__(self, session='test-session'):
        self.session = session
        self.active = 1
        self.calls = []
        self.documents = [{'id': 1, 'path': None, 'dirty': False}]

    def descriptors(self, session):
        self.calls.append(('descriptors', session))
        return [{'session_id': self.session}]

    def request(self, descriptor, payload, timeout):
        self.calls.append(('request', payload['op']))
        return {
            'ok': True, 'document_id': self.active, 'revision': 1,
            'geometry_revision': 1, 'command': None, 'modal': None,
            'documents': list(self.documents),
        }

    def execute_checked(self, *args, **kwargs):
        self.calls.append(('execute_checked',))
        return {'ok': True, 'status': 'completed'}


class FakeClient:
    def __init__(self, helper, descriptor, document_id, namespace, journal,
                 allow_write=False, timeout=30):
        self.helper = helper
        self.descriptor = descriptor
        self.document_id = document_id
        self.namespace = namespace
        self.journal = journal
        self.allow_write = allow_write
        self.solid_count = 0

    def mutate(self, label, operation, **fields):
        self.helper.calls.append(('mutate', label, operation))
        if operation == 'new':
            self.helper.active = 2
            self.helper.documents.append({'id': 2, 'path': None, 'dirty': False})
            return {'document_id': 2}
        if operation == 'save_verified':
            return {'result': {'sha256': 'not-used', 'manifest': {'by_type': {'3D Solid': 1}},
                               'dropped_on_save': 0, 'verified': True}}
        return {'result': {}}

    def read(self, operation, **fields):
        self.helper.calls.append(('read', operation))
        if operation == 'audit':
            total = 0 if self.document_id == 2 and self.solid_count == 0 else 1
            return {'ok': True, 'summary': {'errors': 0, 'warnings': 0},
                    'manifest': {'total': total, 'by_type': {'3D Solid': total}}}
        if operation == 'state':
            return {'document_id': self.document_id, 'revision': 1,
                    'geometry_revision': 1}
        raise AssertionError(operation)

    def recover(self, request_id):
        self.helper.calls.append(('recover', request_id))
        return {'status': 'completed'}


class EnvelopeJobRunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.project = self.base / 'component_project'
        self.modeling = self.base / 'modeling'
        self.job_dir = self.project / 'job'
        self.source_dir = self.project / 'source'
        self.output_dir = self.project / 'cad' / 'parts'
        self.job_dir.mkdir(parents=True)
        self.source_dir.mkdir()
        self.output_dir.mkdir(parents=True)
        self.source = self.source_dir / 'manufacturer-source.txt'
        self.source.write_text('synthetic source fixture', encoding='utf-8')
        self.source_hash = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.output = self.output_dir / 'synthetic-envelope.dwg'
        self.job_path = self.job_dir / 'job.json'
        self.job_path.write_text(json.dumps(self.job()), encoding='utf-8')
        self.cadtools = self.base / 'cadtools-root'
        (self.cadtools / 'cadtools').mkdir(parents=True)
        (self.cadtools / 'cadtools/runtime.py').write_text('', encoding='utf-8')
        (self.cadtools / 'cadtools/verification.py').write_text('', encoding='utf-8')
        self.control = self.base / 'control.py'
        self.control.write_text('# synthetic helper fixture', encoding='utf-8')
        (self.modeling / 'scripts').mkdir(parents=True)
        (self.modeling / 'scripts/envelope_reference.py').write_text(
            '# synthetic reusable helper pin', encoding='utf-8')

    def job(self):
        return {
            'job_id': 'synthetic-envelope-job', 'namespace': 'synthetic-envelope-test',
            'part_id': 'SYNTHETIC-01', 'part_name': 'Synthetic enclosure',
            'representation': 'Synthetic nominal envelope reference',
            'geometry_role': 'reference_envelope', 'geometry_name': 'Synthetic envelope',
            'units': 'mm', 'frame': 'synthetic frame', 'local_frame': 'Origin at lower corner; XYZ positive',
            'origin': [0, 0, 0], 'readback_tolerance': 1e-7,
            'envelope_scope': 'Synthetic test dimensions only',
            'dimension_features': {'x': 'length', 'y': 'width', 'z': 'height'},
            'features': [
                {'name': name, 'required': True, 'value': value, 'unit': 'mm',
                 'source': str(self.source), 'source_sha256': self.source_hash,
                 'source_location': 'synthetic fixture row ' + name,
                 'evidence_status': 'synthetic_test_fixture'}
                for name, value in [('length', 10), ('width', 20), ('height', 30)]
            ],
        }

    def args(self, **changes):
        values = dict(
            job=self.job_path, job_dir=self.job_dir,
            output='${PROJECT_ROOT}/cad/parts/synthetic-envelope.dwg',
            session='test-session', control=self.control, cadtools_root=self.cadtools,
            root=[f'PROJECT_ROOT={self.project}', f'TOOLS_ROOT={self.modeling}'],
            modeling_root_name='TOOLS_ROOT',
            execution_model='synthetic-test-agent',
            allow_write=False,
        )
        values.update(changes)
        return SimpleNamespace(**values)

    def fake_imports(self, helper, geometry_state=None):
        ezdxf = types.ModuleType('ezdxf')
        ezdxf.__version__ = 'synthetic'
        acis = types.ModuleType('ezdxf.acis')
        sab = types.ModuleType('ezdxf.acis.sab')
        sab.parse_sab = lambda data: None
        sab.SabDataLoader = object
        runtime = types.ModuleType('cadtools.runtime')
        runtime.Client = FakeClient
        runtime.Journal = lambda path: object()
        runtime.load_helper = lambda path: helper
        runtime.Uncertain = type('Uncertain', (RuntimeError,), {})
        verification = types.ModuleType('cadtools.verification')

        def save_reopen(client, path, counts):
            Path(path).write_bytes(b'synthetic native output')
            client.helper.active = client.document_id
            client.helper.documents[-1]['path'] = str(path)
            client.solid_count = 1
            digest = hashlib.sha256(Path(path).read_bytes()).hexdigest()
            manifest = {'total': 1, 'by_type': {'3D Solid': 1}}
            audit = {'ok': True, 'summary': {'errors': 0, 'warnings': 0},
                     'manifest': manifest, 'target': {'dropped_on_save': 0}}
            save = {'ok': True, 'status': 'completed', 'verified': True,
                    'target_format': 'dwg', 'dropped_on_save': 0,
                    'sha256': digest, 'bytes': Path(path).stat().st_size,
                    'manifest': manifest, 'audit': audit}
            return {'stage': 'reopened', 'result': 'PASS', 'sha256': digest,
                    'save': save, 'reopened_audit': audit}

        verification.save_reopen = save_reopen
        cadtools = types.ModuleType('cadtools')
        envelope = types.ModuleType('envelope_reference')

        def build_envelope(client, job):
            client.solid_count = 1
            return 'H1'

        def inspect(client, handles, job):
            record = {'handle': 'H1', 'properties': {}}
            check = {'result': 'PASS', 'document_id': client.document_id,
                     'document_revision': 1, 'geometry_revision': 1}
            return {'records': [record]}, check

        class Geometry:
            def metadata(self, *args):
                return None

        envelope.build_envelope = build_envelope
        envelope.inspect = inspect
        envelope.parameters = lambda job: {'dimensions': {'x': 10, 'y': 20, 'z': 30},
                                           'origin': [0, 0, 0], 'tolerance': 1e-7}
        envelope.geometry = lambda client: Geometry()
        metadata = types.ModuleType('source_metadata')
        metadata.compare_source_metadata = lambda *args: {'result': 'PASS'}
        modules = {
            'ezdxf': ezdxf, 'ezdxf.acis': acis, 'ezdxf.acis.sab': sab,
            'cadtools': cadtools, 'cadtools.runtime': runtime,
            'cadtools.verification': verification,
            'envelope_reference': envelope, 'source_metadata': metadata,
        }
        return modules

    def test_named_root_roundtrip_and_portable_metadata_include_source_hash(self):
        roots = runner.parse_roots(self.args().root)
        self.assertEqual(runner.resolve_locator('${PROJECT_ROOT}/source/manufacturer-source.txt', roots),
                         self.source)
        self.assertEqual(runner.source_locator(self.source, roots),
                         '${PROJECT_ROOT}/source/manufacturer-source.txt')
        job, _, _ = runner.resolve_runtime_job(self.job_path, roots)
        lines = runner.expected_metadata(job)
        self.assertTrue(any(self.source_hash in line for line in lines))
        self.assertFalse(any(str(self.base) in line for line in lines))
        self.assertIn('Part ID: SYNTHETIC-01', lines)
        self.assertIn('Envelope scope: Synthetic test dimensions only', lines)
        job['features'].append({
            'name': 'variant_note', 'required': False, 'value': '10 millimetres',
            'unit': 'description', 'source': str(self.source),
            'source_sha256': self.source_hash, 'source_location': 'synthetic variant note',
            'evidence_status': 'synthetic_test_fixture',
        })
        alternate = self._write_job(job)
        runtime, _, _ = runner.resolve_runtime_job(alternate, roots)
        self.assertTrue(any('"10 millimetres"' in line
                            for line in runner.expected_metadata(runtime)))
        self.assertEqual(runner.resolve_locator('../source/manufacturer-source.txt', roots,
                                                self.job_dir), self.source)

    def test_rejects_missing_or_oversized_namespace_and_conflicting_output(self):
        job = self.job()
        del job['namespace']
        with self.assertRaisesRegex(ValueError, 'namespace'):
            runner.resolve_runtime_job(self._write_job(job), runner.parse_roots(self.args().root))
        job['namespace'] = 'x' * 65
        with self.assertRaisesRegex(ValueError, '64 UTF-8 bytes'):
            runner.resolve_runtime_job(self._write_job(job), runner.parse_roots(self.args().root))
        job['namespace'] = 'synthetic-envelope-test'
        job['output_path'] = '${PROJECT_ROOT}/cad/parts/synthetic-envelope.dwg'
        self.job_path.write_text(json.dumps(job), encoding='utf-8')
        args = self.args(output='${PROJECT_ROOT}/cad/parts/different.dwg')
        helper = FakeHelper()
        with patch.dict(sys.modules, self.fake_imports(helper)):
            with self.assertRaisesRegex(ValueError, 'conflicts'):
                runner.run(args)
        self.assertFalse(any(call[0] == 'mutate' for call in helper.calls))
        self.assertFalse(any(call[0] == 'descriptors' for call in helper.calls))

    def test_invalid_metadata_and_root_fail_before_ocs_discovery(self):
        helper = FakeHelper()
        job = self.job()
        job['envelope_scope'] = 17
        self.job_path.write_text(json.dumps(job), encoding='utf-8')
        with patch.dict(sys.modules, self.fake_imports(helper)):
            with self.assertRaisesRegex(ValueError, 'envelope_scope'):
                runner.run(self.args())
        self.assertFalse(any(call[0] == 'descriptors' for call in helper.calls))
        job['envelope_scope'] = 'Synthetic test dimensions only'
        self.job_path.write_text(json.dumps(job), encoding='utf-8')
        with patch.dict(sys.modules, self.fake_imports(helper)):
            with self.assertRaisesRegex(ValueError, 'caller-supplied root'):
                runner.run(self.args(modeling_root_name='MISSING_ROOT'))
        self.assertFalse(any(call[0] == 'descriptors' for call in helper.calls))

    def test_existing_output_or_prior_native_receipt_blocks_replay(self):
        self.output.write_bytes(b'old')
        with self.assertRaises(FileExistsError):
            runner.check_write_targets(self.output, self.job_dir, True)
        self.output.unlink()
        (self.job_dir / 'native-handles.json').write_text('{}', encoding='utf-8')
        with self.assertRaisesRegex(FileExistsError, 'replay'):
            runner.check_write_targets(self.output, self.job_dir, True)
        (self.job_dir / 'native-handles.json').unlink()
        (self.job_dir / 'native-preflight.json').write_text(
            json.dumps({'result': 'FAIL'}), encoding='utf-8')
        with self.assertRaisesRegex(FileExistsError, 'preflight'):
            runner.check_write_targets(self.output, self.job_dir, True)

    def test_default_preflight_reads_state_and_never_mutates_ocs(self):
        helper = FakeHelper()
        with patch.dict(sys.modules, self.fake_imports(helper)):
            result = runner.run(self.args())
        self.assertEqual(result['mode'], 'READ_ONLY_PREFLIGHT')
        self.assertTrue((self.job_dir / 'native-preflight.json').is_file())
        self.assertFalse((self.job_dir / 'ocs-journal.jsonl').exists())
        self.assertFalse(self.output.exists())
        self.assertFalse(any(call[0] == 'mutate' for call in helper.calls))

    def test_saved_reader_import_failure_happens_before_ocs_discovery(self):
        helper = FakeHelper()
        modules = self.fake_imports(helper)
        modules['ezdxf.acis.sab'] = None
        with patch.dict(sys.modules, modules):
            with self.assertRaisesRegex(RuntimeError, 'before OCS writes'):
                runner.run(self.args())
        self.assertFalse(any(call[0] == 'descriptors' for call in helper.calls))
        self.assertFalse((self.job_dir / 'native-preflight.json').exists())

    def test_fake_guarded_orchestration_creates_and_persists_only_when_enabled(self):
        helper = FakeHelper()
        with patch.dict(sys.modules, self.fake_imports(helper)):
            result = runner.run(self.args(allow_write=True))
        self.assertEqual(result['state'], 'REFERENCE_DONE')
        self.assertEqual(result['native_model_sha256'], hashlib.sha256(self.output.read_bytes()).hexdigest())
        self.assertTrue((self.job_dir / 'pre-save-feature-checks.json').is_file())
        self.assertTrue((self.job_dir / 'reopened-source-metadata-check.json').is_file())
        self.assertTrue(any(call[:2] == ('mutate', 'create-isolated-document') for call in helper.calls))
        self.assertTrue((self.job_dir / 'action-occurrences.jsonl').is_file())

    def test_uncertain_mutation_recovers_original_request_without_resubmission(self):
        uncertain = type('Uncertain', (RuntimeError,), {})
        runtime = types.ModuleType('cadtools.runtime')
        runtime.Uncertain = uncertain

        class Client:
            namespace = 'synthetic-request-set'
            calls = []

            def mutate(self, label, operation, allow_wait=False, **fields):
                self.calls.append(('mutate', label, operation))
                raise uncertain('completion not observed')

            def recover(self, request_id, allow_wait=False):
                self.calls.append(('recover', request_id))
                return {'status': 'completed', 'request_id': request_id}

        client = Client()
        with patch.dict(sys.modules, {'cadtools.runtime': runtime}):
            response = runner.RecoveringClient(client).mutate('make-solid', 'entities_create')
        self.assertEqual(response['request_id'], 'synthetic-request-set:make-solid')
        self.assertEqual(client.calls, [
            ('mutate', 'make-solid', 'entities_create'),
            ('recover', 'synthetic-request-set:make-solid'),
        ])

    def test_nested_dropped_on_save_count_fails_persistence_receipt(self):
        self.output.write_bytes(b'synthetic output')
        digest = hashlib.sha256(self.output.read_bytes()).hexdigest()
        manifest = {'total': 1, 'by_type': {'3D Solid': 1}}
        audit = {'ok': True, 'summary': {'errors': 0, 'warnings': 0},
                 'manifest': manifest, 'target': {'dropped_on_save': 1}}
        receipt = {'stage': 'reopened', 'result': 'PASS', 'sha256': digest,
                   'save': {'verified': True, 'dropped_on_save': 0,
                            'sha256': digest, 'manifest': manifest, 'audit': audit},
                   'reopened_audit': audit}
        with self.assertRaisesRegex(ValueError, 'dropped entities'):
            runner.validate_save_receipt(receipt, self.output, {'3D Solid': 1})

    def _write_job(self, value):
        path = self.job_dir / 'alternate-job.json'
        path.write_text(json.dumps(value), encoding='utf-8')
        return path


if __name__ == '__main__':
    unittest.main()
