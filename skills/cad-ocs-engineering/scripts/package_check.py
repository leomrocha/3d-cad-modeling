#!/usr/bin/env python3
"""Check an installed skill's files, dependencies and optional read-only OCS link."""
import argparse
import hashlib
import importlib
import importlib.metadata
import json
from pathlib import Path
import sys


def check(package, session=None, descriptor=None):
    package = Path(package).resolve()
    manifest = json.loads((package / 'package-manifest.json').read_text())
    checked = 0
    for relative, row in manifest['files'].items():
        path = (package / relative).resolve()
        if not path.is_relative_to(package) or hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            raise ValueError('Package file hash mismatch: ' + relative)
        checked += 1
    scripts = package / 'scripts'
    # Only this skill supplies reusable code; installed software dependencies
    # remain on the interpreter's site-packages path.
    sys.path.insert(0, str(scripts))
    imported = []
    for path in sorted(scripts.glob('*.py')):
        if path.stem == 'package_check':
            continue
        module = importlib.import_module(path.stem)
        if Path(module.__file__).resolve().parent != scripts:
            raise ValueError('Module came from outside the installed package: ' + path.stem)
        imported.append(path.stem)
    dependencies = {}
    for line in (package / 'requirements.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        name, version = line.split('==')
        actual = importlib.metadata.version(name)
        if actual != version:
            raise ValueError('Dependency version mismatch: ' + name + ' requires ' + version + ', found ' + actual)
        dependencies[name] = actual
    if manifest['skill'] == 'cad-ocs-engineering':
        for name in ['cadtools.runtime', 'cadtools.geometry', 'cadtools.verification']:
            module = importlib.import_module(name)
            if not Path(module.__file__).resolve().is_relative_to(scripts):
                raise ValueError('OCS adapter came from outside the package')
            imported.append(name)
        import envelope_job_runner
        envelope_job_runner.sab_reader_preflight()
    result = {'result': 'PASS', 'skill': manifest['skill'], 'hashed_files': checked,
              'imported_modules': imported, 'dependencies': dependencies}
    if session or descriptor:
        if manifest['skill'] != 'cad-ocs-engineering':
            raise ValueError('OCS connection belongs to cad-ocs-engineering')
        import ocs_control
        descriptors = ocs_control.descriptors(explicit=descriptor, session=session)
        if len(descriptors) != 1:
            raise ValueError('Select exactly one existing OCS session')
        state = ocs_control.request(descriptors[0], {'op': 'state'}, timeout=15)
        if state.get('ok') is not True:
            raise ValueError('OCS state read failed')
        result['ocs'] = {'result': 'PASS', 'operation': 'state', 'mutations': 0,
                         'document_id': state.get('document_id'), 'revision': state.get('revision')}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session')
    parser.add_argument('--descriptor')
    args = parser.parse_args()
    try:
        print(json.dumps(check(Path(__file__).resolve().parents[1], args.session, args.descriptor), indent=2))
    except (OSError, ValueError, ImportError, RuntimeError) as error:
        print(json.dumps({'result': 'FAIL', 'error': str(error)}))
        sys.exit(1)
