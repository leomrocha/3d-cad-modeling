# Tools

## Software

1. **Python** runs the helper scripts. Dependencies are pinned in [requirements-native.txt](../requirements-native.txt).
2. **OpenCADStudio** provides the native CAD session via MCP server used by the construction and inspection skills.

## Skills

1. [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md) — combines the full OCS modeling contract, session control, component iteration, geometry checks, saved-model verification and computational handoff instructions.
2. [cad-drawing-inspection](../skills/cad-drawing-inspection/SKILL.md) — guides the agent through reading a DXF's units, layers, blocks and source shapes.
3. [cad-source-intake](../skills/cad-source-intake/SKILL.md) — records the request, source files, hashes and corrections as a new input revision.

The [skill catalogue](../skills/README.md) separates these installed skills from proposed workflows. Component-specific procedures are indexed in [cad-ocs-engineering](../skills/cad-ocs-engineering/SKILL.md).

## Files, sources and component records

1. [part_index.py](../scripts/part_index.py) — reads and searches a supplied parts index.
2. [model_inventory.py](../scripts/model_inventory.py) — finds attributed models and filename candidates before a new build, supports exact configuration selection, and preserves known 2D drawing roles through retained-copy hashes. [Start-check procedure](../skills/cad-ocs-engineering/references/existing-model-start-check.md).
3. [source_intake.py](../scripts/source_intake.py) — saves source indexes, request scope and revision receipts.
4. [component_records.py](../scripts/component_records.py) — checks required source values and records individual modeling actions.
5. [source_metadata.py](../scripts/source_metadata.py) — compares expected source labels with the strings stored on a CAD entity.
6. [source_variant_table.py](../scripts/source_variant_table.py) — selects a value from a reviewed table for the specified product variant. The [source procedure](../skills/cad-ocs-engineering/references/source-variant-tables.md) also binds fastener dimensions to the exact standard edition, grade, row and drawing symbol.

7. [retained_artifacts.py](../scripts/retained_artifacts.py) — verifies retained-file hashes, JSON/JSONL syntax and manifest paths using caller-supplied roots. [Manifest procedure](../skills/cad-ocs-engineering/references/retained-artifact-checks.md).

## Drawings and construction

1. [dxf_inspect.py](../scripts/dxf_inspect.py) — lists DXF entities, units, layouts, layers and nested block transforms.
2. [calibrated_trace.py](../scripts/calibrated_trace.py) — converts image points to measured 2D coordinates using reference dimensions, scale and stated uncertainties.
3. [profile_reference.py](../scripts/profile_reference.py) — checks a supplied polygon, extrudes it as reference geometry and inspects the result.
4. [rounded_tube.py](../scripts/rounded_tube.py) — builds and checks a rounded hollow section from supplied dimensions.
5. [axial_motor.py](../scripts/axial_motor.py) — builds and checks the supported housing, shaft and mounting features of a source-bound motor job.
6. [envelope_reference.py](../scripts/envelope_reference.py) — builds and checks a rectangular reference volume from source dimensions.
7. [pixhawk.py](../scripts/pixhawk.py) — builds and checks the Pixhawk 6C mechanical envelope and nominal mounting-thread references.

8. [envelope_job_runner.py](../scripts/envelope_job_runner.py) — runs read-only preflight by default; an authorized write run builds a source-bound rectangular envelope, checks saved geometry and metadata, and closes its completed owned document. [Runner procedure](../skills/cad-ocs-engineering/references/envelope-job-runner.md).

9. [annular_reference.py](../scripts/annular_reference.py) — constructs a plain ring from source-bound bore diameter, outside diameter and thickness in millimetres. Checks analytic cylinder surfaces, end-face loops, closed-body topology and stored source metadata. [Annular-reference procedure](../skills/cad-ocs-engineering/references/annular-reference.md).

10. [hexagonal_reference.py](../scripts/hexagonal_reference.py) — constructs a regular hexagonal prism from source-bound across-flats dimension, height and a placement frame, with an optional source-bound bore. Checks side and cap planes, bore surfaces, topology and metadata. [Hexagonal-reference procedure](../skills/cad-ocs-engineering/references/hexagonal-reference.md).

11. [spherical_seat_profile.py](../scripts/spherical_seat_profile.py) — calculates a closed spherical-seat, collar, shaft and tangent-blend profile from caller-supplied dimensions. [Profile procedure](../skills/cad-ocs-engineering/references/spherical-seat-profile.md).

## Circular-section ring geometry

1. [toroidal_reference.py](../scripts/toroidal_reference.py) — constructs and checks a nominal circular-section ring from source-bound inside and section diameters. [Toroidal-reference procedure](../skills/cad-ocs-engineering/references/toroidal-reference.md).

## Geometry, assemblies and component checks

Some of these are specialized tools for particular geometries. I still have work to do on these things.

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

## CAD document cleanup

1. [ocs_document_cleanup.py](../scripts/ocs_document_cleanup.py) — closes the active owned document after matching its saved-file hash, persistence receipt and geometry revision; checks that unrelated documents retain their paths and dirty states. [Cleanup procedure](../skills/cad-ocs-engineering/references/document-cleanup.md).

## Installed packages and maintenance

1. [build_skill_packages.py](../scripts/build_skill_packages.py) — generates per-skill copies from canonical reusable code and checks them with `--check`.
2. [package_check.py](../scripts/package_check.py) — verifies installed package hashes, imports and pinned dependency versions; component CAD also accepts a selected OCS session for a read-only state check.
3. [ocs_control.py](../scripts/ocs_control.py) — reads an existing authenticated native session and guards explicitly authorized mutation requests.
4. [check_contract.py](../scripts/check_contract.py) — checks caller-supplied point, axis and plane measurements against an explicit coordinate contract.
5. [cadtools runtime](../scripts/cadtools/runtime.py), [geometry](../scripts/cadtools/geometry.py) and [save/reopen verification](../scripts/cadtools/verification.py) — shared OCS adapters included in the component package. [Package contents and maintenance](skill-packaging.md).

## Running the tools

The file, index and DXF command-line helpers can be run from a terminal. Construction and check modules are imported by component jobs with their source values, model records and CAD client. [Setup and command examples](../README.md#installing).
