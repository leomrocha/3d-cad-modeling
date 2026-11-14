"""Verify immutable native solid transfer using explicit source/target bindings.

This pure readback comparison sends no native requests and changes no records.
It transfers only existing geometric check evidence for identical payloads;
source coverage, physical-part counts and persistence retain separate receipts.
"""
import hashlib
import json
from collections import Counter


def _canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)


def _by_handle(rows):
    result={}
    for row in rows:
        h=row.get('handle')
        if not isinstance(h,str) or not h or h in result:raise ValueError('Unique native record handles required')
        result[h]=row
    return result


def _apps(record):
    value=record['properties'].get('common',{}).get('extended_data')
    if value is None:return []
    if not isinstance(value,dict) or not isinstance(value.get('records'),list):raise ValueError('Explicit native extended_data.records schema required')
    rows=value['records']
    if any(not isinstance(r,dict) or not isinstance(r.get('application_name'),str) or not r['application_name'] for r in rows):raise ValueError('Readable metadata application identities required')
    return rows


def verify_solid_transfer(source_records,target_records,bindings,*,added_metadata_apps=(),require_all_sources=True,require_all_targets=True):
    """Require bijective complete ACIS/noncommon properties and retained metadata.

    Optional added metadata applications must be disjoint from original apps;
    every original application record is retained with its original multiplicity.
    Display properties in common have their own scope and are not geometry.
    """
    sources,targets=_by_handle(source_records),_by_handle(target_records)
    if not bindings:raise ValueError('Explicit nonempty solid transfer bindings required')
    allowed=set(added_metadata_apps)
    if any(not isinstance(a,str) or not a for a in allowed):raise ValueError('Readable allowed metadata apps required')
    if type(require_all_sources) is not bool or type(require_all_targets) is not bool:raise ValueError('Explicit coverage flags required')
    seen_source=set();seen_target=set();checks=[]
    for binding in bindings:
        sh,th=binding['source_handle'],binding['target_handle']
        if sh in seen_source or th in seen_target or sh not in sources or th not in targets:raise ValueError('Unique existing source/target mapping required')
        seen_source.add(sh);seen_target.add(th);a,b=sources[sh],targets[th]
        if a.get('type')!='Solid3D' or b.get('type')!='Solid3D':raise ValueError('Solid3D source and target required')
        ap,bp=a['properties'],b['properties']
        for props in (ap,bp):
            acis=props.get('acis_data')
            if not isinstance(acis,dict) or not (acis.get('sat_data') or acis.get('sab_data')):raise ValueError('Nonempty complete native ACIS payload required')
        geometry=_canonical({k:v for k,v in ap.items() if k!='common'})==_canonical({k:v for k,v in bp.items() if k!='common'})
        old,new=_apps(a),_apps(b);original_apps={r['application_name'] for r in old}
        if original_apps & allowed:raise ValueError('Added apps must be disjoint from original provenance')
        retained=[r for r in new if r['application_name'] not in allowed]
        metadata=Counter(map(_canonical,old))==Counter(map(_canonical,retained))
        checks.append(dict(source_handle=sh,target_handle=th,result='PASS' if geometry and metadata and a.get('record_type')==b.get('record_type') else 'FAIL',
                           geometry_preserved=geometry,original_metadata_preserved=metadata,
                           source_acis_sha256=hashlib.sha256(_canonical(ap['acis_data']).encode()).hexdigest(),
                           target_acis_sha256=hashlib.sha256(_canonical(bp['acis_data']).encode()).hexdigest()))
    covered=(not require_all_sources or seen_source==sources.keys()) and (not require_all_targets or seen_target==targets.keys())
    return dict(result='PASS' if covered and all(c['result']=='PASS' for c in checks) else 'FAIL',checks=checks,complete_requested_mapping=covered,
                method='exact full native ACIS and noncommon property equality with original metadata multiplicity')
