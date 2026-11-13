# Guarded envelope job runner

Use `scripts/envelope_job_runner.py` to run an external, source-pinned envelope job through the existing OCS `Client`, `Journal`, `envelope_reference`, `source_metadata`, and `save_reopen` APIs. Component names, source values, request namespace, output path, and scope stay in the caller's job directory. The generic runner contains no product identifiers or dimensions.

## Inputs

1. `--job`: external JSON envelope job. It supplies `job_id`, a nonempty `namespace` of at most 64 UTF-8 bytes, `part_id`, `part_name`, `representation`, `geometry_role="reference_envelope"`, `geometry_name`, `units="mm"`, `frame`, `local_frame`, `origin`, `dimension_features`, source-pinned `features`, and optional `envelope_scope` and `output_path`.
2. `--job-dir`: existing external directory for run receipts. Existing journal, native handles, failure, result, or geometry-check receipts block a new native run.
3. `--output`: requested new `.dwg` path. This CLI value controls the output; an optional job `output_path` must resolve to the same path.
4. `--session`: selected OCS session.
5. `--control`: path to the existing OCS control helper.
6. `--cadtools-root`: explicit directory containing `cadtools/runtime.py` and `cadtools/verification.py`.
7. `--modeling-root-name`: name of the caller-supplied root containing reusable `scripts/` helpers.
8. `--root NAME=ABSOLUTE_PATH`: repeat for each explicit portable root needed by the job. Root names are supplied by the caller. Relative source/output locators resolve from the external job file's directory.
9. `--execution-model`: observed model identity for the run record.
10. `--allow-write`: explicit native-write switch. Omit for read-only preflight.

Example shape (values supplied by the external job):

```text
python scripts/envelope_job_runner.py \
  --job /external/job/envelope.json \
  --job-dir /external/job \
  --output '${PROJECT_ROOT}/cad/parts/reference.dwg' \
  --session SESSION \
  --control /path/to/ocs_control.py \
  --cadtools-root /path/to/cad-construction/scripts \
  --modeling-root-name TOOL_ROOT \
  --root PROJECT_ROOT=/path/to/project \
  --root TOOL_ROOT=/path/to/3dmodeling \
  --execution-model OBSERVED_MODEL
```

## Preflight and execution

1. The runner resolves every feature source through caller-supplied roots or the job-directory base, verifies source hashes through `component_records.require_ready`, normalizes stored source metadata to named-root locators, validates envelope parameters, prepares the complete portable metadata payload, checks the `.dwg` destination and replay receipts, and imports `ezdxf.acis.sab.parse_sab` and `SabDataLoader` in the current interpreter. It checks the combined namespace, separator, readable geometry name and longest generated metadata suffix against the installed client's 128-byte UTF-8 request-ID limit before session discovery or document creation. Shorten the caller's labels when that check fails. Existing failure/error JSON and failed source-feature check records also block native replay.
2. Only after saved-body reader preflight succeeds does the runner import the guarded OCS APIs, load the selected control helper, and read the OCS state. It stores a compact snapshot of document IDs, paths, dirty states, active revisions and command/modal state. It does not create a document during default preflight.
3. Native execution requires `--allow-write`. The runner creates one isolated document through the journalled client, confirms existing document identities and dirty/path states, requires an empty drawing audit, sets millimetre INSUNITS and world UCS, then calls `envelope_reference.build_envelope`.
4. `build_envelope` writes its basic metadata with the action label ending `source metadata`; the runner writes the complete payload with a separate action label ending `complete source binding`. Each journalled mutation has its own request identity. Complete metadata includes component identity, readable name, representation, units, local frame, job identity, scope, feature values, original portable source locators, source SHA-256 values and source locations. The runner compares metadata and native geometry before save and again after `save_reopen` against the same native handle.
5. The native audit requires `ok=true`, zero errors and warnings, the expected solid count and the expected entity type count. Save results must report zero dropped entities. The persisted DWG is hashed and recorded with saved/read-back checks. The runner appends a portable action occurrence and updates `progress.json` when present.
6. After geometry, metadata and save/reopen receipts are written, the runner closes its saved/reopened tab and owned construction tab through `ocs_document_cleanup`. Ownership uses the exact two document IDs and recorded paths/geometry revisions; a dirty construction copy also requires the passing saved-file/hash proof. Close requests carry the geometry revision guard. `document-cleanup.json` and `result.json` record the separate cleanup outcome and helper hash. A cleanup follow-up preserves the completed model state and the existing evidence. The runner preserves all pre-existing tabs.
7. If a native request completion is uncertain, the proxy recovers the original journalled request ID. It never submits the geometry operation again. Existing output, journal, native handles, prior failure records or pre-save verification receipts prevent replay.

## Evidence boundary and checks

The envelope helper creates one axis-aligned rectangular volume. A pass proves only the source dimensions and persistence of that reference volume. Source geometry, datum, origin placement and axis mapping remain the external job's responsibility. The helper does not imply a detailed body, mounting interface, connector pose or surrounding assembly transform.

Run the generic synthetic tests with:

```text
python -m unittest tests.test_envelope_job_runner -v
```

The test suite checks named-root resolution, portable metadata with source hashes and scope, namespace/output validation, replay blocking, reader-import failure before OCS discovery, read-only default behavior and fake guarded orchestration. It does not connect to OCS or verify an installed CAD runtime.

## Asynchronous operation recovery

The shared `RecoveringClient` recovers the original journalled request after an
uncertain response. If immediate recovery also exhausts while the operation is
running, it makes three further recovery calls after 0.25, 0.5 and 1 second.
The mutation is sent once. Definite rejection or error propagates immediately;
persistent uncertainty propagates at the fixed bound. Preserve that request and
its journal for read-only follow-up. See the [executed recovery record](../../../execution/bounded-request-recovery-2026-11-13.md).
