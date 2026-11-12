# Reconstruction reference workflows

These are documented reference workflows, not completed reconstructions. Their ratings are ordinal comparisons under the listed inputs and outputs. No runtime, memory usage or dimensional accuracy has been measured locally. The detailed records are in [reconstruction-details.json](/home/leo/projects/3dmodeling/research/workflows/details/reconstruction-details.json); source claims and access status are in [reconstruction-detail-sources.json](/home/leo/projects/3dmodeling/research/sources/round-03/reconstruction-detail-sources.json).

The comparison keeps human effort, setup effort and compute separate. Scores use the 1–5 meanings in `research/workflows/details/contract.json`. Workflow stage counts are counts of documented transitions, not clicks, jobs or elapsed time. “Visual proxy” and “view synthesis” routes can be quick to inspect; they do not become metric, editable CAD without independent dimensions and feature interpretation.

## Relative ranking

Lower rank means less effort or compute under the stated conditions. Equal values tie.

| Workflow | Human effort rank (score) | Setup rank (score) | Compute rank (score) | Documented stages |
|---|---:|---:|---:|---:|
| REC-R01 Photos + controls → CAD | 4 (5) | 3 (4) | 4 (4) | 5 |
| REC-R02 Video + RGB-D → registered scene | 3 (4) | 3 (4) | 3 (3) | 6 |
| REC-R03 Existing CAD → calibrated photos | 2 (3) | 1 (2) | 1 (1) | 2 |
| REC-R04 Scan + drawing → CAD | 3 (4) | 3 (4) | 3 (3) | 4 |
| REC-R05 Photos + learned depth + splat | 2 (3) | 3 (4) | 4 (4) | 4 |
| REC-R06 Splat + MVS mesh + CAD | 3 (4) | 3 (4) | 4 (4) | 5 |
| REC-R07 3D-anchored sketch + CAD edit | 2 (3) | 2 (3) | 1 (1) | 3 |
| REC-R08 Photogrammetry view synthesis | 1 (2) | 3 (4) | 4 (4) | 2 |
| REC-R09 RGB-D + existing CAD comparison | 2 (3) | 2 (3) | 2 (2) | 4 |
| REC-R10 Single image proxy + measured CAD | 3 (4) | 3 (4) | 4 (4) | 3 |

For REC-R10, the mesh-proxy-only branch has human effort 1; the table scores the full measured-CAD goal. For REC-R08, the table scores Gaussian Splatfacto; NeRF is a separate training output. A point-cloud/mesh extraction is a separate operation. REC-R01 and REC-R06 include dense MVS and CAD remodeling. REC-R03 ends at CAD pose registration and projection residuals.

Stage count ascending: REC-R03 and REC-R08 (2); REC-R07 and REC-R10 (3); REC-R04, REC-R05 and REC-R09 (4); REC-R01 and REC-R06 (5); REC-R02 (6). These values only count stages in the workflow records.

## Reference scripts

Both scripts are reference code and were not executed. Their JSON outputs contain computed values from a successful run, without a hard-coded execution status. They require Python, NumPy, OpenCV or Open3D respectively. Install and model execution are outside this documentation batch.

[calibrate_camera.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/calibrate_camera.py) accepts explicit image paths/globs, checkerboard internal-corner counts, measured square size and length unit. Example invocation:

```sh
python calibrate_camera.py \
  --images 'capture/calibration/*.jpg' \
  --inner-corners 9 6 \
  --square-size 24.5 \
  --unit mm \
  --output calibration.json
```

The values above illustrate CLI syntax only. Supply the actual checkerboard specification and measured square size. The script requires a finite positive square size and at least ten detected views, matching OpenCV's tutorial recommendation. It rejects an output path that resolves to an input image. It writes camera intrinsics, distortion, global calibration RMS, per-image projected-corner RMS/max, image IDs and object-to-camera pose vectors. Calibration produces K and distortion; it does not set the scale of an unrelated object reconstruction. A measured scale object/control set or metric depth sensor is still needed.

[register_clouds.py](/home/leo/projects/3dmodeling/examples/workflows/reconstruction/register_clouds.py) accepts source and target PLY clouds, a caller-provided initial source-to-target 4×4 transform, an explicit maximum correspondence distance and its unit. Example invocation:

```sh
python register_clouds.py \
  --source scan_fragment.ply \
  --target reference.ply \
  --initial-transform init.json \
  --max-correspondence-distance 2.0 \
  --unit mm \
  --max-iterations 30 \
  --output-report registration.json \
  --output-source-ply registered_source.ply
```

The example threshold is illustrative and means 2 mm only because the example selects `mm`; choose it from sampling spacing, noise and the engineering tolerance. `init.json` has a finite, rigid, orthonormal `source_to_target` 4×4 transform with rotation determinant +1. Open3D ICP assumes compatible scale and a useful initial transform. The script requires a finite positive threshold, rejects output paths that collide with any input or with each other, then writes the final source-to-target transform, fitness, inlier RMSE, correspondence count, parameter values and a transformed source derivative. It preserves both input files. The report metrics describe the fitted correspondences; compare independent controls for dimensional accuracy. Point-to-plane mode requires a finite positive normal neighborhood radius and explicit neighbor count.

OpenCV source APIs: [camera calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html), [solvePnP and projection](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html). Open3D source APIs: [ICP registration](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html), [global registration](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html), [RGB-D integration](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html). OpenCV PnP uses camera X-right, Y-down, Z-forward and returns object/world-to-camera pose. Open3D registration returns source-to-target. Each transform adapter must record direction, axes and units.

## Documented tool handoffs

### OpenCV calibration JSON → COLMAP database → OpenMVS

`calibrate_camera.py` writes OpenCV `K`, distortion coefficients `[k1,k2,p1,p2,k3]`, image dimensions and pixel residuals. COLMAP uses a corner-based image-pixel convention whose principal point is `+0.5 px` relative to OpenCV. For a matching camera model, map `K` and distortion to COLMAP `FULL_OPENCV` parameters:

```text
fx, fy, cx+0.5, cy+0.5, k1, k2, p1, p2, k3, 0, 0, 0
```

The zero values fill COLMAP `k4,k5,k6`; this adapter assumes OpenCV's five-coefficient calibration output and a compatible pinhole lens. Pass the resulting comma-separated values to `--ImageReader.camera_params` during feature extraction. Use `--ImageReader.single_camera 1` only when every image has the same physical camera, crop, resolution and focus state. Read the camera back with `pycolmap.Database.read_camera`, verify model/dimensions/parameter order, and select whether bundle adjustment may refine the values. COLMAP refines intrinsics by default. Do not edit its binary SQLite parameter blob manually. Sources: [COLMAP known-intrinsics FAQ](https://colmap.github.io/faq.html), [camera models](https://colmap.github.io/cameras.html).

```sh
colmap feature_extractor --database_path <database.db> --image_path <images> \
  --ImageReader.single_camera 1 --ImageReader.camera_model FULL_OPENCV \
  --ImageReader.camera_params '<adapter-produced-12-values>'
colmap exhaustive_matcher --database_path <database.db>
colmap mapper --database_path <database.db> --image_path <images> --output_path <sparse>
colmap image_undistorter --image_path <images> --input_path <sparse/0> \
  --output_path <dense> --output_type COLMAP
InterfaceCOLMAP -i <dense> -o <scene.mvs> --image-folder <dense/images>
DensifyPointCloud <scene.mvs>
ReconstructMesh <scene_dense.mvs>
```

The COLMAP/OpenMVS handoff is `image_undistorter` → `InterfaceCOLMAP`; the importer consumes undistorted images, sparse camera poses and sparse points and writes an MVS scene. OpenMVG's `openMVG_main_openMVG2openMVS` is a separate exporter route documented by OpenMVS. These paths are not interchangeable adapters. Sources: [COLMAP CLI](https://colmap.github.io/cli.html), [OpenMVS usage](https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md).

### Other documented CLI routes

```sh
# AliceVision Meshroom photogrammetry graph
meshroom_batch --input <images-folder> --output <output-folder>

# Nerfstudio image set → Gaussian scene; geometry remains separate
ns-process-data images --data <images-folder> --output-dir <processed-data>
ns-train splatfacto --data <processed-data>

# TripoSR single-image mesh proxy
python run.py <single-image> --output-dir <output-folder>
```

Meshroom saves graph intermediates and can reuse cached nodes. Nerfstudio uses COLMAP and FFmpeg in the image processing route. TripoSR's own README says its command writes a reconstructed model and reports about 6 GB VRAM for one image. These are documented invocation contracts, not commands executed in this batch. Sources: [Meshroom batch usage](https://github.com/alicevision/Meshroom/blob/develop/INSTALL.md), [Nerfstudio custom data](https://docs.nerf.studio/quickstart/custom_dataset.html), [Nerfstudio Splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html), [TripoSR README](https://github.com/VAST-AI-Research/TripoSR/blob/main/README.md).

## CAD remodeling handoff

For a measured engineering model, use the existing [OCS Engineering skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md). Keep scan and mesh as evidence/reference layers. Create parametric features from named dimensions, datums and component boundaries; label measured, drawing-derived, fitted and assumed values; read back the resulting CAD revision and perform independent checks. Ray-hit annotations in REC-R07 are calculated anchors tied to camera calibration and reconstructed hit geometry. They are not independent physical measurements. Choose sketch meaning and constraints before CAD feature creation.

## Primary source references

- [OpenMVG → OpenMVS stage commands](https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/) — export/import scene, densify, reconstruct mesh, texture.
- [COLMAP CLI](https://github.com/colmap/colmap/blob/main/doc/cli.rst) — scripted SfM and reconstruction command route.
- [Nerfstudio Splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html) — Gaussian PLY and model-specific resource/export notes.
- [Nerfstudio geometry export](https://github.com/nerfstudio-project/nerfstudio/blob/main/docs/quickstart/export_geometry.md) — geometry-export commands; Splatfacto support is constrained by its model FAQ.
- [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3) and [streaming README](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md) — learned depth/pose/geometry route.
- [TripoSR](https://github.com/VAST-AI-Research/TripoSR), [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) and [SAM 3D Objects](https://github.com/facebookresearch/sam-3d-objects) — single-image proxy candidates with different code/weight terms and GPU requirements. See the primary model cards in the source register before selecting a model.

No source originals were downloaded in this batch. Source summaries identify claims reused from the existing reconstruction report versus documentation opened during this batch.
