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


def recover_idle_mutation(client, label, operation, *, fields):
    """Read back a journaled same-document mutation at its exact live idle revision."""
    key = client.namespace + ':' + label
    event = client.journal.requests.get(key, {})
    request = event.get('request', {})
    context = dict(session_id=client.descriptor['session_id'], document_id=client.document_id)
    envelope = {'op', 'request_id', 'document_id', 'revision'}
    if set(fields) & envelope:
        raise ValueError('Supply only the expected mutation operands')
    operands = {k: v for k, v in request.items() if k not in envelope}
    if (event.get('context') != context or request.get('op') != operation
            or request.get('request_id') != key or request.get('document_id') != client.document_id
            or type(request.get('revision')) is not int or operands != fields):
        raise CadError('Original mutation request does not match the recovery contract')
    result = client.recover(key)
    if result.get('ok') is not True or result.get('status') != 'completed' or result.get('request_id') != key:
        raise CadError('The original mutation has no completed receipt')
    completed = result.get('state', {})
    live = client.read('state')
    if (identity(completed) != identity(live) or live['document_id'] != client.document_id
            or live['revision'] < request['revision']
            or any(source.get(k) for source in (completed, live) for k in ('command', 'operation', 'modal'))):
        raise CadError('Recovered mutation no longer matches the idle owned document')
    return result


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


def save_checkpoint(client,path,*,label,expected_counts,receipt_path=None,roots=None,job_id=None,source_pins=(),handles=None,job_path=None):
    """Save a new native DWG checkpoint without reopening or closing the live model."""
    path=Path(path)
    if job_id is not None and (not isinstance(job_id,str) or not job_id):raise CadError('Readable checkpoint job identity required')
    if not path.is_absolute() or path.suffix.lower()!='.dwg':raise CadError('Absolute native DWG checkpoint required')
    from job_paths import selected_roots
    roots=selected_roots(roots, job=job_path, output=path,
                         evidence=Path(receipt_path).parent if receipt_path else None)
    pins=_check_source_pins(source_pins,roots,base=roots.get('JOB_ROOT'))
    if handles is not None and (not isinstance(handles,dict) or any(not isinstance(k,str) or not k or not isinstance(v,str) or not v for k,v in handles.items())):raise CadError('Named checkpoint handle mapping required')
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
    observed_counts = manifest.get('by_type')
    if observed_counts != expected_counts:
        raise CadError(f'Checkpoint entity counts differ: expected {expected_counts!r}, observed {observed_counts!r}')
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
    if _check_source_pins(pins,roots,base=roots.get('JOB_ROOT'))!=pins:raise CadError('Source contract changed during save')
    if job_id is not None:result['job_id']=job_id
    result['source_pins']=pins
    if handles is not None:result['handles']=dict(handles)
    if isinstance(state.get('session_id'),str):result['session_id']=state['session_id']
    if receipt_path:
        from envelope_job_runner import portableize
        atomic_json(receipt_path,portableize(result,roots))
    return result


def _checkpoint_locator(locator,roots,base=None):
    from component_records import resolve_source_locator
    try:
        return resolve_source_locator(locator,roots,base=base)
    except ValueError as error:
        raise CadError(str(error)) from error


def _source_pin_path(pin):
    import re
    if (not isinstance(pin,dict) or set(pin)!={'path','sha256'}
            or not isinstance(pin['path'],str) or not pin['path']
            or not re.fullmatch('[a-f0-9]{64}',str(pin['sha256']))):
        raise CadError('Source pins require exact path and SHA-256')
    return pin['path']


def merge_source_pins(*groups):
    """Combine identical source references before starting a native job.

    Supply one consistent locator spelling per file. File bytes and canonical
    paths are independently checked at the checkpoint.
    """
    merged={}
    for group in groups:
        for pin in group:
            path=_source_pin_path(pin)
            previous=merged.setdefault(path,dict(pin))
            if previous!=pin:
                raise CadError('Conflicting source revisions for '+path)
    return list(merged.values())


def _check_source_pins(pins,roots,base=None):
    from component_records import observe_file
    rows=[];seen=set()
    for pin in pins:
        path=_checkpoint_locator(_source_pin_path(pin),roots,base)
        if path in seen:raise CadError('Duplicate checkpoint source pin')
        seen.add(path)
        if observe_file(path)['sha256']!=pin['sha256']:raise CadError('Checkpoint source revision changed')
        rows.append(dict(pin))
    return rows


def verify_resume_checkpoint(checkpoint,*,job_id,source_pins,state,roots=None,
                             expected_handles=None,actual_handles=None,observed_handles=None,
                             job_path=None,receipt_path=None,output_path=None):
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
    from job_paths import selected_roots
    roots=selected_roots(roots, job=job_path, output=output_path,
                         evidence=Path(receipt_path).parent if receipt_path else None)
    pins=_check_source_pins(source_pins,roots,base=roots.get('JOB_ROOT'))
    if sorted(pins,key=lambda p:p['path'])!=sorted(checkpoint.get('source_pins',[]),key=lambda p:p['path']):
        raise CadError('Checkpoint source contract differs')
    from component_records import observe_file
    saved=_checkpoint_locator(checkpoint['saved_path'],roots)
    if observe_file(saved)['sha256']!=checkpoint.get('sha256'):raise CadError('Checkpoint saved bytes changed')
    if observed_handles is not None:
        if actual_handles is not None or not isinstance(expected_handles, dict):
            raise CadError('Raw live handles require the expected role mapping and no observed role mapping')
        if checkpoint.get('handles') != expected_handles:
            raise CadError('Checkpoint handle mapping differs')
        if not isinstance(observed_handles, (list, tuple)) or any(
            not isinstance(handle, str) or not handle for handle in observed_handles
        ):
            raise CadError('Live handles must be a sequence of nonempty strings')
        expected_values = tuple(expected_handles.values())
        if (any(not isinstance(handle, str) or not handle for handle in expected_values)
                or len(set(expected_values)) != len(expected_values)
                or len(observed_handles) != len(expected_values)
                or set(observed_handles) != set(expected_values)):
            raise CadError('Live handle inventory differs from the saved checkpoint')
    else:
        if (expected_handles is None) != (actual_handles is None):
            raise CadError('Supply both expected and actual handle mappings')
        if expected_handles is not None and (
            checkpoint.get('handles') != expected_handles or expected_handles != actual_handles
        ):
            raise CadError('Checkpoint handle mapping differs')
    return dict(result='PASS',state='RESUME_VERIFIED',job_id=job_id,document_id=epoch[0],geometry_revision=epoch[2],sha256=checkpoint['sha256'])



def verify_finish_checkpoint(checkpoint, *, job_id, source_pins, state, final_stage_request_id,
                             planned_roles, observed_handles, roots=None,
                             job_path=None,receipt_path=None,output_path=None):
    """Bind final verification to the intended completed construction checkpoint."""
    if not isinstance(final_stage_request_id, str) or not final_stage_request_id:
        raise CadError('Expected final construction save request required')
    if checkpoint.get('request_id') != final_stage_request_id:
        raise CadError('Checkpoint is not the expected final construction save')
    if (not isinstance(planned_roles, (list, tuple)) or not planned_roles
            or any(not isinstance(role, str) or not role for role in planned_roles)
            or len(set(planned_roles)) != len(planned_roles)):
        raise CadError('Unique planned occurrence roles required')
    saved_handles = checkpoint.get('handles')
    if not isinstance(saved_handles, dict) or set(saved_handles) != set(planned_roles):
        raise CadError('Final construction checkpoint does not cover the planned occurrence roles')
    verified = verify_resume_checkpoint(
        checkpoint, job_id=job_id, source_pins=source_pins, state=state, roots=roots,
        job_path=job_path, receipt_path=receipt_path, output_path=output_path,
        expected_handles=saved_handles, observed_handles=observed_handles,
    )
    return dict(verified, state='FINAL_VERIFICATION_PENDING',
                construction_save_request_id=final_stage_request_id, occurrence_count=len(planned_roles))
