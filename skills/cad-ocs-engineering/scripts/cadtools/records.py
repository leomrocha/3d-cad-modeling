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


def audit_type_counts(records):
    """Translate observed native entity labels to their audit manifest labels."""
    audit_labels = {'Solid3D': '3D Solid', 'Insert': 'Block Reference'}
    return dict(Counter(audit_labels.get(row['type'], row['type']) for row in records))
