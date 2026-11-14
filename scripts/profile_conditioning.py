"""Reversible positive uniform conditioning of caller-supplied planar profiles.

working = (source-anchor)*scale + translation. Coordinates use the caller's
length unit; scale is dimensionless. No frame, factor, seed or depth is selected.
"""
import copy
import math
from cadtools.geometry import finite,vector
from exact_profiles import validate_edge,compare_loops


def conditioning_point(point, *, anchor, scale, translation=(0,0), inverse=False):
    p=vector(point,2);a=vector(anchor,2);t=vector(translation,2);s=finite(scale)
    if s<=0 or type(inverse) is not bool:raise ValueError('Positive uniform scale and explicit inverse boolean required')
    out=[(p[i]-t[i])/s+a[i] if inverse else (p[i]-a[i])*s+t[i] for i in range(2)]
    if not all(math.isfinite(v) for v in out):raise ValueError('Conditioned coordinates overflow')
    return out


def condition_profiles(loops, *, anchor, scale, translation=(0,0), inverse=False):
    """Map all controls/endpoints/centers; preserve degrees, weights, knots and roles."""
    if not loops:raise ValueError('Complete nonempty profiles required')
    out=copy.deepcopy(loops)
    for loop in out:
        if not loop.get('edges'):raise ValueError('Complete source edges required')
        for e in loop['edges']:
            validate_edge(e)
            fields=('start','end') if e['kind']=='Line' else ('start','end','center') if e['kind']=='Arc' else ()
            for key in fields:e[key]=conditioning_point(e[key],anchor=anchor,scale=scale,translation=translation,inverse=inverse)
            if e['kind']=='NURBS':e['control_points']=[conditioning_point(p,anchor=anchor,scale=scale,translation=translation,inverse=inverse) for p in e['control_points']]
            validate_edge(e)
    return out


def conditioning_roundtrip(loops, *, anchor, scale, translation=(0,0), length_tolerance, parameter_tolerance):
    working=condition_profiles(loops,anchor=anchor,scale=scale,translation=translation)
    restored=condition_profiles(working,anchor=anchor,scale=scale,translation=translation,inverse=True)
    proof=compare_loops(loops,restored,length_tolerance=length_tolerance,parameter_tolerance=parameter_tolerance)
    return dict(result=proof['result'],working_profiles=working,roundtrip_check=proof,
                anchor=list(anchor),scale=scale,translation=list(translation),
                meaning='Input transform roundtrip only; actual restored native geometry requires independent source checks')


def conditioning_depth(depth,scale,*,inverse=False):
    d,s=finite(depth),finite(scale)
    if d<=0 or s<=0 or type(inverse) is not bool:raise ValueError('Positive depth/scale and explicit inverse boolean required')
    out=d/s if inverse else d*s
    if not math.isfinite(out) or out<=0:raise ValueError('Conditioned depth overflows or underflows')
    return out
