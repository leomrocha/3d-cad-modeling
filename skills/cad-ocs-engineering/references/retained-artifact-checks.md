# Retained artifact manifest checks

Use `scripts/retained_artifacts.py` after the final source/path/provenance edits and before the component result commit. It reads caller-owned files and prints a JSON result; it changes no artifact or manifest and connects to no CAD session.

1. Pass the manifest to `python scripts/retained_artifacts.py EXTERNAL_MANIFEST`. It uses the manifest directory for evidence. Add `--job JOB_JSON`, `--project-root PROJECT_DIRECTORY` or `--output SAVED_MODEL` when the manifest refers to those [path origins](paths.md).
2. Supported file records use `path` plus `sha256`, or `retained_path` plus `retained_sha256`. A retained derivative is checked against its retained hash; its original hash remains separate. Relative paths stay within the manifest directory; named-root paths stay within their selected origin. Both `${ROOT_NAME}/path` and the older `ROOT_NAME/path` notation are supported.
3. A null retained path requires an explicit classification or supersession record. Such rows are reported separately. Repeated attributions to the same file and hash are counted separately from unique verified artifacts; conflicting hashes for one path fail. A manifest with no actual retained file fails.
4. The helper reuses `component_records.observe_file` to detect file changes during hashing. It parses saved JSON and JSONL records and checks them again after parsing. The manifest hash is checked before and after the complete pass. Missing files, malformed JSON, stale hashes and escaped paths fail the check.
5. Store the emitted receipt in the component project only after the command succeeds. The receipt records the exact manifest hash, unique file count, repeated attributions and omitted work-only records. A hash/JSON pass establishes retained bytes and record syntax; native geometry, source interpretation and physical behavior retain their own checks.

Synthetic checks: `python -m unittest discover -s tests -p test_retained_artifacts.py`.

## Preflight an indexed model package

Read the destination's current schema and an accepted record of the same type before generating an entry. Check the exact value types used by indexed fields. An intake command that validates the title and asset draft can still accept a record whose material, standard or dimensional entries have the wrong structure for the index builder. Validate the generated record with the destination's supported schema or builder in a draft location before replacing the working indexes. Diff the staged companion and check whitespace, including sections with no entries.

If indexing fails after package preparation, inspect the current catalogue revision and changed paths. Verify the saved model and staged views against the job hashes. When only record metadata is affected, correct the existing entry, regenerate every required index and verify exact lookups and asset paths. Commit the model and regenerated records together after the checked staged diff. Preserve the saved geometry and valid package files during metadata recovery.

## Replace an existing model package revision

Give the construction job a separate folder and a fresh native request namespace. Keep the catalogue ID and asset basenames for the same model identity. Before replacing the catalogue entry, confirm its current revision and native hash, then check that no dependent entry pins that revision. Update affected dependencies as separate scoped work if necessary.

A catalogue locator with a stable ID and basename can resolve to new bytes after replacement. For a downstream preflight that uses earlier verification, check these joins separately:

1. Resolve the current catalogue ID, revision, asset path and file hash. Use that binding when the job calls for the current asset.
2. Resolve each historical receipt to the archived DWG whose bytes match its recorded hash. Preserve that receipt's source identity and measurements with the archived revision.
3. Check the derivative DWG against its own output hash and check the derivative receipt's input hash against the exact predecessor used to create it. A published derivative can also match the current catalogue asset. Both checks still apply.

Record the evidence roles and matching hashes in the new preflight. If a required predecessor cannot be resolved, stop the dependent verification at that missing input. An unchanged catalogue ID or path alone cannot carry forward geometry evidence.

When the reviewed asset set stays the same, call `verify_revision_package(current, replacement, assets, model_name=..., old_sha256=..., new_sha256=...)` from `retained_artifacts.py`. Pass the manifest's sibling filenames and the old and checked new native hashes. It checks both directory inventories, rejects symlinks and returns a digest for every file in each revision. Use the exact checked staged bytes for delivery. Retry a preparation failure with its existing staged files only after comparing them with the checked output. The destination still owns geometry checks, registration, index rebuild and commit.

## Verify a native viewport in a catalogue gallery

Use the successful `save_checkpoint` and `verify_capture` receipts from the same session, document and geometry revision. For receipts without a session ID, establish the shared session from the native request journal. Call `verify_gallery_capture` in [retained_artifacts.py](../scripts/retained_artifacts.py) with the local packages directory, delivered catalogue record and exact preview label. The check compares the indexed model bytes to the checkpoint and the indexed preview bytes to the capture. It returns the record ID, catalogue revision and both hashes. A missing or duplicate label requires a gallery record correction. A hash mismatch identifies the asset to inspect. Visual content review and derivatives such as resized thumbnails have separate checks.
