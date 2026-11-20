# Guarded insertion recovery, resume and assembly verification

## Source-pinned incremental checkpoints

Use [save_checkpoint](../scripts/cadtools/checkpoints.py) with an explicit `job_id`, `source_pins=[{path,sha256}]` and an optional readable part-name-to-handle mapping. Source paths are runtime absolute paths or locators resolved using the selected job record `job_path` and the saved catalogue. The helper checks sources before and after saving, records the source contract, job, session when exposed, document/geometry revision, saved file hash and handles, and preserves the preceding checkpoint on failure. To reopen a stored receipt, supply its path as `receipt_path` and the selected saved DWG as `output_path`. Rooted locators stay inside their declared origins.

Checkpoint counts use the save audit's `manifest.by_type` labels. Native entity records may use different labels for the same object. For example, a record emitted as `LwPolyline` can appear as `Polyline` in the audit. On a count mismatch, reconcile the reported labels against the owned document's exact live handles and intended entity types, then save the existing geometry.

`verify_resume_checkpoint` is an offline gate for a live, idle owned document. Supply the saved receipt, expected job/source pins, current native state, roots and both expected/actual handle mappings when checking them. It verifies the in-progress result, current source hashes, exact saved bytes, session when recorded and document/geometry epoch. It sends no CAD request and infers no completed recipe operations. Reconcile the original action journal before selecting the next operation. A restart that opens a new document needs an explicit new ownership/persistence contract.

Save the created owned document immediately, after each meaningful construction step and before risk, switches or handoff. Resolve an uncertain operation using its original request ID before saving. Save failure stops further modeling. Finish-only resume and arbitrary interrupted construction are separate caller job contracts. Preserve unrelated open documents and original sources. Delete construction profiles only through recorded created-handle ownership; a base drawing can contain unrelated polylines.

For interrupted same-document mutations that complete at an idle boundary, call `recover_idle_mutation` in [cadtools/checkpoints.py](../scripts/cadtools/checkpoints.py). Supply the original label, operation and complete operands from the intended job. The helper checks the journal and exact live revision against the original completion. Read back the affected geometry and save a checkpoint before issuing a dependent mutation. Document opens and unfinished command prompts use their respective recovery procedures.

## Finish after a final-check interruption

Use `verify_finish_checkpoint` in [checkpoints.py](../scripts/cadtools/checkpoints.py) when all planned occurrences were saved after placement and labelling, and final verification was interrupted. Supply the expected save request from the job recipe and journal, the complete role list from the plan, and the independently read live root handles. Verify the same idle document, geometry epoch, source hashes and checkpoint bytes. The result `FINAL_VERIFICATION_PENDING` authorizes the caller's checks only. Read back each occurrence's source identity, native layer and full matrix, then run the final geometry checks and save the definitive file. Keep the last verified checkpoint until that save passes.

Nested definition names may gain numeric suffixes when inserted. Compare intended occurrences using the expected parent, actual transformed geometry and independent source datums, and retain the real handle path in the result. Require unique matches. A literal nested name alone is insufficient.

## Save a completed insertion before labelling

Pass `checkpoint(handle)` as the optional `checkpoint` argument of `insert_component`. It runs after the native insertion completes and the helper verifies the idle document, inserted handle, transform and reused block identity. Use a source-pinned save and raise on failed or uncertain persistence. The helper stops before writing provenance when the save raises. After the callback, its document and geometry revision must still match. Record the saved Insert handle and recover any subsequent metadata request by its original ID.

## Accept only verified INSERT defaults

Use [insert_recovery.py](../scripts/insert_recovery.py) after resolving the previous request's known/unknown status and inspecting the live owned prompt. Select one serialized native writer interval. Existing [runtime](ocs-runtime.md) request bounds and recovery remain authoritative.

1. `insert_default_contract(state, stage=..., planned_value=...)` supports the inspected English INSERT X-scale, Y-scale and rotation prompts. It checks document/revision identity, command name, Enter support, modal/pending-operation state and the complete displayed default. Numeric defaults must equal the caller's planned value. The symbolic Y default `use X scale factor` requires the immediately preceding verified X-scale receipt from the same document/revision/geometry epoch. Different or unrecognized defaults stop.
2. Persist the returned contract with the caller's job. `accept_insert_default(client,label,contract,exclusive_interval=True,checkpoint=...)` binds it durably in the operation journal before one Enter. It checks the contract again, uses the original request ID for uncertain completion/restart, and verifies the expected next prompt. Never replay a prior point request because its error or cancellation message was observed.
3. Rotation completion requires a checkpoint callback. The callback runs after the command is idle. A checkpoint exception stops the job with the completed Insert retained for recovery. Active intermediate prompts require bounded command continuation to the next saveable boundary.
4. The supported prompt grammar is deliberately bounded to the inspected interface. Other installed prompt layouts require inspection and a separate supported contract. A command error alone does not establish whether geometry or placement changed.

## Correct and verify the actual insertion point

`correct_insert_point` in [assembly_build.py](../scripts/assembly_build.py) takes an exact owned Insert handle, caller point and complete intended 4x4 matrix, inspected schema paths, separate length/dimensionless matrix tolerances, serialized writer interval and a checkpoint callback.

It requires an idle document, stable record read, schema support for `/insert_point` and proof that a point-only change produces the entire intended placement. It checkpoints before a new update, submits one expected-old-value property change with the geometry epoch, verifies all other Insert properties and the complete resulting matrix, then checkpoints again. A journalled update is recovered through the original request ID and its completed geometry epoch is checked against readback. It sends no replacement insertion, command cancellation, scale change or rotation change.

The original requested point and actual saved point have separate evidence. Preserve the old record, compare-and-set request, result and failed attempt. Source files, intended transforms, tolerances, handles and metadata remain caller inputs. Existing `insert_component` keeps its explicit-prompt behavior; recovery is an explicitly selected procedure.

## Continue a recovered file input at the insertion-point prompt

Use `continue_insert_after_file` in [assembly_build.py](../scripts/assembly_build.py) when the original file input was journaled, a bounded recovery returns `waiting_input` at the insertion-point prompt, and no later token was submitted. Use the same session, document and journal within the exclusive writer interval. Supply the source hash, original label, intended point and Y scale, and a checkpoint callback receiving the new Insert handle. The helper checks the original file operand, current prompt and response epoch before sending each remaining token once. It calls the checkpoint after confirmed idle completion and before provenance writes. Recover a later submitted input by its own request identity. Preserve the prior checkpoint while an active prompt prevents saving.

## Recover a completed insertion before provenance

Use `recover_insert_component` from [assembly_build.py](../scripts/assembly_build.py) when an interrupted runner already submitted the final `-INSERT` rotation token and has yet to send the provenance write. Supply the same owned client and journal, definition path, preflight source hash, original label and point/scale contract. Recover the completed rotation request by its existing identity. The helper checks the journaled prompts and operands, source file hash, current idle document revision, added native Insert handle and exact starting placement before attaching source provenance. Checkpoint the recovered insertion immediately. When the provenance operation already has a journal intent, resolve that operation from the existing request and checkpoint instead.

## Repeated nested placements and source-world geometry

Use [assembly_verification.py](../scripts/assembly_verification.py) with one declared XYZ frame and length unit.

1. `verify_nested_placements` expands source/target roots with the existing nested instance reader, verifies complete ACIS/noncommon properties and original metadata through [solid transfer](reversible-source-workflows.md), and matches occurrence matrices against explicit source/target geometry bindings. It preserves repeated and coincident occurrence multiplicity. Unit reflection or uniform scale requires the existing explicit reader opt-in. Unsupported block bases, arrays, cycles and exceeded instance bounds stop through the reader.
2. `compare_occurrence_matrices` accepts already expanded occurrences and bijective geometry-definition bindings. Translation tolerance uses the declared length unit; the linear matrix coefficient tolerance is dimensionless. Occurrence paths must be unique. Matching is one-to-one within the tolerance; a global matrix multiset cannot exchange different geometry definitions without detection.
3. `match_world_vertices` takes unique occurrence IDs, complete world point sets, face counts and explicit closed-topology flags. A bounded augmenting-path match handles repeated geometry and multiple compatible candidates. It rejects missing occurrences, changed vertex sets, wrong face counts or open topology. Its scope is vertex sets and topology observations. Analytic surface equations, trims and source-domain coverage retain their own checks. Preserve the original source matrices used to construct the supplied world points.
4. `check_world_envelope` compares actual world vertices with caller-supplied permitted bounds and length tolerance. It returns actual bounds, disjoint status and PASS or SOURCE_REVIEW_REQUIRED. It chooses no dimension threshold, assigns no placeholder identity and modifies no source/model. Preserve the selected candidate, original aggregate and their hashes. Any omission is an explicitly authorized operation on a separate owned derivative.
5. Keep source bodies, repeated physical instances, construction solids and top-level roots separately named and counted. Verify final source hashes and saved/reopened model identity before [closing completed owned documents](document-cleanup.md). Protect active/unrelated paths, dirty states and revisions through every operation.

When the native record inventory supplies handles without role labels, pass the complete live handle sequence as `observed_handles` and the checkpoint contract as `expected_handles` to `verify_resume_checkpoint`. This mode checks the exact handle inventory and preserves the saved role mapping. Use `actual_handles` instead when the live records independently establish role labels.


When a completed native deletion leaves erased handles in the Model Space block list, use `model_space_live_handles` from [records.py](../scripts/cadtools/records.py). Supply the stable Model Space and full entity inventories from one current idle epoch, the named expected root handles and the original same-document delete intent and completed response. Only explicitly erased handles absent from the live inventory can be excluded. Keep the original block list and journal, pass the result's live handles to the resume check and filter only those proven erased references in a local traversal copy. The helper rejects unknown dangling references, still-live deleted handles, missing expected roots and omitted completion evidence.

### Place a rotated occurrence with an existing mirror

Use `assembly_repair.apply_source_placements(..., allow_unit_reflection=True)` when the named Insert already has X and Z scale +1 and signed unit Y scale. Supply its observed matrix and an independently derived target with the same handedness. Calculate the placement fields with `native_fields`. The helper preserves all scales, checks the target before mutation and verifies the full reflected matrix after the write. Save the insertion before placement and save each successfully placed occurrence.
