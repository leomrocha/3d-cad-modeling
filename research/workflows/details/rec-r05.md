# REC-R05 — Photos, learned depth and view-synthesis comparison

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 4/5; computing 4/5.**

Output: Separate SfM and DA3 camera/depth/cloud estimates plus Gaussian view-synthesis scene and control residual comparison.

## Comparison conditions

Multi-view photos with overlap; independent dimensions/targets; selected DA3 and Splatfacto variants and model terms reviewed; same photo set used for comparisons.

## Registered starting artifact types

1. photo-set
2. measurement-set

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format and quality: Original overlapping JPEG/PNG photos with camera metadata and static scene.
2. Artifact: measurement-set; Format and quality: Measured control lengths/points with fit versus withheld labels.

## Reference points, datums and coordinate frames

DA3 depth/pose is a model estimate and can provide metric variant but requires physical controls. COLMAP scale remains arbitrary absent controls. Splat scene optimizes novel-view appearance; it is not a mesh. Similarity alignment for comparing cloud estimates must be reported separately from metric controls.

## Software, libraries and dependencies

1. Name: COLMAP; Licence scope: BSD-3-Clause; Role and api: SfM camera/cloud reconstruction; Dependencies: CLI/pycolmap
2. Name: Depth Anything 3; Licence scope: Apache-2.0 per existing report; Role and api: multi-view prediction, metric depth/pose/cloud outputs; Dependencies: Model weights/environment
3. Name: Nerfstudio Splatfacto/gsplat; Licence scope: Apache-2.0 per existing report; Role and api: train and export Gaussian PLY; Dependencies: CUDA GPU; selected version

## Procedure

1. Step: 1; Action: Run COLMAP sparse reconstruction and preserve component/camera metadata.
2. Step: 2; Action: Run DA3 multi-view or streaming inference; preserve metric/relative model name, confidence, poses and output formats.
3. Step: 3; Action: Train Gaussian view-synthesis scene from photos and known/estimated camera solution.
4. Step: 4; Action: Register estimate clouds with controls; compare withheld lengths, regional residuals and pose consistency.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-03; Name: Estimate camera poses and sparse structure from overlapping photos; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://alicevision.org/; https://github.com/openMVG/openMVG; Prerequisites: Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented; Preserves: Input images; Feature and match database, camera model, sparse reconstruction and settings; Changes or infers: Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor; Checks: Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection; Alternatives: OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available; Automation: mixed; Evidence status: existing_report_registered; Summary: Recover view geometry and camera poses from overlapping images; normalize all exported poses to a named frame and apply scale only from explicit evidence.
2. Id: REC-10; Name: Estimate multi-view depth, camera poses and Gaussian outputs; Inputs: ; Input alternatives: photo-set; video; Outputs: camera-solution; point-cloud; Tools: Depth Anything 3; DA3-Streaming; DA3 Blender add-on; Source urls: https://github.com/ByteDance-Seed/Depth-Anything-3; https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md; https://github.com/xy-gao/DA3-blender; Prerequisites: Appropriate model variant/weights and GPU memory; Camera/image batch and scale metadata; DA3 Blender add-on currently has no LICENSE file at inspected upstream path; Preserves: Input images/video and timestamps; Prediction confidence, camera poses/intrinsics and model revision; Changes or infers: Network predicts depth/rays/poses and may estimate metric-scale depth; Splat and mesh outputs from learned model are generated estimates; Checks: Compare metric depth to independent measured controls; Inspect confidence and cross-view consistency; Compare camera poses to COLMAP/targets; Record output model representation exactly; Alternatives: COLMAP+MVS; Open3D RGB-D with sensor depth; Nerfstudio Splatfacto; Automation: mixed; Evidence status: existing_report_registered; Summary: Use DA3 for learned depth/pose/geometry and optional splats; its metric series remains an estimate that requires controls for dimensional claims.
3. Id: REC-19; Name: Train and export a Gaussian splat scene; Inputs: photo-set; camera-solution; Outputs: gaussian-scene; Tools: Nerfstudio Splatfacto / gsplat; Gaussian PLY export; Source urls: https://docs.nerf.studio/nerfology/methods/splat.html; Prerequisites: Camera poses and image transforms; GPU sized for the selected scene/model; Nerfstudio version and export command recorded; Preserves: Images, poses, configuration, checkpoint and Gaussian PLY; Changes or infers: Fits view-dependent Gaussian representation from capture images; Does not produce analytic CAD surfaces; Checks: Novel-view coverage and held-out render comparison; Pose/image consistency; Keep dimensional claims tied to independent controls; Alternatives: REC-20 NeRF scene; Automation: scripted; Evidence status: documented_capability; Summary: Train one Gaussian scene and export its supported Gaussian representation. Current Splatfacto docs support Gaussian PLY; they state mesh/point-cloud export is unsupported.
4. Id: REC-08; Name: Refine registration and compare point-cloud surfaces; Inputs: measurement-set; point-cloud; Input roles: Role: source cloud; Type: point-cloud; Role: target cloud; Type: point-cloud; Outputs: measurement-set; Tools: Open3D point-to-plane ICP; Open3D evaluate_registration; CloudCompare cloud-to-cloud distance; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Coarse transform; Overlap and consistent units; ICP threshold selected from expected sampling/noise scale; Preserves: Source clouds and original transforms; Correspondence threshold and final transform; Changes or infers: Refines transform to minimize selected correspondence objective; Distance map depends on chosen correspondence and sampling rule; Checks: Fitness and inlier RMSE with units; Independent control residuals; Inspect residual map and non-overlap separately; Alternatives: Robust kernels; Multiway pose graph registration; Target-based transformation; Automation: scripted; Evidence status: documented_capability; Summary: Refine an initialized transform and compute cloud distances; optimizer residual and overlap metrics describe fit to participating points, not absolute truth.

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `Open3D registration_icp(source, target, max_correspondence_distance, init, estimation_method): provide source/target clouds in compatible units and a source-to-target initialization; inspect transformation, fitness and inlier_rmse.`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html

## Output artifacts

1. Representation: Separate SfM and DA3 camera/depth/cloud estimates plus Gaussian view-synthesis scene and control residual comparison.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: No new CAD in this workflow.

## Checks

Compare DA3 metric depth against independent control points; COLMAP reprojection errors; inter-estimate transform; regional cloud residuals; novel-view coverage separately from surface quality.

## Failure recovery

If DA3 and SfM disagree, check camera metadata, moving objects, lens distortion and scale/control definition. Report two estimates separately; do not average without a stated statistical model. If splat render artifacts occur, revise capture coverage; do not substitute splat appearance for dimensional evidence.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Reviewing multiple model outputs and allocating controls requires engineering judgment.
5. **Setup reason:** Combines reconstruction, learned model and CUDA scene training.
6. **Compute reason:** DA3 streaming reports <12 GB GPU memory; Splatfacto docs list ~6 GB default and ~12 GB big; runtime scales with views/resolution.

## Resources and scaling

1. **Cpu:** Image preparation and sparse SfM use CPU.
2. **Gpu:** DA3 Streaming reports below 12 GB memory; Nerfstudio lists about 6 GB for default Splatfacto and 12 GB for Splatfacto-big in source report.
3. **Ram:** Model and reconstruction data scale with view count/resolution; no universal system-RAM minimum.
4. **Storage:** Images, checkpoints and output clouds/splats.
5. **Scaling drivers:** Image resolution/count, chosen DA3 variant, Gaussian scene complexity.
6. **Variants:** Omit Gaussian branch for lower compute; omit DA3 branch to compare conventional SfM alone.

## Original sources

1. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
2. [https://github.com/ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)
3. [https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md)
4. [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)
5. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
