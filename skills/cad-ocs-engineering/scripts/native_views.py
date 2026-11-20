"""Render native solids and straight polyline boundaries with exact instance transforms.

Displayed point bounds describe samples/endpoints. Source geometry and dimensions
remain separate caller inputs. Imports make no native connection or filesystem writes.
"""
import hashlib
import math
from pathlib import Path
import xml.etree.ElementTree as ET

from native_acis import _rigid_world, sat_readback, solid_acis_payload
from native_geometry import wcs_straight_polyline_segments
from step_placements import native_matrix,eye,multiply,apply
from cadtools.records import iter_records,identity
from cadtools.runtime import owned_document,CadError
from ocs_document_cleanup import cleanup_owned_documents


def boundary_curves(data):
    if isinstance(data, str):
        result = sat_readback(data, allow_rigid=True, include_cylinders=False)
        if not result['topology']['reciprocal_closed_partners']:
            raise ValueError('Reciprocal boundary graph required')
        return result['edges']
    from ezdxf.acis.sab import parse_sab
    from ezdxf.acis.const import Tags
    parsed=parse_sab(data)
    if parsed.header.version!=700:raise ValueError('Observed ACIS700 boundary layout required')
    bodies=[e for e in parsed.entities if e.name=='body']
    if len(bodies)!=1:raise ValueError('Exactly one native body required')
    refs=lambda e:[t.value for t in e.data if t.tag==Tags.POINTER and t.value.name!='null-ptr']
    pending=bodies.copy();seen={}
    while pending:
        e=pending.pop()
        if id(e) not in seen:seen[id(e)]=e;pending.extend(refs(e))
    coedges=[e for e in seen.values() if e.name=='coedge']
    if not coedges or any(e.data[3].value.name!='coedge' or id(e.data[3].value) not in seen or e.data[3].value.data[3].value is not e or e.data[3].value.data[4].value is not e.data[4].value for e in coedges):raise ValueError('Reciprocal boundary graph required')
    world,_=_rigid_world(list(seen.values()),Tags,True)
    def vec(token,point=False):
        if token.tag not in (Tags.LOCATION_VEC,Tags.DIRECTION_VEC):raise ValueError('Native vector required')
        values=list(token.value)
        if len(values)!=3 or any(not math.isfinite(v) for v in values):raise ValueError('Finite native vector required')
        return world(values,point)
    edges=[]
    for edge in [e for e in seen.values() if e.name=='edge']:
        vertices=[v for v in refs(edge) if v.name=='vertex'];curves=[c for c in refs(edge) if c.name.endswith('-curve')]
        if len(vertices)!=2 or len(curves)!=1:raise ValueError('Two vertices and one native curve required')
        endpoints=[]
        for vertex in vertices:
            points=[p for p in refs(vertex) if p.name=='point']
            if len(points)!=1:raise ValueError('Boundary point required')
            endpoints.append(vec(points[0].data[1],True))
        curve=curves[0];row=dict(curve_type=curve.name,endpoints=endpoints)
        if curve.name=='ellipse-curve':
            tokens=curve.data
            if len(tokens)!=7 or tokens[4].tag!=Tags.DOUBLE:raise ValueError('Unsupported native ellipse layout')
            start=edge.data[2].value;end=edge.data[4].value
            if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in (start,end,end-start)):raise ValueError('Finite curve interval required')
            major=vec(tokens[3]);normal=vec(tokens[2]);ratio=tokens[4].value
            if not 0<ratio<=1 or not math.isfinite(ratio) or sum(v*v for v in major)<=0 or abs(sum(v*v for v in normal)-1)>1e-8 or abs(sum(a*b for a,b in zip(major,normal)))>1e-8*max(1,math.sqrt(sum(v*v for v in major))):raise ValueError('Invalid ellipse basis')
            row.update(start_parameter=start,end_parameter=end,ellipse=dict(center=vec(tokens[1],True),major_axis=major,normal=normal,minor_to_major_ratio=ratio))
        elif curve.name!='straight-curve':row['representation']='native trim endpoints'
        edges.append(row)
    if not edges:raise ValueError('Native boundary edges required')
    return edges


def sample(edge,*,points_per_revolution=128,endpoint_tolerance=1e-5,max_points=100000):
    if type(points_per_revolution) is not int or points_per_revolution<4 or not math.isfinite(endpoint_tolerance) or endpoint_tolerance<=0 or type(max_points) is not int or max_points<4:raise ValueError('Positive display bounds required')
    if edge['curve_type']=='straight-curve':return edge['endpoints'],False
    if edge['curve_type']!='ellipse-curve':return edge['endpoints'],True
    e=edge['ellipse'];c=e['center'];major=e['major_axis'];n=e['normal'];ratio=e['minor_to_major_ratio']
    minor=[(n[(i+1)%3]*major[(i+2)%3]-n[(i+2)%3]*major[(i+1)%3])*ratio for i in range(3)]
    start,end=edge['start_parameter'],edge['end_parameter'];count=max(3,math.ceil(abs(end-start)/(2*math.pi)*points_per_revolution)+1)
    if count>max_points:raise ValueError('Curve sample bound exceeded')
    points=[[c[i]+math.cos(t)*major[i]+math.sin(t)*minor[i] for i in range(3)] for t in [start+(end-start)*k/(count-1) for k in range(count)]]
    if max(min(math.dist(p,q) for q in edge['endpoints']) for p in (points[0],points[-1]))>endpoint_tolerance:return edge['endpoints'],True
    return points,False


def placed_boundaries(records,blocks,*,max_instances=10000):
    by={r['handle']:r for r in records};by_name={b['name']:b['properties'] for b in blocks};out=[];cache={};instances=[]
    def visit(handle,matrix,path,active):
        if handle in active:raise ValueError('Cyclic native blocks')
        row=by[handle]
        if row['type']=='Insert':
            props=row['properties'];block=by_name[props['block_name']]
            if any(abs(block['base_point'][a])>1e-9 for a in 'xyz'):raise ValueError('Nonzero block base unsupported')
            transform=multiply(matrix,native_matrix(props,allow_unit_reflection=True))
            for child in block['entity_handles']:visit(child if isinstance(child,str) else format(child,'X'),transform,path+[handle],active|{handle})
        elif row['type']=='Circle':return
        elif row['type'] in ('Solid3D','LwPolyline'):
            if len(instances)>=max_instances:raise ValueError('Display instance bound exceeded')
            instances.append(dict(handle=handle,path=path,matrix=matrix))
            if handle not in cache:
                if row['type'] == 'Solid3D':
                    cache[handle] = boundary_curves(solid_acis_payload(row))
                else:
                    cache[handle] = [
                        {'curve_type': 'straight-curve', 'endpoints': ends}
                        for ends in wcs_straight_polyline_segments(row)
                    ]
            for edge in cache[handle]:
                points,fallback=sample(edge)
                out.append(dict(points=[apply(matrix,p) for p in points],endpoints_only=fallback,handle=handle,curve_type=edge['curve_type']))
        else:raise ValueError('Unsupported native display leaf '+row['type'])
    for root in by_name['*Model_Space']['entity_handles']:visit(root if isinstance(root,str) else format(root,'X'),eye(),[],set())
    if not instances:raise ValueError('No supported native boundaries reached')
    return out,instances


def render_views(edges,directory,*,stem,title,formats=('svg',),include_top_isometric=False):
    """Write XY/XZ/YZ and isometric views; optionally add an upright top isometric."""
    directory=Path(directory)
    if not directory.is_dir() or not stem or Path(stem).name!=stem or any(f not in ('svg','png') for f in formats):raise ValueError('Output directory, basename and supported formats required')
    outputs=[]
    projections=[('XY',lambda p:(p[0],p[1])),('XZ',lambda p:(p[0],p[2])),('YZ',lambda p:(p[1],p[2])),('isometric',lambda p:((p[0]-p[1])/math.sqrt(2),(p[0]+p[1]-2*p[2])/math.sqrt(6)))]
    if type(include_top_isometric) is not bool:
        raise ValueError('include_top_isometric must be a boolean')
    if include_top_isometric:
        def top_isometric(point):
            x, y, z = point
            return (x - y) / math.sqrt(2), (2 * z - x - y) / math.sqrt(6)
        projections.append(('top-isometric', top_isometric))
    targets=[directory/(stem+'-'+name+'.'+ext) for name,_ in projections for ext in formats]
    if any(p.exists() for p in targets):raise ValueError('Retain existing views; choose a new output stem')
    for name,project in projections:
        points=[project(p) for edge in edges for p in edge['points']]
        if not points or any(not math.isfinite(v) for p in points for v in p):raise ValueError('Finite display points required')
        lo=[min(p[i] for p in points) for i in (0,1)];hi=[max(p[i] for p in points) for i in (0,1)];span=max(hi[i]-lo[i] for i in (0,1)) or 1
        if 'svg' in formats:
            root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox='0 0 1000 800');ET.SubElement(root,'title').text=title+' | '+name+' | mm'
            ET.SubElement(root,'rect',width='1000',height='800',fill='white')
            ET.SubElement(root,'text',x='20',y='30').text=title+' | '+name+' | native edge samples and trim endpoints (mm)'
            def screen(p):return [500+(p[0]-(lo[0]+hi[0])/2)*700/span,420-(p[1]-(lo[1]+hi[1])/2)*700/span]
            for edge in edges:
                mapped=[screen(project(p)) for p in edge['points']]
                if edge['endpoints_only']:
                    for x,y in mapped:ET.SubElement(root,'circle',cx=str(x),cy=str(y),r='1.5',fill='#425466')
                else:ET.SubElement(root,'polyline',points=' '.join(str(x)+','+str(y) for x,y in mapped),fill='none',stroke='#204e76',**{'stroke-width':'1'})
            path=directory/(stem+'-'+name+'.svg');ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)
            outputs.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),projection=name,format='svg'))
        if 'png' in formats:
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            fig,ax=plt.subplots(figsize=(10,8));ax.set_aspect('equal');ax.set_title(title+' | '+name);ax.set_xlabel('mm');ax.set_ylabel('mm')
            for edge in edges:
                p=[project(p) for p in edge['points']];x,y=zip(*p)
                if edge['endpoints_only']:ax.scatter(x,y,s=2)
                else:ax.plot(x,y,linewidth=.6)
            path=directory/(stem+'-'+name+'.png');fig.savefig(path,dpi=150);plt.close(fig)
            outputs.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),projection=name,format='png'))
    return outputs


def render_saved_model(client,source,directory,*,stem,title,persistence_receipt,formats=('svg',),include_top_isometric=False):
    source=Path(source);digest=hashlib.sha256(source.read_bytes()).hexdigest()
    if persistence_receipt.get('result')!='PASS' or persistence_receipt.get('saved_path')!=str(source) or persistence_receipt.get('sha256')!=digest:raise CadError('Source persistence receipt must bind the saved model')
    owned_document(client,'open-view','open',path=str(source))
    before=client.read('state');baseline=identity(before)
    if client.read('header').get('insertion_units')!=4:raise CadError('Display requires declared native millimetres')
    rows=list(iter_records(client,'entities'));blocks=list(iter_records(client,'block_records'))
    edges,instances=placed_boundaries(rows,blocks)
    if identity(client.read('state'))!=baseline:raise CadError('External activation/revision interrupted display extraction')
    outputs=render_views(edges,directory,stem=stem,title=title,formats=formats,
                         include_top_isometric=include_top_isometric)
    if hashlib.sha256(source.read_bytes()).hexdigest()!=digest:raise CadError('Source changed during rendering')
    evidence=dict(document_id=client.document_id,expected_path=str(source),expected_geometry_revision=baseline[2],construction_copy=False,dirty_discard_allowed=False,saved_model_path=str(source),saved_model_sha256=digest,persistence_receipt=persistence_receipt)
    cleanup=cleanup_owned_documents(state_reader=lambda:client.helper.request(client.descriptor,{'op':'state'},client.timeout),client=client,owned_documents=[evidence],namespace=client.namespace+'-view-cleanup')
    return dict(source_sha256=digest,outputs=outputs,identity=dict(zip(('document_id','revision','geometry_revision'),baseline)),instances=instances,unsupported_trim_edges=sum(e['endpoints_only'] for e in edges),bounds_scope='displayed edge samples and trim endpoints',cleanup=cleanup)
