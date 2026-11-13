# Modeling and inspection scripts

1. Purpose: shared code for source records, part-index access, existing-model lookup, DXF inspection, native geometry checks and parameterized construction.
2. Ownership: shared functions remain here. FERME owns component recipes, dimensions, originals, models and job outputs. Proposed relocations and dependency changes: [script-change plan](../research/repository-split-preparation/script-changes.md).
3. Dependencies: [requirements-native.txt](../requirements-native.txt) pins native-reader packages. Use an existing configured Python environment. OCS construction also imports FERME `skills/cad-construction/scripts/cadtools`; supply its parent through `--cad-modules` where supported or the caller's Python path. OCS control uses the installed engineering skill and explicit current session/document/journal.
4. Inputs: provide the actual external project index, work index, job, CAD root and source paths. Outputs: component inspection/build records and models go to FERME; a tooling self-test writes its own tooling evidence here. Current commands remain unchanged.
5. `part_index.py --index PATH --id ID` searches an index; `component_records.py JOB.json` reports source readiness. Both print JSON.
6. `model_inventory.py --index PATH --work-index PATH --cad-root PATH --project-root PATH [--id ID]` prints model lookup JSON and reads existing files.
7. `source_intake.py --input SPEC.json --output NEW_DIRECTORY` writes a protected source revision. [Input contract](../skills/source-intake/SKILL.md).
8. `dxf_inspect.py SOURCE.dxf --output NEW.json [--space Model] [--layer NAME]` writes a bounded source inventory. [Drawing contract](../skills/drawing-inspection/SKILL.md).
9. Construction requires an authorized source-bound job, current CAD session, explicit destinations and existing-model check. [Component procedure](../skills/component-cad/SKILL.md).
10. Generated `__pycache__` directories are local runtime caches. Proposed Git exclusions belong to the later implementation batch.
