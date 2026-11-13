"""Read supported native OCS ACIS700 SAB records through ezdxf's MIT parser.

This adapter reads geometry; it creates no CAD/export files. Values retain OCS
model coordinates. ACIS header unit metadata is reported separately.
"""
import math


def _rigid_world(reachable,Tags,allow_rigid):
    transforms=[e for e in reachable if e.name=='transform']
    if transforms and not allow_rigid:
        raise ValueError('Transformed SAB requires the rigid-frame reader option')
    if len(transforms)>1:raise ValueError('Multiple native body transforms unsupported')
    matrix=None;translation=None
    if transforms:
        tokens=transforms[0].data
        if len(tokens)<5 or any(t.tag!=Tags.DIRECTION_VEC for t in tokens[:4]) or tokens[4].tag!=Tags.DOUBLE or abs(tokens[4].value-1)>1e-9:
            raise ValueError('Only observed unit-scale native rigid transforms supported')
        matrix=[list(t.value) for t in tokens[:3]];translation=list(tokens[3].value)
        if not all(math.isfinite(v) for col in matrix+[translation] for v in col):raise ValueError('Nonfinite transform')
        for i in range(3):
            for j in range(3):
                if abs(sum(matrix[i][k]*matrix[j][k] for k in range(3))-(1 if i==j else 0))>1e-9:raise ValueError('Nonrigid native transform')
        det=sum(matrix[0][i]*(matrix[1][(i+1)%3]*matrix[2][(i+2)%3]-matrix[1][(i+2)%3]*matrix[2][(i+1)%3]) for i in range(3))
        if abs(det-1)>1e-9:raise ValueError('Reflected or singular native transform unsupported')
    def world(values,point=False):
        if matrix is None:return list(values)
        return [sum(matrix[j][i]*values[j] for j in range(3))+(translation[i] if point else 0) for i in range(3)]
    return world, ({'column_major_rotation':matrix,'translation':translation,'scale':1} if transforms else None)


def sab_structure(data,allow_rigid=False):
    """Read body connectivity and vertices independently of surface equations."""
    from ezdxf.acis.sab import parse_sab
    from ezdxf.acis.const import Tags
    if not isinstance(data,(bytes,bytearray)) or not data:raise ValueError('Nonempty native SAB bytes required')
    b=parse_sab(data)
    if b.header.version!=700:raise ValueError('This adapter supports observed ACIS700 records')
    bodies=[e for e in b.entities if e.name=='body']
    if len(bodies)!=1:raise ValueError('Exactly one body required for component checks')
    pending=bodies.copy();seen={}
    while pending:
        e=pending.pop()
        if id(e) in seen:continue
        seen[id(e)]=e
        pending.extend(t.value for t in e.data if t.tag==Tags.POINTER and t.value.name!='null-ptr')
    reachable=list(seen.values())
    world,body_transform=_rigid_world(reachable,Tags,allow_rigid)
    coedges=[e for e in reachable if e.name=='coedge']
    closed=bool(coedges) and all(e.data[3].value.name=='coedge' and e.data[3].value.data[3].value is e for e in coedges)
    points=[world(list(e.data[1].value),True) for e in reachable if e.name=='point']
    if not points or not all(len(p)==3 and all(math.isfinite(v) for v in p) for p in points):raise ValueError('Finite reachable vertices required')
    return {'points':points,'surface_types':sorted(set(e.name for e in reachable if e.name.endswith('-surface'))),
            'topology':{'bodies':1,'lumps':sum(e.name=='lump' for e in reachable),'shells':sum(e.name=='shell' for e in reachable),
                        'faces':sum(e.name=='face' for e in reachable),'coedges':len(coedges),'reciprocal_closed_partners':closed},
            'method':'native body graph and vertices; surface equations excluded','acis_header_units_in_mm':b.header.units_in_mm}


def named_parts(record, metadata_app, required_parts, aliases=None, **reader_options):
    """Read exact named solids; accept observed Component: labels with optional space."""
    parts={}
    for row in record['records']:
        prop=row['properties']
        labels=[v['String'].split(':',1)[1].strip()
                for app in prop['common']['extended_data']['records']
                if app['application_name']==metadata_app
                for v in app['values'] if v.get('String','').startswith('Component:')]
        if len(labels)!=1 or not labels[0]:raise ValueError('Each solid requires one source component label')
        name=(aliases or {}).get(labels[0],labels[0])
        if name in parts:raise ValueError('Duplicate component label')
        parts[name]=sab_features(bytes(prop['acis_data']['sab_data']),**reader_options)
    if set(parts)!=set(required_parts):raise ValueError('Native component set differs from the source job')
    return parts


def _torus_surface(tokens, Tags, world):
    """Read the observed ACIS700 typed torus record, after its attribute pointer.

    Source: retained native records and the linked SAT format review in
    execution/torus-native-reader-2026-11-13.md. No component dimensions enter
    the decoder. Surface parameter bounds remain outside this observation API.
    """
    expected = [Tags.POINTER, Tags.LOCATION_VEC, Tags.DIRECTION_VEC,
                Tags.DOUBLE, Tags.DOUBLE, Tags.DIRECTION_VEC]
    if len(tokens) < len(expected) or [t.tag for t in tokens[:6]] != expected:
        raise ValueError('Unsupported native torus token layout')
    center, axis, radial = [list(tokens[i].value) for i in (1, 2, 5)]
    if any(len(v) != 3 or not all(math.isfinite(x) for x in v)
           for v in (center, axis, radial)):
        raise ValueError('Invalid native torus vectors')
    major, minor = tokens[3].value, tokens[4].value
    if (not math.isfinite(major) or not math.isfinite(minor)
            or not major > minor > 0):
        raise ValueError('Only positive ring-shaped native tori supported')
    if (abs(sum(x*x for x in axis)-1) > 1e-9
            or abs(sum(x*x for x in radial)-1) > 1e-9
            or abs(sum(a*b for a,b in zip(axis,radial))) > 1e-9):
        raise ValueError('Native torus requires orthonormal axis/reference directions')
    return {'center': world(center, True), 'axis': world(axis),
            'major_radius': major, 'minor_radius': minor}


def sab_features(data,allow_rigid=False,allow_spheres=False,allow_cones=False,include_loops=False,allow_tori=False):
    from ezdxf.acis.sab import parse_sab,SabDataLoader
    from ezdxf.acis.const import Tags
    if not isinstance(data,(bytes,bytearray)) or not data:
        raise ValueError('Nonempty native SAB bytes required')
    b=parse_sab(data)
    if b.header.version!=700:raise ValueError('This adapter supports observed ACIS700 records')
    bodies=[e for e in b.entities if e.name=='body']
    if len(bodies)!=1:raise ValueError('Exactly one body required for component checks')
    # Traverse the actual body graph. Unreferenced surface records cannot supply
    # a passing feature. Keep cycles bounded by entity identity.
    pending=bodies.copy();seen={};refs=lambda e:[t.value for t in e.data if t.tag==Tags.POINTER and t.value.name!='null-ptr']
    while pending:
        e=pending.pop()
        if id(e) in seen:continue
        seen[id(e)]=e;pending.extend(refs(e))
    reachable=list(seen.values())
    world,body_transform=_rigid_world(reachable,Tags,allow_rigid)
    faces=[e for e in reachable if e.name=='face']
    if not faces:raise ValueError('Body has no reachable faces')
    surfaces={}
    for f in faces:
        surf=[e for e in refs(f) if e.name.endswith('-surface')]
        if len(surf)!=1:raise ValueError('Face needs one supported analytic surface')
        allowed=['plane-surface','cone-surface']+(['sphere-surface'] if allow_spheres else [])+(['torus-surface'] if allow_tori else [])
        if surf[0].name not in allowed:
            raise ValueError('Unsupported surface: '+surf[0].name)
        surfaces[id(surf[0])]=surf[0]
    out={'planes':[],'cylinders':[],'cones':[],'spheres':[],'points':[]}
    if allow_tori:out['tori']=[]
    def vec(token):
        if token.tag not in [Tags.LOCATION_VEC,Tags.DIRECTION_VEC]:raise ValueError('Expected native vector token')
        values=list(token.value)
        if len(values)!=3 or not all(math.isfinite(v) for v in values):raise ValueError('Invalid native vector')
        return values
    for e in surfaces.values():
        t=e.data
        if e.name=='plane-surface':out['planes'].append({'origin':world(vec(t[1]),True),'normal':world(vec(t[2]))})
        elif e.name=='torus-surface':
            out['tori'].append(_torus_surface(t,Tags,world))
        elif e.name=='sphere-surface':
            if t[2].tag!=Tags.DOUBLE or not math.isfinite(t[2].value) or t[2].value<=0:raise ValueError('Invalid native sphere radius')
            out['spheres'].append({'origin':world(vec(t[1]),True),'radius':t[2].value})
        else:
            loader=SabDataLoader(t,b.header.version);loader.read_ptr()
            origin=loader.read_vec3();axis=loader.read_vec3();major=loader.read_vec3()
            ratio=loader.read_double();loader.read_interval();loader.read_interval()
            sine=loader.read_double();cosine=loader.read_double();native_radius=loader.read_double()
            if not all(math.isfinite(v) for v in [ratio,sine,cosine,native_radius]+list(origin)+list(axis)+list(major)):
                raise ValueError('Nonfinite native cone/cylinder parameters')
            if abs(ratio-1)>1e-9:raise ValueError('Only circular cone/cylinder sections supported')
            radius=math.sqrt(sum(v*v for v in major))
            if radius<=0 or abs(radius-native_radius)>1e-7:raise ValueError('Contradictory native radii')
            record={'origin':world(origin,True),'axis':world(axis),'radius':radius}
            if abs(sine)<=1e-9 and abs(cosine-1)<=1e-9:out['cylinders'].append(record)
            elif allow_cones:
                record.update(sin_angle=sine,cos_angle=cosine);out['cones'].append(record)
            else:raise ValueError('Noncylindrical cone requires explicit cone option')
    for e in reachable:
        if e.name=='point':out['points'].append(world(vec(e.data[1]),True))
    if not out['points']:raise ValueError('Body has no reachable vertices')
    coedges=[e for e in reachable if e.name=='coedge']
    # The observed ACIS700 coedge fields and ezdxf entity definitions identify
    # the partner at slot3. Require reciprocal partner links for this closed body.
    closed=bool(coedges)
    for e in coedges:
        partner=e.data[3].value
        closed=closed and partner.name=='coedge' and partner.data[3].value is e
    if include_loops:
        out['planar_face_loops']=[]
        def linked(first,next_slot,kind,circular=False):
            rows=[];current=first;visited=set()
            while current.name!='null-ptr':
                if id(current) in visited:
                    if circular and current is first:return rows
                    raise ValueError('Unexpected native link cycle')
                if current.name!=kind:raise ValueError('Unexpected native linked record')
                visited.add(id(current));rows.append(current);current=current.data[next_slot].value
            if circular:raise ValueError('Open native boundary loop')
            return rows
        for face in faces:
            surf=next(e for e in refs(face) if e.name.endswith('-surface'))
            if surf.name!='plane-surface':continue
            loops=[]
            for loop in linked(face.data[2].value,1,'loop'):
                points=[]
                edges=linked(loop.data[2].value,1,'coedge',True)
                for coedge in edges:
                    edge=coedge.data[4].value
                    for vertex in [e for e in refs(edge) if e.name=='vertex']:
                        pt=next(e for e in refs(vertex) if e.name=='point')
                        points.append(world(vec(pt.data[1]),True))
                loops.append({'points':points,'edge_count':len(edges)})
            out['planar_face_loops'].append({'origin':world(vec(surf.data[1]),True),'normal':world(vec(surf.data[2])),'loops':loops})
    if include_loops:
        # Coplanar Boolean fragments share internal edges. Cancel those edges
        # by face ownership before grouping the actual outer/hole boundaries.
        groups={}
        for face in faces:
            surf=next(e for e in refs(face) if e.name.endswith('-surface'))
            if surf.name!='plane-surface':continue
            normal=world(vec(surf.data[2]));origin=world(vec(surf.data[1]),True)
            if next((v for v in normal if abs(v)>1e-9),1)<0:normal=[-v for v in normal]
            key=tuple(round(v,7) for v in normal+[sum(a*b for a,b in zip(normal,origin))])
            groups.setdefault(key,[]).append(face)
        out['planar_boundary_components']=[]
        for plane,members in groups.items():
            member_ids={id(f) for f in members};adj={};coords={}
            for face in members:
                for loop in linked(face.data[2].value,1,'loop'):
                    for coedge in linked(loop.data[2].value,1,'coedge',True):
                        partner=coedge.data[3].value
                        if partner.name=='coedge' and id(partner.data[6].value.data[3].value) in member_ids:continue
                        edge=coedge.data[4].value;vertices=[e for e in refs(edge) if e.name=='vertex']
                        if len(vertices)!=2:continue
                        keys=[]
                        for vertex in vertices:
                            pt=next(e for e in refs(vertex) if e.name=='point')
                            xyz=world(vec(pt.data[1]),True);key=tuple(round(v,7) for v in xyz);coords[key]=xyz;keys.append(key)
                        a,c=keys
                        if a==c:continue
                        adj.setdefault(a,set()).add(c);adj.setdefault(c,set()).add(a)
            remaining=set(adj);components=[]
            while remaining:
                todo=[remaining.pop()];component=set()
                while todo:
                    point=todo.pop()
                    if point in component:continue
                    component.add(point);remaining.discard(point);todo.extend(adj[point]-component)
                points=[coords[k] for k in component]
                components.append({'points':points,'closed_degree_two':all(len(adj[k])==2 for k in component),
                                   'bounds':{'min':[min(p[k] for p in points) for k in range(3)],'max':[max(p[k] for p in points) for k in range(3)]}})
            out['planar_boundary_components'].append({'plane_normal':list(plane[:3]),'plane_offset':plane[3],'components':components})
    out['topology']={'bodies':1,'lumps':sum(e.name=='lump' for e in reachable),
                     'shells':sum(e.name=='shell' for e in reachable),'faces':len(faces),
                     'coedges':len(coedges),'reciprocal_closed_partners':closed}
    if body_transform:out['body_transform']=body_transform
    out['encoding']='SAB';out['decoder']='ezdxf.acis.sab.parse_sab'
    out['acis_header_units_in_mm']=b.header.units_in_mm
    return out
