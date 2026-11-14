"""Source-bound convex planar cell and bilinear loft checks; no native mutations.

All XYZ data use the same caller-declared frame and length unit. These checks
are bounded to convex straight-edge cells and planar bilinear patches.
"""
import math
from collections import Counter
from cadtools.geometry import vector, finite


def sub(a,b): return [x-y for x,y in zip(a,b)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def unit(a):
    a=vector(a); length=math.sqrt(dot(a,a))
    if length==0: raise ValueError('Nonzero normal required')
    return [x/length for x in a]


def outward_normal(normal, sense):
    """ACIS/ezdxf boolean True=reversed, False=forward; SAT literals accepted."""
    if type(sense) is bool: reversed_=sense
    elif sense in ('forward','reversed'): reversed_=sense=='reversed'
    else: raise ValueError('Explicit ACIS face sense required')
    return [x*(-1 if reversed_ else 1) for x in unit(normal)]


def halfspace_check(points, halfspaces, *, tolerance):
    """Caller signs retain sign*dot(normal, point-origin)>=0; returns all residuals."""
    if finite(tolerance)<=0 or not points or not halfspaces: raise ValueError('Points, halfspaces and positive tolerance required')
    points=[vector(p) for p in points]; rows=[]
    for plane in halfspaces:
        sign=plane['retained_sign']
        if type(sign) is not int or sign not in (-1,1): raise ValueError('Explicit retained sign +/-1 required')
        n=unit(plane['normal']); o=vector(plane['origin'])
        values=[sign*dot(n,sub(p,o)) for p in points]
        rows.append(dict(plane_id=plane['id'],minimum=min(values),maximum=max(values),result='PASS' if min(values)>=-tolerance else 'FAIL'))
    return dict(result='PASS' if all(r['result']=='PASS' for r in rows) else 'FAIL',checks=rows)


def convex_cell_check(features, *, expected_vertices, halfspaces, expected_volume,
                      length_tolerance, volume_tolerance):
    """Verify a complete convex straight planar boundary, orientation and volume.

    Accepts sab_features(include_edge_curves=True) output. Per-face source
    support must coincide with a supplied halfspace whose sign retains material.
    Each face has exactly one convex loop; curved/nonconvex/multiple-loop cases
    are rejected. A domain coverage certificate is separate caller evidence.
    """
    lt=finite(length_tolerance); vt=finite(volume_tolerance); ev=finite(expected_volume)
    if lt<=0 or vt<=0 or ev<=0: raise ValueError('Positive tolerances and source volume required')
    points=[vector(p) for p in features['points']]; expected=[vector(p) for p in expected_vertices]
    if len(points)<4 or len(expected)<4: raise ValueError('At least four cell vertices required')
    checks=[]
    def ck(name,ok,**data): checks.append(dict(name=name,result='PASS' if ok else 'FAIL',**data))
    hits=[[j for j,q in enumerate(points) if math.dist(p,q)<=lt] for p in expected]
    ck('complete unique source vertices',len(points)==len(expected) and all(len(h)==1 for h in hits) and len({h[0] for h in hits if len(h)==1})==len(points))
    topo=features['topology'];ck('one closed body',all(topo.get(k)==1 for k in ('bodies','lumps','shells')) and topo.get('reciprocal_closed_partners') is True)
    hs=halfspace_check(points,halfspaces,tolerance=lt);checks.extend(dict(name='retained '+str(v['plane_id']),**v) for v in hs['checks'])
    witness=[sum(p[k] for p in points)/len(points) for k in range(3)]
    faces=features['face_boundary_edges']; edge_counts=Counter(); volume=0.
    for fi,face in enumerate(faces):
        if face['surface_type']!='plane-surface' or len(face['loops'])!=1: raise ValueError('One straight planar convex loop per face required')
        edges=face['loops'][0]['edges']; corner_ids=set(); local_edges=[]
        for edge in edges:
            if edge['curve_type']!='straight-curve': raise ValueError('Analytic straight cell edges required')
            pair=[]
            for p in edge['endpoints']:
                matches=[i for i,q in enumerate(points) if math.dist(p,q)<=lt]
                if len(matches)!=1: raise ValueError('Unambiguous boundary vertex required')
                pair.append(matches[0]); corner_ids.add(matches[0])
            if pair[0]==pair[1]: raise ValueError('Collapsed cell edge')
            key=tuple(sorted(pair));local_edges.append(key);edge_counts[key]+=1
        if len(corner_ids)<3 or len(set(local_edges))!=len(local_edges): raise ValueError('Simple nondegenerate face loop required')
        n=outward_normal(face['support']['normal'],face['reversed']);o=vector(face['support']['origin'])
        corners=[points[i] for i in corner_ids]; center=[sum(p[k] for p in corners)/len(corners) for k in range(3)]
        u=unit(sub(corners[0],center));v=cross(n,u)
        ordered=sorted(corner_ids,key=lambda i:math.atan2(dot(v,sub(points[i],center)),dot(u,sub(points[i],center))))
        polygon_edges={tuple(sorted((a,b))) for a,b in zip(ordered,ordered[1:]+ordered[:1])}
        ck('face '+str(fi)+' complete convex loop',polygon_edges==set(local_edges))
        ck('face '+str(fi)+' planar',all(abs(dot(n,sub(p,o)))<=lt for p in corners))
        ck('face '+str(fi)+' outward material',max(dot(n,sub(p,o)) for p in points)<=lt and dot(n,sub(witness,o)) < -lt)
        supports=[]
        for plane in halfspaces:
            pn=unit(plane['normal']);po=vector(plane['origin'])
            # Compare directions using a dimensionless numerical roundoff bound.
            if abs(dot(n,pn)+plane['retained_sign'])<=1e-9 and abs(dot(pn,sub(o,po)))<=lt: supports.append(plane['id'])
        ck('face '+str(fi)+' source support',bool(supports),source_supports=supports)
        area=[0.,0.,0.]
        for a,b in zip(ordered,ordered[1:]+ordered[:1]):
            term=cross(sub(points[a],center),sub(points[b],center));area=[x+y/2 for x,y in zip(area,term)]
        ck('face '+str(fi)+' nonzero area',dot(area,n)>lt*lt)
        ck('face '+str(fi)+' convex polygon',all(dot(n,cross(sub(points[b],points[a]),sub(points[c],points[a])))>=-lt*max(math.dist(points[a],points[b]),lt) for a,b in zip(ordered,ordered[1:]+ordered[:1]) for c in ordered))
        volume+=dot(sub(center,witness),area)/3
    ck('closed edge incidence and Euler characteristic',bool(edge_counts) and all(v==2 for v in edge_counts.values()) and len(points)-len(edge_counts)+len(faces)==2)
    ck('analytic boundary volume',abs(volume-ev)<=vt,observed=volume,expected=ev)
    return dict(result='PASS' if all(r['result']=='PASS' for r in checks) else 'FAIL',checks=checks,analytic_volume=volume,method='oriented planar polygon boundary integral',length_tolerance=lt,volume_tolerance=vt)


def bilinear_patch_check(expected_columns, observed_columns, *, plane_origin, plane_normal,
                         length_tolerance, jacobian_tolerance):
    """Check ordered 2x2 source correspondence, planar support and no corner fold.

    Columns are [[p00,p01],[p10,p11]]. Jacobian tolerance uses length-unit squared.
    All four Jacobians have one strict sign, proving orientation over this planar
    bilinear patch. Trims, cap loops and whole-solid coverage remain separate.
    """
    lt=finite(length_tolerance); jt=finite(jacobian_tolerance)
    if lt<=0 or jt<=0: raise ValueError('Positive length/area tolerances required')
    def grid(g):
        if len(g)!=2 or any(len(c)!=2 for c in g): raise ValueError('Ordered 2x2 corner columns required')
        return [[vector(p) for p in c] for c in g]
    expected,actual=grid(expected_columns),grid(observed_columns);n=unit(plane_normal);o=vector(plane_origin)
    distances=[math.dist(a,b) for ea,ob in zip(expected,actual) for a,b in zip(ea,ob)]
    residuals=[abs(dot(n,sub(p,o))) for c in actual for p in c]
    p00,p01=actual[0];p10,p11=actual[1];jac=[]
    for u,v in ((0,0),(0,1),(1,0),(1,1)):
        du=[(1-v)*a+v*b for a,b in zip(sub(p10,p00),sub(p11,p01))]
        dv=[(1-u)*a+u*b for a,b in zip(sub(p01,p00),sub(p11,p10))]
        jac.append(dot(n,cross(du,dv)))
    passed=max(distances)<=lt and max(residuals)<=lt and (min(jac)>jt or max(jac)<-jt)
    return dict(result='PASS' if passed else 'FAIL',corner_distances=distances,plane_residuals=residuals,corner_signed_jacobians=jac)
