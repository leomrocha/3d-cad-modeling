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


def save_checkpoint(client,path,*,label,expected_counts,receipt_path=None,roots=None,job_id=None,source_pins=(),handles=None):
    """Save a new native DWG checkpoint without reopening or closing the live model."""
    path=Path(path)
    if job_id is not None and (not isinstance(job_id,str) or not job_id):raise CadError('Readable checkpoint job identity required')
    pins=_check_source_pins(source_pins,roots)
    if handles is not None and (not isinstance(handles,dict) or any(not isinstance(k,str) or not k or not isinstance(v,str) or not v for k,v in handles.items())):raise CadError('Named checkpoint handle mapping required')
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
    audit=owned_audit(client, target_path=path)
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
    if _check_source_pins(pins,roots)!=pins:raise CadError('Source contract changed during save')
    if job_id is not None:result['job_id']=job_id
    result['source_pins']=pins
    if handles is not None:result['handles']=dict(handles)
    if isinstance(state.get('session_id'),str):result['session_id']=state['session_id']
    if receipt_path:
        from envelope_job_runner import portableize
        atomic_json(receipt_path,portableize(result,roots))
    return result


def _checkpoint_locator(locator,roots):
    from component_records import resolve_source_locator
    import re
    path=resolve_source_locator(locator,roots)
    if '${' in locator:
        match=re.fullmatch(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}/.+',locator)
        if not match or not path.is_relative_to(Path(roots[match.group(1)]).resolve()):
            raise CadError('Checkpoint locator escapes its declared root')
    return path


def _check_source_pins(pins,roots):
    from component_records import observe_file,resolve_source_locator
    import re
    rows=[];seen=set()
    for pin in pins:
        if not isinstance(pin,dict) or set(pin)!={'path','sha256'} or not re.fullmatch('[a-f0-9]{64}',str(pin.get('sha256',''))):
            raise CadError('Source pins require exact path and SHA-256')
        path=_checkpoint_locator(pin['path'],roots)
        if path in seen:raise CadError('Duplicate checkpoint source pin')
        seen.add(path)
        if observe_file(path)['sha256']!=pin['sha256']:raise CadError('Checkpoint source revision changed')
        rows.append(dict(pin))
    return rows


def verify_resume_checkpoint(checkpoint,*,job_id,source_pins,state,roots=None,
                             expected_handles=None,actual_handles=None):
    """Offline live-document resume gate; send no native request or mutation.

    This verifies a saved state and its current source contract. It does not infer
    completed recipe operations or replay unfinished commands. Caller reconciles
    action journal effects before constructing the next bounded operation.
    """
    if not isinstance(job_id,str) or not job_id or checkpoint.get('job_id')!=job_id:
        raise CadError('Checkpoint job identity differs')
    if checkpoint.get('result')!='PASS' or checkpoint.get('state')!='IN_PROGRESS':raise CadError('Verified in-progress checkpoint required')
    if state.get('command') or state.get('operation') or state.get('modal'):raise CadError('Resolve active/uncertain native command before resume')
    epoch=identity(state)
    if epoch[0]!=checkpoint.get('document_id') or epoch[2]!=checkpoint.get('geometry_revision'):
        raise CadError('Checkpoint document or geometry epoch differs')
    if checkpoint.get('session_id') is not None and state.get('session_id')!=checkpoint['session_id']:
        raise CadError('Checkpoint native session differs')
    pins=_check_source_pins(source_pins,roots)
    if sorted(pins,key=lambda p:p['path'])!=sorted(checkpoint.get('source_pins',[]),key=lambda p:p['path']):
        raise CadError('Checkpoint source contract differs')
    from component_records import observe_file,resolve_source_locator
    saved=_checkpoint_locator(checkpoint['saved_path'],roots)
    if observe_file(saved)['sha256']!=checkpoint.get('sha256'):raise CadError('Checkpoint saved bytes changed')
    if (expected_handles is None)!=(actual_handles is None):raise CadError('Supply both expected and actual handle mappings')
    if expected_handles is not None and (checkpoint.get('handles')!=expected_handles or expected_handles!=actual_handles):raise CadError('Checkpoint handle mapping differs')
    return dict(result='PASS',state='RESUME_VERIFIED',job_id=job_id,document_id=epoch[0],geometry_revision=epoch[2],sha256=checkpoint['sha256'])
