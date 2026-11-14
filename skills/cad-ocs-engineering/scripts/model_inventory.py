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
from urllib.parse import urlparse
from part_index import load_index, read_json
try:
    from component_records import validate_geometry_requirement, RecordError
except ImportError:
    from .component_records import validate_geometry_requirement, RecordError

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
    # Retaining a source drawing in an evidence packet does not change its
    # dimensional role. Reuse the known original's bytes rather than reopening
    # the drawing or treating its new directory as proof of a component model.
    known_2d={}
    for row in rows:
        if row['role']=='2d_reference':
            known_2d.setdefault(row['sha256'],[]).append(row['path'])
    for row in rows:
        if row['role']=='3d_model_file' and row['sha256'] in known_2d:
            row.update(role='2d_reference',role_basis='byte_identical_known_2d_reference',
                       role_source_paths=known_2d[row['sha256']])
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


def _candidate_review_records(job, root_map):
    """Validate component-specific portable reviews of filename candidates."""
    records=job.get('candidate_reviews', [])
    if not isinstance(records,list):
        raise ValueError('candidate_reviews must be a list')
    prepared=[];seen=set()
    required={'candidate_path','sha256','decision','reason','evidence_locator'}
    for index,record in enumerate(records):
        if not isinstance(record,dict) or set(record)!=required:
            raise ValueError('candidate_reviews[%d] must contain exactly candidate_path, sha256, decision, reason and evidence_locator' % index)
        candidate_path=record['candidate_path']
        if not isinstance(candidate_path,str) or not re.fullmatch(r'\$\{[A-Za-z_][A-Za-z0-9_]*\}/.+',candidate_path):
            raise ValueError('candidate_reviews[%d].candidate_path must use a named-root portable locator' % index)
        resolved=_resolve_review_path(candidate_path,root_map,'candidate_path',index)
        if resolved in seen:
            raise ValueError('Duplicate candidate review path: '+candidate_path)
        seen.add(resolved)
        digest=record['sha256']
        if not isinstance(digest,str) or not re.fullmatch(r'[0-9a-f]{64}',digest):
            raise ValueError('candidate_reviews[%d].sha256 must be 64 lowercase hexadecimal characters' % index)
        if record['decision']!='different_component':
            raise ValueError('candidate_reviews[%d].decision must be different_component' % index)
        reason=record['reason']
        if not isinstance(reason,str) or len(reason.strip())<20:
            raise ValueError('candidate_reviews[%d].reason must give a concrete explanation of at least 20 characters' % index)
        evidence=record['evidence_locator']
        if not isinstance(evidence,str) or not evidence.strip():
            raise ValueError('candidate_reviews[%d].evidence_locator must be nonempty text' % index)
        parsed=urlparse(evidence)
        if parsed.scheme:
            if parsed.scheme!='https' or not parsed.netloc:
                raise ValueError('candidate_reviews[%d].evidence_locator must use HTTPS or a named-root path' % index)
        else:
            if not re.fullmatch(r'\$\{[A-Za-z_][A-Za-z0-9_]*\}/.+',evidence):
                raise ValueError('candidate_reviews[%d].evidence_locator must use a named-root portable locator or HTTPS URL' % index)
            evidence_path=_resolve_review_path(evidence,root_map,'evidence_locator',index)
            if not evidence_path.is_file():
                raise ValueError('Candidate review evidence file is absent: '+evidence)
        prepared.append({'record':record,'resolved_path':str(resolved)})
    return prepared


def _resolve_review_path(locator, root_map, field, index):
    match=re.fullmatch(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}/(.+)',locator)
    if not match:
        raise ValueError('candidate_reviews[%d].%s must use a named-root portable locator' % (index,field))
    name,suffix=match.groups()
    if name not in root_map:
        raise ValueError('Missing configured path root: '+name)
    root=Path(root_map[name])
    if not root.is_absolute():
        raise ValueError('Configured path root must be absolute: '+name)
    resolved=(root/suffix).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as error:
        raise ValueError('candidate_reviews[%d].%s escapes its configured root' % (index,field)) from error
    return resolved


def _apply_candidate_reviews(candidates, job, root_map, protected_paths=()):
    """Dismiss only exact path/hash reviewed filename candidates."""
    reviews=_candidate_review_records(job,root_map)
    by_path={row['resolved_path']:row['record'] for row in reviews}
    protected=set(protected_paths)
    remaining=[];reviewed=[];unmatched=[]
    seen=set()
    for candidate in candidates:
        path=candidate['path'];record=by_path.get(path)
        if record is None:
            remaining.append(candidate)
            continue
        seen.add(path)
        if record['sha256']!=candidate['sha256']:
            remaining.append(candidate)
            unmatched.append({'candidate_path':record['candidate_path'],
                              'status':'STALE_HASH','reviewed_sha256':record['sha256'],
                              'current_sha256':candidate['sha256']})
            continue
        if path in protected:
            remaining.append(candidate)
            unmatched.append({'candidate_path':record['candidate_path'],
                              'status':'LINKED_MODEL_PRECEDENCE','current_sha256':candidate['sha256']})
            continue
        reviewed.append({**candidate,'decision':record['decision'],'reason':record['reason'],
                         'evidence_locator':record['evidence_locator']})
    for row in reviews:
        if row['resolved_path'] not in seen:
            unmatched.append({'candidate_path':row['record']['candidate_path'],
                              'status':'NO_CURRENT_CANDIDATE','reviewed_sha256':row['record']['sha256']})
    return remaining,reviewed,unmatched


def start_check(part,index_path,cad_root,inventory,job=None,root_map=None,configuration=None):
    """Use attributed file links first; block construction on discovered candidates."""
    cad_root=Path(cad_root).resolve();job=job or {};files={p['path']:p for p in inventory}
    try:
        non_geometric=validate_geometry_requirement(job,root_map)
    except RecordError as error:
        raise ValueError(str(error)) from error
    if non_geometric is not None:
        if job.get('part_id') != part.get('id'):
            raise ValueError('Non-geometric job part_id must match the indexed part')
        if configuration is not None or job.get('configurations'):
            raise ValueError('Non-geometric classification cannot be combined with configuration-scoped geometry')
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
        candidates,reviewed_candidates,unmatched_candidate_reviews=_apply_candidate_reviews(
            list(blockers.values()),job,root_map or {},
            protected_paths=[p['path'] for p in unscoped_link_models])
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
            reviewed_candidates=reviewed_candidates,
            unmatched_candidate_reviews=unmatched_candidate_reviews,
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
    filename_candidates=[p for p in inventory if p['role']=='3d_model_file' and p['bytes']>0 and p not in matches and any(v in compact(Path(p['path']).stem) for v in codes)]
    candidates,reviewed_candidates,unmatched_candidate_reviews=_apply_candidate_reviews(
        filename_candidates,job,root_map or {},protected_paths=[p['path'] for p in matches])
    if matches:action='SKIP_EXISTING_MODEL'
    elif non_geometric is not None and candidates:action='REVIEW_EXISTING_CANDIDATES'
    elif non_geometric is not None:action='SKIP_NON_GEOMETRIC'
    elif job.get('state')=='DONE' or part.get('cad_state')=='DONE':action='LOCATE_COMPLETED_MODEL'
    elif candidates:action='REVIEW_EXISTING_CANDIDATES'
    else:action='NEW_MODEL_REQUIRED'
    return dict(part_id=part['id'],part_name=part['name'],recorded_state=job.get('state','NOT_STARTED'),
                action=action,models=matches,candidates=candidates,references_2d=references,
                reviewed_candidates=reviewed_candidates,
                unmatched_candidate_reviews=unmatched_candidate_reviews,
                input_sheet=str(sheet),filesystem_model_files_checked=len(inventory),
                geometry_requirement=non_geometric)


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
