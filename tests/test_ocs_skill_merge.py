"""Dated merge-delivery checks. Opt in with VERIFY_OCS_MERGE_SNAPSHOT=1.

The merge inventory preserves a dated comparison; normal modeling iterations
can improve the skill without rewriting that historical inventory.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.environ.get('VERIFY_OCS_MERGE_SNAPSHOT') == '1', 'Dated merge snapshot check; set VERIFY_OCS_MERGE_SNAPSHOT=1')
class CompleteOcsMerge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads((ROOT / 'research/sources/cad-ocs-engineering-merge-2026-11-13.json').read_text())
        cls.skill = ROOT / 'skills/cad-ocs-engineering'

    def test_every_original_and_component_file_has_retained_destination(self):
        for row in self.record['inventory']:
            with self.subTest(origin=row['origin'], source=row['relative_path']):
                path = ROOT / row['destination']
                self.assertTrue(path.is_relative_to(self.skill))
                self.assertTrue(path.is_file())
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row['destination_sha256'])

    def test_both_workflows_are_merged_directly_in_main_instructions(self):
        main = (self.skill / 'SKILL.md').read_text()
        for row in self.record['workflow_section_coverage']:
            with self.subTest(origin=row['origin'], section=row['source_section']):
                match = re.search(r'^#{2,3} ' + re.escape(row['destination_heading']) + r'\n(.*?)(?=^#{2,3} |\Z)', main, re.M | re.S)
                self.assertIsNotNone(match)
                self.assertEqual(hashlib.sha256(match[1].strip().encode()).hexdigest(), row['body_sha256'])
        self.assertNotIn('component-workflow.md', main)

    def test_concurrent_committed_helper_additions_are_included(self):
        for row in self.record['concurrent_committed_additions']:
            self.assertEqual(hashlib.sha256((ROOT / row['destination']).read_bytes()).hexdigest(), row['sha256'])

    def test_merged_agent_identity_and_portable_source_paths(self):
        agent = (self.skill / 'agents/openai.yaml').read_text()
        self.assertIn('$cad-ocs-engineering', agent)
        for path in self.skill.rglob('*.md'):
            self.assertNotIn('/home/leo/projects/', path.read_text(), str(path.relative_to(self.skill)))
        self.assertFalse((ROOT / 'skills/component-cad').exists())


if __name__ == '__main__':
    unittest.main()
