"""Source-attributed native component insertion with saved placement verification."""
import hashlib
from pathlib import Path
from cadtools.geometry import Geometry,added,vector
from cadtools.runtime import CadError
from cadtools.records import read_stable_entity
from source_metadata import compare_source_metadata
from step_placements import native_matrix,near,classify_hand


def insert_component(client,label,path,*,point=(0,0,0),yscale=1,source_locator):
    path=Path(path);vector(point)
    if yscale not in (-1,1) or isinstance(yscale,bool):raise ValueError('Unit placement or mirror required')
    if not path.is_file() or not isinstance(source_locator,str) or not source_locator:raise ValueError('Source model and portable locator required')
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    client.mutate(label+'-start','start',cmd='-INSERT',allow_wait=True)
    steps=[('file','block name',dict(kind='token',text=str(path))),('point','insertion point',dict(kind='point',point=list(point),space='wcs')),('xscale','X scale factor',dict(kind='token',text='1')),('yscale','Y scale factor',dict(kind='token',text=str(yscale))),('rotation','rotation angle',dict(kind='token',text='0'))]
    for suffix,prompt,fields in steps:
        state=client.read('state');command=state.get('command') or {}
        if state.get('document_id')!=client.document_id or prompt not in command.get('prompt','') or command.get('name') not in ('INSERT','-INSERT'):
            raise CadError('Insertion document/command/prompt differs')
        response=client.mutate(label+'-'+suffix,'input',allow_wait=suffix!='rotation',**fields)
    handle=added(response)
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise CadError('Source changed during insertion')
    lines=['Source model '+source_locator,'Source DWG SHA256 '+digest,'Placement mm '+str(list(point))+'; Y scale '+str(yscale)]
    Geometry(client).metadata(label+'-provenance',[handle],lines)
    row,_=read_stable_entity(client,handle)
    metadata=compare_source_metadata(row,handle,'CADTOOLS_SOURCE',lines)
    if metadata['result']!='PASS':raise CadError('Inserted source metadata differs')
    matrix=native_matrix(row['properties'],allow_unit_reflection=True)
    expected=[[1,0,0,point[0]],[0,yscale,0,point[1]],[0,0,1,point[2]],[0,0,0,1]]
    if not near(matrix,expected):raise CadError('Inserted placement differs')
    return dict(handle=handle,source=source_locator,source_sha256=digest,matrix=matrix,metadata=lines)


def verify_child_placements(client,children):
    result=[]
    for child in children:
        classify_hand(child['matrix'])
        row,identity=read_stable_entity(client,child['handle'])
        if row.get('type')!='Insert':raise CadError('Expected component insertion')
        matrix=native_matrix(row['properties'],allow_unit_reflection=True)
        metadata=compare_source_metadata(row,child['handle'],'CADTOOLS_SOURCE',child['metadata'])
        passed=near(matrix,child['matrix']) and metadata['result']=='PASS'
        result.append(dict(handle=child['handle'],result='PASS' if passed else 'FAIL',identity=identity,matrix=matrix))
    return dict(result='PASS' if result and all(c['result']=='PASS' for c in result) else 'FAIL',checks=result)


def correct_insert_point(client,label,handle,point,*,expected_matrix,schema_paths,
                         checkpoint,exclusive_interval=False,
                         translation_tolerance,linear_tolerance):
    """CAS only an observed Insert point, preserving all other placement fields.

    Caller inspected schema_paths and supplied a complete intended matrix. The
    exact owned document must be idle; checkpoint callbacks run before and after.
    """
    import copy
    from cadtools.geometry import finite
    from assembly_verification import _matrix
    if exclusive_interval is not True or not callable(checkpoint):raise CadError('Serialized writer interval and checkpoint callback required')
    if '/insert_point' not in schema_paths:raise CadError('Inspected schema must support /insert_point')
    point=vector(point);_matrix(expected_matrix)
    for value in (translation_tolerance,linear_tolerance):
        if finite(value)<=0:raise CadError('Positive placement tolerances required')
    state=client.read('state')
    if state.get('document_id')!=client.document_id or state.get('command') or state.get('operation') or state.get('modal'):
        raise CadError('Point correction requires idle owned document')
    before,identity=read_stable_entity(client,handle)
    if before.get('type')!='Insert':raise CadError('Exact native Insert required')
    old=before['properties']['insert_point'];desired=dict(zip('xyz',point))
    candidate=copy.deepcopy(before['properties']);candidate['insert_point']=desired
    matrix=native_matrix(candidate,allow_unit_reflection=True)
    if (any(abs(matrix[i][j]-expected_matrix[i][j])>linear_tolerance for i in range(3) for j in range(3))
            or any(abs(matrix[i][3]-expected_matrix[i][3])>translation_tolerance for i in range(3))):
        raise CadError('Point-only correction cannot produce intended complete placement')
    from cadtools.runtime import RecoveringClient
    key=client.namespace+':'+label
    intent=client.journal.requests.get(key)
    if intent:
        request=intent['request'];updates=request.get('updates',[])
        if (request.get('op')!='set_properties' or request.get('handle')!=handle
                or request.get('collection')!='entities' or len(updates)!=1
                or updates[0].get('path')!='/insert_point' or updates[0].get('value')!=desired):
            raise CadError('Original point-correction intent differs')
        response=client.recover(key)
    else:
        checkpoint('before-point-correction')
        # The expected-value update protects the observed property; document and
        # geometry epoch guards protect the rest of the placement.
        response=RecoveringClient(client).mutate(label,'set_properties',collection='entities',handle=handle,
            geometry_revision=identity['geometry_revision'],updates=[dict(path='/insert_point',value=desired,expected=old)])
    after,epoch=read_stable_entity(client,handle)
    observed_state=response.get('state',{})
    if observed_state.get('document_id')!=client.document_id or observed_state.get('geometry_revision')!=epoch['geometry_revision']:
        raise CadError('Point-correction completion epoch differs from readback')
    if after.get('type')!='Insert':raise CadError('Corrected record identity/type differs')
    if ({k:v for k,v in after['properties'].items() if k!='insert_point'}
            !={k:v for k,v in before['properties'].items() if k!='insert_point'}):
        raise CadError('Point correction changed another Insert property')
    observed=native_matrix(after['properties'],allow_unit_reflection=True)
    if (any(abs(observed[i][j]-expected_matrix[i][j])>linear_tolerance for i in range(3) for j in range(3))
            or any(abs(observed[i][3]-expected_matrix[i][3])>translation_tolerance for i in range(3))):
        raise CadError('Corrected native placement differs')
    checkpoint('after-point-correction')
    return dict(result='PASS',handle=handle,before_point=old,point=desired,matrix=observed,identity=epoch,response=response)
