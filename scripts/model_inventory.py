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

MODEL_SUFFIXES={'.dwg','.step','.stp','.iges','.igs','.stl','.obj','.glb','.gltf','.blend','.3mf','.fcstd'}


def resolve_locator(value, base, root_map=None):
    """Resolve a stored path with explicit roots; reject unresolved placeholders."""
    roots=root_map or {}
    def replace(match):
        name=match.group(1)
        if name not in roots:
            raise ValueError('Missing configured path root: '+name)
        root=Path(roots[name])
        if not root.is_absolute():
            raise ValueError('Configured path root must be absolute: '+name)
        return str(root)
    value=re.sub(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}',replace,str(value))
    if '${' in value:
        raise ValueError('Malformed path root locator: '+value)
    path=Path(value)
    return (path if path.is_absolute() else Path(base)/path).resolve()


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


def _declared_configurations(job):
    """Validate the explicit configuration names in a work record."""
    declarations=job.get('configurations')
    if not isinstance(declarations,list) or not declarations:
        raise ValueError('Configuration check requires a nonempty configurations list')
    by_name={}
    for declaration in declarations:
        if not isinstance(declaration,dict) or not isinstance(declaration.get('name'),str) or not declaration['name'].strip():
            raise ValueError('Each declared configuration requires a nonempty name')
        name=declaration['name']
        if name in by_name:
            raise ValueError('Duplicate declared configuration: '+name)
        by_name[name]=declaration
    return by_name


def start_check(part,index_path,cad_root,inventory,job=None,root_map=None,configuration=None):
    """Use attributed file links first; block construction on discovered candidates."""
    cad_root=Path(cad_root).resolve();job=job or {};files={p['path']:p for p in inventory}
    if configuration is not None:
        declared=_declared_configurations(job)
        if configuration not in declared:
            raise ValueError('Unknown configuration: '+str(configuration))
        selected=declared[configuration]
        scoped_links=[]
        for key in ['model','output','native_model']:
            if selected.get(key):scoped_links.append(str(resolve_locator(selected[key],cad_root,root_map)))
        other_scoped_links=[]
        for name,declaration in declared.items():
            if name==configuration:continue
            for key in ['model','output','native_model']:
                if declaration.get(key):other_scoped_links.append((name,str(resolve_locator(declaration[key],cad_root,root_map))))
        scoped_matches=[files[p] for p in dict.fromkeys(scoped_links) if p in files and files[p]['role']=='3d_model_file' and files[p]['bytes']>0]
        other_matches=[]
        for name,path in dict.fromkeys(other_scoped_links):
            if path in files and files[path]['role']=='3d_model_file' and files[path]['bytes']>0:
                other_matches.append(dict(configuration=name,model=files[path]))

        # Links without a configuration label cannot establish which configuration
        # they represent. Keep them visible as blockers even when another scoped
        # configuration already has a model.
        unscoped_links=[]
        for key in ['model','output','native_model']:
            if job.get(key):unscoped_links.append(str(resolve_locator(job[key],cad_root,root_map)))
        if part.get('existing_cad'):
            unscoped_links.append(str(resolve_locator(part['existing_cad'],cad_root,root_map)))
        sheet=resolve_locator(part['file'],Path(index_path).resolve().parent,root_map)
        if sheet.is_file():
            for target in re.findall(r'\]\(([^)]+)\)',sheet.read_text()):
                if target.startswith(('http:','https:')):continue
                if Path(target).suffix.lower() in MODEL_SUFFIXES:
                    unscoped_links.append(str(resolve_locator(target,sheet.parent,root_map)))
        scoped_paths=set(scoped_links)|{path for _,path in other_scoped_links}
        unscoped_link_models=[files[p] for p in dict.fromkeys(unscoped_links)
                              if p in files and files[p]['role']=='3d_model_file' and files[p]['bytes']>0 and p not in scoped_paths]
        compact=lambda s:re.sub('[^a-z0-9]','',s.casefold())
        codes={compact(v) for v in [part['id']]+re.findall(r'[A-Za-z]*\d[A-Za-z0-9.\-]*',part['name']) if len(compact(v))>=4}
        unscoped_candidates=[p for p in inventory if p['role']=='3d_model_file' and p['bytes']>0
            and p['path'] not in scoped_paths and any(v in compact(Path(p['path']).stem) for v in codes)]
        blockers={p['path']:p for p in unscoped_link_models+unscoped_candidates}
        candidates=list(blockers.values())
        reference_paths=dict.fromkeys(scoped_links+unscoped_links)
        references=[files[p] for p in reference_paths if p in files and files[p]['role']=='2d_reference']
        selected_state=selected.get('state','NOT_STARTED')
        if scoped_matches:action='SKIP_EXISTING_MODEL'
        elif candidates:action='REVIEW_EXISTING_CANDIDATES'
        elif selected_state=='DONE':action='LOCATE_COMPLETED_MODEL'
        else:action='NEW_MODEL_REQUIRED'
        return dict(part_id=part['id'],part_name=part['name'],recorded_state=selected_state,
            action=action,configuration=configuration,models=scoped_matches,
            other_configuration_models=other_matches,candidates=candidates,references_2d=references,
            input_sheet=str(sheet),filesystem_model_files_checked=len(inventory))

    links=[]
    for key in ['model','output','native_model']:
        if job.get(key):links.append(str(resolve_locator(job[key],cad_root,root_map)))
    if part.get('existing_cad'):
        links.append(str(resolve_locator(part['existing_cad'],cad_root,root_map)))
    sheet=resolve_locator(part['file'],Path(index_path).resolve().parent,root_map)
    if sheet.is_file():
        for target in re.findall(r'\]\(([^)]+)\)',sheet.read_text()):
            if target.startswith(('http:','https:')):continue
            if Path(target).suffix.lower() in MODEL_SUFFIXES:
                links.append(str(resolve_locator(target,sheet.parent,root_map)))
    matches=[files[p] for p in dict.fromkeys(links) if p in files and files[p]['role']=='3d_model_file' and files[p]['bytes']>0]
    references=[files[p] for p in dict.fromkeys(links) if p in files and files[p]['role']=='2d_reference']
    compact=lambda s:re.sub('[^a-z0-9]','',s.casefold())
    codes={compact(v) for v in [part['id']]+re.findall(r'[A-Za-z]*\d[A-Za-z0-9.\-]*',part['name']) if len(compact(v))>=4}
    candidates=[p for p in inventory if p['role']=='3d_model_file' and p['bytes']>0 and p not in matches and any(v in compact(Path(p['path']).stem) for v in codes)]
    if matches:action='SKIP_EXISTING_MODEL'
    elif job.get('state')=='DONE' or part.get('cad_state')=='DONE':action='LOCATE_COMPLETED_MODEL'
    elif candidates:action='REVIEW_EXISTING_CANDIDATES'
    else:action='NEW_MODEL_REQUIRED'
    return dict(part_id=part['id'],part_name=part['name'],recorded_state=job.get('state','NOT_STARTED'),
                action=action,models=matches,candidates=candidates,references_2d=references,
                input_sheet=str(sheet),filesystem_model_files_checked=len(inventory))


def audit(index_path,work_index,cad_root,project_root,root_map=None,configuration=None,part_id=None):
    parts=load_index(index_path);work=read_json(work_index);jobs={p['part_id']:p for p in work['jobs']}
    inventory=inventory_models(project_root)
    if configuration is not None and not part_id:
        raise ValueError('--configuration requires --id')
    components=[start_check(p['record'],index_path,cad_root,inventory,jobs.get(p['id']),root_map,
        configuration if configuration is not None and p['id']==part_id else None) for p in parts]
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
    parser.add_argument('--configuration')
    parser.add_argument('--root',action='append',default=[],metavar='NAME=ABSOLUTE_PATH')
    a=parser.parse_args();roots={}
    for entry in a.root:
        name,sep,path=entry.partition('=')
        if not sep or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*',name) or not Path(path).is_absolute():
            parser.error('--root requires NAME=ABSOLUTE_PATH')
        if name in roots:parser.error('Duplicate configured path root: '+name)
        roots[name]=path
    if a.configuration is not None and a.id is None:parser.error('--configuration requires --id')
    try:result=audit(a.index,a.work_index,a.cad_root,a.project_root,roots,a.configuration,a.id)
    except ValueError as exc:parser.error(str(exc))
    if a.id:
        result['components']=[p for p in result['components'] if p['part_id']==a.id]
        if not result['components']:parser.error('Component ID absent from the input index')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
