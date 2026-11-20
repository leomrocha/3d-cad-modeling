import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from component_records import readiness
from job_paths import rooted_path, selected_roots
from retained_artifacts import verify_manifest


class JobPathTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.config = self.root / 'operations.json'
        patch_location = patch('job_paths.location', return_value=self.config)
        patch_location.start()
        self.addCleanup(patch_location.stop)

    def save_parts(self, *names):
        resources = []
        for name in names:
            directory = self.root / name
            directory.mkdir()
            (directory / 'source.md').write_text(name)
            resources.append({'id': name, 'location': str(directory),
                              'methods': [{'probe': 'parts'}]})
        self.config.write_text(json.dumps({'version': 2, 'resources': resources}))

    def test_saved_parts_locator_is_resolved_without_a_folder_map(self):
        self.save_parts('shop')
        self.assertEqual(rooted_path('${PARTS_ROOT}/source.md', selected_roots()),
                         self.root / 'shop/source.md')
        self.assertEqual(rooted_path('${SKILL_ROOT}/scripts/job_paths.py', selected_roots()),
                         Path(__file__).resolve().parents[1] / 'scripts/job_paths.py')

    def test_parts_reference_rejects_ambiguity_and_resolves_exact_id(self):
        self.save_parts('shop one', 'shop-one')
        roots = selected_roots()
        with self.assertRaisesRegex(ValueError, 'select a specific configured parts catalogue'):
            rooted_path('${PARTS_ROOT}/source.md', roots)
        self.assertEqual(rooted_path('${PARTS_73686f70206f6e65}/source.md', roots),
                         self.root / 'shop one/source.md')

    def test_invalid_optional_catalogue_only_affects_parts_reference(self):
        self.config.write_text('{broken')
        roots = selected_roots(job=self.root / 'job.json')
        self.assertEqual(rooted_path('${JOB_ROOT}/source.md', roots),
                         self.root / 'source.md')
        with self.assertRaisesRegex(ValueError, 'Cannot read saved parts catalogue'):
            rooted_path('${PARTS_ROOT}/source.md', roots)

    def test_component_readiness_uses_the_job_record_directory(self):
        source = self.root / 'part.md'
        source.write_text('component input')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        feature = dict(name='height', required=True, value=4, unit='mm',
                       source='part.md', source_sha256=digest,
                       evidence_status='reported', source_location='first line')
        job = dict(job_id='fixture', part_id='fixture', part_name='Fixture',
                   representation='reference', units='mm', frame='world',
                   features=[feature])
        result = readiness(job, job_path=self.root / 'job.json')
        self.assertEqual(result['source_observations'][0]['path'], str(source))

    def test_retained_manifest_derives_its_evidence_origin_and_rejects_unknown(self):
        output = self.root / 'result.json'
        output.write_text('{}')
        manifest = self.root / 'manifest.json'
        digest = hashlib.sha256(output.read_bytes()).hexdigest()

        def verify(locator):
            manifest.write_text(json.dumps({'files': [{'path': locator, 'sha256': digest}]}))
            return verify_manifest(manifest)

        self.assertEqual(verify('${EVIDENCE_ROOT}/result.json')['result'], 'PASS')
        with self.assertRaisesRegex(ValueError, 'Missing configured path root: OTHER'):
            verify('${OTHER}/result.json')
        with self.assertRaisesRegex(ValueError, 'escapes'):
            verify('${EVIDENCE_ROOT}/../result.json')
