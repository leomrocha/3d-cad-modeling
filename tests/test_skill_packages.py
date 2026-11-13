"""Independent local CLI installs; explicit cached CLI and dependency inputs only.

Run with SKILLS_CLI_ROOT and NATIVE_READER_ROOT set to existing software locations.
Set PACKAGING_CHECK_OUTPUT to retain a portable JSON result outside the test tempdir.
"""
import hashlib
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

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('cad-ocs-engineering', 'cad-drawing-inspection', 'cad-source-intake')


@unittest.skipUnless(os.environ.get('SKILLS_CLI_ROOT') and os.environ.get('NATIVE_READER_ROOT'),
                     'Requires explicit cached skills CLI and pinned reader dependencies')
class IndependentSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='independent-skills-')
        cls.addClassCleanup(cls.temp.cleanup)
        cls.base = Path(cls.temp.name)
        cls.home = cls.base / 'home'
        cls.home.mkdir()
        env_path = cls.base / 'python-env'
        venv.EnvBuilder(with_pip=False).create(env_path)
        cls.python = env_path / 'bin/python'
        site = next((env_path / 'lib').glob('python*/site-packages'))
        deps = Path(os.environ['NATIVE_READER_ROOT']).resolve()
        for path in deps.iterdir():
            if path.name in {'__pycache__', 'bin', 'share'}:
                continue
            if path.is_dir():
                shutil.copytree(path, site / path.name)
            elif path.suffix == '.py':
                shutil.copy2(path, site / path.name)
        cls.env = {key: value for key, value in os.environ.items()
                   if key not in {'PYTHONPATH', 'PYTHONHOME', 'VIRTUAL_ENV', 'NODE_OPTIONS',
                                  'CODEX_HOME', 'NATIVE_READER_ROOT', 'SKILLS_CLI_ROOT'}}
        cls.env.update(HOME=str(cls.home), XDG_CONFIG_HOME=str(cls.home / '.config'),
                       DISABLE_TELEMETRY='1', DO_NOT_TRACK='1', CI='1',
                       PYTHONDONTWRITEBYTECODE='1')
        cls.cli = Path(os.environ['SKILLS_CLI_ROOT']).resolve() / 'bin/cli.mjs'
        cls.source = cls.base / 'local-source'
        (cls.source / 'skills').mkdir(parents=True)
        for name in NAMES:
            shutil.copytree(ROOT / 'skills' / name, cls.source / 'skills' / name,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        cls.results = {'cli': '1.8.1', 'telemetry': 'disabled', 'source': 'local copied skills',
                       'isolation': 'temporary virtualenv; copied declared software dependencies; cleared Python path; separate HOME and cwd',
                       'skills': {}}
        cls.installed = {}
        for name in NAMES:
            cwd = cls.base / name
            cwd.mkdir()
            listed = subprocess.run(['node', str(cls.cli), 'add', str(cls.source), '--list'],
                                    cwd=cwd, env=cls.env, text=True, capture_output=True)
            if listed.returncode or not all(n in listed.stdout for n in NAMES):
                raise AssertionError('CLI discovery failed: ' + listed.stdout + listed.stderr)
            install = subprocess.run(['node', str(cls.cli), 'add', str(cls.source), '--skill', name,
                                      '--agent', 'codex', '--copy', '--yes'], cwd=cwd,
                                     env=cls.env, text=True, capture_output=True)
            if install.returncode:
                raise AssertionError('Local CLI installation failed: ' + install.stdout + install.stderr)
            found = list(cwd.rglob('SKILL.md'))
            matches = [p.parent for p in found if p.parent.name == name]
            if len(matches) != 1:
                raise AssertionError('Expected exactly one copied installed skill: ' + str(matches))
            cls.installed[name] = matches[0]
            cls.results['skills'][name] = {'cli_discovery': 'PASS', 'individual_copy_install': 'PASS'}
        # Execution cannot fall back to the temporary CLI source directory.
        shutil.rmtree(cls.source)

    def run_python(self, name, code, *args):
        package = self.installed[name]
        process = subprocess.run([str(self.python), '-I', '-B', '-c',
                                  'import sys;sys.path.insert(0,sys.argv[1]);\n' + code,
                                  str(package / 'scripts'), *map(str, args)],
                                 cwd=self.base, env=self.env, text=True, capture_output=True)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        return json.loads(process.stdout)

    def test_each_package_links_imports_and_command_entrypoints(self):
        for name in NAMES:
            with self.subTest(skill=name):
                package = self.installed[name]
                links = 0
                for doc in package.rglob('*.md'):
                    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
                        parsed = urlsplit(target)
                        if parsed.scheme or target.startswith('#'):
                            continue
                        dest = (doc.parent / unquote(parsed.path)).resolve()
                        self.assertTrue(dest.is_relative_to(package), (doc, target))
                        self.assertTrue(dest.exists(), (doc, target))
                        links += 1
                result = self.run_python(name, "from package_check import check; import json; from pathlib import Path; print(json.dumps(check(Path(sys.argv[1]).parent)))")
                self.assertEqual(result['result'], 'PASS')
                self.results['skills'][name].update(local_links=links, package_check=result)
                if name == 'cad-ocs-engineering':
                    self.assertIn('$cad-ocs-engineering', (package / 'agents/openai.yaml').read_text())
                    for reference in ['ocs-control.md', 'model-contract.md', 'computational-engineering.md', 'sources-and-capabilities.md']:
                        self.assertTrue((package / 'references' / reference).is_file())
                    main = (package / 'SKILL.md').read_text()
                    self.assertIn('## Establish the modeling contract', main)
                    self.assertIn('### Execute and improve component jobs', main)
                    self.results['skills'][name]['full_original_and_component_instructions'] = 'PASS'
                entries = ['source_intake', 'part_index', 'component_records'] if name == 'cad-source-intake' else \
                          ['dxf_inspect', 'part_index', 'component_records'] if name == 'cad-drawing-inspection' else \
                          ['envelope_job_runner', 'rounded_tube', 'model_inventory', 'retained_artifacts', 'ocs_control', 'check_contract']
                for entry in entries:
                    process = subprocess.run([str(self.python), '-E', '-s', '-B', str(package / 'scripts' / (entry + '.py')), '--help'],
                                             cwd=self.base, env=self.env, text=True, capture_output=True)
                    self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
                self.results['skills'][name]['command_help_entries'] = entries

    def test_source_intake_fixture(self):
        code = '''import hashlib,json,tempfile
from pathlib import Path
from source_intake import run,verify_revision
with tempfile.TemporaryDirectory() as folder:
 root=Path(folder); source=root/'source.txt'; source.write_bytes(b'original fixture\\n')
 spec={'job_name':'Isolated package fixture','revision_id':'r1','model':'synthetic fixture','request':{'text':'Register fixture only.','location':'packaging test'},'scope':{'statement':'Register the supplied local fixture.','requested_output':'source index','authorized_paths':[str(root)]},'sources':[{'id':'fixture','title':'Local fixture','summary':'Exact fixture bytes.','kind':'file','locator':str(source),'observed_at':'2026-11-13'}]}
 path=root/'input.json';path.write_text(json.dumps(spec));result=run(path,root/'output');index=verify_revision(Path(result['revision'])/'source-index.json')
 assert source.read_bytes()==b'original fixture\\n'
 assert index['sources'][0]['observation']['sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
 print(json.dumps({'result':'PASS','source_preserved':True,'receipt_verified':True}))'''
        self.results['skills']['cad-source-intake']['fixture'] = self.run_python('cad-source-intake', code)

    def test_dxf_fixture(self):
        code = '''import json,tempfile,hashlib
from pathlib import Path
import ezdxf
from dxf_inspect import inspect
with tempfile.TemporaryDirectory() as folder:
 source=Path(folder)/'drawing.dxf';doc=ezdxf.new();doc.units=4;doc.modelspace().add_circle((5,6),2);doc.saveas(source)
 before=hashlib.sha256(source.read_bytes()).hexdigest();result=inspect(source)
 assert result['units']['label']=='mm'
 assert result['counts']['by_type']=={'CIRCLE':1}
 assert before==hashlib.sha256(source.read_bytes()).hexdigest()
 print(json.dumps({'result':'PASS','units':'mm','circle_count':1,'source_preserved':True}))'''
        self.results['skills']['cad-drawing-inspection']['fixture'] = self.run_python('cad-drawing-inspection', code)

    def test_ocs_coordinate_contract_fixture(self):
        code = """import json
from check_contract import run
contract={'length_unit':'mm','tolerance':{'length':0.001,'angle_deg':0.01},'observations':{'point':{'kind':'point','origin':[0,0,0]},'plane':{'kind':'plane','origin':[0,0,0],'normal':[0,0,1]}},'checks':[{'id':'point-on-plane','kind':'on_plane','point':'point','plane':'plane'}],'evidence':{'kind':'synthetic_fixture','source':'isolated OCS merge fixture'}}
assert run(contract)['all_passed'] is True
contract['observations']['point']['origin']=[0,0,1]
assert run(contract)['all_passed'] is False
print(json.dumps({'result':'PASS','passing_and_failing_coordinates_checked':True,'native_mutations':0}))"""
        self.results['skills']['cad-ocs-engineering']['coordinate_contract_fixture'] = self.run_python('cad-ocs-engineering', code)

    def test_component_defaults_use_bundled_code_and_read_only_transport(self):
        code = '''import json
from pathlib import Path
from unittest.mock import patch
import ocs_control,envelope_job_runner,rounded_tube
from cadtools.runtime import load_helper,Client,Journal,CadError
from cadtools.geometry import Geometry
from cadtools.verification import save_reopen
scripts=Path(sys.argv[1]); helper=load_helper(scripts/'ocs_control.py')
assert Path(helper.__file__).parent==scripts
for module in [envelope_job_runner,rounded_tube]:
 captured=[]
 def parse(parser,*args,**kwargs):
  captured.append(parser);raise RuntimeError('argument capture')
 try:
  with patch('argparse.ArgumentParser.parse_args',parse):module.main()
 except RuntimeError as e:assert str(e)=='argument capture'
 defaults=captured[0].parse_args(['--help']) if False else {a.dest:a.default for a in captured[0]._actions}
 assert Path(defaults['control']).parent==scripts
 if 'cadtools_root' in defaults:assert defaults['cadtools_root']==scripts
class BlockSocket:
 def __init__(self,*args,**kwargs):raise AssertionError('Unexpected network')
with patch('socket.socket',BlockSocket):
 p=envelope_job_runner.sab_reader_preflight()
 assert p['result']=='PASS'
print(json.dumps({'result':'PASS','runtime':'bundled','runner_defaults':'bundled','dependency_preflight':'PASS','native_mutations':0}))'''
        self.results['skills']['cad-ocs-engineering']['defaults'] = self.run_python('cad-ocs-engineering', code)

    @unittest.skipUnless(os.environ.get('OCS_DESCRIPTOR'), 'Requires caller-selected running OCS descriptor')
    def test_read_only_ocs_connection(self):
        code = "from package_check import check; import json; from pathlib import Path; print(json.dumps(check(Path(sys.argv[1]).parent, descriptor=sys.argv[2])))"
        result = self.run_python('cad-ocs-engineering', code, os.environ['OCS_DESCRIPTOR'])
        self.assertEqual(result['ocs']['result'], 'PASS')
        self.assertEqual(result['ocs']['mutations'], 0)
        self.results['skills']['cad-ocs-engineering']['read_only_ocs'] = result['ocs']

    @classmethod
    def tearDownClass(cls):
        output = os.environ.get('PACKAGING_CHECK_OUTPUT')
        if output:
            Path(output).write_text(json.dumps(cls.results, indent=2) + '\n')


if __name__ == '__main__':
    unittest.main()
