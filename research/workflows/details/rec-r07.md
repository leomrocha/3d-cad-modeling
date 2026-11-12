# REC-R07 — 3D-anchored sketch and CAD edit comparison

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 1/5.**

Output: Calculated screen-stroke anchors, interpreted constrained CAD feature and revision-bound comparison report.

## Comparison conditions

Existing calibrated camera solution and mesh/CAD target; screen strokes belong to the image associated with that camera; user supplies feature interpretation and dimensions.

## Registered starting artifact types

1. raster-sketch
2. camera-solution
3. mesh
4. measurement-set

## Detailed source and preparation artifacts

1. Artifact: raster-sketch; Format and quality: Image plus pixel-space strokes in a documented image coordinate system.
2. Artifact: camera-solution; Format and quality: Intrinsics/distortion and camera pose tied to exact view and coordinate frame.
3. Artifact: mesh; Format and quality: Selected raycast surface with transform and revision.
4. Artifact: measurement-set; Format and quality: Physical dimensions/datum controls and explicit intended feature interpretation.

## Reference points, datums and coordinate frames

Pixels map to normalized camera rays with K/distortion inverse, transformed into world by camera pose; ray intersection yields calculated 3D anchors against selected mesh. The mesh and camera are reference evidence. Anchors carry the uncertainty of calibration, pose, mesh and hit selection; they are not independent measurements. Independent dimension controls check CAD.

## Software, libraries and dependencies

1. Name: Blender Python API; Licence scope: GPL-2.0-or-later; Role and api: camera ray projection and Scene.ray_cast; Dependencies: Blender bpy; signature version checked at implementation
2. Name: OpenCV; Licence scope: Apache-2.0 for OpenCV >=4.5 (including current 4.x); older releases retain their release-specific BSD-3-Clause terms; Role and api: projectPoints/PnP for pose calibration or reprojection; Dependencies: Python cv2
3. Name: OCS; Licence scope: Existing local skill contract; Role and api: constrained sketch and feature modeling; Dependencies: OpenCADStudio session

## Procedure

1. Step: 1; Action: Map stroke pixels through image calibration to camera rays; record camera, hit object and face/triangle IDs.
2. Step: 2; Action: Store ray-hit anchors and projection residual context in measurement-set as calculated anchors.
3. Step: 3; Action: Ask for/consume explicit sketch interpretation: surface curve, projected profile or datum-plane sketch; apply dimensions/constraints in OCS.
4. Step: 4; Action: Read back CAD revision and compare with same mesh and independent controls.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-13; Name: Anchor a screen sketch to a 3D surface; Inputs: raster-sketch; camera-solution; Input alternatives: mesh; cad-solid; Outputs: measurement-set; Tools: Blender Scene.ray_cast; screen-to-camera ray projection; OpenCV projectPoints; OCS constrained sketch; Source urls: https://docs.blender.org/api/current/bpy.types.Scene.html; https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html; Prerequisites: Active camera intrinsics and world transform; Named/selected hit surface and units; Semantic meaning chosen: trace, projected curve or planar sketch; Preserves: Original image/stroke; Camera, hit object/component and hit primitive identifier; Changes or infers: Maps pixel strokes to surface hits; occlusion and target surface define anchors; Curve fitting/simplification changes stroke geometry; Checks: Reproject world anchors into source view; Report missed/ambiguous rays and anchor residual; Verify resulting OCS sketch plane and constraints; Alternatives: Annotate a known orthographic view; Click measured fiducials and use PnP; Draw on a CAD datum plane; Automation: mixed; Evidence status: proposed_composition; Summary: Convert 2D screen strokes into calculated 3D surface anchors using the camera solution and selected hit geometry. Preserve calibration and reconstruction evidence; anchors are not independently measured physical dimensions. A separate interpretation step must define sketch plane, constraints and feature meaning.
2. Id: REC-14; Name: Remodel segmented scan evidence as parametric CAD; Inputs: measurement-set; Input alternatives: point-cloud; mesh; Outputs: constrained-sketch; parametric-source; cad-solid; Tools: Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated; Preserves: Raw scan, segmentation indices and fit report; Dimension provenance for every feature; Changes or infers: Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions; Checks: OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls; Alternatives: Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation; Automation: mixed; Evidence status: proposed_composition; Summary: Use fitted scan geometry as evidence and reconstruct an editable feature history through the existing OCS workflow; fitted parameters must remain traceable and not silently become author dimensions.
3. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Code and tool entry points

1. Path: Blender Python Console (native bpy API; no project script); Status: existing_tool_entrypoint; Entrypoint: `depsgraph = bpy.context.evaluated_depsgraph_get(); hit, location, normal, face_index, obj, matrix = bpy.context.scene.ray_cast(depsgraph, origin, direction); origin/direction are world-space rays computed from the calibrated camera and stroke pixel.`; Source urls: https://docs.blender.org/api/current/bpy.types.Scene.html; [SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

## Output artifacts

1. Representation: Calculated screen-stroke anchors, interpreted constrained CAD feature and revision-bound comparison report.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Reproject calculated anchors into original image; flag missed/occluded rays; check camera calibration/view identity; inspect hit distribution; verify OCS constraints and independent physical dimensions.

## Failure recovery

For ambiguous rays, require selected target surface or user selection; preserve multiple hit candidates. For sketch-plane ambiguity, stop at anchors until interpreted. If visible mesh is poorly reconstructed, do not convert anchor hits into physical dimensions.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 1
4. **Human reason:** Small annotation can be quick, while selecting intended CAD meaning needs a human decision.
5. **Setup reason:** Camera projection, raycast adapter and OCS session.
6. **Compute reason:** Raycasting a small stroke set and CAD checks are CPU-light; high-resolution source mesh increases cost.

## Resources and scaling

1. **Cpu:** Ray projection, mesh ray-cast and CAD edits are CPU operations.
2. **Gpu:** No GPU requirement for listed operations.
3. **Ram:** Mesh size and CAD session geometry determine memory.
4. **Storage:** Stroke/image anchors, mesh, CAD revision and reports.
5. **Scaling drivers:** Stroke count, mesh triangle count, CAD feature count.
6. **Variants:** Anchor-only output has low effort; interpreted constrained CAD needs semantic decisions and dimensions.

## Original sources

1. [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)
2. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
