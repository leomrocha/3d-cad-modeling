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
from envelope_job_runner import portableize
from job_paths import NAME, add_job_sources, parse_roots, rooted_path, selected_roots


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


def verify_revision_package(current, replacement, assets, *, model_name, old_sha256,
                            new_sha256):
    """Bind a geometry revision to the existing package and unchanged asset names."""
    names = list(assets)
    if (not names or any(not isinstance(name, str) or not name or
                         name in {'.', '..'} or '/' in name or '\\' in name for name in names)
            or len(set(names)) != len(names) or model_name not in names):
        raise ValueError('Expected unique sibling asset names including the model')
    current, replacement = Path(current), Path(replacement)
    if current.resolve() == replacement.resolve():
        raise ValueError('Stage the replacement in a separate package')
    inventories = []
    for root in (current, replacement):
        entries = {path.name: path for path in root.iterdir()}
        if entries.keys() != set(names) or any(
                path.is_symlink() or not path.is_file() for path in entries.values()):
            raise ValueError('Package inventory differs from the reviewed asset names')
        inventories.append({name: observe_file(entries[name])['sha256'] for name in sorted(names)})
    before, after = inventories
    if before[model_name] != old_sha256 or after[model_name] != new_sha256:
        raise ValueError('Native model hash differs from the reviewed revision')
    if old_sha256 == new_sha256:
        raise ValueError('Geometry revision requires a different native file hash')
    return dict(result='PASS', current_sha256=before, replacement_sha256=after)


def verify_gallery_capture(packages, record, *, view, checkpoint, capture):
    """Resolve one local catalogue preview and compare native model and image bytes."""
    if checkpoint.get('result') != 'PASS' or capture.get('result') != 'PASS':
        raise ValueError('A successful model checkpoint and viewport capture are required')
    for key in ('document_id', 'geometry_revision'):
        if type(checkpoint.get(key)) is not int or checkpoint[key] != capture.get(key):
            raise ValueError('Capture and saved model identities differ')
    if checkpoint.get('session_id') != capture.get('session_id'):
        raise ValueError('Checkpoint and capture sessions differ')
    if not isinstance(view, str) or not view.strip():
        raise ValueError('Select a named native viewport')
    matches = [p for p in record['previews'] if p['view'] == view]
    if len(matches) != 1:
        raise ValueError('Expected one gallery entry for the selected viewport')
    root = Path(packages).resolve()
    for locator, expected in ((record['file'], checkpoint['sha256']),
                              (matches[0]['file'], capture['sha256'])):
        path = (root / locator).resolve()
        if Path(locator).is_absolute() or not path.is_relative_to(root):
            raise ValueError('Expected an asset inside the packages directory')
        if observe_file(path)['sha256'] != expected:
            raise ValueError('Catalogue asset hash differs: ' + locator)
    return dict(result='PASS', record_id=record['id'], revision=record['revision'],
                model_sha256=checkpoint['sha256'], view=view, file=matches[0]['file'],
                image_sha256=capture['sha256'])


def artifact_path(locator, roots, package):
    # Historical manifests also stored named origins without the wrapper.
    prefix, separator, suffix = locator.partition('/')
    if separator and (prefix in roots or (NAME.fullmatch(prefix) and prefix.endswith('_ROOT'))):
        locator = '${' + prefix + '}/' + suffix
    if Path(locator).is_absolute():
        raise ValueError('Stored artifact path requires a portable origin: ' + locator)
    resolved = rooted_path(locator, roots, package)
    if not locator.startswith('${') and not resolved.is_relative_to(package):
        raise ValueError('Retained artifact escapes its package: ' + locator)
    return resolved


def verify_manifest(manifest_path, roots=None):
    manifest_path = Path(manifest_path).resolve()
    package = manifest_path.parent
    roots = selected_roots(roots, evidence=package)
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
        resolved = artifact_path(locator, roots, package)
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
        path=artifact_path(record,roots,package)
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
    parser.add_argument('--job', type=Path, help='Selected job record for source locators')
    parser.add_argument('--project-root', type=Path)
    parser.add_argument('--output', type=Path, help='Selected saved model for output-relative locators')
    parser.add_argument('--root', action='append', default=[], help=argparse.SUPPRESS)
    args = parser.parse_args()
    roots = {}
    try:
        roots = selected_roots(parse_roots(args.root), job=args.job, project=args.project_root,
                               output=args.output)
        if args.job is not None:
            job = json.loads(args.job.read_text(encoding='utf-8'))
            if not isinstance(job, dict):
                raise ValueError('Selected job must be a JSON object')
            add_job_sources(roots, job, args.job.resolve().parent)
        result = verify_manifest(args.manifest, roots)
    except (OSError, ValueError) as error:
        print(json.dumps(portableize({'result': 'FAIL', 'error': str(error)}, roots)),
              file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
