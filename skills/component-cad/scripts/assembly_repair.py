"""Apply a reviewed STEP/native placement plan using the existing guarded client.

Source association and plan selection remain agent decisions. This function
preflights all affected records, performs compare-and-set writes once, and
checks readback plus unchanged underlying solid definitions. The client owns
journalling and same-request recovery; an exception preserves partial results.
"""
from step_placements import native_matrix, native_fields, near


def apply_source_placements(client, changes, original_records):
    if not changes:
        raise ValueError('A reviewed nonempty placement plan is required')
    originals = {r['handle']: r for r in original_records}
    if len(originals) != len(original_records):
        raise ValueError('Duplicate original native handle')
    handles = [p['handle'] for p in changes]
    if len(set(handles)) != len(handles):
        raise ValueError('Duplicate planned native handle')
    prepared = []
    # Reject an inconsistent plan or already changed document before any write.
    for item in changes:
        handle = item['handle']
        original = originals[handle]
        if original['type'] != 'Insert':
            raise ValueError('Placement repair requires native insert records')
        if not near(native_matrix(original['properties']), item['before']):
            raise ValueError('Plan baseline differs from original record')
        fields = native_fields(item['expected'])
        if not near(native_matrix(dict(original['properties'], **item['fields'])), item['expected']):
            raise ValueError('Planned fields differ from source target')
        actual = client.read('records', collection='entities', handles=[handle], limit=1)['records'][0]
        if actual['properties'] != original['properties']:
            raise ValueError('Native insertion changed since source review: ' + handle)
        prepared.append((item, actual, fields))
    observations = []
    for item, old, fields in prepared:
        handle = item['handle']
        updates = [{'path': '/' + k, 'value': v, 'expected': old['properties'][k]}
                   for k, v in fields.items()]
        client.mutate('source-placement-' + handle, 'set_properties',
                      collection='entities', handle=handle, updates=updates)
        actual = client.read('records', collection='entities', handles=[handle], limit=1)['records'][0]
        if not near(native_matrix(actual['properties']), item['expected']):
            raise ValueError('Native placement readback differs: ' + handle)
        observations.append({'handle': handle, 'source_id': item['source_id'],
                             'result': 'PASS', 'record': actual})
    count = 0
    for original in original_records:
        if original['type'] != 'Solid3D':
            continue
        actual = client.read('records', collection='entities', handles=[original['handle']], limit=1)['records'][0]
        if actual['properties']['acis_data'] != original['properties']['acis_data']:
            raise ValueError('Underlying solid definition changed: ' + original['handle'])
        count += 1
    return {'result': 'PASS', 'placements': observations, 'solid_definitions_preserved': count,
            'method': 'Reviewed source matrices, compare-and-set native fields, readback and exact ACIS equality'}
