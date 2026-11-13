# Project skill catalogue

## Skills supplied by this repository

1. [cad-ocs-engineering](cad-ocs-engineering/SKILL.md) — merges OCS modeling contracts, guarded session control, component iteration, geometry checks, saved results and computational handoffs.
2. [cad-drawing-inspection](cad-drawing-inspection/SKILL.md) — inventories DXF entities, units, layers, spaces and nested transforms.
3. [cad-source-intake](cad-source-intake/SKILL.md) — preserves source files, hashes, request scope and corrected input revisions.

Install these skills using the [README instructions](../README.md#installing). The [tools page](../docs/tools.md) lists the Python helpers. Each skill directory includes its runtime files and dependencies. Component CAD includes its OCS control and geometry adapters. [Package maintenance](../docs/skill-packaging.md).

## Component CAD procedure index

1. **Job contract:** [component requirements and action records](cad-ocs-engineering/references/component-procedure.md).
2. **Model reuse:** [existing-model checks and configuration selection](cad-ocs-engineering/references/existing-model-start-check.md).
3. **Source interpretation:** [drawing features](cad-ocs-engineering/references/drawing-feature-checks.md), [limits, datums, drawing scale and dual units](cad-ocs-engineering/references/dimension-limits-and-datums.md), [source-image inspection and retrieval routes](cad-ocs-engineering/references/source-view-evidence.md), [variant tables and fastener standard editions](cad-ocs-engineering/references/source-variant-tables.md).
4. **Traced geometry:** [calibrated coordinates](cad-ocs-engineering/references/calibrated-trace.md), [source-vector perimeter chains](cad-ocs-engineering/references/source-perimeter-chains.md), [profile extrusion](cad-ocs-engineering/references/profile-reference.md).
5. **Construction:** [rounded hollow sections](cad-ocs-engineering/references/source-first-and-tube.md), [axial motors](cad-ocs-engineering/references/axial-motor.md), [rectangular envelopes](cad-ocs-engineering/references/envelope-reference.md), [guarded envelope runner](cad-ocs-engineering/references/envelope-job-runner.md), [Pixhawk clearance geometry](cad-ocs-engineering/references/pixhawk.md), [annular references](cad-ocs-engineering/references/annular-reference.md), [hexagonal references](cad-ocs-engineering/references/hexagonal-reference.md), [toroidal references](cad-ocs-engineering/references/toroidal-reference.md), [spherical-seat profiles](cad-ocs-engineering/references/spherical-seat-profile.md), [conical-washer profiles](cad-ocs-engineering/references/conical-washer-profile.md).
6. **Component checks:** [bearing geometry](cad-ocs-engineering/references/existing-bearing.md), [battery shells and terminals](cad-ocs-engineering/references/existing-battery.md), [tabbed battery cases](cad-ocs-engineering/references/tabbed-battery.md), [smallBMS saved geometry](cad-ocs-engineering/references/small-bms.md), [shared feature comparisons](cad-ocs-engineering/references/shared-feature-checks.md).
7. **Assemblies:** [manufacturer placements](cad-ocs-engineering/references/manufacturer-assembly.md), [scaled imports](cad-ocs-engineering/references/scaled-assemblies.md), [root unit-change plans](cad-ocs-engineering/references/assembly-units.md), [STEP solid inventories](cad-ocs-engineering/references/step-solid-inventory.md).
8. **Completion:** [saved source metadata](cad-ocs-engineering/references/source-metadata.md), [retained-file manifests](cad-ocs-engineering/references/retained-artifact-checks.md), [owned-document cleanup](cad-ocs-engineering/references/document-cleanup.md), [required package completion and registration](cad-ocs-engineering/references/package-completion.md).

The [tools page](../docs/tools.md) lists the packaged helper implementations and their source-bound geometry roles.

## OCS engineering procedures

1. [OCS control](cad-ocs-engineering/references/ocs-control.md) — session discovery, installed schemas and guarded requests.
2. [Computational engineering](cad-ocs-engineering/references/computational-engineering.md) — equations, geometry/material/solver contracts and representation handoffs.
3. [Capability evidence](cad-ocs-engineering/references/sources-and-capabilities.md) — original dated OCS and tool findings with source locators.
4. [Non-geometric requirements](cad-ocs-engineering/references/non-geometric-requirements.md) — explicit source-pinned tasks whose scope requires no CAD geometry.

## Installed package references

1. [Bundled OCS runtime](cad-ocs-engineering/references/ocs-runtime.md), [model and coordinate-check contract](cad-ocs-engineering/references/model-contract.md) and [caller-owned paths](cad-ocs-engineering/references/paths.md) explain cad-ocs-engineering execution from its installed directory.
2. [Package maintenance](../docs/skill-packaging.md) records canonical code ownership, distribution generation and isolated checks.

## Research catalogue

The following catalogue records external candidates and proposed workflow groups from 12 November 2026. Each entry retains its recorded implementation status.

## Existing skills to reuse or assess

| Skill or package | Concrete use | Proposed action and evidence |
| --- | --- | --- |
| Local OCS engineering skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) | Live OCS inspection, model contract, component/frame discipline, measured checks and verified saves | Reuse existing skill and its scripts. User reports partial local success. Record capability gaps through the first modeling fixture. |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Code-defined parametric models with `cadgen`/build123d, saved-file measurement and preview | Assess pinned runtime/bootstrap, telemetry, source conventions and output checks. The separately advertised `step-parts` skill searches a component catalogue. |
| [glotoff/freecad-skills](https://github.com/glotoff/freecad-skills) | FreeCAD user/power-user modeling and API references | Adapt only the exercised operations needed for constrained sketches and editable features. |
| [GitHub Copilot FreeCAD scripting skill](https://github.com/github/awesome-copilot) | FreeCAD Python documents, Part/Sketcher geometry and recompute | Reuse as an API reference, with pinned-version geometry fixtures. Archived exact skill is available in the existing CAD research. |
| [reyk/freecad-ai-skill](https://github.com/reyk/freecad-ai-skill) | Terminal-to-running-FreeCAD Python bridge | Compare its session control with a direct local adapter before adopting its bridge. |
| [mitsuhiko/agent-stuff OpenSCAD skill](https://github.com/mitsuhiko/agent-stuff) | Parameterized CSG, command-line render and multi-view review | Adapt the local OpenSCAD workflow and verify the resulting mesh. |
| [Foster1202/cad-modeling-fusion-skill](https://github.com/Foster1202/cad-modeling-fusion-skill) | ModelSpec schema and code-generation patterns with Fusion, FreeCAD and OpenSCAD backends | Assess reusable schema and open-backend content under its licence. Use the open software backends for this project. |
| Blender workflow skills and MCP bridges | Scene/mesh authoring and interactive inspection | Compare reviewed bridges with native `bpy` scripts. Match each bridge's supported Blender version to the installed version. |

Detailed source, licence and dependency assessments: [CAD and skills](../research/cad-and-skills.md). Original archived candidate files remain in `${ENERGY_RAW_ROOT}/wind-prototypes/cad-workflow/skills/` with the existing research manifests.

## Proposed project workflows

1. `model-brief` — descriptions, dimensions, reference views, part boundaries, units and source evidence.
2. `ocs-engineering` — reuse the existing skill for OCS modeling and inspection.
3. `parametric-solid-modeling` — scripted solid geometry and editable parameters.
4. `drawing-to-cad` — sketch, DXF and SVG interpretation into constrained geometry.
5. `blender-modeling` — scene/mesh authoring, inspection and visual derivatives.
6. `capture-and-calibration` — photo/video/depth capture and independent scale controls.
7. `photogrammetry` — cameras, point clouds and textured surface reconstruction.
8. `point-cloud-and-mesh-processing` — registration, cleanup, fitting and distance checks.
9. `scan-to-cad` — traceable reconstruction-to-feature remodeling, using the OCS model contract.
10. `generative-3d-reference` — learned image/text generation for reference geometry.
11. `gaussian-scene-reference` — view-synthesis scene reconstruction and retained camera metadata.
12. `architecture-ifc` — semantic building elements, relationships and IFC validation.
13. `robot-model-handoff` — joints, frames, visual/collision assets and MJCF/URDF packages.
14. `component-library` — component search, provenance, versioning, placement and reuse.
15. `model-verification` — numeric checks, save/reopen and importer comparisons.

The [implementation plan](../research/implementation-plan.md) defines each workflow's purpose, supporting software, inputs, deliverables and validation sequence. During implementation, package each exercised workflow with its `SKILL.md`, scripts, references and fixtures. Reuse the existing OCS contract across reconstruction and CAD handoffs.

The [workflow operation catalogue](../research/workflows/operation-catalogue.md) maps the proposed skills to source-backed transformations and combined routes. The [source register](../research/sources/source-register.md) and [ideas register](../research/ideas-register.md) retain the original links, summaries and alternative proposals.

## Detailed action and helper contracts

The [skill-to-action map](../research/action-audit/skill-to-actions.md) links the fifteen catalogue entries to all 77 audited operations. Each operation's action records state proposed helper inputs/outputs, existing API dependencies, software and agent decisions, validation cases and recovery. The [workflow-to-action index](../research/action-audit/workflow-to-actions.md) preserves the original 38 routes and their ordered steps. The existing OCS skill retains its documented capability; the map records proposed packaging and supported-backend conditions.

## Component-driven implementation

[Component CAD iterations](cad-ocs-engineering/SKILL.md) uses the external project's existing part index/dictionary, checks source readiness, records individual action occurrences and requires an applied verified skill/script improvement per completed CAD design. [Python part-index access](../scripts/part_index.py) and [component source/action records](../scripts/component_records.py) operate on explicit data paths; FERME retains its parts data, CAD and component evidence.
# Implemented source intake

1. [Record source files, revisions and job scope](cad-source-intake/SKILL.md) implements source capture, corrections and protected revisions for the shared intake action. [Execution evidence](../execution/source-intake.md).

## Implemented DXF inspection

1. [Inspect a DXF drawing before selecting a profile](cad-drawing-inspection/SKILL.md) records source entities, units, spaces, layers and nested block transforms. [Execution evidence](../execution/dxf-inspection.md).

## Continuing iterations and repository ownership

1. Implemented shared procedures include component iteration, source intake, drawing inspection and existing-model checking. The fifteen workflow groups above retain their recorded proposal/implementation status.
2. [Modeling-agent instructions](../research/repository-split-preparation/modeling-agent-instructions.md) define output routing: component recipes/evidence in FERME; shared helper/skill improvements here. Preserve active paths while historical migration is prepared.
3. [Script-change specification](../research/repository-split-preparation/script-changes.md) records the external cadtools dependency, component recipe extraction and integration-test changes proposed for migration.
