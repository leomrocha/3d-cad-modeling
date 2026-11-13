#!/usr/bin/env python3
"""Generate independently installable skills from the canonical reusable code."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import re
import importlib.util
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('cad-ocs-engineering', 'cad-drawing-inspection', 'cad-source-intake')
HOST_ONLY = {'scripts/build_skill_packages.py'}


def local_links(document):
    targets = set()
    for target in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        parsed = urlsplit(target)
        if not parsed.scheme and parsed.path:
            targets.add((document.parent / unquote(parsed.path)).resolve())
    return targets


def check_registrations():
    """Require human-readable helper/procedure indexes and combined source coverage."""
    tool_index = ROOT / 'docs/tools.md'
    skill_index = ROOT / 'skills/README.md'
    tools, procedures = local_links(tool_index), local_links(skill_index)
    register = json.loads((ROOT / 'research/sources/source-register.json').read_text())
    registered = {item.get('local_source_path') for item in register['sources']}
    markdown = (ROOT / 'research/sources/source-register.md').read_text()
    failures = []
    required = {ROOT / relative for relative in source_paths() if Path(relative).name != '__init__.py'}
    for path in required:
        if path.resolve() not in tools:
            failures.append('Tool catalogue entry missing: ' + str(path.relative_to(ROOT)))
    main = ROOT / 'skills/cad-ocs-engineering/SKILL.md'
    references = {path for path in local_links(main)
                  if path.is_relative_to(main.parent / 'references')}
    for path in references:
        if path not in procedures:
            failures.append('Skill procedure index entry missing: ' + str(path.relative_to(ROOT)))
    # Source coverage includes reusable scripts and procedures invoked by the skill.
    for path in required | references:
        relative = str(path.relative_to(ROOT))
        candidates = {relative, '${MODELING_ROOT}/' + relative}
        matches = [item for item in register['sources'] if item.get('local_source_path') in candidates]
        if not candidates & registered:
            failures.append('Combined source registration missing: ' + relative)
        elif any(not re.search(r'^#{2,3} .*' + re.escape(item['id']) + r'\b', markdown, re.M)
                 for item in matches):
            failures.append('Source Markdown index entry missing: ' + relative)
    if failures:
        raise ValueError('\n'.join(sorted(failures)))
    documents = register.get('source_record_documents', [])
    if documents:
        spec = importlib.util.spec_from_file_location(
            'tooling_source_registry', ROOT / 'research/tools/build_workflow_register.py')
        registry = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(registry)
        registry.merge_source_records(ROOT, documents, register['registered_at'], check=True)
    return {'result': 'PASS', 'tool_entries': len(required), 'procedure_entries': len(references)}


def source_paths(committed=False):
    if committed:
        paths = subprocess.check_output(
            ['git', 'ls-tree', '-r', '--name-only', 'HEAD', '--', 'scripts'],
            cwd=ROOT, text=True).splitlines()
        return sorted(p for p in paths if p.endswith('.py') and '__pycache__' not in Path(p).parts)
    paths = sorted(p for p in (ROOT / 'scripts').rglob('*.py') if '__pycache__' not in p.parts)
    for path in paths:
        if not path.resolve().is_relative_to((ROOT / 'scripts').resolve()):
            raise ValueError('Reusable script points outside this repository: ' + str(path.relative_to(ROOT)))
    return [str(p.relative_to(ROOT)) for p in paths]


def module_name(relative):
    parts = list(Path(relative).relative_to('scripts').with_suffix('').parts)
    if parts[-1] == '__init__':
        parts.pop()
    return '.'.join(parts)


def dependency_closure(seeds, paths, committed=False):
    """Include local Python imports and their package initializers transitively."""
    modules = {module_name(p): p for p in paths}
    selected, pending = set(), list(seeds)
    while pending:
        relative = pending.pop()
        if relative in selected:
            continue
        if relative not in paths or relative in HOST_ONLY:
            raise ValueError('Unassigned or missing runtime dependency: ' + relative)
        selected.add(relative)
        try:
            tree = ast.parse(source_bytes(relative, committed), filename=relative)
        except SyntaxError as error:
            raise ValueError('Invalid reusable script: ' + relative + ': ' + error.msg) from error
        name = module_name(relative)
        package = name if Path(relative).name == '__init__.py' else name.rpartition('.')[0]
        imported = [package] if package else []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                base = node.module or ''
                if node.level:
                    parts = package.split('.') if package else []
                    # scripts/ also works as the enclosing namespace package.
                    if node.level > len(parts) + 1:
                        raise ValueError('Relative import outside script package: ' + relative)
                    base = '.'.join(parts[:len(parts) - node.level + 1] + ([base] if base else []))
                imported.append(base)
                imported.extend(base + '.' + alias.name if base else alias.name for alias in node.names)
        for imported_name in imported:
            parts = imported_name.split('.')
            for index in range(1, len(parts) + 1):
                dependency = modules.get('.'.join(parts[:index]))
                if dependency and dependency not in selected:
                    pending.append(dependency)
    return sorted(selected)


def inputs(name, committed=False):
    if name not in SKILLS:
        raise ValueError('Unknown skill package: ' + name)
    paths = source_paths(committed)
    common = ['scripts/component_records.py', 'scripts/part_index.py', 'scripts/package_check.py']
    if name == 'cad-source-intake':
        return dependency_closure(common + ['scripts/source_intake.py'], paths, committed)
    if name == 'cad-drawing-inspection':
        return dependency_closure(common + ['scripts/dxf_inspect.py'], paths, committed)
    # All reusable scripts have a default owner: the complete CAD runtime.
    # The builder itself belongs to the repository's build tooling.
    return dependency_closure([p for p in paths if p not in HOST_ONLY], paths, committed)


def source_bytes(relative, committed=False):
    if committed:
        return subprocess.check_output(["git", "show", "HEAD:" + relative], cwd=ROOT)
    return (ROOT / relative).read_bytes()


def expected(name, committed=False):
    files = {str(Path(p).relative_to('scripts')): p for p in inputs(name, committed)}
    result = {'scripts/' + target: source_bytes(source, committed) for target, source in files.items()}
    result['LICENSE'] = source_bytes('LICENSE', committed)
    result['NOTICE.md'] = source_bytes('scripts/cadtools/NOTICE.md', committed)
    result['requirements.txt'] = (source_bytes('requirements-native.txt', committed)
                                  if name != 'cad-source-intake' else b'# Python 3.12 standard library only.\n')
    manifest = {'skill': name, 'generated_by': 'scripts/build_skill_packages.py',
                'files': {target: {'source': files.get(target.removeprefix('scripts/'),
                           'requirements-native.txt' if target == 'requirements.txt' and name != 'cad-source-intake'
                           else 'LICENSE' if target == 'LICENSE' else 'scripts/cadtools/NOTICE.md' if target == 'NOTICE.md' else 'standard-library declaration'),
                           'sha256': hashlib.sha256(data).hexdigest()}
                          for target, data in sorted(result.items())}}
    result['package-manifest.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
    return result


def build(check=False, committed=False):
    failures = []
    # Preflight every package before changing any generated files.
    plans = []
    for name in SKILLS:
        target = ROOT / 'skills' / name
        files = expected(name, committed)
        old = target / 'package-manifest.json'
        previous = json.loads(old.read_text())['files'] if old.exists() else {}
        for relative in set(previous) | set(files):
            if not (target / relative).resolve().is_relative_to(target.resolve()):
                raise ValueError('Manifest path outside skill package: ' + relative)
        for path in (target / 'scripts').rglob('*.py'):
            if '__pycache__' in path.parts:
                continue
            relative = str(path.relative_to(target))
            if relative not in previous and relative not in files:
                raise ValueError('Unassigned packaged script; register canonical source first: ' + name + '/' + relative)
        plans.append((name, target, files, previous))
    for name, target, files, previous in plans:
        for stale in sorted(set(previous) - set(files)):
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


def complete(regenerate=False, cli_root=None, reader_root=None):
    """Require source sync and actual isolated installation tests before completion."""
    cli_root = cli_root or os.environ.get('SKILLS_CLI_ROOT')
    reader_root = reader_root or os.environ.get('NATIVE_READER_ROOT')
    if not cli_root or not reader_root:
        raise ValueError('Completion requires SKILLS_CLI_ROOT and NATIVE_READER_ROOT '
                         '(or --cli-root and --reader-root); installation checks must run.')
    cli_root, reader_root = Path(cli_root).resolve(), Path(reader_root).resolve()
    if not (cli_root / 'bin/cli.mjs').is_file() or not (reader_root / 'ezdxf').is_dir():
        raise ValueError('Completion requires an existing skills CLI and native-reader dependency directory.')
    if regenerate:
        build()
    build(check=True)
    check_registrations()
    env = dict(os.environ, SKILLS_CLI_ROOT=str(cli_root), NATIVE_READER_ROOT=str(reader_root),
               PYTHONDONTWRITEBYTECODE='1', DISABLE_TELEMETRY='1', DO_NOT_TRACK='1')
    for pattern in ('test_skill_package_build.py', 'test_source_registration.py', 'test_skill_packages.py'):
        process = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover',
                                  '-s', 'tests', '-p', pattern, '-v'], cwd=ROOT, env=env,
                                 text=True, capture_output=True)
        if process.returncode:
            raise ValueError('Package completion checks failed (' + pattern + '):\n' + process.stdout + process.stderr)
        print(process.stdout + process.stderr, file=sys.stderr, end='')
    # Catch helpers changed or created during validation.
    build(check=True)
    check_registrations()
    return {'result': 'PASS', 'mode': 'finalize' if regenerate else 'verify',
            'skills': list(SKILLS), 'synchronisation': 'PASS', 'registrations': 'PASS',
            'isolated_installation_checks': 'PASS',
            'telemetry': 'disabled', 'live_ocs': 'caller-selected descriptor required; optional state check'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--check', action='store_true')
    modes.add_argument('--finalize', action='store_true', help='Regenerate, verify synchronisation and require isolated install checks')
    modes.add_argument('--verify', action='store_true', help='Require synchronisation and isolated install checks without regeneration')
    parser.add_argument('--committed', action='store_true', help='Read canonical bytes from local HEAD; preserve concurrent uncommitted implementations')
    parser.add_argument('--cli-root', help='Existing skills CLI package directory')
    parser.add_argument('--reader-root', help='Existing pinned Python dependency directory')
    args = parser.parse_args()
    if args.committed and (args.finalize or args.verify):
        parser.error('Completion checks use current sources; --committed cannot be combined with --finalize or --verify')
    try:
        result = complete(args.finalize, args.cli_root, args.reader_root) if args.finalize or args.verify else build(args.check, args.committed)
        print(json.dumps(result))
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')
