"""Analytic equal-radius circular clipping and bounded native extrusion (mm)."""
import math
from cadtools.geometry import Geometry,positive,vector
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


def bounded_extrusion(client,boundaries,pickpoint,height,*,label):
    """Extrude a supplied bounded material region; preserve all unrelated handles."""
    positive(height);vector(pickpoint)
    if not boundaries:raise ValueError('Boundaries required')
    prepared=[validate_outline(b['points'],b.get('bulges')) for b in boundaries]
    g=Geometry(SelectionCheckedClient(client))
    initial=client.read('query',limit=1000)
    if initial.get('next_offset') is not None:raise ValueError('Bounded preflight query requires narrower scope')
    before={r['handle'] for r in initial['entities']}
    profiles=[g.profile(label+'-boundary-'+str(i),points,bulges) for i,(points,bulges) in enumerate(prepared)]
    g.select(label+'-clear',[])
    response=client.mutate(label+'-bounded','run',cmd='PRESSPULL '+','.join(str(v) for v in pickpoint)+' '+str(height))
    rows=client.read('query',limit=1000)
    if rows.get('next_offset') is not None:raise ValueError('Bounded result query requires narrower scope')
    created=[r['handle'] for r in rows['entities'] if r['type']=='3D Solid' and r['handle'] not in before]
    if len(created)!=1:raise ValueError('Expected one newly created bounded solid')
    retained=[h for h in profiles if h in {r['handle'] for r in rows['entities']}]
    if retained:client.mutate(label+'-owned-profiles','entities_delete',handles=retained)
    return dict(body=created[0],profiles=profiles,request_id=response.get('request_id'))
