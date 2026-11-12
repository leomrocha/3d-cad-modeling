# Point 04 — Raster drawings and interpreted dimensions

Date: 2026-11-12. Status: **procedure proposal**. Scope: nine operations and 30 actions. Requested procedure-design dispatch: `gpt-6-astra`, `xhigh`; actual executing model identity: **unavailable**.

[Structured operation records](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) contain all 15 fields per action, operation-specific alternatives, four execution modes, merging, migration and future cases. This readable procedure retains the same stable action IDs. The [audit plan](/home/leo/projects/3dmodeling/research/action-audit/plan.md), [original CAD records](/home/leo/projects/3dmodeling/research/workflows/cad-paths.json), [domain records](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json), [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md), [model contract](/home/leo/.codex/skills/ocs-engineering/references/model-contract.md) and [retained implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md) govern source identity, units, frames and evidence. All helper interfaces and execution procedures are proposals; acceptance labels require `MARK AS ACCEPTED`.

## 1. Terms and evidence chain

1. **Raster image:** an image represented by pixels. **OCR**, or optical character recognition, produces text candidates from those pixels. A **VLM**, or vision-language model, interprets images and language together.
2. **Homography:** a projective coordinate mapping between two planes, represented by a matrix. Its controls define that planar mapping. Page-plane perspective, lens distortion, page deformation and drawing-to-object scale have separate evidence and correction models.
3. **Orthographic view:** a projection along parallel lines perpendicular to the view plane. A multiview drawing identifies each view's scale, axes, direction and projection convention. First-angle and third-angle conventions specify how the views are arranged relative to the object.
4. **Graph:** identified nodes and connections. The wall/opening graph records wall paths, junctions, openings and host relationships. **Topology** describes connectivity among geometric elements. **B-rep**, or boundary representation, stores surfaces, edges and their connections.
5. **IFC**, or Industry Foundation Classes, is a building-data format containing element identities, geometry and relationships. A **void relation** associates an opening with the host element it removes material from.
6. **Residual:** a measured difference between corresponding coordinates, curves or quantities. A **pinned revision** is an explicitly fixed revision or file hash. A sketch **degree of freedom** is an independent movement remaining after its constraints.

The source chain is original image → mapped reading/tracing coordinates → literal annotation or stroke candidate → named feature/relationship → explicit constraint or construction parameter → actual geometry → saved output. Every transition retains IDs and source locators.

1. **CAD-02** produces a measurement-set. Rectified image, transform and sampling receipt are ancillary evidence.
2. **CAD-03** produces reviewed text with companion annotation/feature-association records. **CAD-04** produces source-linked vector candidates.
3. **CAD-05** produces a vector-drawing containing the wall/opening graph and its metadata. **CAD-06** consumes a bundle of at least two identified views and produces a reconstruction brief. **CAD-07** consumes views, measurements and that brief to produce a checked solid and measurement-set.
4. **CAD-17** consumes reviewed graph, measurements and vertical parameters to produce CAD wall/opening assembly geometry. **DOM-18** consumes all five original input categories and authors IFC geometry and semantics.
5. **DOM-02** composes raster evidence and actual native constraints. Dimension-only work follows the brief/vector/parameter procedures rather than claiming a raster source.

## 2. Source coordinates, dimensions and branch rules

1. Preserve original image bytes, hash, page/view identity, orientation and pixel dimensions. Every crop, rotation, deskew, resize, perspective warp and calibrated lens remap records its source/target frames, order, direction, pixel-center/grid convention, interpolation, output grid and valid domain. Coordinate maps locate retained source evidence; original pixels supply the unresampled record.
2. Record physical-page controls separately from depicted-object controls. A photographed sheet can be rectified while the freehand drawing still has approximate proportions. Explicit annotated dimensions retain their values and source status; image-derived estimates carry their own uncertainty.
3. A general projective mapping needs sufficient source/target point correspondences in a common plane. The documented four-pair OpenCV case requires a nondegenerate quadrangle configuration. A single length supports scale only under a separately justified restricted model. Fitting controls and independent check controls retain different roles.
4. Each annotation record includes literal glyph string, raw OCR candidates, source view/crop, leader/dimension/extension endpoints, target feature IDs, quantity kind, nominal value, unit, tolerance and count. An OCR rectangle transformed projectively is retained as mapped corner coordinates; nonlinear lens mappings retain their actual mapped boundary and valid domain.
5. Each feature has separate engineering allowance, measurement uncertainty and computational/fit threshold with sources. Solver/kernel criteria and saved/export comparison thresholds also retain their scopes. A pixel displacement is converted through the actual local mapping; it supplies no universal dimensional tolerance.
6. Every branch records source subset/revisions, intended use, feature coverage/detail, units/frame, individual criteria and local/remote/manual resources. A lower-detail arrangement branch can satisfy its envelope/datum requirements while a working-part interface or building opening needs further source evidence.
7. The VLM receives full source views, located crops, original glyphs, candidate overlays and actual numerical reports. It can select supported associations or compatible contributions within the stated task. Conflicting controlling sources or new design intent require the precise user decision. Dimensions are preserved as alternatives rather than averaged.
8. Use the [point03 shared protocol](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json) for source/request identity, isolated candidates, producer/reviewer separation, uncertain native/remote completion and affected-only invalidation. Raster-specific additions and future recovery cases are in this point's `common_protocol` and `common_future_tests`.

## 3. CAD-02 — Rectify a raster drawing plane from known dimensions

**Entry points and evidence.** [OpenCV transforms](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html) provide getPerspectiveTransform and warpPerspective; [calib3d](https://docs.opencv.org/4.13.0/d9/d0c/group__calib3d.html) provides findHomography and calibrated lens correction.

1. **CAD-02-A01 — Identify plane evidence and independent metric controls.** Preserve source pixels/orientation. Locate controls in original pixels and target-plane units. Separate fitting and withheld controls; record transformation prerequisites. Output: Plane/control manifest and selected scale/projective model for CAD-02-A02. Check: One length supports uniform scale only with justified front-parallel/isotropic conditions; projective correction requires sufficient nondegenerate correspondences.
2. **CAD-02-A02 — Estimate plane mapping and rectified derivative.** Validate point order and coordinate conventions. Estimate selected transformation. Create derivative and retain original coordinates/settings. Output: Transform, coordinate inverse where defined, ancillary rectified derivative and fit report. Check: Check finite/invertible mapping and residual distribution across feature regions; inverse maps coordinates, while source pixels remain preserved separately.
3. **CAD-02-A03 — Check independent controls and publish measurements.** Measure withheld controls. Compare differences and regional consistency. Publish measurement-set with ancillary mapping/derivative receipt. Output: Measurement-set with original/transformed coordinates, units/frame, method, uncertainty and readiness; derivative is ancillary. Check: Fitted-control agreement and independent-check agreement remain separate; failures block only affected metric uses.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects plane/control associations and directs transform checks for ambiguous drawings. |
| Software and agent | Software fits and measures; agent evaluates controls and model suitability. |
| Software handles ordinary cases | Checked scan/plane classes use fixed rules; insufficient controls or regional distortion enters review. |
| Deterministic supported case | Explicit plane, nondegenerate controls, settings and withheld criteria produce a checked measurement-set. |

**Alternatives and target quality.** Justified front-parallel scan with uniform scale. Projective planar mapping from adequate point correspondences. Manual point selection followed by numerical fitting/checks. Lower-detail arrangement and precision dimensional uses retain distinct controls/criteria.

**Proposed helpers.** plane preflight consumes image/control evidence and emits model sufficiency, control roles and check IDs. rectification adapter emits matrix/inverse, valid domain, fit diagnostics and sampling receipt. planar checker consumes mapping/checks/criteria and emits residual rows and named downstream readiness. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM reviews full/crop control evidence; software compares independent residuals. Select one coherent mapping per plane; preserve conflicting dimensions and separate planes. Recompute retained coordinates and independent checks; separate reviewer checks meaning.

**Migration condition.** Automate demonstrated scan/planar-photo classes after control sufficiency, degeneracy, wrong-unit, regional-distortion and withheld-check fixtures.

## 4. CAD-03 — Recognize dimension text with OCR

**Entry points and evidence.** [Tesseract](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html) produces raw TSV, or tab-separated values, with hierarchy, boxes, confidence and text. Engineering notation parsing and feature association are proposed components.

1. **CAD-03-A01 — Locate annotations and retain crop mappings.** Locate candidate annotations. Produce recorded reading derivatives. Retain full view and leader/extension context. Output: Text-region crops with full-view references, pixel boxes and crop/deskew/resize mapping. Check: Crop/rotation coordinates map to original pixels; masks preserve inspectable glyph evidence.
2. **CAD-03-A02 — Recognize glyphs and parse engineering notation.** Recognize and preserve raw TSV. Parse literal tokens into separate quantity fields. Retain alternative reads and diagnostics. Output: Raw TSV and parsed candidates retaining literal strings, boxes, hierarchy, confidence and alternatives. Check: Every interpreted field traces to literal source tokens; uncertainty remains explicit.
3. **CAD-03-A03 — Associate text with geometric features.** Locate annotation line/leader and endpoints. Enumerate compatible feature links. Select supported association or retain alternatives. Output: Association records with label region, feature IDs, endpoints/axis, quantity kind and alternatives. Check: Independent reviewer checks meaning; software checks endpoint/axis and quantity consistency.
4. **CAD-03-A04 — Publish reviewed text and association evidence.** Verify controlling glyphs and associations. Record corrections/alternatives. Publish text and per-feature readiness. Output: Reviewed text with source/crop IDs, units/tolerances, associations and unresolved alternatives. Check: Each usable controlling dimension has source-linked literal and association checks.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent transcribes and associates source annotations using software evidence. |
| Software and agent | OCR proposes tokens; agent reviews notation/links; software checks fields. |
| Software handles ordinary cases | Demonstrated annotation classes run fixed parsing; ambiguous symbols/links enter review. |
| Deterministic supported case | Verified text/anchors plus explicit notation rules permit deterministic normalization and export. |

**Alternatives and target quality.** Manual transcription with independent source check. Mapped Tesseract crop candidates with raw TSV. Revision-matched vector dimension records when available. Arrangement labels and controlling precision dimensions retain distinct required review/coverage.

**Proposed helpers.** annotation-region helper emits mapped crops and contextual source locations. annotation parser consumes raw TSV/source context and emits typed candidates with unsupported/ambiguous flags. association helper returns candidate links, source locators and selected/ambiguous states. evidence exporter emits reviewed text plus structured companion records. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM compares original glyphs and line context; software compares quantities and endpoint associations. Combine complementary text/feature evidence; preserve conflicting values without averaging or confidence voting. Independently recheck every controlling merged annotation before downstream use.

**Migration condition.** Automate checked notation/association classes after glyph, decimal, tolerance, repeated-count, leader and ambiguous-feature fixtures; evaluate text and semantic association separately.

## 5. CAD-04 — Extract raster edges, lines and contours

**Entry points and evidence.** [OpenCV features](https://docs.opencv.org/4.13.0/dd/d1a/group__imgproc__feature.html) and [contours](https://docs.opencv.org/4.13.0/d3/dc0/group__imgproc__shape.html) supply HoughLinesP, findContours and approxPolyDP. [Potrace's paper](https://potrace.sourceforge.net/potrace.pdf) describes binary-image tracing into smooth Bézier curves, which are curves defined by control points.

1. **CAD-04-A01 — Separate stroke classes and inspect source regions.** Inspect classes in full view. Create candidate masks. Preserve uncertain/overlapping strokes. Output: Candidate masks for object, annotation, extension, centre and hidden strokes. Check: Overlay masks and confirm required features survive preprocessing.
2. **CAD-04-A02 — Fit source-supported vector candidates.** Extract line and contour candidates. Fit permitted geometry types. Map to plane coordinates with transform and uncertainty. Output: Segments/contours and separately typed arc candidates with support pixels and fit residuals. Check: Review local residual distribution and overlays; short/noisy arcs can retain multiple centres/radii.
3. **CAD-04-A03 — Check geometry and publish vector evidence.** Measure geometry/control differences. Review original-source overlays. Publish selected vector revision and handoff. Output: Vector-drawing with IDs, pixel mapping, topology findings and operation-specific readiness. Check: Check required holes/openings individually; silhouette agreement accompanies feature checks.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects strokes and geometry types, directs fitting and checks. |
| Software and agent | Software proposes curves; agent resolves classes/repairs. |
| Software handles ordinary cases | Checked line-art classes use fixed processing; uncertain roles/curves/gaps enter review. |
| Deterministic supported case | Explicit masks, mapping, curve classes and thresholds produce checked vector candidates. |

**Alternatives and target quality.** Manual source-mapped OCS/FreeCAD trace. OpenCV line/contour extraction with explicit semantic review. Documented learned segmentation as a separate model/weights/resource branch. Reduced arrangement outline and precision feature trace retain individual coverage/limits. Potrace's published binary-bitmap-to-Bezier-contour method supplies another curve-candidate branch; the paper supplies algorithm evidence and the future run identifies its actual executable, terms and settings.

**Proposed helpers.** stroke preflight emits source-mapped class masks and ambiguous regions. curve fitter consumes support pixels/class/criteria and emits typed alternatives, support sets and residuals. raster-vector audit outputs typed geometry, source map, change ledger and named check results. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM compares source overlays and class meaning; software measures controls/residuals/topology. Select compatible curves per feature; new joins retain lineage and explicit criteria. Recheck merged topology, independent dimensions and feature meaning before handoff.

**Migration condition.** Automate demonstrated stroke/curve classes after crossings, double strokes, hidden lines, short arcs, gaps and resolution fixtures.

## 6. CAD-05 — Convert raster floor-plan candidates into a wall and opening graph

**Entry points and evidence.** [Floor-plan recognition](https://openaccess.thecvf.com/content/CVPR2021/html/Lv_Residential_Floor_Plan_Recognition_and_Reconstruction_CVPR_2021_paper.html), [blueprint vectorization](https://openaccess.thecvf.com/content/ACCV2022/papers/Song_Vectorizing_Building_Blueprints_ACCV_2022_paper.pdf) and [structural reconstruction](https://diglib.eg.org/bitstream/handle/10.1111/cgf15007/v43i2_03_15007.pdf) supply research-method evidence. Source-mapped OCS/FreeCAD tracing supplies the manual branch.

1. **CAD-05-A01 — Declare plan conventions and wall/opening candidates.** Choose source-supported wall representation. Locate wall/junction/opening candidates. Retain ambiguous roles with source regions. Output: Wall edge/centreline convention, candidate walls/openings and source locations. Check: Semantic review checks each role against full plan/legend; orthogonality is conditional on source constraints.
2. **CAD-05-A02 — Construct dimensioned wall and opening relationships.** Assign stable node/wall/opening IDs. Connect only supported junctions and attach openings. Apply source dimensions and retain changes/constraints. Output: Graph nodes/wall edges/opening-host records encoded with vector-drawing metadata. Check: Check host existence and interval containment, coincident endpoints within criteria, room boundaries where meaningful and sourced angular relations.
3. **CAD-05-A03 — Verify plan graph and publish vector handoff.** Check geometry and relationships numerically. Compare source overlay and interpreted roles. Publish vector graph with retained alternatives and dimensions. Output: Checked vector-drawing plus graph/source metadata, measurements and per-element readiness. Check: Curved/nonorthogonal walls retain actual geometry; unsupported downstream curves are explicit route exceptions.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets plan symbols/junctions and directs graph construction/checks. |
| Software and agent | Software proposes adjacency/hosts; agent resolves roles and source dimensions. |
| Software handles ordinary cases | Demonstrated plan conventions process ordinary cases; ambiguous junctions/curves/openings enter review. |
| Deterministic supported case | Explicit wall paths, opening hosts, conventions and dimensions produce a checked graph. |

**Alternatives and target quality.** Manual wall/opening trace with source IDs. Line-candidate graph construction from CAD-04. Research segmentation/vectorization model with declared training/domain/runtime evidence. Arrangement graph preserves essential boundaries; dimensioned building graph requires each wall/opening criterion.

**Proposed helpers.** plan candidate ledger accepts traced vectors/measurements and returns wall/opening roles and convention alternatives. graph builder consumes candidates/conventions/criteria and emits nodes, wall paths, opening host/intervals and residuals. plan-graph verifier emits geometric/semantic findings and downstream element readiness. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM compares source symbols and candidate relationships; software checks controls/connectivity/hosts. Combine compatible wall/opening subgraphs through explicit junction remapping; preserve conflicting topology. Recheck graph integrity, source dimensions, required rooms/openings and independent semantics.

**Migration condition.** Migrate checked plan conventions after T/cross junction, curved wall, ambiguous door, nonorthogonal room, host conflict and missing dimension cases.

## 7. CAD-06 — Register orthographic drawing views in a shared coordinate frame

**Entry points and evidence.** [Orthographic matching research](https://xnjdxb.swjtu.edu.cn/en/article/id/9616) and [PlankAssembly](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html) supply method evidence with their input conditions. [CAD-R05](/home/leo/projects/3dmodeling/research/workflows/details/cad-r05.md) records the manual CAD route.

1. **CAD-06-A01 — Identify views and declare their projection frames.** Identify view regions and labels. Declare each view axes/direction/scale. Attach control and convention evidence. Output: View inventory with plane axes, viewing direction, scale, datum and convention evidence. Check: At least two identified views are available; auxiliary/section views have their own projection definition.
2. **CAD-06-A02 — Match source features and solve registration candidates.** Identify shared axes and candidate feature pairs. Estimate permitted view transforms. Compare dimensions and preserve alternate correspondences. Output: Per-view transforms and feature-correspondence alternatives with residuals. Check: Independent controls and shared-axis residuals check registration; equal projections can retain several 3D interpretations.
3. **CAD-06-A03 — Verify registration and publish reconstruction brief.** Validate cross-view controls and identities. Review feature correspondence semantics. Publish registered-view brief and unresolved dependencies. Output: Model-brief containing projection frames, correspondences, known dimensions, inferred/ambiguous fields and readiness. Check: Reconstruction readiness names features and source constraints; successful registration alone cannot choose among equal-projection shapes.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets view conventions and competing correspondences, directing projection checks. |
| Software and agent | Software matches axis-compatible features; agent reviews symmetry, hidden edges and sections. |
| Software handles ordinary cases | Checked view conventions/feature classes run registration; repeated features or conflicting scales enter review. |
| Deterministic supported case | Explicit view frames, feature correspondences and controls produce a checked registration brief. |

**Alternatives and target quality.** Manual alignment with exact view/source controls. Geometric axis/vertex matching for explicit conventions. Registered learned orthographic-reconstruction candidate method within its demonstrated object class. Arrangement view constraints and precision part correspondence retain different required features/criteria.

**Proposed helpers.** view manifest accepts vector bundle/metadata and outputs explicit view-to-model projection definitions. correspondence solver emits candidate links, transform receipts and contradictions from view manifests/vectors. registered-view brief exporter preserves frames, alternate matches and exact downstream prerequisites. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM examines full view set and source annotations; software compares independent coordinates/dimensions. Select coherent view/convention mapping; compatible correspondence evidence joins by source feature ID. Recheck all per-view transforms, controls and source associations before CAD-07.

**Migration condition.** Automate checked view-layout classes after convention reversal, mixed scale, repeated features, auxiliary views and contradictory dimension fixtures.

## 8. CAD-07 — Reconstruct a candidate 3D wireframe and surface from orthographic views

**Entry points and evidence.** [Wireframe reconstruction research](https://www.sciencedirect.com/science/article/pii/S0097849323000766) and [PlankAssembly](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_PlankAssembly_Robust_3D_Reconstruction_from_Three_Orthographic_Views_with_Learnt_ICCV_2023_paper.html) support candidate methods. [Point03 native construction](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md) defines actual supported kernel interfaces and output checks.

1. **CAD-07-A01 — Enumerate source-constrained 3D feature candidates.** Collect constraints from all views. Construct compatible 3D hypotheses. Retain dimension/hidden-feature alternatives and readiness. Output: Candidate vertex/edge/feature hypotheses with source-view links and unresolved degrees of freedom. Check: Every required coordinate/feature has source or explicit inference status; equal projections preserve alternatives.
2. **CAD-07-A02 — Construct candidate edges and bounded surfaces.** Create mapped edges/curves. Construct supported faces or explicit features. Query actual intermediate representation and failed boundaries. Output: Candidate wireframe/faces with feature IDs, source links and construction receipt. Check: Check projected edges and dimensions before sealing; open surface remains an intermediate artifact.
3. **CAD-07-A03 — Form and inspect the required solid.** Attempt the supported body formation. Query actual shape/solid structure. Compare required holes, interfaces and part count. Output: Actual solid candidate or retained incomplete surface state, with structure/geometry check report. Check: CAD-07 cad-solid readiness requires a closed valid supported shape; a surface/mesh alone retains its actual class.
4. **CAD-07-A04 — Project back to every view and publish checked geometry.** Project the actual candidate into every view. Compare independent dimensions and feature coverage. Read back saved output and publish typed geometry/measurements. Output: Checked cad-solid and measured feature set; source projections and saved-readback receipt accompany them. Check: A kernel-valid body with wrong hole/depth fails source checks; equal projections alone cannot resolve unseen geometry.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets competing 3D hypotheses and directs supported feature construction/checks. |
| Software and agent | Software solves projections and constructs explicit features; agent interprets hidden geometry. |
| Software handles ordinary cases | Demonstrated object/view classes reconstruct candidates; ambiguity, invalid boundaries or missing depth enters review. |
| Deterministic supported case | Explicit correspondences, dimensions and supported feature sequence produce a validated solid with all-view checks. |

**Alternatives and target quality.** Manual constrained feature reconstruction in supported CAD. Geometric wireframe/face reconstruction with typed intermediate states. Learned reconstruction candidate within its documented shape class followed by source checks. Lower-detail arrangement candidate and precision part model retain separate hidden-feature and interface requirements.

**Proposed helpers.** reconstruction hypothesis builder emits source-linked candidate edges/features and unresolved dependencies. reconstruction adapter consumes hypothesis/sequence and emits typed edges/faces plus lineage. solid readiness checker accepts candidate boundary/criteria and reports actual class and blocking boundaries. multiview verifier emits located edge/dimension residuals, feature coverage and unresolved alternatives. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM evaluates source interpretation; software measures all-view projections and required dimensions. Select a coherent shape or explicitly author compatible feature composition; retain equal-projection alternatives. New revision repeats solid validity, all-view dimensions/edges, feature semantics and saved readback.

**Migration condition.** Migrate demonstrated object classes after hidden-depth ambiguity, missing view, incorrect correspondence, open shell, wrong hole and projection-equivalent alternative cases.

## 9. CAD-17 — Build wall and opening solids from a confirmed floor-plan graph

**Entry points and evidence.** [Point03 CAD-10](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md) defines native operations and explicit preservation flags. [FreeCAD Part scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Part_scripting.md) documents native shape construction.

1. **CAD-17-A01 — Bind graph elements to sourced vertical parameters.** Read graph/source parameter revisions. Bind wall/opening local frames and vertical values. Check route support and named prerequisites. Output: Per-wall/opening feature plan with units/frame, host IDs and complete or blocked parameter states. Check: Required heights/thicknesses/opening parameters come from sources or explicit decisions; no values are filled from plan appearance.
2. **CAD-17-A02 — Construct walls and opening voids with retained identities.** Construct supported wall body in its declared frame. Create/place identified opening cutter and apply supported void operation. Read back actual wall/void geometry and group separate elements. Output: Wall solids, retained opening cutter/void records and assembly mapping with operation receipts. Check: Each opening affects only intended host geometry; assembly/group representation records actual available identity semantics.
3. **CAD-17-A03 — Validate plan, elevation and saved assembly.** Compare plan projection and controls. Measure vertical and opening features directly. Read back saved assembly and publish element-specific checks. Output: Checked CAD assembly with geometry/source manifest and readiness for named downstream use. Check: Plan projection alone cannot pass height/sill checks; separate wall/opening identity persists after save.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets sourced wall/opening parameters and directs native construction. |
| Software and agent | Software constructs explicit wall/cutter records; agent resolves junction/Boolean exceptions. |
| Software handles ordinary cases | Checked wall/curve classes use fixed construction; missing vertical values or unsupported joins enter review. |
| Deterministic supported case | Explicit graph, elevations, frame and supported feature sequence produce a checked assembly. |

**Alternatives and target quality.** Manual native wall/opening construction from the same graph. Parameterized supported wall/cutter family with explicit source values. Curved/nonorthogonal wall route through an evidenced backend or a named unsupported-feature exception. Plan-only arrangement remains a separate artifact; 3D building geometry requires its vertical parameters.

**Proposed helpers.** wall feature planner emits explicit wall/cutter construction records and feature-level blocking dependencies. wall assembly executor accepts feature records and emits wall/cutter handles, Boolean receipts and source mappings. wall assembly verifier emits plan/elevation/host comparisons and saved-revision mapping. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM compares plan/elevation meaning; software checks local geometry, hosts and dimensions. Combine compatible wall elements with explicit junction/opening mapping; fusion creates a new authored result. Recheck affected junctions, all openings, plan/elevation controls and saved identity mapping.

**Migration condition.** Automate demonstrated wall families after centreline/edge, curved junction, missing elevation, reversed sill, wrong-host cut and partial-Boolean cases.

## 10. DOM-02 — Raster sketch to constrained sketch

**Entry points and evidence.** [Original domain record](/home/leo/projects/3dmodeling/research/workflows/domain-paths.json) and [implementation plan](/home/leo/projects/3dmodeling/research/implementation-plan.md) define the composition. [Point03 CAD-09](/home/leo/projects/3dmodeling/research/action-audit/point-03-vector-and-solid.md) supplies actual native constraint and diagnostic requirements.

1. **DOM-02-A01 — Specify raster-backed sketch requirements.** Preserve raster and locate intended profile. Record controls and constraint sources. Select actual native constraint route. Output: Sketch intake record with source hash, controls, required constraints and route selection. Check: Dimension-only material routes to point01/point03; this raster procedure retains actual raster evidence.
2. **DOM-02-A02 — Compose calibrated vectors and source-linked constraints.** Reuse matching source-processing receipts. Map curves/dimensions to native IDs. Apply explicit constraints and query supported solver diagnostics. Output: Native sketch revision with pixel-to-curve-to-constraint map and reused action receipts. Check: Actual constraint data and source map are present; unavailable required diagnostics remain unresolved.
3. **DOM-02-A03 — Verify solved geometry and saved editability.** Measure solved features and independent controls. Review source overlay and constraints. Save/reopen within construction scope and publish checks. Output: Checked native constrained-sketch, source map and solver/dimensional/semantic report. Check: Correct solver state with wrong association fails semantic/dimensional source check; native constraints survive save.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets raster/freehand intent and directs calibrated tracing/constraints. |
| Software and agent | Software proposes OCR/vectors and solves explicit constraints; agent associates features. |
| Software handles ordinary cases | Checked raster/notation classes compose existing receipts; ambiguous geometry or unsupported diagnostics enters review. |
| Deterministic supported case | Verified pixels/measurements/feature links and explicit constraints produce a checked native sketch. |

**Alternatives and target quality.** Manual source-mapped constrained tracing. OpenCV/OCR-assisted extraction followed by native constraints. Existing source vector route through DOM-03 when that artifact is actually supplied. Arrangement sketch retains freehand estimates; precision profile requires its controlling source dimensions.

**Proposed helpers.** raster-sketch intake emits feature/constraint requirements and source-evidence prerequisites. raster-sketch composer maps source feature records into native geometry/constraints and retains all upstream receipts. raster-sketch verifier outputs source, solver and saved-editability results separately. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM reviews full-view and constraint/source links; software compares dimensions and solver movement. Combine compatible feature evidence/constraints with recorded IDs; contradictory values remain alternatives. Recompute solver/closure, independent controls, source semantics and native saved editability.

**Migration condition.** Migrate checked raster/constraint families after freehand scale, ambiguous glyph, wrong feature association, contradictory constraints and missing diagnostics cases.

## 11. DOM-18 — Raster floor plan to IFC building

**Entry points and evidence.** [IfcOpenShell geometry](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html) and [feature.add_feature](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/feature/add_feature/index.html) document element geometry and host relationships. [DOM-R01](/home/leo/projects/3dmodeling/research/workflows/details/dom-r01.md) records context, units, placement and hierarchy entrypoints.

1. **DOM-18-A01 — Bind all five inputs and element-level building requirements.** Register all five input records. Bind plan/vertical dimensions and reused asset terms. Select compatible graph/geometry receipts or named construction route. Output: Building intake manifest with all five input revisions, element requirements and source-asset terms. Check: Each required element has source-backed geometry/semantic prerequisites; library terms attach to actual reused items.
2. **DOM-18-A02 — Create explicit IFC identity, units and spatial structure.** Create named schema document, units and contexts. Create source-linked spatial elements. Assign declared hierarchy/placements and inspect relationships. Output: IFC document with unique identities, units, representation contexts and spatial hierarchy. Check: Schema/unit and unique-ID checks pass; source storey elevations and local/world transforms match declared frames.
3. **DOM-18-A03 — Author placed wall/opening geometry and host relations.** Create/place wall and opening elements with source-linked representations. Attach existing opening to intended host through explicit void relation. Query geometry, placements, containment and relationship identities. Output: Placed IfcWall/IfcOpeningElement records, representations and explicit host void relationships with source mapping. Check: Element creation, representation/placement and host relation are separately checked; relation API consumes an existing opening. Actual opening geometry is evaluated/queried using the selected supported implementation.
4. **DOM-18-A04 — Validate saved IFC geometry and semantics.** Save and reopen exact IFC output. Measure plan/vertical features and inspect relations/containment. Independently review semantics and publish evidence with readiness. Output: Saved IFC hash, reopened geometry/relationship findings, source/ID map and downstream readiness. Check: Valid schema alone cannot pass wrong host/units/height; required void is checked in evaluated geometry and relation graph.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets source building semantics and directs explicit IFC creation/checks. |
| Software and agent | Software authors explicit geometry/relations; agent resolves classifications, hosts and source ambiguity. |
| Software handles ordinary cases | Demonstrated plan/element classes use checked adapters; unsupported walls, terms, hierarchy or openings enter review. |
| Deterministic supported case | All five inputs, element classes/parameters/placements and supported APIs are explicit; geometry and relation checks are fixed. |

**Alternatives and target quality.** Manual source-linked IFC authoring in Bonsai/IfcOpenShell. Reviewed CAD-05 graph directly drives supported IFC wall/opening families. CAD-17 geometry reuse with an evidenced adapter and separately authored IFC identity/relations. Plan layout and dimensioned semantic building deliverables retain distinct coverage, vertical parameters and validation requirements.

**Proposed helpers.** building intake binder emits linked source/control/asset/element manifest and feature prerequisites. IFC context builder consumes semantic/placement records and emits identity/units/context hierarchy receipts. building element adapter accepts wall/opening/placement records and emits geometry, identity and host-relation receipts. IFC source verifier emits separate schema, relationship, dimensional, projection and source-correspondence reports. Each helper's inputs, outputs, dependency and checks are recorded under its action ID.

**Selection and merge.** VLM compares source roles/host meaning; software checks dimensions, placement and relationship graphs. Merge compatible element/metadata contributions with explicit identity remap and asset terms; preserve conflicting classifications. New IFC revision repeats schema/identity, placement, host void, dimensional, projection and independent semantic checks.

**Migration condition.** Automate checked building element classes after wrong host, units, reversed local axes, missing elevations, duplicate IDs, curved-wall exception and save/reopen fixtures.

## 12. Representation and failure boundaries

1. **Image placement:** OCS [embed_image](/home/leo/projects/3rdparty/OpenCADStudio/docs/automation/API-SPEC.md) supplies position/width and linked/embedded underlay modes. The [image command](/home/leo/projects/3rdparty/OpenCADStudio/src/modules/draw/draw/raster_image.rs) has a pixel-derived display-width fallback. Metric calibration requires the explicit control/mapping receipt.
2. **Curve candidates:** OpenCV contours and polygon simplification retain their actual curve class and residual. A fitted arc needs its own support pixels, estimator and uncertainty. Research floor-plan methods and Potrace's algorithm paper provide method evidence; runtime, model weights, executable version and terms belong to the selected future execution.
3. **Multiview geometry:** repeated features, hidden edges and equal projections can leave several candidates. CAD-07 publishes cad-solid readiness only for an actual closed valid supported shape. Its intermediate edges/faces and unresolved hidden-feature alternatives remain identified.
4. **Wall geometry:** curved/nonorthogonal walls retain their source geometry or a specific backend-support exception. Wall thickness convention, floor datum and vertical/opening dimensions are sourced prerequisites. Native wall/cutter operations use point03's explicit preservation flags. Opening cutters/void records retain their meaning separately from physical wall components.
5. **IFC authoring:** DOM-18 retains raster-plan, dimensions, measurement-set, source-library and model-brief. Create element identity, representation and placement before attaching an existing opening to its host with `feature.add_feature`; the voiding call returns `IfcRelVoidsElement`. Record actual geometry evaluation and check the visible void separately from the relationship. Local wall axes, thickness side and placement `is_si` setting remain explicit.
6. **Independent validation:** numerical checks identify actual geometry, source feature and query/reader. Separate semantic reviewer execution checks glyphs, feature associations, hidden-edge interpretation and wall/opening identity. Record shared pixels, recognizers, model families and kernels so correlated evidence remains visible.
7. **Interrupted actions:** retain original/working hashes, mapping/configuration, raw OCR, candidate feature IDs, partial artifacts and request/response identity. Reconcile native state or remote completion before retry. Malformed selections preserve the previous validated artifact. A changed transform invalidates dependent coordinates; a changed glyph/association invalidates that feature claim and its descendants.
8. **Saved verification:** the generating action writes only its scoped output; verification reopens the exact supplied artifact read-only. Schema validity, kernel validity, dimensional agreement, source identity and required native editability receive separate results.

## 13. Resource and goal selection

| Operation | Local processing basis | Remote inference and manual effort |
| --- | --- | --- |
| CAD-02 plane mapping | Metadata and few controls precede full pixel warping; cost follows output pixels and mapping type | Plane/control interpretation, point selection and additional source measurements |
| CAD-03 annotation reading | Bounded crops precede whole-page OCR; cost follows pixels, language data and candidate count | Glyph/feature association and source transcription review |
| CAD-04 vector candidates | Masks/contours and bounded fits; cost follows pixels, support chains and intersection candidates | Stroke classes, arc/line meaning and local manual traces |
| CAD-05 plan graph | Indexed paths, adjacency and host checks; cost follows graph/intersection size | Wall/opening symbols, junction conventions and conflicting hosts |
| CAD-06 view registration | Projection/control checks and constrained feature matching | View convention, repeated-feature and section interpretation |
| CAD-07 reconstruction | Candidate count, curve/face complexity and kernel operations | Hidden-feature hypotheses and source-supported selection |
| CAD-17 wall solids | Source parameter checks precede wall/cut geometry; cost follows faces and openings | Junction/host intent and bounded failed-feature diagnosis |
| DOM-02 constrained sketch | Reuse matching upstream receipts; solver work follows curves and relations | Constraint-to-source association and freehand meaning |
| DOM-18 semantic building | Input/hierarchy checks precede geometry evaluation; cost follows elements/faces/voids | Classification, host meaning, reuse terms and source verification |

These are conditional qualitative estimates. Actual measurements record fixture, source size, tool/build, hardware, settings, elapsed processing and memory. Local graphics use belongs to the actual display/processing backend. Remote calls, tokens, latency/cost and manual effort have separate records. A learned-processing branch states its model/weights and hardware conditions before resource comparison.

Initial ambiguous sources can use higher reasoning effort for feature interpretation and competing hypotheses. Explicit checked controls, annotations, graph records and construction parameters support software-led processing. Migration applies to the demonstrated action/input class after authorized implementation and tests; the four per-operation modes retain exception routes.

## 14. Future checked cases

The [structured records](/home/leo/projects/3dmodeling/research/action-audit/point-04-operations.json) specify expected outcomes per operation. Future fixtures supply actual source values and criteria before execution.

1. **Plane and mapping:** degenerate/reordered controls, single-length perspective ambiguity, withheld-control failure, regional page deformation, crop/resize/warp/lens-map composition and outside-domain coordinates. Preserve original pixels and distinguish page rectification from freehand object proportions.
2. **Text and curves:** plausible high-confidence wrong glyph, decimal/radius/diameter/tolerance/count confusion, correct text attached to the wrong feature, crossed annotation strokes, double strokes, lost narrow slot, short-arc ambiguity and excessive gap repair.
3. **Graphs and views:** curved/nonorthogonal wall, competing opening hosts, centreline/edge convention, duplicate merged IDs, projection-convention reversal, mixed view scales, repeated features, missing view and multiple shapes with equal projections.
4. **Geometry and IFC:** open surface failing cad-solid, wrong hidden hole, missing vertical dimensions, reversed sill/axis, unintended adjacent-wall cut, lost native constraints, each missing DOM-18 input, wrong host/storey/units and separately evaluated void geometry.
5. **Branches and resumption:** lost VLM response, malformed selection rows, changed source, shared OCR error and different arrangement/precision readiness. Retain raw/request evidence and retry lineage; publish merged changes only after valid source-linked selections and repeat required checks on the new revision.

[Designer notes](/home/leo/projects/3dmodeling/research/action-audit/reviews/point-04-designer.md) record source summaries, original-contract findings, review changes and static documentary checks.
