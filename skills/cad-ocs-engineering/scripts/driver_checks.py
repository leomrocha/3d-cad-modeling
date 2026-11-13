"""Source-bound exterior checks for the exercised Sumitomo driver reconstruction."""
from component_records import require_ready
from native_acis import sab_features,sab_structure
from feature_checks import comparison,closed_body,vertex_extrema,cylinder_pattern


def check(record,job,tolerance=1e-7):
    require_ready(job)
    if job['units']!='mm':raise ValueError('Driver job requires millimetres')
    rows={r['handle']:r for r in record['records'] if 'acis_data' in r['properties']}
    mapping=job['part_handles']
    if set(rows)!=set(mapping.values()) or len(set(mapping.values()))!=len(mapping):raise ValueError('Exact component handle set required')
    parts={};checks=[];methods={}
    for name,handle in mapping.items():
        data=bytes(rows[handle]['properties']['acis_data']['sab_data'])
        # The loft has a separate, explicit vertex/topology route. All other
        # source parts require the strict analytic route exercised previously.
        if name in job['structure_only_parts']:
            parts[name]=sab_structure(data);methods[name]='body graph and vertices; source-outline visual comparison'
        else:
            parts[name]=sab_features(data,allow_rigid=True);methods[name]='native analytic surfaces and vertices'
        checks.append(closed_body(name+' closed body',parts[name]))
    v={f['name']:f['value'] for f in job['features']}
    checks.append(vertex_extrema('mounting baseplate extrema',parts['mounting_baseplate'],[[-v['base length']/2,v['base length']/2],[-v['base width']/2,v['base width']/2],[0,v['base thickness']]],tolerance))
    checks.append(cylinder_pattern('base mounting bore pattern',parts['mounting_baseplate'],v['mount bore diameter'],2,[(x,y) for x in [-v['mount X pitch']/2,v['mount X pitch']/2] for y in [-v['mount Y pitch']/2,v['mount Y pitch']/2]],tolerance))
    points=[p for f in parts.values() for p in f['points']]
    checks.append(comparison('overall vertex height',max(p[2] for p in points),v['overall height'],tolerance,method='native vertex coordinates'))
    checks.append(comparison('housing top vertex height',max(p[2] for p in parts['tapered_housing']['points']),v['housing height'],tolerance,method='native loft vertices'))
    for i,label in enumerate(['U','POSITIVE','V','NEGATIVE','W','B']):
        part=parts['terminal_'+label];x=(i-2.5)*v['terminal pitch']
        checks.append(cylinder_pattern('terminal '+label+' nominal stud',part,v['terminal diameter'],2,[[x,v['terminal Y']]],tolerance))
        checks.append(comparison('terminal '+label+' top height',max(p[2] for p in part['points']),v['terminal height'],tolerance))
    for i in range(6):
        left=max(p[0] for p in parts['terminal_divider_'+str(i)]['points'])
        right=min(p[0] for p in parts['terminal_divider_'+str(i+1)]['points'])
        checks.append(comparison('terminal clear space '+str(i),right-left,v['divider clear space'],tolerance))
    x1=parts['X1_connector_shell']['points'];x2=parts['X2_connector_shell']['points']
    checks.append(comparison('connector shell outer span',max(p[0] for p in x2)-min(p[0] for p in x1),v['connector span'],tolerance))
    for name in ['X1_connector_shell','X2_connector_shell']:
        planes=parts[name]['planes']
        checks.append(comparison(name+' recessed floor exists',int(any(abs(p['normal'][2])>1-tolerance and abs(p['origin'][2]-v['connector cavity floor'])<=tolerance for p in planes)),1,tolerance,'count','native plane surface'))
    return dict(result='PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL',checks=checks,methods=methods,
                document_id=record['document_id'],geometry_revision=record['geometry_revision'],job_id=job['job_id'],
                representation=job['representation'],units='mm')
