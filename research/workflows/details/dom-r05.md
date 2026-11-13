# DOM-R05 — Sketch overlay on existing model to controlled revision

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 2/5; computing 1/5.**

Output: New native CAD revision with sketch-derived constraints and updated exports linked to source revision.

## Comparison conditions

Existing editable native model, sketch/image with at least two measured references, explicit requested edit and source datum mapping.

## Registered starting artifact types

1. raster-sketch
2. vector-drawing
3. cad-solid
4. model-brief
5. dimensions
6. measurement-set

## Detailed source and preparation artifacts

1. Type: native-model-document; Formats: OCS native document; FCStd; Blender .blend; Minimum quality: Opens in owning application; source hash/revision and units known.; Required evidence: file hash; application/version; unit/frame; Handling: Never overwrite source.
2. Type: raster-sketch; Formats: PNG/JPEG/PDF; Minimum quality: Unoccluded lines and at least two independent dimensions/anchors in model frame.; Required evidence: anchor IDs; dimensions; source/status; Handling: Overlay is evidence for constraints, not geometry by itself.
3. Type: model-brief; Formats: text/JSON; Minimum quality: Exact changed features and retained constraints.; Required evidence: feature IDs; scope; tolerances/status; Handling: Ambiguities remain explicit.

## Reference points, datums and coordinate frames

1. Kind: overlay anchors; Fields: pixel coordinate; model coordinate; uncertainty; Frame: sketch pixels → model plane/frame; Source status: measured dimensions/model datums
2. Kind: edit constraints; Fields: dimension and feature references; Frame: new sketch plane → model coordinates; Source status: author instruction

## Software, libraries and dependencies

1. Name: OCS engineering workflow; Role: native geometry revision with frames/provenance; Software license: Local engineering skill / tool-specific terms; Api or entrypoint: OCS skill: explicit units, axes, boundaries, checks; project file opened in OCS; Environment dependencies: Installed OCS environment; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Native editor/runtime remains required; helper code does not issue application commands.; Source urls: SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); [cad-and-skills.md](../../cad-and-skills.md)
2. Name: Blender Python; Role: mesh/sculpt/rendering route when source is a Blender scene; Software license: GPL-3.0-or-later application; asset licenses separate; Api or entrypoint: Background Python `bpy` or UI edit; `blender --background source.blend --python edit.py`; Environment dependencies: Blender-compatible Python and version; Version status: documented source current at 2026-11-12; project install/runtime not exercised; Limitations and asset terms: Mesh edits do not create parametric feature history.; Source urls: https://docs.blender.org/manual/en/latest/advanced/command_line/

## Procedure

1. Action: Duplicate source document and record revision/hash.; Tool: Native CAD application; Command or api: Save a new revision path; retain source and provenance manifest.; Preserves: Original model; Changes or infers: Revision branch.; Check: Reopen source and derivative; compare hashes.; Code status: manual
2. Action: Register sketch anchors to existing datums.; Tool: OCS/FreeCAD/Blender; Command or api: Use measured anchors; constrain scale, rotation and plane; record residuals.; Preserves: Sketch and source model; Changes or infers: Transform only.; Check: Check remaining anchors and dimension residuals.; Code status: assisted
3. Action: Edit native feature or mesh using explicit feature scope.; Tool: Native modeler; Command or api: Apply only named edits and constraints; record changed objects/features.; Preserves: Original constraints; Changes or infers: Native revised model.; Check: Measure changed and retained dimensions; inspect topology.; Code status: manual
4. Action: Export requested neutral/display format as derivative.; Tool: Owning application; Command or api: Use format exporter and record settings/mapping.; Preserves: Native revised file; Changes or infers: STEP/IFC/glTF/OBJ derivatives; semantics vary.; Check: Round-trip reopen and compare bounds/units/IDs.; Code status: existing_tool_entrypoint

## Inputs, outputs and requirements at each registered operation

1. Id: DOM-02; Name: Raster sketch to constrained sketch; Inputs: raster-sketch; Outputs: constrained-sketch; Tools: OpenCADStudio; FreeCAD Sketcher; manual image tracing; Source urls: [implementation-plan.md](../../implementation-plan.md); [cad-and-skills.md](../../cad-and-skills.md); Prerequisites: Known scale or one or more dimension controls; sketch plane/orientation identified.; Preserves: Raster source, pixel coordinates, interpreted scale and dimension-to-pixel references.; Changes or infers: Pixels become line/arc geometry; undimensioned lengths remain image estimates.; Checks: Dimensions trace to source; closure/constraint state; view consistency; scale residual on independent controls.; Alternatives: Vectorization for clean line art; manual constrained sketch for engineering drawings.; Automation: assisted; Evidence status: documented_capability; Summary: Turn a calibrated sketch image into constrained 2D geometry while retaining pixel evidence.; Source ids: DSRC-01; DSRC-03; Input alternatives: dimensions; measurement-set
2. Id: DOM-03; Name: DXF/SVG drawing to constrained profile; Inputs: vector-drawing; Outputs: constrained-sketch; Tools: OpenCADStudio; FreeCAD Sketcher; CadQuery DXF import; OpenSCAD DXF linear_extrude; Source urls: [cad-and-skills.md](../../cad-and-skills.md); [implementation-plan.md](../../implementation-plan.md); Prerequisites: Source units, layers/blocks, target sketch plane and intended entities identified.; Preserves: Source drawing, entity/layer IDs and original coordinates.; Changes or infers: Select/clean curves, convert units if needed, close profiles and apply constraints.; Checks: Open/closed profiles, self-intersections, holes, bounds/area and source dimension comparisons.; Alternatives: OCS-native DXF editing; FreeCAD sketch import; CadQuery DXF profile route.; Automation: mixed; Evidence status: documented_capability; Summary: Create editable profiles from vector drawing entities with explicit filtering and unit handling.; Source ids: DSRC-03; DSRC-01
3. Id: DOM-04; Name: Brief/profile to native CAD solid; Inputs: ; Outputs: native-model-document; cad-solid; Tools: OpenCADStudio baseline; FreeCAD; CadQuery; build123d; OpenSCAD; Source urls: [implementation-plan.md](../../implementation-plan.md); [cad-and-skills.md](../../cad-and-skills.md); README.md (`${OCS_ROOT}/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); Prerequisites: Dimensions, datums, units and component boundaries resolved; backend supports required solid features.; Preserves: Input geometry evidence, editable native document or script and parameter names.; Changes or infers: Construct features/booleans; any assumed design values remain labeled as assumptions.; Checks: Solid validity, feature/part counts, analytic surfaces, controlling dimensions, saved-file reopen.; Alternatives: Interactive OCS/FreeCAD; code-parametric CadQuery/build123d; OpenSCAD CSG source.; Automation: mixed; Evidence status: documented_capability; Summary: Author a CAD solid and save the editable native document. OCS documents/solids need not contain procedural feature history; use DOM-40 for script-based parametric source.; Input alternatives: model-brief; constrained-sketch; parametric-source; Source ids: DSRC-01; DSRC-03; DSRC-04; DSRC-05
4. Id: DOM-05; Name: Export STEP solid; Inputs: ; Outputs: step-file; Tools: OCS STEP exporter; FreeCAD/Open CASCADE STEP import/export; Source urls: [local-baseline.md](../../local-baseline.md); [cad-and-skills.md](../../cad-and-skills.md); README.md (`${OCS_ROOT}/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); Prerequisites: Source/target frame and units declared; recipient supports the chosen STEP schema.; Preserves: Source native file, part identifiers and original STEP bytes.; Changes or infers: Exporter may tessellate or flatten feature history; OCS inspected writer emits planar faces from triangles.; Checks: Reopen in independent consumer; compare solids, bounds, volume, holes and analytic surface types.; Alternatives: Native document for feature history; STEP for geometry exchange; STL/OBJ for mesh-only exchange.; Automation: scripted; Evidence status: local_source_inspected; Summary: Export a CAD solid or B-rep to a neutral STEP file; feature history and exactness depend on the source exporter.; Input alternatives: cad-solid; b-rep; Source ids: DSRC-06; DSRC-03; DSRC-04; DSRC-05
5. Id: DOM-24; Name: Assemble and inspect Blender scene; Inputs: ; Outputs: visual-scene; Tools: Blender Python API; Blender MCP; background Blender scripts; Source urls: https://www.blender.org/features/pipeline/; https://projects.blender.org/lab/blender_mcp/src/branch/main; https://github.com/blender/blender/blob/main/doc/python_api/rst/info_tips_and_tricks.rst; https://uxplanet.org/3d-modeling-with-claude-code-a-practical-blender-workflow-97e6e0b536b0; Prerequisites: Input adapters resolve; transform, units, geometry role and licenses recorded.; Preserves: Source files, object/component IDs, import mapping, unit and axis transforms.; Changes or infers: Builds a render scene, materials/cameras, mesh derivatives; scene-only outputs can drop CAD/BIM/robot semantics.; Checks: Transform/numeric bounds, linked asset paths, representative camera views, exported GLB reopen and object mapping.; Alternatives: Direct scripted background processing for repeatability; MCP for iterative live inspection; OCS remains engineering baseline.; Automation: mixed; Evidence status: documented_capability; Summary: Use Blender for visual composition, mesh work and inspection while retaining native domain models; a camera-solution input alone can produce a camera-only scene.; Source ids: DSRC-31; DSRC-34; DSRC-35; DSRC-39; Input alternatives: cad-solid; mesh; ifc; robot-assembly; camera-solution

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Path: See the selected tool/variant contract.; Summary: Use the software/API entry points below in the recorded procedure; manual CAD, joint and semantic authoring steps use the explicit frames and source data recorded for that step.; Related entrypoints: ; Source urls: SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); [cad-and-skills.md](../../cad-and-skills.md); https://docs.blender.org/manual/en/latest/advanced/command_line/; Entrypoints: OCS skill: explicit units, axes, boundaries, checks; project file opened in OCS; Background Python `bpy` or UI edit; `blender --background source.blend --python edit.py`

## Output artifacts

1. Type: native-model-document; Format: Native application file; Retained: Editable document and retained supported feature history.; Loss or inference: Mesh routes may lack parametric history.
2. Type: cad-solid; Format: STEP/IFC/mesh export as requested; Retained: Exchange geometry.; Loss or inference: Neutral conversion may lose constraints, names, materials and history.

## Checks

1. Source revision preserved and edit IDs recorded.
2. Anchor transform residual below authored tolerance.
3. Changed and retained dimensions checked.
4. Native document reopens; export independently reopens.

## Failure recovery

1. Anchor residual excessive: remeasure/identify sketch plane; do not distort model.
2. Topology breaks: revert derivative, use datum-based feature edit or adjust upstream feature.
3. Only image exists: treat reconstruction as proposal and require dimensions before manufacturing geometry.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 2
3. **Compute:** 1
4. **Human reason:** With measured anchors and specified edit, little interpretation is needed.
5. **Setup reason:** One existing application or script.
6. **Compute reason:** Transform and a few geometry edits are light CPU work.

## Resources and scaling

1. **Cpu:** CPU native CAD and file parsing.
2. **Gpu:** No GPU for constrained sketch; optional Blender rendering.
3. **Ram:** Model feature/mesh count and image size.
4. **Storage:** Native revisions and exported derivatives.
5. **Scaling drivers:** image resolution; feature count; mesh density
6. **Variants:** Clean sketch and native source easiest.; Raster-only outline requires tracing and more effort.

## Detailed branch procedures

1. [cad-r02.md](cad-r02.md)
2. [cad-r04.md](cad-r04.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. ${CODEX_HOME}/skills/ocs-engineering/SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`)
2. [${MODELING_ROOT}/research/cad-and-skills.md](../../cad-and-skills.md)
3. [https://docs.blender.org/manual/en/latest/advanced/command_line/](https://docs.blender.org/manual/en/latest/advanced/command_line/)

Full source summaries: [source register](../../sources/source-register.md).
