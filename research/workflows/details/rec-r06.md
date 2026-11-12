# REC-R06 — Gaussian context, independent mesh and CAD remodel

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 4/5; setup 4/5; computing 4/5.**

Output: Gaussian PLY context, independently generated MVS mesh/cloud and editable CAD aligned to source evidence.

## Comparison conditions

Overlapping photos, camera solution, independent control points; MVS mesh and measured dimensions available for selected CAD features.

## Registered starting artifact types

1. photo-set
2. measurement-set

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format and quality: Static, overlapping multi-view photographs.
2. Artifact: measurement-set; Format and quality: Control lengths/points and dimensions with units and withheld checks.

## Reference points, datums and coordinate frames

Gaussian scene is a view-synthesis representation. REC-17 MVS creates a separate mesh/cloud from photos and camera poses. Controls define scale/checks. CAD features are rebuilt from measurements and explicit interpretation; splat geometry is not assumed to be an analytic surface.

## Software, libraries and dependencies

1. Name: Nerfstudio Splatfacto; Licence scope: Apache-2.0 per existing report; Role and api: Gaussian PLY training/export; Dependencies: CUDA GPU
2. Name: COLMAP + OpenMVS; Licence scope: BSD-3-Clause + AGPL-3.0 OpenMVS; Role and api: sparse solve then DensifyPointCloud/ReconstructMesh; Dependencies: CLIs
3. Name: Open3D; Licence scope: MIT; Role and api: cloud registration/distance metrics; Dependencies: Python
4. Name: OCS; Licence scope: Existing local skill contract; Role and api: parametric remodeling; Dependencies: OpenCADStudio session

## Procedure

1. Step: 1; Action: Estimate camera poses using COLMAP.
2. Step: 2; Action: Train and export Gaussian PLY from Splatfacto for appearance context.
3. Step: 3; Action: Generate dense point cloud and mesh independently using OpenMVS; use measured controls for scale.
4. Step: 4; Action: Remodel selected features in OCS from the dense surface and dimensions; preserve separate splat, mesh, CAD layers.
5. Step: 5; Action: Compare CAD with source cloud and withheld dimensions.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-03; Name: Estimate camera poses and sparse structure from overlapping photos; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://alicevision.org/; https://github.com/openMVG/openMVG; Prerequisites: Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented; Preserves: Input images; Feature and match database, camera model, sparse reconstruction and settings; Changes or infers: Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor; Checks: Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection; Alternatives: OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available; Automation: mixed; Evidence status: existing_report_registered; Summary: Recover view geometry and camera poses from overlapping images; normalize all exported poses to a named frame and apply scale only from explicit evidence.
2. Id: REC-19; Name: Train and export a Gaussian splat scene; Inputs: photo-set; camera-solution; Outputs: gaussian-scene; Tools: Nerfstudio Splatfacto / gsplat; Gaussian PLY export; Source urls: https://docs.nerf.studio/nerfology/methods/splat.html; Prerequisites: Camera poses and image transforms; GPU sized for the selected scene/model; Nerfstudio version and export command recorded; Preserves: Images, poses, configuration, checkpoint and Gaussian PLY; Changes or infers: Fits view-dependent Gaussian representation from capture images; Does not produce analytic CAD surfaces; Checks: Novel-view coverage and held-out render comparison; Pose/image consistency; Keep dimensional claims tied to independent controls; Alternatives: REC-20 NeRF scene; Automation: scripted; Evidence status: documented_capability; Summary: Train one Gaussian scene and export its supported Gaussian representation. Current Splatfacto docs support Gaussian PLY; they state mesh/point-cloud export is unsupported.
3. Id: REC-17; Name: Build dense point cloud and mesh from SfM camera solution; Inputs: photo-set; camera-solution; Outputs: point-cloud; mesh; Tools: OpenMVS DensifyPointCloud; OpenMVS ReconstructMesh; COLMAP dense workspace; Source urls: https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/; https://github.com/colmap/colmap/blob/main/doc/cli.rst; Prerequisites: REC-03 sparse camera solution or equivalent calibrated poses; Overlap, exposure and scene masks retained; Scale supplied by control or metric camera data for dimensional use; Preserves: Sparse scene, images, camera poses and dense reconstruction settings; Changes or infers: Estimates dense visible surface and interpolated mesh; Unseen and occluded surfaces are not recovered from images; Checks: Image reprojection and dense coverage; Withheld control lengths and independent cloud residuals; Compare mesh-to-cloud distances and disconnected components; Alternatives: Open3D TSDF from calibrated RGB-D; Nerfstudio geometry extraction only where model support is established; Automation: scripted; Evidence status: existing_report_registered; Summary: Run dense multi-view stereo after sparse camera recovery. Dense geometry inherits the camera scale and pose errors; triangulation does not itself create metric evidence.
4. Id: REC-14; Name: Remodel segmented scan evidence as parametric CAD; Inputs: measurement-set; Input alternatives: point-cloud; mesh; Outputs: constrained-sketch; parametric-source; cad-solid; Tools: Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated; Preserves: Raw scan, segmentation indices and fit report; Dimension provenance for every feature; Changes or infers: Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions; Checks: OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls; Alternatives: Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation; Automation: mixed; Evidence status: proposed_composition; Summary: Use fitted scan geometry as evidence and reconstruct an editable feature history through the existing OCS workflow; fitted parameters must remain traceable and not silently become author dimensions.
5. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Code and tool entry points

1. Path: [register_clouds.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/register_clouds.py); Status: reference_code; Entrypoint: `python register_clouds.py --source source.ply --target target.ply --initial-transform init.json --max-correspondence-distance <value-in-model-units> --unit <unit> --output-report result.json --output-source-ply registered_source.ply`; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html

## Output artifacts

1. Representation: Gaussian PLY context, independently generated MVS mesh/cloud and editable CAD aligned to source evidence.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Novel view rendering; MVS coverage/mesh completeness; control residuals; source-to-CAD distances; CAD feature dimensions; representation transform consistency.

## Failure recovery

If Splatfacto mesh extraction is requested, its current FAQ says unsupported; use separate MVS or calibrated depth TSDF. If MVS incomplete, improve photos or add sensor depth. If CAD fit to scan deforms beyond controls, revise alignment/feature assumptions.

## Effort and computing classification

1. **Human:** 4
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Requires managing three representations and remodeling semantic features.
5. **Setup reason:** Three software stacks including GPU scene training and OCS modeling.
6. **Compute reason:** Dense stereo plus Gaussian training and CAD comparison; image count/resolution/cloud density drive memory and compute.

## Resources and scaling

1. **Cpu:** COLMAP/OpenMVS and cloud comparison are CPU-capable.
2. **Gpu:** Splatfacto uses CUDA GPU; source report lists ~6 GB default and ~12 GB big. MVS acceleration varies by build.
3. **Ram:** Dense MVS plus Gaussian training can raise memory; no universal system-RAM floor.
4. **Storage:** Store original photos, dense maps, mesh, checkpoint, Gaussian PLY and CAD.
5. **Scaling drivers:** Image resolution/count, scene complexity, MVS depth density and mesh size.
6. **Variants:** Omit scene training for a lower-cost mesh-to-CAD path; omit CAD for visual-only deliverable.

## Original sources

1. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
2. [https://docs.nerf.studio/nerfology/methods/splat.html](https://docs.nerf.studio/nerfology/methods/splat.html)
3. [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/)
4. [https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html)
5. [/home/leo/.codex/skills/ocs-engineering/SKILL.md](/home/leo/.codex/skills/ocs-engineering/SKILL.md)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
