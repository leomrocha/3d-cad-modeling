#!/usr/bin/env python3
"""Read-only DXF entity/context inventory with source IDs and block transforms."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import sys

from component_records import observe_file


PROFILE_TYPES={'LINE','ARC','CIRCLE','ELLIPSE','LWPOLYLINE','POLYLINE','SPLINE'}
ANNOTATION_TYPES={'TEXT','MTEXT','DIMENSION','LEADER','MLEADER','ATTRIB','ATTDEF'}


def serial(value):
    if value is None or isinstance(value,(str,bool,int)):return value
    if isinstance(value,float):
        if not math.isfinite(value):raise ValueError('Nonfinite DXF attribute')
        return value
    if isinstance(value,(list,tuple)) or hasattr(value,'__iter__'):
        return [serial(v) for v in value]
    return str(value)


def inspect(path,space='Model',layers=None,max_entities=10000,max_depth=32,max_bytes=67108864):
    import ezdxf
    from ezdxf.math import Matrix44
    from ezdxf.units import decode
    if max_entities<1 or max_depth<1 or max_bytes<1:raise ValueError('Positive inspection bounds required')
    path=Path(path).resolve()
    if path.stat().st_size>max_bytes:raise ValueError('DXF exceeds explicit byte limit')
    source=observe_file(path);doc=ezdxf.readfile(path,errors='strict')
    names=doc.layouts.names()
    if space not in names:raise ValueError('Unknown drawing space: '+space)
    selected=set(layers or []);available={l.dxf.name for l in doc.layers}
    if selected-available:raise ValueError('Unknown layers: '+', '.join(sorted(selected-available)))
    code=int(doc.header.get('$INSUNITS',0))
    try:unit=decode(code) if code else None
    except (IndexError,ValueError):unit=None
    rows=[];issues=[];visited=0
    def walk(entities,parent,trail,ancestors,inherited_layer='0'):
        nonlocal visited
        if len(ancestors)>max_depth:raise ValueError('DXF block nesting exceeds explicit depth limit')
        for entity in entities:
            visited+=1
            if visited>max_entities:raise ValueError('DXF occurrence inventory exceeds explicit entity limit')
            kind=entity.dxftype();handle=entity.dxf.get('handle')
            source_layer=entity.dxf.get('layer','0')
            effective=inherited_layer if source_layer=='0' else source_layer
            occurrence=trail+[handle or 'unhandled-'+str(visited)]
            keep=not selected or effective in selected
            props={k:serial(v) for k,v in entity.dxf.all_existing_dxf_attribs().items()}
            row={'source_handle':handle,'occurrence_path':occurrence,'type':kind,
                 'source_layer':source_layer,'effective_layer':effective,'selected':keep,
                 'world_from_block_rows':[list(r) for r in parent.rows()],
                 'coordinate_contract':'Source entity attributes retain their own OCS/extrusion; matrix maps containing block coordinates to drawing WCS.',
                 'source_attributes':props}
            row['extrusion_normal']=serial(entity.dxf.get('extrusion',(0,0,1)))
            row['coordinate_system']='OCS' if kind in {'ARC','CIRCLE','LWPOLYLINE'} or (kind=='POLYLINE' and entity.is_2d_polyline) else 'WCS_or_entity_specific'
            if kind=='LWPOLYLINE':
                row['vertices_xy_start_end_width_bulge']=[list(p) for p in entity.get_points('xyseb')]
                row['closed']=entity.closed
            if kind=='POLYLINE':
                row['vertices']=[serial(v.dxf.location) for v in entity.vertices]
                row['closed']=entity.is_closed
            row['role']='block_reference' if kind=='INSERT' else 'profile_candidate' if kind in PROFILE_TYPES else 'annotation' if kind in ANNOTATION_TYPES else 'unclassified'
            rows.append(row)
            if kind!='INSERT':continue
            name=entity.dxf.name;row['block_name']=name
            if name in ancestors:
                issues.append({'kind':'cyclic_block','occurrence_path':occurrence,'block':name});continue
            block=entity.block()
            if block is None:
                issues.append({'kind':'missing_block','occurrence_path':occurrence,'block':name});continue
            row['block_units_code']=block.block_record.dxf.get('units',0)
            row['block_base_point']=serial(block.block.dxf.base_point)
            # ezdxf supplies OCS, scale, rotation and block-base-point handling.
            if entity.mcount>max_entities-visited:raise ValueError('DXF array exceeds explicit entity limit')
            inserts=entity.multi_insert() if entity.mcount>1 else [entity]
            for i,insert in enumerate(inserts):
                matrix=Matrix44.chain(insert.matrix44(),parent)
                branch=occurrence+(['array-cell-'+str(i)] if entity.mcount>1 else [])
                walk(block,matrix,branch,ancestors+[name],effective)
            if entity.attribs:
                # Attached ATTRIB coordinates already belong to the containing
                # reference frame; do not apply the INSERT transform twice.
                walk(entity.attribs,parent,occurrence+['attributes'],ancestors,inherited_layer)
                if entity.mcount>1:issues.append({'kind':'array_attributes_retained_at_source_occurrence','occurrence_path':occurrence})
    walk(doc.layouts.get(space),Matrix44(),[space],[])
    after=observe_file(path)
    if after['sha256']!=source['sha256']:raise ValueError('DXF source changed during inspection')
    chosen=[r for r in rows if r['selected']]
    return {'state':'INVENTORIED','source':source,'reader':{'library':'ezdxf','version':ezdxf.__version__,'recovery':False,'unit_conversion':False},
            'space':space,'available_spaces':names,'selected_layers':sorted(selected),'available_layers':sorted(available),
            'units':{'insunits_code':code,'label':unit,'evidence':'DXF $INSUNITS header','state':'DECLARED' if unit else 'NEEDS_UNIT_EVIDENCE'},
            'limits':{'max_entities':max_entities,'max_depth':max_depth,'max_bytes':max_bytes},
            'counts':{'occurrences':len(rows),'selected_occurrences':len(chosen),'by_type':dict(Counter(r['type'] for r in rows))},
            'entities':rows,'issues':issues,
            'handoff':{'action':'Create a mapped and explicitly cleaned derivative (CAD-08-A02)',
                       'agent_work':'Identify intended profile versus annotations/construction geometry; resolve unit/context evidence and choose target plane.',
                       'geometry_mapping':'Original coordinates and block transforms retained; source entity OCS conversion belongs to the selected geometry adapter.'}}


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path);p.add_argument('--space',default='Model');p.add_argument('--layer',action='append')
    p.add_argument('--max-entities',type=int,default=10000);p.add_argument('--max-depth',type=int,default=32)
    p.add_argument('--max-bytes',type=int,default=67108864);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(argv)
    try:
        if a.output.exists():raise FileExistsError('Existing output preserved: '+str(a.output))
        if a.output.resolve()==a.source.resolve():raise ValueError('Source and output must differ')
        result=inspect(a.source,a.space,a.layer,a.max_entities,a.max_depth,a.max_bytes)
        with a.output.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
        print(json.dumps({'state':result['state'],'output':str(a.output),'counts':result['counts'],'units':result['units']}));return 0
    except (OSError,ValueError,KeyError,ImportError) as e:
        print(json.dumps({'state':'FAILED','error':str(e)}));return 2


if __name__=='__main__':sys.exit(main())
