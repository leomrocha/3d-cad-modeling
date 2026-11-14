"""Read an explicit SVG M/L/C/Z segment grammar and caller-supplied affine frames."""
import math
import re

TOKEN=re.compile(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?')


def finite(values,size):
    values=list(values)
    if len(values)!=size or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in values):raise ValueError('Finite coordinate tuple required')
    return values


def parse_path(path_index,path_data):
    tokens=[];cursor=0
    for match in TOKEN.finditer(path_data):
        if path_data[cursor:match.start()].strip(' ,\t\r\n'):raise ValueError('Unsupported SVG token')
        value=match.group();tokens.append(value if value.isalpha() else float(value));cursor=match.end()
    if path_data[cursor:].strip(' ,\t\r\n'):raise ValueError('Unsupported SVG token')
    if any(isinstance(x,float) and not math.isfinite(x) for x in tokens):raise ValueError('Nonfinite SVG coordinate')
    paths=[];current=[0.,0.];command=None;index=0
    while index<len(tokens):
        if isinstance(tokens[index],str):command=tokens[index];index+=1
        if command is None:raise ValueError('Coordinates require SVG command')
        upper=command.upper();relative=command.islower()
        if upper not in ('M','L','C','Z'):raise ValueError('Unsupported SVG command '+command)
        if upper=='Z':
            if not paths:raise ValueError('Close without path')
            paths[-1]['closed']=True;paths[-1]['segments'].append(dict(command='Z',start=current,end=paths[-1]['move'],controls=[],segment_ordinal=len(paths[-1]['segments'])))
            current=paths[-1]['move'];command=None;continue
        arity=6 if upper=='C' else 2
        if index+arity>len(tokens) or any(isinstance(v,str) for v in tokens[index:index+arity]):raise ValueError('Incomplete SVG segment')
        values=tokens[index:index+arity];index+=arity
        points=[values[i:i+2] for i in range(0,arity,2)]
        if relative:points=[[p[i]+current[i] for i in (0,1)] for p in points]
        if upper=='M':
            current=points[0];paths.append(dict(path_index=path_index,subpath_ordinal=len(paths),move=current,segments=[],closed=False));command='l' if relative else 'L';continue
        if not paths:raise ValueError('Drawing segment requires initial move')
        paths[-1]['segments'].append(dict(command=upper,start=current,end=points[-1],controls=points[:-1],segment_ordinal=len(paths[-1]['segments'])))
        current=points[-1]
    if not paths:raise ValueError('Empty SVG path')
    return paths


def page_point(raw,matrix):
    x,y=finite(raw,2);a,b,c,d,e,f=finite(matrix,6)
    result=[a*x+c*y+e,b*x+d*y+f]
    return finite(result,2)


def local_point(raw,matrix,translation,*,units_per_page_unit,y_sign=-1):
    scale=finite([units_per_page_unit],1)[0];translation=finite(translation,2)
    if scale<=0 or y_sign not in (-1,1):raise ValueError('Positive conversion scale and signed Y axis required')
    p=page_point(raw,matrix)
    return finite([p[0]*scale+translation[0],y_sign*p[1]*scale+translation[1]],2)


def cubic_point(points,t):
    if len(points)!=4:raise ValueError('Four cubic control points required')
    points=[finite(p,2) for p in points];finite([t],1)
    if not 0<=t<=1:raise ValueError('Curve parameter must lie in [0,1]')
    u=1-t
    return finite([u**3*points[0][i]+3*u*u*t*points[1][i]+3*u*t*t*points[2][i]+t**3*points[3][i] for i in (0,1)],2)


def distance_to_segment(point,a,b):
    point=finite(point,2);a=finite(a,2);b=finite(b,2)
    delta=[b[i]-a[i] for i in (0,1)];den=sum(x*x for x in delta)
    t=0 if den==0 else max(0,min(1,sum((point[i]-a[i])*delta[i] for i in (0,1))/den))
    q=[a[i]+t*delta[i] for i in (0,1)]
    return max(abs(point[i]-q[i]) for i in (0,1)),t,q
