# CAD-R09 — Research reconstruction from orthographic projections

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 5/5; setup 5/5; computing 3/5.**

Output: cad-solid + parametric-source

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. vector-drawing
2. measurement-set
3. model-brief

## Detailed source and preparation artifacts

1. Artifact: vector-drawing; Format: DXF or SVG with registered orthographic views where required; Requirement: calibrated orthographic views with sufficient overlap/features; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** calibrated orthographic views with sufficient overlap/features
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: Published; Role: Published orthographic reconstruction methods; License: Research paper only; no software licence implied.; Apis: Published orthographic reconstruction method; no general-purpose CLI; use as mathematical method reference; Dependencies: Paper does not assert an installable dependency; manual implementation uses FreeCAD Sketcher and Part.; Source urls: https://xnjdxb.swjtu.edu.cn/en/article/id/9616; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md
2. Name: FreeCAD; Role: FreeCAD Sketcher/Part; License: LGPL-2.1-or-later per project licensing page.; Apis: FreeCAD Python console/macros; App.newDocument; Sketcher::SketchObject.addGeometry/addConstraint; Part::Feature.Shape or PartDesign::Body/Feature for solids; ViewPart/TechDraw orthographic projection; import/export via Draft/Part; Dependencies: FreeCAD application with bundled Python, Sketcher, Part and (for assemblies) chosen Assembly workbench; system Python generally cannot import FreeCAD modules.; Source urls: https://xnjdxb.swjtu.edu.cn/en/article/id/9616; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md

## Procedure

1. Order: 1; Action: Normalize projection/scales; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: infer correspondence and topology; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: solve candidate geometry; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: encode a constrained CAD model; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: compare rendered projections against source views.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-06; Name: Register orthographic drawing views in a shared coordinate frame; Inputs: vector-drawing; Outputs: model-brief; Tools: view segmentation; projection-axis declaration; line/vertex matching; dimension reconciliation; Source urls: https://xnjdxb.swjtu.edu.cn/en/article/id/9616; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html; Prerequisites: The vector drawing contains multiple identified orthographic views.; Identify front/top/side and first-angle/third-angle layout.; Identify view scales and shared datum from geometry or annotations.; Keep each source view 2D axes and projection direction.; Treat the input vector-drawing as a bundle containing at least two identified orthographic views, not as a single view.; Preserves: View labels and source coordinates; Per-view scales; Candidate feature correspondences; Changes or infers: Maps 2D view coordinates into common 3D projection coordinates and proposes corresponding edges.; Checks: Projected edge coordinates agree across views within source resolution/tolerance.; Control dimensions agree across views.; Flag multiple possible correspondences.; Alternatives: Manual view alignment in OCS/FreeCAD; Orthographic line-matching reconstruction research methods; Automation: assisted; Evidence status: proposed_composition; Summary: Published methods establish coordinate-transform and cross-view matching routes; a learned reconstruction must still be checked against the actual drawing dimensions.
2. Id: CAD-07; Name: Reconstruct a candidate 3D wireframe and surface from orthographic views; Inputs: vector-drawing; measurement-set; model-brief; Outputs: cad-solid; measurement-set; Tools: multi-view edge correspondence; wireframe/face reconstruction; OpenCASCADE or FreeCAD surface/solid creation; Source urls: https://www.sciencedirect.com/science/article/pii/S0097849323000766; https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html; Prerequisites: Register views and scale before matching.; Resolve edge and face ambiguity using dimensions, section views or author input.; Mark inferred surfaces and hidden features.; Preserves: Input views and cross-view correspondence graph; Explicitly traced dimensions; Changes or infers: Creates candidate 3D edges, faces and a watertight solid; hidden surfaces are inferred from the view set and method.; Checks: Project generated model into each input view and compare edge residuals.; Check manifold/solid validity, dimensions and feature count.; Compare native feature history separately from imported shape.; Alternatives: Human-in-the-loop FreeCAD feature reconstruction; Construct a CSG feature program from confirmed views; Automation: assisted; Evidence status: proposed_composition; Summary: Proposed composition of published orthographic reconstruction methods and a CAD kernel: candidate edges/faces may be inferred from multiple views. This research does not document a deployable open reconstruction application.
3. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `Human match corresponding edges across calibrated views; FreeCAD Sketcher::SketchObject.addGeometry/addConstraint; FreeCAD Part Design workbench: invoke Pad/Pocket on reviewed sketches; render aligned orthographic views for comparison`; Status: existing_tool_entrypoint; Source urls: https://xnjdxb.swjtu.edu.cn/en/article/id/9616; https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md; Notes: Published methods guide view correspondence; all feature choices remain manually reviewed. No research code was installed or executed.

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

1. **Human:** 5
2. **Setup:** 5
3. **Compute:** 3
4. **Human reason:** Ambiguity and hidden geometry require iterative expert interpretation.
5. **Setup reason:** Research method implementation/custom correspondence and geometry adapter.
6. **Compute reason:** CPU geometry moderate; solving complexity scales with features/views; papers describe methods rather than ready-to-run tools.

## Resources and scaling

1. **Cpu:** CPU geometry moderate; solving complexity scales with features/views; papers describe methods rather than ready-to-run tools.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with projection views, correspondence candidates and solid hypotheses.
4. **Storage:** Preserve projection originals, correspondence graph, method code and candidate solids.
5. **Scaling drivers:** projection views, correspondence candidates and solid hypotheses
6. **Variants:** Manual CAD baseline; learned research variants need their own model environment.

## Original sources

1. [https://xnjdxb.swjtu.edu.cn/en/article/id/9616](https://xnjdxb.swjtu.edu.cn/en/article/id/9616)
2. [https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md)

Full source summaries: [source register](../../sources/source-register.md).
