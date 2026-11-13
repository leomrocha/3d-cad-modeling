# CAD-R07 — Depth scan aligned to existing housing

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 3/5.**

Output: cad-solid + measurement-set

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. depth-frames
2. cad-solid
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: depth-frames; Format: Raw depth/RGB images, intrinsics, depth scale, poses/extrinsics; Requirement: calibrated depth frames and known housing datum/features; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** calibrated depth frames and known housing datum/features
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: Open3D; Role: Open3D RGB-D/TSDF; License: MIT.; Apis: open3d.pipelines.integration.ScalableTSDFVolume; RGBDImage.create_from_color_and_depth; TSDFVolume.integrate(rgbd,intrinsic,extrinsic); Dependencies: Python Open3D, NumPy; RGB-D integration needs calibrated intrinsics and per-frame poses/depth scale.; Source urls: https://github.com/CloudCompare/CloudCompare
2. Name: CloudCompare; Role: CloudCompare; License: GPL-2.0-or-later application; CCLib LGPL-2.0 per repository.; Apis: CloudCompare CLI: CloudCompare -O cloud.ply -C_EXPORT_FMT PLY -SAVE_CLOUDS; GUI align/register tools; Dependencies: CloudCompare desktop/CLI; plugins optional for specialized formats.; Source urls: https://github.com/CloudCompare/CloudCompare
3. Name: OCS/FreeCAD; Role: OCS/FreeCAD; License: OCS GPL-3.0; FreeCAD LGPL-2.1-or-later.; Apis: OCS --mcp: ocs_sessions/ocs_read/ocs_execute; FreeCAD Part::Feature/PartDesign::Body; Point-cloud alignment in Open3D/CloudCompare then explicit transform; Dependencies: OCS desktop+MCP and existing ocs-engineering helper or FreeCAD application Python.; Source urls: https://github.com/CloudCompare/CloudCompare

## Procedure

1. Order: 1; Action: Fuse calibrated depth frames to cloud/mesh; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: register to datum; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: compare measured envelope/interfaces; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: remodel only required interface geometry; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: verify deviations.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-11; Name: Fit analytic features to scans or image-derived point clouds; Inputs: ; Outputs: measurement-set; cad-solid; Tools: point-cloud registration and segmentation; least-squares plane/cylinder/axis fits; FreeCAD/build123d; Source urls: [reconstruction.md](../../reconstruction.md); README.md (`${ARCHITECTURE_ROOT}/research/README.md`); Prerequisites: Input is already a metric, registered point cloud, depth sequence, or mesh with a declared coordinate frame.; Identify functional interfaces and label unsampled/occluded surfaces.; Keep fit residuals and input samples with each analytic feature.; Preserves: Original images/depth/point samples; Camera solution and transforms; Feature-fit inputs and residual records; Changes or infers: Fits planes, cylinders, axes or freeform surfaces from noisy samples; fits are calculated approximations.; Checks: Independent control distances; Registration and reprojection residuals; Fit residual distribution/outlier mask; Held-out cloud-to-CAD distances; Interface dimensions; Alternatives: Manual measurements from calibrated views; Use mesh as visual/collision reference without analytic remodeling; Automation: assisted; Evidence status: proposed_composition; Summary: Fit analytic planes, cylinders and axes to an already calibrated/registered metric point cloud, depth sequence or mesh, retaining residuals and uncertain regions. Photograph-to-cloud reconstruction is a separate upstream operation.; Input alternatives: depth-frames; measurement-set; point-cloud; measurement-set; mesh; measurement-set
2. Id: CAD-12; Name: Assemble existing CAD or source-library components; Inputs: cad-solid; Outputs: cad-assembly; Tools: OCS blocks/groups; FreeCAD App::Link/Assembly; build123d/CadQuery Assembly; unit and frame mapping; Source urls: [domains-and-components.md](../../domains-and-components.md); README.md (`${OCS_ROOT}/docs/automation/README.md`); https://cadquery.readthedocs.io/en/stable/; Prerequisites: Record component source/license/hash and representation.; Establish local units, origin, axis directions and interface frames for each part.; Separate source components from placeholders.; Provide a distinct base cad-solid plus either a source-library component or one or more additional cad-solid component files; identify each occurrence separately.; Preserves: Component identities and source files; Occurrence transforms and assembly hierarchy; Native component boundaries; Changes or infers: Places parts using declared mating frames; inferred contact or fastener geometry is proposal unless sourced.; Checks: Frame/transform consistency; Interface dimension agreement; Component counts and source hashes; Collision/clearance only with supported exact geometry and query; Alternatives: Visual-only assembly in Blender; OCS block/group drawing arrangement; Full parametric assembly in FreeCAD or Python code-CAD; Automation: mixed; Evidence status: proposed_composition; Summary: Build an assembly from identified components and explicit transforms; preserve the difference between imported component geometry and inferred placeholders.; Input alternatives: source-library; cad-solid
3. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `Open3D ScalableTSDFVolume.integrate(rgbd,intrinsic,extrinsic); CloudCompare registration/alignment; FreeCAD Part::Feature remodeling`; Status: existing_tool_entrypoint; Source urls: https://github.com/CloudCompare/CloudCompare; Notes: Documented application/API workflow. Human review steps remain manual; command/runtime not exercised in this research.

## Output artifacts

1. **Representations:** cad-solid; measurement-set
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: scan registration; Quantity: control-point residuals, interface distances and bounds; Unit: mm; Acceptance: residuals below declared sensor/measurement tolerance; Method: Open3D/CloudCompare registration report and independent caliper/control check.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 3
4. **Human reason:** Registration and inaccessible interfaces require review; existing housing constrains alignment.
5. **Setup reason:** Depth sensor calibration and point-cloud tools.
6. **Compute reason:** Moderate-to-high CPU/RAM by frame count/resolution; GPU optional by backend.

## Resources and scaling

1. **Cpu:** Moderate-to-high CPU/RAM by frame count/resolution; GPU optional by backend.
2. **Gpu:** CPU geometry baseline; graphics display acceleration is separate.
3. **Ram:** Scales with depth frame count, TSDF voxels and cloud points.
4. **Storage:** Preserve depth/RGB, calibration, poses, fused cloud and housing CAD.
5. **Scaling drivers:** depth frame count, TSDF voxels and cloud points
6. **Variants:** Registered cloud skips upstream fusion; raw frames need calibration and fusion.

## Detailed branch procedures

1. [rec-r09.md](rec-r09.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://github.com/CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare)

Full source summaries: [source register](../../sources/source-register.md).
