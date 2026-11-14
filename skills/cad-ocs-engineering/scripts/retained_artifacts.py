#!/usr/bin/env python3
"""Verify an external retained-file manifest without changing its artifacts."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

from component_records import observe_file
from envelope_job_runner import parse_roots, portableize, resolve_locator


def write_table(path,rows,fields):
    """Write a new TSV and verify exact serialized rows; preserve existing outputs."""
    path=Path(path);fields=list(fields);rows=list(rows)
    if not fields or len(set(fields))!=len(fields) or any(not isinstance(f,str) or not f for f in fields):raise ValueError('Unique nonempty table fields required')
    if any(set(row)!=set(fields) for row in rows):raise ValueError('Every row must match the declared table schema')
    expected=[{k:'' if row[k] is None else str(row[k]) for k in fields} for row in rows]
    with path.open('x',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
    with path.open(newline='',encoding='utf-8') as stream:
        reader=csv.DictReader(stream,delimiter='\t');actual=list(reader)
        if reader.fieldnames!=fields or actual!=expected:raise ValueError('Table readback differs')
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),rows=len(rows),result='PASS')


def verify_manifest(manifest_path, roots):
    manifest_path = Path(manifest_path).resolve()
    package = manifest_path.parent
    before = observe_file(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if observe_file(manifest_path) != before:
        raise ValueError('Manifest changed during capture')
    if not isinstance(manifest, dict):
        raise ValueError('Manifest must contain an object')
    entries = manifest.get('files')
    if not isinstance(entries, list) or not entries:
        raise ValueError('Manifest requires a nonempty files list')
    checked, omitted, duplicates, seen = [], [], [], {}
    for index, row in enumerate(entries):
        if not isinstance(row, dict):
            raise ValueError('Manifest file entries must be objects')
        locator = row.get('retained_path', row.get('path'))
        if locator is None and 'retained_path' in row:
            if row.get('classification') or row.get('superseded_by'):
                omitted.append({'index': index, 'reason': row.get('classification', 'superseded')})
                continue
            raise ValueError('Null retained path requires an explicit classification')
        if not isinstance(locator, str) or not locator.strip():
            raise ValueError('Retained file entry requires a nonempty path')
        expected = row.get('retained_sha256', row.get('sha256'))
        if not isinstance(expected, str) or not re.fullmatch('[0-9a-fA-F]{64}', expected):
            raise ValueError('Retained file entry requires a SHA-256 digest: ' + locator)
        # Older portable records use ROOT_NAME/ without the ${...} wrapper.
        prefix, separator, suffix = locator.partition('/')
        named = re.match(r'^\$\{([A-Za-z_][A-Za-z0-9_]*)\}/', locator)
        if separator and prefix in roots:
            resolved = (roots[prefix] / suffix).resolve()
            boundary = roots[prefix].resolve()
        else:
            if Path(locator).is_absolute():
                raise ValueError('Stored artifact path requires a portable root: ' + locator)
            resolved = resolve_locator(locator, roots, package)
            boundary = roots[named.group(1)].resolve() if named else package
        if not resolved.is_relative_to(boundary):
            raise ValueError('Retained artifact escapes its declared root or package: ' + locator)
        if resolved in seen:
            if seen[resolved] != expected.lower():
                raise ValueError('Conflicting retained artifact hashes: ' + locator)
            duplicates.append({'index': index, 'path': locator,
                               'sha256': expected.lower()})
            continue
        seen[resolved] = expected.lower()
        observed = observe_file(resolved)
        if observed['sha256'].lower() != expected.lower():
            raise ValueError('Retained artifact hash mismatch: ' + locator)
        if resolved.suffix == '.json':
            json.loads(resolved.read_text(encoding='utf-8'))
        elif resolved.suffix == '.jsonl':
            for line in resolved.read_text(encoding='utf-8').splitlines():
                if line.strip():
                    json.loads(line)
        if resolved.suffix in {'.json', '.jsonl'} and observe_file(resolved) != observed:
            raise ValueError('Retained JSON changed during parsing: ' + locator)
        checked.append({'path': locator, 'sha256': observed['sha256'],
                        'bytes': observed['bytes'], 'result': 'PASS'})
    if not checked:
        raise ValueError('Manifest contains no retained artifacts to verify')
    if observe_file(manifest_path) != before:
        raise ValueError('Manifest changed during verification')
    relationships=verify_relationships(manifest.get('relationships',[]),manifest,roots,package)
    return portableize({'result': 'PASS', 'manifest': str(manifest_path),
                        'manifest_sha256': before['sha256'],
                        'verified_count': len(checked), 'files': checked,
                        'duplicate_attributions': duplicates,
                        'omitted_entries': omitted,'verified_relationships':relationships}, roots)


def verify_relationships(bindings,manifest,roots,package):
    """Verify JSON-pointer digest bindings between already registered artifacts."""
    entries={r.get('retained_path',r.get('path')):r.get('retained_sha256',r.get('sha256')) for r in manifest['files']}
    if not isinstance(bindings,list):raise ValueError('Relationship bindings must be a list')
    results=[]
    for binding in bindings:
        record=binding['record'];artifact=binding['artifact'];pointer=binding['field']
        if record not in entries or artifact not in entries or not isinstance(pointer,str) or not pointer.startswith('/'):
            raise ValueError('Relationship needs registered artifacts and a JSON pointer')
        prefix,_,suffix=record.partition('/')
        path=(roots[prefix]/suffix).resolve() if prefix in roots else resolve_locator(record,roots,package)
        before=observe_file(path)
        if before['sha256']!=entries[record]:raise ValueError('Relationship record changed')
        value=json.loads(path.read_text())
        for field in pointer[1:].split('/'):
            field=field.replace('~1','/').replace('~0','~')
            value=value[int(field)] if isinstance(value,list) else value[field]
        if value!=entries[artifact] or observe_file(path)!=before:raise ValueError('Artifact relationship hash mismatch')
        results.append(dict(record=record,artifact=artifact,field=pointer,result='PASS'))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--root', action='append', default=[], metavar='NAME=ABSOLUTE_PATH')
    args = parser.parse_args()
    roots = {}
    try:
        roots = parse_roots(args.root)
        result = verify_manifest(args.manifest, roots)
    except (OSError, ValueError) as error:
        print(json.dumps(portableize({'result': 'FAIL', 'error': str(error)}, roots)),
              file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
