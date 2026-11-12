# REC-R03 — Existing CAD aligned to calibrated photos

Date: 2026-11-12. Classification: analyst assessment under the stated conditions.

**Manual effort 3/5; setup 2/5; computing 1/5.**

Output: Camera pose linking a known CAD revision to photo views and pixel reprojection report.

## Comparison conditions

CAD datum and units known; visible unique CAD landmarks; calibrated camera; pixel correspondences identified in the supplied measurement set.

## Registered starting artifact types

1. parametric-source
2. photo-set
3. measurement-set

## Detailed source and preparation artifacts

1. Artifact: parametric-source; Format and quality: Native editable CAD source and revision identifier.
2. Artifact: photo-set; Format and quality: Calibration and object image set with stable camera/lens settings.
3. Artifact: measurement-set; Format and quality: CAD/world 3D point IDs and corresponding 2D pixel coordinates; units explicit.

## Reference points, datums and coordinate frames

PnP uses labeled pairs (X,Y,Z) in CAD/world frame and (u,v) pixels plus K/distortion. OpenCV outputs object/world-to-camera. Camera axes X-right Y-down Z-forward. A separate calibration target is required for K/distortion unless a documented calibration exists. Held-out CAD landmarks check pose, not hidden geometry.

## Software, libraries and dependencies

1. Name: OpenCV; Licence scope: Apache-2.0 for OpenCV >=4.5 (including current 4.x); older releases retain their release-specific BSD-3-Clause terms; Role and api: calibrateCamera; solvePnPRansac; projectPoints; Dependencies: Python cv2 + NumPy
2. Name: OCS/Blender; Licence scope: Project-specific / GPL-licensed Blender; Role and api: CAD landmarks and camera image overlays; Dependencies: Existing CAD importer and image projection

## Procedure

1. Step: 1; Action: Use calibrate_camera.py on measured calibration board views if no valid camera solution exists.
2. Step: 2; Action: Create correspondences from known CAD coordinates and measured image pixels.
3. Step: 3; Action: Run solvePnPRansac with camera matrix and distortion; save object-to-camera transform and inlier list.
4. Step: 4; Action: Project withheld CAD landmarks/edges with projectPoints and report pixel residuals; preserve native CAD revision.

## Inputs, outputs and requirements at each registered operation

1. Id: REC-01; Name: Calibrate camera intrinsics and distortion; Inputs: photo-set; measurement-set; Outputs: camera-solution; Tools: OpenCV calibrateCamera; checkerboard or Charuco target; Source urls: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html; Prerequisites: Known target geometry and units; Images cover target orientations and image field; Camera/lens/focus state recorded; Preserves: Original images; Target dimensions and capture metadata; Changes or infers: Estimates intrinsics and lens-distortion coefficients; Undistorted images are derivatives; Checks: Calibration reprojection RMS and per-image residuals; Undistort a held-out target image and compare straight edges; Keep calibration target coordinates in declared units; Alternatives: COLMAP self-calibration for capture-derived focal/intrinsic estimates; Manufacturer calibration only when specific camera/lens state is known; Automation: scripted; Evidence status: documented_capability; Summary: Solve camera intrinsics/distortion from corresponding known target coordinates and detected image points; target size supplies metric length scale to later pose solutions.
2. Id: REC-12; Name: Register existing CAD to calibrated photographs or scan points; Inputs: measurement-set; Outputs: camera-solution; measurement-set; Tools: CAD tessellation with named 3D landmarks; OpenCV solvePnPRansac; Open3D global registration and ICP; Source urls: https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html; https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html; https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html; Prerequisites: Known CAD units, component datum and exact CAD revision; Visible identifiable CAD landmarks or scan geometry; Camera calibration for photo route; Preserves: Authoritative CAD revision and its units; Photo/scan source and registration transform; Changes or infers: Estimates CAD-to-camera/world transform; Surface registration uses a tessellated derivative of CAD; Checks: Independent landmark reprojection residuals; Scan-to-CAD distance map and interface dimensions; Check symmetries/partial overlap for alternate poses; Alternatives: Surveyed fiducials; Manual datum alignment; Photogrammetric camera solve with control targets; Automation: mixed; Evidence status: proposed_composition; Summary: Register a known CAD revision to measured photo landmarks or sampled scan geometry; the source CAD and scan/photo remain separate evidence.; Input choice groups: parametric-source; cad-solid; photo-set; point-cloud; mesh

## Code and tool entry points

1. Path: [calibrate_camera.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/calibrate_camera.py); Status: reference_code; Entrypoint: `python calibrate_camera.py --images <glob-or-path> ... --inner-corners <cols> <rows> --square-size <measured> --unit <mm|cm|m|in> --output calibration.json`; Source urls: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

## Output artifacts

1. Representation: Camera pose linking a known CAD revision to photo views and pixel reprojection report.; Dimensional status: Metric only where tied to explicit controls/sensor calibration; learned visual surfaces and view-synthesis products remain inferred or appearance representations.; Editable cad dependency: No new CAD in this workflow.

## Checks

PnP inlier count and spatial spread; pixel RMS/max residual on fit and withheld landmarks; coordinate-frame transform direction; repeated views yield consistent pose.

## Failure recovery

For a plausible but wrong pose, verify correspondence labels and CAD revision; add spatially distributed landmarks; resolve symmetric/ambiguous geometry with a target or known datum. Recalibrate after lens/focus change.

## Effort and computing classification

1. **Human:** 3
2. **Setup:** 2
3. **Compute:** 1
4. **Human reason:** Landmark identification and correspondence checking need judgment; geometry is already known.
5. **Setup reason:** One OpenCV script plus CAD landmark export.
6. **Compute reason:** PnP and projection are small CPU matrix operations; image resolution/count have low scaling cost.

## Resources and scaling

1. **Cpu:** OpenCV calibration/PnP and projection use CPU.
2. **Gpu:** No GPU required.
3. **Ram:** Low; calibration images are loaded in memory.
4. **Storage:** Low; outputs are camera matrices and residual reports.
5. **Scaling drivers:** Image resolution, number of calibration views and landmark count.
6. **Variants:** Existing calibration avoids re-solving intrinsics; view projection remains CPU-light.

## Original sources

1. [https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
2. [https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html)

Full source summaries: [source register](/home/leo/projects/3dmodeling/research/sources/source-register.md).
