#!/usr/bin/env python3
"""Source-readiness checks and append-only component action occurrences.

Data/output paths belong to the caller's component project. This module never
imports a CAD client, connects to a session or chooses a missing geometry value.
"""
import argparse
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys

try:
    from .part_index import read_json
except ImportError:
    from part_index import read_json


class RecordError(ValueError):
    pass


def resolve_source_locator(locator, root_map=None):
    """Resolve an absolute or explicitly rooted source path for validation."""
    if not isinstance(locator, str) or not locator.strip():
        raise RecordError('Source path must be a nonempty locator')
    roots = root_map or {}
    def replace(match):
        name = match.group(1)
        if name not in roots:
            raise RecordError('Missing configured path root: ' + name)
        root = Path(roots[name])
        if not root.is_absolute():
            raise RecordError('Configured path root must be absolute: ' + name)
        return str(root)
    value = re.sub(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}', replace, locator)
    if '${' in value:
        raise RecordError('Malformed source path root locator')
    path = Path(value)
    if not path.is_absolute():
        raise RecordError('Source path must be absolute or use an explicit named root')
    return path.resolve()


def validate_geometry_requirement(job, root_map=None):
    """Validate explicit non-geometric scope; return its observed source pin."""
    requirement = job.get('geometry_requirement')
    if requirement is None:
        return None
    if not isinstance(requirement, dict) or set(requirement) != {'kind', 'cad_required', 'source'}:
        raise RecordError('geometry_requirement must contain exactly kind, cad_required and source')
    if requirement.get('kind') != 'non_geometric_consumable':
        raise RecordError('Unsupported geometry_requirement kind')
    if requirement.get('cad_required') is not False:
        raise RecordError('non_geometric_consumable requires cad_required=false')
    if job.get('geometry_required') is True or job.get('geometry_role'):
        raise RecordError('Non-geometric classification conflicts with an explicit geometry declaration')
    source = requirement.get('source')
    if not isinstance(source, dict) or set(source) != {'path', 'sha256', 'location'}:
        raise RecordError('Non-geometric classification needs exact source path, sha256 and location')
    digest = source.get('sha256')
    if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-fA-F]{64}', digest):
        raise RecordError('Non-geometric source needs a SHA-256 digest')
    location = source.get('location')
    if not isinstance(location, str) or not location.strip():
        raise RecordError('Non-geometric source needs a readable location')
    path = resolve_source_locator(source.get('path'), root_map)
    observation = observe_file(path)
    if observation['sha256'].casefold() != digest.casefold():
        raise RecordError('Non-geometric source revision changed')
    return {'kind': requirement['kind'], 'cad_required': False,
            'source': {'sha256': digest.casefold(), 'location': location.strip(),
                       'bytes': observation['bytes']}}


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise RecordError('Finite numeric value required')
    return value


def observe_file(path):
    path = Path(path).resolve()
    before = path.stat()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    after = path.stat()
    fields = ('st_dev', 'st_ino', 'st_size', 'st_mtime_ns', 'st_ctime_ns')
    if any(getattr(before, k) != getattr(after, k) for k in fields):
        raise RecordError('Source changed during capture: ' + str(path))
    return {'path': str(path), 'sha256': digest.hexdigest(), 'bytes': after.st_size}


def readiness(job, root_map=None):
    for key in ('job_id', 'part_id', 'part_name', 'representation', 'units', 'frame'):
        if not job.get(key):
            raise RecordError('Missing job field: ' + key)
    geometry_requirement = validate_geometry_requirement(job, root_map)
    if geometry_requirement is not None:
        return {'job_id': job['job_id'], 'part_id': job['part_id'],
                'part_name': job['part_name'], 'state': 'SOURCE_READY_NON_GEOMETRIC',
                'questions': [], 'source_observations': [],
                'geometry_requirement': geometry_requirement,
                'meaning': 'Pinned source explicitly classifies this task as requiring no CAD geometry.'}
    if not isinstance(job.get('features'), list) or not job['features']:
        raise RecordError('Nonempty feature requirements are required')
    if not any(f.get('required') is True for f in job['features'] if isinstance(f, dict)):
        raise RecordError('At least one required feature is needed')
    seen, observations, questions = set(), [], []
    for feature in job['features']:
        if not isinstance(feature, dict):
            raise RecordError('Feature records must be objects')
        name = feature.get('name')
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise RecordError('Unique readable feature names are required')
        seen.add(name)
        if type(feature.get('required')) is not bool:
            raise RecordError('Feature required flag must be explicit: ' + name)
        source = feature.get('source')
        expected_hash = feature.get('source_sha256')
        value = feature.get('value')
        if value is None:
            if feature['required']:
                question = feature.get('question')
                if not isinstance(question, str) or not question.strip():
                    raise RecordError('Required feature needs its exact input question: ' + name)
                questions.append({'feature': name, 'question': question})
            continue
        if not feature.get('unit') or not feature.get('evidence_status') or not feature.get('source_location'):
            raise RecordError('Value needs units, source location and evidence status: ' + name)
        if isinstance(value, (float, int)):
            finite(value)
        if not source or not expected_hash:
            raise RecordError('Supplied value needs a source file and expected digest: ' + name)
        obs = observe_file(source)
        if obs['sha256'] != expected_hash:
            raise RecordError('Source revision changed for ' + name)
        observations.append({'feature': name, **obs})
    return {'job_id': job['job_id'], 'part_id': job['part_id'],
            'part_name': job['part_name'], 'state': 'NEEDS_INPUT' if questions else 'SOURCE_READY',
            'questions': questions, 'source_observations': observations,
            'meaning': 'Required input coverage and source revision checks; geometry construction and measurement have separate results.'}


def require_ready(job, root_map=None):
    result = readiness(job, root_map)
    if result['state'] != 'SOURCE_READY':
        if result['state'] == 'SOURCE_READY_NON_GEOMETRIC':
            raise RecordError('CAD geometry is not required for this source-bound job; CAD construction is prohibited')
        raise RecordError('Input required: ' + '; '.join(x['question'] for x in result['questions']))
    return result


REQUIRED_ACTION_FIELDS = ('occurrence_id', 'job_id', 'part_id', 'part_name', 'action_id',
                         'action_name', 'inputs', 'outputs', 'prerequisites', 'software',
                         'agent', 'representation', 'units', 'frame', 'preserved',
                         'changed_or_inferred', 'alternatives', 'downstream', 'checks',
                         'result', 'evidence')


def append_occurrence(path, occurrence):
    for field in REQUIRED_ACTION_FIELDS:
        if field not in occurrence or occurrence[field] is None or occurrence[field] == '':
            raise RecordError('Action occurrence needs ' + field)
    for field in ('occurrence_id','job_id','part_id','part_name','action_id','action_name','representation','units','frame','result'):
        if not isinstance(occurrence[field], str) or not occurrence[field].strip():
            raise RecordError('Readable nonempty string required for ' + field)
    if occurrence['result'] not in {'PASS', 'FAIL', 'NEEDS_INPUT', 'UNKNOWN'}:
        raise RecordError('Unknown occurrence result')
    # Check serialisability before opening or appending the journal.
    line = json.dumps(occurrence, ensure_ascii=False, allow_nan=False, sort_keys=True) + '\n'
    path = Path(path)
    with path.open('a+', encoding='utf-8') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        stream.seek(0)
        for old in stream:
            record = json.loads(old)
            if record['occurrence_id'] == occurrence['occurrence_id']:
                raise RecordError('Occurrence already recorded; use a new identity for a new result')
        stream.write(line)
        stream.flush()
        os.fsync(stream.fileno())
    return occurrence['occurrence_id']


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('job', type=Path)
    p.add_argument('--root', action='append', default=[], metavar='NAME=ABSOLUTE_PATH')
    args = p.parse_args(argv)
    try:
        roots = {}
        for entry in args.root:
            name, sep, path = entry.partition('=')
            if not sep or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', name) or not Path(path).is_absolute():
                raise RecordError('--root requires NAME=ABSOLUTE_PATH')
            if name in roots:
                raise RecordError('Duplicate configured path root: ' + name)
            roots[name] = path
        result = readiness(read_json(args.job), roots)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0 if result['state'] in {'SOURCE_READY', 'SOURCE_READY_NON_GEOMETRIC'} else 1
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
