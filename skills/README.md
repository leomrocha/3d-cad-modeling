# Project skill catalogue

## Skills supplied by this repository

1. [component-cad](component-cad/SKILL.md) — checks for existing models, binds source requirements, guides native CAD construction and verifies saved results.
2. [drawing-inspection](drawing-inspection/SKILL.md) — inventories DXF entities, units, layers, spaces and nested transforms.
3. [source-intake](source-intake/SKILL.md) — preserves source files, hashes, request scope and corrected input revisions.

Install these skills using the [README instructions](../README.md#installing). The [tools page](../docs/tools.md) lists the Python helpers. Native CAD control uses the separately installed `ocs-engineering` skill.

## Component CAD procedure index

1. **Job contract:** [component requirements and action records](component-cad/references/component-procedure.md).
2. **Model reuse:** [existing-model checks and configuration selection](component-cad/references/existing-model-start-check.md).
3. **Source interpretation:** [drawing features](component-cad/references/drawing-feature-checks.md), [limits, datums, drawing scale and dual units](component-cad/references/dimension-limits-and-datums.md), [source-image inspection and retrieval routes](component-cad/references/source-view-evidence.md), [variant tables and fastener standard editions](component-cad/references/source-variant-tables.md).
4. **Traced geometry:** [calibrated coordinates](component-cad/references/calibrated-trace.md), [source-vector perimeter chains](component-cad/references/source-perimeter-chains.md), [profile extrusion](component-cad/references/profile-reference.md).
5. **Construction:** [rounded hollow sections](component-cad/references/source-first-and-tube.md), [axial motors](component-cad/references/axial-motor.md), [rectangular envelopes](component-cad/references/envelope-reference.md), [guarded envelope runner](component-cad/references/envelope-job-runner.md), [Pixhawk clearance geometry](component-cad/references/pixhawk.md), [annular references](component-cad/references/annular-reference.md), [hexagonal references](component-cad/references/hexagonal-reference.md).
6. **Component checks:** [bearing geometry](component-cad/references/existing-bearing.md), [battery shells and terminals](component-cad/references/existing-battery.md), [tabbed battery cases](component-cad/references/tabbed-battery.md), [smallBMS saved geometry](component-cad/references/small-bms.md), [shared feature comparisons](component-cad/references/shared-feature-checks.md).
7. **Assemblies:** [manufacturer placements](component-cad/references/manufacturer-assembly.md), [scaled imports](component-cad/references/scaled-assemblies.md), [root unit-change plans](component-cad/references/assembly-units.md), [STEP solid inventories](component-cad/references/step-solid-inventory.md).
8. **Completion:** [saved source metadata](component-cad/references/source-metadata.md), [retained-file manifests](component-cad/references/retained-artifact-checks.md), [owned-document cleanup](component-cad/references/document-cleanup.md).

The circular-section torus procedure is being added in the modeling work. Its current development status is listed on the [tools page](../docs/tools.md#helpers-in-progress).

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

[Component CAD iterations](component-cad/SKILL.md) uses the external project's existing part index/dictionary, checks source readiness, records individual action occurrences and requires an applied verified skill/script improvement per completed CAD design. [Python part-index access](../scripts/part_index.py) and [component source/action records](../scripts/component_records.py) operate on explicit data paths; FERME retains its parts data, CAD and component evidence.
# Implemented source intake

1. [Record source files, revisions and job scope](source-intake/SKILL.md) implements source capture, corrections and protected revisions for the shared intake action. [Execution evidence](../execution/source-intake.md).

## Implemented DXF inspection

1. [Inspect a DXF drawing before selecting a profile](drawing-inspection/SKILL.md) records source entities, units, spaces, layers and nested block transforms. [Execution evidence](../execution/dxf-inspection.md).

## Continuing iterations and repository ownership

1. Implemented shared procedures include component iteration, source intake, drawing inspection and existing-model checking. The fifteen workflow groups above retain their recorded proposal/implementation status.
2. [Modeling-agent instructions](../research/repository-split-preparation/modeling-agent-instructions.md) define output routing: component recipes/evidence in FERME; shared helper/skill improvements here. Preserve active paths while historical migration is prepared.
3. [Script-change specification](../research/repository-split-preparation/script-changes.md) records the external cadtools dependency, component recipe extraction and integration-test changes proposed for migration.
