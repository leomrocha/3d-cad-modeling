"""Expand caller-supplied assembly records and recover completed insertion evidence."""
from collections import Counter
import hashlib
import json
from pathlib import Path
from step_placements import eye,multiply,classify_hand


def placement(child):
    if 'matrix' in child:value=child['matrix']
    else:
        x,y,z=child.get('point',[0,0,0]);value=[[1,0,0,x],[0,child.get('yscale',1),0,y],[0,0,1,z],[0,0,0,1]]
    classify_hand(value)
    return value


def expand_occurrences(root,groups,*,max_occurrences=100000,max_depth=128):
    """Group IDs identify records; leaf IDs identify parts, irrespective of solid count."""
    if type(max_occurrences) is not int or max_occurrences<1:raise ValueError('Positive occurrence bound required')
    if type(max_depth) is not int or not 1<=max_depth<=128:raise ValueError('Depth bound must lie in 1..128')
    out=[]
    def visit(key,matrix,path,active):
        if key in active:raise ValueError('Cyclic assembly records')
        if len(active)>=max_depth:raise ValueError('Assembly depth bound exceeded')
        group=groups[key]
        for child in group['children']:
            source=child['source'];transform=multiply(matrix,placement(child));ancestry=path+[child['name']]
            digest=child.get('source_sha256')
            if not isinstance(digest,str) or len(digest)!=64 or any(c not in '0123456789abcdef' for c in digest):raise ValueError('Insertion-time source digest required')
            if source in groups:
                if groups[source]['sha256']!=digest:raise ValueError('Inserted group revision differs from expansion record')
                visit(source,transform,ancestry,active|{key})
            else:
                if len(out)>=max_occurrences:raise ValueError('Occurrence bound exceeded')
                out.append(dict(part=source,source_sha256=digest,name=child['name'],hand=classify_hand(transform),matrix=transform,path=ancestry))
    visit(root,eye(),[],set())
    if not out:raise ValueError('No leaf part occurrences reached')
    counts=Counter((r['part'],r['source_sha256'],r['hand']) for r in out)
    return dict(occurrences=out,quantities=[dict(part=p,source_sha256=h,hand=hand,quantity=n) for (p,h,hand),n in sorted(counts.items())])


def rollup_embedded_parts(root, records, *, asset_sha256, max_occurrences=100000, max_depth=128):
    """Count leaf packages from proven, embedded catalogue dependencies."""
    if not callable(asset_sha256):
        raise ValueError('A caller-supplied asset hash reader is required')
    if type(max_occurrences) is not int or max_occurrences < 1:
        raise ValueError('Positive occurrence bound required')
    if type(max_depth) is not int or not 1 <= max_depth <= 128:
        raise ValueError('Depth bound must lie in 1..128')
    hashes = {}
    quantities = Counter()
    total = 0

    def model_hash(key):
        if key not in hashes:
            digest = asset_sha256(records[key])
            if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
                raise ValueError('A lowercase SHA-256 is required for ' + key)
            hashes[key] = digest
        return hashes[key]

    def visit(key, factor, active):
        nonlocal total
        if key in active:
            raise ValueError('Cyclic embedded dependency at ' + key)
        if len(active) >= max_depth:
            raise ValueError('Embedded dependency depth exceeded')
        if factor > max_occurrences:
            raise ValueError('Occurrence bound exceeded')
        if key not in records or records[key].get('id') != key:
            raise ValueError('Embedded package identity is missing or differs: ' + key)
        row = records[key]
        model_hash(key)
        members = [r for r in row.get('model_references', []) if r['dependency'] == 'embedded']
        if not members:
            total += factor
            if total > max_occurrences:
                raise ValueError('Occurrence bound exceeded')
            quantities[key] += factor
            return
        names = set()
        for member in members:
            child = member['id']
            labels = member['occurrences']
            if (not isinstance(labels, list) or not labels
                    or any(not isinstance(label, str) or not label.strip() for label in labels)
                    or len(set(labels)) != len(labels) or names.intersection(labels)):
                raise ValueError('Missing or duplicate occurrence labels in ' + key)
            if child not in records or member['revision'] != records[child].get('revision'):
                raise ValueError('Embedded package revision differs: ' + child)
            if member['sha256'] != model_hash(child):
                raise ValueError('Embedded package bytes differ: ' + child)
            names.update(labels)
            visit(child, factor * len(labels), active | {key})

    visit(root, 1, set())
    return dict(root=root, root_sha256=hashes[root], total_occurrences=total,
                quantities=[dict(id=key, revision=records[key].get('revision'), sha256=hashes[key],
                                 quantity=quantity) for key, quantity in sorted(quantities.items())])


def recover_insert_sequence(events,*,prefix,count,source_digest):
    """Recover the declared file/point/xscale/yscale/rotation/provenance protocol."""
    if type(count) is not int or count<1:raise ValueError('Positive insertion count required')
    intents={};replies={}
    for event in events:
        if event.get('event')=='intent':
            req=event['request'];key=req['request_id']
            if key in intents:raise ValueError('Duplicate insertion intent')
            intents[key]=req
        elif event.get('event')=='response':replies.setdefault(event['request_id'],[]).append(event['response'])
    children=[]
    for i in range(count):
        base=prefix+':member-'+str(i)+'-'
        for suffix in ('file','point','xscale','yscale','rotation','provenance'):
            key=base+suffix;responses=replies.get(key,[])
            if key not in intents or not responses:raise ValueError('Incomplete insertion evidence')
            if any(r.get('status') in ('failed','rejected','cancelled') for r in responses):raise ValueError('Failed insertion response retained')
            terminal=[r for r in responses if r.get('status') not in ('accepted','running') and r.get('code')!='response_timeout']
            allowed=('completed',) if suffix in ('rotation','provenance') else ('completed','waiting_input')
            if not terminal or any(not r.get('ok') or r.get('status') not in allowed for r in terminal):raise ValueError('Insertion step not confirmed')
            if any(r!=terminal[0] for r in terminal[1:]):raise ValueError('Conflicting terminal insertion responses')
        source=intents[base+'file']['text'];digest=source_digest(source)
        text=''.join(row['value'] for row in intents[base+'provenance']['data'] if row['code']==1000)
        if 'Source DWG SHA256 '+digest not in text:raise ValueError('Insertion source hash differs')
        if float(intents[base+'xscale']['text'])!=1 or float(intents[base+'rotation']['text'])!=0:raise ValueError('Unsupported insertion sequence transform')
        child=dict(name=Path(source).stem,source=source,source_sha256=digest,point=intents[base+'point']['point'],yscale=float(intents[base+'yscale']['text']))
        placement(child);children.append(child)
    return children


def write_occurrence_tables(directory,stem,result,*,roots=None):
    """Retain quantities and placements as independently verified hashed TSV files."""
    from retained_artifacts import write_table
    from envelope_job_runner import portableize
    directory=Path(directory)
    if not directory.is_dir() or not stem or Path(stem).name!=stem:raise ValueError('Existing output directory and basename required')
    parts=directory/(stem+'-parts.tsv');instances=directory/(stem+'-instances.tsv')
    if parts.exists() or instances.exists():raise ValueError('Preserve existing occurrence tables')
    stored=portableize(result,roots or {})
    quantities=stored['quantities'];occurrences=stored['occurrences']
    if any(Path(row['part']).is_absolute() for row in quantities+occurrences):raise ValueError('Stored part paths require explicit named roots')
    if sum(row['quantity'] for row in quantities)!=len(occurrences):raise ValueError('Quantity total differs from occurrence count')
    expected=Counter((r['part'],r['source_sha256'],r['hand']) for r in occurrences)
    reported={(r['part'],r['source_sha256'],r['hand']):r['quantity'] for r in quantities}
    if len(reported)!=len(quantities) or reported!=expected or any(type(n) is not int or n<=0 for n in reported.values()):raise ValueError('Reported quantities differ from actual occurrences')
    positions=[dict(name=r['name'],part=r['part'],source_sha256=r['source_sha256'],hand=r['hand'],path=json.dumps(r['path']),matrix=json.dumps(r['matrix'],allow_nan=False)) for r in occurrences]
    for row in occurrences:
        if classify_hand(row['matrix'])!=row['hand']:raise ValueError('Occurrence hand differs from placement')
    return dict(parts=write_table(parts,quantities,['part','source_sha256','hand','quantity']),instances=write_table(instances,positions,['name','part','source_sha256','hand','path','matrix']))
