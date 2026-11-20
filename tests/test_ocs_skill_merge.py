"""Check the CAD skill identity and documentation paths."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OcsSkillPackage(unittest.TestCase):
    skill = ROOT / "skills/cad-ocs-engineering"

    def test_merged_agent_identity_and_portable_source_paths(self):
        self.assertNotIn('component-workflow.md', (self.skill / 'SKILL.md').read_text())
        agent = (self.skill / 'agents/openai.yaml').read_text()
        self.assertIn('$cad-ocs-engineering', agent)
        for path in self.skill.rglob('*.md'):
            self.assertNotIn('/home/leo/projects/', path.read_text(), str(path.relative_to(self.skill)))
        self.assertFalse((ROOT / 'skills/component-cad').exists())


if __name__ == '__main__':
    unittest.main()
