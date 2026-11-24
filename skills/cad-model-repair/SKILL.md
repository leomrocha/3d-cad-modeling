---
name: cad-model-repair
description: Repair model labels, layers and assembly navigation. Correct a source-linked hole diameter or image outline, save a separate revision and remeasure dependent and independent features after reopening.
---

# Repair an existing CAD model

Use the [operation selection procedure](references/modeling-operation-selection.md) for component reuse, provider capability checks and job evidence. Apply it to the requested operation. Open the local operation catalogue on first use and after a request to refresh available skills.

1. Tell the user that scripts, native derivatives, receipts and before/after views stay in the owning project. Contributions are optional. Hash the original and its dependencies. Record the specific failing user action and capture its starting view. Obtain an unused output path in that same project.
2. Inspect the actual document, bodies, instances, transforms and native hierarchy. Build a mapping with one row per target occurrence, original native locator, proposed stable identity, parent, readable name, role, layer/group, source and fields to change. Include untouched objects in the baseline. If two equal bodies have no distinguishable source binding, return the two candidates and ask which occurrence gets which assignment. Keep both unchanged until resolved.
3. Use native setters on a separately saved derivative. On OCS use the selected document/revision, validate the target handles, record the native operation, reread the entity and layer table, and save an incremental checkpoint. Preserve existing application XDATA, source identifiers, unrelated layer membership and material assignments. An override for one instance belongs to that occurrence. A display colour has no authority to set physical material.
4. For native Blender mesh objects, the [Blender repair helper](scripts/repair_blend.py) implements the bounded name, navigation-property and additional collection operations below. Use the native API of the selected application for another format. Inspect how that application displays and queries each assignment before applying it to the project file.
5. Independently reopen the output. Compare part and occurrence counts, geometry and topology, units, per-object world placement and assembly relations with the baseline. Inspect sourced material, appearance, untouched objects and links. Query by readable identity, select the intended occurrence, isolate the group, check its sibling and restore visibility. Record native tree/property evidence and matched-camera views. Repeat the repair on another derivative with the same desired assignments and verify no duplicate memberships or identities.
6. Record the original and derivative hashes, mapping evidence, reader version and checks. Report unresolved mappings per object. Keep the source original and prior evidence. Offer a local contribution preview for a reusable improvement.

## Blender mesh repair

Supply a JSON mapping with source_sha256 and an objects array. Each row gives source_name, id, label, role and layer. Use source_name from the actual object list, id from the verified identity mapping and layer as the name of a collection to add. For a repeat run, pin the new input hash and retain the desired assignments. The helper resolves a renamed object by its stable ID and checks for conflicting source-name matches. Keep the original mapping evidence in the job. Run Blender with factory startup, disabled auto-execution and a nonzero Python error exit code. Supply the helper path followed by the three job paths:

```sh
blender -b --factory-startup --disable-autoexec --python-exit-code 1 --python "$SKILL_ROOT/scripts/repair_blend.py" -- original.blend mapping.json repaired.blend
```

This operation checks mesh connectivity, local vertex positions, object transforms and parent relationships across save/reopen. After reopening, the helper selects each mapped object by its persisted identity. It isolates each requested collection by temporarily hiding nonmembers in the active view layer, verifies the visible set, then restores selection and visibility. This works for objects that also belong to another collection. Keep separate evidence for modifiers, physical materials and other required properties. Use self-contained native inputs for this helper.

For a native drawing repair, compare retained solid properties and feature history as well as occurrence handles and poses. Reapply the mapping to the repaired copy and reopen the second derivative. Compare the resulting entity properties. If several occurrences share a definition, resolve their locations in the parent frame before assigning names.

## Source-linked correction

Identify the affected occurrence from its source revision, parent and role. Resolve ambiguity before applying a correction. A revised image mask returns to source intake and invalidates its dependent profile. A changed part number returns to indexed lookup. Save a separate model revision for a role correction. Reopen, repeat the failing selection, compare sibling identity and transform, then reapply the mapping to check idempotence.

For a diameter correction, bind the original and revised source field (with units) to the owning model revision, native feature identifier and entry centre. For imported STEP bind the revision-specific cylindrical face and its two rims to the source field using centre, axis, diameter, depth and end condition. Resolve the feature again after export because STEP entity numbers can change. Identify the mating feature, its diameter and the clearance convention. Record the signed diametral clearance as the measured bore diameter minus the mating diameter. Distinguish the represented cylinder from a nominal thread envelope when the imported screw uses a simplified thread.

In a native feature model, edit the identified driving diameter and retain its centre and axis constraints. For a complete imported cylindrical bore, apply an axis-preserving direct edit to its wall. The engineering skill’s batch modification procedure supports this operation for enlargement of one selected STEP bore. Save a separate revision. Measure both revisions at the same entry centre. Compare the hole diameter, centre, depth, mating clearance and one identified independent hole after reopening. Retain the request, source and derivative hashes, and actual write calls. Count read-only Boolean comparisons separately from geometry edits. A native editor can recompute the host and its dependencies internally. Keep existing independent source analysis, catalogue results and placements.

For an outline correction, identify the source revision and instance mask, the extraction inputs (including calibration and frame), the resulting profile, the CAD feature that consumes that profile and the measurement that reads the feature. Rerun that extraction, revise that feature and remeasure it after reopening. Compare a separate feature with its prior result. If multiple profiles or features match the source, record their identifiers and request the intended binding before editing.

For additive mesh patches, use the engineering skill's mesh repair evidence operation to relate original triangles and boundary edges to the saved derivative. Use source vertices for fitted dimensions. Identify added triangles explicitly when measuring repaired surfaces.
