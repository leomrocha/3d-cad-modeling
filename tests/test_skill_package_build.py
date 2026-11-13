"""Package registration lifecycle and mandatory completion-gate regression checks."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('skill_package_builder', ROOT / 'scripts/build_skill_packages.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class CurrentPackages(unittest.TestCase):
    def test_current_distribution_is_synchronised(self):
        # Runs in ordinary final unittest discovery, without optional CLI inputs.
        self.assertEqual(builder.build(check=True)['result'], 'PASS')

    def test_catalogues_and_source_register_cover_current_tools(self):
        self.assertEqual(builder.check_registrations()['result'], 'PASS')


class PackageLifecycle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='package-lifecycle-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch = patch.object(builder, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        for relative, content in {
            'LICENSE': 'Fixture license\n',
            'requirements-native.txt': 'ezdxf==1.4.5\n',
            'scripts/cadtools/NOTICE.md': 'Fixture attribution\n',
            'scripts/cadtools/__init__.py': '',
            'scripts/component_records.py': 'VALUE = 1\n',
            'scripts/part_index.py': 'VALUE = 1\n',
            'scripts/package_check.py': 'VALUE = 1\n',
            'scripts/source_intake.py': 'VALUE = 1\n',
            'scripts/dxf_inspect.py': 'VALUE = 1\n',
        }.items():
            self.write(relative, content)
        self.cli = self.root / 'cli'
        self.reader = self.root / 'reader'
        self.write('cli/bin/cli.mjs', '// fixture\n')
        (self.reader / 'ezdxf').mkdir(parents=True)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def register_fixture(self):
        paths = [p for p in builder.source_paths() if Path(p).name != '__init__.py']
        self.write('docs/tools.md', '\n'.join('[tool](../' + p + ')' for p in paths))
        self.write('skills/README.md', '# Fixture catalogue\n')
        self.write('skills/cad-ocs-engineering/SKILL.md', '# Fixture skill\n')
        records = [{'id': 'fixture-' + Path(p).stem, 'local_source_path': p} for p in paths]
        self.write('research/sources/source-register.json', json.dumps({'sources': records}))
        self.write('research/sources/source-register.md', '\n'.join(
            '<a id="' + r['id'] + '"></a>\n\n## ' + r['id'] + ' — Fixture source' for r in records))

    def test_creation_modification_deletion_and_transitive_registration(self):
        builder.build()
        self.write('scripts/new_helper.py', 'from cadtools import extra\nVALUE = extra.VALUE\n')
        self.write('scripts/cadtools/extra.py', 'VALUE = 2\n')
        self.write('scripts/source_intake.py', 'import new_helper\n')
        with self.assertRaisesRegex(ValueError, 'differs from canonical'):
            builder.build(check=True)
        builder.build()
        for name in ('cad-ocs-engineering', 'cad-source-intake'):
            package = self.root / 'skills' / name
            manifest = json.loads((package / 'package-manifest.json').read_text())
            for relative in ('scripts/new_helper.py', 'scripts/cadtools/extra.py', 'scripts/cadtools/__init__.py'):
                self.assertIn(relative, manifest['files'])
                self.assertTrue((package / relative).is_file())
        self.assertFalse((self.root / 'skills/cad-drawing-inspection/scripts/new_helper.py').exists())
        self.write('scripts/cadtools/extra.py', 'VALUE = 3\n')
        with self.assertRaisesRegex(ValueError, 'differs from canonical'):
            builder.build(check=True)
        builder.build()
        self.assertEqual((self.root / 'skills/cad-source-intake/scripts/cadtools/extra.py').read_text(), 'VALUE = 3\n')
        self.write('scripts/source_intake.py', 'VALUE = 1\n')
        (self.root / 'scripts/new_helper.py').unlink()
        (self.root / 'scripts/cadtools/extra.py').unlink()
        with self.assertRaisesRegex(ValueError, 'stale'):
            builder.build(check=True)
        builder.build()
        for name in builder.SKILLS:
            self.assertFalse((self.root / 'skills' / name / 'scripts/new_helper.py').exists())
            self.assertFalse((self.root / 'skills' / name / 'scripts/cadtools/extra.py').exists())
        self.assertEqual(builder.build(check=True)['result'], 'PASS')

    def test_unassigned_build_tool_import_fails_before_generation(self):
        self.write('scripts/build_skill_packages.py', 'VALUE = 1\n')
        self.write('scripts/source_intake.py', 'import build_skill_packages\n')
        with self.assertRaisesRegex(ValueError, 'Unassigned'):
            builder.build()
        self.assertFalse((self.root / 'skills').exists())

    def test_namespace_relative_imports_include_local_dependencies(self):
        self.write('scripts/source_intake.py', 'from . import local_helper\n')
        self.write('scripts/local_helper.py', 'VALUE = 1\n')
        builder.build()
        self.assertTrue((self.root / 'skills/cad-source-intake/scripts/local_helper.py').is_file())

    def test_invalid_new_helper_fails_before_generation(self):
        self.write('scripts/new_helper.py', 'def broken(\n')
        with self.assertRaisesRegex(ValueError, 'Invalid reusable script'):
            builder.build()
        self.assertFalse((self.root / 'skills').exists())

    def test_unregistered_installed_script_is_preserved_and_reported(self):
        builder.build()
        orphan = self.write('skills/cad-source-intake/scripts/orphan.py', 'VALUE = 1\n')
        with self.assertRaisesRegex(ValueError, 'Unassigned packaged script'):
            builder.build()
        self.assertEqual(orphan.read_text(), 'VALUE = 1\n')

    def test_completion_requires_inputs_before_generation(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, 'Completion requires'):
                builder.complete(regenerate=True)
        self.assertFalse((self.root / 'skills').exists())

    def test_verify_detects_skipped_synchronisation_before_tests(self):
        builder.build()
        self.write('scripts/new_helper.py', 'VALUE = 1\n')
        with patch.object(builder.subprocess, 'run') as run:
            with self.assertRaisesRegex(ValueError, 'differs from canonical'):
                builder.complete(cli_root=self.cli, reader_root=self.reader)
            run.assert_not_called()

    def test_finalize_propagates_installation_check_failure(self):
        self.register_fixture()
        failed = subprocess.CompletedProcess([], 1, '', 'installation fixture failed')
        with patch.object(builder.subprocess, 'run', return_value=failed):
            with self.assertRaisesRegex(ValueError, 'completion checks failed'):
                builder.complete(regenerate=True, cli_root=self.cli, reader_root=self.reader)
        self.assertEqual(builder.build(check=True)['result'], 'PASS')

    def test_source_change_during_checks_prevents_completion(self):
        self.register_fixture()
        def mutate(command, **kwargs):
            self.write('scripts/new_helper.py', 'VALUE = 1\n')
            return subprocess.CompletedProcess(command, 0, '', '')
        with patch.object(builder.subprocess, 'run', side_effect=mutate):
            with self.assertRaisesRegex(ValueError, 'differs from canonical'):
                builder.complete(regenerate=True, cli_root=self.cli, reader_root=self.reader)

    def test_missing_catalogue_and_source_entries_are_reported(self):
        self.register_fixture()
        self.write('scripts/new_helper.py', 'VALUE = 1\n')
        with self.assertRaisesRegex(ValueError, 'Tool catalogue entry missing'):
            builder.check_registrations()
        self.write('docs/tools.md', (self.root / 'docs/tools.md').read_text() + '\n[new](../scripts/new_helper.py)\n')
        with self.assertRaisesRegex(ValueError, 'Combined source registration missing'):
            builder.check_registrations()

    def test_missing_procedure_index_entry_is_reported(self):
        self.register_fixture()
        self.write('skills/cad-ocs-engineering/references/new.md', '# Fixture procedure\n')
        self.write('skills/cad-ocs-engineering/SKILL.md', '[procedure](references/new.md)\n')
        with self.assertRaisesRegex(ValueError, 'Skill procedure index entry missing'):
            builder.check_registrations()

    def test_previous_manifest_cannot_delete_outside_package(self):
        builder.build()
        manifest = self.root / 'skills/cad-ocs-engineering/package-manifest.json'
        data = json.loads(manifest.read_text())
        data['files']['../../outside.py'] = {'source': 'fixture', 'sha256': 'fixture'}
        manifest.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Manifest path outside'):
            builder.build()


if __name__ == '__main__':
    unittest.main()
