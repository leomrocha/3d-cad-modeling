"""Select one value from a reviewer-transcribed variant comparison table.

This module checks table structure and exact row/header association. It does
not read HTML, verify a transcription against its source, or validate source
authenticity; those remain caller-owned evidence checks.
"""


def select_cell(table, variant_header, row_label):
    """Return one cell bound to an exact variant header and row label.

    ``table`` is a normalized caller-supplied mapping with ``table_id``,
    ``source_location``, ``headers`` and ``rows``. Each row has a ``label``
    and a ``values`` list with one nonempty string per header. The caller
    supplies and records source identity, URL, hash, date and transcription
    review separately.
    """
    if not isinstance(table, dict):
        raise ValueError('table must be an object')
    for field in ('table_id', 'source_location'):
        value = table.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(field + ' must be a nonempty string')
    headers = table.get('headers')
    rows = table.get('rows')
    if not isinstance(headers, list) or not headers:
        raise ValueError('headers must be a nonempty list')
    if not isinstance(rows, list) or not rows:
        raise ValueError('rows must be a nonempty list')
    if not isinstance(variant_header, str) or not variant_header.strip():
        raise ValueError('variant_header must be a nonempty exact string')
    if not isinstance(row_label, str) or not row_label.strip():
        raise ValueError('row_label must be a nonempty exact string')

    normalized_headers = []
    for header in headers:
        if not isinstance(header, str) or not header.strip():
            raise ValueError('each header must be a nonempty string')
        normalized_headers.append(header.strip().casefold())
    if len(set(normalized_headers)) != len(normalized_headers):
        raise ValueError('duplicate variant/header labels are ambiguous')
    selected = [index for index, header in enumerate(headers)
                if header == variant_header]
    if len(selected) != 1:
        raise ValueError('variant_header must match exactly one header')

    normalized_labels = set()
    selected_row = None
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('each row must be an object')
        label = row.get('label')
        values = row.get('values')
        if not isinstance(label, str) or not label.strip():
            raise ValueError('each row needs a nonempty label')
        normalized_label = label.strip().casefold()
        if normalized_label in normalized_labels:
            raise ValueError('duplicate table row labels are ambiguous')
        normalized_labels.add(normalized_label)
        if not isinstance(values, list) or len(values) != len(headers):
            raise ValueError('each row must have exactly one cell per header')
        if any(not isinstance(value, str) or not value.strip() for value in values):
            raise ValueError('each table cell must be a nonempty string')
        if label == row_label:
            selected_row = (label, values)
    if selected_row is None:
        raise ValueError('row_label must match exactly one row')

    label, values = selected_row
    index = selected[0]
    return {
        'table_id': table['table_id'],
        'source_location': table['source_location'],
        'variant_header': headers[index],
        'row_label': label,
        'value': values[index],
        'header_index': index,
    }
