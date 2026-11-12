"""Read the exercised AP214 identity-target placements and plan native repairs.

Read-only: callers review the source/drawing association before any OCS write.
Handles only explicit finite orthonormal AXIS2_PLACEMENT_3D frames, explicit
point/direction triples and identity second frames. Native insert angles are
radians and insertion points are stored in object coordinates in this case.
Adapted matrix operations from FERME's inspect_victron_import.py; correction
uses original STEP placements rather than a proximity-based alignment.
"""
import math
import re


def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def unit(v):
    if len(v)!=3 or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in v):raise ValueError('Finite 3-vector required')
    n=math.sqrt(dot(v,v))
    if n<1e-12:raise ValueError('Nonzero direction required')
    return [x/n for x in v]
def eye():return [[float(i==j) for j in range(4)] for i in range(4)]
def near(a,b,tol=1e-7):return all(abs(a[i][j]-b[i][j])<=tol for i in range(4) for j in range(4))
def apply(m,p):return [sum(m[i][j]*p[j] for j in range(3))+m[i][3] for i in range(3)]
def multiply(a,b):return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def inverse(m):
    r=eye()
    for i in range(3):
        for j in range(3):r[i][j]=m[j][i]
        r[i][3]=-sum(r[i][j]*m[j][3] for j in range(3))
    return r

def basis(z):
    z=unit(z);x=unit(cross([0,1,0] if abs(z[0])<1/64 and abs(z[1])<1/64 else [0,0,1],z))
    return [x,cross(z,x),z]

def xyz(v):return [v[k] for k in ['x','y','z']]

def native_matrix(p):
    if p.get('column_count',1)!=1 or p.get('row_count',1)!=1:raise ValueError('Array inserts unsupported')
    axes=basis(xyz(p['normal']));a=p['rotation'];c,s=math.cos(a),math.sin(a)
    x=[axes[0][i]*c+axes[1][i]*s for i in range(3)];y=[-axes[0][i]*s+axes[1][i]*c for i in range(3)]
    scales=[p[k] for k in ['x_scale','y_scale','z_scale']]
    if any(abs(v-1)>1e-7 for v in scales):raise ValueError('Unit-scale insert required')
    m=eye();o=xyz(p['insert_point'])
    for i in range(3):
        m[i][:3]=[x[i],y[i],axes[2][i]]
        m[i][3]=sum(axes[j][i]*o[j] for j in range(3))
    return m


def native_fields(m):
    z=[m[i][2] for i in range(3)];axes=basis(z);x=[m[i][0] for i in range(3)];o=[m[i][3] for i in range(3)]
    return {'normal':dict(zip('xyz',z)),
            'rotation':math.atan2(dot(x,axes[1]),dot(x,axes[0])),
            'insert_point':dict(zip('xyz',[dot(o,a) for a in axes]))}


def identity_target_placements(text):
    if "'AUTOMOTIVE_DESIGN'" not in text:raise ValueError('Exercised AP214 source required')
    pairs=re.findall(r'#(\d+)\s*=\s*(.*?);',text,re.S)
    entries={int(k):v.strip() for k,v in pairs}
    if len(entries)!=len(pairs):raise ValueError('Duplicate STEP entity identifier')
    refs=lambda v:list(map(int,re.findall(r'#(\d+)',v)))
    def vector(i,kind):
        v=entries[i]
        if not v.startswith(kind+' '):raise ValueError('Explicit '+kind+' required')
        hit=re.fullmatch(kind+r"\s*\(\s*'(?:[^']|'')*'\s*,\s*\(([^()]+)\)\s*\)",v,re.S)
        if not hit:raise ValueError('Unsupported STEP vector syntax')
        values=list(map(float,hit[1].split(',')))
        if len(values)!=3 or not all(math.isfinite(x) for x in values):raise ValueError('Finite STEP coordinate triple required')
        return values
    def frame(i):
        v=entries[i];r=refs(v)
        if not v.startswith('AXIS2_PLACEMENT_3D ') or len(r)!=3:raise ValueError('Explicit STEP axis frame required')
        o=vector(r[0],'CARTESIAN_POINT');z=unit(vector(r[1],'DIRECTION'));x=unit(vector(r[2],'DIRECTION'))
        if abs(dot(x,z))>1e-9:raise ValueError('Nonorthogonal STEP frame')
        y=cross(z,x);m=eye()
        for k in range(3):m[k]=[x[k],y[k],z[k],o[k]]
        return m
    out=[]
    for i,v in entries.items():
        if not v.startswith('ITEM_DEFINED_TRANSFORMATION '):continue
        r=refs(v)
        if len(r)!=2:raise ValueError('Two explicit placement references required')
        first,second=map(frame,r)
        if not near(second,eye()):raise ValueError('Nonidentity target frame requires another source reader')
        out.append({'source_id':i,'frame_ids':r,'matrix':first})
    if not out:raise ValueError('No supported STEP placements found')
    return out


def reversed_placement_plan(records,placements):
    changes=[]
    for r in records:
        if r['type']!='Insert':continue
        p=r['properties'];m=native_matrix(p)
        if near(m,eye()):continue
        hits=[v for v in placements if near(m,inverse(v['matrix']))]
        if len(hits)!=1:raise ValueError('Unique reversed source placement required for '+r['handle'])
        target=hits[0];fields=native_fields(target['matrix'])
        test=dict(p,**fields)
        if not near(native_matrix(test),target['matrix']):raise ValueError('Native field round-trip differs')
        changes.append({'handle':r['handle'],'block_name':p['block_name'],'source_id':target['source_id'],
                        'frame_ids':target['frame_ids'],'before':m,'expected':target['matrix'],'fields':fields})
    if not changes:raise ValueError('No observed reversed placements')
    return changes


def solid_instances(records,block_records,root_handles,max_instances=10000):
    """Traverse native block membership with instance identity and rigid frames.

    This exercised reader requires zero block base points, single inserts and
    unit scales. Unsupported leaves/cycles fail before returning partial data.
    """
    if type(max_instances) is not int or max_instances<=0:raise ValueError('Positive instance bound required')
    by_handle={r['handle']:r for r in records};blocks={r['name']:r['properties'] for r in block_records};out=[]
    def visit(handle,m,path,active):
        if handle in active:raise ValueError('Cyclic native block membership')
        r=by_handle[handle]
        if r['type']=='Solid3D':
            if len(out)>=max_instances:raise ValueError('Native instance bound exceeded')
            out.append({'handle':handle,'path':path+[handle],'matrix':m});return
        if r['type']!='Insert':raise ValueError('Unsupported native assembly leaf '+r['type'])
        p=r['properties'];b=blocks[p['block_name']]
        if any(abs(v)>1e-9 for v in xyz(b['base_point'])):raise ValueError('Nonzero block base requires another reader')
        for child in b['entity_handles']:visit(format(child,'X'),multiply(m,native_matrix(p)),path+[handle],active|{handle})
    for root in root_handles:visit(root,eye(),[],set())
    if not out:raise ValueError('No solid instances reached')
    return out


def identity_sat_vertices(text):
    """Read observed SAT point records with zero or one explicit identity transform.

    Used for pre-save comparison with the reachable saved SAB vertices. This
    function reports point records; it does not claim curved-surface bounds.
    """
    points=[];transforms=0
    for line in text.splitlines():
        t=line.split()
        if not t:continue
        if t[0]=='transform':
            transforms+=1
            if transforms>1 or list(map(float,t[3:16]))!=[1,0,0,0,1,0,0,0,1,0,0,0,1]:raise ValueError('Identity SAT transform required')
        if t[0]=='point':
            p=list(map(float,t[4:7]))
            if len(p)!=3 or not all(math.isfinite(v) for v in p):raise ValueError('Finite SAT point triple required')
            points.append(p)
    if not points:raise ValueError('SAT point records required')
    return points
