"""Stable native record pagination and entity readback using a caller-bound client."""
from collections import Counter

from .runtime import CadError


def identity(state):
    keys=('document_id','revision','geometry_revision')
    if not state.get('ok') or any(type(state.get(k)) is not int for k in keys):
        raise CadError('Native state needs document and revision identities')
    return tuple(state[k] for k in keys)


def iter_records(client,collection,*,page_size=8,max_pages=100000,**filters):
    if type(page_size) is not int or page_size<1 or type(max_pages) is not int or max_pages<1:
        raise ValueError('Positive page and iteration bounds required')
    baseline=identity(client.read('state'))
    if baseline[0]!=client.document_id:raise CadError('Bound document is inactive')
    offset=0;limit=page_size;seen=set()
    for _ in range(max_pages):
        if identity(client.read('state'))!=baseline:raise CadError('Document changed during pagination')
        try:response=client.read('records',collection=collection,offset=offset,limit=limit,**filters)
        except Exception as error:
            if 'response exceeds 16 MiB' not in str(error) or limit==1:raise
            limit=max(1,limit//2)
            continue
        for k,v in zip(('document_id','revision','geometry_revision'),baseline):
            if k in response and response[k]!=v:raise CadError('Record page identity differs')
        if identity(client.read('state'))!=baseline:raise CadError('Document changed during page read')
        rows=response.get('records')
        if not isinstance(rows,list) or len(rows)>limit:raise CadError('Malformed record page')
        for row in rows:
            key=row.get('handle',row.get('name'))
            if key is None or key in seen:raise CadError('Missing or duplicate record identity')
            seen.add(key)
            yield row
        next_offset=response.get('next_offset')
        if next_offset is None:return
        if type(next_offset) is not int or next_offset<=offset or not rows:raise CadError('Nonprogressing record offset')
        offset=next_offset
    raise CadError('Record page bound reached')


def read_stable_entity(client,handle):
    before=identity(client.read('state'))
    if before[0]!=client.document_id:raise CadError('Bound document is inactive')
    response=client.read('records',collection='entities',handles=[handle],limit=1)
    rows=response.get('records',[])
    if len(rows)!=1 or rows[0].get('handle')!=handle:raise CadError('Exact native handle required')
    for source in (response,rows[0]):
        for key,value in zip(('document_id','revision','geometry_revision'),before):
            if key in source and source[key]!=value:raise CadError('Native record identity differs')
    if identity(client.read('state'))!=before:raise CadError('Document changed during entity read')
    return rows[0],dict(zip(('document_id','revision','geometry_revision'),before))


def motion_role_handles(roles, *, moving, stationary):
    """Resolve an exhaustive, non-overlapping native motion partition.

    The caller binds each in-scope physical role to one current live handle.
    Moving and stationary roles must come from the mechanism's design.
    The moving order is retained for the native request.
    """
    moving = tuple(moving)
    stationary = tuple(stationary)
    classified = moving + stationary
    if not moving or len(classified) != len(set(classified)):
        raise CadError('Motion roles require a nonempty moving group and unique classification')
    missing = sorted(set(roles) - set(classified))
    unexpected = sorted(set(classified) - set(roles))
    if missing or unexpected:
        raise CadError(f'Motion role coverage differs. Unclassified: {missing}. Unknown: {unexpected}.')
    handles = list(roles.values())
    if any(not isinstance(handle, str) or not handle for handle in handles) or len(set(handles)) != len(handles):
        raise CadError('Each motion role requires a unique native handle')
    return tuple(roles[role] for role in moving)


def audit_type_counts(records):
    """Translate observed native entity labels to their audit manifest labels."""
    audit_labels = {'Solid3D': '3D Solid', 'Insert': 'Block Reference'}
    return dict(Counter(audit_labels.get(row['type'], row['type']) for row in records))


def model_space_live_handles(model_space, entity_records, expected_handles, *, document_id,
                             erase_intent, erase_response):
    """Separate proven erased references from a complete current model-space inventory."""
    if (type(document_id) is not int or document_id < 1
            or erase_intent.get('op') != 'entities_delete'
            or erase_intent.get('document_id') != document_id
            or not erase_intent.get('request_id')
            or erase_intent.get('request_id') != erase_response.get('request_id')
            or erase_response.get('ok') is not True
            or erase_response.get('status') != 'completed'):
        raise CadError('Completed same-request deletion for the owned document required')
    erased = erase_intent.get('handles')
    if (not isinstance(erased, list) or not erased
            or erase_response.get('result', {}).get('erased') != len(erased)):
        raise CadError('Explicit fully erased handle inventory required')

    return _reconcile_model_space(model_space, entity_records, expected_handles, erased)


def model_space_after_revolve(model_space, entity_records, expected_handles, *, document_id,
                              profile_handle, solid_handle, revolve_intent, revolve_response):
    """Resolve a consumed profile using the completed native REVOLVE change list."""
    consumed = consumed_profile_transition(document_id=document_id, command='REVOLVE',
        profile_handle=profile_handle, solid_handle=solid_handle, intent=revolve_intent,
        response=revolve_response)
    rows = list(entity_records)
    if not any(r.get('handle') == solid_handle and r.get('type') == 'Solid3D' for r in rows):
        raise CadError('Expected generated solid in live inventory')
    return _reconcile_model_space(model_space, rows, expected_handles, [consumed['profile_handle']])


def consumed_profile_transition(*, document_id, command, profile_handle, solid_handle, intent, response):
    """Identify the removed profile and added solid in an owned command receipt."""
    request_id = intent.get('request_id')
    tokens = intent.get('cmd', '').split()
    if (command not in ('EXTRUDE','REVOLVE') or type(document_id) is not int or document_id < 1
            or not isinstance(profile_handle,str) or not profile_handle
            or not isinstance(solid_handle,str) or not solid_handle or profile_handle == solid_handle
            or intent.get('op') != 'run' or tokens[:1] != [command]
            or intent.get('document_id') != document_id
            or response.get('state', {}).get('document_id') != document_id
            or not request_id or request_id != response.get('request_id')
            or response.get('ok') is not True
            or response.get('status') != 'completed'):
        raise CadError('Completed same-request profile construction for the owned document required')
    changes = response.get('changes')
    if (not isinstance(changes, list) or len(changes) != 2
            or not all(isinstance(change, dict) for change in changes)
            or not any(change.get('kind') == 'Removed' and change.get('handle') == profile_handle
                       for change in changes)
            or not any(change.get('kind') == 'Added' and change.get('handle') == solid_handle
                       for change in changes)):
        raise CadError('Expected one consumed profile and one new solid in profile construction changes')
    return dict(request_id=request_id, profile_handle=profile_handle, solid_handle=solid_handle)


def _reconcile_model_space(model_space, entity_records, expected_handles, erased):
    if model_space.get('name') != '*Model_Space':
        raise CadError('Exact Model Space block record required')

    def unique_handles(values):
        handles = []
        for value in values:
            if type(value) is int and value > 0:
                value = format(value, 'X')
            if not isinstance(value, str) or not value:
                raise CadError('Nonempty native handle required')
            handles.append(value)
        if len(handles) != len(set(handles)):
            raise CadError('Duplicate handle in native inventory')
        return handles

    references = unique_handles(model_space['properties']['entity_handles'])
    expected = set(unique_handles(expected_handles))
    inventory = set(unique_handles(row['handle'] for row in entity_records))
    erased_handles = set(unique_handles(erased))
    retired_refs = set(references) - inventory
    live = [handle for handle in references if handle in inventory]
    if inventory & erased_handles or retired_refs - erased_handles or set(live) != expected:
        raise CadError('Unexpected, unresolved or missing Model Space handle')
    return dict(live_handles=live, erased_references=sorted(retired_refs))
