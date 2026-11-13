"""Focused source-register merges preserve history and validate both indexes."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('source_registry', ROOT / 'research/tools/build_workflow_register.py')
registry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registry)


class SourceRegistration(unittest.TestCase):
    def test_merge_preserves_existing_ids_original_observations_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sources = root / 'research/sources'
            sources.mkdir(parents=True)
            original = {'id': 'SRC-existing', 'url': None,
                        'local_source_path': '${MODELING_ROOT}/scripts/helper.py',
                        'title': 'Existing helper', 'summary': 'Original summary',
                        'registered_at': '2026-11-12', 'evidence_statuses': ['existing_record'],
                        'observations': [{'sha256': 'original-hash'}], 'referring_documents': ['old.md']}
            (sources / 'source-register.json').write_text(json.dumps({'sources': [original]}))
            (sources / 'source-register.md').write_text('# Sources\n\n<a id="src-existing"></a>\n\n## Original\n\n## Unrelated retained section\n\nOriginal retained text.\n')
            new = {'local_original': 'scripts/helper.py', 'title': 'Observed helper', 'summary': 'New observation',
                   'observation_date': '2026-11-13', 'evidence_status': 'local_file_inspected',
                   'original_sha256': 'retained-original', 'referring_documents': ['new.md']}
            document = 'research/sources/fixture.json'
            (root / document).write_text(json.dumps({'records': [new]}))
            with self.assertRaisesRegex(ValueError, 'stale'):
                registry.merge_source_records(root, [document], '2026-11-13', check=True)
            registry.merge_source_records(root, [document], '2026-11-13')
            merged = json.loads((sources / 'source-register.json').read_text())['sources']
            self.assertEqual(json.loads((sources / 'source-register.json').read_text())['source_record_documents'], [document])
            self.assertEqual(len(merged), 1)
            self.assertEqual(merged[0]['id'], original['id'])
            self.assertEqual(merged[0]['observations'][0]['sha256'], 'original-hash')
            self.assertEqual(merged[0]['observations'][1]['original_sha256'], 'retained-original')
            self.assertIn('new.md', merged[0]['referring_documents'])
            self.assertIn('../../scripts/helper.py', (sources / 'source-register.md').read_text())
            self.assertIn('## Unrelated retained section\n\nOriginal retained text.', (sources / 'source-register.md').read_text())
            self.assertEqual(registry.merge_source_records(root, [document], '2026-11-13', check=True)['result'], 'PASS')
            registry.merge_source_records(root, [document], '2026-11-13')
            self.assertEqual(len(json.loads((sources / 'source-register.json').read_text())['sources'][0]['observations']), 2)


if __name__ == '__main__':
    unittest.main()
