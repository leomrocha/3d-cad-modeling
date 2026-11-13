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
import sys

try:
    from .part_index import read_json
except ImportError:
    from part_index import read_json


class RecordError(ValueError):
    pass


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


def readiness(job):
    for key in ('job_id', 'part_id', 'part_name', 'representation', 'units', 'frame'):
        if not job.get(key):
            raise RecordError('Missing job field: ' + key)
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


def require_ready(job):
    result = readiness(job)
    if result['state'] != 'SOURCE_READY':
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
    args = p.parse_args(argv)
    try:
        result = readiness(read_json(args.job))
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0 if result['state'] == 'SOURCE_READY' else 1
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
