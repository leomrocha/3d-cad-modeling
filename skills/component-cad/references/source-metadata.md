# Check saved native source metadata

Use [source_metadata.py](/home/leo/projects/3dmodeling/scripts/source_metadata.py) when verifying the string metadata written by the existing OCS `Geometry.metadata` adapter.

1. Retain the actual native entity record from the intended document and geometry revision. Pass that record, its requested handle, the metadata application name and the expected source lines to `compare_source_metadata`. The caller retains document and revision binding with the read receipt.
2. The comparator reads `properties.common.extended_data.records`, selects the unique matching `application_name` and compares its ordered `String` values with the expected lines split into 100-character chunks. This matches the exercised adapter's string-chunk format. A different chunk size is an explicit caller input for a different known writer.
3. A missing application or differing text/order returns FAIL with actual and expected chunks. A wrong entity handle, duplicate application record or unsupported payload raises a format/identity error. The function performs no native mutation.
4. Compare both pre-save and reopened native records when establishing persistence. A check result that repeats the caller's expected scope text alone does not establish stored native metadata.
5. Write identity, representation, units, frame, source job and scope together. The existing adapter uses replacement `xdata_set` for one application; separate writes replace the preceding values.

Nine synthetic tests exercise full payload retention, a scope-only overwrite, changed scope/order, a different/missing application, wrong handle, duplicate application and malformed values. Component-specific expected lines and actual records remain in the component project.
