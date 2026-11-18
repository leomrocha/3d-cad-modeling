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
