"""Analytic equal-radius circular clipping and bounded native extrusion (mm)."""
import math
from cadtools.geometry import Geometry,added,positive,vector
from rounded_tube import SelectionCheckedClient
from plate_reference import validate_outline
from profile_reference import validate_profile


def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return [a[0]-b[0],a[1]-b[1]]
def add(a,b):return [a[0]+b[0],a[1]+b[1]]
def scale(a,k):return [a[0]*k,a[1]*k]


def inside(point,poly):
    result=False;x,y=point
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:result=not result
    return result


def line_circle(a,b,c,r,tolerance):
    d=sub(b,a);q=sub(a,c);aa=sum(x*x for x in d)
    if aa==0:raise ValueError('Zero-length stock segment')
    bb=2*sum(x*y for x,y in zip(d,q));cc=sum(x*x for x in q)-r*r
    disc=bb*bb-4*aa*cc
    if disc<0:
        if abs(disc)>tolerance*max(1.,bb*bb,abs(4*aa*cc)):return []
        disc=0
    return sorted(set(max(0,min(1,t)) for t in [(-bb-math.sqrt(disc))/(2*aa),(-bb+math.sqrt(disc))/(2*aa)] if -tolerance<=t<=1+tolerance))


def circles(c,d,r,tolerance):
    delta=sub(d,c);distance=math.hypot(*delta)
    if distance<tolerance:raise ValueError('Coincident circles require source deduplication')
    if distance>2*r+tolerance:return []
    middle=scale(add(c,d),.5);height=math.sqrt(max(0,r*r-distance*distance/4));normal=[-delta[1]/distance,delta[0]/distance]
    return [add(middle,scale(normal,height)),add(middle,scale(normal,-height))]


def rectangular_face_overlap(first, second, *, normal_axis, tolerance):
    """Measure two independently identified rectangular faces in one Cartesian frame.

    Each face is an ordered, hole-free four-corner loop parallel to the chosen
    plane. The return describes projected geometry. The caller establishes
    material side, trim identity and permitted contact conditions.
    """
    positive(tolerance)
    if type(normal_axis) is not int or normal_axis not in (0, 1, 2):
        raise ValueError('Expected an XYZ normal axis index')
    axes = [axis for axis in range(3) if axis != normal_axis]

    def rectangle(loop):
        points = [vector(point) for point in loop]
        if len(points) != 4:
            raise ValueError('Expected four ordered rectangle corners')
        normal = [point[normal_axis] for point in points]
        if max(normal) - min(normal) > tolerance:
            raise ValueError('Rectangle is not parallel to the selected plane')
        spans = [(min(point[axis] for point in points), max(point[axis] for point in points))
                 for axis in axes]
        if any(high - low <= 2 * tolerance for low, high in spans):
            raise ValueError('Rectangle corner assignments are ambiguous')
        corner_ids = []
        for point in points:
            corner = []
            for axis, (low, high) in zip(axes, spans, strict=True):
                value = point[axis]
                if min(abs(value - low), abs(value - high)) > tolerance:
                    raise ValueError('Face has a nonrectangular corner')
                corner.append(int(abs(value - low) > tolerance))
            corner_ids.append(tuple(corner))
        pairs = zip(corner_ids, corner_ids[1:] + corner_ids[:1], strict=True)
        if len(set(corner_ids)) != 4 or any(sum(a != b for a, b in zip(u, v, strict=True)) != 1
                                           for u, v in pairs):
            raise ValueError('Corners do not follow a rectangular perimeter')
        return spans, (min(normal), max(normal))

    first_spans, first_normal = rectangle(first)
    second_spans, second_normal = rectangle(second)
    widths = [max(0, min(hi1, hi2) - max(lo1, lo2))
              for (lo1, hi1), (lo2, hi2) in zip(first_spans, second_spans, strict=True)]
    normal_offset = (sum(second_normal) - sum(first_normal)) / 2
    coplanar = max(*first_normal, *second_normal) - min(*first_normal, *second_normal) <= tolerance
    projected_area = math.prod(widths)
    return dict(in_plane_axes=axes, normal_offset=normal_offset, coplanar=coplanar,
                projected_overlap_lengths=widths, projected_overlap_area=projected_area,
                coplanar_overlap_area=projected_area if coplanar else 0)


def rectangular_opening_perimeters(segments, *, outer_bounds, inner_bounds, tolerance):
    """Check both projected rectangular loops and count straight end-face seams."""
    positive(tolerance)
    outer = [vector(corner, 2) for corner in outer_bounds]
    inner = [vector(corner, 2) for corner in inner_bounds]
    if len(outer) != 2 or len(inner) != 2 or not all(
            outer[0][axis] + 2 * tolerance < inner[0][axis]
            and inner[0][axis] + 2 * tolerance < inner[1][axis]
            and inner[1][axis] + 2 * tolerance < outer[1][axis] for axis in range(2)):
        raise ValueError('Expected two strictly nested, nondegenerate rectangle bounds')

    rectangles = {'outer': outer, 'inner': inner}
    coverage = {(label, axis, side): [] for label in rectangles
                for axis in range(2) for side in range(2)}
    seams = 0
    for first, second in segments:
        a, b = vector(first, 2), vector(second, 2)
        changed = [axis for axis in range(2) if abs(a[axis] - b[axis]) > tolerance]
        if len(changed) != 1:
            raise ValueError('Expected a nonzero axis-parallel end edge')
        along, = changed
        normal = 1 - along
        lo, hi = sorted((a[along], b[along]))
        sides = [(label, normal, side)
                 for label, box in rectangles.items() for side in range(2)
                 if all(abs(point[normal] - box[side][normal]) <= tolerance for point in (a, b))
                 and lo >= box[0][along] - tolerance and hi <= box[1][along] + tolerance]
        if len(sides) == 1:
            coverage[sides[0]].append((lo, hi))
            continue
        within_wall = all(inner[0][normal] - tolerance <= point[normal] <= inner[1][normal] + tolerance
                          for point in (a, b))
        spans_wall = any(abs(lo - wall_lo) <= tolerance and abs(hi - wall_hi) <= tolerance
                         for wall_lo, wall_hi in ((outer[0][along], inner[0][along]),
                                                  (inner[1][along], outer[1][along])))
        if not (within_wall and spans_wall):
            raise ValueError('End edge lies outside the allowed perimeter and wall seams')
        seams += 1

    lengths = {'outer': 0.0, 'inner': 0.0}
    for (label, normal, side), intervals in coverage.items():
        lo, hi = [corner[1 - normal] for corner in rectangles[label]]
        current = lo
        for start, stop in sorted(intervals):
            if abs(start - current) > tolerance or stop <= current:
                raise ValueError(f'{label} perimeter has a gap or overlapping edges')
            current = stop
            lengths[label] += stop - start
        if abs(current - hi) > tolerance:
            raise ValueError(f'{label} perimeter has an incomplete side')
    return dict(edge_lengths=lengths, wall_seam_count=seams)


def conservative_tool_polygon(source, *, margin, tolerance, max_vertices, max_added_area, quad_segs=2):
    """Simplify a caller-provided planar clearance/tool polygon with bounded enlargement."""
    positive(margin);positive(tolerance);positive(max_added_area)
    if type(max_vertices) is not int or max_vertices < 3:
        raise ValueError('At least three cutter vertices required')
    if type(quad_segs) is not int or quad_segs < 1:
        raise ValueError('Positive buffer segment count required')
    if source.geom_type != 'Polygon' or not source.is_valid or source.is_empty or source.interiors:
        raise ValueError('Source must be one valid planar polygon without holes')
    candidate = source.buffer(margin,quad_segs=quad_segs).simplify(tolerance,preserve_topology=True)
    if (candidate.geom_type != 'Polygon' or not candidate.is_valid or candidate.is_empty
            or candidate.interiors or not candidate.covers(source)):
        raise ValueError('Reduced tool must fully contain the source clearance profile')
    vertex_count = len(candidate.exterior.coords)-1
    if vertex_count > max_vertices:
        raise ValueError('Reduced tool exceeds the declared vertex limit')
    added_area = candidate.area-source.area
    if not math.isfinite(added_area) or not 0 <= added_area <= max_added_area:
        raise ValueError('Reduced tool exceeds the permitted area growth')
    return candidate


def clip_circular_openings(poly,centres,radius,*,tolerance):
    """Return exact line/arc loops for polygon stock minus equal-radius disks."""
    poly=validate_profile(poly);r=positive(radius);positive(tolerance)
    centres=[vector(c,2) for c in centres]
    if sum(cross(a,b) for a,b in zip(poly,poly[1:]+poly[:1]))<0:poly.reverse()
    for i,c in enumerate(centres):
        if any(math.dist(c,d)<=tolerance for d in centres[:i]):raise ValueError('Coincident opening centres')
    edges=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        params=sorted(set([0,1]+[t for c in centres for t in line_circle(a,b,c,r,tolerance)]))
        for lo,hi in zip(params,params[1:]):
            if hi-lo<tolerance:continue
            delta=sub(b,a);mid=add(a,scale(delta,(lo+hi)/2))
            if all(math.dist(mid,c)>=r-tolerance for c in centres):
                edges.append(dict(a=add(a,scale(delta,lo)),b=add(a,scale(delta,hi)),bulge=0,curve='stock line'))
    for index,c in enumerate(centres):
        angles=[0.,math.pi]
        for a,b in zip(poly,poly[1:]+poly[:1]):
            for t in line_circle(a,b,c,r,tolerance):
                p=add(a,scale(sub(b,a),t));angles.append(math.atan2(p[1]-c[1],p[0]-c[0])%(2*math.pi))
        for other,d in enumerate(centres):
            if other!=index:angles.extend(math.atan2(p[1]-c[1],p[0]-c[0])%(2*math.pi) for p in circles(c,d,r,tolerance))
        angles=sorted(set(round(x,13) for x in angles))
        for lo,hi in zip(angles,angles[1:]+[angles[0]+2*math.pi]):
            if hi-lo<tolerance:continue
            mid=add(c,[r*math.cos((lo+hi)/2),r*math.sin((lo+hi)/2)])
            if inside(mid,poly) and all(other==index or math.dist(mid,d)>=r-tolerance for other,d in enumerate(centres)):
                a=add(c,[r*math.cos(hi),r*math.sin(hi)]);b=add(c,[r*math.cos(lo),r*math.sin(lo)])
                edges.append(dict(a=a,b=b,bulge=math.tan((lo-hi)/4),curve='circular access arc',centre_mm=c,radius_mm=r))
    remaining=edges[:];loops=[]
    while remaining:
        loop=[remaining.pop(0)]
        while math.dist(loop[-1]['b'],loop[0]['a'])>tolerance:
            options=[(i,e) for i,e in enumerate(remaining) if math.dist(e['a'],loop[-1]['b'])<=tolerance]
            if len(options)!=1:raise ValueError('Open or ambiguous analytic boundary')
            i,edge=options[0];remaining.pop(i);loop.append(edge)
        area=sum(cross(e['a'],e['b'])/2 for e in loop)
        for e in loop:
            if e['bulge']:
                angle=4*math.atan(e['bulge']);area+=r*r*(angle-math.sin(angle))/2
        if abs(area)<=tolerance:raise ValueError('Degenerate analytic loop')
        loops.append(dict(points_mm=[e['a'] for e in loop],bulges={i:e['bulge'] for i,e in enumerate(loop) if e['bulge']},segments=loop,signed_area_mm2=area,boundary_role='outer' if area>0 else 'opening'))
    return loops


def bounded_extrusion(client, boundaries, pickpoint, height, *, label, checkpoint=None):
    """Extrude a bounded region and optionally persist each completed native stage.

    The checkpoint callback receives a stage label and the owned handles still
    present in the drawing. Raise on an unsuccessful or uncertain save to stop
    before any subsequent geometry change.
    """
    positive(height)
    vector(pickpoint)
    if not boundaries:
        raise ValueError('Boundaries required')
    if checkpoint is not None and not callable(checkpoint):
        raise TypeError('Checkpoint must be callable')
    prepared = [validate_outline(b['points'], b.get('bulges')) for b in boundaries]
    geometry = Geometry(SelectionCheckedClient(client))
    initial = client.read('query', limit=1000)
    if initial.get('next_offset') is not None:
        raise ValueError('Bounded preflight query requires narrower scope')
    before = {row['handle'] for row in initial['entities']}
    profiles = []
    for index, (points, bulges) in enumerate(prepared):
        stage = f'{label}-boundary-{index}'
        profiles.append(geometry.profile(stage, points, bulges))
        if checkpoint is not None:
            checkpoint(stage, tuple(profiles))
    geometry.select(label + '-clear', [])
    response = client.mutate(
        label + '-bounded', 'run',
        cmd='PRESSPULL ' + ','.join(str(value) for value in pickpoint) + ' ' + str(height),
    )
    rows = client.read('query', limit=1000)
    if rows.get('next_offset') is not None:
        raise ValueError('Bounded result query requires narrower scope')
    created = [
        row['handle'] for row in rows['entities']
        if row['type'] == '3D Solid' and row['handle'] not in before
    ]
    if len(created) != 1:
        raise ValueError('Expected one newly created bounded solid')
    body = created[0]
    present = {row['handle'] for row in rows['entities']}
    retained = [handle for handle in profiles if handle in present]
    if checkpoint is not None:
        checkpoint(label + '-solid', (body, *retained))
    if retained:
        client.mutate(label + '-owned-profiles', 'entities_delete', handles=retained)
        if checkpoint is not None:
            checkpoint(label + '-profiles-cleared', (body,))
    return dict(body=body, profiles=profiles, request_id=response.get('request_id'))


def revolve_profile_y(client, points, *, label, checkpoint, bulges=None):
    """Revolve an owned planar profile about Y, saving each completed stage.

    The caller supplies a valid radial section, preflighted in the local XY
    frame. The checkpoint receives a stage name and the owned live handles.
    It must raise if persistence fails or remains uncertain.
    """
    if not callable(checkpoint):
        raise TypeError('A revolve checkpoint callback is required')
    section, curves = validate_outline(points, bulges)
    geometry = Geometry(SelectionCheckedClient(client))
    profile = geometry.profile(label + '-section', section, curves)
    checkpoint(label + '-section', (profile,))
    geometry.select(label + '-select-section', [profile])
    response = geometry.run(label + '-revolve', 'REVOLVE Y 360')
    body = added(response)
    observed = client.read('query', limit=1000)
    if observed.get('next_offset') is not None:
        raise ValueError('Revolve result query requires narrower scope')
    kinds = {row['handle']: row['type'] for row in observed['entities']}
    if profile == body or kinds.get(body) != '3D Solid':
        raise ValueError('Expected one newly revolved solid')
    if profile in kinds:
        checkpoint(label + '-solid', (body, profile))
        client.mutate(label + '-erase-section', 'entities_delete', handles=[profile])
        checkpoint(label + '-section-cleared', (body,))
    else:
        checkpoint(label + '-solid', (body,))
    return dict(body=body, profile=profile, request_id=response.get('request_id'))
