"""Read supported native OCS ACIS700 SAB records through ezdxf's MIT parser.

This adapter reads geometry; it creates no CAD/export files. Values retain OCS
model coordinates. ACIS header unit metadata is reported separately.
"""
import math


def sab_features(data):
    from ezdxf.acis.sab import parse_sab
    from ezdxf.acis.const import Tags
    if not isinstance(data,(bytes,bytearray)) or not data:
        raise ValueError('Nonempty native SAB bytes required')
    b=parse_sab(data)
    if b.header.version!=700:raise ValueError('This adapter supports observed ACIS700 records')
    bodies=[e for e in b.entities if e.name=='body']
    if len(bodies)!=1:raise ValueError('Exactly one body required for component checks')
    # Traverse the actual body graph. Unreferenced surface records cannot supply
    # a passing feature. Keep cycles bounded by entity identity.
    pending=bodies.copy();seen={};refs=lambda e:[t.value for t in e.data if t.tag==Tags.POINTER and t.value.name!='null-ptr']
    while pending:
        e=pending.pop()
        if id(e) in seen:continue
        seen[id(e)]=e;pending.extend(refs(e))
    reachable=list(seen.values())
    if any(e.name=='transform' for e in reachable):
        raise ValueError('Transformed SAB requires an explicit frame reader')
    faces=[e for e in reachable if e.name=='face']
    if not faces:raise ValueError('Body has no reachable faces')
    surfaces={}
    for f in faces:
        surf=[e for e in refs(f) if e.name.endswith('-surface')]
        if len(surf)!=1:raise ValueError('Face needs one supported analytic surface')
        if surf[0].name not in ['plane-surface','cone-surface']:
            raise ValueError('Unsupported surface: '+surf[0].name)
        surfaces[id(surf[0])]=surf[0]
    out={'planes':[],'cylinders':[],'points':[]}
    def vec(token):
        if token.tag not in [Tags.LOCATION_VEC,Tags.DIRECTION_VEC]:raise ValueError('Expected native vector token')
        values=list(token.value)
        if len(values)!=3 or not all(math.isfinite(v) for v in values):raise ValueError('Invalid native vector')
        return values
    for e in surfaces.values():
        t=e.data
        if e.name=='plane-surface':out['planes'].append({'origin':vec(t[1]),'normal':vec(t[2])})
        else:
            # Native cone-surface fields: pattern, origin, axis, major vector,
            # ratio, u interval, sin(angle), cos(angle), radius, other bounds.
            # The observed unbounded u interval uses two BOOL_FALSE tokens.
            if len(t)<10 or any(t[i].tag!=Tags.DOUBLE for i in [4,7,8,9]):
                raise ValueError('Unsupported cone parameter layout')
            if not all(math.isfinite(t[i].value) for i in [4,7,8,9]):
                raise ValueError('Nonfinite native cylinder parameters')
            if abs(t[4].value-1)>1e-9 or abs(t[7].value)>1e-9 or abs(t[8].value-1)>1e-9:
                raise ValueError('Only circular cylindrical surfaces supported')
            major=vec(t[3]);radius=math.sqrt(sum(v*v for v in major))
            if not math.isfinite(radius) or radius<=0 or abs(radius-t[9].value)>1e-7:
                raise ValueError('Contradictory native cylinder radii')
            out['cylinders'].append({'origin':vec(t[1]),'axis':vec(t[2]),'radius':radius})
    for e in reachable:
        if e.name=='point':out['points'].append(vec(e.data[1]))
    if not out['points']:raise ValueError('Body has no reachable vertices')
    coedges=[e for e in reachable if e.name=='coedge']
    # The observed ACIS700 coedge fields and ezdxf entity definitions identify
    # the partner at slot3. Require reciprocal partner links for this closed body.
    closed=bool(coedges)
    for e in coedges:
        partner=e.data[3].value
        closed=closed and partner.name=='coedge' and partner.data[3].value is e
    out['topology']={'bodies':1,'lumps':sum(e.name=='lump' for e in reachable),
                     'shells':sum(e.name=='shell' for e in reachable),'faces':len(faces),
                     'coedges':len(coedges),'reciprocal_closed_partners':closed}
    out['encoding']='SAB';out['decoder']='ezdxf.acis.sab.parse_sab'
    out['acis_header_units_in_mm']=b.header.units_in_mm
    return out
