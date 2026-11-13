# REC-R02 — Video and RGB-D to registered metric scene

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 3/5.**

Output: Registered RGB photo-derived cloud and sensor-depth cloud, fused depth mesh and a checked source-to-target transform.

## Comparison conditions

Video frames overlap with RGB-D capture or share enough geometry; depth calibration, RGB-depth extrinsics and sensor units are known; motion/rolling-shutter errors are controlled.

## Registered starting artifact types

1. video
2. depth-frames
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: video; Format and quality: Original video with timestamps and camera metadata; sufficient parallax and sharp frames.
2. Artifact: depth-frames; Format and quality: RGB/depth frames and camera intrinsics/extrinsics; raw depth scale/range stated.
3. Artifact: measurement-set; Format and quality: Independent control distances/targets and frame coordinates; withheld controls retained.

## Reference points, datums and coordinate frames

Depth sensor calibration provides per-frame camera intrinsics, depth scale and RGB-depth extrinsics. COLMAP estimates RGB camera poses; depth odometry or sensor trajectory estimates range poses. FPFH/RANSAC establishes a coarse transform between distinct source/target clouds; ICP refines only with same-scale clouds and a good initial transform. Withheld dimensions test drift.

## Software, libraries and dependencies

1. Name: FFmpeg; Licence scope: LGPL/GPL build-dependent; Role and api: ffmpeg frame extraction; Dependencies: FFmpeg CLI
2. Name: COLMAP; Licence scope: BSD-3-Clause; Role and api: SfM CLI/pycolmap; Dependencies: Photo set
3. Name: Open3D; Licence scope: MIT; Role and api: RGB-D odometry, global registration, registration_icp, TSDF integration; Dependencies: Python open3d + calibrated frames
4. Name: CloudCompare; Licence scope: GPL-2.0-or-later; Role and api: CLI cloud processing / distance map; Dependencies: CloudCompare executable

## Procedure

1. Step: 1; Action: Extract selected frames preserving source timestamps and frame indices.
2. Step: 2; Action: Estimate RGB camera poses/cloud with COLMAP; estimate depth trajectory/cloud from calibrated frames or sensor SLAM.
3. Step: 3; Action: Use global registration for coarse alignment if needed, followed by Open3D registration_icp using explicit initial 4x4 and model-unit threshold.
4. Step: 4; Action: Integrate depth frames through TSDF with calibrated trajectory; compare loop closure and independent controls.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-04; Name: Convert video into an image reconstruction dataset; Inputs: video; Outputs: photo-set; Tools: ffmpeg frame extraction; blur/duplicate-frame filtering; COLMAP or Meshroom downstream; Source urls: https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md; https://github.com/nerfstudio-project/nerfstudio; Prerequisites: Video stream has sufficient viewpoint change; Timestamps and frame rate retained; Avoid excessive adjacent near-duplicate frames; Preserves: Original video; Frame index and presentation timestamp for every extracted image; Changes or infers: Selects a frame subset; frame selection can omit views or moving events; Checks: Frame sharpness and coverage by viewing direction; Image timestamp monotonicity; Motion/rolling-shutter and exposure consistency; Alternatives: DA3-Streaming directly on long image sequences; RGB-D video route through REC-05; Automation: assisted; Evidence status: proposed_composition; Summary: Create a controlled photo-set from video while retaining original timeline provenance; selected frame sampling is an input transformation that affects camera coverage.
2. Id: REC-03; Name: Estimate camera poses and sparse structure from overlapping photos; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://alicevision.org/; https://github.com/openMVG/openMVG; Prerequisites: Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented; Preserves: Input images; Feature and match database, camera model, sparse reconstruction and settings; Changes or infers: Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor; Checks: Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection; Alternatives: OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available; Automation: mixed; Evidence status: existing_report_registered; Summary: Recover view geometry and camera poses from overlapping images; normalize all exported poses to a named frame and apply scale only from explicit evidence.
3. Id: REC-05; Name: Register RGB and depth frames and estimate sequence poses; Inputs: depth-frames; Outputs: camera-solution; point-cloud; Tools: Open3D RGB-D odometry; sensor SDK calibration; Open3D camera intrinsics/trajectory; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html; https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: Color/depth camera intrinsics; Depth scale and units; RGB-to-depth extrinsic transform; Pose convention recorded; Preserves: Raw color/depth frames; Sensor calibration and per-frame transforms; Changes or infers: Estimates frame-to-frame motion if poses are not provided; Depth samples are projected into camera coordinates; Checks: Known-depth/range baseline residuals; Frame registration residuals and loop closure; Check synchronized frames and depth/color alignment; Alternatives: Hardware SLAM trajectory; Surveyed poses; LiDAR/target registration; Automation: scripted; Evidence status: existing_report_registered; Summary: Associate color and depth in a shared camera model, then estimate or import frame poses for fusion. Sensor metric units do not remove calibration bias or trajectory drift.
4. Id: REC-07; Name: Estimate coarse transform between point clouds; Inputs: point-cloud; Input roles: Role: source cloud; Type: point-cloud; Role: target cloud; Type: point-cloud; Outputs: measurement-set; Tools: Open3D FPFH; Open3D RANSAC global registration; CloudCompare alignment; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; Prerequisites: Same scale or explicitly estimated Sim(3) scale; Overlap with geometric features; Point coordinates and units documented; Preserves: Both original clouds; Source/target identities; Changes or infers: Estimates rigid or chosen similarity transform and correspondences; Checks: RANSAC inlier set and correspondence checks; Fitness/inlier RMSE after transform; Control targets withheld from fitting; Alternatives: Known targets/PnP; Manual three-point initialization; Feature registration from CAD datums; Automation: scripted; Evidence status: documented_capability; Summary: Find a coarse point-cloud alignment from local features, then pass the transform and inliers to refinement; feature ambiguity and symmetry can produce a plausible wrong pose.
5. Id: REC-08; Name: Refine registration and compare point-cloud surfaces; Inputs: measurement-set; point-cloud; Input roles: Role: source cloud; Type: point-cloud; Role: target cloud; Type: point-cloud; Outputs: measurement-set; Tools: Open3D point-to-plane ICP; Open3D evaluate_registration; CloudCompare cloud-to-cloud distance; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Coarse transform; Overlap and consistent units; ICP threshold selected from expected sampling/noise scale; Preserves: Source clouds and original transforms; Correspondence threshold and final transform; Changes or infers: Refines transform to minimize selected correspondence objective; Distance map depends on chosen correspondence and sampling rule; Checks: Fitness and inlier RMSE with units; Independent control residuals; Inspect residual map and non-overlap separately; Alternatives: Robust kernels; Multiway pose graph registration; Target-based transformation; Automation: scripted; Evidence status: documented_capability; Summary: Refine an initialized transform and compute cloud distances; optimizer residual and overlap metrics describe fit to participating points, not absolute truth.
6. Id: REC-06; Name: Integrate calibrated RGB-D frames into point cloud or TSDF mesh; Inputs: depth-frames; camera-solution; Outputs: point-cloud; mesh; Tools: Open3D ScalableTSDFVolume; Open3D RGBDImage; Open3D marching-cubes extraction; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html; Prerequisites: REC-05 calibration and pose trajectory; Depth units/range threshold; Voxel length and truncation distance chosen in stated units; Preserves: Raw depth frames and integration trajectory; Color data and TSDF settings; Changes or infers: Fuses samples into voxel representation and interpolated surface; Occluded regions remain unobserved or become algorithmically filled; Checks: Independent dimensions and loop-closure drift; Compare two voxel lengths against the same controls; Report registration and surface residual distributions; Alternatives: Point-cloud accumulation without TSDF; Sensor-native mesh; COLMAP/MVS surface from RGB; Automation: scripted; Evidence status: documented_capability; Summary: Fuse RGB-D into a scalable TSDF and extract a triangle mesh; voxel length controls discretization and noise response, not measured accuracy.

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `Open3D registration_icp(source, target, max_correspondence_distance, init, estimation_method): provide source/target clouds in compatible units and a source-to-target initialization; inspect transformation, fitness and inlier_rmse.`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html

## Output artifacts

1. Representation: Registered RGB photo-derived cloud and sensor-depth cloud, fused depth mesh and a checked source-to-target transform.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: No new CAD in this workflow.

## Checks

Timestamp and sharpness coverage; RGB/depth alignment; source-to-target transform direction; ICP fitness/inlier RMSE; loop closure; held-out range controls; TSDF mesh-to-point-cloud residuals.

## Failure recovery

If visual odometry drifts, add loop closure/targets or use sensor SLAM; if ICP fails, check units, initial transform, overlap and symmetry. Do not change threshold to hide a systematic residual. If RGB/depth edges disagree, check synchronization and extrinsics.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 3
4. **Human reason:** Combines two sensing paths and frame alignment, but stops at a registered metric scene.
5. **Setup reason:** Requires video extraction, sensor calibration and reconstruction/registration tools.
6. **Compute reason:** Dense cloud registration and TSDF integrate many samples; compute scales with frame count, image dimensions and voxel density.

## Resources and scaling

1. **Cpu:** Frame extraction, Open3D ICP and TSDF have CPU paths.
2. **Gpu:** GPU use depends on selected SfM/SLAM backend; no requirement for core Open3D example.
3. **Ram:** RAM scales with frame count, point count and voxel volume.
4. **Storage:** Original video, extracted frames, depth, cloud and mesh storage scale with duration/resolution.
5. **Scaling drivers:** Frame count/resolution, point density, TSDF voxel length and cloud overlap.
6. **Variants:** RGB-D-only route removes photo SfM comparison; photo-only route loses sensor depth metric input.

## Original sources

1. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_odometry.html)
2. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
3. [https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html)
4. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
5. [https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html)
6. [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md)
7. [https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode)

Full source summaries: [source register](../../sources/source-register.md).
