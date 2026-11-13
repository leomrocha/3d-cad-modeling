# Point 05 visual and evidence review — existing CAD with photographs and scans

Registration date: 2026-11-12. Status: **DONE — local documentary review**. Procedures and validation cases below are proposals. Scope: CAD-11, CAD-02B, REC-01, REC-02, REC-07, REC-08, REC-09, REC-12, REC-13, REC-14, REC-15, REC-16, DOM-19 and DOM-23, with readable names below.

Requested assignment: `gpt-6.1-sol`, reasoning effort `xhigh`. Actual executing model identity: **unavailable in this agent environment**. Live instructions, audit plan, original operation records, local reconstruction reports/dossiers and source summaries were inspected. External URLs are reused at their recorded evidence states. The executed output is this review document.

The [point-02 visual review](point-02-visual.md), [point-03 visual review](point-03-visual.md) and [point-04 visual review](point-04-visual.md) define common source identity, units/frames, view packages, feature lineage and merged-revision checks. This review adds camera, cloud-registration, surface-fitting and existing-model annotation requirements.

## 1. Findings for the point-05 definition

1. **Photo and scan branches have different outputs.** REC-12's photo branch can produce a camera pose from camera evidence and known correspondences. Its scan branch produces a spatial alignment and surface-comparison record. Retain those conditions beside the original camera-solution/measurement outputs. DOM-19's outputs are `registration-transform` and `point-cloud`. Any camera-pose operation uses its own explicit branch and camera evidence.
2. **Camera evidence belongs to the actual processed image.** Record camera/lens/focus state, calibration model, image resolution, crop/rotation/resize/undistortion mappings, pixel convention and transform direction. A calibration-target unit supports target-based metric pose; an unrelated monocular reconstruction retains its own scale/control evidence.
3. **Registration metrics describe a particular fit.** Record participating source/target regions, units, sampling, normals, correspondence thresholds, initialization and transform class. Symmetry, partial overlap and geometrically degenerate regions receive explicit alternative-pose and independent-control checks.
4. **A surface fit preserves observation and intent separately.** Plane/cylinder/axis parameters are calculated from retained samples and masks. A drawing's nominal dimension, an as-observed fitted dimension and an authored idealization carry separate values, revisions and intended uses. A residual alone supplies a surface difference; attribution to wear, damage or another cause needs its own evidence.
5. **Screen annotations need depth and feature meaning.** REC-13 ray anchors depend on the recorded camera and selected hit geometry. Retain object/component/revision, primitive/hit identity, ray/depth/occlusion and the chosen meaning of trace, projected curve or planar sketch. The resulting anchors are calculated geometry evidence.
6. **Parametric remodeling preserves feature lineage.** REC-14/DOM-23 map sampled regions, drawings and measurements into named parameters and editable native/source artifacts. Record actual backend feature/history persistence. The inspected OCS baseline supports native geometry; particular feature-history or script outputs receive their actual backend conditions.
7. **Refinement checks a new revision against fixed evidence.** REC-16 keeps source scans, independent controls and comparison regions fixed for an edit comparison. A changed registration or sampling rule creates a separate comparison branch. Revalidate source correspondence, critical dimensions and saved/reopened artifacts after any evidence merge or edit.

## 2. Proposed VLM procedure and evidence package

A **VLM — vision-language model** processes images and language together. Here it proposes CAD/photo/scan feature correspondences, interprets source differences and compares candidate alignments or remodels. Software computes camera transforms, registration, ray hits, primitive fits and revision-bound measurements. Reasoning results keep their source regions and measured comparison rows.

1. **Freeze identities.** Record the native CAD revision and component/occurrence IDs, original photo/frame hashes, scan/cloud/mesh hashes, drawing revision and required feature criteria. Name source and target roles in every comparison.
2. **Prepare camera/view evidence.** Retain original images, processed image identity, pixel dimensions and preprocessing mappings. Record intrinsics/distortion, calibrated camera/lens/focus state, pose convention and source calibration revision. Views rendered from CAD retain their geometry revision, visibility/clipping state and camera.
3. **Propose landmark correspondences.** Give the VLM full-view context and labelled crops of the actual CAD/photo/scan regions. Identify the same physical corner, axis, mounting face, target or feature across sources. Preserve alternative matches for repetitive, symmetric or occluded features. Keep image pixels, CAD entities and scan sample IDs together in the correspondence record.
4. **Compare candidate alignments.** Software calculates pose/registration and regional checks. The VLM examines labelled overlays, independent-control differences, orientation/handedness and alternative-pose results. Record a proposed selection and its evidence, or the exact distinguishing feature needed to resolve a remaining alternative.
5. **Interpret fitted regions.** Examine segment membership, coverage, mixed surfaces, partial arcs, source drawings and the intended CAD feature. Propose the named feature/parameter association and distinguish observed shape from a requested nominal or idealized model.
6. **Interpret annotations.** Read the instruction/stroke with full-view and selected-surface evidence. Associate it with the intended component, feature and edit scope. Separate a screen trace, a projected surface curve and a datum-plane sketch before constructing constraints.
7. **Review the revised artifact.** Compare the saved native/derived revision with its source evidence, required interfaces and fixed comparison regions. Retain the semantic review separately from numerical checks and reasoning-model agreement.

| Evidence group | Point-05 additions to the shared record |
| --- | --- |
| Camera/image | Source/processed image IDs, dimensions, crop/resize/rotation/lens mappings, intrinsics, distortion convention, lens/focus state, calibration revision, pixel convention, pose direction and axes |
| CAD landmark | Component/occurrence/feature ID, native entity or datum, source coordinate/frame, CAD revision and tessellation identity where used |
| Scan correspondence | Original sample/face IDs, region/mask, source/target roles, units/frame, sampling/filtering/normal settings and correspondence classification |
| Transform | Rigid or chosen similarity class, allowed scale, direction, source/target frame, initialization, fitted/independent controls and settings |
| Fit | Primitive hypothesis, selected sample IDs, excluded mask, spatial/angular coverage, residuals, parameter units/frame and sensitivity cases |
| Annotation | Original pixels/stroke, camera/view revision, ray definition, selected hit object/primitive, calculated hit/depth, occlusion/no-hit status and interpreted feature meaning |
| Remodeling | Source-to-parameter map, nominal/observed/assumed status, native feature/source IDs, changed/retained dimensions and dependent artifacts |

## 3. Operation-specific actions and check boundaries

| Operation | Concrete proposed interpretation/action | Software result and required checks |
| --- | --- | --- |
| **CAD-11 — Fit analytic features to scans or image-derived point clouds** | Consume already metric/registered evidence. Select the functional region and candidate plane/cylinder/axis/freeform interpretation; identify unsampled or occluded regions. | Retain samples, segmentation/outlier masks, fit settings and residual distribution. Compare independent dimensions and held-out cloud-to-CAD distances. Any resulting solid carries a separate named construction/native revision with parameter lineage. |
| **CAD-02B — Calibrate camera poses from photographs and known controls** | Associate known calibration geometry/3D points with actual image features and source units. Record the camera model and input-image state. | Preserve detected points, target geometry, calibration/pose results and reprojection residuals. Check independent controls and calibration/image-resolution consistency. |
| **REC-01 — Calibrate camera intrinsics and distortion** | Identify camera/lens/focus state, target geometry and image-field/orientation coverage. Classify manufacturer, target-based or self-calibrated input evidence by its actual source. | Preserve original target images/coordinates and fitted intrinsics/distortion. Record per-image/RMS residuals and a held-out target check; keep undistorted images as derivatives with mappings. |
| **REC-02 — Solve camera pose from known 3D-to-2D correspondences** | Review CAD/world landmark identity and pixel location, including symmetry/occlusion alternatives. | Record object/world-to-camera rotation/translation, intrinsics/distortion and camera-axis convention. Compare pixel reprojection and independent target correspondences. Preserve target units in translation. |
| **REC-07 — Estimate coarse transform between point clouds** | Identify source/target regions, shared geometric features and alternative alignments. Select the supported rigid/similarity route according to scale evidence. | Retain FPFH/RANSAC or target/manual initialization settings, inliers and transform. Compare independent controls and candidate poses; report overlap/sampling and correspondence checks. A scale-estimating path names the actual solver/settings. |
| **REC-08 — Refine registration and compare point-cloud surfaces** | Examine coarse pose, geometric support, symmetry, overlap and non-overlap. Distinguish plausible local fits from source-supported feature correspondence. | Preserve initial/final transform, normals, threshold, objective and participating points. Report fitness/inlier RMSE, independent-control residuals and regional distance maps. Point-to-plane checks retain useful-normal/coverage evidence. |
| **REC-09 — Segment point clouds and fit candidate primitive evidence** | Select component/feature regions and diagnose mixed surfaces or partial arcs. Review candidate plane/cluster/primitive meaning against source evidence. | Preserve original indices, masks, thresholds, inlier counts, coefficients and residuals. Compare alternative supported thresholds/regions and record parameter sensitivity and coverage. |
| **REC-12 — Register existing CAD to calibrated photographs or scan points** | Select exact CAD and photo/scan evidence, then review visible landmarks or sampled surface correspondence. Keep alternate symmetric/partial-overlap poses. | Photo branch: camera pose and independent landmark reprojection. Scan branch: spatial transform, distance map and interface/control measurements. Preserve CAD tessellation settings and source-to-derivative entity mapping. |
| **REC-13 — Anchor a screen sketch to a 3D surface** | Identify target component/surface and stroke meaning. Review near/far surfaces, hidden surfaces and stroke portions crossing silhouettes. | Calculate rays/hits under the recorded camera; retain hit object/primitive and no-hit/ambiguous cases. Reproject anchors, compare source pixels and check any later sketch plane/constraints separately. |
| **REC-14 — Remodel segmented scan evidence as parametric CAD** | Map observed/fitted/drawing dimensions to named features; define the intended observed, nominal or idealized result from the scoped brief. | Preserve raw scan/indices/fits and feature provenance. Record actual native sketch/source/solid artifacts supported by the backend. Check solid validity, required dimensions, regional held-out residuals and saved-file reopen. |
| **REC-15 — Reconcile scan surfaces with dimensioned drawings** | Associate the drawing's exact item/revision/datums with the observed component and scan regions. Preserve competing source values and proposed interpretations. | Fit using identified controls and reserve independent checks. Report drawing-to-scan differences, coverage, datum consistency and per-feature outliers. Separate source-variant models remain available. |
| **REC-16 — Iterate CAD edits against registered evidence** | Propose one bounded feature edit with its source/goal and expected changed/retained quantities. Compare the new model's meaning with the prior one. | Read back the edited revision; use fixed scan/controls, regions, threshold and sampling rules. Report regional maximum/RMS/quantiles plus functional dimension changes and saved artifact identity. |
| **DOM-19 — Register scan to building frame** | Identify IFC/source element datums, project/local/georeferenced frames and measured distributed controls. Review the correct wall/element correspondence where geometry repeats. | Preserve raw scan and the source-to-building transform. Compare local held-out residuals and occlusion/coverage. Record the `registration-transform` and aligned `point-cloud` outputs, retaining the source scan separately. |
| **DOM-23 — Scan or mesh to parametric CAD remodeling** | Combine the stated source-input branch with measured controls, target function and model brief. Retain source-region→feature→parameter associations. | Record actual cloud/mesh selection and its scale/frame, independent interface dimensions, source evidence and editable artifacts. Check held-out surface distances, functional interfaces, valid solid and saved/reopened geometry. |

The original records label CAD-02B, REC-01/02/07/08/09 and DOM-19/23 as documented capabilities; CAD-11 and REC-12/13/14/15/16 are proposed compositions. The procedure above adds proposed model orchestration and evidence checks. Original [CAD](../../workflows/cad-paths.json), [reconstruction](../../workflows/reconstruction-paths.json) and [domain](../../workflows/domain-paths.json) records retain their input contracts and labels.

## 4. Camera, overlay and registration comparison

1. **Bind the camera to its image.** Use the intrinsics/distortion appropriate to the actual image resolution and processing. Preserve the original-to-working image mapping and applicable calibration revision. OpenCV's registered PnP convention is camera X right, Y down, Z forward; record the explicit conversion to the receiving CAD/render frame.
2. **Preserve direction and handedness.** Name world/object-to-camera and source-cloud-to-target transforms explicitly, with units and permitted scale. Store inverses as named derived transforms. Record any axis reflection separately from a rotation.
3. **Review overlays as observations.** Record source image, camera/CAD revision, rendered visibility/occlusion, colour overlay and region. Inspect landmarks, silhouette and orientation; pair controlling claims with pose/geometry measurements.
4. **Distinguish calibration, pose and source geometry.** Camera/pose changes can change overlay alignment. Keep independent image landmarks and physical dimensions so a fit can be checked against controls reserved from optimization. Preserve the source CAD while diagnosing whether a mismatch lies in correspondence, camera, registration or geometric difference.
5. **Challenge cloud alignment with alternate poses.** Use source identity, named datums and independent controls for symmetric/repeated geometry. Compare partial-overlap regions and non-overlap separately. Retain the fit objective, masks and actual settings beside its metrics.
6. **Challenge degenerate evidence.** A planar patch, short arc or narrow overlapping strip can leave competing motion/feature interpretations. Record the supported directions/extent and distinguish them with distributed controls or another source region. Keep alternative candidates when those observations remain compatible.
7. **Keep comparisons reproducible.** Freeze source/target sampling, CAD tessellation, comparison direction, normals, region masks and threshold for a revision comparison. A changed configuration creates a separate run with its own result.

## 5. Fitting, drawing reconciliation and annotation depth

### 5.1 Analytic fitting and nominal/observed candidates

1. Retain the sampled region, its frame/units and observed coverage. A fitted cylinder from a partial arc carries that coverage and its sensitivity results alongside radius/axis estimates.
2. Record the intended output: an observed surface candidate, a source drawing's nominal geometry or a scoped idealized functional model. Keep the source value and fitted result side by side, with source item/revision and parameter identity.
3. Compare regional residuals and independent interface dimensions. A deviation can be investigated as scan/calibration/registration error, source revision difference or physical shape difference. A wear/damage claim carries its own inspection/measurement evidence.
4. Merge complementary observations about the same feature when their identities, frames and source conditions agree. Preserve conflicting values as separate candidates; an authored replacement value needs its explicit rule and source/decision.
5. Keep unobserved surfaces and functional details with their inference status. A simplified arrangement can use retained scan/mesh context; a precision interface requires its actual controlling dimensions and checks.

### 5.2 Screen annotations and ray anchors

1. Preserve the annotation image/stroke, exact source view/camera, model/mesh revision and selected target surface. Record whether the requested result is a surface trace, projected curve or planar sketch.
2. Calculate each ray and hit under that camera. Record the selected object/occurrence and primitive, hit position/depth and applicable transform. Preserve near/far/occluded alternatives and no-hit portions.
3. Reproject anchors into the original view through the actual image mapping and compare the selected pixels. This checks the recorded projection/anchor relation; source dimensions and independent controls supply metric evidence for the intended feature.
4. Map the retained anchors to the later CAD plane/constraint/feature interpretation. Store the fitting/simplification parameters and changed stroke geometry. Use a bounded interpretation for a stroke crossing empty space, a silhouette or several components.
5. Inspect the installed ray-cast interface before any future implementation. The existing Blender source record reports an indexed `Scene.ray_cast` entry and an HTTP 402 direct-page retrieval; it supplies a limited capability lead with that exact evidence state.

## 6. Candidate selection, refinement and independent validation

| Candidate option | Use condition | Required comparison |
| --- | --- | --- |
| CAD/photo alignment | Known component revision and usable calibrated landmarks | Independent reprojection, units/axes, correspondence and controlling geometry |
| Coarse then refined cloud alignment | Geometric overlap and supported initialization/scale route | Alternative poses, independent controls, regional fit/coverage and fixed comparison configuration |
| Reduced-detail scan/mesh reference | Arrangement or appearance goal with declared required features | Source identity, frame, visible coverage and required envelope/interface checks |
| As-observed fitted CAD | Observed regions and independent measurements support the requested model | Fit coverage/sensitivity, held-out distances and functional dimensions |
| Nominal/drawing CAD | Identified drawing/item revision defines requested geometry | Source dimensions/datums plus separately reported scan differences |
| Scoped idealized functional CAD | Brief defines the idealization and its required interfaces | Authored assumptions/parameters, required-feature criteria and retained observational evidence |

1. Give candidates the same frozen evidence revision, required features and intended use. Record their differing detail and accuracy targets.
2. Compare source identity, units/frames and correspondence before geometry metrics. Give the VLM original views/regions, candidate overlays, fit/control reports and parameter differences.
3. Record evidence-linked whole-candidate selection, compatible evidence/feature merge or retained alternatives within the stated intent. Preserve branch origins and selection reasons. A conflict requiring new intent becomes the precise dependent question.
4. For refinement, declare the changed parameter/feature, objective, check configuration and stop criterion from the brief or scoped decision. Preserve each failed/pass result and the reason for another bounded iteration.
5. After merge/edit, remeasure the new geometry revision against fixed independent controls and required interfaces. Check source correspondence with a separate semantic reviewer, then validate native save/reopen and actual downstream artifact hashes. Agreement between model calls remains a review result with its own input identity.

## 7. Software migration, failure handling and resource classes

| Repeated step proposed for software | Fixture/expected behavior before migration | Agent exception task |
| --- | --- | --- |
| Camera/image manifest and reprojection | Original/processed image mappings, resolution changes, distortion and explicit pose-direction cases | Resolve source camera state and landmark identity conflicts |
| Coarse/fine registration receipt | Correct pose, symmetric wrong pose, partial overlap, planar degeneracy and differing scale cases | Choose source-supported datum/candidate or identify the next distinguishing source |
| Regional segmentation/fit | Mixed surfaces, outlier mask, partial arc and threshold-sensitivity cases with retained sample IDs | Interpret the functional feature and observed/nominal model goal |
| Screen-ray anchor package | Multiple surfaces, occlusion, no-hit and changed-view/model-revision cases | Resolve target surface and annotation meaning |
| Drawing/scan comparison | Item revision mismatch, unit/frame difference, conflicting source dimensions and known local difference | Interpret source correspondence and preserve competing explanations |
| Revision comparison and invalidation | One changed feature, fixed independent checks and interrupted operation case | Select the earliest failed semantic/geometry transition and bounded correction |

The four execution options apply per demonstrated input class: an agent can direct explicit tool operations; software and agent can combine calculations with association review; software can process ordinary cases and report named exceptions; fully explicit supported inputs can use a complete software action with its defined checks. Preserve the [implementation plan](../../implementation-plan.md) and demonstrate the particular implementation on retained expected cases before assigning software-led status.

On interruption, retain input hashes, camera/transform revisions, sampled regions/masks, fit/call/operation IDs and completed feature rows. Query the same CAD operation identity before another mutation. A changed camera calibration invalidates dependent poses, overlays and anchors; a changed registration invalidates dependent source-to-CAD comparisons; a changed scan mask/fit invalidates its dependent parameters; a changed CAD feature invalidates affected measurements and exports. Keep unaffected evidence and previous checked revisions.

Resource records distinguish these cases:

1. **Small calibrated landmark/annotation case:** point/pixel bookkeeping, PnP and selected ray queries; record image/view count, landmarks, hit/miss count, CPU time and actual rendering/model-call cost.
2. **Regional scan fit/comparison:** record selected/raw point counts, normals, neighborhood/feature settings, sample masks, CAD tessellation and peak RAM/time. Compare the same required-feature checks for reduced versus retained sampling.
3. **Large cloud/building registration:** record total/overlap point counts, spatial extent, indexing, candidate transforms, distance-map size and local/georeferenced frame handling. Record GPU/VRAM only where the selected implementation uses it.
4. **Parametric remodel/refinement:** record native feature/part counts, regeneration/query/export time, stored revisions and comparison work per iteration.
5. **Reasoning/visual review:** record local/remote model, requested and actual exposed identity/effort, full-view/crop resolution/count, evidence transmitted, calls, latency/cost and manual interpretation. Compare controlling-feature accuracy, semantic correspondence and further refinement for the same goal.

## 8. Local evidence and original source URLs reused

All local records below were read on 2026-11-12. External-source claims keep their registered evidence status and version/context.

| Local record / original URL | Concrete summary used here | Evidence status |
| --- | --- | --- |
| [CAD operations](../../workflows/cad-paths.json), [reconstruction operations](../../workflows/reconstruction-paths.json), [domain operations](../../workflows/domain-paths.json), [audit plan](../plan.md) | Fourteen operation contracts, source roles, conditional camera/scan evidence and feature-specific checks | Local records/proposals inspected |
| [Reconstruction assessment](../../reconstruction.md), [depth/CAD dossier](../../workflows/details/rec-r09.md), [overlay revision dossier](../../workflows/details/dom-r05.md) | Separate image/scan evidence from CAD interpretation; retain controls, camera/transform state, comparison regions and bounded revisions | Existing local reports/dossiers inspected |
| [OpenCV camera calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html), [CAD record's versioned tutorial URL](https://docs.opencv.org/4.12.0/dc/dbb/tutorial_py_calibration.html), [calibration overview](https://docs.opencv.org/5.0/main_modules/calib.html) | Registered summaries describe target/image correspondences, intrinsics/distortion and physical target units; round-three summary separates unrelated monocular reconstruction scale | `web_inspected`, reused from [round-two CAD](../../sources/round-02/cad-sources.json), [round-two reconstruction](../../sources/round-02/reconstruction-sources.json) and [round-three reconstruction records](../../sources/round-03/reconstruction-detail-sources.json) |
| [OpenCV PnP](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html) | Registered summary describes known 3D/2D correspondences, intrinsics/distortion, object/world-to-camera rotation/translation and X-right/Y-down/Z-forward convention | `web_inspected`, reused from round-two/three reconstruction records |
| [Open3D global registration](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html) | Registered summary describes FPFH/RANSAC, correspondence pruning, transform/fitness/inlier RMSE and subsequent ICP | `web_inspected` in round two; `existing_report_registered` in round three reconstruction records |
| [Open3D ICP](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) | Registered summaries describe initialized point-to-point/point-to-plane refinement, thresholds, normals, transforms and fit metrics | `web_inspected`, reused from round-two/three reconstruction records |
| [Open3D point-cloud operations](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html) | Registered summaries describe plane segmentation, DBSCAN clustering, normal estimation, inlier indices and coefficients | `web_inspected`, reused from round-two/three reconstruction records |
| [CloudCompare repository](https://github.com/CloudCompare/CloudCompare), [command-line mode](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode) | Registered summaries identify interactive alignment/inspection and ordered open/process/save CLI operations; exact commands depend on the selected version/operation | `existing_report_registered`, reused from reconstruction records and assessment |
| [Blender Scene API](https://docs.blender.org/api/current/bpy.types.Scene.html) | Existing record identifies indexed `Scene.ray_cast`/annotation API entries; direct page returned HTTP 402, so installed signature/behavior remains a future capability check | `web_inspected` with that retrieval limitation in [round-two reconstruction records](../../sources/round-02/reconstruction-sources.json) |
| OCS engineering skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`), [CAD assessment](../../cad-and-skills.md) | Existing local evidence defines native-revision readback, part/frame boundaries, supported numerical-check scope and uncertain-operation recovery; CAD assessment records history/export conditions | Local sources read in the preceding point reviews and reused |

## 9. Integration handoff

1. Integrate conditional photo/scan outputs, source-bound camera/image records, registration alternatives, fit/nominal distinctions, ray-hit provenance and fixed-evidence refinement into point 05 as proposals.
2. Keep original operation/input labels and inspected-source limitations visible. Preserve source assets, earlier revisions and the implementation-plan sequence.
3. The coordinator owns source/graph consistency and checkpoint/result commits. This review writes only its assigned document.
