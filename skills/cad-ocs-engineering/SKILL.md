---
name: cad-ocs-engineering
description: Create, inspect and revise native engineering geometry in OpenCADStudio with explicit parts, units, frames, source-bound measurements, incremental saves and guarded request recovery. Use for CAD modeling and automation, component reuse checks, assembly placements and saved native views.
---

# CAD OCS Engineering

Use the [operation selection procedure](references/modeling-operation-selection.md) for component reuse, provider capability checks and job evidence. Apply it to the requested operation. Open the local operation catalogue on first use and after a request to refresh available skills.

Use the bundled native-control, geometry and verification helpers. Supply component inputs and output locations through the caller's job. Keep detailed solids, reconstructed shapes and clearance envelopes explicitly labeled.

## First response for a modeling job

Before creating job files, tell the user:

> During this job I’ll save modeling files, scripts and check results in your local project. You can reuse the scripts and procedures on future jobs. These files stay local. If the job produces a reusable improvement, I’ll ask whether you want to contribute it. You’ll see the exact changes before choosing whether to open a GitHub pull request.

Proceed with the authorized modeling work. Ask about participation at completion when there is a specific improvement to share.

## Package setup

Use Python 3.12 on Linux or macOS, the pinned requirements.txt dependencies and an already-running OpenCADStudio native-control session. SKILL_ROOT identifies this installed directory. All helper and procedure links resolve within this package.

```sh
"$SELECTED_PYTHON" "$SKILL_ROOT/scripts/package_check.py"
```

Select the existing session explicitly with --session SESSION or --descriptor DESCRIPTOR_JSON where supported. Read [runtime and recovery](references/ocs-runtime.md), [native control](references/ocs-control.md) and [caller paths](references/paths.md) before connection. Keep session credentials private.

## Establish the modeling contract

1. Read the task and owning-project instructions. Identify the authorized inspection, construction, revision, saving, conversion or simulation scope. Preserve existing authorization and source originals.
2. Bind source identities, hashes, representation, units, origin, right-handed axes, datums, named parts and interface requirements. Source dimensions, assumptions, proposals and measured geometry retain their own evidence labels.
3. Use [component records](references/component-procedure.md) for required features and readiness. Resolve a named required input before dependent construction. Match drawing extension-line endpoints and measurement kind using [drawing-feature checks](references/drawing-feature-checks.md).
4. Keep materials separate from display colors. Use explicit source/job values for physical properties, loads, limits, tolerances and reference geometry.

For freehand designs, use the [concept sketch handoff](references/source-view-evidence.md#use-a-hand-drawn-concept-for-cad) to select catalogue parts and distinguish layout intent from feature dimensions.

For ruler photographs or parts dimensioned across several views, follow the [photo and multi-view drawing procedure](references/source-view-evidence.md#ruler-photographs-and-multi-view-blueprints) before using the affected coordinates in a sketch. For mating parts, record the intended interface and its dimensional limits using [assembly evidence](references/assembly-evidence.md#judge-a-mating-interface).

### Check existing component implementations

Inspect actual matching models and all manifest, work-record, input-sheet and CAD-index references, including NOT_STARTED entries. Mark matching completed components DONE with their readable names, actual model paths and recorded checks. Reuse that geometry and those checks, then select an unfinished item. Construction starts only after reconciliation establishes that the required matching model is absent. Follow [model inventory](references/existing-model-start-check.md).

## Construct and check bounded changes

1. Inspect installed command/entity/record schemas and native state before unfamiliar requests. Select one existing session and one owned document. Bind each mutation to its document, expected revision and stable request ID. Use one writer and a coordinated exclusive interval for interactive native sequences.
2. Bind NEW and OPEN to their exact completed response document IDs using [owned document helpers](scripts/cadtools/runtime.py). An active state read verifies that ID. Stop on external activation, changed geometry or an unexpected command/prompt; preserve the existing request and checkpoint.
3. accepted/running and response_timeout require bounded same-ID polling. waiting_input requires inspected prompt handling. Recover a lost response using the original intent's session/document context. A completed mutation is never replayed under a new ID.
4. Use [stable records](scripts/cadtools/records.py), supported [native geometry](scripts/native_geometry.py) and [feature comparisons](references/shared-feature-checks.md). Keep expected source dimensions independent of measurements. Record actual handles and document/geometry revisions.
5. Use [insertion, resume and assembly verification](references/insertion-resume-verification.md), [reversible source workflows](references/reversible-source-workflows.md), [exact source checks](references/exact-source-checks.md) and [reusable geometry and assembly methods](references/generic-integration.md) for plates, bounded profiles, rounded sections, sidewall cuts, placement matrices, insertion and quantities. Supply all component constants through the job.
6. Inspect corresponding native model views. [Boundary rendering](scripts/native_views.py) uses native SAT and SAB solid records, straight polylines and actual nested placements. Record unsupported trim endpoints as displayed points. A displayed sample extent has its own measurement scope.
7. Use [surface and mesh recovery](references/surface-mesh-recovery.md) for precision-controlled rational evaluation, open-triangle validity, DXF layer derivatives and recorded cancellation checks. Respect the caller's authorized save-only or save/reopen persistence method and label its evidence explicitly.

### Save work in progress

1. **Save files and native models incrementally while their status is IN_PROGRESS.** Save the created owned document immediately, then after each meaningful modeling step, and before a long or failure-prone operation, pause or handoff. Set a maximum interval between saves for the job, using elapsed time or completed operations, and split long runs into batches that reach saveable boundaries within that interval. Completion requires another save of the final revision.
2. Use caller-owned output paths and the authorized native format/version. Pass the absolute checkpoint path, DWG format and version 2018 to the pre-save audit for a native DWG checkpoint. Keep source originals unchanged. Retain the previous verified checkpoint while writing a new versioned checkpoint; for supporting files, use a verified temporary-file replacement when supported. Keep checkpoints in persistent job storage through restart and handoff.
3. Save at an idle command boundary on the exact owned document, using its current revision and a stable request ID. Resolve a pending command or uncertain operation through its recorded identity before saving. An active command that prevents saving requires a shorter batch or a supported resumable boundary before more construction proceeds.
4. Verify each save's actual completion, expected path, persisted file and SHA-256; inspect the save audit and dropped-data report where supported. Persist the document ID, geometry revision, checkpoint path/hash, completed operation and resume information with the job. Preserve the previous verified checkpoint if saving or verification fails, and resolve that failure before further model changes. Recover an uncertain save by its original request ID.
5. Resume from the latest verified checkpoint together with the operation journal, checking document identity and already committed effects before further edits. Keep IN_PROGRESS and completed states explicit. Final geometry, metadata and save/reopen checks apply to the completed revision before document cleanup.

### Execute and improve component jobs

1. Record readable action/component identities, source inputs, prerequisites, outputs, representations, units/frames, actual checks and completed/failed operation evidence in caller-owned persistent job storage.
2. Reuse supported shared helpers before writing replacements. Preserve existing function contracts and source attribution. Keep component recipes and dimensions in job inputs.
3. Check geometry and metadata before/after saving; verify actual source/model/image/table hash relationships through [retained artifacts](references/retained-artifact-checks.md).
4. Close completed owned documents only after saved-model persistence and final checks, using [document cleanup](references/document-cleanup.md). Preserve ongoing and unrelated documents, failed attempts and source originals.
5. Require an applied, verified reusable improvement and run the [component completion gate](references/component-completion.md) before recording DONE. Preserve partial models when a later stage fails.
6. Validate the installed package through [package completion](references/package-completion.md). Report actual executing model identity when exposed; otherwise record unavailable. Keep code checks, native execution, inspected pixels and acceptance separate.

## Procedure selection

1. **Source interpretation:** [dimension limits and datums](references/dimension-limits-and-datums.md), [source-view evidence](references/source-view-evidence.md), [exact variants](references/source-variant-tables.md), [calibrated tracing](references/calibrated-trace.md), [vector perimeter chains](references/source-perimeter-chains.md).
2. **Native solids:** [rounded tubes](references/source-first-and-tube.md), [axial shapes](references/axial-motor.md), [traced profiles](references/profile-reference.md), [rectangular references](references/envelope-reference.md), [annular references](references/annular-reference.md), [hexagonal references](references/hexagonal-reference.md), [hex heads and shafts](references/hex-screw-reference.md), [toroidal references](references/toroidal-reference.md), [spherical seats](references/spherical-seat-profile.md), [conical washers](references/conical-washer-profile.md).
3. **Reusable jobs:** [envelope runner](references/envelope-job-runner.md), [annular runner](references/annular-job-runner.md), [mounting-envelope references](references/pixhawk.md), [non-geometric requirements](references/non-geometric-requirements.md).
4. **Inspection:** [bearing assemblies](references/existing-bearing.md), [battery shell interfaces](references/existing-battery.md), [named tabbed solids](references/tabbed-battery.md), [saved body comparisons](references/small-bms.md), [circular boundaries](references/circular-boundary-checks.md), [native metadata](references/source-metadata.md).
5. **Assemblies:** [source placements](references/manufacturer-assembly.md), [unit conversion and mirrors](references/scaled-assemblies.md), [unit planning](references/assembly-units.md), [STEP solid inventory](references/step-solid-inventory.md).

For straight removal and installation paths, use the [service clearance procedure](references/service-clearance.md) with saved occurrence identities and caller-declared motion. It covers continuous axial bore checks, seated lifts and source attribution at saved endpoints.

## Save and computational handoff

Save IN_PROGRESS files and models incrementally and save the completed revision again. Use the authorized path, native format and version; preserve source originals. Audit saved data, inspect dropped information and verify file hashes and geometry through the caller's authorized persistence method. Label current and reopened checks explicitly. Keep a previous verified checkpoint throughout long jobs.

For calculations and solver work, use [computational engineering](references/computational-engineering.md) and the [model contract](references/model-contract.md). Supply actual material, load, boundary and convergence inputs. Format conversion records its source, target, tool and preserved/changed information.

## Report and preserve evidence

Report actual actions, paths, units, frames, measurements, errors and checks. Keep original source bytes, native models, operation journals, verified checkpoints and output receipts in caller-owned persistent storage. Use [evidence labels and capability checks](references/sources-and-capabilities.md) and report the representation actually constructed.

After reporting the completed job, name its reusable improvement and ask, “Would you like a local preview of a contribution with this change?” Follow the [optional contribution procedure](references/contributing.md) on opt-in or a later contribution request. Only explicit approval of the final diff and destination authorizes a push and pull request.

For recovered source assemblies, use [assembly evidence](references/assembly-evidence.md) to bind occurrences, photo constraints, mounting patterns, finite interference and source trims to their measured representations.

Archive raw CAD JSON, JSONL and debug history for every job revision using the [job history archive procedure](references/job-history-archive.md).

## Private parts and image-derived profiles

Use [private_catalogue.py](scripts/private_catalogue.py) SOURCE DESTINATION CAD_MODELS_BUILD_PY with an external --python that can run the trusted CAD Models builder. Supply --metadata JSON keyed by relative filename for confirmed id, designation, role, units, aliases, standards or dimensions. Query the returned directory as a named source with catalogue_candidates.py. Check source-relative path, content hash, model role, thread or seal suffix and mating geometry. For an exact field check, supply variant and evidence in the private metadata, then pass --variant REQUIREMENTS_JSON to catalogue_candidates.py. Inspect mating geometry after a field match. Pin the snapshot with the occurrence.

For an image-only part, use cad-source-intake and cad-drawing-inspection, optionally cad-opencv-setup. Receive the original hash, oriented planar loops, controls and residuals. Confirm nominal features, datum, inner loops and depth before passing them into plate_reference.build_plate. Reopen and inspect independent vertices and cylindrical surfaces. Keep the nominal parameter and original pixel estimates separate. For multiview or RGB-D input require camera intrinsics, pose, metric scale, visibility and independent checks for the affected features.

For a second occurrence of an imported DWG, pass the checked first occurrence as the previous argument to insert_component. This uses its native block name. Verify one source definition and two transforms after reopen. Set INSUNITS to 4 for an explicitly millimetre fixture and read it again in the receiving file.

Use [installed modeling operations](references/modeling-input-operations.md) for a missing standard fastener, partial surface or mating-interface search, mesh feature recovery, text or multi-view editable sequences, solver feedback, camera alignment, or RGB-D surface generation. Select the first operation that supplies the requested downstream decision.
