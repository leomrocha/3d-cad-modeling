"""Exercise the repository audit with staged, committed, and untracked inputs."""
from datetime import date
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / 'maintenance/check_repository.py'
BUILDER = 'scripts/build_skill_packages.py'


class RepositoryAuditTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        self.git('init', '--quiet')
        self.git('config', 'user.name', 'Repository audit test')
        self.git('config', 'user.email', 'audit@example.invalid')

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.repo, text=True)

    def write(self, relative, value):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8')
        return path

    def audit(self, *args):
        return subprocess.run([sys.executable, str(CHECKER), *args], cwd=self.repo,
                              capture_output=True, text=True)

    def test_asset_parent_is_checked_and_asset_body_is_skipped(self):
        today = date.today()
        for value in (today.isoformat(), today.strftime('%Y%m%d'),
                      today.strftime('%d-%B-%Y')):
            path = f'media/export_{value}/model.step'
            self.write(path, today.isoformat())
            self.git('add', '--', path)
        result = self.audit('--index')
        self.assertEqual(result.returncode, 1, result)
        self.assertEqual(result.stdout.count('ERROR dated-path'), 3)
        self.assertNotIn('ERROR calendar-date', result.stdout)

    def test_source_study_credit_requires_a_dated_licence_and_link(self):
        day = date.today().isoformat()
        self.write("reader.py", f"# Read {day}. Upstream licence: MIT. https://github.com/project/reader\n"
                   f"# Read {day}.\n")
        self.git("add", "--", "reader.py")
        result = self.audit("--index")
        self.assertIn("REVIEW source-attribution", result.stdout)
        self.assertEqual(result.stdout.count("ERROR calendar-date"), 1)

    def test_staged_private_reference_cannot_be_hidden_by_worktree(self):
        retired_project = 'fer' + 'me'
        path = self.write('guide.md', f'Send the model to {retired_project}.\n')
        self.git('add', '--', 'guide.md')
        path.write_text('Save the model in the job output directory.\n')
        result = self.audit('--index')
        self.assertEqual(result.returncode, 1, result)
        self.assertIn(f'guide.md:1: ERROR private-reference: {retired_project!r}', result.stdout)

    def test_named_commit_ignores_link_target_added_after_commit(self):
        self.write('guide.md', '[Drawing](inputs/plate.txt#view)\n')
        self.git('add', '--', 'guide.md')
        self.git('commit', '--quiet', '-m', 'Test snapshot')
        revision = self.git('rev-parse', 'HEAD').strip()
        self.write('inputs/plate.txt', 'Illustrative input.\n')
        result = self.audit('--index')
        self.assertEqual(result.returncode, 1, result)
        self.assertIn("guide.md:1: ERROR untracked-link: 'inputs/plate.txt#view'", result.stdout)
        self.git('add', '--', 'inputs/plate.txt')
        self.assertEqual(self.audit('--index').returncode, 0)
        self.assertEqual(self.audit('--commit', revision).returncode, 1)

    def test_classification_reports_identifiers_alongside_blocking_dates(self):
        today = date.today()
        number = today.isoformat()
        self.write('NOTICE.md', f'Copyright (c) {today.year} Sample Author\n'
                               f'Protocol binding: {{"protocolVersion":"{number}"}}\n'
                               f'Recorded on {number}.\n')
        self.git('add', '--', 'NOTICE.md')
        result = self.audit('--index')
        self.assertEqual(result.returncode, 1, result)
        self.assertIn('NOTICE.md:1: REVIEW copyright-year:', result.stdout)
        self.assertIn('NOTICE.md:2: REVIEW protocol-version:', result.stdout)
        self.assertIn('NOTICE.md:3: ERROR calendar-date:', result.stdout)

    def test_stale_package_is_detected_even_with_a_current_worktree_copy(self):
        # Seed the temporary repository from tracked package inputs and generate fresh copies.
        files = subprocess.check_output(
            ['git', 'ls-files', '-z', '--', 'scripts/', 'skills/', 'translator/',
             'format_translation/', 'LICENSE', 'requirements-native.txt',
             'docs/modeling-operation-selection.md'], cwd=ROOT).decode().split('\0')
        for name in filter(None, files):
            target = self.repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / name).read_bytes())
        subprocess.run([sys.executable, BUILDER], cwd=self.repo, check=True, capture_output=True)
        source = self.repo / 'scripts/assembly_units.py'
        installed = self.repo / 'skills/cad-ocs-engineering/scripts/assembly_units.py'
        self.git('add', '--all')
        with source.open('a') as stream:
            stream.write('\n# Changed canonical output.\n')
        self.git('add', '--', str(source.relative_to(self.repo)))
        installed.write_bytes(source.read_bytes())
        result = self.audit('--index')
        self.assertEqual(result.returncode, 1, result)
        self.assertIn(f'{installed.relative_to(self.repo)}:1: ERROR package-sync:', result.stdout)


if __name__ == '__main__':
    unittest.main()
