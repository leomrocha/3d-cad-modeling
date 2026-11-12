# REC-R09 — RGB-D metric scan and CAD comparison

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 3/5; computing 2/5.**

Output: Calibrated depth point cloud/TSDF mesh registered to existing CAD with residual report.

## Comparison conditions

Depth sensor calibration, depth scale, frame poses and CAD revision/units available; CAD overlap with scan is sufficient.

## Registered starting artifact types

1. depth-frames
2. cad-solid
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: depth-frames; Format and quality: Synchronized RGB/depth sequences, sensor intrinsics, depth units and RGB-depth extrinsics.
2. Artifact: cad-solid; Format and quality: Existing CAD solid and exact revision with units/datums.
3. Artifact: measurement-set; Format and quality: Sensor/target controls, known CAD landmarks and independent dimensions.

## Reference points, datums and coordinate frames

Sensor depth scale provides metric input with calibration uncertainty. RGB-D odometry provides estimated poses. Open3D TSDF uses poses and intrinsics. Global cloud registration/ICP registers sampled surface to tessellated CAD; the CAD is a hypothesis and independent controls validate the transform.

## Software, libraries and dependencies

1. Name: Open3D; Licence scope: MIT; Role and api: RGBD odometry, ScalableTSDFVolume, registration_icp, evaluate_registration; Dependencies: Python open3d
2. Name: CloudCompare; Licence scope: GPL-2.0-or-later; Role and api: surface distances and inspection; Dependencies: CLI/GUI
3. Name: OCS; Licence scope: Existing local skill contract; Role and api: read CAD datum/units and comparison revision; Dependencies: OpenCADStudio

## Procedure

1. Step: 1; Action: Validate depth scale and extrinsics against measured target.
2. Step: 2; Action: Estimate/import pose trajectory and project depth into camera frame.
3. Step: 3; Action: Integrate TSDF with explicit voxel length and truncation.
4. Step: 4; Action: Register cloud/mesh against CAD with known init or feature matching then ICP.
5. Step: 5; Action: Report independent control and CAD surface distances; preserve input CAD.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-05; Name: Register RGB and depth frames and estimate sequence poses; Inputs: depth-frames; Outputs: camera-solution; point-cloud; Tools: Open3D RGB-D odometry; sensor SDK calibration; Open3D camera intrinsics/trajectory; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: Color/depth camera intrinsics; Depth scale and units; RGB-to-depth extrinsic transform; Pose convention recorded; Preserves: Raw color/depth frames; Sensor calibration and per-frame transforms; Changes or infers: Estimates frame-to-frame motion if poses are not provided; Depth samples are projected into camera coordinates; Checks: Known-depth/range baseline residuals; Frame registration residuals and loop closure; Check synchronized frames and depth/color alignment; Alternatives: Hardware SLAM trajectory; Surveyed poses; LiDAR/target registration; Automation: scripted; Evidence status: existing_report_registered; Summary: Associate color and depth in a shared camera model, then estimate or import frame poses for fusion. Sensor metric units do not remove calibration bias or trajectory drift.
2. Id: REC-06; Name: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Inputs: depth-frames; camera-solution; Outputs: point-cloud; mesh; Tools: Open3D ScalableTSDFVolume; Open3D RGBDImage; Open3D marching-cubes extraction; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: REC-05 calibration and pose trajectory; Depth units/range threshold; Voxel length and truncation distance chosen in stated units; Preserves: Raw depth frames and integration trajectory; Color data and TSDF settings; Changes or infers: Fuses samples into voxel representation and interpolated surface; Occluded regions remain unobserved or become algorithmically filled; Checks: Independent dimensions and loop-closure drift; Compare two voxel lengths against the same controls; Report registration and surface residual distributions; Alternatives: Point-cloud accumulation without TSDF; Sensor-native mesh; COLMAP/MVS surface from RGB; Automation: scripted; Evidence status: documented_capability; Summary: Fuse RGB-D into a scalable TSDF and extract a triangle mesh; voxel length controls discretization and noise response, not measured accuracy.
3. Id: REC-12; Name: Register existing CAD to calibrated photographs or scan points; Inputs: measurement-set; Outputs: camera-solution; measurement-set; Tools: CAD tessellation with named 3D landmarks; OpenCV solvePnPRansac; Open3D global registration and ICP; Source urls: https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html; https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Known CAD units, component datum and exact CAD revision; Visible identifiable CAD landmarks or scan geometry; Camera calibration for photo route; Preserves: Authoritative CAD revision and its units; Photo/scan source and registration transform; Changes or infers: Estimates CAD-to-camera/world transform; Surface registration uses a tessellated derivative of CAD; Checks: Independent landmark reprojection residuals; Scan-to-CAD distance map and interface dimensions; Check symmetries/partial overlap for alternate poses; Alternatives: Surveyed fiducials; Manual datum alignment; Photogrammetric camera solve with control targets; Automation: mixed; Evidence status: proposed_composition; Summary: Register a known CAD revision to measured photo landmarks or sampled scan geometry; the source CAD and scan/photo remain separate evidence.; Input choice groups: parametric-source; cad-solid; photo-set; point-cloud; mesh
4. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `Open3D registration_icp(source, target, max_correspondence_distance, init, estimation_method): provide source/target clouds in compatible units and a source-to-target initialization; inspect transformation, fitness and inlier_rmse.`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html

## Output artifacts

1. Representation: Calibrated depth point cloud/TSDF mesh registered to existing CAD with residual report.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Known-range sensor tests; trajectory loop closure; voxel sensitivity; source-to-target transform; ICP fitness/inlier RMSE; held-out CAD control residuals.

## Failure recovery

If depth holes or multipath appear, inspect range/reflectance and sensor operating range. If ICP converges to wrong symmetric pose, use CAD datums/targets. If TSDF smears, check trajectory drift and RGB-depth synchronization.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 3
3. **Compute:** 2
4. **Human reason:** Inputs already contain metric sensor depth and CAD; work centers on calibration/registration checks.
5. **Setup reason:** Open3D pipeline and sensor calibration data plus CAD import.
6. **Compute reason:** TSDF and ICP scale with number of frames/points and voxel length; CPU path is available.

## Resources and scaling

1. **Cpu:** Open3D odometry, TSDF, ICP and CAD checks have CPU routes.
2. **Gpu:** GPU optional by selected sensor/model backend.
3. **Ram:** Frame count, depth dimensions, voxel grid and point count.
4. **Storage:** Depth/color frames, pose trajectory, TSDF and registered derivatives.
5. **Scaling drivers:** Voxel length, integration bounds, frame count, depth range and CAD tessellation.
6. **Variants:** Comparison-only can use existing CAD tessellation; lower frame sampling reduces compute but may increase gaps.

## Original sources

1. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html)
2. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)
3. [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)
4. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
5. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
