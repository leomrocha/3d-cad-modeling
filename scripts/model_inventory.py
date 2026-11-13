#!/usr/bin/env python3
"""Check existing component files before starting another CAD construction.

Reads the external parts manifest, work records, input sheets and filesystem.
Creates no files and never connects to CAD. The caller records reconciliation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from part_index import load_index, read_json

MODEL_SUFFIXES={'.dwg','.step','.stp','.stl','.obj','.glb','.gltf','.blend','.3mf','.fcstd'}


def inventory_models(project_root):
    rows=[]
    for p in sorted(Path(project_root).resolve().rglob('*')):
        if not p.is_file() or p.suffix.lower() not in MODEL_SUFFIXES or '.git' in p.parts:
            continue
        if p.name.startswith('.'):continue
        rows.append(dict(path=str(p),format=p.suffix.lower()[1:],bytes=p.stat().st_size,
                         sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                         role='2d_reference' if '2d_schemas' in p.parts else '3d_model_file'))
    return rows


def start_check(part,index_path,cad_root,inventory,job=None):
    """Use attributed file links first; block construction on discovered candidates."""
    cad_root=Path(cad_root).resolve();job=job or {};files={p['path']:p for p in inventory}
    links=[]
    for key in ['model','output','native_model']:
        if job.get(key):links.append(str(Path(job[key]).resolve()))
    if part.get('existing_cad'):
        p=Path(part['existing_cad']);links.append(str(p.resolve() if p.is_absolute() else (cad_root/p).resolve()))
    sheet=Path(index_path).resolve().parent/part['file']
    if sheet.is_file():
        for target in re.findall(r'\]\(([^)]+)\)',sheet.read_text()):
            if target.startswith(('http:','https:')):continue
            p=Path(target)
            if p.suffix.lower() in MODEL_SUFFIXES:links.append(str((p if p.is_absolute() else sheet.parent/p).resolve()))
    matches=[files[p] for p in dict.fromkeys(links) if p in files and files[p]['role']=='3d_model_file' and files[p]['bytes']>0]
    references=[files[p] for p in dict.fromkeys(links) if p in files and files[p]['role']=='2d_reference']
    compact=lambda s:re.sub('[^a-z0-9]','',s.casefold())
    codes={compact(v) for v in re.findall(r'[A-Za-z]*\d[A-Za-z0-9.\-]*',part['name']) if len(compact(v))>=4}
    candidates=[p for p in inventory if p['role']=='3d_model_file' and p['bytes']>0 and p not in matches and any(v in compact(Path(p['path']).stem) for v in codes)]
    if matches:action='SKIP_EXISTING_MODEL'
    elif job.get('state')=='DONE' or part.get('cad_state')=='DONE':action='LOCATE_COMPLETED_MODEL'
    elif candidates:action='REVIEW_EXISTING_CANDIDATES'
    else:action='NEW_MODEL_REQUIRED'
    return dict(part_id=part['id'],part_name=part['name'],recorded_state=job.get('state','NOT_STARTED'),
                action=action,models=matches,candidates=candidates,references_2d=references,
                input_sheet=str(sheet),filesystem_model_files_checked=len(inventory))


def audit(index_path,work_index,cad_root,project_root):
    parts=load_index(index_path);work=read_json(work_index);jobs={p['part_id']:p for p in work['jobs']}
    inventory=inventory_models(project_root)
    components=[start_check(p['record'],index_path,cad_root,inventory,jobs.get(p['id'])) for p in parts]
    owners={}
    for row in components:
        for model in row['models']:owners.setdefault(model['path'],set()).add(row['part_id'])
    for row in components:
        dependencies=set(jobs.get(row['part_id'],{}).get('geometry_inputs',[]))
        related=[m for m in row['candidates'] if owners.get(m['path'],set()) & dependencies]
        row['dependency_models']=related
        row['candidates']=[m for m in row['candidates'] if m not in related]
        if row['action']=='REVIEW_EXISTING_CANDIDATES' and not row['candidates']:row['action']='NEW_MODEL_REQUIRED'
    return dict(inventory=inventory,components=components)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['index','work-index','cad-root','project-root']:parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--id')
    a=parser.parse_args();result=audit(a.index,a.work_index,a.cad_root,a.project_root)
    if a.id:
        result['components']=[p for p in result['components'] if p['part_id']==a.id]
        if not result['components']:parser.error('Component ID absent from the input index')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
