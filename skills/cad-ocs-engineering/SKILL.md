---
name: cad-ocs-engineering
description: Create, inspect and revise engineering geometry in OpenCADStudio (OCS), with explicit parts, units, coordinate frames, measured checks and simulation handoffs. Use for OCS modeling and CAD automation; not for illustrative images or silently selecting designs, dimensions, materials or another CAD application. Execute a component CAD job using an external project's part index and existing OCS tools, recording source readiness, action occurrences and a verified reusable improvement.
---

# CAD OCS Engineering

Use installed OCS geometry and control capabilities. Keep author requirements, engineering inputs and agent proposals distinct. A generated picture is not a geometric model or physical validation.

Use this skill when a real component job develops the reusable tools in this repository. Use the bundled [OCS runtime instructions](references/ocs-runtime.md) for native control and geometry. The component project owns its parts data, CAD artifacts and raw job evidence; this repository owns reusable code, tests and instructions.

## Package setup

Set `SKILL_ROOT` to this installed skill directory, containing `SKILL.md`, `scripts/`, `references/` and `requirements.txt`. All `scripts/` locators below refer to this directory. Use Python 3.12 on Linux or macOS and install the pinned dependencies in a caller-owned environment:

```sh
python3 -m venv "$JOB_ROOT/cad-env"
. "$JOB_ROOT/cad-env/bin/activate"
python -m pip install -r "$SKILL_ROOT/requirements.txt"
python "$SKILL_ROOT/scripts/package_check.py"
```

The package includes its OCS control helper and `cadtools` runtime, geometry and save/reopen code. Select the caller's already-running OpenCADStudio session explicitly. Use `package_check.py --session SESSION` or `--descriptor DESCRIPTOR_JSON` for a read-only connection check. [Runtime and model contract](references/ocs-runtime.md). [Portable job roots](references/paths.md).

## Establish the modeling contract

1. Read project instructions and the current request. Identify the authorized scope: inspection, document setup, geometry, revision, save, conversion or simulation. Preserve project authorization and exact-format conversion rules; do not impose a new approval convention.
2. Inspect supplied source views. Record the references, current corrections and accepted/rejected/unresolved items. Do not reuse rejected images as design evidence. Sketch arrangement is not a dimension unless dimensioned.
3. Establish units, origin, axes, datums, part boundaries and motion. Separate lateral displacement from height and axial position. Record author-defined constraints before modeling. Ask in ordinary chat about a missing input that blocks the next action; do not invent dimensions or move parts to avoid a collision.
4. Connected parts are not necessarily fused or monolithic. Keep display color, visibility layer, render material and physical material separate. Use provisional values only when that kind of provisional modeling is authorized, with labels.

Read [model-contract.md](references/model-contract.md) for multi-part modeling and numeric constraint inputs. It is not a turbine design.

### Bind component requirements

1. Preserve original source bytes, proposal/source labels, required features, units, local datums and assembly frame. `scripts/component_records.py JOB.json` checks required feature coverage and pinned source revisions. Its code/output contract is described in [the procedure](references/component-procedure.md).
2. A required feature with a named unresolved input produces `NEEDS_INPUT`. Resolve that feature before dependent construction. The first FERME tube case has supplied 40 x 40 x 3 mm nominal dimensions and separate cut lengths; its corner profile requires the recorded source or task input. Keep the exact question with that feature.
3. `SOURCE_READY` records input coverage. Native construction, geometry readback, saved-file persistence and visual checks produce their own results.
4. Before comparing drawing dimensions with native geometry, use the [drawing-feature check procedure](references/drawing-feature-checks.md). Identify extension-line endpoints and match the measurement kind; keep hole pitch, full surface bounds and reachable-point extrema distinct in the result records.
5. For standard-defined features, read the [source-first and hollow-section procedure](references/source-first-and-tube.md). Record stock lookup, standards search, source-access review and formula calculation as individual actions before binding the construction inputs.

## Inspect the actual OCS session

Read [ocs-control.md](references/ocs-control.md) before first connection or unfamiliar control work.

- Prefer exposed `ocs_sessions`, `ocs_read`, `ocs_execute`, `ocs_capture` tools. When absent, `scripts/ocs_control.py` uses an existing authenticated native local session. It does not launch, install or reconfigure OCS.
- Discover the session; read state, capabilities, document identity/revision and unit settings. Session descriptors contain private tokens: never print them.
- Read installed command/entity/record schemas before constructing unfamiliar requests. A command declaration is not a successful operation; upstream API examples are not proof of installed support.
- Preserve unsaved and concurrent work. Do not clear, close, replace or save an open document as a side effect of making another model.
- Do not infer scale from screenshots or camera zoom.

### Check existing component implementations

1. Before every component start, check both its work status and the actual 3D files. Read the input manifest, work record, sheet links, existing CAD index and filesystem inventory, including available manufacturer models. Run the [existing-model start check](references/existing-model-start-check.md). A matching existing model is DONE for the current build list: record its path and reuse its existing checks, then select an unfinished component. A stale NOT_STARTED or IN_PROGRESS entry does not start another construction, inspection or capture cycle for that model.
2. Reuse the existing `Client`, `Journal`, `Geometry` and verification functions for their supported actions. Select their helper, session, document and journal explicitly. Read the bundled [OCS runtime instructions](references/ocs-runtime.md) before connecting.
3. Use `scripts/part_index.py --index PATH --id PART_ID` to read the actual external index. Add another `--index` for an existing dictionary. Results retain source namespaces, original records and source hashes. A matching name/ID in two indexes remains two attributed records.

## Construct and check bounded changes

1. Plan the next edit using stable readable part names, current handles and the installed schema. Do not substitute FreeCAD, Fusion or build123d calls for unknown OCS APIs.
2. Bind authorized mutations to the session, document, expected revision and caller-stable `request_id`. For selection-dependent edits, use explicit expected handles/selection supported by the installed protocol, not an unexamined GUI selection. Use state returned by the preceding operation. `accepted`, `running` and `waiting_input` are not completion. A failed batch can have committed earlier steps.
3. On timeout/lost response, query the operation with the same identity; do not replay under a new ID because completion is unknown. Refresh after a definitive stale-state rejection and reconsider the edit. Never restart a partially completed batch blindly.
4. Read back changed parts, properties and geometry. Tie numeric checks to document revision and source handles. `scripts/check_contract.py` checks supplied point/axis/plane measurements; it does not query OCS or validate solids.
5. Inspect corresponding orthographic views from the same model, after authorized view changes. Do not invent separate geometry for each view or generate authoritative CAD views with imagegen. Turn a visible concern into an actual measured check when supported.
6. Unsupported/failed checks stay unverified. Overlapping bounding boxes do not prove collision; disjoint boxes only rule out overlap for the represented geometry/pose. A screenshot does not prove a dimension. Axis checks do not establish gear teeth engagement or bearing fit.

Inspect layer/material/group/block schemas before organizing parts. Name parts and functional visibility groups as agreed. Do not fuse separate components just to color them. Rendered metal supplies no density, modulus, strength or anisotropy. Keep unselected engineering materials unselected.

### Execute and improve component jobs

1. Map each job step to its readable action name and graph reference. Append component-specific occurrences with input/output revisions, representation, units/frames, preserved/changed information, alternatives, downstream conditions and actual check evidence.
2. Use one writer for the selected CAD document. Preserve unrelated open work. Use stable request IDs and the existing same-ID recovery mechanism for uncertain completion.
3. Record successful and failed occurrences. Document a repeated procedure with its supported conditions before extracting or extending its Python implementation. Reuse a matching function first.
4. Every completed component iteration includes an applied, verified improvement to the current skill/procedure or script. A future task or confirmation of existing behavior supports the improvement's selection.
5. Bind geometric observations to source expectations and actual document/geometry revisions. Verify save/reopen and captured component identity separately. After retaining those checks, use the [completed-document cleanup procedure](references/document-cleanup.md) to close the iteration's saved/reopened and temporary documents. Keep ongoing and unrelated work open. Update component/part records in the owning project and tool/action definitions here, then commit the scoped results and cleanup receipt.
6. For the exercised rounded hollow-section route, use the [native construction and recovery procedure](references/source-first-and-tube.md). It records the installed selection semantics, direct bounded-area extrusion and the reopened SAB feature-reader result from the rail build.
7. For an existing detailed bearing, use the [source-bound inspection and derivative procedure](references/existing-bearing.md). It covers transformed native solids, fragmented mounting-plane boundaries, source dimension failures, selective housing revision and saved derivative checks.
8. For an existing battery module, use the [saved shell and terminal check procedure](references/existing-battery.md). It preserves source/reconstruction labels, reuses component-name reading and checks the source-specific shell, mounting and terminal geometry.
9. For a check repeated across component families, use the [shared feature-check procedure](references/shared-feature-checks.md). It defines the independently sourced expectations, measured inputs, supported software conditions, agent interpretation, failure cases and cross-component checks required before reuse.
10. For a dimensioned motor with axial cylinder/plane interfaces and a keyed shaft, use the [axial motor procedure](references/axial-motor.md). It records source-leader review, nominal blind-thread cuts, keyway construction, analytic radius checks, individual hole-bottom checks and the actual saved motor case.
11. For imported manufacturer assemblies, use the [source-placement and persisted-assembly procedure](references/manufacturer-assembly.md). It distinguishes block definitions from placed instances, checks complete STEP/native matrices, records the exercised inverse-placement correction, preserves solid definitions and compares reopened geometry. Its repeated placement-write procedure uses `scripts/assembly_repair.py` after source-plan review, with full baseline preflight, compare-and-set writes and unchanged-solid checks. Check actual captured component identity separately from native document state; the procedure records the exercised stale-image failure.

12. For an assembly whose outer insertion converts source units, use the [scaled assembly procedure](references/scaled-assemblies.md). Read the drawing header and source units, explicitly enable positive uniform-scale traversal, and preserve the conversion separately from internal placement corrections.

13. For a battery case formed from named exterior solids with repeated planar recesses, use the [tabbed battery procedure](references/tabbed-battery.md). Keep measurement groups and reconstruction inputs in the external component job; check every cover boundary and record visual identity separately.

14. For a source-defined clearance volume, use the [generic envelope-reference procedure](references/envelope-reference.md). It consumes external job values, validates inputs before writes, and binds readback to the actual document, handle and stable geometry revision. Keep the reference representation explicit.
15. For calibrated raster coordinates, use the [generic trace procedure](references/calibrated-trace.md). Pass image points, origin, signed scale and uncertainties as inputs; retain the complete product-error term in the uncertainty bound. Source images and case point tables remain in the component project.
16. For an explicit drawing-unit change at assembly roots, use the [generic unit-planning procedure](references/assembly-units.md). The read-only planner scales root translation and scale together using supplied unit definitions. Native execution and source-unit evidence remain with the component job.
17. For a source-traced polygon used as a clearance reference, use the [profile-extrusion procedure](references/profile-reference.md). It checks input spans against independent source dimensions before writes, rejects invalid polygons and numeric collapse, and keeps native geometry, source expectations and metadata checks separate.
18. Before matching imported native solid counts to STEP source definitions, use the [STEP entity inventory](references/step-solid-inventory.md). Include supported solids containing voids, retain their entity IDs, and keep shell and complex-entity counts separate.
19. For source tables containing adjacent product variants, use the [exact variant-column procedure](references/source-variant-tables.md). Retain the reviewed source transcription and select each specification through its exact header and row label.
20. For a source-bound rectangular envelope job, use the [guarded envelope job runner](references/envelope-job-runner.md). Supply component inputs and named roots externally; the default is read-only preflight. The native route checks reader imports, preserves existing documents, uses exact-ID recovery and checks geometry, metadata and saved-file evidence.

21. For source `Max`/`Min` dimensions and measurements from different datum planes, use the [dimension-limit and datum procedure](references/dimension-limits-and-datums.md). Preserve printed limits, arithmetic relations and image-traced coordinates as separate inputs.
22. Before binding image-based dimensions, use the [source-view evidence procedure](references/source-view-evidence.md). Record actual inspected pixels and source revision separately from web-generated descriptions.
23. For a perimeter assembled from source vector segments, use the [source-vector chain procedure](references/source-perimeter-chains.md). Retain resolvable source segment identities, endpoint joins and independent printed-dimension checks.
24. For a source-defined plain ring, use the [annular-reference procedure](references/annular-reference.md). Supply bore diameter, outside diameter, thickness, local frame and source bindings from the component job. The helper checks analytic cylindrical surfaces, annular end-face loops, connected-body topology and the actual stored metadata application.
25. For a source-defined regular hexagonal reference, use the [hexagonal-reference procedure](references/hexagonal-reference.md). Supply across-flats dimension, height, frame and pinned source features. Bind an optional bore to its own source dimension; retain thread designations and standard limits separately. The helper checks all expected planar surface families, optional bore surfaces, topology and portable source metadata.

26. For saved source labels, use the [native metadata procedure](references/source-metadata.md). Compare actual entity string chunks with the expected source lines before and after saving.
27. For SAT-to-SAB geometry persistence, use the [smallBMS comparison procedure](references/small-bms.md) within its supported frame and body conditions.
28. For the source-dimensioned Pixhawk 6C clearance envelope and mounting references, use the [Pixhawk procedure](references/pixhawk.md).
29. After final provenance and path edits, use the [retained-artifact manifest check](references/retained-artifact-checks.md). Keep the emitted receipt with the component records in the owning project.

30. For a circular-section ring defined by inside diameter and section diameter, use the [toroidal-reference procedure](references/toroidal-reference.md). Supply source-bound dimensions and an explicit centre and axis. Preserve saved native surface records before extending their decoder; verify analytic radii and body closure before completing the component.

### Additional component procedures

1. For an explicitly source-pinned non-geometric task, use the [non-geometric requirement procedure](references/non-geometric-requirements.md). Preserve its classification and source hash through readiness and existing-model checks.
2. For a bounded spherical seat with a collar, shaft and tangent blend, use the [spherical-seat profile procedure](references/spherical-seat-profile.md). Supply all source dimensions through the component job; retain analytic surface, transition and persistence checks.

## Save and computational handoff

- Save only to an authorized path, format and version. Follow exact conversion authorization requirements; preserve originals. Mesh visibility is not editable-solid or feature-history equivalence.
- Where supported, audit the intended target and use `save_verified`; inspect dropped data and reopen results. Record the output hash and checked properties, not just a success label.
- Read [computational-engineering.md](references/computational-engineering.md) for equations, procedural geometry or solver work. OCS remains selected CAD. PicoGK/ShapeKernel are optional supplements, not installed or enabled by this skill. Noyron's public description is not a public executable physics engine.
- Do not run a solver with invented materials, loads, boundary conditions or convergence criteria. Separate measured experiments, analytical checks, numerical predictions and manufacturer statements.

## Report and preserve evidence

Report actual actions, paths, measurements and unresolved errors. State actual executing model if exposed; otherwise unavailable, never the requested model as a substitute. Automated checks and author acceptance are different facts.

Initial evidence is linked in [sources-and-capabilities.md](references/sources-and-capabilities.md). Recheck the installed build after updates. Follow project original-source archiving/provenance rules; reference existing originals rather than duplicate them.
