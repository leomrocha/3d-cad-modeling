# Source-defined envelope reference

Use `${MODELING_ROOT}/scripts/envelope_reference.py` when the source supports an overall product or clearance envelope and a detailed component body is not available. The output is one axis-aligned reference volume. It carries no implied PCB outline, mounting surface, connector locations or physical construction.

## Input and preflight

1. Run the existing component model start gate and inspect the owning project's input sheet, manifest, work record, model links, CAD index and file inventory.
2. Preserve each source original under the owning component job, with exact URL, retrieval time, MIME, local path, byte count and SHA-256. Keep source claim, user input and calculated value labels.
3. Pin every envelope dimension in the external job through `component_records.py`. The job supplies readable `part_id`/`part_name`, `job_id`, `representation`, `geometry_role="reference_envelope"`, `geometry_name`, `units="mm"`, `frame`, `local_frame`, `origin` and a `dimension_features` mapping for `x`, `y` and `z` to three distinct required source-feature names.
4. Each mapped feature must have a finite positive value, matching units, source path and expected source hash, source locator, and evidence status. `parameters(job)` runs the existing source readiness check and validates all dimensions, origin coordinates, names, role and numerical tolerance before the helper loads the OCS geometry adapter. An optional nonempty `envelope_scope` supplies the source's stated coverage for native metadata and the verification expectation; omit it to preserve the earlier job format.
5. Before the first native write, check the exact Python runtime that will read back the saved ACIS body. For SAB checks, run an import check for `ezdxf.acis.sab.parse_sab` and `SabDataLoader` with the same interpreter and `PYTHONPATH` planned for save/reopen verification. If imports fail, select an already installed runtime or stop before creating a document; do not discover the dependency only after saving.
6. The supported construction frame is the explicit local XY profile and +Z extrusion. The caller owns any transform into a larger assembly. Values are millimetres; no unit conversion is implicit.

## Construction and checks

1. `build_envelope(client, job)` forms four profile corners from the supplied origin and X/Y spans, then uses the existing `Geometry.extrude` and guarded `SelectionCheckedClient` route for the Z span. It adds readable metadata with the external component name, representation, units, frame and job identity. When `envelope_scope` is supplied, it appends the source-coverage statement to that same metadata record.
2. The representation must remain a reference envelope. Do not add undimensioned details or label the output as detailed component geometry.
3. `inspect(client, {"envelope": handle}, job)` reads the actual OCS solid. It binds the check to `client.document_id`, requires the returned entity handle and `Solid3D` type to match, and confirms active document, document revision and geometry revision remain stable around the record read. SAT inspection uses the existing identity-transform point reader; SAB inspection uses the native ACIS body reader. `verify(features, job)` compares native vertex extrema to the three source-bound extents and checks the closed body when topology is available. The numerical tolerance is a software comparison threshold, separate from source/manufacturing tolerance. Its result carries the optional `envelope_scope` for evidence review.
4. Save to a new authorized native document path, reopen the saved file, then repeat the readback checks against the reopened document. Compare pre-save SAT points with reopened SAB through the existing `small_bms.compare_sat_sab` helper where supported. Record output hash and exact native document identity separately from component identity.
5. The scope text returned by `verify()` comes from the job. Use the [native source-metadata comparison](source-metadata.md) on actual `CADTOOLS_SOURCE` xdata when checking metadata persistence. `Geometry.metadata` uses `xdata_set`; write identity, units, frame, job and optional scope together because another call for that application replaces the previous values.
6. Keep the source-defined detail gate separate. A reference-envelope pass establishes only the checked dimensions and persistence of the represented reference volume.

## Verification scope

`tests/test_envelope_reference.py` uses synthetic, temporary source fixtures. It checks parameterized profile/extrusion values, rejects a zero dimension and a detailed-body role before loading geometry or issuing writes, and checks passing and failing native vertex extrema. These tests exercise the generic preflight and comparison contract; they do not validate a physical product or an OCS installation.
