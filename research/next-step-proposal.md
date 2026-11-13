# Proposed next stages

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 12 November 2026. Status: proposal.

This proposal develops the existing [implementation plan](implementation-plan.md) using the [workflow map](workflows/README.md). It preserves that plan's sequence and adds a focused evidence review before implementation. The starting checkpoint for documenting this proposal is `6ef39be`.

## 1. Resolve the handoffs needed by the first pilots

Scope: use the registered research to prepare four route cards: text/dimensions to native CAD; sketch/DXF to CAD; photographs/controls to remodeled CAD; and component assemblies to IFC or MJCF.

1. Review the exact tool/API, input/output representation, editable source, units, frames, licence and hardware prerequisites at each transition.
2. Use targeted Luna research for specific source gaps: OCS native solids and interchange, reconstruction scale/camera transforms, and IFC/robot semantic mapping. Reuse existing source records and archived originals.
3. Separate documented capabilities, locally exercised operations, proposed handoffs and experimental methods in the route cards.
4. Record each tool choice as a proposal with the source evidence and fixture that would test it.

Deliverable: route-selection table, four route cards, source updates and a bounded list of experiments. This is the proposed immediate work package because the current map already supplies operation families and source references.

Evidence: [CAD paths](workflows/cad-paths.md), [reconstruction paths](workflows/reconstruction-paths.md), [domain paths](workflows/domain-paths.md), [original sources](sources/source-register.md).

## 2. Define shared model and component records

1. Specify records for the model brief, original evidence, artifact/revision, component, named interface frame and execution/check report.
2. Carry units, transforms, component identities, dimensions, inference labels, source hashes and licences through every derivative.
3. Include separate visual, collision, CAD and semantic representations in each component record.
4. Define three fixture briefs: a dimensioned bracket and mating plate; a room with an opening; and a rigid photographed object with independent control measurements. Fixture dimensions and check tolerances come from their declared briefs.

Deliverable: versioned record schemas, fixture specifications and a small pilot component catalogue structure. These records give the different tools a common exchange contract.

Evidence: [component contract](implementation-plan.md#6-component-library-contract), [representation definitions](workflows/representations.json), [composition rules](workflows/composition-rules.md).

## 3. Establish the OCS modeling baseline

1. Reuse [OCS engineering (`cad-ocs-engineering`)](../skills/cad-ocs-engineering/SKILL.md) and record the actual session/build capabilities used by the fixture. Original source: `${CODEX_HOME}/skills/ocs-engineering/SKILL.md`.
2. Model the bracket and mating plate with named parts, declared datums and dimensions; make one parameter or dimension revision through the supported native workflow.
3. Read back dimensions, part identity and geometry; save and reopen the native document; inspect the requested derivative in its receiving application.
4. Record the STEP export's actual surface representation alongside native-solid results. The inspected exporter consumes tessellated meshes.

Deliverable: an exercised OCS route, capability receipt, native example, measured checks and focused skill improvements. This stage builds directly on the user's reported partial local success.

Evidence: [local baseline](local-baseline.md), [OCS source exporter](https://github.com/HakanSeven12/OpenCADStudio/blob/main/src/io/step.rs).

## 4. Validate text, sketches and 2D drawings to CAD

1. Use the same bracket brief for text/dimensions, a raster sketch and a DXF/SVG profile.
2. Compare build123d and CadQuery for the procedural-solid route; assess FreeCAD where editable constrained sketches and feature history are required.
3. Verify profile closure, dimension association, solid validity, analytic surfaces, component count and saved-output readback.
4. Derive a Blender visual asset and compare its scale, axes and component placements with the source CAD.

Deliverable: one documented procedural-solid route, a drawing-to-CAD workflow, Blender derivatives and reusable skill scripts. Using the same fixture supports a direct comparison of the routes.

Evidence: [CAD skill assessment](cad-and-skills.md), [CAD recipes](workflows/cad-paths.json), [build123d](https://github.com/gumyr/build123d), [CadQuery](https://github.com/CadQuery/cadquery), [FreeCAD](https://github.com/FreeCAD/FreeCAD).

## 5. Validate measured reconstruction and mixed-input remodeling

1. Reconstruct the rigid-object fixture from overlapping photographs and measured controls through a selected COLMAP/Meshroom route.
2. Keep calibration, scale fitting and independent assessment measurements as distinct evidence roles. Report residuals in millimetres for the checked regions and dimensions.
3. Use Open3D/CloudCompare to register surfaces, segment regions and derive feature-fit evidence; remodel selected features through the existing CAD contract.
4. Combine a scan with a drawing or an identified library component, preserving source disagreements and inference labels.
5. Add the sketch-over-3D loop: store the camera and calculated surface anchors, interpret feature intent, revise native CAD and compare the changed revision.
6. Compare Gaussian visual context and learned image-to-3D outputs against the same references as optional branches, recording their representation and dimensional evidence.

Deliverable: photo/scan-to-reference, scan-to-CAD and annotation/edit workflows with retained inputs and deviation reports. These connect photographic and sketch evidence to editable geometry.

Evidence: [reconstruction assessment](reconstruction.md), [reconstruction operations](workflows/reconstruction-paths.json), [combined workflows](workflows/combined-workflows.md).

## 6. Validate architecture, robotics and component reuse

1. Create the room fixture as semantic IFC with a storey, wall, opening and placed component; check geometry, object identities and relationships.
2. Build an articulated assembly with explicit bodies, joints, axes, limits and source-linked physical properties. Export MJCF and URDF where required by the consumers.
3. Produce separate visual and collision assets; check units, transforms, joint motion and selected contact cases in the loaded model.
4. Combine the building or scanned environment with the robot scene using recorded coordinate transforms.
5. Populate the pilot catalogue with authored parts, an assembly, an architectural element and selected sourced components. Retain item-level licences and named interfaces.

Deliverable: IFC and robot examples, source/component mappings, domain workflow skills and a reusable pilot library. These demonstrate the named architecture and robotics uses with the same provenance contract.

Evidence: [domain assessment](domains-and-components.md), [domain operations](workflows/domain-paths.json), [IFC/MuJoCo combinations](workflows/combined-workflows.md).

## 7. Package the exercised workflows

1. Give each exercised workflow a focused `SKILL.md`, scripts, references, supported versions and an example.
2. Add a shared CLI for intake, component lookup, execution, checks and explicit export.
3. Pin dependencies by workflow family and retain job state, logs, source revisions and output hashes.
4. Re-run the relevant fixture after a tool, skill, component or format-adapter change; record the measured result and changed capability status.
5. Apply the before/after commit and full source/idea registration rules to every work package.

Deliverable: a reusable modeling toolkit whose supported routes have executable examples and recorded checks. This packages the workflows exercised by the preceding stages.

Evidence: [skill catalogue](../skills/README.md), [existing integration stage](implementation-plan.md#stage-6--workflow-integration), [documentation policy](documentation-policy.md).
