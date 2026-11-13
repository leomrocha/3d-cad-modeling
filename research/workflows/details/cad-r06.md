# CAD-R06 — Photographs plus scale controls to remodeled part

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 4/5.**

Output: cad-solid + mesh

## Comparison conditions

One bounded input artifact set with the stated minimum quality; no unmeasured dimensions are promoted to fact. Ratings compare complete workflow under current contract scales.

## Registered starting artifact types

1. photo-set
2. measurement-set
3. source-library

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format: Original JPEG/PNG plus camera metadata; Requirement: overlapping calibrated images, scale controls, visible access; Quality: Readable/registered input with explicit units and known provenance.; Provenance: Keep original unchanged; record measurements and source page/frame.

## Reference points, datums and coordinate frames

1. **Datum:** Explicitly selected datum/control origin before reconstruction
2. **Axes:** Record coordinate frame, projection and handedness in the project units
3. **Controls:** overlapping calibrated images, scale controls, visible access
4. **Unit:** Explicit source units; normalize to mm only with documented scale

## Software, libraries and dependencies

1. Name: COLMAP; Role: COLMAP CLI; License: BSD-3-Clause.; Apis: colmap automatic_reconstructor --workspace_path W --image_path I --quality medium; image_undistorter; patch_match_stereo; stereo_fusion; poisson_mesher; Dependencies: COLMAP binary, camera/image inputs; dense MVS often uses CUDA-capable GPU, although sparse reconstruction can be CPU.; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://github.com/colmap/colmap/blob/main/LICENSE
2. Name: Meshroom/AliceVision; Role: Meshroom/AliceVision; License: Meshroom MPL-2.0; AliceVision licensing should be checked for exact component/build.; Apis: Meshroom GUI photogrammetry graph (CameraInit, FeatureExtraction, ImageMatching, FeatureMatching, StructureFromMotion, PrepareDenseScene, DepthMap, DepthMapFilter, Meshing, Texturing); AliceVision CLI nodes; Dependencies: Meshroom plus AliceVision binaries and supported feature/depth nodes; dense stages depend on installed CPU/GPU backend and drivers.; Source urls: https://github.com/alicevision/Meshroom/blob/develop/COPYING.md; https://meshroom.readthedocs.io/en/latest/
3. Name: Open3D; Role: Open3D; License: MIT.; Apis: open3d.pipelines.integration.ScalableTSDFVolume; RGBDImage.create_from_color_and_depth; TSDFVolume.integrate(rgbd,intrinsic,extrinsic); Dependencies: Python Open3D, NumPy; RGB-D integration needs calibrated intrinsics and per-frame poses/depth scale.; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://github.com/alicevision/Meshroom/blob/develop/COPYING.md
4. Name: OCS/FreeCAD; Role: OCS/FreeCAD; License: OCS GPL-3.0; FreeCAD LGPL-2.1-or-later.; Apis: OCS --mcp: ocs_sessions/ocs_read/ocs_execute; FreeCAD Part::Feature/PartDesign::Body; Point-cloud alignment in Open3D/CloudCompare then explicit transform; Dependencies: OCS desktop+MCP and existing ocs-engineering helper or FreeCAD application Python.; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://github.com/alicevision/Meshroom/blob/develop/COPYING.md

## Procedure

1. Order: 1; Action: Capture overlapping views with scale controls; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: documented_capability
2. Order: 2; Action: reconstruct camera poses and dense surface using COLMAP or Meshroom; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
3. Order: 3; Action: register controls; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
4. Order: 4; Action: inspect cloud/mesh; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition
5. Order: 5; Action: remodel engineering features.; Tool or command: Documented tools in software list; Human review: Confirm units, topology, inferred values and representation handoff.; Status: proposed_composition

## Inputs, outputs and requirements at each registered operation

1. Id: CAD-16; Name: Reconstruct camera poses and dense visible geometry from overlapping photos; Inputs: photo-set; measurement-set; Outputs: camera-solution; point-cloud; mesh; Tools: COLMAP or AliceVision/Meshroom; scale/control-point alignment; Source urls: [reconstruction.md](../../reconstruction.md); https://github.com/colmap/colmap; https://github.com/colmap/colmap/blob/main/doc/cli.rst; Prerequisites: Provide overlapping, sharp views of a rigid scene and measured scale/control data.; Inspect image-registration coverage, camera solution and dense-stage output; each output is a reconstruction result, not a direct measurement of hidden surfaces.; Preserves: Input images and source IDs; Estimated camera poses and control-point associations; Raw sparse/dense reconstruction outputs; Changes or infers: Estimates camera poses and visible 3D samples/surfaces from image correspondences; unobserved surfaces and metric values outside control data remain inferred.; Sparse reconstruction scale is fixed from supplied measurement-set controls; local surface detail between/behind views remains estimated or absent.; Checks: Review registered-view coverage, reprojection errors and camera poses.; Check control-point residuals and independent withheld dimensions.; Inspect cloud/mesh for holes, duplicate surfaces and outliers; record scale and frame transforms.; Alternatives: RGB-D/LiDAR point-cloud acquisition; Manual photogrammetry review and reconstruction; Automation: mixed; Evidence status: proposed_composition; Summary: Existing reconstruction research documents COLMAP and Meshroom photo-to-cloud/mesh paths and their quality gates. This operation is a proposed composition from those documented tools; no local runtime was exercised.
2. Id: CAD-11; Name: Fit analytic features to scans or image-derived point clouds; Inputs: ; Outputs: measurement-set; cad-solid; Tools: point-cloud registration and segmentation; least-squares plane/cylinder/axis fits; FreeCAD/build123d; Source urls: [reconstruction.md](../../reconstruction.md); README.md (`${ARCHITECTURE_ROOT}/research/README.md`); Prerequisites: Input is already a metric, registered point cloud, depth sequence, or mesh with a declared coordinate frame.; Identify functional interfaces and label unsampled/occluded surfaces.; Keep fit residuals and input samples with each analytic feature.; Preserves: Original images/depth/point samples; Camera solution and transforms; Feature-fit inputs and residual records; Changes or infers: Fits planes, cylinders, axes or freeform surfaces from noisy samples; fits are calculated approximations.; Checks: Independent control distances; Registration and reprojection residuals; Fit residual distribution/outlier mask; Held-out cloud-to-CAD distances; Interface dimensions; Alternatives: Manual measurements from calibrated views; Use mesh as visual/collision reference without analytic remodeling; Automation: assisted; Evidence status: proposed_composition; Summary: Fit analytic planes, cylinders and axes to an already calibrated/registered metric point cloud, depth sequence or mesh, retaining residuals and uncertain regions. Photograph-to-cloud reconstruction is a separate upstream operation.; Input alternatives: depth-frames; measurement-set; point-cloud; measurement-set; mesh; measurement-set
3. Id: CAD-12; Name: Assemble existing CAD or source-library components; Inputs: cad-solid; Outputs: cad-assembly; Tools: OCS blocks/groups; FreeCAD App::Link/Assembly; build123d/CadQuery Assembly; unit and frame mapping; Source urls: [domains-and-components.md](../../domains-and-components.md); README.md (`${OCS_ROOT}/docs/automation/README.md`); https://cadquery.readthedocs.io/en/stable/; Prerequisites: Record component source/license/hash and representation.; Establish local units, origin, axis directions and interface frames for each part.; Separate source components from placeholders.; Provide a distinct base cad-solid plus either a source-library component or one or more additional cad-solid component files; identify each occurrence separately.; Preserves: Component identities and source files; Occurrence transforms and assembly hierarchy; Native component boundaries; Changes or infers: Places parts using declared mating frames; inferred contact or fastener geometry is proposal unless sourced.; Checks: Frame/transform consistency; Interface dimension agreement; Component counts and source hashes; Collision/clearance only with supported exact geometry and query; Alternatives: Visual-only assembly in Blender; OCS block/group drawing arrangement; Full parametric assembly in FreeCAD or Python code-CAD; Automation: mixed; Evidence status: proposed_composition; Summary: Build an assembly from identified components and explicit transforms; preserve the difference between imported component geometry and inferred placeholders.; Input alternatives: source-library; cad-solid
4. Id: CAD-13; Name: Verify model geometry and saved output; Inputs: ; Outputs: measurement-set; verification-report; Tools: OCS read/measure/audit/save_verified; FreeCAD B-rep readback; build123d/CadQuery shape checks; independent importer; mesh validation; Source urls: README.md (`${OCS_ROOT}/docs/automation/README.md`); step.rs (`${OCS_ROOT}/src/io/step.rs`); SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`); https://build123d.readthedocs.io/en/stable/; Prerequisites: Know the expected geometry representation and destination units.; Tie checks to the exact document revision and output file hash.; Set a check tolerance from source accuracy or explicit engineering requirement.; A fabrication-package is an input artifact to inspect, not an output created by verification.; Preserves: Source revision and hash; Output hash and conversion settings; Measured check results and failed checks; Changes or infers: Reads or reopens derivatives and calculates verification measurements; does not repair by itself.; Checks: Bounds, solid count, face types, volume and key dimensions; Entity/semantic manifest and save audit; Reopen in independent application; Feature history versus geometry-only transfer; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Persist operation IDs, artifact revision/hash, units, result values and failed checks in verification-report.; Alternatives: Visual review as a supplement; Application-native save audit; Separate neutral-file round-trip; Automation: scripted; Evidence status: proposed_composition; Summary: Read back the saved artifact, run applicable checks, and persist measured bounds/dimensions plus artifact identity and failed checks for downstream diagnosis.; Input alternatives: cad-solid; cad-assembly; parametric-source; constrained-sketch; fabrication-package; mesh; native-model-document

## Documented third-party tool and API entry points

1. Entrypoint: `colmap automatic_reconstructor --workspace_path W --image_path I --quality medium; inspect dense cloud/mesh; register scale controls; remodel in FreeCAD/OCS`; Status: existing_tool_entrypoint; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://github.com/alicevision/Meshroom/blob/develop/COPYING.md; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Notes: Documented application/API workflow. Human review steps remain manual; command/runtime not exercised in this research.

## Output artifacts

1. **Representations:** cad-solid; mesh
2. **Editable source:** Preserve input source and native CAD source where generated; neutral mesh/STEP does not retain upstream feature semantics.
3. **Preserves:** original inputs; declared units and datum; reviewed measurements/provenance
4. **Loss or inference:** occluded or hidden geometry requires explicit inference; representation conversion may discard feature history or unit metadata

## Checks

1. Object: photogrammetry/remodel; Quantity: camera reprojection, scale control and interface dimensions; Unit: pixels plus mm controls; Acceptance: registered controls agree within declared measurement uncertainty; Method: Inspect COLMAP reprojection/registered cameras and compare cloud/remodel to scale targets.

## Failure recovery

1. Failure: Scale, topology or registration mismatch; Recovery: Stop downstream export; preserve source; recheck units/datums and rerun only the affected stage.
2. Failure: Ambiguous hidden feature or weak evidence; Recovery: Mark as unresolved candidate; request a new measurement/view or retain parameter range.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Occluded surfaces and feature semantics require human remodeling.
5. **Setup reason:** Photogrammetry stack, camera workflow and CAD handoff.
6. **Compute reason:** Dense reconstruction is compute-heavy; GPU accelerates common dense-MVS routes; CPU/RAM/storage rise with images.

## Resources and scaling

1. **Cpu:** Dense reconstruction is compute-heavy; GPU accelerates common dense-MVS routes; CPU/RAM/storage rise with images.
2. **Gpu:** Selected reconstruction backend requirement.
3. **Ram:** Scales with image count/resolution, depth maps and dense points.
4. **Storage:** Preserve photographs, camera solution, dense workspace, mesh and CAD.
5. **Scaling drivers:** image count/resolution, depth maps and dense points
6. **Variants:** COLMAP dense acceleration follows its source requirements; explicit OpenMVS alternative bridge in REC-R01.

## Detailed branch procedures

1. [rec-r01.md](rec-r01.md)

Follow the linked branch procedure for the referenced input preparation and tool/API requirements. Apply the recorded units, frames and measurement checks before merging its outputs.

## Original sources

1. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
2. [https://github.com/alicevision/Meshroom/blob/develop/COPYING.md](https://github.com/alicevision/Meshroom/blob/develop/COPYING.md)
3. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)

Full source summaries: [source register](../../sources/source-register.md).
