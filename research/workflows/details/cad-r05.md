# CAD-R05 — Orthographic views to manually reconstructed part

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 3/5; computing 2/5.**

Output: cad-solid + parametric-source

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. vector-drawing
2. measurement-set
3. model-brief

## Detailed source and preparation artifacts

1. Artifact: vector-drawing; Format: DXF or SVG with registered orthographic views where required; Requirement: matched front/top/side views and dimensions; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** matched front/top/side views and dimensions
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: FreeCAD; Role: FreeCAD Sketcher/Part; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html
2. Name: orthographic; Role: orthographic reconstruction methods; License: Research paper only; no software licence implied.; Apis: Published reconstruction formulation; no general-purpose software API claimed; Dependencies: Paper reproduction requires its research code/data if available plus a compatible ML environment; proposed manual CAD route needs FreeCAD only.; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html

## Procedure

1. Order: 1; Action: Establish common datums and projection; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: identify corresponding edges; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: resolve dimensions; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: sketch constrained features; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: compare projected views and dimensions.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-06; Name: Register orthographic drawing views in a shared coordinate frame; Inputs: vector-drawing; Outputs: model-brief; Tools: view segmentation; projection-axis declaration; line/vertex matching; dimension reconciliation; Source urls: https://xnjdxb.swjtu.edu.cn/en/article/id/9616; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html; Prerequisites: The vector drawing contains multiple identified orthographic views.; Identify front/top/side and first-angle/third-angle layout.; Identify view scales and shared datum from geometry or annotations.; Keep each source view 2D axes and projection direction.; Treat the input vector-drawing as a bundle containing at least two identified orthographic views, not as a single view.; Preserves: View labels and source coordinates; Per-view scales; Candidate feature correspondences; Changes or infers: Maps 2D view coordinates into common 3D projection coordinates and proposes corresponding edges.; Checks: Projected edge coordinates agree across views within source resolution/tolerance.; Control dimensions agree across views.; Flag multiple possible correspondences.; Alternatives: Manual view alignment in OCS/FreeCAD; Orthographic line-matching reconstruction research methods; Automation: assisted; Evidence status: proposed_composition; Summary: Published methods establish coordinate-transform and cross-view matching routes; a learned reconstruction must still be checked against the actual drawing dimensions.
2. Id: CAD-07; Name: Reconstruct a candidate 3D wireframe and surface from orthographic views; Inputs: vector-drawing; measurement-set; model-brief; Outputs: cad-solid; measurement-set; Tools: multi-view edge correspondence; wireframe/face reconstruction; OpenCASCADE or FreeCAD surface/solid creation; Source urls: https://www.sciencedirect.com/science/article/pii/S0097849323000766; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html; Prerequisites: Register views and scale before matching.; Resolve edge and face ambiguity using dimensions, section views or author input.; Mark inferred surfaces and hidden features.; Preserves: Input views and cross-view correspondence graph; Explicitly traced dimensions; Changes or infers: Creates candidate 3D edges, faces and a watertight solid; hidden surfaces are inferred from the view set and method.; Checks: Project generated model into each input view and compare edge residuals.; Check manifold/solid validity, dimensions and feature count.; Compare native feature history separately from imported shape.; Alternatives: Human-in-the-loop FreeCAD feature reconstruction; Construct a CSG feature program from confirmed views; Automation: assisted; Evidence status: proposed_composition; Summary: Proposed composition of published orthographic reconstruction methods and a CAD kernel: candidate edges/faces may be inferred from multiple views. This research does not document a deployable open reconstruction application.
3. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `FreeCAD Sketcher::SketchObject.addGeometry/addConstraint; FreeCAD Part Design workbench: invoke Pad/Pocket on reviewed sketches; TechDraw orthographic views; manual correspondence review`; Status: existing_tool_entrypoint; Source urls: https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html; Notes: Documented application/API workflow. Human review steps remain manual; command/runtime not exercised in this research.

## Output artifacts

1. **Representations:** cad-solid; parametric-source
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: orthographic reconstruction; Quantity: projected outlines and explicit dimensions; Unit: source drawing units; Acceptance: front/top/side projections align with source within stated drawing tolerance; Method: Render CAD views from same projection and overlay/compare dimensions.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 3
3. **Compute:** 2
4. **Human reason:** View correspondence, hidden edges and missing dimensions require substantial interpretation.
5. **Setup reason:** CAD app plus view alignment and constraint setup.
6. **Compute reason:** Moderate CPU B-rep; view count/features dominate, no GPU.

## Resources and scaling

1. **Cpu:** Moderate CPU B-rep; view count/features dominate, no GPU.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with view count, matched edges and candidate B-rep topology.
4. **Storage:** Preserve vector views, feature matches, native CAD and projection checks.
5. **Scaling drivers:** view count, matched edges and candidate B-rep topology
6. **Variants:** Vector baseline; raster views add tracing and rectification.

## Original sources

1. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)
2. [https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html)

Full source summaries: [source register](../../sources/source-register.md).
