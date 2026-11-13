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


def closed_body(name,features):
    t=features['topology']
    return comparison(name,[t['bodies'],t['lumps'],t['shells'],int(t['reciprocal_closed_partners'])],[1,1,1,1],1e-9,'count','native connected body and reciprocal coedge graph')


def vertex_extrema(name,features,expected,tolerance):
    points=features['points']
    if not points:raise ValueError('Native vertex observations required')
    return comparison(name,[[min(p[i] for p in points),max(p[i] for p in points)] for i in range(3)],expected,tolerance,
                      method='native vertex coordinate extrema')


def cylinder_pattern(name,features,diameter,axis,centres,tolerance):
    if type(axis) is not int or axis not in [0,1,2] or isinstance(diameter,bool) or not math.isfinite(diameter) or diameter<=0:
        raise ValueError('Positive finite diameter and Cartesian axis required')
    if not centres or any(len(p)!=2 or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in p) for p in centres):
        raise ValueError('Nonempty finite expected axis centres required')
    coordinates=[i for i in range(3) if i!=axis];positions=[]
    for c in features['cylinders']:
        if abs(c['radius']*2-diameter)>tolerance or abs(abs(c['axis'][axis])-1)>tolerance:continue
        if any(abs(c['axis'][i])>tolerance for i in coordinates):continue
        point=[c['origin'][i] for i in coordinates]
        if not any(all(abs(a-b)<=tolerance for a,b in zip(point,p)) for p in positions):positions.append(point)
    return comparison(name,sorted(positions),sorted([list(p) for p in centres]),tolerance,
                      method='native circular cylinders; coincident patches deduplicated; axis projection')


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
