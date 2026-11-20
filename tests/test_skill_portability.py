"""Distribution boundaries and reusable helper operation in an isolated installation."""
import ast
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote,urlsplit

ROOT=Path(__file__).resolve().parents[1]
PROJECT_LOCATOR = re.compile(r'(?i)fer' r'me|/home/|/tmp/|\$\{(?:ENERGY|OCS|MODELING|CODEX)[A-Z_]*\}')


def without_credit_urls(text):
    """Exclude labeled author-credit links from runtime dependency checks."""
    credit_link = re.compile(r'(?<!!)\[([^]\n]+)\]\(https?://[^\s)]+\)')
    return '\n'.join(
        credit_link.sub(r'\1', line) if line.startswith('Attribution — ') else line
        for line in text.splitlines()
    )


class PortableDistribution(unittest.TestCase):
    def test_every_reference_is_inside_its_skill(self):
        for name in ('cad-ocs-engineering','cad-drawing-inspection','cad-source-intake'):
            package=ROOT/'skills'/name
            for doc in package.rglob('*.md'):
                if '__pycache__' in doc.parts:continue
                text=doc.read_text()
                self.assertNotRegex(text, PROJECT_LOCATOR)
                self.assertNotRegex(text,r'caller-owned_ROOT|component-led-|engineering/module-development|\$\{SKILL_ROOT\}/tests|gpt-[A-Za-z0-9.]')
                text = without_credit_urls(text)
                self.assertNotRegex(text, r'(?i)https?://')
                for target in re.findall(r'\]\(([^)]+)\)',text):
                    parsed=urlsplit(target)
                    self.assertFalse(parsed.scheme,(doc,target))
                    path=(doc.parent/unquote(parsed.path)).resolve()
                    self.assertTrue(path.is_relative_to(package.resolve()),(doc,target))
                    self.assertTrue(path.exists(),(doc,target))
    def test_credit_exception_is_limited_to_author_links(self):
        url = 'https://example.org/source'
        link = f'[original author]({url})'
        self.assertNotIn(url, without_credit_urls('Attribution — ' + link))
        for text in ('Download ' + link, 'Attribution — !' + link, 'Attribution — ' + url):
            self.assertIn(url, without_credit_urls(text))

    def test_packaged_scripts_have_no_specific_project_locator(self):
        for p in (ROOT/'skills').rglob('*.py'):
            text=p.read_text()
            self.assertNotRegex(text, PROJECT_LOCATOR)
            ast.parse(text)

    def test_manifest_sources_and_procedure_hashes_are_bundled(self):
        import hashlib
        for name in ('cad-ocs-engineering','cad-drawing-inspection','cad-source-intake'):
            package=ROOT/'skills'/name;manifest=json.loads((package/'package-manifest.json').read_text())
            self.assertIn('SKILL.md',manifest['files'])
            for target,row in manifest['files'].items():
                self.assertEqual(row['source'],target)
                self.assertTrue((package/row['source']).is_file())
                self.assertEqual(hashlib.sha256((package/target).read_bytes()).hexdigest(),row['sha256'])


if __name__=='__main__':unittest.main()
