"""Build source-bound motor interface geometry with existing guarded OCS tools.

External source jobs own dimensions and representation choices. This recipe
constructs the dimensioned housing/pilot, exposed keyed shaft and rear region.
It retains the source frame, nominal-thread representation and physical roles.
"""
import importlib
from component_records import require_ready
from rounded_tube import SelectionCheckedClient


def parameters(job):
    import math
    require_ready(job)
    if job['units']!='mm':raise ValueError('Motor recipe requires millimetres')
    p={f['name']:f['value'] for f in job['features']}
    if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<=0 for v in p.values()):
        raise ValueError('Positive finite motor dimensions required')
    if not (p['rear extent']>p['main case length'] and p['shaft end']>p['pilot projection']
            and p['shaft thread diameter']<p['shaft diameter']
            and p['shaft thread depth']<p['shaft end']-p['pilot projection']
            and p['keyway width']<p['shaft diameter']
            and p['keyway extent']<p['shaft end']-p['pilot projection']
            and p['shaft diameter']/2<p['keyway opposite tangent distance']<p['shaft diameter']):
        raise ValueError('Unsupported motor axial/keyway geometry')
    over=job['construction']['cut_overrun_mm']
    if isinstance(over,bool) or not isinstance(over,(int,float)) or not math.isfinite(over) or over<=0:
        raise ValueError('Positive finite construction overrun required')
    return p


def geometry(client):
    return importlib.import_module('cadtools.geometry').Geometry(SelectionCheckedClient(client))


def housing(client,job):
    p=parameters(job);g=geometry(client)
    main=g.cylinder('main-housing',[0,0,-p['main case length']],p['main case diameter']/2,p['main case length'])
    pilot=g.cylinder('locating-pilot',[0,0,0],p['pilot diameter']/2,p['pilot projection'])
    body=g.combine('housing-pilot-union',[main,pilot])
    over=job['construction']['cut_overrun_mm'];cutters=[]
    for label,angles,face in [('outer',[0,90,180,270],0),('inner',[45,135,225,315],p['pilot projection'])]:
        cutters+=g.holes(label+'-mount',p[label+' mounting pcd'],angles,p[label+' mounting diameter']/2,
                         face-p[label+' mounting depth'],p[label+' mounting depth']+over)
    g.subtract('mounting-blind-holes',body,cutters)
    g.metadata('housing-source',[body],[job['part_name'],'Stationary housing/pilot mechanical reference',
               job['frame'],'Nominal threaded-hole cylinders; source depths from respective front faces'])
    return body


def shaft(client,job):
    p=parameters(job);g=geometry(client);over=job['construction']['cut_overrun_mm']
    body=g.cylinder('exposed-shaft',[0,0,p['pilot projection']],p['shaft diameter']/2,p['shaft end']-p['pilot projection'])
    thread=g.cylinder('shaft-end-thread',[0,0,p['shaft end']-p['shaft thread depth']],p['shaft thread diameter']/2,p['shaft thread depth']+over)
    w=p['keyway width'];start=p['shaft end']-p['keyway extent'];end=p['shaft end']+over
    points=[[-w/2,start+w/2],[-w/2,end],[w/2,end],[w/2,start+w/2]]
    profile=g.profile('keyway-boundary',points,{3:-1})
    ymax=p['shaft diameter']/2+over;floor=p['keyway opposite tangent distance']-p['shaft diameter']/2
    g.move('keyway-profile-height',[profile],[0,0,-ymax]);g.select('keyway-profile-selection',[profile])
    added=importlib.import_module('cadtools.geometry').added
    cutter=added(g.run('keyway-extrusion','EXTRUDE '+str(ymax-floor)))
    if profile in {e['handle'] for e in client.read('query',limit=100)['entities']}:
        client.mutate('keyway-profile-cleanup','entities_delete',handles=[profile])
    g.rotate('keyway-to-shaft',[cutter],'X',90)
    g.subtract('shaft-thread-and-keyway',body,[thread,cutter])
    g.metadata('shaft-source',[body],[job['part_name'],'Rotating exposed shaft mechanical reference',
               job['frame'],'Source keyway section and axial extent; nominal shaft-end thread cylinder'])
    return body


def rear(client,job):
    p=parameters(job);g=geometry(client)
    body=g.cylinder('rear-region',[0,0,-p['rear extent']],p['rear section diameter']/2,p['rear extent']-p['main case length'])
    g.metadata('rear-source',[body],[job['part_name'],'Rear dimensioned reference region',job['frame']])
    return body


def verify(features, job, tolerance=1e-7):
    """Compare analytic surfaces to the external source job, in its local frame.

    A circular face can have only one seam vertex. Radius is read from the
    cylinder equation; blind depths are checked against bottom planes. This
    checks surface locations, not thread form, material or manufacturing fit.
    """
    import math
    from feature_checks import comparison, cylinder_pattern
    p=parameters(job);checks=[]
    def planes(part,axis,targets,name):
        observed=sorted({round(v['origin'][axis],9) for v in features[part]['planes']
                         if abs(abs(v['normal'][axis])-1)<=tolerance})
        checks.append(comparison(name,observed,sorted(targets),tolerance))
    def cylinders(part,diameter,centres,name,axis=2):
        checks.append(cylinder_pattern(name,features[part],diameter,axis,centres,tolerance))
    cylinders('housing',p['main case diameter'],[[0,0]],'main housing diameter and axis')
    cylinders('housing',p['pilot diameter'],[[0,0]],'locating pilot diameter and axis')
    for group,angles in [('outer',[0,90,180,270]),('inner',[45,135,225,315])]:
        radius=p[group+' mounting pcd']/2
        centres=[[radius*math.cos(math.radians(a)),radius*math.sin(math.radians(a))] for a in angles]
        cylinders('housing',p[group+' mounting diameter'],centres,group+' mounting nominal thread pattern')
        bottom=(0 if group=='outer' else p['pilot projection'])-p[group+' mounting depth']
        observed=sorted([v['origin'][:2] for v in features['housing']['planes']
                         if abs(abs(v['normal'][2])-1)<=tolerance and abs(v['origin'][2]-bottom)<=tolerance])
        checks.append(comparison(group+' mounting blind bottoms at each hole',observed,sorted(centres),tolerance))
    planes('housing',2,[-p['main case length'],0,p['pilot projection'],
                       -p['outer mounting depth'],p['pilot projection']-p['inner mounting depth']],
           'housing end, pilot face and blind hole bottom planes')
    cylinders('shaft',p['shaft diameter'],[[0,0]],'shaft diameter and axis')
    cylinders('shaft',p['shaft thread diameter'],[[0,0]],'shaft end nominal thread diameter and axis')
    planes('shaft',2,[p['pilot projection'],p['shaft end']-p['shaft thread depth'],p['shaft end']],
           'shaft ends and blind thread bottom plane')
    planes('shaft',0,[-p['keyway width']/2,p['keyway width']/2],'keyway side walls')
    planes('shaft',1,[p['keyway opposite tangent distance']-p['shaft diameter']/2],'keyway floor')
    # Rounded inner keyway end: its axis runs radially, along Y.
    cylinders('shaft',p['keyway width'],[[0,p['shaft end']-p['keyway extent']+p['keyway width']/2]],
              'rounded keyway end radius and axial station',axis=1)
    cylinders('rear',p['rear section diameter'],[[0,0]],'rear region diameter and axis')
    planes('rear',2,[-p['rear extent'],-p['main case length']],'rear region end planes')
    for name,f in features.items():
        if 'topology' in f:
            from feature_checks import closed_body
            checks.append(closed_body(name+' closed connected body',f))
    return {'result':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',
            'method':'native analytic cylinder equations and planar face stations',
            'numeric_tolerance_mm':tolerance,'checks':checks,
            'scope':'source-bound mechanical interfaces; nominal thread cylinders'}


def inspect(client,handles,job):
    """Read the actual current records; support the existing strict SAT/SAB readers."""
    from rounded_tube import sat_features
    from native_acis import sab_features
    records=client.read('records',collection='entities',handles=list(handles.values()),limit=len(handles))
    by_handle={r['handle']:r for r in records['records']};features={}
    for name,handle in handles.items():
        a=by_handle[handle]['properties']['acis_data']
        features[name]=sat_features(a['sat_data']) if a['sat_data'] else sab_features(bytes(a['sab_data']))
    checks=verify(features,job)
    checks.update(document_id=records['document_id'],revision=records['revision'],
                  geometry_revision=records['geometry_revision'],handles=handles,features=features)
    return records,checks
