# Tools

## Software 

1. **Python** runs the helper scripts. Dependencies are pinned in [requirements-native.txt](../requirements-native.txt).
2. **OpenCADStudio** provides the native CAD session via MCP server used by the construction and inspection skills.

## Skills

1. [component-cad](../skills/component-cad/SKILL.md) — guides the agent through an existing-model check, component construction, geometry checks and a reusable tooling improvement.
2. [drawing-inspection](../skills/drawing-inspection/SKILL.md) — guides the agent through reading a DXF's units, layers, blocks and source shapes.
3. [source-intake](../skills/source-intake/SKILL.md) — records the request, source files, hashes and corrections as a new input revision.

## Files, sources and component records

1. [part_index.py](../scripts/part_index.py) — reads and searches a supplied parts index.
2. [model_inventory.py](../scripts/model_inventory.py) — finds existing model files and checks their component identity before a new build.
3. [source_intake.py](../scripts/source_intake.py) — saves source indexes, request scope and revision receipts.
4. [component_records.py](../scripts/component_records.py) — checks required source values and records individual modeling actions.
5. [source_metadata.py](../scripts/source_metadata.py) — compares expected source labels with the strings stored on a CAD entity.
6. [source_variant_table.py](../scripts/source_variant_table.py) — selects a value from a reviewed table for the specified product variant.

## Drawings and construction

1. [dxf_inspect.py](../scripts/dxf_inspect.py) — lists DXF entities, units, layouts, layers and nested block transforms.
2. [calibrated_trace.py](../scripts/calibrated_trace.py) — converts image points to measured 2D coordinates using reference dimensions, scale and stated uncertainties.
3. [profile_reference.py](../scripts/profile_reference.py) — checks a supplied polygon, extrudes it as reference geometry and inspects the result.
4. [rounded_tube.py](../scripts/rounded_tube.py) — builds and checks a rounded hollow section from supplied dimensions.
5. [axial_motor.py](../scripts/axial_motor.py) — builds and checks the supported housing, shaft and mounting features of a source-bound motor job.
6. [envelope_reference.py](../scripts/envelope_reference.py) — builds and checks a rectangular reference volume from source dimensions.
7. [pixhawk.py](../scripts/pixhawk.py) — builds and checks the Pixhawk 6C mechanical envelope and nominal mounting-thread references.

## Geometry, assemblies and component checks

Note that some of these are specialized tools for particular geometries, I still have work to do on these things.

1. [native_acis.py](../scripts/native_acis.py) — reads supported native solid records for geometry inspection.
2. [step_solid_inventory.py](../scripts/step_solid_inventory.py) — inventories STEP solid definitions without counting nested shells as additional solids.
3. [step_placements.py](../scripts/step_placements.py) — reads supported STEP/native placement matrices and compares component positions.
4. [assembly_units.py](../scripts/assembly_units.py) — prepares a unit-change plan for specified assembly root inserts, preserving internal geometry.
5. [assembly_repair.py](../scripts/assembly_repair.py) — applies a reviewed component-placement correction through the guarded CAD client.
6. [feature_checks.py](../scripts/feature_checks.py) — compares measured boundaries, cylinders and other native features with supplied expectations.
7. [small_bms.py](../scripts/small_bms.py) — compares supported solid points and assembly instances before and after saving.
8. [pillow_block.py](../scripts/pillow_block.py) — checks the supported bearing housing, rings, mounting slots and associated parts.
9. [battery_module.py](../scripts/battery_module.py) — checks the supported battery shells, terminals and tabbed-case patterns.
10. [driver_checks.py](../scripts/driver_checks.py) — checks the supported Sumitomo driver exterior and component features.

## Running the tools

The file, index and DXF command-line helpers can be run from a terminal. Construction and check modules are imported by component jobs with their source values, model records and CAD client. [Setup and command examples](../README.md#installing-and-using-it).
