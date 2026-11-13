# Exact variant columns in source tables

Use `${MODELING_ROOT}/scripts/source_variant_table.py` when a manufacturer or engineering table places specifications for multiple variants in adjacent columns. The helper selects one cell from an explicitly transcribed table using the exact column header and exact row label.

1. The caller records the original source URL or local source path, retrieval or observation date, source title, content type, source hash when a file was retained, the table location, and a reviewer-checked transcription. The helper does not fetch, parse, authenticate, or compare the transcription with the source.
2. Supply a table object with the numbered fields `table_id`, `source_location`, `headers`, and `rows`. `headers` preserves the source column labels. Each row contains `label` and a `values` list in the same order as `headers`; each row must have one nonempty string cell per header.
3. Call `select_cell(table, variant_header, row_label)` with the exact source header and row label. The returned record includes the selected header, row, raw cell text, source table location, and header index. The result records a table transcription association; it does not establish the authenticity of that transcription or the physical accuracy of the source claim.
4. The helper rejects missing or repeated headers, a header with no exact match, repeated row labels, malformed rows, empty cells, and a missing exact row label. Header and row duplicate detection is case-insensitive after trimming whitespace; selection itself requires exact case-sensitive text.
5. Keep adjacent variant values as separate source claims. A value from a neighboring column cannot support the requested product unless the source explicitly maps that column to that product.
6. Apply product-specific units, evidence status, original source URL/path, source hash, date, and concrete feature checks in the external component job. A successful selector result is not a geometry or native CAD check.

`tests/test_source_variant_table.py` uses synthetic table records. It checks exact column association, duplicate and malformed input rejection, and neighbor-column separation. It does not inspect a product source or validate a component.
