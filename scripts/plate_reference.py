"""Parameterized native plate operations. Coordinates mm, rotations degrees."""
import math
from cadtools.geometry import Geometry, vector, positive, finite
from rounded_tube import SelectionCheckedClient
from profile_reference import validate_profile
from feature_checks import closed_body, vertex_extrema, cylinder_pattern, comparison
from cadtools.records import read_stable_entity
from native_acis import sab_features


def outline(bounds,radius=0):
    (a,b),(c,d),_=bounds
    for value in [a,b,c,d,radius]:
        if not math.isfinite(value):raise ValueError('Finite outline values required')
    if a>=b or c>=d or radius<0 or 2*radius>=min(b-a,d-c):raise ValueError('Invalid outline spans/radius')
    if radius:
        r=radius
        return [[a+r,c],[b-r,c],[b,c+r],[b,d-r],[b-r,d],[a+r,d],[a,d-r],[a,c+r]],{i:math.tan(math.pi/8) for i in (1,3,5,7)}
    return [[a,c],[b,c],[b,d],[a,d]],{}


def validate_outline(points,bulges=None):
    points=[vector(p,2) for p in points];bulges=dict(bulges or {})
    for i,value in (bulges or {}).items():
        if type(i) is not int or not 0<=i<len(points) or isinstance(value,bool) or not math.isfinite(value):raise ValueError('Finite indexed bulges required')
    # Two analytic arcs can form a complete circle. Split one arc exactly so
    # the existing native polyline adapter receives at least three vertices.
    if len(points)==2 and any(bulges.values()):
        i=next(k for k in range(2) if bulges.get(k,0));a=points[i];b=points[(i+1)%2];value=bulges[i]
        dx,dy=b[0]-a[0],b[1]-a[1]
        if dx==dy==0:raise ValueError('Distinct arc endpoints required')
        factor=(1-value*value)/(4*value);centre=[(a[0]+b[0])/2-dy*factor,(a[1]+b[1])/2+dx*factor]
        angle=2*math.atan(value);ux,uy=a[0]-centre[0],a[1]-centre[1]
        middle=[centre[0]+ux*math.cos(angle)-uy*math.sin(angle),centre[1]+ux*math.sin(angle)+uy*math.cos(angle)]
        half=math.tan(math.atan(value)/2);points.insert(i+1,middle)
        bulges={k if k<=i else k+1:v for k,v in bulges.items()};bulges[i]=half;bulges[i+1]=half
    points=validate_profile(points)
    # Straight vertex chords must be simple; the caller's source contract supplies
    # analytic arc intersections and independently checked opening boundaries.
    return points,bulges


def cylinder_cutter(g,label,axis,centre,diameter,span,overrun):
    vector(centre,2);positive(diameter);positive(span[1]-span[0]);positive(overrun)
    p,q=centre;lo,hi=span
    if axis==2:return g.cylinder(label,[p,q,lo-overrun],diameter/2,hi-lo+2*overrun)
    if axis==1:
        h=g.cylinder(label,[p,-q,lo-overrun],diameter/2,hi-lo+2*overrun);g.rotate(label+'-axis',[h],'X',-90);return h
    if axis==0:
        h=g.cylinder(label,[-q,p,lo-overrun],diameter/2,hi-lo+2*overrun);g.rotate(label+'-axis',[h],'Y',90);return h
    raise ValueError('Cartesian cutter axis required')


def countersink_tool_profile(*, bore, mouth, angle_degrees, inner_radius, overrun):
    """Return the annular cutter in (radius, axial distance from transition)."""
    for value in (bore, mouth, inner_radius, overrun):
        positive(value)
    angle = finite(angle_degrees)
    if mouth <= bore or not 0 < angle < 180:
        raise ValueError('A larger mouth and an included angle in (0, 180) are required')
    slope = math.tan(math.radians(angle / 2))
    depth = (mouth - bore) / (2 * slope)
    radial_overrun = overrun * slope
    if bore / 2 - radial_overrun <= inner_radius:
        raise ValueError('Cutter lower outer radius must clear the inner radius')
    return dict(depth_mm=depth, profile=[
        [inner_radius, -overrun], [bore / 2 - radial_overrun, -overrun],
        [mouth / 2 + radial_overrun, depth + overrun], [inner_radius, depth + overrun],
    ])


def pin_seat_relief(*, shank_radius, bore_radius, head_radius, shoulder_station,
                    seat_station, outer_station, axis_sign):
    """Plan the annular material removal at a coaxial flat seat, in mm."""
    for radius in (shank_radius, bore_radius, head_radius):
        positive(radius)
    for station in (shoulder_station, seat_station, outer_station):
        finite(station)
    if type(axis_sign) is not int or axis_sign not in (-1, 1):
        raise ValueError('Axis sign must point from shank to head')
    if not shank_radius <= bore_radius < head_radius:
        raise ValueError('The shank must fit the bore and the head must overlap the seat')
    if axis_sign * (outer_station - shoulder_station) <= 0:
        raise ValueError('The head must have positive thickness')
    depth = finite(axis_sign * (seat_station - shoulder_station))
    if depth <= 0:
        return dict(action='retain', seat_gap_mm=-depth)
    if axis_sign * (outer_station - seat_station) <= 0:
        raise ValueError('Relief would consume the full head thickness')
    return dict(action='relieve', depth_mm=depth, radial_span_mm=[shank_radius, head_radius],
                axial_span_mm=sorted((shoulder_station, seat_station)),
                remaining_head_mm=finite(axis_sign * (outer_station - seat_station)))


def matching_countersink_fit(*, seat_bore, seat_mouth, head_shank, head_outer, angle_degrees):
    """Return ideal axial setback and overlap for two coaxial, equal-angle cones."""
    for value in (seat_bore, seat_mouth, head_shank, head_outer):
        positive(value)
    angle = finite(angle_degrees)
    if seat_mouth <= seat_bore or head_outer <= head_shank or not 0 < angle < 180:
        raise ValueError('Two nonempty cones and an included angle in (0, 180) are required')
    shared_small = max(seat_bore, head_shank)
    shared_large = min(seat_mouth, head_outer)
    if shared_small >= shared_large:
        raise ValueError('Conical diameter ranges must overlap')
    diameter_slope = 2 * math.tan(math.radians(angle / 2))
    return dict(head_setback_mm=(seat_mouth - head_outer) / diameter_slope,
                facing_cone_axial_span_mm=(shared_large - shared_small) / diameter_slope)


def build_plate(client,spec,*,label='plate'):
    """Consume a caller recipe; return body and owned handles. Run no save/cleanup."""
    bounds=spec['sketch_bounds'];points=spec['outline'];bulges=spec.get('bulges',{})
    points,bulges=validate_outline(points,bulges);positive(bounds[2][1]-bounds[2][0])
    overrun=positive(spec['cutter_overrun_mm'])
    # Validate the whole recipe before any native command.
    for hole in spec.get('holes',[]):
        if type(hole['axis']) is not int or hole['axis'] not in (0,1,2):raise ValueError('Invalid hole axis')
        positive(hole['diameter']);positive(hole.get('span',bounds[hole['axis']])[1]-hole.get('span',bounds[hole['axis']])[0])
        if not hole['centres']:raise ValueError('Nonempty hole centres required')
        for centre in hole['centres']:vector(centre,2)
    cutouts=[validate_outline(cut['points'],cut.get('bulges')) for cut in spec.get('cutouts',[])]
    for axis,degrees in spec.get('rotations',[]):
        if axis not in ('X','Y','Z') or not math.isfinite(degrees):raise ValueError('Invalid rotation')
    vector(spec.get('translation',[0,0,0]))
    g=Geometry(SelectionCheckedClient(client));z=bounds[2][0]
    body=g.extrude(label,points,z,bounds[2][1]-z,bulges);cutters=[]
    for i,hole in enumerate(spec.get('holes',[])):
        for j,centre in enumerate(hole['centres']):cutters.append(cylinder_cutter(g,f'{label}-hole-{i}-{j}',hole['axis'],centre,hole['diameter'],hole.get('span',bounds[hole['axis']]),overrun))
    for i,(cut_points,cut_bulges) in enumerate(cutouts):
        cutters.append(g.extrude(f'{label}-cutout-{i}',cut_points,z-overrun,bounds[2][1]-z+2*overrun,cut_bulges))
    if cutters:g.subtract(label+'-cuts',body,cutters)
    for i,(axis,degrees) in enumerate(spec.get('rotations',[])):g.rotate(f'{label}-frame-{i}',[body],axis,degrees)
    if spec.get('translation'):g.move(label+'-position',[body],spec['translation'])
    if spec.get('metadata'):g.metadata(label+'-source',[body],spec['metadata'])
    return dict(body=body)


def verify_plate(features,*,name,bounds,hole_groups=(),witness_points=(),tolerance):
    checks=[closed_body(name,features),vertex_extrema(name+' coordinate extrema',features,bounds,tolerance)]
    for i,h in enumerate(hole_groups):checks.append(cylinder_pattern(name+' hole '+str(i),features,h['diameter'],h['axis'],h['centres'],tolerance))
    if witness_points:
        observed=[int(any(all(abs(a-b)<=tolerance for a,b in zip(p,q)) for q in features['points'])) for p in witness_points]
        checks.append(comparison(name+' boundary witnesses',observed,[1]*len(observed),tolerance,'count'))
    return dict(result='PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',checks=checks)


def native_features(client,handle,**options):
    row,identity=read_stable_entity(client,handle)
    if row.get('type')!='Solid3D':raise ValueError('Native solid required')
    return sab_features(bytes(row['properties']['acis_data']['sab_data']),**options),identity


def cut_sidewalls(client, body, *, axis, centre, diameter, intervals, label, checkpoint=None):
    """Cut bounded wall intervals, optionally saving each completed native stage.

    The caller establishes cavity equivalence and can pass a checkpoint
    callback receiving the stage name and only the live owned handles.
    """
    if not intervals:
        raise ValueError('Explicit material wall intervals required')
    if axis not in (0, 1, 2):
        raise ValueError('Cartesian axis required')
    if checkpoint is not None and not callable(checkpoint):
        raise TypeError('Sidewall checkpoint must be callable')
    p, q = vector(centre, 2)
    positive(diameter)
    for lo, hi in intervals:
        positive(hi - lo)
    ordered = sorted(intervals)
    if any(b[0] < a[1] for a, b in zip(ordered, ordered[1:])):
        raise ValueError('Disjoint wall cutter intervals required')
    geometry = Geometry(SelectionCheckedClient(client))
    rotations = (('Y', 90), ('X', -90), None)
    for index, (lo, hi) in enumerate(intervals):
        key = f'{label}-{index}'
        origins = ([-q, p, lo], [p, -q, lo], [p, q, lo])
        cutter = geometry.cylinder(key, origins[axis], diameter / 2, hi - lo)
        if checkpoint is not None:
            checkpoint(key + '-cutter', (body, cutter))
        rotation = rotations[axis]
        if rotation is not None:
            geometry.rotate(key + '-axis', [cutter], *rotation)
            if checkpoint is not None:
                checkpoint(key + '-aligned', (body, cutter))
        geometry.subtract(key + '-subtract', body, [cutter])
        if checkpoint is not None:
            checkpoint(key + '-wall', (body,))
    return body
