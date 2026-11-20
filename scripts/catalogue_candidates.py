"""Resolve hits from the CAD Models search CLI to assets in named local snapshots."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def lookup(search_cli, data, query, *, include_record=None, interpreter=sys.executable):
    """Read one standard CAD Models snapshot. Return candidates for identity review."""
    index = data / 'catalogue.sqlite'
    catalogue = data / 'catalogue.json'
    index_hash = digest(index)
    raw = catalogue.read_bytes()
    rows = json.loads(raw)
    records = {row['id']: row for row in rows}
    if len(records) != len(rows):
        raise ValueError('Duplicate catalogue record ID')
    output = subprocess.run([str(interpreter), str(search_cli), '--data', str(data),
                             '--limit', '1000', '--', query], check=True,
                            capture_output=True, text=True)
    hits = json.loads(output.stdout)
    selected = {}
    for hit in hits:
        row = records[hit['id']]
        if any(row.get(key) != hit.get(key) for key in ('name', 'dimensions', 'standards')):
            raise ValueError('Index and asset record disagree: ' + hit['id'])
        selected[row['id']] = hit['exact']
    if include_record is not None:
        for row in rows:
            if row['id'] not in selected and include_record(row):
                selected[row['id']] = False

    candidates = []
    root = (data / 'packages').resolve()
    for identifier, exact in selected.items():
        row = records[identifier]
        item = dict(id=row['id'], name=row['name'], exact_search_hit=exact,
                    dimensions=row.get('dimensions'), standards=row.get('standards'))
        for key in ('manufacturer', 'family', 'base', 'designation', 'part_number',
                    'closure', 'sides', 'evidence', 'designation_evidence'):
            if key in row:
                item[key] = row[key]
        if isinstance(row.get('variant'), dict):
            item['variant'] = row['variant']
        locator = row.get('file')
        if locator:
            path = (root / locator).resolve()
            if Path(locator).is_absolute() or not path.is_relative_to(root):
                raise ValueError('Asset outside package root: ' + str(locator))
            item['file'] = 'packages/' + locator
            if path.is_file() and path.stat().st_size:
                item['sha256'] = digest(path)
        origin = row.get('private_source')
        if origin is not None:
            if not item.get('sha256') or item['sha256'] != origin['sha256']:
                raise ValueError('Private asset differs from snapshot: ' + row['id'])
            item['private_source'] = origin
        candidates.append(item)
    catalogue_hash = hashlib.sha256(raw).hexdigest()
    if index_hash != digest(index) or catalogue_hash != digest(catalogue):
        raise ValueError('Catalogue changed during lookup')
    return dict(index_sha256=index_hash, catalogue_sha256=catalogue_hash,
                reached_search_limit=len(hits) == 1000, candidates=candidates)


def variant_check(candidate, requirements):
    """Compare exact job-supplied variant fields to the private source evidence."""
    source = candidate.get("private_source") or {}
    fields = source.get("variant") or {}
    evidence = source.get("evidence")
    mismatches = {key: fields[key] for key, value in requirements.items()
                  if key in fields and fields[key] != value}
    missing = [key for key in requirements if key not in fields or fields[key] is None]
    if mismatches:
        status = "different-variant"
    elif not requirements or missing or not evidence:
        status = "needs-evidence"
    else:
        status = "fields-match"
    return dict(status=status, required=requirements, mismatches=mismatches,
                missing=missing, evidence=evidence)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--search-cli', required=True, type=Path,
                        help='Trusted cad-models scripts/search.py')
    parser.add_argument('--source', nargs=2, action='append', required=True,
                        metavar=('NAME', 'DATA_DIRECTORY'))
    parser.add_argument('--variant', type=Path, help='JSON object of required variant fields and values')
    parser.add_argument('query')
    args = parser.parse_args()
    if not args.query.strip():
        parser.error('Supply a part identifier, designation or search term')
    required = json.loads(args.variant.read_text()) if args.variant else None
    if required is not None and (not isinstance(required, dict) or any(v is None for v in required.values())):
        parser.error("Supply named variant fields with known values")
    results = {}
    for name, directory in args.source:
        if name in results:
            parser.error('Duplicate source name: ' + name)
        try:
            results[name] = lookup(args.search_cli, Path(directory), args.query)
            if required is not None:
                for candidate in results[name]['candidates']:
                    candidate['variant_check'] = variant_check(candidate, required)
        except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
            results[name] = dict(error=str(error))
    print(json.dumps(dict(query=args.query, sources=results), indent=2))
    return int(any('error' in row for row in results.values()))


if __name__ == '__main__':
    sys.exit(main())
