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
