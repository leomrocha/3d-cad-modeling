# Image, video and scan reconstruction for CAD remodeling

Research date: 12 November 2026. Sources below are project documentation, repositories or papers accessed on this date. Search-result and web-read content was not downloaded as a local original. No software was installed or executed. Recommendations are proposals for staged experiments.

## Decision

Use a two-track workflow. For measured reconstruction, estimate camera poses and geometry from overlapping photographs/video with COLMAP or AliceVision/Meshroom; use a depth sensor or calibrated scale/control points where metric dimensions matter. For visual scene context, train a Gaussian-splat or NeRF representation through Nerfstudio/gsplat. Bring the point cloud or textured mesh into CloudCompare and Blender for cleanup and registration. Rebuild engineering parts as constrained CAD solids in FreeCAD/OpenCASCADE or the project's chosen CAD system, using measured dimensions and explicit feature constraints. Treat the scan as evidence and a reference surface. Treat the rebuilt CAD as a separate interpretation with traceable dimensions.

Use single-image learned 3D models only to propose missing appearance or rough shape. Their hidden surfaces, dimensions, topology, and component boundaries are generated estimates, not observations. They are unsuitable as dimensional evidence.

## What each representation establishes

| Representation | Recoverable from input | Dimensional status | Best use | Main failure/check |
|---|---|---|---|---|
| SfM sparse points + camera poses (COLMAP, AliceVision, OpenMVG) | Image feature locations, relative camera poses, sparse scene points | Monocular reconstruction has arbitrary similarity scale (translation/rotation/scale gauge); scale needs a measured distance, calibrated baseline, surveyed controls, or metric sensor | Camera alignment, coverage review, scene framing, scale alignment | Inspect registered image count, reprojection residuals, camera poses, and control-point residuals |
| MVS dense point cloud / textured triangle mesh | Visible surfaces with texture/color inferred from multiple views | Scale inherits SfM scale/control; local accuracy depends on image sampling, calibration, baseline, texture and surface behavior | Surface inspection and reference for remodeling | Compare withheld measurements and repeated distances; inspect holes, double layers, vegetation, reflections, blur and edge artifacts |
| RGB-D / LiDAR point cloud or TSDF mesh | Sensor depth samples integrated across views | Potentially metric from sensor calibration, but affected by range bias, registration drift, depth noise and scale calibration | Rooms, objects, as-built reference, scan-to-CAD comparison | Verify against independent lengths and loop closure; record sensor model, range and registration residuals |
| 3D Gaussian Splatting / NeRF | View-dependent radiance and camera-consistent appearance | Usually inherits SfM poses and arbitrary scale; appearance can be excellent while geometry is diffuse or view-dependent | Navigable visual reference, documenting context, camera viewpoints | Test novel views and depth consistency; do not dimension from splat opacity/ellipsoid centers |
| Single-image learned mesh (TripoSR, TRELLIS, Hunyuan3D) | A plausible complete object conditioned by visible pixels and learned priors | Unknown scale unless imposed afterward; unseen sides and internal features are inferred | Ideation, blocking, noncritical visual proxies | Compare every critical view with source and replace inferred geometry with measured constraints |
| Parametric CAD remodeling | Explicit solids, sketches, dimensions, datums, components and constraints | Metric only to the extent of source measurements and declared assumptions | Fabrication, assemblies, simulation handoff | Validate dimensions against independent controls and report residuals/uncertainty |

Image scale recovery: if a known control length is measured as `d_model` in an SfM model and its real length is `d_real`, apply similarity scale `s = d_real / d_model`. Use at least two separated, independently measured controls to detect a wrong correspondence or reconstruction distortion; more controls distributed in depth and across the scene allow a residual check. One scale bar fixes global scale but cannot diagnose nonuniform local deformation. Preserve source units and transform as recorded metadata. A printed ruler is only as reliable as its known spacing, visibility, placement and camera calibration.

## Open-source workflow candidates

| Tool | Role and interfaces | License and restrictions | Hardware evidence |
|---|---|---|---|
| COLMAP + pycolmap | General SfM/MVS; GUI, CLI and Python bindings. CLI supports scripting, database, feature/matching, mapper, dense stages; exports camera/point formats consumed by other reconstruction tools. | COLMAP BSD-3-Clause/new BSD per official repository; check third-party algorithms/dependencies and cite them as required. | Sparse SfM is comparatively CPU tolerant; dense PatchMatch stereo is GPU/CUDA dependent in common upstream builds. Confirm actual build/backend before promising CPU-only dense operation. Official docs do not give a universal minimum GPU/RAM number. |
| AliceVision + Meshroom | Node graph desktop workflow from feature extraction through SfM, depth maps, mesh, texture and exports; AliceVision CLI nodes support graph-based automation. Strong approachable photo-to-mesh path. | MPL-2.0 for Meshroom and AliceVision; review bundled third-party licenses for redistribution. Project FAQ states user-created media belongs to creator and commercial use is allowed under software license. | Current install docs should be checked for build-specific CUDA. Older official Meshroom hardware page states NVIDIA CUDA, 8 GB minimum, 32 GB and GTX 1070 recommended; those figures are dated and should not be represented as current minimum. CPU draft meshing is documented. |
| OpenMVG + OpenMVS | OpenMVG performs feature matching/SfM; OpenMVS imports the scene and computes dense point cloud, mesh and texture. CLI and explicit intermediate scene files support reproducible pipeline composition. | OpenMVG MPL-2.0 with MIT/BSD subparts. OpenMVS upstream LICENSE is GNU Affero General Public License version 3 (AGPL-3.0). | CPU-capable pipeline options exist; dense performance depends on image count/resolution, memory and selected build. No universal minimum found in upstream evidence consulted. |
| Open3D | Python/C++ library for point-cloud IO, registration, RGB-D integration/TSDF, surface reconstruction, visualization and tensor/GPU operations; scripts can automate validation and conversions. | MIT; repository lists third-party dependencies with their own terms. | CPU supported; CUDA builds expose GPU operations. TSDF voxel size is a user-chosen resolution, not accuracy: smaller voxel length raises detail and noise sensitivity. |
| CloudCompare | Desktop point-cloud/mesh inspection, cropping, registration, scalar fields, cloud/mesh distance and command-line batch processing. Formats include common PLY/XYZ/E57/mesh formats subject to build/plugins. | CloudCompare/ccViewer applications and qCC components are GPL-2.0-or-later; CCLib core is LGPL-2.0 per official license page. | Designed for large clouds. Upstream says typical 10M+ points and up to 120M with 2 GB RAM (repository claim; actual memory varies with attributes, operations and build). |
| Blender | Mesh cleanup, decimation, remesh/retopology, alignment, visual reference composition, scripting with `bpy`, and interchange via PLY/OBJ/STL/glTF/USD; Gaussian-splat add-ons exist. | Blender software and Python API add-ons are GPL; created artwork belongs to the creator. Each extension and asset library has separate terms. | General 3D workstation GPU. Memory depends on mesh, textures and modifiers; no reconstruction-specific universal minimum. |
| Nerfstudio / gsplat | COLMAP ingestion, Nerfacto/Splatfacto training, viewer, camera-path rendering and export. `gsplat` is an Apache-2.0 CUDA rasterization/training library; Nerfstudio provides a documented modular CLI and web viewer. | gsplat and Nerfstudio code repositories state Apache-2.0. Original Inria 3DGS implementation and datasets have separate terms. | Nerfstudio documents approx. 6 GB VRAM for default Splatfacto and 12 GB for Splatfacto-big. CUDA build/runtime required for gsplat path. |

### Tool selection

1. **Default photo-to-reference mesh:** Meshroom for visual graph-based operation; COLMAP/pycolmap when Python automation, explicit pipeline steps, or integration with Nerfstudio is the priority.
2. **CPU-friendly and modular alternative:** OpenMVG plus OpenMVS; test actual build and dataset before choosing for repeated batch work.
3. **Depth scan path:** Open3D TSDF integration for scripted RGB-D; CloudCompare for interactive registration, cropping, and distance checks. Preserve raw scan and transforms.
4. **Photorealistic context:** COLMAP camera solution into Nerfstudio Splatfacto/gsplat. Keep the splat as a reference layer and use explicit camera/scale metadata.
5. **CAD surface remodeling:** Blender for visual cleanup and reference alignment; a parametric CAD application such as FreeCAD/OpenCASCADE for dimensioned sketches, features, Boolean solids and STEP export. A triangle mesh converted to a solid is still faceted scan-derived geometry unless deliberately remodeled.
6. **Single-view shape proposal:** TripoSR source and pretrained model card state MIT; its README reports about 6 GB VRAM for one image and A100 generation in under 0.5 seconds. TRELLIS.2-4B source and model card also state MIT; its README requires Linux and an NVIDIA GPU with at least 24 GB memory. Both output plausible textured meshes with unobserved geometry inferred from one image. SAM 3D Objects local code and checkpoints use Meta's custom SAM License and require Linux/NVIDIA >=32 GB VRAM. DA3 and DA3Metric-Large state Apache-2.0 and generate multi-view geometry/depth/pose and Gaussian outputs; DA3Metric is a scale-estimation aid to be checked against controls. The third-party DA3 Blender add-on exports point-cloud geometry nodes. Tencent Hunyuan3D-2.1 provides shape and texture models, but its community license explicitly excludes the EU, UK and South Korea.

## Calibration and dimensional reliability protocol

1. Record camera make/model, lens, focal length, focus state, image dimensions, image preprocessing, and whether stabilization/zoom changed during capture. Lock focus and zoom where possible; avoid digital zoom and aggressive image resizing.
2. Calibrate intrinsics and lens distortion using a checkerboard/Charuco target across the image field when measurements matter. Keep calibration images and report calibration reprojection RMS and per-view errors. Recalibrate after a lens/focus configuration change.
3. Capture overlapping views with distributed baselines. Include scale bars or surveyed control targets visible from multiple views; place controls across depth and the scene extent. Do not infer metric scale from focal length metadata alone.
4. Solve camera poses and inspect which images register, track coverage, reprojection error distribution, camera path, sparse point outliers and disconnected components. Mask moving objects/background where they poison matching.
5. Align scale and coordinate frame from documented control points. Use a rigid/similarity transform; do not apply unconstrained nonuniform scaling to make one dimension fit.
6. Validate against withheld independent dimensions. Report measured control values, model values, residuals in mm, mean absolute residual and maximum absolute residual. If claims matter, repeat with a second capture and compare. Report uncertainty based on instrument resolution, control placement and reconstruction residuals; never present mesh vertex precision as measurement accuracy.
7. For a mesh, sample distances from controls and cross-sections. Distinguish surface accuracy from visual texture quality. Shiny, transparent, dark, repetitive, featureless and moving surfaces can produce missing or false geometry.
8. For RGB-D/LiDAR, retain raw frames/points, sensor calibration, registration transforms and loop-closure results. Check drift over a closed path and compare measured baselines.
9. CAD remodeling must list every governing dimension and its evidence source: direct measurement, drawing, calibrated reconstruction, or inferred assumption. Use datums and constraints to encode measured geometry; keep inferred hidden geometry labeled as an assumption. Compare the remodeled surfaces against the scan with a distance map and inspect outliers.

Practical claim levels:

- **Visual reference:** overlap and viewpoint look plausible; no metric claim.
- **Scale set:** one measured length establishes global unit scale; local dimensional accuracy remains uncharacterized.
- **Control-fitted:** several measured controls constrain scale/pose; report their fit residuals.
- **Independently checked:** withheld dimensions and repeat capture agree within a stated tolerance; this supports a bounded accuracy claim for the checked region and setup.

## Actionable decision matrix

| Input | First pipeline | Expected output | Quality gates | CPU/GPU experiment |
|---|---|---|---|---|
| 20–50 overlapping still photos of a textured rigid object, with scale bars | Meshroom graph or COLMAP GUI; export cameras, sparse cloud, dense cloud, textured mesh | Camera solution, sparse/dense cloud, textured triangle mesh with assigned scale | Registration coverage; reprojection residuals; two independent measured lengths; mesh holes/double surfaces | CPU: feature extraction/matching and sparse mapper on small set. GPU: dense stage on same images. Compare completeness/time and controls. |
| Walkaround video of room/site | Extract sharp frames at view changes; COLMAP or Meshroom; Nerfstudio for splat | Camera poses + sparse model; optional dense mesh and 3DGS scene | Frame blur/overlap, camera loop closure, control-point residuals, withheld dimensions, novel-view inspection | CPU sparse solve on sampled frames; GPU MVS vs Splatfacto. Record image count, resolution, memory/time. |
| RGB-D sequence | Open3D RGB-D odometry/TSDF or sensor's raw point export; CloudCompare alignment | Metric point cloud/TSDF mesh and per-frame transforms | Sensor calibration, loop closure drift, known-distance residual, voxel size stated | CPU Open3D small indoor sequence; GPU tensor path if supported; compare against unintegrated frames. |
| Survey/LiDAR point cloud + photos | CloudCompare point registration; COLMAP with fixed control references if useful; Blender alignment | Colored point cloud/mesh and camera-aligned visual context | Independent target residuals; registration overlap; coordinate frame/unit record | CPU ICP and distance map; GPU visualization/mesh if available. |
| Single photo or sketch of unknown object | TRELLIS/TripoSR for proposal, then manual constrained CAD remodeling | Textured generated mesh for visual blocking; separate CAD part | Compare visible silhouette; assign dimensions only from drawing/measurements; flag hidden geometry as inferred | GPU inference where model supports; CPU baseline is not an engineering metric. Compare model versions and license. |
| Dimensioned 2D drawing or measured orthographic references | Interpret drawing into sketches/features in parametric CAD; use image as underlay | Editable solid/assembly with constraints, datums, units and source references | Recompute independent dimensions; check projected views and feature tree; compare against drawing tolerances | CPU-first parametric CAD. Optional GPU rendering does not affect geometry validity. |

## Staged experiments before installation or integration

1. **Capture design (CPU/documentation):** write a one-page protocol for one rigid object and one room, including three independent control distances and camera metadata. No software selection is made from this step alone.
2. **Small photogrammetry set (CPU sparse):** 20–30 sharp images, checkerboard calibration, coded targets and a scale bar. Run feature/matching/SfM only; record registered-image fraction, reprojection errors and arbitrary scale.
3. **Dense comparison (GPU and CPU-capable alternative):** run MVS on the same fixed images using COLMAP and Meshroom, then OpenMVG/OpenMVS if CUDA access or licensing needs point there. Compare withheld control residuals, completeness and runtime; textured appearance is not an accuracy score.
4. **Video/scene experiment:** sample a short walkaround with loop closure; compare dense mesh against Splatfacto novel views and a sensor/known-distance reference. Choose mesh for measured surface checks and splat for navigable visual context.
5. **Depth experiment:** integrate a short calibrated RGB-D sequence with Open3D at two documented voxel lengths. Compare independent length residuals and drift; smaller voxels are not presumed more accurate.
6. **CAD remodel experiment:** choose a simple object with a measured drawing. Rebuild as a parametric solid from the scan reference; record each dimension source and a CloudCompare/Open3D deviation map. Export STEP and verify units and component boundaries in a receiving CAD application.
7. **Single-image proposal comparison:** only after exact model, source-code, weight, and dataset terms are reviewed. Generate proposals for the same object, measure visible silhouette deviation and document hidden-surface differences. Never use the generated mesh to establish dimensions.

## Proposed workflow skills and integrations

Proposals for `skills/` (no files created):

1. `photo-to-reference-mesh`: capture checklist, calibration/control-point metadata, COLMAP/Meshroom run profiles, quality report, and outputs in PLY/OBJ/GLB plus source images and camera solution.
2. `scan-to-cad-remodel`: import point cloud/mesh, preserve raw source and transforms, align datums, derive constrained sketches, label inferred geometry, export STEP and deviation report.
3. `gaussian-scene-reference`: COLMAP-to-Nerfstudio/gsplat processing and camera paths, with scale metadata visibly separate from view-synthesis quality.
4. `reconstruction-quality-report`: collect tool version/configuration, registered-image count, reprojection and control residuals, scale transform, mesh/cloud statistics, and file hashes.

No reconstruction-specific skill or MCP wrapper was found in the project root. README identifies a proposed `skills/` catalogue, but currently it contains only its README. Suitable automation seams are COLMAP CLI/pycolmap, Meshroom graph files and AliceVision node CLI, OpenMVG/OpenMVS executables, Open3D Python/C++, CloudCompare CLI, Blender `bpy`, and Nerfstudio CLI. For CAD edits and dimensioned geometry, use OpenCADStudio if available in the project environment or FreeCAD/OpenCASCADE interchange; do not make a mesh-only pipeline the source of truth for engineering dimensions.

## Primary sources

- COLMAP repository (scope and license): https://github.com/colmap/colmap
- COLMAP CLI documentation: https://github.com/colmap/colmap/blob/main/doc/cli.rst
- pycolmap API: https://colmap.github.io/pycolmap/index.html
- AliceVision official project (MPL-2.0; workflows): https://alicevision.org/
- Meshroom install/automation docs: https://meshroom.readthedocs.io/en/latest/
- Meshroom copying/licenses: https://github.com/alicevision/Meshroom/blob/develop/COPYING.md
- Meshroom hardware requirements (legacy version; treat numbers as historical): https://meshroom-manual.readthedocs.io/en/bibtex1/install/requirements/requirements.html
- OpenMVG repository and license: https://github.com/openMVG/openMVG
- OpenMVS repository: https://github.com/cdcseacave/openMVS
- OpenMVS exact upstream license: https://raw.githubusercontent.com/cdcseacave/openMVS/master/LICENSE
- OpenMVS processing stages: https://openmvg.readthedocs.io/en/stable/software/MVS/OpenMVS/
- Open3D RGB-D TSDF integration: https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html
- Open3D repository/license: https://github.com/isl-org/Open3D
- CloudCompare repository and license: https://github.com/CloudCompare/CloudCompare
- CloudCompare command line: https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode
- Blender license and artwork terms: https://www.blender.org/about/license/
- Nerfstudio Splatfacto memory and workflow: https://docs.nerf.studio/nerfology/methods/splat.html
- gsplat repository/license: https://github.com/nerfstudio-project/gsplat
- TripoSR research paper: https://arxiv.org/abs/2403.02151
- TripoSR source: https://github.com/VAST-AI-Research/TripoSR
- TripoSR model card (MIT code and pretrained weights): https://huggingface.co/stabilityai/TripoSR
- TRELLIS repository (repository declares MIT; dataset/model-weight terms and restrictions must be assessed separately): https://github.com/microsoft/TRELLIS
- TRELLIS.2 Microsoft Research overview: https://www.microsoft.com/en-us/research/workbench/project/trellis
- Hunyuan3D-2 source and current community license: https://github.com/Tencent-Hunyuan/Hunyuan3D-2
- SAM 3D Objects official repository: https://github.com/facebookresearch/sam-3d-objects
- SAM 3D Objects setup (Linux/NVIDIA >=32 GB VRAM): https://github.com/facebookresearch/sam-3d-objects/blob/main/doc/setup.md
- SAM 3D custom license (covers source, checkpoints and code): https://github.com/facebookresearch/sam-3d-objects/blob/main/LICENSE
- Depth Anything 3 repository/license and CLI/API: https://github.com/ByteDance-Seed/Depth-Anything-3
- DA3Metric-Large model card (Apache-2.0; depth/camera/point-cloud outputs): https://huggingface.co/depth-anything/DA3Metric-Large
- DA3 Streaming documentation (<12 GB GPU memory claim): https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md
- DA3 Blender add-on source (third-party): https://github.com/xy-gao/DA3-blender
- TRELLIS.2-4B model card (MIT): https://huggingface.co/microsoft/TRELLIS.2-4B
- Hunyuan3D-2.1 repository and model usage: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
- Hunyuan3D-2.1 model card/license: https://huggingface.co/tencent/Hunyuan3D-2.1

## Supplied skill and model links

- **Reddit: “Any Claude Code skills you’d recommend for building a 3D game from scratch?”** https://www.reddit.com/r/aigamedev/comments/1xj5z85/any_claude_code_skills_youd_recommend_for/ — opened successfully. It is a community discussion, not a technical test or primary model source. Comments mention Blender MCP and hosted services including Meshy, Hunyuan, Tripo and Rodin, but provide no reproducible quality/accuracy comparisons. One commenter reports a generated model with two million faces; this is an anecdote and not a performance specification. It motivates mesh-decimation/topology checks for game assets, outside dimensional CAD evidence.
- **MCP Market: “Generate 3D Model”** https://mcpmarket.com/tools/skills/generate-3d-model — listing opened. It describes a downloadable Claude Code skill by TomekGancarczyk that calls Fal.ai `fal-ai/sam-3/3d-objects`, performs image/mask segmentation and cloud generation, downloads GLB assets, and emits React Three Fiber/Rapier snippets. The source skill/GitHub repository was identified as https://github.com/TomekGancarczyk/kata-workshop-cc; the skill file itself was not retrieved through the listing's failed “SKILL.md” click, so its complete prompt, dependency list, and behavior remain uninspected. The repository is a MIT-licensed React Three Fiber game workshop starter, not evidence that the hosted model or its generated outputs carry MIT terms. Do not treat the listing's “open” description as evidence of local inference.
- **Underlying SAM 3D model service** https://fal.ai/models/fal-ai/sam-3/3d-objects/api — official Fal endpoint documentation opened. It requires an API key and sends an image URL or uploaded/base64 image to a hosted API; output schema includes Gaussian splat PLY, GLB mesh, metadata and optional per-object results. This is cloud inference, not a local reconstruction workflow. The endpoint advertises commercial use; that is Fal's service claim and does not by itself establish whether this endpoint uses the exact upstream Meta checkpoint or the terms governing output reuse. The API accepts optional pointmap/depth input, but this does not make output metrically validated.
- **SAM 3D Objects upstream** https://github.com/facebookresearch/sam-3d-objects — inspected official README, setup guide and license. Code and checkpoints are explicitly both covered by Meta's custom SAM License. It grants limited worldwide use, reproduction, distribution, modifications and a patent license, subject to the agreement; redistribution passes the license through. The text includes trade-control/end-use limits, an indemnity in favor of Meta, termination conditions and California governing law. The official setup requires 64-bit Linux and an NVIDIA GPU with at least 32 GB VRAM. The README runs local Python inference from an image and object mask, and exports a Gaussian-splat PLY; it does not state a metric accuracy guarantee. This is a local learned single-image reconstruction candidate, while the Fal API is a separate hosted service path; the Fal page does not establish that its endpoint weights are licensed identically to the public repository weights.
- **Depth Anything 3 / DA3 Blender** — the ByteDance upstream README says DA3 handles arbitrary visual inputs, estimates camera intrinsics/extrinsics, depth, multi-view geometry and 3D Gaussians; exports GLB, NPZ, PLY and Gaussian videos. DA3Metric-Large's Hugging Face card states Apache-2.0, 0.35B parameters, monocular metric-depth specialization and canonical metric depth (depth is calibrated with focal length); it still needs independent controls for project accuracy. The official DA3-Streaming README reports long-sequence inference below 12 GB GPU memory and exports poses, intrinsics and a fused PLY. The separate `xy-gao/DA3-blender` add-on accepts an image folder and creates Geometry Nodes point clouds; it uses DA3, has a model-download/dependency installer, claims 4 GB VRAM can process a batch of ten at 504x280, and warns higher resolution increases VRAM. Its README labels the metric model as approximately life-size and says it is twice as slow; layered per-image textured meshes need manual cleanup. The GitHub repository exposes no LICENSE file at the inspected `main` URL, so add-on reuse/distribution rights are unknown; treat it as an optional user's local UI experiment, not a project dependency until terms are established.
- **TRELLIS and TRELLIS.2** — Microsoft TRELLIS repository declares MIT for code; the README links TRELLIS-image-large weights, whose model card/weight terms were not established in this review. TRELLIS.2-4B repository and Hugging Face model card both declare MIT for source and model. Its official README requires Linux, NVIDIA GPU with at least 24 GB memory, CUDA Toolkit (12.4 recommended), Python >=3.8; it verifies A100/H100. It exports a textured mesh/GLB. Reported H100 inference is about 3 s at 512³, 17 s at 1024³ and 60 s at 1536³; these are source benchmarks, not expected times on other hardware. This output remains a learned single-view asset proposal with inferred backsides and no measured scale.
- **Hunyuan3D current 2.1 variant** — upstream repo and Hugging Face model card identify Hunyuan3D-Shape-v2-1 (3.3B parameters) and Hunyuan3D-Paint-v2-1 (2B); README reports 10 GB VRAM for shape, 21 GB for texture and 29 GB for combined generation. README says tested with Python 3.10/PyTorch 2.5.1+cu124 and supports macOS, Windows and Linux. The 2.1 license explicitly says it does not apply in the EU, UK or South Korea; the 2.0 agreement likewise excludes those territories. Therefore these variants are not recommended for use from France under the published agreements. Hunyuan3D-2 README advertises 6 GB shape/16 GB shape+texture for its smaller variants, while a model-zoo docs page says 24.5 GB combined; this documentation conflicts, and each variant's usage still inherits the territorial restriction.
- **Project OCS skill reuse:** the installed [OCS Engineering skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md) already specifies units, coordinate frames, datums, part boundaries, evidence labels, read-back checks and separation of mesh appearance from editable CAD. Reuse this skill for the remodeling stage. Extend its invocation/context with reconstruction metadata (source images/scans, camera calibration, control-point coordinates, scale transform, units, reconstruction residuals, and inferred-hidden-geometry labels) rather than proposing another skill that duplicates its CAD contract. The project README identifies OpenCADStudio for engineering geometry; the OCS skill's installed-session instructions and `sources-and-capabilities.md` should be checked when implementation begins. No OCS operation was performed in this research task.

### Supplied-link access record

| Supplied URL | Access status | Evidence and classification |
|---|---|---|
| Reddit thread above | Opened successfully | User post and comments read. Community recommendations only; no model/service license or accuracy proof. |
| MCP Market listing above | Opened successfully | Listing read; linked underlying skill repository and claimed Fal endpoint identified. Skill document click failed (web tool returned an avatar-cache fetch error); exact skill code/prompt not inspected. |
| Underlying linked skill repo | Repository page opened | MIT listing and project files show a game workshop starter. The `/generate-3d-model` skill payload was not found in repository overview; no dependency manifest for that exact skill was verified. |
| Fal SAM 3D endpoint docs | Opened successfully | Hosted API, API-key auth, image inputs, GLB/PLY outputs and metadata schema observed. Upstream weights/license and output rights remain unestablished by the endpoint page. |
| Meta SAM 3D Objects upstream | Official README, setup and LICENSE opened | Local code and checkpoints share custom SAM License; minimum Linux x86-64 and NVIDIA >=32 GB VRAM. License is custom and has trade-control/end-use and indemnity terms. |
| ByteDance DA3 upstream and metric checkpoint | README, LICENSE and DA3Metric-Large card opened | Upstream code and metric checkpoint report Apache-2.0; outputs include camera/depth/point-cloud/splat formats; DA3 Streaming reports <12 GB GPU memory. |
| xy-gao DA3 Blender add-on | README and requirements opened; LICENSE URL returned 404 | Third-party add-on uses DA3 and downloads dependencies/models; README claims Blender 4.2/4.4/5.0 support and provides a low-VRAM batch example. Add-on licensing remains unknown. |
| Microsoft TRELLIS.2 | Official README, LICENSE and Hugging Face card opened | Both source and 4B model card say MIT. Official minimum is Linux + NVIDIA GPU >=24 GB; tested on A100/H100. |
| Tencent Hunyuan3D-2.1 / 2.0 | Official READMEs and community licenses opened | Model/code weights under Tencent custom agreement. Both exclude EU, UK and South Korea. 2.1 README reports 10/21/29 GB shape/texture/combined VRAM. |


