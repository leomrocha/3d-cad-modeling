#!/usr/bin/env python3
"""Generate independently installable skills from the canonical reusable code."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('component-cad', 'drawing-inspection', 'source-intake')


def inputs(name):
    common = ['scripts/component_records.py', 'scripts/part_index.py', 'scripts/package_check.py']
    if name == 'source-intake':
        return common + ['scripts/source_intake.py']
    if name == 'drawing-inspection':
        return common + ['scripts/dxf_inspect.py']
    return sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'scripts').rglob('*.py')
                  if p.name not in {'build_skill_packages.py'} and '__pycache__' not in p.parts)


def source_bytes(relative, committed=False):
    if committed:
        return subprocess.check_output(["git", "show", "HEAD:" + relative], cwd=ROOT)
    return (ROOT / relative).read_bytes()


def expected(name, committed=False):
    files = {str(Path(p).relative_to('scripts')): p for p in inputs(name)}
    result = {'scripts/' + target: source_bytes(source, committed) for target, source in files.items()}
    result['LICENSE'] = source_bytes('LICENSE', committed)
    result['NOTICE.md'] = source_bytes('scripts/cadtools/NOTICE.md', committed)
    result['requirements.txt'] = (source_bytes('requirements-native.txt', committed)
                                  if name != 'source-intake' else b'# Python 3.12 standard library only.\n')
    manifest = {'skill': name, 'generated_by': 'scripts/build_skill_packages.py',
                'files': {target: {'source': files.get(target.removeprefix('scripts/'),
                           'requirements-native.txt' if target == 'requirements.txt' and name != 'source-intake'
                           else 'LICENSE' if target == 'LICENSE' else 'scripts/cadtools/NOTICE.md' if target == 'NOTICE.md' else 'standard-library declaration'),
                           'sha256': hashlib.sha256(data).hexdigest()}
                          for target, data in sorted(result.items())}}
    result['package-manifest.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    return result


def build(check=False, committed=False):
    failures = []
    for name in SKILLS:
        target = ROOT / 'skills' / name
        files = expected(name, committed)
        old = target / 'package-manifest.json'
        previous = json.loads(old.read_text())['files'] if old.exists() else {}
        for stale in set(previous) - set(files):
            if check:
                failures.append(name + '/' + stale + ' is stale')
            else:
                (target / stale).unlink(missing_ok=True)
        for relative, data in files.items():
            path = target / relative
            if check:
                if not path.is_file() or path.read_bytes() != data:
                    failures.append(name + '/' + relative + ' differs from canonical source')
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
    if failures:
        raise ValueError('\n'.join(failures))
    return {'result': 'PASS', 'mode': 'check' if check else 'generate', 'skills': list(SKILLS), 'source': 'committed HEAD' if committed else 'worktree'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--committed', action='store_true', help='Read canonical bytes from local HEAD; preserve concurrent uncommitted implementations')
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.check, args.committed)))
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
