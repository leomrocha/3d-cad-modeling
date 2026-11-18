---
name: cad-model-repair
description: Repair an existing CAD model with generic or duplicate labels, missing layers, or unusable assembly navigation. Diagnose observed defects, save a separate native revision and verify geometry, identity and navigation after reopening.
---

# Repair an existing model's navigation

1. Tell the user that scripts, native derivatives, receipts and before/after views stay in the owning project. Contributions are optional. Hash the original and its dependencies. Record the specific failing user action and capture its starting view. Obtain an unused output path in that same project.
2. Inspect the actual document, bodies, instances, transforms and native hierarchy. Build a mapping with one row per target occurrence, original native locator, proposed stable identity, parent, readable name, role, layer/group, source and fields to change. Include untouched objects in the baseline. If two equal bodies have no distinguishable source binding, return the two candidates and ask which occurrence gets which assignment. Keep both unchanged until resolved.
3. Use native setters on a separately saved derivative. On OCS use the selected document/revision, validate the target handles, record the native operation, reread the entity and layer table, and save an incremental checkpoint. Preserve existing application XDATA, source identifiers, unrelated layer membership and material assignments. An override for one instance belongs to that occurrence. A display colour has no authority to set physical material.
4. For native Blender mesh objects, the [Blender repair helper](scripts/repair_blend.py) implements the bounded name, navigation-property and additional collection operations below. Use the native API of the selected application for another format. Inspect how that application displays and queries each assignment before applying it to the project file.
5. Independently reopen the output. Compare part and occurrence counts, geometry and topology, units, per-object world placement and assembly relations with the baseline. Inspect sourced material, appearance, untouched objects and links. Query by readable identity, select the intended occurrence, isolate the group, check its sibling and restore visibility. Record native tree/property evidence and matched-camera views. Repeat the repair on another derivative with the same desired assignments and verify no duplicate memberships or identities.
6. Record the original and derivative hashes, mapping evidence, reader version and checks. Report unresolved mappings per object. Keep the source original and prior evidence. Offer a local contribution preview for a reusable improvement.

## Blender mesh repair

Supply a JSON mapping with source_sha256 and an objects array. Each row gives source_name, id, label, role and layer. Use source_name from the actual object list, id from the verified identity mapping and layer as the name of a collection to add. Keep the original mapping evidence in the job. Run Blender with factory startup, disabled auto-execution and a nonzero Python error exit code. Supply the helper path followed by the three job paths:

```sh
blender -b --factory-startup --disable-autoexec --python-exit-code 1 --python "$SKILL_ROOT/scripts/repair_blend.py" -- original.blend mapping.json repaired.blend
```

This operation checks mesh connectivity, local vertex positions, object transforms and parent relationships across save/reopen. Keep separate evidence for modifiers, physical materials, selection and any other required properties. Use self-contained native inputs for this helper.
