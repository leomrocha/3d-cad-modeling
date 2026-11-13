# Point 07 — Capture, reconstruction and appearance scenes

Date: 12 November 2026. Status: **DONE — documentation and independent review**. The 17 operation definitions, 51 actions, helper specifications and future cases are proposals. Requested designer dispatch: `gpt-6-astra`, effort `xhigh`. Actual runtime model identity: **unavailable**.

The [structured action records](point-07-operations.json) contain all fifteen required fields per action. This document gives the ordered actions, actual tool boundaries, helper contracts, execution choices and validation. The [audit plan](plan.md), [sequence](sequence.json) and [original implementation plan](../implementation-plan.md) retain their existing scope. Source evidence is recorded in the [primary-source review](reviews/point-07-sources.md) and [26 successful inspections plus four failed attempts](../sources/round-05/point-07-web-sources.json). The designer read these local records; Luna performed the external inspection.

## 1. Terms and preserved contracts

1. **Structure from motion (SfM)** estimates cameras and sparse 3D points from matching image features. **Bundle adjustment** jointly refines cameras and points. **Multi-view stereo (MVS)** estimates denser surfaces using several camera views. **Reprojection** maps 3D points back into a camera image; a **residual** is the difference from the named reference after the stated mapping or fit.
2. **RGB-D** means colour images paired with depth. **Odometry** estimates motion between successive frames. A **voxel** is a cell in a 3D grid. A **truncated signed distance field (TSDF)** stores a bounded signed-distance estimate near a surface; surface extraction creates a mesh from that field. A **normal** is a surface direction perpendicular to its local plane; **topology** describes how vertices, edges and faces connect. **Decimation** reduces mesh faces and creates a derivative whose local shape changes need checks.
3. **Intrinsics** describe camera imaging geometry, including focal and principal-point parameters. **Extrinsics** describe the camera position and orientation relative to another frame. A **quaternion** is a four-component rotation representation whose component order/convention must be recorded. **Normalization** here means a documented coordinate reorientation, translation or scaling. A **mask** identifies image regions used or excluded by an operation.
4. A **Gaussian scene** contains learned spatial Gaussian rendering primitives, including position, extent/orientation, opacity and appearance parameters. A **neural radiance field (NeRF)** is a trained representation queried to render views. A **renderer** produces an image from a representation and camera. A training **checkpoint** stores model state for loading or resumption. **PLY** can carry point attributes or triangle faces; **GLB** is a binary glTF scene container. The actual fields and consumer determine the representation.
5. A **vision-language model (VLM)** reasons over image and text evidence. A **sidecar** is a separate metadata file associated with an artifact. **VRAM** is graphics-processor memory. A **pinned revision** is an explicitly fixed revision or content hash. A **branch** is an isolated candidate procedure with its own inputs, settings and result.
6. **CAD-16 — photo-derived geometry** requires `photo-set` AND `measurement-set` and all three outputs: cameras, cloud and mesh. **REC-03 — sparse reconstruction** supplies cameras and sparse cloud; **REC-17/DOM-28 — dense reconstruction** supplies cloud and mesh. Fusion and meshing are separate stages. Source: [original CAD contracts](../workflows/cad-paths.json) and [original reconstruction contracts](../workflows/reconstruction-paths.json).
7. **DOM-20 — photo reconstruction** declares photos → cameras and cloud, while its title also mentions video/mesh. REC-04 supplies the video-to-photo stage; REC-17/DOM-28 supplies mesh. **DOM-21 — depth reconstruction** declares depth plus measurements → cloud; REC-06 supplies a separate cloud-and-mesh fusion branch. **DOM-22 — Gaussian appearance** declares `gaussian-scene`; DOM-30 declares `nerf-scene`. These source-contract findings preserve the [original domain records](../workflows/domain-paths.json).
8. **REC-10 — learned cameras/cloud** accepts photos OR video and requires cameras plus cloud; optional Gaussian products retain their own type. **REC-11 — visual scene** packages a named Gaussian/NeRF subtype with its renderer assets. **REC-18 — single-image mesh** selects one source image and a mesh-capable backend. The inspected SAM 3D Objects example produces Gaussian PLY; TripoSR and TRELLIS.2 document mesh routes. Generic Nerfstudio TSDF documentation and Splatfacto-specific unsupported mesh/cloud export wording form a recorded source conflict; the selected model/version requires an actual capability check.

## 2. Common source and execution protocol

1. **Scope and evidence status.** PROPOSAL documentation/implementation design for the seventeen unchanged original operation contracts. Existing sources establish scoped capabilities; future helper, reconstruction, training, inference and test actions have not been executed in this batch. Acceptance is recorded only by MARK AS ACCEPTED. Requested dispatch gpt-6-astra/xhigh; actual runtime identity unavailable.

2. **Capture and rights lineage.** Hash original capture/video/depth bytes and each derivative. Record original path/URL, acquisition time/device/camera state, rights/consent/source restrictions, frame/timestamp IDs, mask/calibration revisions and preprocessing chain. Distinguish physical capture, generated image, rendered view and synthetic validation fixture. Preserve source code, dependency, checkpoint/model-weight, dataset and input/output-asset licence records separately with exact version and source evidence status.

3. **Camera and pixel mappings.** For each image retain dimensions, pixel-centre/grid convention, crop/resize/rotation/undistortion map and valid domain, camera/lens/focus/zoom group, intrinsic matrix and distortion model/parameters. Intrinsics describe imaging geometry; extrinsics describe camera position/orientation relative to a named frame. Record handedness/axes/units, quaternion order, transform source→target and whether scale is included. COLMAP inspected 4.3.0.dev0 camera page and format give +Z viewing and world→camera Hamilton (qw,qx,qy,qz) plus translation. Its top-left pixel centre is (0.5,0.5); the FAQ's +0.5 to cx/cy applies only to the stated OpenCV/Kalibr integer-centred source convention. Apply crop/resize mapping and any pixel-convention correction once, then compare projections and actual saved camera readback. Calibration-target units alone do not set unrelated scene scale.

4. **Nerfstudio parser mappings.** Nerfstudio camera basis is +X right,+Y up,+Z backward, viewing -Z; transforms.json columns hold camera axes and translation holds camera origin. Camera-basis conversion and world normalization are separate recorded transforms. Inspected mutable-main parser exposes orientation_method=up, center_method=poses, auto_scale_poses=true, scale_factor=1 and scene_scale=1 as source defaults, not project choices. scene_scale controls box bounds. Retain actual orientation_override, applied_transform/applied_scale, dataparser_transform and dataparser_scale. Source auto-scale uses reciprocal maximum absolute camera-origin coordinate times configured scale; metadata scale also contributes. The source fallback COLMAP mapping [[0,1,0,0],[1,0,0,0],[0,0,-1,0]] applies only under its documented dataset/metadata condition. Save the actual returned composition; map back by undoing scale separately and applying the inverse recorded frame transform in the adapter's verified order. Do not apply a second assumed axis or focal conversion. Test known camera origins/projections before training, including zero-extent/degenerate normalization inputs. PROPOSAL adapter contract: declare p_normalized = s*(R*p_source+t), with finite positive s and orthonormal rigid R; its reverse is p_source = R^T*(p_normalized/s-t). This equation defines the chosen adapter order and must be matched to the selected parser's actual composed metadata/output fields before use. Camera origins follow the position mapping; camera orientation/basis is converted separately. Test nontrivial translation and scale on known points and camera origins so applying inverse transform before undoing scale is detected.

5. **Depth encoding, motion and fusion.** Record raw depth representation, physical units, axial-depth versus ray-range convention, invalid sentinel/mask, sensor intrinsics/distortion, RGB-depth extrinsics, registration/resampling, timestamp synchronization and per-frame pose source. Open3D v0.20.0 RGBDImage.h declares depth_scale=1000, depth_trunc=3, convert_rgb_to_intensity=true. RGBDImageFactory.cpp requires equal color/depth dimensions and forwards settings; Image.cpp divides raw depth by scale then zeros values >= truncation. Raw zero remains zero. Choose actual source-specific scale, invalid/range mask and grayscale policy; precheck negative/nonfinite data rather than assuming these are rejected. Tutorial truncation 4 is its example. Pairwise odometry returns success, 4×4 motion, 6×6 information; selected adapter must establish trajectory direction and information meaning. TSDF adapter takes explicitly world→camera extrinsics; tutorial inverse(camera_pose) corresponds to its camera-to-world poses, so invert only when actual source direction requires it. Retain skipped-frame reasons, voxel length, signed-distance truncation, integration bounds/order/weights and valid support. Grid detail and information/confidence scores do not supply physical uncertainty.

6. **Learned output and metric evidence.** Bind exact model/checkpoint/hash, configuration, preprocessing, seed/backend and source rights. DA3Metric-Large card reports depth/confidence [N,H,W], world→camera extrinsics [N,3,4], intrinsics [N,3,3] and a canonical-metric-depth/focal-length claim without its reference/divisor. Discover actual selected API depth units/conversion before metric use; apply no invented or duplicate focal conversion. Preserve model confidence's documented meaning; independent measured controls establish dimensional residuals. SAM 3D Objects inspected image+mask example returns Gaussian PLY; TripoSR and TRELLIS.2 provide separate mesh-producing routes. Generated back/occluded surfaces retain inference lineage.

7. **Actual representations and supported exports.** Sparse points, dense MVS samples, calibrated depth samples, TSDF-extracted surfaces, generated mesh, Gaussian rendering parameters and NeRF state have distinct typed receipts. Inspect actual PLY attributes and faces; extension equality does not make Gaussian centres/covariances/opacity observed surface samples. COLMAP stereo_fusion outputs cloud; poisson_mesher/delaunay_mesher or supported OpenMVS ReconstructMesh creates the separate mesh. Open3D consistent-normal propagation uses neighbours and does not prove outward orientation; Poisson returns mesh+density and ball-pivoting needs oriented normals+radii in coordinate units. Preserve pre-edit meshes, region/sample/face maps and settings for smoothing/fill/decimation. Quadric target triangle count is checked against actual local shape changes. NeRF/Gaussian visual-scene packages retain actual config/checkpoint/renderer/assets and supported export subtype. Generic Nerfstudio TSDF and Splatfacto-specific unsupported mesh/cloud pages conflict; model/version capability gates that extraction. A proposed appearance+independent mesh+CAD composition keeps each layer and measured transform intact.

8. **Feature criteria.** For every named feature and downstream operation record intended use, required coverage/detail, source dimension/position/shape, units/frame and status. Engineering allowance, source measurement uncertainty, reconstruction/fit residual, approximation/discretization setting and computational comparison threshold each retain their own source and meaning. Context/layout, viewing appearance and working-interface/house/robot targets use their supplied criteria; no numeric default invents engineering acceptance. READY/BLOCKED names the feature, downstream operation and missing/failed criterion.

9. **Evaluation participation.** Freeze calibration, pose/SfM, scale/registration-fit, training, camera-optimization, tuning/selection and evaluation roles per source image/control. Heldout physical controls are excluded from the fit they evaluate; heldout calibration-view projection needs the point-05 independently defined pose procedure. An image excluded from radiance training but used for SfM retains shared pose/calibration dependence. Cross-method outputs list shared photos/masks/poses/measurements/checkpoints. Generated/rendered novel views are derived internal checks; real additional captures/measurements retain actual acquisition evidence. After repeated tuning on evaluation evidence, record its selection role and use a separately recorded evaluation source for a new independent claim.

10. **Candidate selection and compatible merging.** For each isolated candidate record source subset/revisions, intended use, requested detail, feature coverage, tolerance/uncertainty criteria, units/frame, method/version/seed and local/remote/manual resource fields. Give the VLM original full views plus mapped crops, camera/sample/feature IDs, source/control regions and numerical reports. Return evidence-linked whole-candidate choice, compatible region/layer selection, alternatives or source conflict. Do not average contradictory source dimensions or geometry meanings. Region/geometry edits or composition create a new revision with source-per-feature map and explicit scope. Reopen saved outputs and rerun affected numerical/source-projection/topology/control checks. A separate semantic review execution, distinct from the producing/selecting agent, checks original sources and the new revision; record both actual/requested identities and common source dependencies.

11. **Local, remote and manual resources.** Perform manifest/rights/type checks, selected-image camera projection, sparse or bounded-depth/mesh preview and selected-region comparison before dense reconstruction or full training. Record source bytes, images/frames and resolution, camera/track/point/face counts, voxel/grid extent, ray batches, iterations/Gaussian counts, checkpoint size, build/backend, CPU/GPU identity, RAM/VRAM and observed run cost when executed. OpenMVS develop documents CPU SGM and memory sub-scenes with seam checks; COLMAP dense backend support is build-dependent. TripoSR about 6 GB, TRELLIS.2 Linux/NVIDIA>=24 GB (CUDA 12.4 recommended), SAM Objects Linux 64-bit/NVIDIA>=32 GB are exact repository setup claims. DA3 Streaming memory depends on dataset/resolution/chunk/overlap. Source claims do not measure this workstation. Remote VLM/model-service location, actual model when exposed, requested effort, request bytes, calls/tokens/latency/cost and manual interpretation/edit time are independent records. Proposed parallel branches share preparation but actual computational runs follow project concurrency scope.

12. **Failure and resumption.** Give every future native/tool/remote request an ID, input hashes, exact configuration/version, intended output path/revision and validated boundary. On uncertain completion inspect actual outputs/job/checkpoint state before retry; retain partial files and completed stage receipts. Remote inference/VLM preserves request/prompt/input IDs, raw/partial responses and request status; reconcile provider completion before a bounded retry with lineage. Validate returned selection rows/IDs/types/evidence before changing a merged artifact. Interrupted writes use separate partial versus published-complete identities. Re-hash source/calibration/mask/model/control dependencies on resume; changed inputs invalidate affected descendants only. Preserve prior results and failures; do not silently overwrite or treat an empty/truncated output as success.

13. **Migration from agent actions to software.** PROPOSAL migrate one supported input/model/parser/output/consumer class at a time after checked cases establish actual source/transform/output/exception behavior. First retain agent-selected evidence and compare software decisions with those checked cases. Automate deterministic parsing, mappings and numerical tests with explicit exception triggers; retain source interpretation/new design choices and unsupported classes with reasoning. Regressions restore the reviewed agent route for affected classes. Fixture results establish exercised behavior only, while physical/source correctness keeps independent controls.

Source entrypoints for these common clauses:

| Source | Concrete interface or condition |
| --- | --- |
| [COLMAP format](https://colmap.github.io/format.html), [camera models](https://colmap.github.io/cameras.html), [FAQ](https://colmap.github.io/faq.html), [CLI](https://colmap.github.io/cli.html) | Camera models, world-to-camera poses, conditional pixel-centre conversion and separate sparse/dense/meshing stages. |
| [OpenMVS develop usage](https://github.com/cdcseacave/openMVS/blob/develop/docs/wiki/Usage.md) | `InterfaceCOLMAP` consumes the matching undistorted workspace; `DensifyPointCloud` and `ReconstructMesh` materialize separate outputs; CPU matching and sub-scenes have explicit conditions. |
| [Open3D v0.20.0 header](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImage.h), [factory](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/RGBDImageFactory.cpp), [depth conversion](https://raw.githubusercontent.com/isl-org/Open3D/v0.20.0/cpp/open3d/geometry/Image.cpp) | Defaults, equal image dimensions and actual divide-then-truncate behavior have separate owning sources. |
| [Open3D odometry](https://www.open3d.org/docs/latest/python_api/open3d.pipelines.odometry.compute_rgbd_odometry.html), [integration](https://www.open3d.org/docs/latest/tutorial/pipelines/rgbd_integration.html), [PointCloud](https://www.open3d.org/docs/latest/python_api/open3d.geometry.PointCloud.html), [TriangleMesh](https://www.open3d.org/docs/latest/python_api/open3d.geometry.TriangleMesh.html) | Motion outputs, pose-directed integration, normals, surface reconstruction and measured decimation derivatives. |
| [Nerfstudio conventions](https://docs.nerf.studio/quickstart/data_conventions.html), [parser source](https://raw.githubusercontent.com/nerfstudio-project/nerfstudio/main/nerfstudio/data/dataparsers/nerfstudio_dataparser.py), [custom data](https://docs.nerf.studio/quickstart/custom_dataset.html) | Supplied cameras, basis and pixel conventions, actual parser transform/scale and metadata conditions. |
| [Splatfacto](https://docs.nerf.studio/nerfology/methods/splat.html), [geometry export](https://docs.nerf.studio/quickstart/export_geometry.html) | Gaussian export and the recorded generic-versus-method-specific surface-export conflict. |
| [DA3](https://github.com/ByteDance-Seed/Depth-Anything-3), [Streaming](https://github.com/ByteDance-Seed/Depth-Anything-3/blob/main/da3_streaming/README.md), [DA3Metric-Large card](https://huggingface.co/depth-anything/DA3Metric-Large) | Exact variant outputs, chunk/resource conditions, camera arrays and bounded metric/focal claim. |
| [TripoSR](https://github.com/VAST-AI-Research/TripoSR), [TRELLIS.2](https://github.com/microsoft/TRELLIS.2), [SAM Objects](https://github.com/facebookresearch/sam-3d-objects), [SAM setup](https://github.com/facebookresearch/sam-3d-objects/blob/main/doc/setup.md) | Model-specific mesh versus Gaussian output and stated hardware conditions. |

The [point-05 alignment procedure](point-05-alignment-and-remodeling.md) supplies camera/control and CAD remodeling handoffs. The [point-02 reuse procedure](point-02-component-reuse.md) supplies revision and compatible-component checks. The OCS engineering skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) govern a separately scoped CAD handoff; reconstruction does not itself create parametric CAD history. OCS remains the project's native CAD route, and another CAD adapter requires its documented capability and scoped proposal.

## 3. REC-04 — Convert video into an image reconstruction dataset

[Original contract](../workflows/reconstruction-paths.json): **video → photo-set**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-04-A01 — Inventory video timing camera state and coverage.** (1) Pin original stream bytes and metadata. (2) Identify camera-state/scene intervals. (3) Define sharpness, redundancy and viewpoint coverage criteria. Output: Source hash/stream manifest, scene intervals and frame-selection criteria. Check: Frame rate alone cannot reconstruct variable presentation timestamps; physical capture and synthetic frames remain labelled.

1. **REC-04-A02 — Extract selected frames with reversible timeline mapping.** (1) Decode selected original frame events. (2) Apply only recorded image transforms. (3) Write images and exact source-frame/timestamp associations. Output: Frame images with original index/timestamp/source hash and pixel-processing map. Check: Derived frame label must identify original event; duplicates and interpolation retain explicit status.

1. **REC-04-A03 — Check dataset quality and camera compatibility.** (1) Compare selected frames to source interval. (2) Check timing, viewpoint bridges and camera groups. (3) Publish dataset and retained source-quality issues. Output: Checked photo-set with coverage, quality and timing exceptions. Check: Many adjacent images do not substitute geometric baseline; moving/blurred regions remain explicit.

Existing entrypoints and proposed helper interfaces:

1. **REC-04-A01.** Software: Use supported ffprobe/decoder metadata inspection; inventory resolution/rate/rotation and variable timing. Proposal: video intake emits stream/timebase/camera/rights records and selection plan.

1. **REC-04-A02.** Software: Decode selected source frames with supported FFmpeg selection; retain exact timestamps and avoid synthesizing intermediate views. Proposal: frame extractor accepts timeline selections and outputs images plus frame/time/pixel manifest.

1. **REC-04-A03.** Software: Check hashes, monotonic timestamps per stream, duplicate rates and compatible image/calibration dimensions. Proposal: frame-set verifier emits per-image quality/camera/timeline readiness.

Execution choices:

1. **Agent directs.** Agent reviews timeline/viewpoint evidence and directs selection.

1. **Software and agent.** Software extracts/filters; agent reviews coverage and dynamics.

1. **Software ordinary cases.** Checked capture classes select frames with quality/timing exceptions.

1. **Complete software procedure.** Explicit timestamps/transforms/criteria yield reproducible frame dataset.

Alternatives and target detail: Manually selected original keyframes with exact timeline records. Bounded automatic sharpness/redundancy selection followed by coverage review. Low-detail context can use fewer views; metric reconstruction requires observed coverage and independent controls.

Candidate selection and merge: Frame-density/selection candidates share source stream and intended view coverage; camera groups/resources explicit. VLM compares original interval/viewpoint evidence; software reports timing/quality/coverage statistics. Combine unique original frames with exact source mapping; generated/interpolated views retain separate evidence class. Recheck duplicates, timing, camera groups and coverage of the new dataset.

Software migration: Automate demonstrated codec/camera classes after variable-rate, rotated frames, motion, blur and lost-timeline fixtures.

Future cases: Variable-rate clip preserves original presentation timestamps rather than index/fixed-fps guess. Frame interpolation is labelled generated and cannot act as independent measured view. Sparse sampling omits a viewpoint bridge and triggers dataset coverage exception.

## 4. REC-03 — Estimate camera poses and sparse structure from overlapping photos

[Original contract](../workflows/reconstruction-paths.json): **photo-set → camera-solution AND point-cloud**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-03-A01 — Bind image identities calibration groups and sparse-solve settings.** (1) Pin dataset and camera groups. (2) Bind image transforms to intrinsic/distortion convention. (3) Reserve independent views/controls and choose sparse settings. Output: Dataset/camera-group manifest, fit/check split and sparse configuration. Check: Photo-only input permits arbitrary-scale reconstruction; original scale-control checks apply only when linked metric evidence exists.

1. **REC-03-A02 — Estimate sparse cameras and points with retained hypotheses.** (1) Extract features and match declared image pairs. (2) Estimate cameras/points under recorded calibration-refinement policy. (3) Retain components, track associations and alternative hypotheses. Output: Feature/match database, camera poses/intrinsics, sparse points and reconstruction components. Store COLMAP image poses as world→camera Hamilton (qw,qx,qy,qz) plus translation and preserve source image/camera IDs. Check: Camera database/model readback matches image dimensions/model parameters; disconnected components keep independent frames.

1. **REC-03-A03 — Validate camera coverage and scale evidence.** (1) Check camera/track coverage and source correspondence. (2) If metric use is requested, solve named control transform and test withheld controls. (3) Publish exact sparse outputs and remaining component/scale states. Output: Checked sparse model, normalized pose convention, control/coverage report and scale transform if supported. Check: Calibration target units alone do not scale an unrelated photo object; two scale lengths do not automatically determine full spatial datum.

Existing entrypoints and proposed helper interfaces:

1. **REC-03-A01.** Software: Inspect images and camera models; map calibration through verified adapter; group shared intrinsics only for documented shared state. COLMAP +0.5 principal-point correction is conditional on actual source/destination pixel conventions; read back saved camera model/parameters. Proposal: SfM intake emits per-image camera/model/mask records and explicit scale status.

1. **REC-03-A02.** Software: Use documented feature_extractor, chosen matcher and mapper or selected equivalent; preserve raw components and bundle-adjustment calibration policy. Proposal: sparse runner emits database/model/settings plus registered/unregistered-image and component reports.

1. **REC-03-A03.** Software: Inspect registered-view/component coverage, residual distribution and poses; apply sourced similarity/scale only with sufficient controls and reserve independent checks. Proposal: sparse verifier emits per-camera/component readiness, control residuals and explicit arbitrary/metric scale state.

Execution choices:

1. **Agent directs.** Agent interprets camera/source ambiguity and directs solve.

1. **Software and agent.** Software estimates/readbacks; agent reviews components/controls.

1. **Software ordinary cases.** Checked capture classes solve with disconnected/degenerate/calibration exceptions.

1. **Complete software procedure.** Pinned dataset/camera configuration and supported algorithm produce reproducible sparse candidate/check records.

Alternatives and target detail: COLMAP sparse route with explicit calibration policy. Separate Meshroom/OpenMVG route with its actual camera representation. Arbitrary-scale context reconstruction versus metric working references uses distinct control requirements.

Candidate selection and merge: Sparse backend/camera-model candidates share captured dataset and reserved controls but retain solver/settings lineage. VLM checks physical track/region meaning; software compares independent projections, connectivity and control residuals. Select coherent camera model/component; cross-component merge requires explicit registration evidence. Reproject retained observations and repeat independent control, camera-group and scale checks.

Software migration: Automate checked camera/capture classes after pixel convention, repeated texture, low baseline, calibration drift and disconnected-component fixtures.

Future cases: Unrelated calibration board size cannot silently set scene scale. All views rotate around one centre: weak depth observability remains explicit. Two disconnected sparse components retain separate frames until supported registration. Withheld control used in scale fit is detected as evaluation leakage.

## 5. CAD-16 — Reconstruct camera poses and dense visible geometry from overlapping photos

[Original contract](../workflows/cad-paths.json): **photo-set AND measurement-set → camera-solution AND point-cloud AND mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **CAD-16-A01 — Bind complete photo and metric-control contract.** (1) Pin photos and measurement-set. (2) Map fit controls versus independent checks. (3) Set frame, feature coverage and camera/cloud/mesh output requirements. Output: Dataset/control/frame plan selecting sparse and dense stages. Check: Original contract requires all three outputs; inferred hidden geometry retains its evidence label.

1. **CAD-16-A02 — Compose sparse and dense visible-surface reconstruction.** (1) Complete checked sparse camera/scale stage. (2) Compute selected dense/fusion surface route. (3) Retain separate cloud/mesh outputs and source/transform records. Output: Stage receipts and all three actual output artifacts with common source/scale/frame lineage. Check: Sparse cloud alone cannot satisfy dense/mesh target; meshing/filling cannot promote hidden regions to observations.

1. **CAD-16-A03 — Validate metric reference and saved three-output package.** (1) Read all three saved artifacts. (2) Compare independent controls and source-supported geometry coverage. (3) Publish complete outputs with observed/inferred and use-specific states. Output: Camera-solution, point-cloud and mesh with per-feature metric/coverage/readback results. Check: Appearance agreement alone cannot qualify working interfaces or hidden dimensions.

Existing entrypoints and proposed helper interfaces:

1. **CAD-16-A01.** Software: Validate capture/calibration through REC-03 intake and measurements through point01/05 contracts. Proposal: reconstruction planner emits source/control plan and prerequisites for all three outputs.

1. **CAD-16-A02.** Software: Run REC-03 sparse checks, then REC-17/DOM-28 dense cloud and mesh stages only when prerequisites pass. Proposal: stage composer links immutable sparse/dense/mesh receipts and common metric transform.

1. **CAD-16-A03.** Software: Reopen outputs; compare camera/image consistency, controls, cloud/mesh distances, holes/outliers and frame propagation. Proposal: package verifier emits each output's actual type/source/frame and feature-readiness report.

Execution choices:

1. **Agent directs.** Agent interprets controls/coverage and directs composed stages.

1. **Software and agent.** Software reconstructs/measures; agent reviews source and hidden-region meaning.

1. **Software ordinary cases.** Demonstrated capture/control classes run with camera/coverage/output exceptions.

1. **Complete software procedure.** Explicit supported dataset/settings/controls produce repeatable three-output package.

Alternatives and target detail: Calibrated RGB-D with independent controls when suitable. Separate COLMAP/OpenMVS or Meshroom reconstruction branches. Context mesh can retain incomplete surfaces; working CAD reference requires per-feature dimensional/coverage evidence.

Candidate selection and merge: Camera/dense alternatives share photos and independent controls with explicit detail/resource targets. VLM reviews observed feature association; software checks control residuals and surface consistency. Select compatible camera/surface evidence; cross-backend merge needs common source/frame and retained uncertainty. Reopen final three-output package and repeat camera, scale, feature and independent semantic checks.

Software migration: Automate checked capture/control/backend combinations after scale, missing mesh, occlusion, symmetry and partial-stage recovery fixtures.

Future cases: Camera/cloud produced but mesh stage fails: complete CAD-16 handoff remains partial. Mesh fills unseen underside; region stays inferred and cannot pass measurement evidence. Dense result improves appearance while withheld interface error worsens; feature criterion controls readiness.

## 6. REC-05 — Register RGB and depth frames and estimate sequence poses

[Original contract](../workflows/reconstruction-paths.json): **depth-frames → camera-solution AND point-cloud**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-05-A01 — Bind sensor calibration timing and depth encoding.** (1) Pin raw frames/calibration and timing. (2) Decode depth scale/range/invalid conventions. (3) Check RGB-depth registration and pose-source prerequisites. Output: Per-frame sensor/calibration/time manifest and alignment/validity plan. Check: Depth numeric values require declared divisor/units; different clocks/extrinsics cannot be treated as aligned frames.

1. **REC-05-A02 — Estimate or import sequence poses and projected samples.** (1) Project valid calibrated depth samples. (2) Estimate/import named sequence transforms. (3) Compose trajectory under one documented convention and retain failures. Output: Per-frame poses, relative transforms, projected samples and success/overlap diagnostics. Check: A successful local fit does not remove global drift; missing intervals remain explicit.

1. **REC-05-A03 — Validate trajectory and metric depth independently.** (1) Compare independent range and scene controls. (2) Inspect trajectory/loop consistency and excluded regions. (3) Publish poses/cloud with supported intervals and uncertainty. Output: Checked outputs with scale/frame, drift, coverage and control results. Check: Sensor metric scale does not guarantee dimensional accuracy or drift-free trajectory.

Existing entrypoints and proposed helper interfaces:

1. **REC-05-A01.** Software: Decode stated depth representation; inspect synchronization/image sizes; preserve invalid masks and calibrated registration parameters. Open3D v0.20.0 RGBDImage.h declares defaults; Image.cpp divides raw depth by depth_scale and zeros >= depth_trunc. Use sensor-specific settings, invalid mask and axial-versus-ray-range convention. Proposal: RGB-D intake emits calibrated frame pairs, depth units/validity and source-to-target camera mapping.

1. **REC-05-A02.** Software: Use supported RGB-D odometry or imported sensor/survey poses; project valid depth using matching intrinsics and preserve transform direction at each boundary. compute_rgbd_odometry returns success, pairwise 4x4 motion and 6x6 information; verify selected adapter direction before composing trajectory. Proposal: pose adapter emits pairwise/source-to-world transforms, sample IDs and failed intervals.

1. **REC-05-A03.** Software: Read back trajectory/points; test transform inverses, range bias, loop closure and distributed controls. Proposal: trajectory verifier emits per-segment control/drift and output-readiness records.

Execution choices:

1. **Agent directs.** Agent interprets sensor evidence and directs pose recovery.

1. **Software and agent.** Software aligns/projects/estimates; agent reviews dynamic/overlap ambiguity.

1. **Software ordinary cases.** Checked sensor/capture classes process with calibration/timing exceptions.

1. **Complete software procedure.** Explicit calibration/pose inputs and supported algorithm yield repeatable source-linked outputs.

Alternatives and target detail: Use recorded hardware trajectory with source convention. Use surveyed poses or checked RGB-D odometry. Context cloud versus working measurement reference has different control/drift requirements.

Candidate selection and merge: Pose/calibration candidates share raw frames and independent controls; source conditions/resources recorded. VLM reviews physical/dynamic regions; software compares range, pose and control residuals. Select compatible segments with explicit bridge transforms; preserve conflicting trajectories. Reproject/recheck raw-frame samples, drift and independent controls under merged trajectory.

Software migration: Automate demonstrated sensors after unit divisor, invalid depth, asynchronous RGB/depth, pose inversion and drift fixtures.

Future cases: Depth divisor error creates coherent but wrong scale; known-range check fails. RGB and depth timestamps mismatch at moving edge; registration is rejected/segmented. Source-to-target pose composed backwards fails independent trajectory/control check.

## 7. REC-06 — Integrate calibrated RGB-D frames into point cloud or TSDF mesh

[Original contract](../workflows/reconstruction-paths.json): **depth-frames AND camera-solution → point-cloud AND mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-06-A01 — Resolve fusion grid and pose convention.** (1) Match each frame to calibration/pose revision. (2) Convert poses to exact integration convention. (3) Set source-backed voxel/truncation/range criteria and protected features. Output: Integration manifest with frame order, world frame, validity masks and grid settings. Check: Depth truncation and signed-distance truncation are separate quantities; no implicit unit/default conversion.

1. **REC-06-A02 — Integrate observations and extract explicit geometry.** (1) Integrate valid frames in recorded order/convention. (2) Extract required cloud and mesh separately. (3) Retain source support, interpolation and excluded-region records. Output: TSDF state or replay receipt, extracted cloud and mesh, observation/support metadata. Check: Empty volume or cloud-only extraction leaves required outputs partial; interpolated closure remains inferred.

1. **REC-06-A03 — Compare fusion candidates and independent controls.** (1) Measure saved outputs against independent controls. (2) Compare source-supported surfaces and bounded voxel alternatives. (3) Publish both artifacts with use-specific readiness. Output: Cloud/mesh metric, drift, coverage and source/readback report. Check: Smaller voxel or lower fit residual does not automatically improve measured accuracy.

Existing entrypoints and proposed helper interfaces:

1. **REC-06-A01.** Software: Use explicit world→camera integration extrinsics. The tutorial uses inverse(camera_pose) for its camera-to-world input; invert only the actual opposite-direction input. Check matching image/intrinsic/pose revisions, depth units and bounded region. Proposal: fusion preflight emits per-frame integration transform and units/settings receipt.

1. **REC-06-A02.** Software: Use ScalableTSDFVolume integration and supported cloud/triangle extraction; retain exact grid/range/pose settings and filled/unobserved-region classification. Proposal: fusion runner emits both geometry types and frame-to-surface/support evidence or documented mapping limits.

1. **REC-06-A03.** Software: Reopen outputs; compare independent controls and directed sample/surface residuals; inspect holes, double walls and protected features. Proposal: verifier reports per-feature/control error, coverage and approximation changes across settings.

Execution choices:

1. **Agent directs.** Agent selects observation scope and directs fusion.

1. **Software and agent.** Software integrates/extracts/checks; agent reviews inferred surfaces.

1. **Software ordinary cases.** Checked calibrated sequences run with pose/range/coverage exceptions.

1. **Complete software procedure.** Complete compatible frames/poses/settings produce deterministic supported fusion outputs.

Alternatives and target detail: Accumulate source-linked clouds without TSDF when surface interpolation is unnecessary. Use sensor-native mesh with independent source/readback evidence. Context surface and working interface mesh retain different coverage/accuracy requirements.

Candidate selection and merge: Voxel/truncation/pose candidates share raw data and reserved controls with declared detail/resource targets. VLM checks source surface identity; software compares controls, coverage and regional residuals. Choose coherent volume/settings or explicitly registered compatible regions with source lineage. Recheck source projections, independent dimensions, holes and required two-output readback.

Software migration: Automate tested calibration/scene classes after inverse extrinsic, depth scale, empty volume, duplicate integration and thin-feature fixtures.

Future cases: Wrong pose inverse creates double surface and fails raw-frame/control checks. Depth range cutoff differs from TSDF truncation and remains separately configured. Changing voxel size preserves controls for comparison; fine-grid noise can fail interface criterion. Lost integration acknowledgement cannot replay a frame twice without reconciliation.

## 8. DOM-21 — Depth frames to registered point cloud or mesh

[Original contract](../workflows/domain-paths.json): **depth-frames AND measurement-set → point-cloud**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-21-A01 — Bind mandatory depth and measurement evidence.** (1) Pin frames and measurement-set. (2) Map physical controls and pose source. (3) Define registered-cloud frame and target features. Output: Control/calibration/frame plan for registered point-cloud. Check: Original output is point-cloud; mesh title wording is recorded as a separate downstream branch.

1. **DOM-21-A02 — Project register and publish source-linked cloud candidate.** (1) Project and register valid samples. (2) Apply recorded filtering/accumulation or fusion. (3) Write cloud and calibration/pose/control mapping. Output: Registered point-cloud and point/frame/filter/transform lineage. Check: Filtered points remain traceable; mesh generation is not required to fulfill this typed output.

1. **DOM-21-A03 — Check registered cloud controls and source coverage.** (1) Reopen cloud and verify frame/units. (2) Compare independent measured controls. (3) Publish cloud and explicit downstream mesh/appearance dependencies. Output: Control/drift/coverage report and registered point-cloud. Check: Sensor units or plausible bounds cannot replace independent dimensional checks.

Existing entrypoints and proposed helper interfaces:

1. **DOM-21-A01.** Software: Validate sensor data through REC-05 intake; resolve metric frame controls and required coverage. Proposal: depth-domain intake emits mandatory-input receipt and point-cloud prerequisites.

1. **DOM-21-A02.** Software: Compose REC-05 projection/poses and supported cloud accumulation/fusion; optional REC-06 route retains its separate mesh output. Proposal: depth-cloud composer emits actual cloud, source membership and removed/inferred-region ledger.

1. **DOM-21-A03.** Software: Compare known lengths/targets, local residuals, loop/drift and excluded regions; verify units/transform application. Proposal: registered-cloud checker emits per-feature metric/coverage and lineage results.

Execution choices:

1. **Agent directs.** Agent maps measurements and directs sensor/cloud stages.

1. **Software and agent.** Software projects/registers/checks; agent reviews control identity.

1. **Software ordinary cases.** Checked sensor/control classes process with uncertainty/coverage exceptions.

1. **Complete software procedure.** Complete calibrated frames/poses/controls produce checked point-cloud.

Alternatives and target detail: Per-frame or accumulated cloud when fusion adds no required value. REC-06 explicit TSDF mesh branch or DOM-29 cloud meshing. Layout scan and working dimensional reference retain different control/coverage criteria.

Candidate selection and merge: Cloud processing candidates share raw depth and control revisions; filtering/detail targets recorded. VLM examines sample/feature identity; software compares independent control/drift and coverage. Combine compatible registered segments with retained source maps and overlap rules. Recheck common frame, duplicate/removed points and independent controls.

Software migration: Automate demonstrated sensor/control pipelines after missing mandatory measurements, depth units, drift and source-loss fixtures.

Future cases: Missing measurement-set cannot be silently bypassed by sensor metric claim. Cloud succeeds without mesh and fulfills original typed output. Filtering removes required small feature; coverage/feature check fails.

## 9. REC-17 — Build dense point cloud and mesh from SfM camera solution

[Original contract](../workflows/reconstruction-paths.json): **photo-set AND camera-solution → point-cloud AND mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-17-A01 — Validate sparse-to-dense image and camera handoff.** (1) Verify supplied image/camera revisions. (2) Create documented undistorted workspace without losing source mappings. (3) Select bounded dense settings and supported backend. Output: Undistorted image/camera workspace and dense-backend/settings plan. Check: Undistorted intrinsics and pixels must agree; a sparse camera model carries its own arbitrary/metric scale status.

1. **REC-17-A02 — Estimate dense depth and fuse visible samples.** (1) Estimate depth for declared view neighbors. (2) Check consistency and fuse supported samples. (3) Retain unfused/invalid regions and source-camera lineage. Output: Per-view dense depth/confidence and fused cloud with camera/settings lineage. Check: Empty or sparse-only cloud cannot satisfy declared dense coverage; fusion creates no mesh output.

1. **REC-17-A03 — Mesh dense cloud and validate both outputs.** (1) Create mesh through explicit supported meshing stage. (2) Reopen cloud/mesh and compare source support, protected features and controls. (3) Publish both outputs with coverage and approximation records. Output: Actual cloud and triangle mesh plus source/approximation/readback report. Check: Successful fusion alone cannot satisfy mesh contract; same captures produce dependent evidence, not independent truth.

Existing entrypoints and proposed helper interfaces:

1. **REC-17-A01.** Software: Read sparse model and verify image/model pairing; use image_undistorter with documented output convention; inspect selected dense backend/build. Proposal: dense intake emits source-to-undistorted image/camera map and compatible workspace receipt.

1. **REC-17-A02.** Software: COLMAP patch_match_stereo then stereo_fusion, or InterfaceCOLMAP→DensifyPointCloud under documented image/camera bridge; preserve selected backend differences. Proposal: dense runner emits depth/fusion artifacts and source support/coverage manifest.

1. **REC-17-A03.** Software: Use supported COLMAP poisson_mesher/delaunay_mesher or OpenMVS ReconstructMesh with actual cloud input; inspect normals/holes/components and compare mesh/cloud/controls. Proposal: dense-output publisher emits both typed artifacts with per-feature observed/inferred status.

Execution choices:

1. **Agent directs.** Agent interprets coverage and directs dense/mesh stages.

1. **Software and agent.** Software reconstructs/checks; agent reviews inferred regions.

1. **Software ordinary cases.** Checked image/camera/backend classes run with hardware/coverage/mesh exceptions.

1. **Complete software procedure.** Explicit compatible workspace/settings produce repeatable supported cloud/mesh results.

Alternatives and target detail: COLMAP stereo/fusion plus explicit mesher. OpenMVS importer/densify/reconstruct route with actual camera bridge. Measured RGB-D route where appropriate; context mesh and working surface reference have distinct feature criteria.

Candidate selection and merge: Dense backend/resolution candidates share camera/input/control revisions with separate resource/detail targets. VLM reviews source-visible feature support; software compares controls, dense coverage and mesh residuals. Choose compatible surfaces with common frames and lineage; keep seams and inferred regions explicit. Recheck source projections, protected features, independent dimensions and both saved outputs.

Software migration: Automate tested dense/import/meshing classes after mismatched cameras, empty fusion, missing mesh, hardware and seam fixtures.

Future cases: Cloud fusion succeeds but mesher fails: cloud retained, combined output partial. Sub-scene meshing creates a seam at required interface and fails local comparison. Image IDs match names but hashes/calibration differ; dense preflight rejects stale workspace.

## 10. DOM-28 — Dense multi-view stereo to point cloud and mesh

[Original contract](../workflows/domain-paths.json): **photo-set AND camera-solution → point-cloud AND mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-28-A01 — Bind supplied cameras and required surface outputs.** (1) Bind exact photo/camera pair. (2) Record scale/frame and required features. (3) Select compatible dense and mesh stages. Output: Camera/image/frame validation receipt and both-output requirements. Check: Calibrated intrinsics alone do not establish unrelated scene scale.

1. **DOM-28-A02 — Compose dense estimation fusion and meshing.** (1) Run compatible dense depth/fusion. (2) Run explicit supported meshing. (3) Retain per-stage artifacts and common source/frame lineage. Output: Both artifacts plus per-stage depth/fusion/mesh/settings receipts. Check: Names/format suffixes cannot substitute actual dense samples and triangle faces.

1. **DOM-28-A03 — Check source geometry and independent controls.** (1) Check actual saved geometry types and frame. (2) Compare independent controls/protected features. (3) Publish both outputs and their use-specific evidence. Output: Coverage, frame, geometric residual and per-feature readiness report. Check: Rendered surface plausibility cannot pass metric or occluded-feature requirement.

Existing entrypoints and proposed helper interfaces:

1. **DOM-28-A01.** Software: Reuse REC-17 workspace preflight; inspect backend output types and required coverage. Proposal: domain dense planner emits image/camera/settings and cloud/mesh dependency graph.

1. **DOM-28-A02.** Software: Execute REC-17 supported stages; preserve exact mesher and nonempty/output-type checks. Proposal: domain composer links dense/cloud/mesh stages without treating one output as another.

1. **DOM-28-A03.** Software: Reopen and compare required interfaces, holes/components, source projection and cloud/mesh residuals. Proposal: dense-domain verifier emits output-completeness and source/metric findings.

Execution choices:

1. **Agent directs.** Agent interprets domain surface requirements and directs stages.

1. **Software and agent.** Software reconstructs/reads/measures; agent reviews inference/coverage.

1. **Software ordinary cases.** Checked dense pipeline families process with explicit stage/output exceptions.

1. **Complete software procedure.** Compatible fixed inputs/settings yield reproducible two-output package.

Alternatives and target detail: COLMAP dense chain with explicit mesh stage. OpenMVS/Meshroom route with documented handoff and actual outputs. Sensor-depth or appearance-scene branch has a separately typed contract.

Candidate selection and merge: Domain dense candidates share source/camera/control revisions and state distinct detail/resource criteria. VLM evaluates source-visible features; software compares saved geometry and independent controls. Select compatible cloud/mesh pair or source-linked regions; retain cross-method dependencies. Repeat frame, two-output completeness, source and per-feature independent checks.

Software migration: Automate demonstrated data/backend classes after arbitrary scale, omitted mesher, disconnected coverage and source revision fixtures.

Future cases: Sparse cloud mislabeled dense fails required coverage. Mesh output absent retains partial domain handoff. Scale transform applied to mesh but not cloud fails common-frame check.

## 11. DOM-29 — Point cloud to surface mesh

[Original contract](../workflows/domain-paths.json): **point-cloud → mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-29-A01 — Inspect point evidence normals and meshing assumptions.** (1) Inspect actual point representation and source evidence. (2) Select/filter regions with original IDs. (3) Prepare method-specific normals and closure assumptions. Output: Method/normal/filter plan and source-point membership map. Check: Gaussian PLY centers/covariances/opacity require separately defined surface extraction before this geometry route.

1. **DOM-29-A02 — Reconstruct surface and retain every cleanup derivative.** (1) Run selected reconstruction with recorded parameters. (2) Label supported versus extrapolated surface regions. (3) Apply explicitly scoped cleanup/decimation as new derivatives. Output: Raw reconstructed mesh, optional cleaned/decimated variants and point/region source map. Check: Closed-looking Poisson surface can include inferred empty-space closure; triangle target is not error guarantee.

1. **DOM-29-A03 — Compare surface and protected features to source.** (1) Read actual final mesh and compare with raw reconstruction. (2) Measure protected features and both directed source residuals. (3) Check independent controls/capture projection and publish evidence. Output: Directed residual, coverage, topology and feature-readback reports. Check: Bounds/volume and low one-way residual cannot pass overfilled gaps or lost thin features.

Existing entrypoints and proposed helper interfaces:

1. **DOM-29-A01.** Software: Inspect PLY/other fields; reject Gaussian rendering parameters as measured surface cloud; estimate/orient normals where method requires and retain neighborhood settings. Open3D orient_normals_consistent_tangent_plane(k) propagates neighbour consistency; check outward/side orientation against capture evidence separately. Proposal: meshing intake emits validated geometric point set, normal lineage and method prerequisites.

1. **DOM-29-A02.** Software: Open3D create_from_point_cloud_poisson takes an oriented point cloud and returns mesh plus density; create_from_point_cloud_ball_pivoting takes oriented cloud and length-unit radii. simplify_quadric_decimation targets triangle count with stated maximum_error/boundary_weight; retain original mesh and measure actual feature deviation. Proposal: surface adapter emits raw mesh plus independent cleanup derivatives and change/support ledger.

1. **DOM-29-A03.** Software: Compare cloud→mesh and mesh→cloud with sampling/direction reported; query holes/components/normals and required passages; reproject to original captures when available. Proposal: mesh checker emits per-feature before/after deviation, topology/coverage and downstream-readiness results.

Execution choices:

1. **Agent directs.** Agent selects surface meaning/method and directs cleanup.

1. **Software and agent.** Software reconstructs/measures; agent reviews inferred closure.

1. **Software ordinary cases.** Checked cloud/method classes run with normals/coverage/type exceptions.

1. **Complete software procedure.** Explicit geometric samples/settings/criteria produce supported mesh and change ledger.

Alternatives and target detail: Poisson for suitable oriented coverage with extrapolation evidence. Ball pivoting for supported sampled surfaces. Retain cloud or separate measured CAD remodeling when surface fill lacks evidence; context/working meshes have distinct criteria.

Candidate selection and merge: Meshing/normal/cleanup candidates share source sample IDs and protected controls with different detail targets. VLM reviews observed surface context; software compares directional residuals, topology and features. Select compatible regions/mesh version with explicit seams and inference labels. Repeat topology, source support, protected-feature and independent-control checks on saved mesh.

Software migration: Automate demonstrated sampling/method classes after normal flips, open gaps, Gaussian-type mismatch, thin features and cleanup regressions.

Future cases: Gaussian PLY shares extension with point cloud but fails geometric source-type preflight. Decimation preserves bounds yet closes a passage; feature check fails. Inconsistent normals cause false surface sheet and fail source/coverage check. Low cloud→mesh error with large inferred back surface is exposed by reverse coverage/inference records.

## 12. DOM-20 — Photos/video to camera solution, point cloud and mesh

[Original contract](../workflows/domain-paths.json): **photo-set → camera-solution AND point-cloud**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-20-A01 — Resolve literal photo input and cloud detail target.** (1) Verify actual photo-set input. (2) Declare sparse or dense cloud target. (3) Bind camera/scale evidence and output coverage criteria. Output: Input/quality/frame plan and camera/cloud output specification. Check: Title's video/mesh wording does not alter photo-set→camera-solution+point-cloud contract.

1. **DOM-20-A02 — Recover cameras and the declared cloud representation.** (1) Estimate/check sparse camera geometry. (2) Generate declared cloud detail through supported stages. (3) Save exact camera/cloud artifacts and frame mappings. Output: Camera-solution plus explicitly sparse/dense point-cloud with stage/source receipts. Check: Mesh is not required output; absent camera or cloud remains partial.

1. **DOM-20-A03 — Validate saved domain outputs and downstream conditions.** (1) Reopen cameras and cloud. (2) Compare source/camera coverage and applicable independent controls. (3) Publish original outputs with explicit downstream transitions. Output: Camera/coverage/source/frame report and use-specific outputs. Check: Cloud/file format cannot be substituted by Gaussian parameters or scene checkpoint.

Existing entrypoints and proposed helper interfaces:

1. **DOM-20-A01.** Software: Validate images/camera model through REC-03; require prior video extraction if original source is video. Proposal: domain photo intake distinguishes typed photo input from video upstream and mesh downstream dependencies.

1. **DOM-20-A02.** Software: Compose REC-03; add supported dense sampling only when declared, preserving actual cloud type; mesh remains explicit REC-17/DOM-28 branch. Proposal: photo-domain composer emits camera/cloud and typed optional-stage ledger.

1. **DOM-20-A03.** Software: Verify image/pose mapping, component coverage, cloud detail and scale/frame; apply independent controls as required. Proposal: photo-domain verifier emits exact-output and downstream mesh/metric prerequisites.

Execution choices:

1. **Agent directs.** Agent interprets capture/detail target and directs reconstruction.

1. **Software and agent.** Software solves/checks; agent reviews source correspondence.

1. **Software ordinary cases.** Checked capture classes process with camera/coverage exceptions.

1. **Complete software procedure.** Explicit supported photo/configuration contract yields typed cameras/cloud.

Alternatives and target detail: Sparse camera/cloud for initial context. Dense cloud with explicit additional stage. Video uses REC-04 first; mesh uses REC-17/DOM-28; working metric use requires its controls.

Candidate selection and merge: Sparse/dense/backend candidates share source photos and declared camera/control evidence. VLM reviews captured feature associations; software compares coverage/pose/control reports. Choose coherent camera/cloud representation at declared detail; preserve other branches separately. Read saved outputs and repeat camera/source/frame and applicable metric checks.

Software migration: Automate demonstrated photo/dataset classes after video-input, cloud-detail, disconnected component and output-type fixtures.

Future cases: Video file alone cannot satisfy photo-set without explicit extraction receipt. Cameras+sparse cloud can satisfy declared sparse target without mesh. A Gaussian PLY cannot silently satisfy point-cloud output semantics.

## 13. REC-10 — Estimate multi-view depth, camera poses and Gaussian outputs

[Original contract](../workflows/reconstruction-paths.json): **one alternative: photo-set OR video → camera-solution AND point-cloud**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-10-A01 — Bind learned reconstruction variant, images and camera roles.** (1) Identify the actual checkpoint and source input class. (2) Bind image transforms, masks, camera roles and control partitions. (3) Record the required camera/cloud exports and feature criteria. Output: Inference manifest with source/generated origin, variant/checkpoint hash, processed image mapping, supplied-versus-estimated camera policy, output names and scale status. Check: Check literal one-of input, all files/revisions, rights references and actual model export contract; a GLB-only example cannot complete camera-solution plus point-cloud.

1. **REC-10-A02 — Estimate depth and cameras and materialize the declared cloud.** (1) Run the scoped inference into a new result revision during future execution. (2) Decode actual output fields and retain depth/sample-to-image correspondence. (3) Materialize both camera and geometric-cloud artifacts with explicit frame/scale and optional-product separation. Output: Camera-solution, point-cloud, per-frame depth/confidence where enabled, raw model output and export receipt; optional Gaussian output stays a separate typed derivative. Check: Read back every camera/image match, matrix direction and finite valid sample; detect missing camera export, arbitrary scale and Gaussian attributes before classifying a PLY as geometric samples.

1. **REC-10-A03 — Compare predictions with independent controls and conventional candidates.** (1) Align candidates using named fit evidence and freeze the transform. (2) Compare withheld controls and captured-view features. (3) Select or retain alternatives, then independently validate the selected/new merged revision. Output: Per-feature comparison report, selected candidate or unresolved alternatives, camera/cloud handoff and independent semantic review. Check: Both typed outputs exist; independent checks use reserved controls; inferred hidden regions retain inferred status; same-source predictions do not count as independent acquisitions. Card-only focal conversion ambiguity blocks a metric claim until the actual adapter's units/recipe are checked.

Existing entrypoints and proposed helper interfaces:

1. **REC-10-A01.** Software: Inspect selected DA3 entrypoint/version, export settings and checkpoint support; streaming configuration must actually emit intrinsics/poses plus cloud to fulfill this operation. PROPOSAL learned-input planner: image/video manifest + selected model card/config → exact input/output manifest, camera policy, expected coordinate/scale record and blocked conditions.

1. **REC-10-A02.** Software: Use documented DA3 photo/video or streaming route; read raw camera arrays/conventions and cloud attributes, apply a recorded transform only once. Discover release-specific output schema before interpreting it. DA3Metric-Large card fields are depth/confidence [N,H,W], W2C extrinsics [N,3,4] and K [N,3,3]; actual selected API metric/focal conversion must be established without inventing a card-missing divisor or converting twice. PROPOSAL DA3 result adapter: raw depth/camera/confidence exports + image/config manifest → named camera records, typed geometric cloud, frame/scale receipt and partial-output status.

1. **REC-10-A03.** Software: Project/reproject sampled geometry through actual cameras; align only using designated fit controls; calculate withheld distances and source-region differences with typed cloud readers. PROPOSAL prediction comparison ledger: predicted and conventional candidates + fit/check partition → regional errors, selection reasons, common dependencies and per-feature readiness.

Execution choices:

1. **Agent directs.** Reasoning agent proposes variants, masks and source-feature interpretations; software executes/checks the selected supported route.

1. **Software and agent.** Agent fixes identity/control associations; software performs inference, export decoding and numerical checks with exception review.

1. **Software ordinary cases.** A recognized model/input/export class runs automatically; ambiguous camera fields, missing output, scale or confidence meaning returns to the agent.

1. **Complete software procedure.** A pinned model/config/dataset reruns a tested adapter with reproducibility settings and numerical checks; model determinism is measured for that backend, not assumed.

Alternatives and target detail: Sparse CPU photogrammetry for minimum camera/coverage evidence; DA3 predicted context for a selected subset; full learned multi-view candidate for stated regions; independent MVS or calibrated-depth surface for working features.

Candidate selection and merge: Give learned and conventional branches their exact variant, image subset, intended detail, feature coverage, scale/control and resource records. VLM chooses supported feature correspondence using original images and measured report; independent reviewer checks semantic choice. Combine camera/cloud revisions only through a documented common-frame mapping and compatible sample provenance; preserve learned and observed region labels. Re-read cameras and cloud, repeat affected withheld controls/coverage and review seam/identity semantics.

Software migration: PROPOSAL migrate export decoding, camera convention and per-region checks after checked fixtures for each exact DA3 variant/output class; retain agent routing for unsupported schema, generated regions and ambiguous feature meanings.

Future cases: Metric versus relative checkpoint on same data preserves separate scale claims; GLB-only export stays partial; confidence score with biased depth cannot become a dimensional error bound; streaming missing chunk and changed overlap preserve coverage gaps; Gaussian PLY presented as a cloud is rejected by typed adapter.

## 14. REC-18 — Generate a single-image mesh proxy

[Original contract](../workflows/reconstruction-paths.json): **photo-set → mesh**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-18-A01 — Select one source image and a mesh-producing model contract.** (1) Select and hash the one source image and mask. (2) Match the chosen model to a triangle-mesh output contract. (3) Record visible evidence, hidden-region interpretation and scope criteria. Output: Single-image generation manifest with mask/preprocessing, generated-region policy, model/output contract and resource conditions. Check: Input selection remains explicit; actual source image rather than a rendered substitute is identified; unsupported Gaussian-only output cannot satisfy mesh.

1. **REC-18-A02 — Generate and preserve the proxy mesh and its coordinate frame.** (1) Generate to a new revision under the selected configuration. (2) Save the original returned mesh before any editing. (3) Decode its actual topology, scale/frame and materials into a typed mesh receipt. Output: Generated triangle mesh, optional texture/materials, raw model output, bounds/frame/unit-status and generation receipt. Check: Read back face indices, finite coordinates, normals, bounds/material references and actual mesh payload; a preview image or Gaussian file is a partial output.

1. **REC-18-A03 — Evaluate visible fit and gate geometric reuse by independent evidence.** (1) Compare visible source projections and independent measurements separately. (2) Select source-supported candidates and retain hidden alternatives. (3) Recheck the selected mesh revision and issue a use-specific handoff. Output: Proxy evaluation, visible/inferred feature map, selected candidate and scoped handoff to point-05 remodeling or visual context. Check: Generated back views of the candidate count as internal visualization; independent capture/control IDs are preserved; mesh validity alone cannot pass dimensional requirements.

Existing entrypoints and proposed helper interfaces:

1. **REC-18-A01.** Software: Inspect exact model interface/checkpoint/output and preprocessing; TRELLIS.2 pipeline returns mesh and optional GLB; keep SAM Gaussian route outside a direct mesh completion claim. PROPOSAL proxy-input planner: chosen image/mask + model specification + intended use → generation request, output type and visible/inferred region map.

1. **REC-18-A02.** Software: Future adapter invokes selected documented model, records raw mesh and texture outputs, reads vertices/faces/material references and export axes; save derivative before optional cleanup. PROPOSAL proxy exporter: raw model result + input/config receipt → mesh/material package, frame/normalization map and per-region generated lineage.

1. **REC-18-A03.** Software: Render under the matched camera, compare original-pixel masks and measured controls; run mesh validity/local topology checks before reuse. PROPOSAL proxy qualification ledger: mesh + actual capture/control evidence → feature readiness by intended use, candidate selection and remodeling requirements.

Execution choices:

1. **Agent directs.** Agent interprets target/mask and compares proxy candidates; software generates mesh and computes checks.

1. **Software and agent.** Agent supplies source-feature and use decisions; software executes pinned generator, export/readback and projection checks.

1. **Software ordinary cases.** Recognized object/mask and direct mesh backend produce a candidate; unsupported output/occlusion/scale requirements trigger reasoning review.

1. **Complete software procedure.** Pinned image/mask/checkpoint/config supports a repeatable fixture-tested proxy adapter; numerical equality depends on tested inference/backend settings.

Alternatives and target detail: Single-image context proxy; multi-image conventional reconstruction when real views exist; measured CAD remodeling for working interfaces; image+mask Gaussian appearance branch keeps its own output type.

Candidate selection and merge: Record exact source image, mask, variant, intended-use/detail and generated-region labels for each proxy; record common checkpoint dependencies. VLM selects visible feature agreement supported by original source and controls; separate reviewer checks claims about hidden surfaces. Compatible texture/geometry packaging preserves source mapping; cross-candidate geometry edits become a new authored mesh with explicit modeling scope and lineage. Recheck topology, source projection, required dimensions and visible/inferred labels on the new revision.

Software migration: PROPOSAL automate validated input/mask/export types and use-specific checks after fixtures; keep new invisible-geometry design and unsupported model outputs with the reasoning agent.

Future cases: SAM Objects Gaussian PLY cannot fulfill direct mesh; a generated backside conflicts with a newly supplied real view; equal silhouette but wrong depth fails working-interface checks; mesh export loses texture or flips frame; changed checkpoint invalidates candidate checks.

## 15. REC-19 — Train and export a Gaussian splat scene

[Original contract](../workflows/reconstruction-paths.json): **photo-set AND camera-solution → gaussian-scene**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-19-A01 — Prepare a Gaussian training dataset with verified camera mapping.** (1) Pair every image with its source camera and pixel convention. (2) Apply only the required camera-basis and world transforms, then read parsed values. (3) Freeze training, camera-refinement, tuning and evaluation participation. Output: Dataset/parser receipt with original-to-training camera/world transforms, scale, image assignments, camera-optimization policy and feature evaluation plan. Check: Check camera projection against source before training; reject duplicate axis flip/scale normalization; evaluation images used in SfM retain their shared pose dependence.

1. **REC-19-A02 — Train and export the actual Gaussian scene representation.** (1) Train the chosen candidate into a separate checkpoint lineage during future execution. (2) Export only supported Gaussian representation and preserve raw state. (3) Read attributes and renderer/frame compatibility into the package receipt. Output: Gaussian scene package with training config/checkpoint, renderer/version, exported Gaussian PLY when supported, bounds/frame mapping and artifact hashes. Check: Load with the named Gaussian renderer; verify image/camera/frame associations and required attributes. Ordinary point-cloud readers cannot establish Gaussian-scene completeness.

1. **REC-19-A03 — Evaluate captured-view appearance and geometry handoff boundaries.** (1) Render actual captured evaluation cameras and compare named regions. (2) Select the evidence-supported scene or retain conflicting alternatives. (3) Reopen selected package and validate any separately proposed mesh/CAD alignment on the new composition revision. Output: Appearance evaluation with shared dependencies, selected Gaussian revision, renderer receipt and explicit geometry/composite proposal. Check: Generated novel views retain checkpoint lineage; training-heldout/SfM-used views are labelled accordingly; Splatfacto geometry export remains capability-gated despite generic TSDF wording.

Existing entrypoints and proposed helper interfaces:

1. **REC-19-A01.** Software: Use an evidenced supplied-camera parser or prepared transforms.json pathway with version discovery; read actual parsed cameras, auto-orientation/centering/scale settings and output transform. Do not rerun default pose estimation unintentionally. Preserve actual dataparser_transform and dataparser_scale, applied metadata and orientation override; scene_scale is box extent. Use the recorded inverse composition for round trip, as specified in common_protocol.parser_contract. PROPOSAL Gaussian dataset adapter: photos + supplied cameras + selected parser/config → training dataset, camera/world normalization receipt, readback differences and participation table.

1. **REC-19-A02.** Software: Use selected Splatfacto training and Gaussian export; preserve checkpoint/config and inspect exported attributes expected by the chosen renderer. Record actual GPU/backend requirements and resumable state. PROPOSAL Gaussian package adapter: trained state + parser transform + supported Gaussian export → typed gaussian-scene with renderer assets, attribute manifest and resume receipt.

1. **REC-19-A03.** Software: Render evaluation cameras using pinned renderer; compare captured regions under stated exposure/mask policy; verify scene transform by known source projections; typed-check any additional mesh. PROPOSAL Gaussian evaluation/composition ledger: scene + captured checks + optional geometry transforms → region results, compatible scene layers and fresh composite validation.

Execution choices:

1. **Agent directs.** Agent interprets coverage/masks and chooses supported scene candidates; software trains, exports and renders measured comparisons.

1. **Software and agent.** Agent sets evidence associations and exceptions; software handles parser readback, training/checkpoints and image comparisons.

1. **Software ordinary cases.** Recognized camera/parser/export contracts train and evaluate automatically; conflicting scale/roles or unsupported geometry export returns for review.

1. **Complete software procedure.** Pinned dataset/parser/config/backend supports tested replay and comparison; stochastic training reproducibility is measured for the chosen build.

Alternatives and target detail: Minimal captured-view context; bounded Gaussian preview; full required viewing coverage; independently reconstructed mesh plus Gaussian appearance plus parametric CAD as a proposed layered composition.

Candidate selection and merge: Pin common photos/cameras and record branch image subsets/detail/Gaussian settings, required viewpoints and resources. VLM selects with actual source/evaluation crops and numerical reports; shared SfM and checkpoint dependencies stay visible. Compose compatible appearance and geometry layers through explicit transforms; Gaussian parameters remain their own typed layer, and conflicting appearance candidates remain separate. Reopen renderable scene, check camera projection/world scale and every affected layer/interface; independent reviewer rechecks source-region interpretation.

Software migration: PROPOSAL migrate supplied-camera parsing, Gaussian package checks and region comparisons after fixtures for each method/version/renderer; retain unsupported-export and semantic-region exceptions for agent reasoning.

Future cases: Already converted camera receives no second axis flip; hidden parser normalization changes scale and fails readback; heldout-from-training but SfM-used image reports shared pose dependency; Gaussian PLY passed as observed cloud fails; generic TSDF versus Splatfacto unsupported export stays a capability conflict; interrupted checkpoint/export resumes from complete lineage.

## 16. REC-20 — Train and export a NeRF scene

[Original contract](../workflows/reconstruction-paths.json): **photo-set AND camera-solution → nerf-scene**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-20-A01 — Bind NeRF method, supplied cameras and training-space transforms.** (1) Bind source images to exact camera records and calibration. (2) Build the selected parser input and read its actual camera/world transforms. (3) Freeze appearance training, camera optimization, tuning and evaluation roles. Output: NeRF dataset receipt with camera basis/world orientation/centering/scale transforms, parser readback and source participation table. Check: Projection agreement is checked before training; a generic processing route that re-estimates supplied poses must be explicitly requested and produce a new camera revision.

1. **REC-20-A02 — Train and save a renderable NeRF state.** (1) Train into a named checkpoint lineage under pinned inputs during future execution. (2) Save model/config/renderer dependencies and inspect complete state. (3) Record the actual supported consumer and gate optional surface extraction by method inputs. Output: NeRF scene package: config, weights/checkpoint, renderer/code version, bounds, camera/world map and hashes; conditional mesh export is a separate derivative. Check: Reopen checkpoint with selected renderer and render a recorded camera; an exported preview GLB alone is insufficient for a resumable NeRF-state claim.

1. **REC-20-A03 — Validate scene appearance and any separately extracted geometry.** (1) Evaluate source-heldout appearance with its actual shared camera dependencies. (2) Validate optional extracted surface independently by required feature. (3) Select/package the scene and recheck any new geometry/CAD composition revision. Output: Region-based appearance report, actual scene consumer receipt, optional geometry validation and selected revision. Check: Field-derived meshes retain inference/extraction provenance; generated evaluation views are internal tests; Gaussian exports cannot substitute for nerf-scene state.

Existing entrypoints and proposed helper interfaces:

1. **REC-20-A01.** Software: Read selected parser inputs/settings and actual camera values; convert source camera basis only when required; preserve inverse world normalization and any camera-optimization changes. Preserve actual dataparser_transform and dataparser_scale, applied metadata and orientation override; scene_scale is box extent. Use the recorded inverse composition for round trip, as specified in common_protocol.parser_contract. PROPOSAL NeRF input adapter: photos/cameras/config → parsed dataset, reversible world transform, camera comparison and partition manifest.

1. **REC-20-A02.** Software: Use supported NeRF trainer/save/load route; preserve config/checkpoint and renderer dependencies. Before optional export, verify method supplies depth/normals/field needed by that exporter. PROPOSAL NeRF package adapter: training state/config + transform receipt → renderable nerf-scene and separately typed optional export with support/loss map.

1. **REC-20-A03.** Software: Render fixed captured evaluation cameras; compare named regions; if extraction is supported, read mesh topology/frame, reproject to sources and check withheld dimensions without replacing the trained state. PROPOSAL NeRF qualification adapter: trained scene + actual captures + optional extracted geometry/control evidence → appearance and geometry reports with independent readiness.

Execution choices:

1. **Agent directs.** Agent interprets view coverage and model-specific export eligibility; software trains, renders and measures.

1. **Software and agent.** Agent defines source-feature/evaluation roles; software performs camera readback, checkpointing and numerical comparisons.

1. **Software ordinary cases.** Recognized NeRF method/parser with checked output can run; unsupported normals/depth/export or camera semantics triggers exception review.

1. **Complete software procedure.** Pinned method/dataset/config uses tested replay and renderer checks; convergence and stochastic variation remain measured properties.

Alternatives and target detail: Camera-only or captured-image context first; bounded NeRF preview; required-view appearance training; method-supported extracted mesh or independent MVS mesh plus CAD as a proposed composition.

Candidate selection and merge: Record exact method/parser/dataset/splits, required viewing/detail and resource observations; isolate checkpoints. VLM compares captured source regions, actual renderer outputs and numerical evidence, with independent semantic review. Compose separately typed NeRF, geometric mesh and CAD through checked transforms; editing or combining extracted surfaces creates a new geometry revision. Reopen renderer state, compare source-camera projections and verify changed geometry/interfaces and semantic mappings.

Software migration: PROPOSAL automate each checked parser/method/checkpoint/renderer and export class separately; promote only after failures for scale/basis/splits/extraction and resume are detected on known cases.

Future cases: Missing predicted normals blocks Poisson exporter while scene stays complete; changed world normalization misaligns CAD and is detected; training-view render cannot count as independent appearance test; field mesh passes global bounds but closes an opening and fails regional check; partial checkpoint/config mismatch cannot resume silently.

## 17. REC-11 — Train NeRF or Gaussian scene for view synthesis

[Original contract](../workflows/reconstruction-paths.json): **photo-set AND camera-solution → visual-scene**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **REC-11-A01 — Choose the actual renderable scene subtype and consumer.** (1) Identify the required visual consumer and source regions. (2) Select the evidenced Gaussian/NeRF subtype and payload. (3) Bind camera parsing and representation-specific output/validation actions. Output: Scene dispatch record naming Gaussian or NeRF subtype, renderer, config/checkpoint/assets, camera route and optional separate geometry branch. Check: Consumer supports the actual subtype and required assets; a generic visual-scene type cannot conceal missing renderer/checkpoint dependencies.

1. **REC-11-A02 — Execute the selected typed training route and package its scene.** (1) Run the selected typed training/package procedure. (2) Bind all saved scene assets and transforms into a manifest. (3) Load the manifest with its named renderer and retain the observed consumer receipt. Output: Visual-scene manifest referencing actual Gaussian or NeRF package, renderer/version, config/checkpoint/assets, world transform and export loss map. Check: All referenced assets exist and hashes match; named consumer actually loads the scene; mesh/GLB expectations require their separate supported export branch.

1. **REC-11-A03 — Validate scene use and proposed appearance/mesh/CAD composition.** (1) Validate rendering against named real evaluation captures. (2) Compose only explicitly requested compatible layers through checked transforms. (3) Reopen the new composition and repeat affected numerical and independent semantic checks. Output: Visual-scene evaluation and selected revision; optional composition manifest with typed layers, transforms, source mappings and independent checks. Check: Each layer preserves its representation and source role; shared camera/model dependencies are stated; a visual alignment cannot replace critical interface measurements.

Existing entrypoints and proposed helper interfaces:

1. **REC-11-A01.** Software: Inspect chosen method and consumer interface; resolve whether visual-scene contains training state/renderer assets or a supported exported scene subtype. PROPOSAL scene dispatcher: photos/cameras + consumer requirements + capability evidence → typed method route and explicit visual-scene payload manifest.

1. **REC-11-A02.** Software: Invoke the selected typed procedure in future execution; verify saved state and supported export; package actual renderer dependencies and raw source revisions. PROPOSAL visual-scene manifest builder: checked Gaussian/NeRF package + consumer contract → generic visual-scene with exact subtype, dependency closure and load receipt.

1. **REC-11-A03.** Software: Render fixed captured views; if composition is in scope, calculate/read actual source→target transforms and compare projection and critical geometric controls for each layer. PROPOSAL scene composition ledger: typed appearance package + optional mesh/CAD + measured transforms → layered scene manifest, affected checks and source-per-feature report.

Execution choices:

1. **Agent directs.** Agent chooses subtype/consumer and resolves scene meaning; software executes the chosen typed route and checks its loadable package.

1. **Software and agent.** Agent sets source/consumer associations; software composes checked manifests, renders and measures.

1. **Software ordinary cases.** Supported subtype/consumer pair dispatches automatically; unsupported export/renderer or ambiguous source roles returns to reasoning.

1. **Complete software procedure.** A fixture-tested exact subtype/renderer/config package can be rebuilt/checked with recorded stochastic limitations.

Alternatives and target detail: Camera/image context with minimal local preprocessing; Gaussian appearance; NeRF appearance; independent mesh+CAD with an appearance layer as an explicit compatible composition proposal.

Candidate selection and merge: Pin same source/camera revisions and record intended consumer, detail/viewpoint coverage, method and cost for each subtype. VLM selects actual source/consumer fit using real captures and numerical evidence; separate reviewer checks semantics. Combine typed layers only through explicit frame mapping and compatible renderer interfaces; checkpoints or learned primitives are not averaged. Reload new scene revision and repeat source projection, required geometry checks and independent layer/feature interpretation.

Software migration: PROPOSAL automate supported subtype/consumer dispatch after fixtures for complete dependency manifests and camera transforms; keep new renderer/export combinations with reasoning review.

Future cases: Gaussian scene declared GLB without supported export fails consumer check; missing checkpoint dependency keeps visual-scene partial; equal visual bounds but wrong CAD scale fails composition controls; compatible scene layers with changed parser scale trigger affected revalidation.

## 18. DOM-22 — Photographs to Gaussian/NeRF visual scene

[Original contract](../workflows/domain-paths.json): **photo-set AND camera-solution → gaussian-scene**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-22-A01 — Bind the domain Gaussian scene contract.** (1) Read the literal photo/camera inputs and Gaussian output. (2) Map domain regions to source pixels and intended views. (3) Select the supported Gaussian route and recorded frame handoff. Output: Gaussian domain route receipt with feature-to-source mapping, camera policy and explicit link to REC-19; NeRF requests route separately to DOM-30. Check: NeRF or mesh request is explicitly dispatched to its own operation; every required region has source/evaluation roles and consumer support.

1. **DOM-22-A02 — Build the Gaussian scene and preserve domain mappings.** (1) Execute the checked Gaussian procedure under the pinned domain request. (2) Attach source-region/domain IDs and actual world mapping. (3) Reopen the scene with its renderer and record required asset completeness. Output: Gaussian scene package and domain mapping sidecar with checkpoint, renderer, parsed-camera/world transform and export attributes. Check: Typed Gaussian attributes and renderer state match; source feature identity is retained through mappings; node/primitive order does not create semantic IDs.

1. **DOM-22-A03 — Check domain appearance and explicit geometric overlays.** (1) Evaluate named domain regions against real captures. (2) Check any separate geometry overlay with independent controls. (3) Select and reopen the new package/composition, repeating affected checks. Output: Domain region report, selected Gaussian revision and optional checked composition manifest. Check: Gaussian coverage cannot satisfy missing physical geometry; optional overlay requires actual feature/frame checks; generated views retain shared checkpoint lineage.

Existing entrypoints and proposed helper interfaces:

1. **DOM-22-A01.** Software: Typed dispatcher verifies input camera coverage and exact Gaussian renderer/export support; preserves element/component IDs as a sidecar mapping. PROPOSAL domain Gaussian planner: photos/cameras + domain feature/use map → REC-19 request, typed gaussian-scene consumer and coverage criteria.

1. **DOM-22-A02.** Software: Use REC-19 A01/A02; preserve domain IDs through source region mapping and scene transform, rather than assuming each learned primitive has a physical component identity. PROPOSAL domain scene packager: Gaussian state + source/domain map → gaussian-scene with stable source feature references and actual renderer receipt.

1. **DOM-22-A03.** Software: Render actual evaluation cameras; check source-region coverage; if geometry overlay is scoped, apply checked transforms and query required measured interfaces/placements. PROPOSAL domain appearance report: Gaussian scene + captured checks + optional measured geometry → region readiness and compatible overlay receipt.

Execution choices:

1. **Agent directs.** Agent interprets domain region/view needs; software runs REC-19 and checks actual output.

1. **Software and agent.** Agent supplies feature mappings; software packages Gaussian assets and quantitative comparisons.

1. **Software ordinary cases.** Recognized source/camera/domain mapping follows checked Gaussian route; subtype or identity exceptions return for review.

1. **Complete software procedure.** Pinned domain/source/map/config supports fixture-tested package creation and readback, retaining measured training variability.

Alternatives and target detail: Camera-only/domain source inspection; bounded Gaussian context; full required-view Gaussian scene; independent geometric model with Gaussian appearance overlay; NeRF is the explicit DOM-30 alternative.

Candidate selection and merge: Record common photo/camera revisions plus domain coverage/detail/consumer and resource criteria per Gaussian candidate. VLM selects source-supported domain associations and viewing results; independent reviewer checks semantic mapping. Compose compatible domain geometry as a separate typed layer with measured transform; keep contradictory region identities as alternatives. Reopen Gaussian renderer and any overlay, repeat region/camera and critical geometric checks.

Software migration: PROPOSAL migrate stable domain mappings, package/export and per-view checks by supported input/consumer class; preserve reasoning for semantic identity and new geometry choices.

Future cases: Broad title cannot return NeRF as Gaussian output; learned primitive reordering preserves source sidecar identity; trained-heldout view used in camera fitting reports dependency; overlay mm/metre mismatch fails independent controls.

## 19. DOM-30 — Photos to NeRF visual scene

[Original contract](../workflows/domain-paths.json): **photo-set AND camera-solution → nerf-scene**. The corresponding JSON record supplies each action's exact inputs, evidence, role assignments, criteria and resource conditions.

1. **DOM-30-A01 — Bind domain features and cameras to the NeRF route.** (1) Pair domain features with source images and cameras. (2) Select the NeRF method/consumer and explicit parser route. (3) Freeze source/evaluation roles and required region criteria. Output: Domain NeRF request referencing REC-20, input camera/parser mapping and required source/view coverage. Check: Both inputs and camera coverage are present; actual renderer supports NeRF payload; parser coordinate/scale discovery is assigned before training.

1. **DOM-30-A02 — Train and package the domain NeRF state.** (1) Execute the pinned NeRF preparation/training/package route. (2) Bind domain identities to source regions and training-world transforms. (3) Reopen saved state with the named renderer and record actual package completeness. Output: NeRF config/checkpoint/renderer package, domain source sidecar, parser transform/scale and complete/partial receipt. Check: Checkpoint/config/renderer dependencies load; domain/source mappings remain revision-bound; an optional extracted mesh cannot replace NeRF state.

1. **DOM-30-A03 — Evaluate domain viewing results and optional surface reuse.** (1) Compare real captured domain views under recorded cameras. (2) Evaluate any supported extracted surface with independent physical controls. (3) Reopen the selected scene/composition and perform affected numerical and semantic checks. Output: Domain appearance report, selected NeRF revision and optional separate geometry/composition validation receipt. Check: Generated novel views retain derived status; NeRF geometry cannot inherit IFC/component semantics from appearance; new geometric layers preserve original identity evidence.

Existing entrypoints and proposed helper interfaces:

1. **DOM-30-A01.** Software: Inspect selected supplied-camera parser and renderer; validate feature/image links and actual normalization receipt requirements. PROPOSAL domain NeRF planner: source photos/cameras + domain/view goals → REC-20 request, parser/renderer contract and required region checks.

1. **DOM-30-A02.** Software: Run REC-20 A01/A02 in future execution; attach domain/source references and actual parsed-camera/world mapping; preserve checkpoint/assets. PROPOSAL domain NeRF packager: trained NeRF + domain/source map → loadable nerf-scene manifest with renderer, frame chain and artifact dependencies.

1. **DOM-30-A03.** Software: Render named captured evaluation views; compare domain regions; inspect supported optional extraction's geometry and frame against controls before geometric reuse. PROPOSAL domain NeRF qualification: scene + source/check roles + optional geometry → per-region appearance/geometry readiness and affected dependency checks.

Execution choices:

1. **Agent directs.** Agent identifies domain regions and supported method/extraction; software trains/renders/measures.

1. **Software and agent.** Agent defines domain/source evidence; software performs parser, package and region checks.

1. **Software ordinary cases.** Supported NeRF/domain map/consumer class runs with exceptions for unresolved camera, identity or export support.

1. **Complete software procedure.** Pinned method/input/domain map allows checked package replay; reproducibility claims depend on tested backend settings.

Alternatives and target detail: Minimal photos/cameras context; bounded NeRF preview; required-view scene training; independent measured mesh/CAD or supported extracted surface as separately checked geometry.

Candidate selection and merge: Pin common source/camera/domain IDs and record method/detail/view coverage/criteria/resources for each NeRF candidate. VLM chooses captured-evidence-supported appearance and feature identity; separate reviewer checks meanings and shared dependencies. Compatible appearance and geometry layers keep typed assets and explicit transform chain; conflicting inferred surfaces remain alternatives. Reload trained state and optional composition, repeat source-view comparison and affected physical/domain checks.

Software migration: PROPOSAL migrate recognized domain parser/state/renderer and evaluation classes after fixtures; new surface extraction, geometry semantics and source ambiguity stay with reasoning.

Future cases: NeRF checkpoint without renderer/config stays partial; parser world scale error changes geometry overlay and fails controls; field extraction fills a doorway despite similar render and fails domain geometry check; shared evaluation/camera dependencies are retained; changed domain geometry invalidates only its composition descendants.

## 20. Shared future cases and documentary verification

1. Camera preprocessing: known crop/resize/distortion and integer-centred versus corner-grid source with already-converted duplicate case; expected actual camera readback/projection and exactly one required convention conversion.

2. Nerfstudio parser: supplied applied_transform/applied_scale, orientation override, fallback condition and zero camera extent; expected recorded dataparser_transform/scale, separate scene_scale bounds, guarded degeneracy and known-point round trip without duplicate axes/scale. Include nonzero translation with nonunit scale under the declared p_normalized=s*(R*p_source+t) contract and verify reverse order with known points/origins.

3. Depth encoding: millimetre, metre, zero sentinel, negative/nonfinite and exact truncation boundary, mismatched RGB size/time/extrinsics; expected source-specific conversion/masks and correct >= truncation zeroing, with required calibration/timing failure identified.

4. Pose direction: camera-to-world and world-to-camera inputs with same physical scene, plus swapped pairwise motion; expected identical checked integration only after explicit conditional inversion and composition.

5. Independent evidence: train-heldout image used in SfM, fit control reused for evaluation and generated back view; expected exact participation/common-dependency report and no independent physical claim from derived evidence.

6. Typed PLY: geometric samples, face mesh and Gaussian parameter attributes under same extension; expected correct dispatch and blocked Gaussian-to-observed-cloud meshing.

7. Learned metric depth: raw canonical versus already-converted selected API outputs and ambiguous card-only focal rule; expected no invented/divisor or duplicate conversion, separate confidence and measured residual records.

8. Surface preservation: thin wall, opening, disconnected parts and uneven/biased normals; smoothing/fill/decimation may preserve bounds while changing required local topology; expected original derivative map and local failure.

9. Dense/chunk recovery: partial cloud with missing mesh, disconnected sparse components, GPU unsupported build, chunk seam and changed source calibration; expected precise partial output, bounded alternate branch and affected invalidation.

10. Scene export: generic TSDF claim versus selected Splatfacto unsupported route, missing NeRF renderer/config, direct SAM Gaussian output under requested mesh; expected representation-specific completion and capability-gated alternate route.

11. Remote interruption: lost inference/VLM response, malformed selection rows and changed source after resume; expected retained raw request/response, reconciled/retried lineage, no publication until valid complete selection and affected-only invalidation.

12. Compatible appearance+mesh+CAD composition and contradictory regional geometry: expected typed layers/common transforms, source-supported selection without averaging, new revision and separate numerical/semantic post-merge checks.

The tests above specify future fixture inputs and expected outcomes. Documentation checks cover exact operation/action coverage, fifteen-field completeness, four execution modes, matching Markdown action IDs, local links and file formatting. Review evidence is in the [software review](reviews/point-07-software.md), [visual/evidence review](reviews/point-07-visual.md), [source review](reviews/point-07-sources.md) and [designer notes](reviews/point-07-designer.md). The [independent review](reviews/point-07-independent.md) is DONE; both recorded findings are resolved after reread.
