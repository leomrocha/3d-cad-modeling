#!/usr/bin/env python3
"""Audit tracked paths, text, links, and generated packages in one Git snapshot."""
import argparse
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit


YEAR = r'[12][0-9]{3}'
MONTH = (r'Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|'
         r'Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?')
DATE = re.compile(
    rf'(?<![0-9A-Za-z])(?:{YEAR}[-_/.]\d{{1,2}}[-_/.]\d{{1,2}}|'
    rf'\d{{1,2}}[-_/.]\d{{1,2}}[-_/.]{YEAR}|'
    rf'\d{{1,2}}[ _-]+(?:{MONTH})[ _-]+{YEAR}|'
    rf'(?:{MONTH})[ _-]+\d{{1,2}},?[ _-]+{YEAR})(?!\d)', re.IGNORECASE)
COMPACT_DATE = re.compile(r'(?<![0-9A-Za-z])([12]\d{3})(\d{2})(\d{2})(?![0-9A-Za-z])')
COPYRIGHT_YEAR = re.compile(rf'\bcopyright\s*(?:\(c\)|©)?\s*({YEAR}(?:\s*[-–,]\s*{YEAR})*)\b', re.I)
STANDARD_EDITION = re.compile(rf'\b(?:ISO(?:/IEC)?|IEC|DIN|EN|ASTM)\s+[A-Z]*\d+(?:-\d+)?:({YEAR})\b')
PROTOCOL_DATE = re.compile(
    rf'(?:"(?:protocolVersion|protocol_version)"\s*:\s*"|'
    rf'https://modelcontextprotocol\.io/specification/)({YEAR}-\d{{2}}-\d{{2}})')
PRIVATE_REFERENCE = re.compile(
    r'(?<![a-z0-9])fer' r'me(?![a-z0-9])|/(?:home|Users)/[^/\s`"\']+/(?:projects/|\.[\w.-]+/)|'
    r'\$\{[A-Z_]*RAW_ROOT\}|\b(?:private|personal)[ -]+(?:research[ -]+)?archive\b',
    re.I)
HISTORICAL_PROSE = re.compile(
    r'\bin (?:this|the previous) (?:chat|session)\b|\binitial live evidence\b|'
    r'\brepository [\w-]+ training trial\b', re.I)

ASSET_EXTENSIONS = frozenset({
    '.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.bmp', '.ico', '.tif', '.tiff',
    '.mp4', '.mov', '.webm', '.mp3', '.ogg', '.wav', '.pdf', '.zip', '.npz',
    '.step', '.stp', '.stl', '.obj', '.sat', '.sab', '.iges', '.igs', '.dxf',
    '.dwg', '.brep', '.ifc', '.blend', '.fcstd', '.f3d', '.3mf',
})
MARKDOWN_LINK = re.compile(
    r'\]\(\s*(?:<([^>\n]+)>|((?:\\[()]|[^\s()]|\([^()]*\))+))'
    r'(?:\s+(?:"[^"]*"|\'[^\']*\'))?\s*\)')
MARKDOWN_REFERENCE = re.compile(r'^\s{0,3}\[(?!\^)[^\]]+\]:\s*(?:<([^>]+)>|(\S+))')
HTML_LINK = re.compile(r'''\b(?:href|src|poster)\s*=\s*(["'])(.*?)\1''', re.I)
INLINE_CODE = re.compile(r'(`+).*?\1')
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')
JEKYLL_LINK = re.compile(r"^{{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*}}$")
BUILDER = 'scripts/build_skill_packages.py'


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    rule: str
    match: str
    blocking: bool = True

    def __str__(self):
        level = 'ERROR' if self.blocking else 'REVIEW'
        return f'{self.path}:{self.line}: {level} {self.rule}: {self.match!r}'


def git(*args):
    return subprocess.check_output(['git', *args])


def snapshot(commit):
    """Read paths, modes, and object IDs solely from the selected Git tree or index."""
    if commit is not None:
        tree = git('rev-parse', '--verify', '--end-of-options', commit + '^{commit}').strip().decode()
        rows = git('ls-tree', '-rz', tree)
    else:
        rows = git('ls-files', '--stage', '-z')

    entries = {}
    for row in rows.split(b'\0'):
        if not row:
            continue
        metadata, raw_path = row.split(b'\t', 1)
        mode, second, third = metadata.decode().split()
        path = os.fsdecode(raw_path)
        if commit is None and third != '0':
            raise ValueError(f'Unmerged index entry: {path}')
        entries[path] = (mode, third if commit is not None else second)
    return entries


@contextmanager
def read_objects():
    with subprocess.Popen(['git', 'cat-file', '--batch'], stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE) as proc:
        def read(object_id):
            proc.stdin.write(object_id.encode() + b'\n')
            proc.stdin.flush()
            header = proc.stdout.readline().split()
            if len(header) != 3 or header[1] != b'blob':
                raise ValueError(f'Unavailable Git blob: {object_id}')
            data = proc.stdout.read(int(header[2]))
            if proc.stdout.read(1) != b'\n':
                raise ValueError(f'Incomplete Git blob: {object_id}')
            return data

        try:
            yield read
        finally:
            proc.stdin.close()


def valid_date(year, month, day):
    try:
        date(int(year), int(month), int(day))
    except ValueError:
        return False
    return True


def dates(line):
    for match in DATE.finditer(line):
        yield match.span(), match[0]
    for match in COMPACT_DATE.finditer(line):
        if valid_date(*match.groups()):
            yield match.span(), match[0]


def scan_line(path, number, line, *, filename=False):
    for pattern, rule in ((PRIVATE_REFERENCE, 'private-reference'),
                          (HISTORICAL_PROSE, 'historical-prose')):
        for match in pattern.finditer(line):
            yield Finding(path, number, rule, match[0])

    labelled = {}
    if not filename:
        for pattern, rule in ((COPYRIGHT_YEAR, 'copyright-year'),
                              (STANDARD_EDITION, 'standard-edition'),
                              (PROTOCOL_DATE, 'protocol-version')):
            for match in pattern.finditer(line):
                if rule == 'protocol-version' and not valid_date(*match[1].split('-')):
                    continue
                labelled[match.span(1)] = rule
                yield Finding(path, number, rule, match[1], blocking=False)

    # Allow the dated attribution explicitly requested for source-study comments.
    if not filename and path.endswith(".py"):
        attribution = re.fullmatch(
            r"# Read (\d{4}-\d{2}-\d{2})\. Upstream licence: [\w.() +\-]+\. https://github\.com/[\w.-]+/[\w.-]+", line)
        if attribution and valid_date(*attribution[1].split("-")):
            labelled[attribution.span(1)] = "source-attribution"
            yield Finding(path, number, "source-attribution", attribution[1], blocking=False)

    for span, value in dates(line):
        if span not in labelled:
            yield Finding(path, number, 'dated-path' if filename else 'calendar-date', value)


def link_targets(line, markdown):
    if markdown:
        for pattern in (MARKDOWN_LINK, MARKDOWN_REFERENCE):
            for match in pattern.finditer(line):
                yield match[1] or match[2]
    for match in HTML_LINK.finditer(line):
        yield match[2]


def resolve_link(path, link):
    # Generated GitHub Pages links map back to their source documents.
    base = posixpath.dirname(path)
    relative_url = JEKYLL_LINK.fullmatch(link)
    if relative_url:
        base = 'docs'
        link = relative_url[1].lstrip('/')
        if not link:
            return base
    if link.startswith(('{{', '{%')):
        return None
    parsed = urlsplit(link)
    if (parsed.scheme and parsed.scheme != 'file') or parsed.netloc or not parsed.path:
        return None
    target = unquote(parsed.path).replace(r'\(', '(').replace(r'\)', ')')
    if target.startswith('/'):
        if not parsed.scheme and path.startswith('docs/'):
            return posixpath.normpath('docs' + target)
        return target
    return posixpath.normpath(posixpath.join(base, target))


def scan_text(path, body, tracked, directories):
    markdown = path.endswith(('.md', '.markdown'))
    html = path.endswith(('.html', '.htm'))
    fence = None
    for number, line in enumerate(body.splitlines(), 1):
        yield from scan_line(path, number, line)
        if not (markdown or html):
            continue
        marker = FENCE.match(line) if markdown else None
        if marker:
            delimiter = marker[1]
            if fence is None:
                fence = delimiter
            elif delimiter.startswith(fence) and line[marker.end():].strip() == '':
                fence = None
            continue
        if fence:
            continue
        for link in link_targets(INLINE_CODE.sub('', line), markdown):
            try:
                target = resolve_link(path, link)
            except ValueError:
                yield Finding(path, number, 'invalid-link', link)
                continue
            if target is None or target in tracked or target in directories:
                continue
            if path.startswith('docs/') and target.endswith('.html') and target[:-5] + '.md' in tracked:
                continue
            yield Finding(path, number, 'untracked-link', link)


def package_findings(root):
    """Reuse the package builder against the same bytes audited above."""
    result = subprocess.run([sys.executable, BUILDER, '--check'], cwd=root,
                            text=True, capture_output=True)
    if not result.returncode:
        return
    for message in (result.stderr or result.stdout).splitlines():
        path, separator, _ = message.partition(' ')
        if separator and path.startswith('cad-') and '/' in path:
            path = 'skills/' + path
        else:
            path = BUILDER
        yield Finding(path, 1, 'package-sync', message)


def check(commit):
    entries = snapshot(commit)
    directories = {parent.as_posix() for name in entries for parent in PurePosixPath(name).parents}
    with tempfile.TemporaryDirectory(prefix='repository-audit-') as temporary, read_objects() as read:
        root = Path(temporary)
        for path, (mode, object_id) in sorted(entries.items()):
            yield from scan_line(path, 1, path, filename=True)
            if mode not in ('100644', '100755'):
                yield Finding(path, 1, 'unsupported-entry', mode)
                continue

            asset = PurePosixPath(path).suffix.lower() in ASSET_EXTENSIONS
            package_input = path == BUILDER or path.startswith(
                ('scripts/', 'skills/', 'translator/', 'format_translation/')) or path in (
                    'LICENSE', 'requirements-native.txt', 'docs/modeling-operation-selection.md')
            if asset and not package_input:
                continue
            data = read(object_id)
            if package_input:
                output = root / path
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(data)
            if not asset and b'\0' not in data:
                yield from scan_text(path, data.decode('utf-8', errors='replace'), entries, directories)
        if BUILDER in entries and (root / BUILDER).is_file():
            yield from package_findings(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--index', action='store_true', help='Check the staged index')
    target.add_argument('--commit', metavar='REV', help='Check the tree of a local commit')
    args = parser.parse_args()
    try:
        findings = list(check(args.commit))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'Repository audit failed: {error}\n')
    for finding in findings:
        print(finding)
    failures = sum(finding.blocking for finding in findings)
    print(f'Repository audit {"FAIL" if failures else "PASS"} '
          f'({failures} errors, {len(findings) - failures} labelled identifiers or notices)')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
