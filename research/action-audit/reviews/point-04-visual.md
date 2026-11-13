# Point 04 visual and evidence review — raster drawings and orthographic views

Registration date: 2026-11-12. Status: **DONE — local documentary review**. Procedures and validation cases below are proposals. Scope: CAD-02, CAD-03, CAD-04, CAD-05, CAD-06, CAD-07, CAD-17, DOM-02 and DOM-18, with readable names below.

Requested assignment: `gpt-6.1-sol`, reasoning effort `xhigh`. Actual executing model identity: **unavailable in this agent environment**. Local project instructions, audit plan, original operations, dossiers and source-register summaries were inspected. External URLs retain their registered inspection status. This review's executed output is its document.

The [point-01 visual review](visual-review.md), [point-02 visual review](point-02-visual.md) and [point-03 visual review](point-03-visual.md) supply the shared feature ledger, units/frames, revision-bound views, branch merge and vector-to-solid checks. This review adds raster/source-coordinate and cross-view interpretation requirements.

## 1. Findings for the point-04 procedure

1. **Image formation and depicted geometry have separate records.** Lens distortion, perspective of a photographed page, page deformation and drawing-to-object scale are different effects. CAD-02's planar transform uses matched points on one plane and independent in-plane controls. Record which plane those controls describe and their units. Explicit dimensions on a freehand sketch remain source values beside the sketch's image-estimated proportions.
2. **Dimension recognition includes glyph, association and meaning.** Retain the original string and source region, candidate parsed value, unit/tolerance notation, dimension/leader/extension-line endpoints, associated feature and view. CAD-03's OCR text/boxes/confidence provide one part of that evidence. A correct number attached to the wrong edge produces a source-association error.
3. **Vector candidates retain their stroke roles.** CAD-04 supplies candidate segments/contours. The interpretation assigns object edge, hidden edge, centreline, dimension line, extension line, leader, text, wall edge or opening symbol. A contour around thick raster ink can describe the stroke boundary; the intended component/profile requires its own reviewed association.
4. **Orthographic reconstruction keeps alternative correspondences.** CAD-06 consumes multiple identified views with individual scales, axes and projection directions. Its first-angle/third-angle convention and source labels control registration. CAD-07 can retain different depth/hidden-feature candidates with matching projections; source dimensions, sections and feature identities determine the dependent construction.
5. **Floor-plan interpretation retains wall and opening identity.** CAD-05 needs a wall edge/centreline convention, graph IDs and opening-host associations. CAD-17 consumes that graph plus explicit vertical parameters and datum. DOM-18 adds an IFC output with its own element/relationship checks and all five original input categories.
6. **Numerical projection and semantic review have separate results.** Project each generated candidate back into its source views with recorded transforms, compare the intended features and independent controls, then review whether the correspondences and line roles mean the same thing as the source. The merged artifact receives new checks against its own revision.

## 2. Proposed VLM responsibilities and source-coordinate procedure

A **VLM — vision-language model** processes images and language together. In point 04 it interprets labelled pixels, engineering notation, feature correspondence and competing candidate models. Image-processing software supplies recorded transforms, candidate pixels/vectors and numerical comparison results. The procedure gives the model the actual source regions and the reason each geometric quantity is required.

1. **Retain the full source.** Record source file/page identity, hash, pixel width/height, page orientation and acquisition evidence. Identify a scanned drawing, a photograph of a page or an image of a physical object according to supplied evidence. Keep different source views separately named.
2. **Record the image transform chain.** Retain original-to-working crop, rotation, deskew, rectification, resampling and any calibrated lens-remapping operation with its settings/version and transform direction. Store the mapping appropriate to that operation, including validity masks where required. Keep full-view context for every crop.
3. **Separate page-plane and object scale.** Record physical page controls when they rectify a photographed sheet. Record drawing-plane/object controls when they map depicted coordinates to engineering units. Identify front-parallel scale assumptions, known drawing dimensions and sketch estimates separately.
4. **Propose dimension readings.** Show the VLM the full view and crops containing glyphs, arrowheads, dimension/extension lines and associated feature endpoints. Preserve competing readings of decimals, diameter/radius signs, tolerance signs, limits, repeated-feature counts and unit symbols. Record the raw glyphs before normalization.
5. **Associate dimensions with features.** Trace each line/leader to a named edge, axis, circle, opening or endpoint pair in the relevant view. Record the source pixel coordinates of that association, its source-to-working mapping and the proposed engineering quantity. Preserve alternative associations when the crop excludes the controlling context.
6. **Classify strokes and topology.** Review object versus annotation/hidden/construction lines. Map candidate segment IDs to closed loops, hole loops, separate parts or wall/opening graph IDs. Compare both the original pixels and any extraction overlay; retain changes caused by thresholding or simplification.
7. **Associate views.** Record front/top/side/section labels, projection convention, per-view scale, datum and axis direction. Match named features using dimensions and line roles. The VLM proposes correspondences and records the evidence distinguishing alternatives.
8. **Review resulting geometry.** Compare labelled orthographic/model-to-source projections of the same artifact revision with the source regions and query receipts. For a suspicious feature, specify the bounded dimension, axis, plane or topology query needed to check it.

Proposed dimension record additions to the shared feature ledger:

| Record group | Raster-specific fields |
| --- | --- |
| Source position | Full-image/page ID, raw pixels, crop bounds, orientation and complete working-to-source coordinate mapping |
| Literal notation | Original glyph string, OCR candidate strings/boxes/confidence, decimal/unit/tolerance/count notation |
| Association | Dimension-line/leader ID, arrowhead and extension-line endpoints, object feature IDs and view ID |
| Meaning | Diameter/radius/length/angle/offset/count interpretation, datum, sign and source evidence class |
| Numerical evidence | Explicit annotation value, pixel-derived estimate or independent measurement; transform/control IDs and criterion source |
| Review | Candidate reading/association, source regions examined, reasoning result and dependent feature state |

## 3. Operation-specific procedures and check boundaries

| Operation | Proposed interpretation/action | Numerical/topological checks and retained handoff |
| --- | --- | --- |
| **CAD-02 — Rectify a raster drawing plane from known dimensions** | Identify the plane and matched controls; distinguish page perspective from source drawing scale and any lens/page-deformation evidence. Use front-parallel scaling or the documented planar-transform route under their respective input conditions. | Retain original/mapped control coordinates, units, correspondence and transform. The CAD-R02 four-point example supplies a recipe case. Check independent in-plane lengths and local regions; preserve the original image and rectified artifact identity. |
| **CAD-03 — Recognize dimension text with OCR** | Read candidate glyphs against the original source and resolve quantity/feature association using the full view and connected linework. | Keep OCR TSV hierarchy, boxes, confidence and candidate strings; retain literal and parsed values separately. Compare every controlling value, symbol, unit and feature association with the source. |
| **CAD-04 — Extract raster edges, lines and contours** | Select preprocessing/extraction candidates and classify strokes into object, annotation and construction roles. Retain uncertain candidates and the pixels supporting each segment. | Record threshold/Hough/contour/simplification parameters, endpoint coordinates, candidate IDs, gaps and intersections. Overlay on source and compare displacement in declared calibrated coordinates. Preserve changes in stroke topology. |
| **CAD-05 — Convert raster floor-plan candidates into a wall and opening graph** | Identify wall edge/centreline convention, wall junctions, room boundaries, opening symbols and host walls. Keep source labels and their geometry separate. | Check graph connectivity, wall endpoints/junctions, intended opening-host attachment, known lengths and applicable orientation relations. Retain source pixel→vector→graph mappings and ambiguous symbol/connection candidates. |
| **CAD-06 — Register orthographic drawing views in a shared coordinate frame** | Identify view labels and projection convention, per-view scale and axes; propose feature correspondences from source evidence. Its input remains a multi-view bundle. | Record each view-plane→model projection mapping. Compare shared coordinates and control dimensions; retain correspondence alternatives and their source regions. A two-view input and the three-view PlankAssembly research input retain their respective conditions. |
| **CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views** | Build the candidate only from the registered views, measurement evidence and brief. Label inferred hidden features/surfaces and retain depth/face alternatives required by the source ambiguity. | Project generated geometry into each view and compare corresponding edges/features. Check solid/manifold state, part/feature counts and required dimensions. Retain the correspondence graph, native/constructed representation and its checked revision. |
| **CAD-17 — Build wall and opening solids from a confirmed floor-plan graph** | Construct the confirmed graph using sourced wall height, thickness convention, floor datum, opening width/height and sill/head positions required by the brief. Preserve separate identities. | Query wall/opening dimensions and elevations, opening-host geometry and room/graph connectivity. Compare generated plan projections with source controls. Retain the CAD assembly and graph/parameter lineage; IFC classification belongs to its explicit semantic operation. |
| **DOM-02 — Raster sketch to constrained sketch** | Compose the source/image transform, interpreted profile and explicit dimension constraints. Image-estimated undimensioned lengths keep that evidence class. | Preserve pixel→feature→constraint mapping, source units/frame, independent scale residuals, closed loops and solver state. Apply point-03 source-to-constraint checks to the actual native sketch. |
| **DOM-18 — Raster floor plan to IFC building** | Consume the raster, dimensions, measured controls, source-library records and normalized brief. Carry wall/opening interpretations into identified IFC elements and relationships. | Check wall/opening geometry, units, elevations, spatial containment, element/area checks and IFC validation. Preserve source-library item identity/terms and raster→graph→IFC element mapping. Compare the saved IFC's host/void relationships and geometry with the interpreted source. |

Original evidence labels remain visible: CAD-02/CAD-03 and DOM-02/DOM-18 carry documented-capability labels; CAD-04/CAD-05/CAD-06/CAD-07/CAD-17 carry proposed-composition labels in the original records. The present detailed VLM orchestration, merge and validation procedures are proposals. The floor-plan and orthographic papers supply method evidence with their own datasets and input conditions.

## 4. Goal-specific branches, comparison and merge

| Proposed branch | Retained result | Required evidence/check |
| --- | --- | --- |
| Explicit-dimension branch | Source glyphs, checked values, feature anchors and datum relations | Full-source/crop review plus literal/parsed-value comparison; downstream dimensions consume those values |
| Image-vector branch | Candidate linework, loops and source-coordinate mapping | Pixel overlay, calibrated endpoint/curve displacement, topology and annotation separation |
| Reduced-detail sketch branch | Required arrangement/features with declared image-derived or explicit dimension evidence | Required-feature completeness, source/axis identity and the criteria for that sketch purpose |
| Precision feature branch | Required interface dimensions, named axes/planes and constrained/native geometry | Feature-specific sourced dimensional/angular criteria and actual geometry readback |
| Orthographic candidate branches | Alternative feature correspondences, depth/hidden-surface hypotheses and resulting models | Per-view projection comparisons, source dimensions, feature identity and independent controls |
| Floor-plan branches | Manual trace or source-backed detector proposals, wall/opening graph and CAD/IFC route | Graph/host identity, dimensions, plan projection, vertical inputs and output-specific validation |

Proposed comparison/merge procedure:

1. Freeze source/brief revisions and each branch's intended use, required features and criteria. Store each branch's detail and accuracy target independently.
2. Put candidate features into common units and frames while preserving source pixel, working image, view plane and model frames. Match feature identities before comparing values or merging linework.
3. Calculate differences by feature and evidence class: glyph reading, endpoint association, transform/scale, line role, graph connection, view correspondence, depth or geometric construction.
4. Provide the VLM the original full views, cited crops, candidate overlays, source values and numerical/topology reports. Request evidence-linked selection of a whole candidate or compatible feature evidence within the stated goal.
5. Retain complementary evidence for the same identified feature with its source. Preserve incompatible readings and geometry interpretations as alternatives; identify the exact source association or intended design decision needed by the dependent action.
6. Construct a new merged record/artifact revision with feature-to-branch lineage and selection reasons. Re-run required topology, scale, dimensional, projection and output checks against that new revision.
7. Use a separate semantic reviewer to compare the merged feature associations, hidden/visible line meaning, wall/opening identity and view conventions with original evidence. Keep its findings separate from numerical checks and model agreement.

A lower-detail sketch and a precision interface can share source identity while carrying different required-feature sets. Their controlling measurements keep the criteria supplied for their stated purpose. This review assigns no numerical tolerance or hidden dimension.

## 5. Model-to-source projection and independent measurements

1. **Generate the correct view.** Project candidate geometry into each registered orthographic view or drawing plane using its recorded frame and projection convention. For a photographed page, map that drawing-plane projection through the recorded image transform to the original source coordinates.
2. **Compare corresponding features.** Measure endpoint/edge/curve differences for the named feature and relevant regions. Record pixel residuals and, where calibration supports it, differences in drawing/model units. Preserve the transform/control provenance used by that conversion.
3. **Check extra and missing structure.** Compare the intended holes, hidden edges, boundaries and openings in each view. Identify whether a candidate projection includes a feature that the source assigns to annotation or another view.
4. **Reserve independent controls.** Keep controls used to choose scale/pose distinct from controls used to assess the result. Record both roles explicitly. Report local residuals and controlling feature measurements beside aggregate fit values.
5. **Check actual geometry.** Query the saved native/reopened artifact's required dimensions, axes, part counts and topology with its owning application or supported geometry adapter. Preserve artifact revision/hash and measured entity IDs.
6. **Inspect semantic correspondence separately.** Verify that the numerical query measures the intended component, source feature or wall/opening pair. A matching silhouette can coexist with different depth or hidden structure; retain the source-supported alternatives.
7. **Validate the actual consumer.** For the DOM-18 IFC branch, compare element identity, containment, opening-host/void relationship and saved geometry with the source graph. Keep the raster/CAD graph evidence beside the IFC semantic result.

Plan raster controls, OCR/source claims, CAD solver criteria, source dimensional tolerances, measurement uncertainty and projection residual criteria retain their individual meanings and sources. The [CAD-R02](../../workflows/details/cad-r02.md), [CAD-R03](../../workflows/details/cad-r03.md), [CAD-R05](../../workflows/details/cad-r05.md) and [DOM-R01](../../workflows/details/dom-r01.md) dossiers provide the original route and check context.

## 6. Repeatable software migration, exceptions and resumption

| Proposed repeatable component | Agent interpretation retained | Exception/resumption rule |
| --- | --- | --- |
| Image-transform manifest and control comparison | Select the relevant plane, control identity and source scale meaning | Conflicting controls, page deformation or source scale require a bounded interpretation with retained original coordinates |
| OCR candidate/region package | Resolve glyphs, units, tolerance notation and connected dimension-feature meaning | Unreadable or competing readings retain candidate strings/crops and the exact dependent feature question |
| Stroke/line/contour extraction | Classify engineering/plan roles and source-authorized joins | Crossing/merged text/annotation/object strokes retain separate candidates, parameters and overlay evidence |
| Profile/wall graph checks | Resolve loop/part and wall/opening-host semantics | Ambiguous junctions, symbols or contour roles preserve candidate graphs and source regions |
| Orthographic coordinate/projection comparison | Choose source-supported view/feature correspondence | Multiple depth/hidden-feature solutions retain separate candidates and their checks |
| Candidate-model/IFC validation | Review source-feature and semantic relationship identity | Failed feature/relationship rows identify the earliest dependent transition to revisit |

1. **Agent directs work:** review the relevant full views/crops and direct explicit candidate extraction, association and checks for ambiguous inputs.
2. **Software and agent work together:** software produces image/line/OCR/graph/projection results; the agent selects associations and diagnoses failed or competing candidates.
3. **Software handles ordinary cases:** use a demonstrated page/drawing/symbol/profile/view class with an explicit exception report and retained evidence package.
4. **Software handles the complete action:** process supplied controls, checked feature associations and machine-readable construction/check rules for the supported class; record actual outputs and failures.

Before migration, define expected successful, ambiguous, invalid and interrupted cases for the particular component. An authorized implementation must demonstrate that class before software-led status is assigned. Preserve the [existing implementation plan](../../implementation-plan.md) and its current stage order.

On interruption, retain source/working-image hashes, transform chain, completed candidate/feature IDs, call/operation identity and partial results. Resume from the last completed bounded stage against the same inputs. A changed dimension reading invalidates its dependent constraint/construction checks; a changed page transform invalidates affected coordinate-derived linework, measurements and projections. Query the same CAD operation identity before replaying an uncertain mutation, following the existing OCS recovery contract.

## 7. Validation cases and resource records for a future run

1. **Photographed planar page:** checked controls define one plane; expect retained transform/mapping and independent in-plane length checks.
2. **Lens/page deformation or freehand proportions:** supply evidence distinguishing the effects; expect explicit source/transform classes and preserved dimension values with image estimates.
3. **Engineering glyphs:** diameter/radius, decimal, tolerance, unit and count notation have checked source transcriptions; expect literal/parsed records and correct feature anchors.
4. **Crop loses context:** dimension text and controlling endpoints require separate regions; expect full-view linkage and retained source-coordinate mappings.
5. **Annotation crosses an outline:** expect object/dimension/extension-line candidates with distinct roles and a correct reviewed loop.
6. **Wall/opening symbols:** include thick wall strokes, junctions, an opening and room labels; expect the chosen edge/centreline convention, graph and host IDs to persist.
7. **Projection convention:** use labelled first/third-angle examples with checked axes; expect source-specific view transforms and feature correspondences.
8. **Ambiguous hidden depth:** several models share visible projections; expect retained alternatives and the source feature/decision required for dependent construction.
9. **Reduced-detail and precision goals:** compare required features and criteria for each; expect source identity and per-feature evidence to survive simplification.
10. **Merged branch:** complementary dimension and line evidence are selected; expect the merged revision's own projection, numerical and semantic checks.
11. **Vertical building inputs:** a plan graph and explicit wall/opening elevations supply the construction; expect source-linked vertical parameters and correct plan/host/elevation checks.
12. **IFC host association:** two walls are visually close; expect the correct source wall→opening→IFC relationship mapping and independent semantic review.
13. **Interrupted extraction/model call:** retain completed rows and frozen inputs; expect bounded continuation and coherent feature/revision identity.

A future resource receipt separates preprocessing/rectification, OCR, extraction, association, graph/view comparison, construction and validation time. Record raster dimensions/pages, full-view/crop counts, resampling settings, candidate segments/loops/graph nodes/view matches, geometry size, CPU time, wall time, peak RAM and GPU/VRAM where actually used. Model receipts record local/remote location, actual exposed model/effort, evidence transmitted, calls, latency/cost and manual intervention. Compare semantic correspondence, controlling-feature accuracy, retained alternatives and further refinement work for the same goal. The dossier ratings remain their original qualitative assessments; these procedures require case-specific measurements.

## 8. Local sources and original URLs reused

All local records below were inspected on 2026-11-12. Original web sources are reused at their registered evidence state.

| Local record / original URL | Summary used here | Evidence status |
| --- | --- | --- |
| [Original CAD operations](../../workflows/cad-paths.json), [domain operations](../../workflows/domain-paths.json), [audit plan](../plan.md) | Nine operation contracts, method/representation boundaries, per-action evidence and goal-specific criteria | Local records/proposals inspected |
| [CAD-R02 raster-sketch dossier](../../workflows/details/cad-r02.md), [CAD-R03 floor-plan dossier](../../workflows/details/cad-r03.md), [CAD-R05 orthographic dossier](../../workflows/details/cad-r05.md), [DOM-R01 building dossier](../../workflows/details/dom-r01.md) | Source-to-image/feature controls, OCR/line candidates, manual/algorithmic graph interpretation, orthographic ambiguity and geometry/IFC checks | Existing local assessments inspected |
| [OpenCV calibration overview](https://docs.opencv.org/5.0/main_modules/calib.html) | Registered summary covers calibration/pose correspondences and planar homography's one-plane relationship | `web_inspected`, reused from [round-two CAD sources](../../sources/round-02/cad-sources.json) |
| [OpenCV image transformations](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html) | CAD-R02 records `getPerspectiveTransform` and `warpPerspective` for planar rectification, with retained controls and independent length checks | Existing dossier/source record reused |
| [OpenCV camera calibration tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) | Registered summary describes intrinsic/radial/tangential distortion estimation and undistortion from known pattern/image correspondences | `web_inspected`, reused from [round-two reconstruction sources](../../sources/round-02/reconstruction-sources.json) |
| [Tesseract command-line usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html), [dossier's exact GitHub documentation URL](https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md) | Registered summary supplies TSV page/block/line/word IDs, pixel boxes, text and confidence; engineering association is the proposed review step | `web_inspected` in [round-two CAD sources](../../sources/round-02/cad-sources.json); GitHub URL retained through CAD-R02 |
| [OpenCV feature detection](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html), [shape analysis](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html) | Registered summaries supply Hough segment endpoints, contours and polygon approximation with pixel-coordinate settings | `web_inspected`, reused from [round-two CAD sources](../../sources/round-02/cad-sources.json) |
| [Residential Floor Plan Recognition and Reconstruction](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html) | Registered summary describes floor-plan segmentation/vectorization and study-specific recognition/reconstruction results | `web_inspected` in [round-two CAD sources](../../sources/round-02/cad-sources.json); `existing_report_registered` in [round-three records](../../sources/round-03/cad-detail-sources.json) |
| [Vectorizing Building Blueprints](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf) | Registered summary describes raster blueprint primitive/vector/structure methods; the dossier records method evidence with a manual/CAD handoff | `web_inspected` in round-two; `existing_report_registered` in round-three CAD sources |
| [Raster-to-Graph floor-plan paper](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf) | Registered summary describes learned wall junction/segment prediction as an ordered graph | `web_inspected`, reused from [round-two CAD sources](../../sources/round-02/cad-sources.json) |
| [Engineering-drawing coordinate transformations](https://xnjdxb.swjtu.edu.cn/en/article/id/9616) | Registered summary describes segmented views, intermediate 2.5D frames and cross-view coordinate constraints | `web_inspected` in round-two; `existing_report_registered` in round-three CAD sources |
| [Automatic 3D CAD reconstruction from 2D orthographic drawings](https://www.sciencedirect.com/science/article/pii/S0097849323000766) | Registered summary describes projected-edge matching, wireframe, face/loop extraction and watertight construction with study-specific evaluation | `web_inspected`, reused from [round-two CAD sources](../../sources/round-02/cad-sources.json) |
| [PlankAssembly](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html) | Registered summary describes a three-orthographic-view transformer/shape-program method and noisy/incomplete benchmark inputs | `web_inspected` in round-two; `existing_report_registered` in round-three CAD sources |
| [IfcOpenShell geometry creation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html), [opening feature API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html) | Registered summaries describe supplied geometry/placements and the opening-to-host-wall void relation used by the IFC branch | `web_inspected`, reused from [round-three domain sources](../../sources/round-03/domain-detail-sources.json) |

## 9. Integration handoff

1. Integrate the raster coordinate/annotation fields, one-plane calibration boundary, view/feature alternatives, graph identities and separate numerical/semantic checks as point-04 proposals.
2. Preserve original operation/dossier labels and method-specific source conditions; retain the current implementation plan and source originals.
3. The coordinator owns source/graph consistency checks and the checkpoint/result commits. This review writes only its assigned document.
