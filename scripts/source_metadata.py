"""Compare string metadata with an actual native entity record.

The caller supplies the application name and the expected readable lines.
The supported payload is the ordered string chunks written by Geometry.metadata.
Native document/revision binding belongs to the caller's retained read receipt.
"""


def compare_source_metadata(record, requested_handle, application, expected_lines,
                            chunk_size=100):
    """Check identity and compare ordered native string chunks exactly."""
    for label, value in [('requested_handle', requested_handle),
                         ('application', application)]:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(label + ' must be a nonempty string')
    if not isinstance(record, dict) or record.get('handle') != requested_handle:
        raise ValueError('Native record handle differs from requested handle')
    if type(chunk_size) is not int or chunk_size <= 0:
        raise ValueError('chunk_size must be a positive integer')
    if not isinstance(expected_lines, (list, tuple)) or not expected_lines \
            or any(not isinstance(line, str) or not line for line in expected_lines):
        raise ValueError('Expected metadata needs nonempty string lines')
    expected = [line[i:i + chunk_size] for line in expected_lines
                for i in range(0, len(line), chunk_size)]
    properties = record.get('properties')
    if not isinstance(properties, dict):
        raise ValueError('Native record properties are required')
    common = properties.get('common')
    if not isinstance(common, dict):
        raise ValueError('Native common properties are required')
    extended = common.get('extended_data')
    if extended is None:
        entries = []
    elif isinstance(extended, dict) and isinstance(extended.get('records'), list):
        entries = extended['records']
    else:
        raise ValueError('Unsupported native extended_data format')
    if any(not isinstance(entry, dict) for entry in entries):
        raise ValueError('Native extended_data entries must be records')
    matches = [entry for entry in entries
               if entry.get('application_name') == application]
    if len(matches) > 1:
        raise ValueError('Duplicate metadata application records')
    observed = []
    if matches:
        values = matches[0].get('values')
        if not isinstance(values, list):
            raise ValueError('Native metadata values must be a list')
        for value in values:
            if not isinstance(value, dict) or set(value) != {'String'} \
                    or not isinstance(value['String'], str):
                raise ValueError('Expected native string metadata values')
            observed.append(value['String'])
    return {'result': 'PASS' if observed == expected else 'FAIL',
            'method': 'ordered native extended-data string chunk comparison',
            'handle': requested_handle, 'application': application,
            'chunk_size': chunk_size, 'application_present': bool(matches),
            'observed': observed, 'expected': expected}
