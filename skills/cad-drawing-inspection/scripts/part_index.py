#!/usr/bin/env python3
"""Read and search an external project's existing parts index/dictionary."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


class IndexError(ValueError):
    pass


def _unique(items):
    result = {}
    for key, value in items:
        if key in result:
            raise IndexError('Duplicate JSON key: ' + key)
        result[key] = value
    return result


def parse_json(text):
    def reject(token):
        raise IndexError('Nonfinite JSON number: ' + token)
    return json.loads(text, object_pairs_hook=_unique, parse_constant=reject)


def read_json(path):
    return parse_json(Path(path).read_text(encoding='utf-8'))


def load_index(path):
    """Return original rows plus their source identity, without merging namespaces."""
    path = Path(path).resolve()
    raw = path.read_bytes()
    data = parse_json(raw.decode('utf-8'))
    if isinstance(data, list):
        rows, kind = data, 'component_input'
    elif isinstance(data, dict) and isinstance(data.get('entries'), list):
        rows, kind = data['entries'], 'dictionary_entry'
    else:
        raise IndexError('Expected a component list or dictionary entries')
    seen, result = set(), []
    for row in rows:
        if not isinstance(row, dict):
            raise IndexError('Part records must be objects')
        identifier, name = row.get('id'), row.get('name')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            raise IndexError('Unique nonempty part IDs are required within each index')
        if not isinstance(name, str) or not name.strip():
            raise IndexError('Readable part name is required: ' + identifier)
        seen.add(identifier)
        result.append({'id': identifier, 'name': name, 'record_kind': kind,
                       'index': str(path), 'index_sha256': hashlib.sha256(raw).hexdigest(),
                       'record': row})
    return result


def search(paths, query='', identifier=None):
    terms = query.casefold().split()
    results = []
    for path in paths:
        for row in load_index(path):
            if identifier is not None and row['id'] != identifier:
                continue
            # Values retain their explicit source namespace and formal/standard data.
            haystack = json.dumps(row['record'], ensure_ascii=False).casefold()
            if all(term in haystack for term in terms):
                results.append(row)
    return results


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index', action='append', required=True, type=Path)
    p.add_argument('--query', default='')
    p.add_argument('--id')
    args = p.parse_args(argv)
    try:
        rows = search(args.index, args.query, args.id)
        print(json.dumps({'matches': rows, 'count': len(rows)}, indent=2,
                         ensure_ascii=False, allow_nan=False))
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
