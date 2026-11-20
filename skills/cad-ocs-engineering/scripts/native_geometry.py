"""Encoding-aware native feature reads and explicit OCS point transformations."""
import math
from native_acis import sab_structure,sab_features,_sat_body_entities,_sat_cone_parameters
from step_placements import identity_sat_vertices,solid_instances,apply
from cadtools.records import read_stable_entity


def sat_structure(text):
    from ezdxf.acis.sat import parse_sat
    identity_sat_vertices(text)  # Enforces the supported identity transform contract.
    parsed=parse_sat(text);_,entities=_sat_body_entities(parsed);coedges=[e for e in entities if e.name=='coedge']
    seen={id(e) for e in entities}
    closed=bool(coedges) and all(len(e.data)>4 and e.data[3].name=='coedge' and id(e.data[3]) in seen and e.data[3].data[3] is e and e.data[3].data[4] is e.data[4] for e in coedges)
    features=dict(planes=[],cylinders=[],cones=[],points=[])
    for e in entities:
        if e.name=='point':
            p=list(map(float,e.data[1:4]))
            if len(p)!=3 or not all(math.isfinite(x) for x in p):raise ValueError('Finite SAT vertex required')
            features['points'].append(p)
        if e.name=='plane-surface':
            data=list(map(float,e.data[1:7]))
            if len(data)!=6 or not all(math.isfinite(x) for x in data):raise ValueError('Finite SAT plane required')
            features['planes'].append(dict(origin=data[:3],normal=data[3:]))
        elif e.name in ('cone-surface','cylinder-surface'):
            origin,axis,major,ratio,sine,cosine,radius=_sat_cone_parameters(e.data,parsed.header.version)
            values=origin+axis+major+[ratio,sine,cosine,radius]
            if any(not math.isfinite(v) for v in values) or abs(ratio-1)>1e-9 or radius<=0 or abs(math.sqrt(sum(v*v for v in major))-radius)>1e-7:raise ValueError('Invalid SAT circular support')
            row=dict(origin=origin,axis=axis,radius=radius)
            if abs(sine)<=1e-9 and abs(cosine-1)<=1e-9:features['cylinders'].append(row)
            else:row.update(sin_angle=sine,cos_angle=cosine);features['cones'].append(row)
        elif e.name.endswith('-surface'):raise ValueError('Unsupported SAT analytic surface '+e.name)
    if not features['points']:raise ValueError('Reachable SAT vertices required')
    features['topology']=dict(bodies=1,lumps=sum(e.name=='lump' for e in entities),shells=sum(e.name=='shell' for e in entities),coedges=len(coedges),reciprocal_closed_partners=closed)
    features.update(encoding='SAT',acis_header_units_in_mm=parsed.header.units_in_mm)
    return features


def features_from_record(record,*,require_sab=False,**options):
    if record.get('type')!='Solid3D':raise ValueError('Native Solid3D record required')
    acis=record['properties']['acis_data'];raw=acis.get('sab_data')
    if raw:return sab_features(bytes(raw),**options)
    if require_sab:raise ValueError('Saved binary topology required')
    if options:raise ValueError('SAT reader requires its explicit identity-frame contract')
    return sat_structure(acis['sat_data'])


def read_native_features(client,handle,*,require_sab=False,**options):
    row,identity=read_stable_entity(client,handle)
    return row,features_from_record(row,require_sab=require_sab,**options),identity


def source_points(record,*,prefer_sab=False):
    acis=record['properties']['acis_data']
    if acis.get('sab_data') and (prefer_sab or not acis.get('sat_data')):
        value=sab_structure(bytes(acis['sab_data']),allow_rigid=True)
        return value['points'],'reachable SAB vertices'
    return identity_sat_vertices(acis['sat_data']),'identity-frame SAT point records'


def assembly_point_extrema(records,blocks,roots,*,allow_uniform_scale=False,allow_unit_reflection=False):
    by={r['handle']:r for r in records};points=[]
    instances=solid_instances(records,blocks,roots,allow_uniform_scale=allow_uniform_scale,allow_unit_reflection=allow_unit_reflection)
    for instance in instances:
        local,_=source_points(by[instance['handle']]);points.extend(apply(instance['matrix'],p) for p in local)
    return dict(instances=instances,vertex_ranges=[[min(p[i] for p in points),max(p[i] for p in points)] for i in range(3)],scope='placed observed vertices in caller-declared drawing units')


def wcs_polyline_vertices(record):
    from ezdxf.math import OCS,Vec3
    if record.get('type')!='LwPolyline':raise ValueError('Native lightweight polyline required')
    p=record['properties'];normal=[p['normal'][a] for a in 'xyz'];elevation=p.get('elevation',0.)
    if any(not isinstance(v,(int,float)) or isinstance(v,bool) or not math.isfinite(v) for v in normal+[elevation]) or sum(v*v for v in normal)<1e-24:raise ValueError('Finite nonzero OCS frame required')
    result=[];frame=OCS(normal)
    for vertex in p['vertices']:
        xy=[vertex['location'][a] for a in ('x','y')]
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) for v in xy):raise ValueError('Finite polyline coordinates required')
        result.append(list(frame.to_wcs(Vec3(*xy,elevation))))
    return result
