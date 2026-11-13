# Retained artifact manifest checks

Use `scripts/retained_artifacts.py` after the final source/path/provenance edits and before the component result commit. It reads caller-owned files and prints a JSON result; it changes no artifact or manifest and connects to no CAD session.

1. Pass the external manifest and its named roots: `python scripts/retained_artifacts.py EXTERNAL_MANIFEST --root PROJECT_ROOT=ABSOLUTE_PROJECT_PATH`. Add another `--root` for a root explicitly referenced by the manifest.
2. Supported file records use `path` plus `sha256`, or `retained_path` plus `retained_sha256`. A retained derivative is checked against its retained hash; its original hash remains separate. Relative paths stay within the manifest directory; named-root paths stay within their explicitly supplied root. Both `${ROOT_NAME}/path` and the older `ROOT_NAME/path` notation are supported.
3. A null retained path requires an explicit classification or supersession record. Such rows are reported separately. Repeated attributions to the same file and hash are counted separately from unique verified artifacts; conflicting hashes for one path fail. A manifest with no actual retained file fails.
4. The helper reuses `component_records.observe_file` to detect file changes during hashing. It parses saved JSON and JSONL records and checks them again after parsing. The manifest hash is checked before and after the complete pass. Missing files, malformed JSON, stale hashes and escaped paths fail the check.
5. Store the emitted receipt in the component project only after the command succeeds. The receipt records the exact manifest hash, unique file count, repeated attributions and omitted work-only records. A hash/JSON pass establishes retained bytes and record syntax; native geometry, source interpretation and physical behavior retain their own checks.

Synthetic checks: `python -m unittest discover -s tests -p test_retained_artifacts.py`.
