# REC-R10 — Single-image mesh proxy and evidence-based CAD remodel

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 4/5.**

Output: Learned single-view mesh proxy, followed by constrained CAD built from supplied independent dimensions and measured data.

## Comparison conditions

One image suffices for a visual proxy. Full CAD path additionally requires measured dimensions, drawing views or other evidence for unseen geometry and scale.

## Registered starting artifact types

1. photo-set
2. measurement-set
3. model-brief

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format and quality: Single object photograph with clean silhouette/lighting; input set contains one selected view.
2. Artifact: measurement-set; Format and quality: Independent dimensions, target frame and observed landmarks for CAD authoring/checks.
3. Artifact: model-brief; Format and quality: Part identity/features and output scope; no dimensions are inferred from brief.

## Reference points, datums and coordinate frames

Image-to-3D models infer backside/occluded surfaces from priors and do not establish physical scale. Measurements provide dimensional evidence. Additional views are required to compare unseen geometry; surface proxy is not editable parametric CAD.

## Software, libraries and dependencies

1. Name: TripoSR; Licence scope: MIT code/model per existing report; Role and api: single-image textured mesh inference; Dependencies: approximately 6 GB VRAM reported upstream
2. Name: TRELLIS.2-4B; Licence scope: MIT repository/model card per existing report; Role and api: single-image mesh/GLB generation; Dependencies: Linux NVIDIA GPU >=24 GB
3. Name: SAM 3D Objects; Licence scope: Custom Meta SAM terms per existing report; Role and api: single-image object reconstruction; Dependencies: Linux NVIDIA GPU >=32 GB
4. Name: OCS; Licence scope: Existing local skill contract; Role and api: constrained CAD remodeling using measured dimensions; Dependencies: OpenCADStudio session

## Procedure

1. Step: 1; Action: For the TripoSR branch, run the upstream documented command `python run.py <single-image> --output-dir <output-folder>` to create a mesh proxy; alternatively run the selected TRELLIS.2 or SAM 3D model under its own documented environment and checkpoint terms. Retain model revision and image provenance.
2. Step: 2; Action: Measure/control source dimensions independently; compare visible silhouette across any extra views.
3. Step: 3; Action: Rebuild selected features with constraints in OCS using supplied dimensions; label unseen geometry as inferred.
4. Step: 4; Action: Read back CAD and compare to independent measurements, not proxy surface alone.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-18; Name: Generate a single-image mesh proxy; Inputs: photo-set; Outputs: mesh; Tools: TripoSR; TRELLIS.2; SAM 3D Objects; Source urls: https://github.com/VAST-AI-Research/TripoSR; https://github.com/microsoft/TRELLIS.2; https://github.com/facebookresearch/sam-3d-objects; Prerequisites: Exactly one selected image and model revision recorded; Model weights and model terms recorded separately from source-code licence; Dimensions or measured controls supplied separately before dimensional CAD use; Preserves: Source image and model/checkpoint metadata; Changes or infers: Predicts backside and occluded geometry from learned priors; Mesh scale is not established by image appearance alone; Checks: Compare silhouette with additional views; Compare explicitly measured dimensions; Mark hidden surfaces as inferred before CAD remodeling; Alternatives: Multi-view photogrammetry or calibrated scan; Automation: scripted; Evidence status: existing_report_registered; Summary: Generate a visual mesh proxy from one image. The output is inferred geometry with no independent metric scale.
2. Id: REC-14; Name: Remodel segmented scan evidence as parametric CAD; Inputs: measurement-set; Input alternatives: point-cloud; mesh; Outputs: constrained-sketch; parametric-source; cad-solid; Tools: Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated; Preserves: Raw scan, segmentation indices and fit report; Dimension provenance for every feature; Changes or infers: Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions; Checks: OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls; Alternatives: Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation; Automation: mixed; Evidence status: proposed_composition; Summary: Use fitted scan geometry as evidence and reconstruct an editable feature history through the existing OCS workflow; fitted parameters must remain traceable and not silently become author dimensions.
3. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Documented third-party tool and API entry points

1. Path: TripoSR CLI (native tool entrypoint; no project script); Status: existing_tool_entrypoint; Entrypoint: `python run.py <single-image> --output-dir <output-folder>`; Source urls: https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md; https://huggingface.co/stabilityai/TripoSR

## Output artifacts

1. Representation: Learned single-view mesh proxy, followed by constrained CAD built from supplied independent dimensions and measured data.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Source silhouette; model/revision/weight terms; dimension comparisons; CAD constraints and units; separate proxy-vs-CAD residual from physical measurement residual.

## Failure recovery

If inferred backside is inconsistent with extra views, retain proxy as visual placeholder and remodel manually. If critical dimensions are absent, stop at mesh proxy; do not scale from image appearance. If model terms exclude intended use, switch model before generating deliverable.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Single-view proxy is easy, but full measured CAD remodeling is hard because unseen shape requires independent evidence and feature decisions.
5. **Setup reason:** Learned model setup, checkpoint terms and OCS CAD environment.
6. **Compute reason:** GPU requirements vary sharply: TripoSR ~6 GB, TRELLIS.2-4B >=24 GB, SAM 3D >=32 GB per existing source reports.

## Resources and scaling

1. **Cpu:** Image preparation and OCS readback use CPU; inference backend may use GPU.
2. **Gpu:** TripoSR ~6 GB; TRELLIS.2-4B >=24 GB; SAM 3D Objects >=32 GB NVIDIA per existing report.
3. **Ram:** Model-specific VRAM plus point/mesh processing; no common system-RAM minimum.
4. **Storage:** Model checkpoints, source images, generated textures/mesh and CAD revisions.
5. **Scaling drivers:** Model family, texture/resolution settings, single-view ambiguity and CAD feature count.
6. **Variants:** Proxy-only route has low human effort and GPU inference; full measured CAD requires more evidence and high human interpretation.

## Original sources

1. [https://github.com/VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR)
2. [https://huggingface.co/stabilityai/TripoSR](https://huggingface.co/stabilityai/TripoSR)
3. [https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)
4. [https://huggingface.co/microsoft/TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)
5. [https://github.com/facebookresearch/sam-3d-objects](https://github.com/facebookresearch/sam-3d-objects)
6. ${CODEX_HOME}/skills/ocs-engineering/SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`)
7. [https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md](https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md)

Full source summaries: [source register](../../sources/source-register.md).
