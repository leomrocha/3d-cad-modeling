"""Analytic equal-radius circular clipping and bounded native extrusion (mm)."""
import math
from cadtools.geometry import Geometry,added,finite,positive,vector
from cadtools.runtime import CadError
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



def straight_profile_station_intervals(vertices, station, *, axis=0, tolerance=1e-6):
    """Return material intervals along a section of one straight-edged loop.

    Pass vertices in original connected order and one caller-selected section
    station on the chosen axis. Intervals use the other axis. Stations within
    tolerance of a vertex require a separately qualified edge or vertex case.
    """
    if type(axis) is not int or axis not in (0, 1):
        raise ValueError("Section axis must be 0 or 1")
    station = finite(station)
    tolerance = positive(tolerance)
    polygon = validate_profile(vertices)
    offsets = [p[axis] - station for p in polygon]
    if any(abs(value) <= tolerance for value in offsets):
        raise ValueError("Section station meets a profile vertex within tolerance")

    transverse = 1 - axis
    crossings = []
    for i, first in enumerate(polygon):
        j = (i + 1) % len(polygon)
        if (offsets[i] < 0) == (offsets[j] < 0):
            continue
        second = polygon[j]
        fraction = offsets[i] / (offsets[i] - offsets[j])
        crossings.append(first[transverse] + fraction * (second[transverse] - first[transverse]))
    crossings.sort()
    if len(crossings) % 2 or any(b - a <= tolerance for a, b in zip(crossings, crossings[1:])):
        raise ValueError("Section crossings are ambiguous at the requested tolerance")
    return list(zip(crossings[::2], crossings[1::2], strict=True))


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


def round_ended_slot_profile(width, first, last):
    """Return a closed XY slot with exact semicircle bulges, centred on X = 0."""
    half = positive(width) / 2
    first, last = finite(first), finite(last)
    lower_centre, upper_centre = first + half, last - half
    if lower_centre >= upper_centre:
        raise ValueError('Round-ended slot length must exceed its width')
    points = [[-half,lower_centre], [half,lower_centre],
              [half,upper_centre], [-half,upper_centre]]
    return points, {0:1, 2:1}


def _two_circle_frame(first, second, r0, r1):
    x0, y0 = first
    x1, y1 = second
    dx, dy = x1 - x0, y1 - y0
    distance = math.hypot(dx, dy)
    if not math.isfinite(distance) or distance <= abs(r0 - r1):
        raise ValueError('Two distinct external tangents require separated centres and non-contained circles')
    axis = (dx / distance, dy / distance)
    transverse = (-axis[1], axis[0])
    axial = (r0 - r1) / distance
    lateral = math.sqrt((1 - axial) * (1 + axial))
    low = tuple(axial * u - lateral * v for u, v in zip(axis, transverse, strict=True))
    high = tuple(axial * u + lateral * v for u, v in zip(axis, transverse, strict=True))
    return axis, axial, low, high


def two_circle_tangent_hull(first, second, first_radius, second_radius):
    """Return a counterclockwise exact bulged hull of two planar circles."""
    a, b = (tuple(finite(value) for value in centre) for centre in (first, second))
    r0, r1 = positive(first_radius), positive(second_radius)
    axis, axial, low, high = _two_circle_frame(a, b, r0, r1)

    def point(centre, radius, direction):
        return [value + radius * component for value, component in zip(centre, direction, strict=True)]

    points = [point(a, r0, low), point(b, r1, low), point(b, r1, axis),
              point(b, r1, high), point(a, r0, high), point(a, r0, tuple(-v for v in axis))]
    second_half_angle = math.acos(axial)
    first_bulge = math.tan((math.pi - second_half_angle) / 4)
    second_bulge = math.tan(second_half_angle / 4)
    return validate_outline(points, {1:second_bulge, 2:second_bulge, 4:first_bulge, 5:first_bulge})


def two_circle_band_box_clearance(bounds, centres, inner_radii, outer_radii, *, tolerance=1e-6):
    """Screen a planar box against nested two-circle tangent hulls.

    Bounds and both hulls share one Cartesian frame and length unit. A
    positive result proves separation for the supplied box representation.
    No separation certificate means a candidate, including possible contact.
    """
    points = tuple(tuple(finite(value) for value in c) for c in centres)
    inners = tuple(positive(r) for r in inner_radii)
    outers = tuple(positive(r) for r in outer_radii)
    if any(a >= b for a,b in zip(inners,outers,strict=True)):
        raise ValueError('The outer radius must exceed the inner radius at each centre')
    (x0,y0),(x1,y1) = (tuple(finite(value) for value in corner) for corner in bounds)
    if x0 > x1 or y0 > y1:
        raise ValueError('Expected increasing planar box bounds')
    tolerance = positive(tolerance)
    corners = [(x,y) for x in (x0,x1) for y in (y0,y1)]
    axis, axial, *inner_normals = _two_circle_frame(*points,*inners)
    _, _, *outer_normals = _two_circle_frame(*points,*outers)

    def dot(a,b):
        return a[0]*b[0] + a[1]*b[1]

    def support(normal, radii):
        return max(dot(normal,centre) + radius for centre,radius in zip(points,radii,strict=True))

    def inner_violation(point):
        # Each circle provides the support on one angular interval delimited
        # by the common tangents. Its unconstrained radial maximum may lie
        # inside that interval, otherwise an endpoint supplies the maximum.
        values = [dot(n,point)-support(n,inners) for n in inner_normals]
        for i,(centre,radius) in enumerate(zip(points,inners,strict=True)):
            delta = (point[0]-centre[0], point[1]-centre[1])
            length = math.hypot(*delta)
            projection = dot(delta,axis) - axial*length
            if (i == 0 and projection <= 0) or (i == 1 and projection >= 0):
                values.append(length-radius)
        return max(values)

    inner_gap = -max(map(inner_violation,corners))
    if inner_gap > tolerance:
        return dict(result='INSIDE_INNER_HULL',gap_lower_bound=inner_gap)

    outer_normals.extend(((1,0),(-1,0),(0,1),(0,-1)))
    for x,y in points:
        nearest = (min(max(x,x0),x1),min(max(y,y0),y1))
        for a,b in (*corners,nearest):
            length = math.hypot(a-x,b-y)
            if length:
                outer_normals.append(((a-x)/length,(b-y)/length))
    outer_gap = max(min(dot(n,p) for p in corners)-support(n,outers) for n in outer_normals)
    if outer_gap > tolerance:
        return dict(result='OUTSIDE_OUTER_HULL',gap_lower_bound=outer_gap)
    return dict(result='CANDIDATE',gap_lower_bound=None)


def reframe_planar_profile(points, bulges, *, origin, u_axis, v_axis):
    """Map a closed bulged outline between perpendicular cardinal frames."""
    x0, y0 = (finite(value) for value in origin)
    ux, uy = (finite(value) for value in u_axis)
    vx, vy = (finite(value) for value in v_axis)
    if (any(value not in (-1, 0, 1) for value in (ux, uy, vx, vy))
            or abs(ux) + abs(uy) != 1 or abs(vx) + abs(vy) != 1
            or ux * vx + uy * vy != 0):
        raise CadError("Planar frame axes must be perpendicular signed cardinal axes")
    source, curves = validate_outline(points, bulges)
    determinant = ux * vy - uy * vx
    mapped = [[x0 + ux * u + vx * v, y0 + uy * u + vy * v] for u, v in source]
    return validate_outline(mapped, {index: determinant * b for index, b in curves.items()})


def quarter_bend_section(centre, inside_radius, thickness, upright_length, floor_length):
    """Return a lower-left quarter bend with tangent legs up and to the right.

    The lengths exclude the bend and are measured from their respective
    tangent stations. The closed result uses two exact quarter-circle bulges.
    """
    x, y = (finite(value) for value in centre)
    inner = positive(inside_radius)
    wall = positive(thickness)
    upright = positive(upright_length)
    floor = positive(floor_length)
    outer = inner + wall
    if not x - outer < x - inner < x < x + floor or not y - outer < y - inner < y < y + upright:
        raise CadError("Quarter bend dimensions collapse in the supplied coordinates")
    coordinates = [
        [x - outer, y + upright],
        [x - outer, y],
        [x, y - outer],
        [x + floor, y - outer],
        [x + floor, y - inner],
        [x, y - inner],
        [x - inner, y],
        [x - inner, y + upright],
    ]
    quarter = math.tan(math.pi / 8)
    return validate_outline(coordinates, {1: quarter, 5: -quarter})


def offset_bend_section(lower_centre, inside_radius, thickness, bridge_length,
                        lower_leg_length, upper_leg_length):
    """Return a Z section with two opposing 90-degree bends.

    The lower straight leg extends downward, the web runs right, and the
    upper straight leg extends upward. Straight lengths start at tangencies.
    """
    x0, y0 = (finite(value) for value in lower_centre)
    inner = positive(inside_radius)
    wall = positive(thickness)
    bridge = positive(bridge_length)
    lower = positive(lower_leg_length)
    upper = positive(upper_leg_length)
    outer = inner + wall
    x1, y1 = x0 + bridge, y0 + inner + outer
    if (not x0 - outer < x0 - inner < x0 < x1 < x1 + inner < x1 + outer
            or not y0 - lower < y0 < y0 + inner < y0 + outer < y1 < y1 + upper):
        raise CadError("Offset bend dimensions collapse in the supplied coordinates")
    outline = [
        [x0 - outer, y0 - lower], [x0 - inner, y0 - lower],
        [x0 - inner, y0], [x0, y0 + inner],
        [x1, y0 + inner], [x1 + outer, y1],
        [x1 + outer, y1 + upper], [x1 + inner, y1 + upper],
        [x1 + inner, y1], [x1, y0 + outer],
        [x0, y0 + outer], [x0 - outer, y0],
    ]
    quarter = math.tan(math.pi / 8)
    return validate_outline(outline, {2: -quarter, 4: quarter, 8: -quarter, 10: quarter})


def ellipse_arc_chord_error_bound(major_radius, parameter_step_radians):
    """Bound the planar deviation between an ellipse arc and its sample chord."""
    radius = positive(major_radius)
    step = positive(parameter_step_radians)
    if step > math.pi:
        raise CadError('Sample parameter step must be at most pi radians')
    return radius * (2 * math.sin(step/4)**2)



def rolling_corner_offset(vertices, vertex_index, radius, exit_normal, *, max_chord_error):
    """Return a round body's centre arc from an incoming straight support edge.

    The ordered polygon has no holes. The exit normal must lie in the outer
    normal cone of the selected convex vertex. The returned error bounds the
    deviation of the joined chords from the continuous centre arc.
    """
    polygon = validate_profile(vertices)
    if type(vertex_index) is not int or not 0 <= vertex_index < len(polygon):
        raise ValueError("A valid profile corner index is required")
    radius, limit = positive(radius), positive(max_chord_error)
    if limit >= radius:
        raise ValueError("Chord error must be smaller than the rolling radius")

    vertex = polygon[vertex_index]
    relative = [sub(point, vertex) for point in polygon]
    area = sum(cross(a, b) for a, b in zip(relative, relative[1:] + relative[:1], strict=True))
    winding = 1 if area > 0 else -1

    def unit(values):
        u, v = vector(values, 2)
        length = math.hypot(u, v)
        if length == 0:
            raise ValueError("A nonzero normal or edge direction is required")
        return [u / length, v / length]

    def outward(tangent):
        u, v = unit(tangent)
        return [winding * v, -winding * u]

    incoming = outward(sub(vertex, polygon[vertex_index - 1]))
    outgoing = outward(sub(polygon[(vertex_index + 1) % len(polygon)], vertex))
    exit_unit = unit(exit_normal)

    def dot(a, b):
        return sum(x * y for x, y in zip(a, b, strict=True))

    def offset_angle(target):
        return winding * math.atan2(cross(incoming, target), dot(incoming, target))

    cone, angle = offset_angle(outgoing), offset_angle(exit_unit)
    if not 0 < angle <= cone + 1e-12 or not 0 < cone < math.pi:
        raise ValueError("Exit normal must advance within a convex corner's outer cone")
    epsilon = max(1.0, max(math.hypot(*point) for point in relative)) * 1e-12
    if any(dot(n, point) > epsilon for point in relative for n in (incoming, exit_unit)):
        raise ValueError("Both endpoint normals must support the entire profile")
    step_limit = 4 * math.asin(math.sqrt(0.5 * (limit / radius)))
    if step_limit < angle / 4096:
        raise ValueError("Requested chord bound requires more than 4096 intervals")
    count = math.ceil(angle / step_limit)
    step = angle / count
    heading = math.atan2(incoming[1], incoming[0])
    centres = [[vertex[0] + radius * math.cos(heading + winding * step * i),
                vertex[1] + radius * math.sin(heading + winding * step * i)]
               for i in range(count + 1)]
    return dict(centre_points=centres, chord_error=ellipse_arc_chord_error_bound(radius, step))


def annular_seat_with_radial_slot(inner_radius, outer_radius, slot_width, slot_radial_end):
    """Projected annulus left by one centred radial slot reaching from the inner bore."""
    r, outer, half = positive(inner_radius), positive(outer_radius), positive(slot_width)/2
    end = positive(slot_radial_end)
    if not half < r <= end or math.hypot(half,end) > outer:
        raise ValueError('Slot must cross the inner arc and end inside the outer circle')
    annulus = math.pi*(outer**2-r**2)
    inner_arc_area = half*math.sqrt(r**2-half**2)+r**2*math.asin(half/r)
    removed = 2*half*end-inner_arc_area
    return dict(annulus_area_mm2=annulus,removed_area_mm2=removed,projected_overlap_mm2=annulus-removed)


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
