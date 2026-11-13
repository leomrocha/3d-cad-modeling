---
name: component-cad
description: Execute a component CAD job using an external project's part index and existing OCS tools, recording source readiness, action occurrences and a verified reusable improvement.
---

# Component CAD iterations

Use this skill when a real component job develops the reusable tools in this repository. Use the installed OCS engineering skill for native control and geometry. The component project owns its parts data, CAD artifacts and raw job evidence; this repository owns reusable code, tests and instructions.

## Read current implementations first

1. Before every component start, check both its work status and the actual 3D files. Read the input manifest, work record, sheet links, existing CAD index and filesystem inventory, including available manufacturer models. Run the [existing-model start check](references/existing-model-start-check.md). A matching existing model is DONE for the current build list: record its path and reuse its existing checks, then select an unfinished component. A stale NOT_STARTED or IN_PROGRESS entry does not start another construction, inspection or capture cycle for that model. Existing FERME implementations are indexed in `${FERME_ROOT}/skills/cad-automation-and-reuse.md`.
2. Reuse the existing `Client`, `Journal`, `Geometry` and verification functions for their supported actions. Select their helper, session, document and journal explicitly. Read the installed OCS control instructions before connecting.
3. Use `scripts/part_index.py --index PATH --id PART_ID` to read the actual external index. Add another `--index` for an existing dictionary. Results retain source namespaces, original records and source hashes. A matching name/ID in two indexes remains two attributed records.

## Bind the component requirements

1. Preserve original source bytes, proposal/source labels, required features, units, local datums and assembly frame. `scripts/component_records.py JOB.json` checks required feature coverage and pinned source revisions. Its code/output contract is described in [the procedure](references/component-procedure.md).
2. A required feature with a named unresolved input produces `NEEDS_INPUT`. Resolve that feature before dependent construction. The first FERME tube case has supplied 40 x 40 x 3 mm nominal dimensions and separate cut lengths; its corner profile requires the recorded source or task input. Keep the exact question with that feature.
3. `SOURCE_READY` records input coverage. Native construction, geometry readback, saved-file persistence and visual checks produce their own results.
4. Before comparing drawing dimensions with native geometry, use the [drawing-feature check procedure](references/drawing-feature-checks.md). Identify extension-line endpoints and match the measurement kind; keep hole pitch, full surface bounds and reachable-point extrema distinct in the result records.
5. For standard-defined features, read the [source-first and hollow-section procedure](references/source-first-and-tube.md). Record stock lookup, standards search, source-access review and formula calculation as individual actions before binding the construction inputs.

## Execute and improve

1. Map each job step to its readable action name and graph reference. Append component-specific occurrences with input/output revisions, representation, units/frames, preserved/changed information, alternatives, downstream conditions and actual check evidence.
2. Use one writer for the selected CAD document. Preserve unrelated open work. Use stable request IDs and the existing same-ID recovery mechanism for uncertain completion.
3. Record successful and failed occurrences. Document a repeated procedure with its supported conditions before extracting or extending its Python implementation. Reuse a matching function first.
4. Every completed component iteration includes an applied, verified improvement to the current skill/procedure or script. A future task or confirmation of existing behavior supports the improvement's selection.
5. Bind geometric observations to source expectations and actual document/geometry revisions. Verify save/reopen and captured component identity separately. Update component/part records in the owning project and tool/action definitions here, then commit the scoped results.
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
