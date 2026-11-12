# REC-R08 — Photogrammetry visual scene for downstream cameras

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 2/5; setup 4/5; computing 4/5.**

Output: Navigable Gaussian-splat scene with camera poses and original capture provenance; NeRF alternative tracked separately.

## Comparison conditions

Adequate overlapping image set and known camera poses or workable COLMAP solve; output goal is view synthesis and camera navigation, not dimensional CAD.

## Registered starting artifact types

1. photo-set

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format and quality: Overlapping JPEG/PNG image sequence with timestamps/camera metadata.
2. Artifact: camera-solution; Format and quality: COLMAP or supplied intrinsics and per-view poses; output coordinate convention retained.

## Reference points, datums and coordinate frames

Images and poses determine the learned scene coordinates; no metric scale without control. Splatfacto produces Gaussian representation/PLY. NeRF checkpoint is another separate representation. Geometry export route is model-specific and not implied by training.

## Software, libraries and dependencies

1. Name: COLMAP; Licence scope: BSD-3-Clause; Role and api: camera solve; Dependencies: CLI
2. Name: Nerfstudio Splatfacto/gsplat; Licence scope: Apache-2.0 per existing report; Role and api: ns-process-data, ns-train splatfacto, Gaussian PLY export; Dependencies: CUDA GPU
3. Name: Nerfstudio nerfacto; Licence scope: Apache-2.0 per existing report; Role and api: NeRF training/checkpoint; Dependencies: CLI and viewer

## Procedure

1. Step: 1; Action: Run COLMAP pose recovery or import the supplied camera solution and preserve image-to-camera mapping.
2. Step: 2; Action: Prepare the images with `ns-process-data images --data <images-folder> --output-dir <processed-data>`; Nerfstudio’s image pipeline uses COLMAP and requires FFmpeg.
3. Step: 3; Action: Train the Gaussian route with `ns-train splatfacto --data <processed-data>` and export its supported Gaussian PLY. The NeRF alternative uses `ns-train nerfacto --data <processed-data>` and keeps a separate checkpoint.
4. Step: 4; Action: Inspect held-out novel views and preserve the checkpoint, processed transforms and original photo set. Any mesh must come from a separate documented geometry extraction step.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-03; Name: Estimate camera poses and sparse structure from overlapping photos; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://alicevision.org/; https://github.com/openMVG/openMVG; Prerequisites: Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented; Preserves: Input images; Feature and match database, camera model, sparse reconstruction and settings; Changes or infers: Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor; Checks: Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection; Alternatives: OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available; Automation: mixed; Evidence status: existing_report_registered; Summary: Recover view geometry and camera poses from overlapping images; normalize all exported poses to a named frame and apply scale only from explicit evidence.
2. Id: REC-19; Name: Train and export a Gaussian splat scene; Inputs: photo-set; camera-solution; Outputs: gaussian-scene; Tools: Nerfstudio Splatfacto / gsplat; Gaussian PLY export; Source urls: https://docs.nerf.studio/nerfology/methods/splat.html; Prerequisites: Camera poses and image transforms; GPU sized for the selected scene/model; Nerfstudio version and export command recorded; Preserves: Images, poses, configuration, checkpoint and Gaussian PLY; Changes or infers: Fits view-dependent Gaussian representation from capture images; Does not produce analytic CAD surfaces; Checks: Novel-view coverage and held-out render comparison; Pose/image consistency; Keep dimensional claims tied to independent controls; Alternatives: REC-20 NeRF scene; Automation: scripted; Evidence status: documented_capability; Summary: Train one Gaussian scene and export its supported Gaussian representation. Current Splatfacto docs support Gaussian PLY; they state mesh/point-cloud export is unsupported.

## Documented third-party tool and API entry points

1. Path: Nerfstudio CLI (native tool entrypoint; no project script); Status: existing_tool_entrypoint; Entrypoint: `ns-process-data images --data <images-folder> --output-dir <processed-data> && ns-train splatfacto --data <processed-data> ; use ns-train nerfacto --data <processed-data> for the separate NeRF branch.`; Source urls: https://docs.nerf.studio/quickstart/custom_dataset.html; https://docs.nerf.studio/nerfology/methods/splat.html

## Output artifacts

1. Representation: Navigable Gaussian-splat scene with camera poses and original capture provenance; NeRF alternative tracked separately.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: No new CAD in this workflow.

## Checks

Image-to-camera association; training convergence/held-out views; scene coverage; saved pose transforms; dimension claims tested only with independent controls.

## Failure recovery

If camera solve fragments, capture more overlap or resolve moving objects/lens model. If novel views ghost, check pose and exposure consistency. For mesh, use separately checked MVS/TSDF workflow and model-specific extraction support.

## Effort and computing classification

1. **Human:** 2
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Good capture and a visual-only goal leave little semantic interpretation.
5. **Setup reason:** GPU model environment and Nerfstudio processing/training CLI.
6. **Compute reason:** Splatfacto documented memory approx. 6 GB default / 12 GB big; scaling with views, resolution and scene complexity.

## Resources and scaling

1. **Cpu:** COLMAP camera solve runs on CPU; Nerfstudio handles scene training.
2. **Gpu:** Source report: Splatfacto ~6 GB GPU memory default and ~12 GB big; confirm variant docs.
3. **Ram:** Depends on image resolution/count and representation; no universal RAM floor.
4. **Storage:** Store images, training checkpoint, Gaussian PLY and renders.
5. **Scaling drivers:** Capture count/resolution, scene coverage and model variant.
6. **Variants:** NeRF and Gaussian are separate outputs; omit geometry extraction for visual delivery.

## Original sources

1. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
2. [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/custom_dataset.md)
3. [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)
4. [https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md)
5. [https://docs.nerf.studio/quickstart/custom_dataset.html](https://docs.nerf.studio/quickstart/custom_dataset.html)
6. [https://docs.nerf.studio/quickstart/installation.html](https://docs.nerf.studio/quickstart/installation.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
