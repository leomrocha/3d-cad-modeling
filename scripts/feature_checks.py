"""Reusable comparisons on measured native features, independent of part names.

Callers supply expected dimensions/positions from their pinned source job.
Vertex extrema describe the observed vertices; they are not general bounds
for an arbitrary curved surface between those vertices.
"""
import math


def comparison(name,actual,expected,tolerance,unit='mm',method='native feature comparison'):
    if not math.isfinite(tolerance) or tolerance<=0:raise ValueError('Positive finite numerical threshold required')
    def flat(x):
        if isinstance(x,(list,tuple)):return [v for y in x for v in flat(y)]
        if isinstance(x,bool) or not isinstance(x,(float,int)) or not math.isfinite(x):raise ValueError('Finite numeric observations required')
        return [x]
    a,b=flat(actual),flat(expected)
    if not b:raise ValueError('Nonempty expected measurements required')
    return dict(check=name,observed=actual,expected=expected,numeric_tolerance=tolerance,unit=unit,method=method,
                result='PASS' if len(a)==len(b) and all(abs(x-y)<=tolerance for x,y in zip(a,b)) else 'FAIL')


def axis_aligned_edge_coverage(segments, *, decimal_places):
    """Return the covered intervals for straight Cartesian boundary segments.

    Supply native straight-edge endpoints in one checked frame and length
    unit. Round only at the job's stated comparison precision. Coincident,
    touching or overlapping segments on the same line share one interval.
    """
    if type(decimal_places) is not int or decimal_places < 0:
        raise ValueError("Nonnegative decimal place count required")
    supports = {}
    for segment in segments:
        if len(segment) != 2 or any(len(point) != 3 for point in segment):
            raise ValueError("Two Cartesian points required per segment")
        if any(type(value) not in (int, float) or not math.isfinite(value)
               for point in segment for value in point):
            raise ValueError("Finite coordinates required")
        a, b = (tuple(round(value, decimal_places) for value in point) for point in segment)
        axes = [i for i in range(3) if a[i] != b[i]]
        if len(axes) != 1:
            raise ValueError("Nonzero axis-aligned edge required at the specified precision")
        axis, = axes
        support = (axis, *(value for i, value in enumerate(a) if i != axis))
        supports.setdefault(support, []).append(tuple(sorted((a[axis], b[axis]))))
    if not supports:
        raise ValueError("At least one segment required")
    coverage = {}
    for support, intervals in supports.items():
        merged = []
        for low, high in sorted(intervals):
            if merged and low <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], high))
            else:
                merged.append((low, high))
        coverage[support] = tuple(merged)
    return coverage


def axial_datum_chain(name, stations, offsets, tolerance):
    """Check each signed source distance between successive observed positions."""
    if len(stations)<2 or len(offsets)!=len(stations)-1:
        raise ValueError('One signed offset per successive station pair required')
    comparison(name+' stations',stations,stations,tolerance)
    observed = [b-a for a,b in zip(stations[:-1],stations[1:],strict=True)]
    result = comparison(name,observed,offsets,tolerance,
                        method='Independent signed dimensions between successive axial datums')
    result['observed_stations'] = list(stations)
    return result


def circular_opening_edge_land(centre, radius, side_planes):
    """Return signed lands beside a circle between two parallel side planes.

    All coordinates share one length unit. The planes are perpendicular to
    the declared transverse coordinate and the circle lies in a face along
    that coordinate. A negative land denotes breakout at that plane.
    """
    if len(side_planes)!=2:
        raise ValueError('Two side plane coordinates required')
    low, high = side_planes
    for value in (centre, radius, low, high):
        if type(value) not in (float, int) or not math.isfinite(value):
            raise ValueError('Finite coordinates and radius required')
    if low>=high or radius<=0:
        raise ValueError('Ordered side planes and positive radius required')
    low_land = centre-low-radius
    high_land = high-centre-radius
    if not math.isfinite(low_land) or not math.isfinite(high_land):
        raise ValueError('Edge land cannot be represented with finite coordinates')
    return dict(low=low_land, high=high_land, minimum=min(low_land, high_land))


def perpendicular_through_bore(name, *, shaft_axis, shaft_centre, shaft_radius, shaft_stations,
                                 bore_axis, bore_centre, bore_radius, cutter_stations, tolerance):
    """Screen a centred perpendicular through bore in one Cartesian frame.

    Each centre lists the coordinates orthogonal to its own axis in X/Y/Z
    order. Cutter stations describe the full finite cutter, including overrun.
    Read back the cut cylinder and its exit trims after construction.
    """
    axes = (shaft_axis, bore_axis)
    if any(type(axis) is not int or axis not in (0, 1, 2) for axis in axes) or shaft_axis == bore_axis:
        raise ValueError("Two distinct Cartesian axes required")
    if len(shaft_centre) != 2 or len(bore_centre) != 2 or len(cutter_stations) != 2:
        raise ValueError("Two centre coordinates per axis and two cutter stations required")
    dimensions = [shaft_centre, bore_centre, shaft_radius, bore_radius, cutter_stations]
    comparison(name + " inputs", dimensions, dimensions, tolerance)
    if shaft_radius <= 0 or bore_radius <= 0 or cutter_stations[0] >= cutter_stations[1]:
        raise ValueError("Positive radii and increasing cutter stations required")

    shaft = dict(zip((axis for axis in range(3) if axis != shaft_axis), shaft_centre, strict=True))
    bore = dict(zip((axis for axis in range(3) if axis != bore_axis), bore_centre, strict=True))
    remaining_axis, = shaft.keys() & bore.keys()
    misalignment = bore[remaining_axis] - shaft[remaining_axis]
    axial_land = circular_opening_edge_land(bore[shaft_axis], bore_radius, shaft_stations)
    transverse_land = shaft_radius - bore_radius - abs(misalignment)
    required = [shaft[bore_axis] - shaft_radius, shaft[bore_axis] + shaft_radius]
    cutter_overrun = [required[0] - cutter_stations[0], cutter_stations[1] - required[1]]
    passes = (abs(misalignment) <= tolerance and axial_land["minimum"] > tolerance
              and transverse_land > tolerance and min(cutter_overrun) >= -tolerance)
    return dict(check=name, result="PASS" if passes else "FAIL", common_axis_offset=misalignment,
                remaining_end_land=axial_land, remaining_transverse_land=transverse_land,
                required_cutter_stations=required, observed_cutter_stations=list(cutter_stations),
                cutter_overrun=cutter_overrun, numeric_tolerance=tolerance)


def concentric_through_keyway_section(bore_diameter, outer_diameter, width, radial_depth):
    """Return nominal section datums for a rectangular +Y keyway in a centred bore."""
    inputs = (bore_diameter, outer_diameter, width, radial_depth)
    if any(type(value) not in (int, float) or not math.isfinite(value) or value<=0 for value in inputs):
        raise ValueError('Positive finite keyway section dimensions required')
    if not width < bore_diameter < outer_diameter:
        raise ValueError('Expected keyway width < bore diameter < outer diameter')
    bore_radius, outer_radius, half_width = bore_diameter/2, outer_diameter/2, width/2
    fraction = half_width/bore_radius
    mouth = bore_radius*math.sqrt((1-fraction)*(1+fraction))
    floor = bore_radius+radial_depth
    roof = outer_radius-math.hypot(half_width,floor)
    if not all(math.isfinite(value) for value in (mouth,floor,roof)):
        raise ValueError('Keyway section cannot be represented with finite dimensions')
    return dict(half_width=half_width,mouth_from_axis=mouth,floor_from_axis=floor,
                minimum_radial_wall=roof)


def closed_body(name,features):
    t=features['topology']
    return comparison(name,[t['bodies'],t['lumps'],t['shells'],int(t['reciprocal_closed_partners'])],[1,1,1,1],1e-9,'count','native connected body and reciprocal coedge graph')


def vertex_extrema(name,features,expected,tolerance):
    points=features['points']
    if not points:raise ValueError('Native vertex observations required')
    return comparison(name,[[min(p[i] for p in points),max(p[i] for p in points)] for i in range(3)],expected,tolerance,
                      method='native vertex coordinate extrema')


def cylinder_pattern(name,features,diameter,axis,centres,tolerance):
    comparison(name+' tolerance', [0], [0], tolerance)
    if type(axis) is not int or axis not in [0,1,2] or isinstance(diameter,bool) or not math.isfinite(diameter) or diameter<=0:
        raise ValueError('Positive finite diameter and Cartesian axis required')
    if not centres or any(len(p)!=2 or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in p) for p in centres):
        raise ValueError('Nonempty finite expected axis centres required')
    coordinates=[i for i in range(3) if i!=axis];positions=[]
    for c in features['cylinders']:
        comparison(name+' native cylinder', [c['radius']]+list(c['axis'])+list(c['origin']),
                   [c['radius']]+list(c['axis'])+list(c['origin']), tolerance)
        if abs(c['radius']*2-diameter)>tolerance or abs(abs(c['axis'][axis])-1)>tolerance:continue
        if any(abs(c['axis'][i])>tolerance for i in coordinates):continue
        point=[c['origin'][i] for i in coordinates]
        if not any(all(abs(a-b)<=tolerance for a,b in zip(point,p)) for p in positions):positions.append(point)
    result=comparison(name,sorted(positions),sorted([list(p) for p in centres]),tolerance,
                      method='native circular cylinders; coincident patches deduplicated; one-to-one coordinate tolerance matching')
    remaining=list(range(len(result['observed'])));pairs=[]
    for expected in result['expected']:
        candidates=[i for i in remaining if all(abs(a-b)<=tolerance for a,b in zip(result['observed'][i],expected))]
        if len(candidates)!=1:break
        i=candidates[0];remaining.remove(i)
        pairs.append(dict(observed=result['observed'][i],expected=expected))
    result.update(result='PASS' if len(pairs)==len(centres) and not remaining else 'FAIL',matched_pairs=pairs)
    return result


def circular_trim_stations(name, points, *, axis, centres, radius, stations, tolerance):
    """Check observed ring samples on requested axial stations in a Cartesian frame."""
    if type(axis) is not int or axis not in (0,1,2):
        raise ValueError('Cartesian ring axis required')
    if not centres or any(len(centre)!=2 for centre in centres) or not stations:
        raise ValueError('Expected ring centres and stations required')
    if radius <= 0 or tolerance >= radius/2:
        raise ValueError('Positive ring radius and a smaller geometric tolerance required')
    expected = [radius, list(stations), list(centres)]
    comparison(name+' inputs',expected,expected,tolerance)
    if not points or any(len(p)!=3 for p in points):
        raise ValueError('Observed XYZ boundary samples required')
    comparison(name+' points',points,points,tolerance)
    transverse = [i for i in range(3) if i != axis]
    records = []
    for centre in centres:
        for station in stations:
            vectors = {(p[transverse[0]]-centre[0],p[transverse[1]]-centre[1])
                       for p in points if abs(p[axis]-station)<=tolerance
                       and abs(math.hypot(p[transverse[0]]-centre[0],
                                          p[transverse[1]]-centre[1])-radius)<=tolerance}
            signs = {(x>0,y>0) for x,y in vectors if abs(x)>tolerance and abs(y)>tolerance}
            records.append(dict(centre=list(centre),station=station,sample_count=len(vectors),
                                passed=len(vectors)>=8 and len(signs)==4))
    return dict(check=name,result='PASS' if all(r['passed'] for r in records) else 'FAIL',
                numeric_tolerance=tolerance, method='Distributed native circular boundary samples',
                rings=records)


def round_ended_slot_tangents(name, edges, *, axis, centres, radius, stations, tolerance):
    """Match the two native straight tangents at each requested slot rim."""
    if type(axis) is not int or axis not in (0,1,2) or len(centres)!=2 or not stations:
        raise ValueError('Expected one Cartesian axis, two slot centres and stations')
    if any(len(centre)!=2 for centre in centres) or radius<=0 or tolerance>=radius/2:
        raise ValueError('Expected finite planar centres and a positive slot radius')
    expected=[list(centres),list(stations),radius]
    comparison(name+' inputs',expected,expected,tolerance)
    first,second=centres
    dx,dy=(second[i]-first[i] for i in range(2))
    spacing=math.hypot(dx,dy)
    if spacing<=2*tolerance:
        raise ValueError('Slot centres must be distinct at the declared tolerance')
    normal=(-dy/spacing,dx/spacing)
    straight=[]
    for edge in edges:
        if edge['curve_type']!='straight-curve' or edge.get('endpoints_only'):
            continue
        points=edge['points']
        if len(points)!=2 or any(len(p)!=3 for p in points):
            raise ValueError('Expected two XYZ endpoints for each straight edge')
        comparison(name+' edge',points,points,tolerance)
        straight.append(points)

    records=[]
    for station in stations:
        for side in (-1,1):
            targets=[]
            for centre in centres:
                xyz=[v+side*radius*n for v,n in zip(centre,normal,strict=True)]
                xyz.insert(axis,station)
                targets.append(xyz)
            match=any(all(math.dist(a,b)<=tolerance for a,b in zip(pair,targets,strict=True))
                      for edge in straight for pair in (edge,edge[::-1]))
            records.append(dict(station=station,side=side,expected_endpoints=targets,passed=match))
    return dict(check=name,result='PASS' if all(r['passed'] for r in records) else 'FAIL',
                numeric_tolerance=tolerance,tangents=records)


def cylinder_wall_checks(name, faces, *, axis, centre, radius, side, outer, inner_limit, tolerance):
    """Check actual cylinder-face boundary vertices on one declared sidewall (mm)."""
    if type(axis) is not int or axis not in (0,1,2) or side not in (-1,1):
        raise ValueError('Cartesian axis and side sign required')
    comparison(name+' input',list(centre)+[radius,outer,inner_limit],list(centre)+[radius,outer,inner_limit],tolerance)
    if len(centre)!=2 or not 0<inner_limit<outer or radius<=0:raise ValueError('Invalid wall dimensions')
    coords=[i for i in range(3) if i!=axis];matches=[]
    for face in faces:
        support=face['support'];points=[p for loop in face['loops'] for edge in loop['edges'] for p in edge['endpoints']]
        if face['surface_type']!='cone-surface' or 'sin_angle' in support or not points:continue
        if abs(support['radius']-radius)>tolerance or abs(abs(support['axis'][axis])-1)>tolerance:continue
        if any(abs(support['axis'][i])>tolerance for i in coords):continue
        if any(abs(support['origin'][i]-v)>tolerance for i,v in zip(coords,centre)):continue
        if all(side*p[axis]>=-tolerance for p in points):matches.append(points)
    points=[p for group in matches for p in group]
    for point in points:comparison(name+' vertex',point,point,tolerance)
    axial=[side*p[axis] for p in points]
    passed=bool(points) and any(abs(x-outer)<=tolerance for x in axial) and any(0<=x<=inner_limit+tolerance for x in axial)
    passed=passed and all(abs(math.hypot(*(p[i]-v for i,v in zip(coords,centre)))-radius)<=tolerance for p in points)
    return dict(check=name,result='PASS' if passed else 'FAIL',unit='mm',axis=axis,side=side,
                observed_absolute_wall_vertex_span=[min(axial),max(axial)] if axial else [],
                method='Native cylindrical face support and reciprocal face-boundary endpoints')


def planar_boundary_pattern(name,features,axis,level,spans,centres,tolerance):
    """Compare closed native planar boundaries with a sourced position pattern."""
    if type(axis) is not int or axis not in [0,1,2]:
        raise ValueError('Cartesian plane axis required')
    comparison(name+' input validation',[level]+list(spans),[level]+list(spans),tolerance)
    if len(spans)!=2 or any(v<=0 for v in spans) or not centres:
        raise ValueError('Two positive spans and nonempty centres required')
    for centre in centres:
        if len(centre)!=2:raise ValueError('Two coordinates per plane centre required')
        comparison(name+' centre validation',centre,centre,tolerance)
    if len({tuple(p) for p in centres})!=len(centres):raise ValueError('Distinct expected centres required')
    coordinates=[i for i in range(3) if i!=axis];actual=[];closed=True
    for plane in features['planar_boundary_components']:
        normal=plane['plane_normal']
        if abs(abs(normal[axis])-1)>tolerance:continue
        if abs(plane['plane_offset']/normal[axis]-level)>tolerance:continue
        for boundary in plane['components']:
            b=boundary['bounds'];closed=closed and boundary['closed_degree_two']
            actual.append([[(b['min'][i]+b['max'][i])/2 for i in coordinates],
                           [b['max'][i]-b['min'][i] for i in coordinates]])
    actual.sort(key=lambda x:tuple(x[0]));expected=sorted([[list(p),list(spans)] for p in centres],key=lambda x:tuple(x[0]))
    result=comparison(name,actual,expected,tolerance,method='native coplanar boundary components, centres and spans')
    result['all_boundaries_closed']=closed
    if not closed:result['result']='FAIL'
    return result


def feature_vertices(name, observed, expected, tolerance):
    """Locate distinct feature corners among one reopened solid's vertices, in mm."""
    if type(tolerance) not in (int, float) or not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("A positive finite tolerance in mm is required")

    def points(values):
        result = []
        for point in values:
            if len(point) != 3 or any(type(x) not in (float, int) or not math.isfinite(x) for x in point):
                raise ValueError("Each vertex requires three finite coordinates in mm")
            result.append(tuple(point))
        return result

    targets = points(expected)
    if not targets or len(set(targets)) != len(targets):
        raise ValueError("Distinct source feature corners are required")
    vertices = sorted(set(points(observed)))
    matches = []
    for target in targets:
        nearest = min(vertices, key=lambda p: math.dist(target, p), default=None)
        distance = math.dist(target, nearest) if nearest is not None else None
        matches.append(dict(expected=target, observed=nearest, distance_mm=distance))
    passed = (len({m["observed"] for m in matches}) == len(targets)
              and all(m["distance_mm"] is not None and m["distance_mm"] <= tolerance for m in matches))
    return dict(check=name, result="PASS" if passed else "FAIL", tolerance_mm=tolerance, corners=matches)
