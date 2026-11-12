"""Source-bound saved-shell and terminal checks for the exercised Leaf geometry.

Dimensions and reconstruction choices are supplied by the external component
job. This module reads native records and creates no geometry or files.
"""
import math
from component_records import require_ready
from native_acis import named_parts
from feature_checks import comparison,closed_body,vertex_extrema,cylinder_pattern


def check(record,job,tolerance=1e-7):
    require_ready(job)
    if job['units']!='mm' or not math.isfinite(tolerance) or tolerance<=0:
        raise ValueError('Millimetres and a positive finite numerical threshold required')
    p=named_parts(record,job['metadata_app'],job['required_parts'],allow_rigid=True)
    v={f['name']:f['value'] for f in job['features']};checks=[]
    def compare(name,actual,expected,unit='mm'):
        checks.append(comparison(name,actual,expected,tolerance,unit))
    for name,part in p.items():
        checks.append(closed_body(name+' closed connected body',part))
    shells=[p['upper_pressed_shell'],p['lower_pressed_shell']]
    points=[point for part in shells for point in part['points']]
    checks.append(vertex_extrema('can envelope',{'points':points},
            [[-v['can length']/2,v['can length']/2],[-v['can width']/2,v['can width']/2],[0,v['can thickness']]],tolerance))
    for name in ['upper_pressed_shell','lower_pressed_shell']:
        part=p[name]
        bores=[c for c in part['cylinders'] if abs(2*c['radius']-v['mount bore diameter'])<=tolerance]
        expected=sorted((x,y) for x in [-v['mount X offset'],v['mount X offset']] for y in [-v['mount Y offset'],v['mount Y offset']])
        checks.append(cylinder_pattern(name+' mounting bore centres',part,v['mount bore diameter'],2,expected,tolerance))
        compare(name+' mounting bore axes',[int(bool(bores)),int(all(abs(abs(c['axis'][2])-1)<=tolerance for c in bores))],[1,1],'count')
        # Require actual inner wall planes separated from each outer straight wall.
        for axis,label,dimension in [(0,'X','can length'),(1,'Y','can width')]:
            planes={round(a['origin'][axis],7) for a in part['planes'] if abs(abs(a['normal'][axis])-1)<=tolerance}
            expected=[sign*(v[dimension]/2-v['perimeter wall']) for sign in [-1,1]]
            compare(name+' '+label+' inner wall planes',[int(any(abs(x-e)<=tolerance for x in planes)) for e in expected],[1,1],'count')
    for i,y in enumerate([-v['terminal pitch'],0,v['terminal pitch']],1):
        contact=p[f'terminal_{i}_contact'];insulator=p[f'terminal_{i}_insulator']
        dia=v['tap bore diameter'] if i==2 else v['power bore diameter']
        bores=[c for c in contact['cylinders'] if abs(c['radius']*2-dia)<=tolerance]
        compare(f'terminal {i} nominal bore exists',int(bool(bores)),1,'count')
        for j,c in enumerate(bores):compare(f'terminal {i} bore axis {j}',[c['origin'][1],c['origin'][2],abs(c['axis'][0])],[y,v['terminal height'],1])
        xs=[a[0] for a in contact['points']];compare(f'terminal {i} contact face',max(xs),v['can length']/2+v['terminal projection'])
        size=v['tap pedestal size'] if i==2 else v['power pedestal size']
        points=insulator['points'];compare(f'terminal {i} pedestal section',[[min(a[j] for a in points),max(a[j] for a in points)] for j in [1,2]],[[y-size/2,y+size/2],[v['terminal height']-size/2,v['terminal height']+size/2]])
    return dict(result='PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',
                checks=checks,job_id=job['job_id'],document_id=record['document_id'],geometry_revision=record['geometry_revision'],
                method='actual saved SAB surfaces, transformed vertices and source-bound named parts',
                representation=job['representation'],units='mm')
