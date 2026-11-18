---
layout: default
title: Create and repair navigable CAD models
---

# Create and repair navigable CAD models

Install either skill from a local checkout of the navigation branch. Run the command from the project where you use your agent, substituting the location of the existing skills checkout.

```sh
npx skills add "$MODELING_ROOT" --skill cad-model-navigation --skill cad-model-repair
```

1. **Create a part or assembly.** Ask the agent to apply `cad-model-navigation` while modeling. For example, “Use one spacer definition for both spacers. Let me select each by its installed position, then isolate the hardware.” The skill records model identities when bodies are created, checks their native assignments and repeats the lookup after reopening.
2. **Repair an existing model.** Ask for `cad-model-repair` and a new native output file. Identify the action that fails today, such as “I cannot hide the cover without also hiding the frame.” The agent inventories the original, maps objects to evidenced names and groups, saves a derivative, and checks the reopened geometry, placement and assignments.
3. **Inspect the result.** Ask for the same camera before and after isolating a group, the selected occurrence in the native model tree, and the independently reopened object inventory. Known physical material, surface finish and display colour are separate properties.

## Sharing a model and its views

Check the preview as well as the CAD file. Blender can embed the originating file path in PNG text metadata even when the image shows no filename. A native document can also retain a file-browser directory independently of its asset links. Inspect both before preparing a public contribution. For a corrected preview, compare decoded pixels; for a corrected model, reopen it and compare geometry, identities, materials and placements. Record the new file hashes in the owning project.

## Checking an assembly handoff

1. Select each of two identical fasteners by its installed name. Reopen the drawing and check the parent, position and layer for each one.
2. For a cut joint, inspect the seat with its mating part hidden. Check the cut corners on the saved receiving body against the source profile in the same coordinate frame.
3. Record what the destination actually preserves for each material: an object property, a native material assignment or a display colour. Check the saved file and the exchanged file separately.
4. Search the intended parts catalogue by definition ID. Record the dataset and file hash so the assembly can be rebuilt with the same part. A hit in a draft index qualifies that draft.
