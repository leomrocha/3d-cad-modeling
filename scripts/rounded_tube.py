#!/usr/bin/env python3
"""Source-bound rounded hollow-section construction using existing FERME OCS tools.

Units: mm. Section is XY centred at origin; cut length is +Z. Native geometry
checks read supported planar/cylindrical SAT or SAB surfaces and vertices.
"""
import argparse
import importlib
import json
import math
from pathlib import Path
import sys

from component_records import require_ready
from part_index import read_json


def dimensions(job):
    require_ready(job)
    f = {v['name']: v['value'] for v in job['features']}
    names = ['section width', 'section height', 'wall thickness', 'cut length',
             'outer corner radius', 'inner corner radius']
    p = {n: f[n] for n in names}
    if any(isinstance(v, bool) or not isinstance(v, (int, float))
           or not math.isfinite(v) or v <= 0 for v in p.values()):
        raise ValueError('Positive finite tube dimensions required')
    w,h,t,length,ro,ri = (p[n] for n in names)
    if not (w > 2*t and h > 2*t and ro < min(w,h)/2
            and ri < min(w-2*t,h-2*t)/2):
        raise ValueError('Tube section has no supported straight walls')
    if abs(ro-ri-t)>1e-9:
        raise ValueError('This recipe supports constant-thickness concentric corners')
    if job['units'] != 'mm':
        raise ValueError('Tube recipe requires millimetres')
    return p


def rounded_profile(w,h,r):
    if not all(math.isfinite(v) and v>0 for v in (w,h,r)) or 2*r>=min(w,h):
        raise ValueError('Rounded rectangle needs positive straight wall lengths')
    x,y=w/2,h/2
    points=[[-x+r,-y],[x-r,-y],[x,-y+r],[x,y-r],
            [x-r,y],[-x+r,y],[-x,y-r],[-x,-y+r]]
    return points,{i:math.tan(math.pi/8) for i in (1,3,5,7)}


class SelectionCheckedClient:
    """Adapt the installed select(clear=True) semantics and verify actual picks.

    OCS2026.42 treats clear=True as a clear-only operation even with handles.
    Its explicit handles selection already replaces the current selection.
    """
    def __init__(self,client):self.client=client
    def __getattr__(self,name):return getattr(self.client,name)
    def mutate(self,label,op,**fields):
        if op=='select':
            handles=fields.get('handles',[])
            fields['clear']=not bool(handles)
            response=self.client.mutate(label,op,**fields)
            selected=response.get('state',{}).get('selection')
            if selected is None:selected=self.client.read('state').get('selection')
            if sorted(selected or [])!=sorted(handles):
                raise ValueError('Selection readback differs; inspect before dependent command')
            return response
        return self.client.mutate(label,op,**fields)


def construct(client,job,outer_profile=None,route="bounded-area"):
    p=dimensions(job)
    Geometry=importlib.import_module('cadtools.geometry').Geometry
    g=Geometry(SelectionCheckedClient(client))
    w,h,t,length,ro,ri=(p[n] for n in ['section width','section height','wall thickness',
                                     'cut length','outer corner radius','inner corner radius'])
    outer,ob=rounded_profile(w,h,ro)
    inner,ib=rounded_profile(w-2*t,h-2*t,ri)
    if route=='bounded-area':
        if outer_profile:raise ValueError('Profile resume belongs to solid-subtract route')
        profiles=[g.profile('outer-boundary',outer,ob),g.profile('inner-boundary',inner,ib)]
        g.select('bounded-clear',[])
        # Pick midway through a straight wall, derived from section/wall inputs.
        response=client.mutate('bounded-extrude','run',allow_wait=True,
                               cmd=f'PRESSPULL {w/2-t/2},0,0 {length}')
        state=client.read('state')
        if state.get('command'):
            if state['command'].get('name')!='PRESSPULL':raise ValueError('Unexpected active command')
            client.mutate('bounded-finish','cancel')
        entities=client.read('query',limit=20)['entities']
        solids=[e['handle'] for e in entities if e['type']=='3D Solid']
        if len(solids)!=1:raise ValueError('Bounded extrusion must produce one native solid')
        solid=solids[0]
        # Delete only this call's temporary profile entities, keeping the solid.
        live={e['handle'] for e in entities}
        own=[h for h in profiles if h in live]
        if own:client.mutate('bounded-profile-cleanup','entities_delete',handles=own)
        g.metadata('source-label',[solid],[job['part_name'],job['representation'],
                   'Units mm; section XY; length +Z; origin front-end centre'])
        return solid
    if route=='planar-region':
        if outer_profile:raise ValueError('Profile resume belongs to solid-subtract route')
        added=importlib.import_module('cadtools.geometry').added
        regions=[]
        for name,points,bulges in [('outer-region',outer,ob),('inner-region',inner,ib)]:
            profile=g.profile(name,points,bulges)
            g.select(name+'-selection',[profile])
            regions.append(added(g.run(name+'-create','REGION')))
        region=g.subtract('planar-hollow',regions[0],[regions[1]])
        g.select('region-extrude-selection',[region])
        solid=added(g.run('region-extrude','EXTRUDE '+str(length)))
        g.metadata('source-label',[solid],[job['part_name'],job['representation'],
                   'Units mm; section XY; cut length +Z; origin front-end centre'])
        return solid
    if outer_profile is None:
        base=g.extrude('outer',outer,0,length,ob)
    else:
        record=client.read('records',collection='entities',handles=[outer_profile],limit=1)['records'][0]
        prop=record['properties']
        actual=[[v['location']['x'],v['location']['y']] for v in prop['vertices']]
        arcs=[v['bulge'] for v in prop['vertices']]
        if record['type']!='LwPolyline' or actual!=outer or arcs!=[ob.get(i,0) for i in range(8)] or not prop['is_closed'] or prop['elevation']!=0:
            raise ValueError('Preserved profile differs from sourced construction profile')
        g.select('resume-outer-selection',[outer_profile])
        base=importlib.import_module('cadtools.geometry').added(g.run('resume-outer-extrude','EXTRUDE '+str(length)))
    # Existing FERME profile recipe uses 0.1mm through-cut overrun on each end.
    cutter=g.extrude('bore',inner,-0.1,length+0.2,ib)
    solid=g.subtract('hollow',base,[cutter])
    g.metadata('source-label',[solid],[job['part_name'],job['representation'],
                 'Units mm; section XY; cut length +Z; local origin at front-end centre',
                 'Parameters and evidence: '+str(job['job_id'])])
    return solid


def sat_features(text):
    """Strict subset adapted from FERME check_ngv064_wheel.py surface reader.

    This recipe's native unrotated extrusion has identity axes; reject transformed
    or unfamiliar bodies rather than interpreting them as supported observations.
    """
    out={'planes':[],'cylinders':[],'points':[]}
    for line in text.splitlines():
        t=line.split()
        if not t:continue
        if t[0]=='transform':
            raise ValueError('Transformed SAT body requires a separate frame reader')
        if t[0]=='plane-surface':
            out['planes'].append({'origin':list(map(float,t[4:7])),
                                  'normal':list(map(float,t[7:10]))})
        elif t[0]=='cone-surface':
            if abs(float(t[16]))>1e-9 or abs(float(t[17])-1)>1e-9:
                raise ValueError('Noncylindrical cone outside tube surface reader')
            out['cylinders'].append({'origin':list(map(float,t[4:7])),
                                    'axis':list(map(float,t[7:10])),
                                    'radius':math.sqrt(sum(float(v)**2 for v in t[10:13]))})
        elif t[0]=='point':out['points'].append(list(map(float,t[4:7])))
    if not out['points'] or not out['planes'] or not out['cylinders']:
        raise ValueError('Required tube surfaces/vertices absent from native SAT')
    return out


def verify_features(features,p,tol=1e-7):
    """Numerical readback tolerance only; manufacturing limits remain source data."""
    if not math.isfinite(tol) or tol<0:raise ValueError('Finite nonnegative tolerance required')
    w,h,t,length,ro,ri=(p[n] for n in ['section width','section height','wall thickness',
                                     'cut length','outer corner radius','inner corner radius'])
    checks=[]
    def check(name,condition,observed):
        checks.append({'name':name,'result':'PASS' if condition else 'FAIL','observed':observed})
    near=lambda a,b:abs(a-b)<=tol
    ext=[[min(v[k] for v in features['points']),max(v[k] for v in features['points'])] for k in range(3)]
    expected=[[-w/2,w/2],[-h/2,h/2],[0,length]]
    check('outer section and cut length',all(near(a,b) for x,y in zip(ext,expected) for a,b in zip(x,y)),ext)
    planes=features['planes']
    for axis,span in [(0,w),(1,h)]:
        values=sorted({round(v['origin'][axis],10) for v in planes
                       if near(abs(v['normal'][axis]),1)})
        targets=sorted([-span/2,-span/2+t,span/2-t,span/2])
        check('wall planes '+('X' if axis==0 else 'Y'),len(values)==4 and all(near(a,b) for a,b in zip(values,targets)),values)
    ends=sorted({round(v['origin'][2],10) for v in planes if near(abs(v['normal'][2]),1)})
    check('square end planes',len(ends)==2 and near(ends[0],0) and near(ends[1],length),ends)
    cylinders=features['cylinders']
    targets=[(sx*(w/2-ro),sy*(h/2-ro),r) for sx in (-1,1) for sy in (-1,1) for r in (ro,ri)]
    unmatched=list(cylinders)
    for x,y,r in targets:
        hit=next((i for i,c in enumerate(unmatched) if near(c['origin'][0],x) and near(c['origin'][1],y)
                  and near(c['radius'],r) and near(abs(c['axis'][2]),1)),None)
        if hit is not None:unmatched.pop(hit)
        else:break
    check('four outer and four inner corner cylinders',hit is not None and not unmatched and len(cylinders)==8,cylinders)
    return {'result':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',
            'method':'native SAT surface and vertex observations','numeric_tolerance_mm':tol,'checks':checks}


def inspect(client,handle,job,record_path=None):
    records=client.read('records',collection='entities',handles=[handle],limit=1)
    if len(records.get('records',[]))!=1:raise ValueError('Expected one tube solid record')
    if record_path is not None:
        Path(record_path).write_text(json.dumps(records,indent=2)+'\n')
    acis=records['records'][0]['properties']['acis_data']
    text=acis['sat_data']
    encoding='SAT'
    if text:
        features=sat_features(text)
    else:
        encoding='SAB'
        try:
            from native_acis import sab_features
            features=sab_features(bytes(acis.get('sab_data',[])))
        except Exception as error:
            return records,{'result':'UNKNOWN','method':'native entity record inspection',
                            'reason':'SAB feature read unavailable: '+type(error).__name__+': '+str(error),
                            'encoding':'SAB' if acis.get('sab_data') else 'empty',
                            'document_id':records['document_id'],'revision':records['revision'],
                            'geometry_revision':records['geometry_revision'],'handle':handle}
    result=verify_features(features,dimensions(job))
    result['method']='native '+encoding+' surface and vertex observations'
    if encoding=='SAB':
        topology=features['topology']
        result['checks'].append({'name':'one closed connected hollow-section body','result':'PASS' if topology['lumps']==1 and topology['shells']==1 and topology['reciprocal_closed_partners'] else 'FAIL','observed':topology})
        result['result']='PASS' if all(c['result']=='PASS' for c in result['checks']) else 'FAIL'
    result.update(document_id=records['document_id'],revision=records['revision'],
                  geometry_revision=records['geometry_revision'],handle=handle,features=features)
    return records,result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('job',type=Path)
    for name in ['cad-modules','control','session','namespace','journal','work-dir','output']:ap.add_argument('--'+name,required=True)
    ap.add_argument('--allow-write',action='store_true')
    ap.add_argument('--route',choices=['solid-subtract','planar-region','bounded-area'],default='bounded-area')
    ap.add_argument('--resume-profile',help='Verified surviving outer profile after a definitive no-effect extrusion')
    a=ap.parse_args();job=read_json(a.job);dimensions(job)
    if not a.allow_write:raise ValueError('Explicit --allow-write required')
    work=Path(a.work_dir);output=Path(a.output)
    if not work.is_dir() or output.exists() or not output.is_absolute():raise ValueError('Existing work directory and new absolute model destination required')
    if (work/'initial-state.json').exists() and not a.resume_profile:
        raise ValueError('Existing build evidence requires explicit stage inspection')
    if Path(a.journal).exists() and not a.resume_profile:raise ValueError('Existing journal requires stage inspection and same-ID recovery')
    sys.path.insert(0,a.cad_modules)
    from cadtools.runtime import Client,Journal,load_helper
    from cadtools.verification import save_reopen
    helper=load_helper(a.control);ds=helper.descriptors(session=a.session)
    if len(ds)!=1:raise ValueError('Expected exact existing session descriptor')
    state=helper.request(ds[0],{'op':'state'},30)
    if not state.get('ok') or state.get('command') or state.get('modal'):raise ValueError('Idle existing session required')
    def write(name,value):(work/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    client=Client(helper,ds[0],state['document_id'],a.namespace,Journal(a.journal),allow_write=True)
    if a.resume_profile:
        checkpoint=read_json(work/'document-checkpoint.json')
        if checkpoint['document_id']!=state['document_id']:raise ValueError('Resume document differs')
        entities=client.read('query',limit=10)['entities']
        if len(entities)!=1 or entities[0]['handle']!=a.resume_profile:raise ValueError('Resume requires the inspected sole surviving profile')
    else:
        write('initial-state.json',state)
        client.mutate('isolated-document','new')
        state=helper.request(ds[0],{'op':'state'},30);client.document_id=state['document_id']
        if client.read('query',limit=1).get('entities'):raise ValueError('New target must be empty')
        client.checkpoint(work/'document-checkpoint.json',{})
        client.mutate('millimetres','sysvar',set={'INSUNITS':4})
        client.mutate('world-coordinates','run',cmd='UCS W')
    solid=construct(client,job,a.resume_profile,a.route)
    client.checkpoint(work/'body-checkpoint.json',{'tube':solid})
    records,checks=inspect(client,solid,job,work/'pre-save-records.json');write('pre-save-checks.json',checks)
    if checks['result']!='PASS':raise ValueError('Native geometry checks failed; inspect checkpoint')
    persistence=save_reopen(client,str(output),{'3D Solid':1});write('persistence.json',persistence)
    records,checks=inspect(client,solid,job,work/'reopened-records.json');write('reopened-checks.json',checks)
    client.checkpoint(work/'reopened-checkpoint.json',{'tube':solid})
    if checks['result']!='PASS':
        print(json.dumps({'result':checks['result'],'path':str(output),'check':checks}))
        return 1
    print(json.dumps({'result':'PASS','path':str(output),'document_id':client.document_id,'handle':solid}))
    return 0

if __name__=='__main__':sys.exit(main())
