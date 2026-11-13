# REC-R01 — Calibrated photos and controls to editable CAD

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 5/5; setup 4/5; computing 4/5.**

Output: Metric-anchored camera solution, dense surface reference and constrained CAD interpretation.

## Comparison conditions

Multi-view photos with adequate overlap and stable exposure; at least ten diverse calibration-target views if using the OpenCV calibration route; explicit scale/control measurements; dense MVS and selected OCS feature modeling.

## Registered starting artifact types

1. photo-set
2. measurement-set

## Detailed source and preparation artifacts

1. Artifact: photo-set; Format and quality: JPG/PNG originals with camera metadata; sharp overlapping views and visible calibration board in calibration subset.
2. Artifact: measurement-set; Format and quality: JSON/CSV target dimensions and 3D control coordinates with units, plus named image-pixel correspondences or board measurements.
3. Artifact: model-brief; Format and quality: Text naming components, datums and intended CAD feature scope; it supplies semantics, not dimensions.

## Reference points, datums and coordinate frames

Board corners: object coordinates in target frame and pixel detections. Calibration target establishes intrinsics and target-frame units; camera calibration alone does not scale the object capture. At least two separated measured scale/control distances are used to set/check reconstruction scale; reserve one or more controls from fitting. COLMAP adapter detail: OpenCV pixel-center principal point is shifted +0.5 px in x and y for COLMAP; OpenCV’s five coefficients [k1,k2,p1,p2,k3] map into COLMAP FULL_OPENCV [k1,k2,p1,p2,k3,k4,k5,k6] with the final three set to zero. Verify COLMAP camera database readback after feature extraction. COLMAP bundle adjustment refines parameters by default unless controlled; choose this based on calibration evidence.

## Software, libraries and dependencies

1. Name: OpenCV; Licence scope: Apache-2.0 for OpenCV >=4.5 (including current 4.x); older releases retain their release-specific BSD-3-Clause terms; Role and api: calibrateCamera, projectPoints; Dependencies: Python cv2 + NumPy
2. Name: COLMAP / pycolmap; Licence scope: BSD-3-Clause; Role and api: feature extraction, matching, mapper; CLI or pycolmap; Dependencies: COLMAP environment
3. Name: OpenMVS; Licence scope: AGPL-3.0; Role and api: DensifyPointCloud, ReconstructMesh; Dependencies: OpenMVG exported scene / MVS executables
4. Name: OCS; Licence scope: Existing local skill contract; Role and api: Existing OCS session controls and constrained CAD readback; Dependencies: OpenCADStudio session + OCS Engineering skill
5. Name: AliceVision Meshroom alternate; Licence scope: MPL-2.0 per upstream repository; Role and api: meshroom_batch --input <image-folder> --output <output-folder> invokes the documented photogrammetry pipeline; `--save <project.mg>` persists the graph. This route manages its own graph and calibration; it does not consume the OpenCV calibration JSON adapter above.; Dependencies: Meshroom/AliceVision bundled executable and pipeline resources; NVIDIA CUDA recommended for full reconstruction per official release notes.

## Procedure

1. Step: 1; Action: Calibrate the board-image subset with OpenCV calibrateCamera/projectPoints using the board inner-corner count, measured square size and unit; retain the per-image residuals.
2. Step: 2; Action: Adapt the calibration JSON to COLMAP explicitly. For an OpenCV five-coefficient calibration result, use COLMAP FULL_OPENCV parameters [fx, fy, cx+0.5, cy+0.5, k1, k2, p1, p2, k3, 0, 0, 0]. The +0.5 shifts OpenCV pixel-center coordinates to COLMAP’s corner-based convention. Supply these during feature_extractor with --ImageReader.camera_model FULL_OPENCV --ImageReader.camera_params <comma-separated values> and --ImageReader.single_camera 1 only if every image has identical sensor/crop/focus settings. Read the stored camera back through pycolmap.Database.read_camera and compare width, height, model and every parameter before mapping; choose whether bundle adjustment may refine intrinsics. Never edit the binary SQLite camera parameter blob by hand.
3. Step: 3; Action: Run COLMAP feature_extractor, matcher and mapper on the photo set, producing database.db and a sparse/0 camera model with sparse points.
4. Step: 4; Action: Bridge the COLMAP sparse result to OpenMVS: run colmap image_undistorter --image_path <images> --input_path sparse/0 --output_path dense --output_type COLMAP, then InterfaceCOLMAP -i dense -o scene.mvs --image-folder dense/images. Run DensifyPointCloud scene.mvs and ReconstructMesh scene_dense.mvs. This explicit importer consumes undistorted images, sparse camera poses and sparse cloud.
5. Step: 5; Action: Set the reconstruction’s metric frame/scale from distributed measured controls, reserve independent control lengths, then remodel selected features in OCS with dimensions labeled by evidence and read back the CAD revision.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-01; Name: Calibrate camera intrinsics and distortion; Inputs: photo-set; measurement-set; Outputs: camera-solution; Tools: OpenCV calibrateCamera; checkerboard or Charuco target; Source urls: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html; Prerequisites: Known target geometry and units; Images cover target orientations and image field; Camera/lens/focus state recorded; Preserves: Original images; Target dimensions and capture metadata; Changes or infers: Estimates intrinsics and lens-distortion coefficients; Undistorted images are derivatives; Checks: Calibration reprojection RMS and per-image residuals; Undistort a held-out target image and compare straight edges; Keep calibration target coordinates in declared units; Alternatives: COLMAP self-calibration for capture-derived focal/intrinsic estimates; Manufacturer calibration only when specific camera/lens state is known; Automation: scripted; Evidence status: documented_capability; Summary: Solve camera intrinsics/distortion from corresponding known target coordinates and detected image points; target size supplies metric length scale to later pose solutions.
2. Id: REC-03; Name: Estimate camera poses and sparse structure from overlapping photos; Inputs: photo-set; Outputs: camera-solution; point-cloud; Tools: COLMAP/pycolmap; AliceVision/Meshroom; OpenMVG; Source urls: https://github.com/colmap/colmap/blob/main/doc/cli.rst; https://alicevision.org/; https://github.com/openMVG/openMVG; Prerequisites: Static scene or moving objects masked; Overlap and texture sufficient for feature matching; Camera model/preprocessing documented; Preserves: Input images; Feature and match database, camera model, sparse reconstruction and settings; Changes or infers: Estimates camera poses and sparse 3D points; Monocular reconstruction scale is arbitrary absent controls/metric sensor; Checks: Registered image fraction and component connectivity; Reprojection residual distribution; Camera path and sparse outliers; At least two separated scale controls for local distortion detection; Alternatives: OpenMVG+OpenMVS; Depth Anything 3 multi-view pose/depth estimate; Surveyed camera poses when available; Automation: mixed; Evidence status: existing_report_registered; Summary: Recover view geometry and camera poses from overlapping images; normalize all exported poses to a named frame and apply scale only from explicit evidence.
3. Id: REC-17; Name: Build dense point cloud and mesh from SfM camera solution; Inputs: photo-set; camera-solution; Outputs: point-cloud; mesh; Tools: OpenMVS DensifyPointCloud; OpenMVS ReconstructMesh; COLMAP dense workspace; Source urls: https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/; https://github.com/colmap/colmap/blob/main/doc/cli.rst; Prerequisites: REC-03 sparse camera solution or equivalent calibrated poses; Overlap, exposure and scene masks retained; Scale supplied by control or metric camera data for dimensional use; Preserves: Sparse scene, images, camera poses and dense reconstruction settings; Changes or infers: Estimates dense visible surface and interpolated mesh; Unseen and occluded surfaces are not recovered from images; Checks: Image reprojection and dense coverage; Withheld control lengths and independent cloud residuals; Compare mesh-to-cloud distances and disconnected components; Alternatives: Open3D TSDF from calibrated RGB-D; Nerfstudio geometry extraction only where model support is established; Automation: scripted; Evidence status: existing_report_registered; Summary: Run dense multi-view stereo after sparse camera recovery. Dense geometry inherits the camera scale and pose errors; triangulation does not itself create metric evidence.
4. Id: REC-14; Name: Remodel segmented scan evidence as parametric CAD; Inputs: measurement-set; Input alternatives: point-cloud; mesh; Outputs: constrained-sketch; parametric-source; cad-solid; Tools: Open3D feature fits; OpenCADStudio OCS skill; parametric CAD backend; Source urls: https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Registered scan and datum frame; Dimensions labeled measured/drawing/fit/assumed; Component boundaries and units stated; Preserves: Raw scan, segmentation indices and fit report; Dimension provenance for every feature; Changes or infers: Replaces noisy sampled boundaries with constrained feature model; Hidden surfaces/functional details require explicit assumptions; Checks: OCS readback of geometry/revision; Solid validity and independent dimensions; Scan-to-CAD residual maps by surface and withheld controls; Alternatives: Mesh kept as reference-only deliverable; Faceted mesh-derived solid when that is the required representation; Automation: mixed; Evidence status: proposed_composition; Summary: Use fitted scan geometry as evidence and reconstruct an editable feature history through the existing OCS workflow; fitted parameters must remain traceable and not silently become author dimensions.
5. Id: REC-16; Name: Iterate CAD edits against registered evidence; Inputs: measurement-set; Input alternatives: cad-solid; parametric-source; Input choice groups: point-cloud; mesh; Outputs: measurement-set; Tools: OCS revision-bound edit/readback; Open3D distance queries; CloudCompare distance command; Source urls: https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode; Prerequisites: Immutable source scan and transform; CAD revision identity; Comparison regions and thresholds with units; Preserves: Prior CAD and scan revisions; Check configuration and dimensional source links; Changes or infers: Applies bounded CAD edit and computes deltas; Checks: Read back edited model; Compare same registered scan/controls across revisions; Report regional max/RMS/quantiles and functional dimension changes; Alternatives: Manual visual compare; Independent target metrology; Cross-section comparison; Automation: mixed; Evidence status: proposed_composition; Summary: Use a repeatable scan-to-CAD comparison loop while preserving the source and tying every reported deviation to exact model revisions and regions.

## Documented third-party tool and API entry points

1. Status: existing_tool_entrypoint; Entrypoint: `OpenCV findChessboardCornersSB, calibrateCamera and projectPoints: supply board object coordinates, detected image corners and image dimensions; retain intrinsics, distortion, poses and reprojection residuals.`; Source urls: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

## Output artifacts

1. Representation: Metric-anchored camera solution, dense surface reference and constrained CAD interpretation.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: OCS remodeling is a separate feature-interpretation stage requiring explicit dimensions, coordinate frame, constraints and readback.

## Checks

Pixel reprojection residuals; registered image fraction; withheld scale-control length error; mesh-to-cloud regional distances; OCS readback and independent feature dimensions. COLMAP camera DB readback: model name, image width/height and parameter values equal the adapter values after principal point conversion; verify whether bundle-adjustment refinement is enabled. Check COLMAP sparse reprojection and camera model before OpenMVS conversion.

## Failure recovery

If calibration residuals cluster by image edge, verify lens/focus and corner detections; recapture target views if insufficient. If SfM separates into components, improve overlap/mask moving objects. If dense mesh is incomplete, adjust image coverage/lighting or use calibrated depth. If control residuals vary spatially, retain warp evidence and rebuild with more distributed controls rather than only uniform scale. If COLMAP intrinsics differ from calibration unexpectedly, inspect parameter ordering, OpenCV-to-COLMAP +0.5 px principal-point conversion, image resize/crop and bundle-adjustment refinement. Reinitialize the database with corrected feature_extractor options or use pycolmap.Database.update_camera, then read back the camera. If InterfaceCOLMAP rejects the scene, confirm image_undistorter produced COLMAP dense workspace with matching undistorted images and camera records.

## Effort and computing classification

1. **Human:** 5
2. **Setup:** 4
3. **Compute:** 4
4. **Human reason:** Full measured reconstruction plus semantic CAD remodeling has several interpretation and validation stages.
5. **Setup reason:** Requires camera calibration, photogrammetry, MVS and OCS adapters.
6. **Compute reason:** Dense MVS is CPU/RAM intensive; GPU acceleration is backend dependent; no universal minimum is established.

## Resources and scaling

1. **Cpu:** OpenMVG/MVS supports CPU processing; image count/resolution affect time.
2. **Gpu:** MVS acceleration varies by build; no universal GPU minimum was documented.
3. **Ram:** Dense depth maps raise RAM use with image size and camera count; no universal minimum.
4. **Storage:** Keep images, sparse scene, dense maps and mesh; storage grows with source resolution and MVS outputs.
5. **Scaling drivers:** Image count/resolution, depth-map resolution, overlap and dense reconstruction parameters.
6. **Variants:** Sparse-only reconstruction lowers cost but omits a dense surface; metric CAD still requires controls and OCS interpretation.

## Original sources

1. [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
2. [https://github.com/colmap/colmap/blob/main/doc/cli.rst](https://github.com/colmap/colmap/blob/main/doc/cli.rst)
3. [https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/)
4. [https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html)
5. ${CODEX_HOME}/skills/ocs-engineering/SKILL.md (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`)
6. [https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md](https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md)
7. [https://colmap.github.io/faq.html](https://colmap.github.io/faq.html)
8. [https://colmap.github.io/cameras.html](https://colmap.github.io/cameras.html)
9. [https://github.com/alicevision/Meshroom/blob/develop/INSTALL.md](https://github.com/alicevision/Meshroom/blob/develop/INSTALL.md)

Full source summaries: [source register](../../sources/source-register.md).
