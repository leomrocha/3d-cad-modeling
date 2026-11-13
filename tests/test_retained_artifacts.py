import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from retained_artifacts import verify_manifest


class RetainedArtifactsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.package = self.root / 'packet'
        self.package.mkdir()
        self.artifact = self.package / 'check.json'
        self.artifact.write_text('{"result":"PASS"}\n')
        self.digest = hashlib.sha256(self.artifact.read_bytes()).hexdigest()
        self.manifest = self.package / 'manifest.json'

    def verify(self, files):
        self.manifest.write_text(json.dumps({'files': files}))
        return verify_manifest(self.manifest, {'PROJECT_ROOT': self.root})

    def test_verifies_portable_paths_and_current_derivative_hash(self):
        for locator in ['check.json', '${PROJECT_ROOT}/packet/check.json', 'PROJECT_ROOT/packet/check.json']:
            result = self.verify([{'retained_path': locator, 'sha256': '0'*64,
                                   'retained_sha256': self.digest}])
            self.assertEqual(result['verified_count'], 1)
            self.assertEqual(result['files'][0]['sha256'], self.digest)
            self.assertNotIn(str(self.root), json.dumps(result))

    def test_detects_changed_artifact(self):
        self.artifact.write_text('{"result":"FAIL"}\n')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.verify([{'path': 'check.json', 'sha256': self.digest}])

    def test_parses_saved_json_even_when_hash_matches(self):
        self.artifact.write_text('{}\\n')
        digest = hashlib.sha256(self.artifact.read_bytes()).hexdigest()
        with self.assertRaises(json.JSONDecodeError):
            self.verify([{'path': 'check.json', 'sha256': digest}])

    def test_work_only_rows_are_explicit_and_cannot_produce_empty_pass(self):
        omitted = {'retained_path': None, 'classification': 'work-only original', 'sha256': '0'*64}
        result = self.verify([omitted, {'path': 'check.json', 'sha256': self.digest}])
        self.assertEqual(len(result['omitted_entries']), 1)
        with self.assertRaisesRegex(ValueError, 'no retained artifacts'):
            self.verify([omitted])
        with self.assertRaisesRegex(ValueError, 'classification'):
            self.verify([{'retained_path': None}])

    def test_repeated_attribution_keeps_one_artifact_and_rejects_conflicting_hash(self):
        result = self.verify([{'path': 'check.json', 'sha256': self.digest}]*2)
        self.assertEqual(result['verified_count'], 1)
        self.assertEqual(len(result['duplicate_attributions']), 1)
        with self.assertRaisesRegex(ValueError, 'Conflicting'):
            self.verify([{'path': 'check.json', 'sha256': self.digest},
                         {'path': 'check.json', 'sha256': '0'*64}])

    def test_rejects_package_escape_and_missing_digest(self):
        for files, message in [
            ([{'path': '../outside.json', 'sha256': self.digest}], 'escapes'),
            ([{'path': 'check.json'}], 'SHA-256'),
        ]:
            with self.assertRaisesRegex(ValueError, message):
                self.verify(files)

    def test_explicit_root_can_reference_shared_case_code_outside_packet(self):
        shared = self.root / 'shared.py'
        shared.write_text('# retained case code\n')
        digest = hashlib.sha256(shared.read_bytes()).hexdigest()
        result = self.verify([{'path': '${PROJECT_ROOT}/shared.py', 'sha256': digest}])
        self.assertEqual(result['verified_count'], 1)
        with self.assertRaisesRegex(ValueError, 'escapes'):
            self.verify([{'path': '${PROJECT_ROOT}/../outside.py', 'sha256': digest}])


if __name__ == '__main__':
    unittest.main()
