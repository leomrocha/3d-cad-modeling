"""Read supported native OCS ACIS700 SAB and SAT records through ezdxf's MIT parser.

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


def _sab_body_graph(data):
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
    return b,seen


def sab_structure(data,allow_rigid=False):
    """Read body connectivity and vertices independently of surface equations."""
    from ezdxf.acis.const import Tags

    b, seen = _sab_body_graph(data)
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


def sab_straight_planar_faces(data, face_indices, *, tolerance_mm, allow_rigid=False):
    """Read selected reachable ACIS700 planar face loops with straight edges."""
    from ezdxf.acis.const import Tags

    if not math.isfinite(tolerance_mm) or tolerance_mm <= 0:
        raise ValueError('Positive planar face tolerance required')
    model, reachable = _sab_body_graph(data)
    indices = list(face_indices)
    if not indices or any(type(i) is not int or not 0 <= i < len(model.entities) for i in indices):
        raise ValueError('Valid SAB entity indices required')
    if len(set(indices)) != len(indices):
        raise ValueError('Duplicate face entity index')
    world, _ = _rigid_world(reachable.values(), Tags, allow_rigid)

    def read_point(vertex):
        if vertex.name != 'vertex':
            raise ValueError('Native edge endpoint requires a vertex')
        points = [token.value for token in vertex.data
                  if token.tag == Tags.POINTER and token.value.name == 'point']
        if len(points) != 1:
            raise ValueError('Native edge endpoint requires one vertex point')
        point = points[0].data[1]
        if point.tag != Tags.LOCATION_VEC or not all(math.isfinite(v) for v in point.value):
            raise ValueError('Finite native boundary point required')
        return world(point.value, True)

    result = []
    for index in indices:
        face = model.entities[index]
        if id(face) not in reachable or face.name != 'face':
            raise ValueError('Selected entity is not a reachable face')
        surface = face.data[5].value
        loop = face.data[2].value
        if (surface.name != 'plane-surface' or loop.name != 'loop'
                or loop.data[1].value.name != 'null-ptr' or loop.data[3].value is not face):
            raise ValueError('Selected face requires one planar boundary loop')
        origin = world(surface.data[1].value, True)
        normal = world(surface.data[2].value)
        if not all(math.isfinite(v) for v in origin + normal) or abs(math.hypot(*normal)-1) > 1e-8:
            raise ValueError('Finite planar support with unit normal required')
        start = loop.data[2].value
        current = start
        visited = set()
        edges = []
        while id(current) not in visited:
            if current.name != 'coedge' or current.data[6].value is not loop:
                raise ValueError('Selected planar face has an invalid boundary link')
            visited.add(id(current))
            edge = current.data[4].value
            sense = current.data[5]
            if edge.name != 'edge' or edge.data[6].value.name != 'straight-curve':
                raise ValueError('Selected planar face requires straight boundary edges')
            if sense.tag not in (Tags.BOOL_TRUE, Tags.BOOL_FALSE):
                raise ValueError('Explicit native coedge sense required')
            a, b = (read_point(edge.data[i].value) for i in (1, 3))
            edges.append((b, a) if sense.value else (a, b))
            current = current.data[1].value
        if (current is not start or len(edges) < 3
                or any(math.dist(end, edges[(i+1) % len(edges)][0]) > tolerance_mm
                       or math.dist(begin, end) <= tolerance_mm
                       for i, (begin, end) in enumerate(edges))):
            raise ValueError('Selected planar face boundary is open or degenerate')
        if any(abs(sum((p-o)*n for p,o,n in zip(point,origin,normal,strict=True))) > tolerance_mm
               for edge in edges for point in edge):
            raise ValueError('Boundary point differs from selected plane')
        result.append(dict(entity_index=index, origin=origin, normal=normal,
                           vertices=[begin for begin, _ in edges]))
    return result


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
    the supported native torus layout. Caller dimensions enter
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


def sab_features(data,allow_rigid=False,allow_spheres=False,allow_cones=False,include_loops=False,allow_tori=False,include_edge_curves=False,edge_policy='strict'):
    if edge_policy not in ('strict','endpoints'):raise ValueError('Unknown boundary policy')
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
    surface_feature_by_id={}
    for e in surfaces.values():
        t=e.data
        if e.name=='plane-surface':
            row={'origin':world(vec(t[1]),True),'normal':world(vec(t[2]))}
            out['planes'].append(row);surface_feature_by_id[id(e)]=row
        elif e.name=='torus-surface':
            row=_torus_surface(t,Tags,world);out['tori'].append(row);surface_feature_by_id[id(e)]=row
        elif e.name=='sphere-surface':
            if t[2].tag!=Tags.DOUBLE or not math.isfinite(t[2].value) or t[2].value<=0:raise ValueError('Invalid native sphere radius')
            row={'origin':world(vec(t[1]),True),'radius':t[2].value}
            out['spheres'].append(row);surface_feature_by_id[id(e)]=row
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
            if abs(sine)<=1e-9 and abs(cosine-1)<=1e-9:
                out['cylinders'].append(record);surface_feature_by_id[id(e)]=record
            elif allow_cones:
                record.update(sin_angle=sine,cos_angle=cosine)
                out['cones'].append(record);surface_feature_by_id[id(e)]=record
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
    if include_edge_curves:
        # Preserve the face -> loop -> coedge -> edge graph and its analytic
        # boundary curves. This is opt-in because older callers consume the
        # compact loop summaries above. The typed edge layout is accepted only
        # for the observed ACIS700 straight/ellipse records.
        coedge_owner={}
        face_surfaces=[]
        for i,face in enumerate(faces):
            surf=next(e for e in refs(face) if e.name.endswith('-surface'))
            face_surfaces.append(surf)
            for loop in linked(face.data[2].value,1,'loop'):
                for coedge in linked(loop.data[2].value,1,'coedge',True):
                    old=coedge_owner.get(id(coedge))
                    if old is not None and old!=i:
                        raise ValueError('Coedge belongs to multiple faces')
                    coedge_owner[id(coedge)]=i
        boundary_faces=[]
        for i,face in enumerate(faces):
            surf=face_surfaces[i]
            face_row={'face_index':i,'surface_type':surf.name,'loops':[]}
            support=surface_feature_by_id.get(id(surf))
            if support is None:
                raise ValueError('Face surface has no decoded analytic support')
            face_row['support']=support
            sense=face.data[6]
            if sense.tag not in (Tags.BOOL_TRUE,Tags.BOOL_FALSE):
                raise ValueError('Explicit ACIS face sense required')
            face_row['reversed']=sense.tag==Tags.BOOL_TRUE
            if surf.name=='plane-surface':
                face_row['outward_normal']=[v*(-1 if face_row['reversed'] else 1) for v in support['normal']]
            for loop in linked(face.data[2].value,1,'loop'):
                edge_rows=[]
                for coedge in linked(loop.data[2].value,1,'coedge',True):
                    edge=coedge.data[4].value
                    curves=[e for e in refs(edge) if e.name.endswith('-curve')]
                    if len(curves)!=1:
                        raise ValueError('Each edge needs one supported analytic curve')
                    curve=curves[0]
                    vertices=[e for e in refs(edge) if e.name=='vertex']
                    if len(vertices)!=2:
                        raise ValueError('Each boundary edge needs two vertices')
                    endpoints=[]
                    for vertex in vertices:
                        point=next((e for e in refs(vertex) if e.name=='point'),None)
                        if point is None or len(point.data)<2:
                            raise ValueError('Boundary vertex has no point')
                        endpoints.append(world(vec(point.data[1]),True))
                    if (len(edge.data)<=6 or edge.data[2].tag!=Tags.DOUBLE
                            or edge.data[4].tag!=Tags.DOUBLE):
                        raise ValueError('Unsupported edge parameter token layout')
                    start=edge.data[2].value
                    end=edge.data[4].value
                    if (not isinstance(start,(int,float)) or isinstance(start,bool)
                            or not isinstance(end,(int,float)) or isinstance(end,bool)
                            or not math.isfinite(start) or not math.isfinite(end)):
                        raise ValueError('Boundary edge parameter interval must be finite')
                    span=end-start
                    if not math.isfinite(span):
                        raise ValueError('Boundary edge parameter span must be finite')
                    partner=coedge.data[3].value
                    partner_index=coedge_owner.get(id(partner))
                    if (partner.name!='coedge' or partner_index is None
                            or partner is coedge or partner.data[3].value is not coedge
                            or partner.data[4].value is not edge):
                        raise ValueError('Boundary coedge partner must belong to a supported face')
                    if coedge.data[5].tag not in [Tags.BOOL_TRUE,Tags.BOOL_FALSE]:
                        raise ValueError('Unsupported coedge sense token')
                    row={'curve_type':curve.name,'start_parameter':start,'end_parameter':end,
                         'parameter_span':span,
                         'full_period_2pi':abs(abs(span)-2*math.pi)<=1e-9,
                         'endpoints':endpoints,'coedge_sense':coedge.data[5].value,
                         'partner_face_index':partner_index,
                         'partner_surface_type':face_surfaces[partner_index].name}
                    if curve.name=='straight-curve':
                        expected=[Tags.POINTER,Tags.LOCATION_VEC,Tags.DIRECTION_VEC,
                                  Tags.BOOL_FALSE,Tags.BOOL_FALSE]
                        if len(curve.data)!=len(expected) or [t.tag for t in curve.data]!=expected:
                            raise ValueError('Unsupported straight-curve token layout')
                        origin=vec(curve.data[1]);direction=vec(curve.data[2])
                        if abs(sum(v*v for v in direction)-1)>1e-8 and edge_policy=='strict':
                            raise ValueError('Straight-curve direction must be unit length')
                        row['line']={'origin':world(origin,True),'direction':world(direction)}
                    elif curve.name=='ellipse-curve':
                        expected=[Tags.POINTER,Tags.LOCATION_VEC,Tags.DIRECTION_VEC,
                                  Tags.DIRECTION_VEC,Tags.DOUBLE,Tags.BOOL_FALSE,Tags.BOOL_FALSE]
                        if len(curve.data)!=len(expected) or [t.tag for t in curve.data]!=expected:
                            raise ValueError('Unsupported ellipse-curve token layout')
                        center=world(vec(curve.data[1]),True)
                        normal=world(vec(curve.data[2]))
                        major_axis=world(vec(curve.data[3]))
                        ratio=curve.data[4].value
                        major_radius=math.sqrt(sum(v*v for v in major_axis))
                        if (not math.isfinite(ratio) or not 0<ratio<=1
                                or not math.isfinite(major_radius) or major_radius<=0
                                or abs(sum(v*v for v in normal)-1)>1e-8
                                or abs(sum(a*b for a,b in zip(normal,major_axis)))>1e-8*max(1.0,major_radius)):
                            raise ValueError('Unsupported or invalid ellipse-curve parameters')
                        row['ellipse']={'center':center,'normal':normal,
                                        'major_axis':major_axis,
                                        'major_radius':major_radius,
                                        'minor_to_major_ratio':ratio,
                                        'minor_radius':major_radius*ratio,
                                        'is_circle':abs(ratio-1)<=1e-9}
                    else:
                        if edge_policy=='strict':raise ValueError('Unsupported boundary curve: '+curve.name)
                        row['representation']='native trim endpoints'
                    edge_rows.append(row)
                face_row['loops'].append({'edge_count':len(edge_rows),'edges':edge_rows})
            boundary_faces.append(face_row)
        out['face_boundary_edges']=boundary_faces
        out['face_boundary_edge_index_scope']='face_index and partner_face_index refer only to rows in this payload'
    out['encoding']='SAB';out['decoder']='ezdxf.acis.sab.parse_sab'
    out['acis_header_units_in_mm']=b.header.units_in_mm
    return out


def _sat_body_entities(parsed):
    bodies = [entity for entity in parsed.entities if entity.name == 'body']
    if len(bodies) != 1:
        raise ValueError('Exactly one native SAT body required')
    body = bodies[0]
    pending = [body]
    reachable = {}
    while pending:
        entity = pending.pop()
        if id(entity) not in reachable:
            reachable[id(entity)] = entity
            pending.extend(ref for ref in entity.data
                           if hasattr(ref, 'name') and ref.name != 'null-ptr')
    return body, list(reachable.values())


def _sat_cone_parameters(tokens, version):
    from ezdxf.acis.sat import SatDataLoader

    loader = SatDataLoader(tokens, version)
    loader.read_ptr()
    origin, axis, major = (list(loader.read_vec3()) for _ in range(3))
    ratio = loader.read_double()
    loader.read_interval()
    loader.read_interval()
    sine, cosine, radius = (loader.read_double() for _ in range(3))
    return origin, axis, major, ratio, sine, cosine, radius


def _sat_curved_surface(name, fields, world):
    """Decode the observed ACIS700 sphere and ring torus support surfaces."""
    if name == 'sphere-surface':
        if len(fields) < 12 or fields[11] not in ('forward_v', 'reverse_v'):
            raise ValueError('Unsupported SAT sphere layout')
        radius = float(fields[4])
        if not math.isfinite(radius) or radius <= 0:
            raise ValueError('Positive finite SAT sphere radius required')
        return {'origin': world(fields[1:4], True), 'radius': radius}
    if name != 'torus-surface' or len(fields) < 13 or fields[12] not in ('forward_v', 'reverse_v'):
        raise ValueError('Unsupported SAT torus layout')
    centre = world(fields[1:4], True)
    axis = world(fields[4:7])
    major, minor = map(float, fields[7:9])
    radial = world(fields[9:12])
    if not math.isfinite(major) or not math.isfinite(minor) or not major > minor > 0:
        raise ValueError('Only positive ring-shaped SAT tori supported')
    if (abs(sum(x*x for x in axis)-1) > 1e-9
            or abs(sum(x*x for x in radial)-1) > 1e-9
            or abs(sum(a*b for a,b in zip(axis,radial))) > 1e-9):
        raise ValueError('SAT torus requires orthonormal axis/reference directions')
    return {'center': centre, 'axis': axis, 'major_radius': major, 'minor_radius': minor}


def sat_readback(data, *, allow_rigid=False, include_cylinders=True, include_cones=False,
                 include_spheres=False, include_tori=False):
    """Read live OCS ACIS700 text topology, vertices and supported curves.

    Unknown edge equations retain their native trim endpoints. Only circular
    cylindrical support surfaces and requested cone, sphere and ring torus surfaces are extracted.
    ACIS header units describe the payload and do not rescale coordinates.
    """
    from ezdxf.acis.sat import SatEntity, parse_sat

    if not isinstance(data, str) or not data.strip():
        raise ValueError('Nonempty native SAT text required')
    parsed = parse_sat(data)
    if parsed.header.version != 700:
        raise ValueError('Observed ACIS700 SAT layout required')
    body, entities = _sat_body_entities(parsed)
    matrix, translation = _sat_transform(body.data[-1], allow_rigid)

    def world(values, point=False):
        vector = [float(value) for value in values]
        if len(vector) != 3 or any(not math.isfinite(v) for v in vector):
            raise ValueError('Finite SAT vector required')
        if matrix is None:
            return vector
        return [
            sum(matrix[j][i] * vector[j] for j in range(3)) +
            (translation[i] if point else 0)
            for i in range(3)
        ]

    points = [_sat_point(entity, world) for entity in entities if entity.name == 'point']
    faces = [entity for entity in entities if entity.name == 'face']
    if not faces or not points:
        raise ValueError('A native SAT body requires faces and vertices')
    coedges = [entity for entity in entities if entity.name == 'coedge']
    closed = bool(coedges) and all(_sat_reciprocal(entity) for entity in coedges)

    # Only face-bound surfaces describe this represented body.
    surfaces = {}
    for face in faces:
        support = [ref for ref in face.data
                   if isinstance(ref, SatEntity) and ref.name.endswith('-surface')]
        if len(support) != 1:
            raise ValueError('Expected one SAT support surface per face')
        surfaces[id(support[0])] = support[0]
    cylinders, cones = [], []
    if include_cylinders or include_cones:
        for surface in surfaces.values():
            if surface.name in ('cone-surface', 'cylinder-surface'):
                feature = _sat_round_surface(surface.data, world, include_cones)
                if feature is None:
                    continue
                if 'sin_angle' in feature:
                    cones.append(feature)
                elif include_cylinders:
                    cylinders.append(feature)
    edges = [_sat_edge(entity, world) for entity in entities if entity.name == 'edge']
    if not edges:
        raise ValueError('Native SAT boundary edges required')
    result = {
        'encoding': 'native SAT ACIS 700',
        'points': points,
        'surface_types': sorted({surface.name for surface in surfaces.values()}),
        'cylinders': cylinders,
        'edges': edges,
        'acis_header_units_in_mm': parsed.header.units_in_mm,
        'topology': {
            'bodies': 1,
            'lumps': sum(entity.name == 'lump' for entity in entities),
            'shells': sum(entity.name == 'shell' for entity in entities),
            'faces': len(faces),
            'coedges': len(coedges),
            'reciprocal_closed_partners': closed,
        },
    }
    if include_cones:
        result['cones'] = cones
    for requested, key, name in ((include_spheres,'spheres','sphere-surface'),
                                 (include_tori,'tori','torus-surface')):
        if requested:
            result[key]=[_sat_curved_surface(name,surface.data,world) for surface in surfaces.values()
                         if surface.name==name]
    if matrix is not None:
        result['body_transform'] = {
            'column_major_rotation': matrix,
            'translation': translation,
            'scale': 1,
        }
    return result


def _sat_transform(transform, allow_rigid):
    if getattr(transform, 'name', None) == 'null-ptr':
        return None, None
    if not allow_rigid:
        raise ValueError('Transformed SAT requires the rigid-frame reader option')
    if getattr(transform, 'name', None) != 'transform' or len(transform.data) != 16:
        raise ValueError('Unsupported SAT body transform')
    values = [float(value) for value in transform.data[:13]]
    if (any(not math.isfinite(value) for value in values) or
            abs(values[12] - 1) > 1e-9 or
            transform.data[-2:] != ['no_reflect', 'no_shear']):
        raise ValueError('Only unit-scale SAT rigid transforms supported')
    rotation = [values[i:i + 3] for i in (0, 3, 6)]
    for i, column in enumerate(rotation):
        if any(abs(sum(a * b for a, b in zip(column, other)) - (i == j)) > 1e-8
               for j, other in enumerate(rotation)):
            raise ValueError('Nonrigid SAT body transform')
    x, y, z = rotation
    determinant = sum(x[i] * (y[(i + 1) % 3] * z[(i + 2) % 3] -
                              y[(i + 2) % 3] * z[(i + 1) % 3]) for i in range(3))
    if abs(determinant - 1) > 1e-8:
        raise ValueError('Reflected or singular SAT body transform unsupported')
    return rotation, values[9:12]


def _sat_reciprocal(coedge):
    if len(coedge.data) < 5:
        return False
    partner, edge = coedge.data[3:5]
    return (getattr(partner, 'name', None) == 'coedge' and partner is not coedge and
            getattr(edge, 'name', None) == 'edge' and len(partner.data) >= 5 and
            partner.data[3] is coedge and partner.data[4] is edge)


def _sat_point(point, world):
    if getattr(point, 'name', None) != 'point':
        raise ValueError('Boundary vertex requires a native SAT point')
    return world(point.data[1:4], point=True)


def _sat_edge(edge, world):
    data = edge.data
    vertices = [data[i] for i in (1, 3)]
    curve = data[6]
    if any(getattr(v, 'name', None) != 'vertex' for v in vertices):
        raise ValueError('Two native SAT edge vertices required')
    curve_type = getattr(curve, 'name', '')
    if not curve_type.endswith('-curve'):
        raise ValueError('Expected a native SAT boundary curve')
    result = {
        'curve_type': curve_type,
        'endpoints': [_sat_point(vertex.data[2], world) for vertex in vertices],
    }
    if curve_type == 'ellipse-curve':
        tokens = curve.data
        start, end, ratio = float(data[2]), float(data[4]), float(tokens[10])
        normal, major = world(tokens[4:7]), world(tokens[7:10])
        if (not all(math.isfinite(v) for v in (start, end, end - start, ratio)) or
                not 0 < ratio <= 1 or math.hypot(*major) <= 0 or
                abs(math.hypot(*normal) - 1) > 1e-8 or
                abs(sum(a * b for a, b in zip(normal, major))) >
                1e-8 * max(1, math.hypot(*major))):
            raise ValueError('Invalid SAT ellipse basis or interval')
        result.update(start_parameter=start, end_parameter=end, ellipse={
            'center': world(tokens[1:4], point=True), 'normal': normal,
            'major_axis': major, 'minor_to_major_ratio': ratio,
        })
    elif curve_type != 'straight-curve':
        result['representation'] = 'native trim endpoints'
    return result


def _sat_round_surface(tokens, world, include_cones):
    origin, axis, major, ratio, sine, cosine, radius = _sat_cone_parameters(tokens, 700)
    if any(not math.isfinite(value) for value in (ratio, sine, cosine, radius)):
        raise ValueError('Nonfinite SAT cone or cylinder parameters')
    if abs(ratio - 1) > 1e-9:
        return None
    is_cone = abs(sine) > 1e-9 or abs(cosine - 1) > 1e-9
    if is_cone and not include_cones:
        return None
    axis = world(axis)
    major = world(major)
    if (radius <= 0 or abs(math.hypot(*major) - radius) > 1e-7 or
            abs(math.hypot(*axis) - 1) > 1e-8):
        raise ValueError('Invalid SAT circular surface axis or radius')
    result = {'origin': world(origin, point=True), 'axis': axis, 'radius': radius}
    if is_cone:
        if (abs(sine) <= 1e-9 or cosine <= 1e-9 or
                abs(sine * sine + cosine * cosine - 1) > 1e-8 or
                abs(sum(a * b for a, b in zip(axis, major))) > 1e-8 * max(1, radius)):
            raise ValueError('Invalid SAT circular cone angle or reference plane')
        result.update(sin_angle=sine, cos_angle=cosine)
    return result


def solid_acis_payload(record):
    """Select the observed Solid3D native record payload without changing it."""
    if record.get('type') != 'Solid3D':
        raise ValueError('Solid3D native record required')
    data = record['properties']['acis_data']
    binary = data.get('is_binary')
    if binary is True or (binary is None and data.get('sab_data')):
        payload = bytes(data['sab_data'])
    elif binary is False or (binary is None and data.get('sat_data')):
        payload = data['sat_data']
        if not isinstance(payload, str):
            raise ValueError('Native text payload must be SAT text')
    else:
        raise ValueError('Unknown native ACIS payload representation')
    if not payload:
        raise ValueError('Nonempty native ACIS payload required')
    return payload
