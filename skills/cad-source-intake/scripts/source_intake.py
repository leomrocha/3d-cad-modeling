#!/usr/bin/env python3
"""Record immutable local source/scope revisions using existing observation code.

No network or CAD connection. Each explicit output directory is reserved once.
Success publishes its revision subdirectory atomically; failed observations keep
an incomplete directory and a failure receipt. Earlier revisions are read-only.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from urllib.parse import urlsplit

from component_records import observe_file, RecordError
from part_index import parse_json, read_json


class SourceConflict(ValueError):
    pass


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Nonempty text required: ' + label)
    return value


def dump(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False,
                                    allow_nan=False)+'\n', encoding='utf-8')


def validate(spec):
    if not isinstance(spec, dict):
        raise ValueError('Input must be an object')
    # Also rejects finite JSON syntax whose exponent overflows float parsing.
    json.dumps(spec, allow_nan=False)
    for key in ['job_name', 'revision_id', 'model']:
        text(spec.get(key), key)
    for key in ['text', 'location']:
        text(spec.get('request', {}).get(key), 'request.'+key)
    scope=spec.get('scope', {})
    for key in ['statement', 'requested_output']:
        text(scope.get(key), 'scope.'+key)
    paths=scope.get('authorized_paths')
    if not isinstance(paths, list) or not paths or any(not isinstance(p,str) or not Path(p).is_absolute() for p in paths):
        raise ValueError('scope.authorized_paths must contain absolute paths')
    sources=spec.get('sources')
    if not isinstance(sources, list) or not sources:
        raise ValueError('Nonempty sources required')
    ids=set()
    for s in sources:
        if not isinstance(s,dict):raise ValueError('Source must be an object')
        for key in ['id','title','summary','kind','locator','observed_at']:
            text(s.get(key), 'source.'+key)
        if s['id'] in ids:raise ValueError('Duplicate source ID: '+s['id'])
        ids.add(s['id'])
        datetime.fromisoformat(s['observed_at'].replace('Z','+00:00'))
        if s['kind']=='file':
            if not Path(s['locator']).is_absolute():raise ValueError('File source locator must be absolute')
        elif s['kind']=='text':
            if not isinstance(s.get('text'),str):raise ValueError('Exact text field required')
        elif s['kind']=='url':
            u=urlsplit(s['locator'])
            if u.scheme not in ['http','https'] or not u.hostname:raise ValueError('HTTP(S) URL locator required')
        else:raise ValueError('Unsupported source kind: '+s['kind'])
        if 'expected_sha256' in s and (not isinstance(s['expected_sha256'],str) or len(s['expected_sha256'])!=64 or any(c not in '0123456789abcdef' for c in s['expected_sha256'])):
            raise ValueError('Lowercase SHA-256 required')
    parents={s['id']:s.get('parent_id') for s in sources}
    for sid,parent in parents.items():
        chain={sid}
        while parent is not None:
            if parent not in ids:raise ValueError('Unknown parent source: '+str(parent))
            if parent in chain:raise ValueError('Source parent cycle: '+sid)
            chain.add(parent);parent=parents[parent]
    correction_ids=set()
    for c in spec.get('corrections',[]):
        for key in ['id','source_id','statement','location']:text(c.get(key),'correction.'+key)
        if c['id'] in correction_ids:raise ValueError('Duplicate correction ID: '+c['id'])
        correction_ids.add(c['id'])
        if c['source_id'] not in ids:raise ValueError('Unknown correction source: '+c['source_id'])
    for c in spec.get('conflicts',[]):
        text(c.get('summary'),'conflict.summary');text(c.get('affected_scope'),'conflict.affected_scope')
        if not isinstance(c.get('source_ids'),list) or len(set(c['source_ids']))<2 or not set(c['source_ids'])<=ids:
            raise ValueError('Conflict must reference at least two known sources')
    return spec


def verify_revision(path):
    """Verify published artifacts before consuming an explicit prior revision."""
    path=Path(path).resolve()
    receipt=read_json(path.parent/'receipt.json')
    if receipt.get('state')!='COMPLETE':raise ValueError('Prior intake must be complete')
    for name in ['source-index.json','scope.md']:
        if digest((path.parent/name).read_bytes())!=receipt['artifacts'][name]['sha256']:
            raise ValueError('Prior intake artifact changed: '+name)
    if path.name!='source-index.json':raise ValueError('Prior revision must identify source-index.json')
    return read_json(path)


def capture(spec):
    prior=None
    if spec.get('prior_revision'):
        prior=verify_revision(spec['prior_revision'])
        if prior['revision_id']==spec['revision_id']:raise ValueError('New revision ID required')
        if prior['job_name']!=spec['job_name']:raise ValueError('Prior job identity differs')
    previous={s['id']:s for s in prior['sources']} if prior else {}
    rows=[]
    for source in spec['sources']:
        row=dict(source)
        try:
            if source['kind']=='file':
                obs=observe_file(source['locator'])
                row['observation']={'state':'local_file_observed',**obs}
            elif source['kind']=='text':
                raw=source['text'].encode('utf-8')
                row['observation']={'state':'supplied_text_retained','sha256':digest(raw),'bytes':len(raw)}
            else:
                row['observation']={'state':'registered_url_reference','network_requests':0}
            expected=source.get('expected_sha256')
            if expected and row['observation'].get('sha256')!=expected:
                raise SourceConflict('Pinned source bytes changed: '+source['id'])
        except (OSError,RecordError) as error:
            raise SourceConflict('Source '+source['id']+': '+str(error)) from error
        if source['id'] in previous:
            old=previous[source['id']]
            row['previous_observation']=old['observation']
            row['content_changed']=old['observation'].get('sha256')!=row['observation'].get('sha256')
            row['locator_changed']=old['locator']!=source['locator']
        rows.append(row)
    return {'format_version':1,'job_name':spec['job_name'],'revision_id':spec['revision_id'],
            'request':spec['request'],'request_sha256':digest(spec['request']['text'].encode('utf-8')),
            'scope':spec['scope'],'sources':rows,'corrections':spec.get('corrections',[]),
            'conflicts':spec.get('conflicts',[]),'prior_revision':spec.get('prior_revision'),
            'prior_index_sha256':digest(Path(spec['prior_revision']).read_bytes()) if prior else None,
            'scope_path':'scope.md'}


def scope_markdown(index):
    def block(s):
        fence='`'*(max([len(v) for v in __import__('re').findall(r'`+',s)]+[2])+1)
        return fence+'text\n'+s+'\n'+fence+'\n'
    return ('# '+index['job_name']+'\n\nRevision: '+index['revision_id']+'\n\n'
            '## Exact request\n\n'+block(index['request']['text'])+'\n'
            'Source location: '+index['request']['location']+'\n\n'
            '## Recorded scope\n\n'+block(index['scope']['statement'])+'\n'
            'Requested output: '+index['scope']['requested_output']+'\n\n'
            'Authorized paths:\n\n'+''.join(str(i)+'. '+p+'\n' for i,p in enumerate(index['scope']['authorized_paths'],1))+'\n'
            'Source observations, corrections and conflicts: source-index.json\n')


def run(input_path, output):
    started=time.perf_counter();input_path=Path(input_path).resolve();output=Path(output).absolute()
    before=observe_file(input_path);raw=input_path.read_bytes();spec=validate(parse_json(raw.decode('utf-8')))
    if digest(raw)!=before['sha256'] or observe_file(input_path)['sha256']!=before['sha256']:
        raise SourceConflict('Input changed during capture')
    # Exclusive reservation protects completed and incomplete attempts alike.
    output.mkdir(mode=0o700,parents=False,exist_ok=False)
    stage=output/'incomplete';stage.mkdir()
    try:
        index=capture(spec)
        dump(stage/'source-index.json',index)
        (stage/'scope.md').write_text(scope_markdown(index),encoding='utf-8')
        artifacts={name:observe_file(stage/name) for name in ['source-index.json','scope.md']}
        for obs in artifacts.values():obs.pop('path')
        receipt={'state':'COMPLETE','revision_id':spec['revision_id'],'model':spec['model'],
                 'input':before,'artifacts':artifacts,'python':sys.version.split()[0],
                 'tool_sha256':digest(Path(__file__).read_bytes()),
                 'completed_at':datetime.now(timezone.utc).isoformat(),
                 'elapsed_seconds':time.perf_counter()-started,'network_requests':0}
        dump(stage/'receipt.json',receipt)
        # Validate the staged output set before its atomic publication.
        verify_revision(stage/'source-index.json')
        os.rename(stage,output/'revision')
        return {'state':'COMPLETE','revision':str(output/'revision'),
                'source_count':len(index['sources']),'elapsed_seconds':receipt['elapsed_seconds']}
    except Exception as error:
        dump(output/'failure.json',{'state':'FAILED','exception':type(error).__name__,
                                   'error':str(error),'input':before,
                                   'incomplete_directory':str(stage)})
        raise


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    args=p.parse_args(argv)
    try:
        print(json.dumps(run(args.input,args.output),ensure_ascii=False));return 0
    except (SourceConflict,RecordError) as error:
        print(json.dumps({'state':'FAILED','error':str(error)}));return 1
    except (OSError,ValueError,KeyError,TypeError) as error:
        print(json.dumps({'state':'FAILED','error':str(error)}));return 2


if __name__=='__main__':sys.exit(main())
