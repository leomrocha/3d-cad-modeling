"""Durable caller-owned stage evidence and incremental native save checkpoints."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile

from .runtime import CadError, RecoveringClient
from .verification import require_audit, owned_audit
from .records import identity


def atomic_json(path,value):
    path=Path(path)
    data=json.dumps(value,indent=2,allow_nan=False)+'\n'
    fd,name=tempfile.mkstemp(prefix=path.name+'.',suffix='.tmp',dir=path.parent)
    try:
        with os.fdopen(fd,'w') as stream:
            stream.write(data);stream.flush();os.fsync(stream.fileno())
        os.replace(name,path)
        directory=os.open(path.parent,os.O_RDONLY)
        try:os.fsync(directory)
        finally:os.close(directory)
    finally:
        if os.path.exists(name):os.unlink(name)


def write_stage_checkpoint(path,job_id,stage,payload,*,order=('pre_save','save_reopen','reopened')):
    path=Path(path)
    if not isinstance(job_id,str) or not job_id or not order or len(set(order))!=len(order) or stage not in order:
        raise ValueError('Job identity and unique stage order required')
    # The caller owns this persistent lock file; it serializes checkpoint writers.
    with path.with_suffix(path.suffix+'.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        data=json.loads(path.read_text()) if path.exists() else dict(job_id=job_id,stages={})
        if data.get('job_id')!=job_id or not isinstance(data.get('stages'),dict):raise CadError('Checkpoint identity/schema differs')
        stages=data['stages']
        if list(stages)!=list(order[:len(stages)]) or len(stages)>=len(order) or order[len(stages)]!=stage:
            raise CadError('Checkpoint stages must form an unrepeated ordered prefix')
        stages[stage]=payload
        atomic_json(path,data)
    return data


def save_checkpoint(client,path,*,label,expected_counts,receipt_path=None,roots=None):
    """Save a new native DWG checkpoint without reopening or closing the live model."""
    path=Path(path)
    if receipt_path and not roots:raise CadError('Stored checkpoint receipt requires explicit caller roots')
    if not path.is_absolute() or path.suffix.lower()!='.dwg':raise CadError('Absolute native DWG checkpoint required')
    key=client.namespace+':'+label
    intent=client.journal.requests.get(key)
    if intent and (intent['request'].get('path')!=str(path) or intent['request']['op']!='save_verified'):
        raise CadError('Checkpoint intent differs')
    if path.exists() and not intent:raise CadError('Checkpoint already exists; retain it')
    state=client.read('state')
    if state.get('document_id')!=client.document_id or state.get('command') or state.get('modal') or state.get('operation'):
        raise CadError('Checkpoint requires idle owned document')
    baseline=identity(state)
    if intent and (intent['request'].get('geometry_revision')!=baseline[2]
                   or intent.get('context',{}).get('document_id')!=client.document_id):
        raise CadError('Checkpoint recovery belongs to another document or geometry epoch')
    audit=owned_audit(client)
    if identity(client.read('state'))!=baseline:raise CadError('Checkpoint epoch changed during audit')
    manifest=require_audit(audit)
    if manifest.get('by_type')!=expected_counts:raise CadError('Checkpoint entity counts differ')
    if intent:response=client.recover(key)
    else:response=RecoveringClient(client).mutate(label,'save_verified',path=str(path),target_format='dwg',target_version='2018',geometry_revision=state['geometry_revision'])
    saved=response.get('result',{})
    if not saved.get('verified') or saved.get('dropped_on_save')!=0 or saved.get('manifest')!=manifest:
        raise CadError('Checkpoint save verification failed')
    if saved.get('saved')!=str(path) or not path.is_file():raise CadError('Checkpoint path differs')
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest!=saved.get('sha256'):raise CadError('Checkpoint file hash differs')
    after=client.read('state')
    if after['document_id']!=client.document_id or after['geometry_revision']!=state['geometry_revision']:
        raise CadError('Geometry changed during checkpoint')
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise CadError('Checkpoint file changed before receipt')
    result=dict(result='PASS',state='IN_PROGRESS',saved_path=str(path),sha256=digest,
                document_id=client.document_id,geometry_revision=state['geometry_revision'],request_id=key,save=saved)
    if receipt_path:
        from envelope_job_runner import portableize
        atomic_json(receipt_path,portableize(result,roots))
    return result
