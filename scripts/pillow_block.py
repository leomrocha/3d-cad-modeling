"""Check a source-bound, ten-solid pillow block from actual native OCS records.

Expected dimensions and component metadata names belong to the external job.
Supported observations: analytic ACIS700 SAB, proper rigid transforms and
coplanar boundary cancellation. Numerical comparison is not a fit tolerance.
"""
import math
from component_records import require_ready
from native_acis import sab_features


def read_parts(record, job):
    parts = {}
    for row in record['records']:
        prop = row['properties']
        labels = [v['String'][11:] for app in prop['common']['extended_data']['records']
                  if app['application_name'] == job['metadata_app']
                  for v in app['values'] if v.get('String', '').startswith('Component: ')]
        if len(labels) != 1:
            raise ValueError('Each solid requires one source component label')
        name = job.get('part_aliases', {}).get(labels[0], labels[0])
        if name in parts:
            raise ValueError('Duplicate component label')
        parts[name] = sab_features(bytes(prop['acis_data']['sab_data']),
                                  allow_rigid=True, allow_spheres=True,
                                  allow_cones=True, include_loops=True)
    if set(parts) != set(job['required_parts']):
        raise ValueError('Native component set differs from the source job')
    return parts


def check(record, job, tolerance=1e-7):
    require_ready(job)
    if job['units'] != 'mm' or not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Millimetres and positive finite comparison tolerance required')
    parts = read_parts(record, job)
    values = {v['name']: v['value'] for v in job['features']}
    results = []
    def compare(name, actual, expected, unit='mm'):
        actual = list(actual) if isinstance(actual, (list, tuple)) else [actual]
        expected = list(expected) if isinstance(expected, (list, tuple)) else [expected]
        good = len(actual) == len(expected) and all(
            math.isfinite(a) and abs(a-b) <= tolerance for a,b in zip(actual,expected))
        results.append(dict(check=name, observed=actual, expected=expected, unit=unit,
                            numeric_tolerance=tolerance, result='PASS' if good else 'FAIL'))
    for name,p in parts.items():
        t=p['topology']
        compare(name+' connected closed body',
                [t['bodies'],t['lumps'],t['shells'],int(t['reciprocal_closed_partners'])],
                [1,1,1,1], 'count')
    housing=parts['housing']; points=housing['points']
    lo=[min(p[i] for p in points) for i in range(3)]
    hi=[max(p[i] for p in points) for i in range(3)]
    compare('housing envelope',[hi[i]-lo[i] for i in range(3)],
            [values[n] for n in ['housing length','housing base width','housing height']])
    crown=[p[1] for p in points if abs(p[2]-values['housing height'])<=tolerance]
    compare('housing top width',max(crown)-min(crown) if crown else math.nan,
            values['housing top width'])
    base=[g for g in housing['planar_boundary_components']
          if all(abs(a-b)<=tolerance for a,b in zip(g['plane_normal'],[0,0,1]))
          and abs(g['plane_offset'])<=tolerance]
    slots=[]
    for group in base:
        for c in group['components']:
            a,b=c['bounds']['min'],c['bounds']['max']
            if abs(b[0]-a[0]-values['slot length'])<=tolerance and abs(b[1]-a[1]-values['slot width'])<=tolerance:
                slots.append(((a[0]+b[0])/2,(a[1]+b[1])/2,c['closed_degree_two']))
    slots.sort()
    compare('two closed mounting slots',len(slots),2,'count')
    if len(slots)==2:
        compare('mounting slot centres',[slots[0][0],slots[1][0],slots[0][1],slots[1][1]],
                [-values['slot centre distance']/2,values['slot centre distance']/2,0,0])
        compare('mounting slot closed boundaries',[int(s[2]) for s in slots],[1,1],'count')
    compare('foot shoulder planes',int(any(abs(p['origin'][2]-values['foot height'])<=tolerance and abs(abs(p['normal'][2])-1)<=tolerance for p in housing['planes'])),1,'count')
    inner=parts['bearing_inner_ring']
    bores=[c for c in inner['cylinders'] if abs(c['radius']-values['shaft bore diameter']/2)<=tolerance]
    compare('shaft bore surface exists',int(bool(bores)),1,'count')
    for i,c in enumerate(bores):
        compare('shaft bore axis '+str(i),[c['origin'][0],c['origin'][2],abs(c['axis'][1])],[0,values['shaft height'],1])
    ends=sorted(set(round(p['origin'][1],7) for p in inner['planes'] if abs(abs(p['normal'][1])-1)<=tolerance))
    compare('inner ring axial faces',[min(ends),max(ends)],[-values['locking side face offset'],values['inner ring width']-values['locking side face offset']])
    for label in ['housing','bearing_outer_ring']:
        spheres=parts[label]['spheres']
        compare(label+' spherical seat exists',int(bool(spheres)),1,'count')
        for i,s in enumerate(spheres):
            compare(label+' spherical seat '+str(i),s['origin']+[s['radius']],[0,0,values['shaft height'],values['outer bearing diameter']/2])
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    def hex_offsets(part,axis,centre):
        return sorted(set(round(abs(dot(p['normal'],[a-b for a,b in zip(p['origin'],centre)])),7)
                          for p in part['planes'] if abs(dot(p['normal'],axis))<=tolerance))
    axes=[]
    for label in ['locking_screw_1','locking_screw_2']:
        p=parts[label];c=p['cylinders'][0];axes.append(c['axis'])
        compare(label+' nominal diameter',c['radius']*2,values['screw nominal diameter'])
        compare(label+' axial position',c['origin'][1],-values['locking side face offset']+values['screw axial offset'])
        compare(label+' socket half across flats',hex_offsets(p,c['axis'],c['origin']),[values['screw socket across flats']/2])
    compare('locking screw angle',math.degrees(math.acos(max(-1,min(1,dot(*axes))))),values['screw angular spacing'],'deg')
    for prefix in ['contact_seal','seal_flinger']:
        for suffix,sign in [('front',-1),('rear',1)]:
            p=parts[prefix+'_'+suffix]
            radii=sorted(set(round(c['radius'],7) for c in p['cylinders']))
            outer='seal outer radius' if prefix=='contact_seal' else 'flinger outer radius'
            compare(prefix+' '+suffix+' radii',radii,[values['seal inner radius'],values[outer]])
            a,b=('seal inner station','seal outer station') if prefix=='contact_seal' else ('seal outer station','flinger outer station')
            faces=sorted(set(round(p['origin'][1],7) for p in p['planes'] if abs(abs(p['normal'][1])-1)<=tolerance))
            compare(prefix+' '+suffix+' axial faces',faces,sorted([sign*values[a],sign*values[b]]))
    grease=parts['grease_fitting'];axis=grease['cylinders'][0]['axis']
    compare('grease fitting angle',math.degrees(math.acos(abs(axis[2]))),values['grease angle'],'deg')
    compare('grease fitting shaft offset',grease['cylinders'][0]['origin'][1],values['grease axial offset'])
    compare('grease hex half across flats',hex_offsets(grease,axis,grease['cylinders'][0]['origin']),[values['grease hex across flats']/2])
    compare('grease head diameter surface',int(any(abs(c['radius']*2-values['grease head diameter'])<=tolerance for c in grease['cones'])),1,'count')
    return dict(result='PASS' if all(r['result']=='PASS' for r in results) else 'FAIL',
                method='source-bound native SAB analytic surfaces and trimmed boundaries',
                document_id=record['document_id'],geometry_revision=record['geometry_revision'],
                job_id=job['job_id'],checks=results,
                interpretation='OCS millimetre model coordinates; source-labelled reconstruction and nominal threads',
                acis_header_units_in_mm=sorted(set(p['acis_header_units_in_mm'] for p in parts.values())))
