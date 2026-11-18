"""Exercise the fourth skill alone with an isolated interpreter and local CLI."""
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
import venv


from test_skill_packages import NAMES as LEGACY_INSTALL_CASES

ROOT = Path(__file__).resolve().parents[1]
NAME = 'cad-mcp-translator'


@unittest.skipUnless(os.environ.get('SKILLS_CLI_ROOT'), 'Requires cached local skills CLI')
class TranslatorInstallation(unittest.TestCase):
    def test_install_from_local_source_without_siblings_or_cad_dependencies(self):
        spec = importlib.util.spec_from_file_location('cad_distribution_builder',
                                                       ROOT / 'scripts/build_skill_packages.py')
        builder_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder_module)
        self.assertEqual(set(LEGACY_INSTALL_CASES) | {NAME, builder_module.FORMAT}, set(builder_module.SKILLS))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            work = root / 'job'
            work.mkdir()
            shutil.copytree(ROOT / 'skills' / NAME, source / 'skills' / NAME,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            env = dict(os.environ, HOME=str(root / 'home'), USERPROFILE=str(root / 'home'),
                       XDG_CONFIG_HOME=str(root / 'settings'), DISABLE_TELEMETRY='1',
                       DO_NOT_TRACK='1', CI='1')
            for key in ('CODEX_HOME', 'NATIVE_READER_ROOT', 'PYTHONPATH', 'VIRTUAL_ENV'):
                env.pop(key, None)
            cli = Path(env['SKILLS_CLI_ROOT']).resolve() / 'bin/cli.mjs'
            result = subprocess.run(['node', str(cli), 'add', str(source), '--skill', NAME,
                                     '--agent', 'codex', '--copy', '--yes'],
                                    cwd=work, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            shutil.rmtree(source)
            packages = [p.parent for p in work.rglob('SKILL.md')]
            self.assertEqual([p.name for p in packages], [NAME])
            package, = packages
            environment = root / 'empty-env'
            builder = venv.EnvBuilder(with_pip=False)
            builder.create(environment)
            interpreter = builder.ensure_directories(environment).env_exe
            def run(*args):
                return subprocess.run([interpreter, '-I', '-B', *map(str, args)], cwd=work,
                                      env=env, capture_output=True, text=True)
            package_check = package / 'scripts/package_check.py'
            checked = run(package_check)
            self.assertEqual(checked.returncode, 0, checked.stderr)
            self.assertEqual(json.loads(checked.stdout)['result'], 'PASS')
            for page in package.rglob('*.md'):
                for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', page.read_text()):
                    target = urlsplit(link)
                    if target.scheme or not target.path:
                        continue
                    path = (page.parent / unquote(target.path)).resolve()
                    self.assertTrue(path.is_relative_to(package.resolve()) and path.exists(), (page, link))
            for name in ('translator', 'bore_check', 'state'):
                code = ('import importlib,pathlib,sys; root=pathlib.Path(sys.argv[1]);'
                        'sys.path.insert(0,str(root)); module=importlib.import_module(sys.argv[2]);'
                        'assert pathlib.Path(module.__file__).resolve().parent==root')
                result = run('-c', code, (package / 'scripts').resolve(), name)
                self.assertEqual(result.returncode, 0, result.stderr)
            planned = run(package / 'scripts/translator.py', '--application', 'openscad',
                          '--bridge', 'Nilusche/OpenscadMCP', '--operation', 'edit-bore-diameter')
            self.assertEqual(planned.returncode, 0, planned.stderr)
            self.assertEqual(json.loads(planned.stdout)['status'], 'DOCUMENTED')
            fixture = package / 'fixtures/plate.scad'
            original = fixture.read_bytes()
            fixture.write_bytes(original + b'// tamper')
            self.assertNotEqual(run(package_check).returncode, 0)
            fixture.unlink()
            self.assertNotEqual(run(package_check).returncode, 0)
            fixture.write_bytes(original)
            (package / 'mappings/unregistered.json').write_text('{}')
            self.assertNotEqual(run(package_check).returncode, 0)
