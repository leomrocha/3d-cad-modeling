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


def lookup(search_cli, data, query):
    """Read one standard CAD Models snapshot. Return candidates for identity review."""
    index = data / 'catalogue.sqlite'
    catalogue = data / 'catalogue.json'
    index_hash = digest(index)
    raw = catalogue.read_bytes()
    rows = json.loads(raw)
    records = {row['id']: row for row in rows}
    if len(records) != len(rows):
        raise ValueError('Duplicate catalogue record ID')
    output = subprocess.run([sys.executable, str(search_cli), '--data', str(data),
                             '--limit', '1000', '--', query], check=True,
                            capture_output=True, text=True)
    hits = json.loads(output.stdout)
    candidates = []
    root = (data / 'packages').resolve()
    for hit in hits:
        row = records[hit['id']]
        if any(row.get(key) != hit.get(key) for key in ('name', 'dimensions', 'standards')):
            raise ValueError('Index and asset record disagree: ' + hit['id'])
        item = dict(id=row['id'], name=row['name'], exact_search_hit=hit['exact'],
                    dimensions=row.get('dimensions'), standards=row.get('standards'))
        locator = row.get('file')
        if locator:
            path = (root / locator).resolve()
            if Path(locator).is_absolute() or not path.is_relative_to(root):
                raise ValueError('Asset outside package root: ' + str(locator))
            item['file'] = 'packages/' + locator
            if path.is_file() and path.stat().st_size:
                item['sha256'] = digest(path)
        candidates.append(item)
    catalogue_hash = hashlib.sha256(raw).hexdigest()
    if index_hash != digest(index) or catalogue_hash != digest(catalogue):
        raise ValueError('Catalogue changed during lookup')
    return dict(index_sha256=index_hash, catalogue_sha256=catalogue_hash,
                reached_search_limit=len(hits) == 1000, candidates=candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--search-cli', required=True, type=Path,
                        help='Trusted cad-models scripts/search.py')
    parser.add_argument('--source', nargs=2, action='append', required=True,
                        metavar=('NAME', 'DATA_DIRECTORY'))
    parser.add_argument('query')
    args = parser.parse_args()
    if not args.query.strip():
        parser.error('Supply a part identifier, designation or search term')
    results = {}
    for name, directory in args.source:
        if name in results:
            parser.error('Duplicate source name: ' + name)
        try:
            results[name] = lookup(args.search_cli, Path(directory), args.query)
        except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
            results[name] = dict(error=str(error))
    print(json.dumps(dict(query=args.query, sources=results), indent=2))
    return int(any('error' in row for row in results.values()))


if __name__ == '__main__':
    sys.exit(main())
