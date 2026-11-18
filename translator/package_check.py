"""Verify an installed, standard-library-only CAD MCP translator distribution."""
import hashlib
import json
from pathlib import Path
import sys


REQUIRED = {
    'SKILL.md', 'references/operations.md', 'references/contributing.md',
    'mappings/openscad.json', 'mappings/freecad.json', 'mappings/fusion.json',
    'fixtures/plate.scad', 'scripts/translator.py', 'scripts/state.py',
    'scripts/bore_check.py', 'scripts/package_check.py', 'requirements.txt', 'LICENSE',
}


def check(package):
    root = Path(package).resolve()
    paths = set()
    for path in root.rglob('*'):
        if path.is_symlink():
            raise ValueError('Unexpected symlink: ' + str(path))
        if path.is_dir():
            continue
        relative = path.relative_to(root)
        if relative.parts[:2] == ('scripts', '__pycache__') and path.suffix == '.pyc':
            continue
        paths.add(relative.as_posix())
    expected = REQUIRED | {'package-manifest.json'}
    if paths != expected:
        raise ValueError('Package inventory mismatch: ' + ', '.join(sorted(paths ^ expected)))
    manifest = json.loads((root / 'package-manifest.json').read_text())
    if manifest['skill'] != 'cad-mcp-translator' or set(manifest['files']) != REQUIRED:
        raise ValueError('Translator manifest inventory mismatch')
    for relative, row in manifest['files'].items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != row['sha256']:
            raise ValueError('Package hash mismatch: ' + relative)
    return {'result': 'PASS', 'skill': manifest['skill'], 'hashed_files': len(REQUIRED)}


if __name__ == '__main__':
    try:
        print(json.dumps(check(Path(__file__).resolve().parents[1])))
    except (KeyError, OSError, TypeError, ValueError) as error:
        print(json.dumps({'result': 'FAIL', 'error': str(error)}), file=sys.stderr)
        sys.exit(1)
