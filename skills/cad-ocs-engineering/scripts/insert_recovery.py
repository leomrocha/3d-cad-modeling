"""Explicit native INSERT default contracts with durable same-request recovery.

Caller owns the document and a serialized writer interval. This module never
replays a prior insertion-point request, cancels commands or adopts documents.
"""
import hashlib
import json
import re
from decimal import Decimal,InvalidOperation
from cadtools.geometry import finite
from cadtools.records import identity
from cadtools.runtime import CadError,RecoveringClient

_PATTERNS={
    'xscale':r'Enter X scale factor\b.*<([^<>]+)>:\s*',
    'yscale':r'Enter Y scale factor\b.*<([^<>]+)>:\s*',
    'rotation':r'Specify rotation angle\b.*<([^<>]+)>:\s*',
}
_NEXT={'xscale':'yscale','yscale':'rotation','rotation':None}


def _phase(state):
    command=state.get('command') or {}
    if command.get('name') not in ('INSERT','-INSERT') or 'enter' not in command.get('accepts',[]):
        raise CadError('Expected INSERT prompt accepting Enter')
    matches=[(stage,re.fullmatch(pattern,command.get('prompt',''),re.I)) for stage,pattern in _PATTERNS.items()]
    hits=[(stage,match.group(1).strip()) for stage,match in matches if match]
    if len(hits)!=1:raise CadError('Unknown or ambiguous INSERT prompt')
    return hits[0]


def insert_default_contract(state,*,stage,planned_value,x_scale_receipt=None):
    """Verify a displayed numeric default or a same-epoch inherited X scale."""
    before=identity(state);finite(planned_value)
    if state.get('modal') or state.get('operation'):raise CadError('INSERT default requires no pending operation or modal')
    actual,token=_phase(state)
    if actual!=stage:raise CadError('INSERT prompt stage differs')
    if stage=='yscale' and token.casefold()=='use x scale factor':
        receipt=x_scale_receipt or {}
        if (receipt.get('result')!='PASS' or receipt.get('stage')!='xscale'
                or receipt.get('after_identity')!=list(before)):
            raise CadError('Inherited Y default requires same-document/epoch verified X scale')
        token=receipt['value']
    try:default=Decimal(str(token));planned=Decimal(str(planned_value))
    except InvalidOperation as error:raise CadError('Unrecognized INSERT default value') from error
    if not default.is_finite() or default!=planned:raise CadError('Displayed default differs from planned value')
    return dict(stage=stage,value=str(planned),before_identity=list(before),prompt=state['command']['prompt'],
                expected_next=_NEXT[stage],command_name=state['command']['name'],planned_value=planned_value,
                x_scale_receipt=({k:x_scale_receipt[k] for k in ('result','stage','after_identity','value')} if stage=='yscale' and x_scale_receipt else None))


def _same_state(client,state,contract):
    if identity(state)!=tuple(contract['before_identity']) or state['document_id']!=client.document_id:
        raise CadError('INSERT contract document/revision differs')
    if state.get('modal') or state.get('operation') or _phase(state)[0]!=contract['stage'] or state['command']['prompt']!=contract['prompt'] or state['command']['name']!=contract['command_name']:
        raise CadError('INSERT prompt changed before accepting default')


def accept_insert_default(client,label,contract,*,exclusive_interval=False,checkpoint=None):
    """Send one guarded Enter, or recover its original request after restart.

    Persist the supplied contract with the job. Rotation completion requires a
    checkpoint callback; callback failure stops caller construction immediately.
    """
    if exclusive_interval is not True:raise CadError('Serialized owned writer interval required')
    stage=contract['stage']
    if stage not in _NEXT or contract.get('expected_next')!=_NEXT[stage]:raise CadError('Invalid default-stage contract')
    if stage=='rotation' and not callable(checkpoint):raise CadError('Completed insertion requires a checkpoint callback')
    # Reconstruct the original displayed-default guard, including inherited Y
    # value already bound by the original contract. Reject malformed contracts.
    if len(contract.get('before_identity',[]))!=3 or contract['before_identity'][0]!=client.document_id:
        raise CadError('Owned INSERT contract required')
    key=client.namespace+':'+label
    payload=json.dumps(contract,sort_keys=True,separators=(',',':'),allow_nan=False)
    digest=hashlib.sha256(payload.encode()).hexdigest()
    events=[]
    if client.journal.path.exists():events=[json.loads(line) for line in client.journal.path.read_text().splitlines() if line.strip()]
    bound=[e for e in events if e.get('event')=='insert_default_contract' and e.get('request_id')==key]
    if bound and any(e.get('sha256')!=digest for e in bound):raise CadError('Original INSERT default contract differs')
    intent=client.journal.requests.get(key)
    if intent:
        request=intent['request']
        if (not bound or request.get('op')!='input' or request.get('kind')!='enter'
                or request.get('document_id')!=client.document_id or request.get('geometry_revision')!=contract['before_identity'][2]):
            raise CadError('Original INSERT input intent differs')
        response=client.recover(key,allow_wait=True)
    else:
        state=client.read('state');_same_state(client,state,contract)
        checked=insert_default_contract(state,stage=stage,planned_value=contract['planned_value'],x_scale_receipt=contract.get('x_scale_receipt'))
        if checked!=contract:raise CadError('INSERT default contract fails current prompt validation')
        if not bound:client.journal.append(dict(event='insert_default_contract',request_id=key,sha256=digest,contract=contract))
        _same_state(client,client.read('state'),contract)
        response=RecoveringClient(client).mutate(label,'input',kind='enter',allow_wait=True,geometry_revision=contract['before_identity'][2])
    after=client.read('state');epoch=identity(after)
    if epoch[0]!=client.document_id or after.get('modal') or after.get('operation'):raise CadError('INSERT completion document or operation differs')
    if _NEXT[stage] is None:
        if after.get('command') is not None:raise CadError('INSERT rotation did not finish the command')
        checkpoint('insert-completed')
    elif _phase(after)[0]!=_NEXT[stage]:raise CadError('INSERT did not advance to the expected next prompt')
    return dict(result='PASS',stage=stage,value=contract['value'],after_identity=list(epoch),request_id=key,response=response)


def verify_cancelled_insert(before,after,response,*,expected_request_id,
                            before_snapshots,after_snapshots):
    """Verify one recorded cancellation; send no request and grant no permission.

    Caller supplies complete root, Insert and block snapshots after resolving
    earlier requests. Snapshot equality covers only the supplied collections.
    Save the recovered idle document before constructing another occurrence.
    """
    if not expected_request_id or response.get('request_id')!=expected_request_id:
        raise CadError('Exact original cancellation request identity required')
    if response.get('ok') is not True or response.get('status')!='cancelled':
        raise CadError('Successful terminal cancelled response required')
    original=identity(before)
    if identity(after)!=original or identity(response.get('state',{}))!=original:
        raise CadError('Cancellation changed document or geometry epoch')
    if before.get('session_id') is not None and any(s.get('session_id')!=before['session_id'] for s in (after,response.get('state',{}))):
        raise CadError('Cancellation native session differs')
    if (before.get('command') or {}).get('name') not in ('INSERT','-INSERT') or before.get('operation') or before.get('modal'):
        raise CadError('Inspected pending INSERT with no active operation required')
    if after.get('command') or after.get('operation') or after.get('modal'):
        raise CadError('Cancellation did not reach an idle document')
    if set(before_snapshots)!={'roots','inserts','blocks'} or set(after_snapshots)!=set(before_snapshots):
        raise CadError('Complete caller root, Insert and block collections required')
    def indexed(rows):
        out={}
        for row in rows:
            handle=row.get('handle')
            if not isinstance(handle,str) or not handle or handle in out:raise CadError('Unique snapshot handles required')
            out[handle]=row
        return out
    for name in before_snapshots:
        old,new=indexed(before_snapshots[name]),indexed(after_snapshots[name])
        if not old or old!=new:raise CadError('Cancellation changed supplied '+name+' records')
    if not set(indexed(before_snapshots['roots']))<=set(indexed(before_snapshots['inserts'])):
        raise CadError('Pending INSERT snapshot roots must be preserved Insert records')
    return dict(result='PASS',request_id=expected_request_id,document_id=original[0],
                geometry_revision=original[2],scope='unchanged supplied root, Insert and block record sets; idle state',
                next_action='Save verified idle checkpoint before further construction')
