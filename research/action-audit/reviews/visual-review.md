# Visual interpretation review — descriptions and explicit dimensions to a model brief

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Registration date: 2026-11-12. Status: documentation review completed; procedure additions below are proposals. Scope: generic **CAD-01 — Extract a model brief from text and dimensions** and **DOM-01 — Normalize model brief**, with optional supporting images or drawings. The reviewed material is the existing local workflow documentation and source register. This review uses no model specimen and reports no image interpretation or geometry execution result.

Dispatcher identifier: `gpt-6.1-sol`; requested reasoning setting: `xhigh`. Actual executing model identity: unavailable in this agent environment. These dispatcher settings identify the assignment; they supply no measured performance result.

## 1. Proposed operation boundary

1. Preserve the supplied description, dimension records and optional source views as the input revision. Extract component names, dimensions, relations, required outputs and intended use into a source-linked model brief.
2. Use a reasoning language model for text interpretation. Use a **VLM — vision-language model**, a model that accepts images and text, when the task includes image content. Record each proposed interpretation beside the source passage or image region that supports it.
3. Produce a brief, a feature evidence matrix, conflicts, dependent questions and per-feature readiness. Geometry construction consumes that brief through an explicitly scoped later operation.
4. Preserve the current [implementation plan](../../implementation-plan.md), including its stages. These proposals expand its intake and verification detail. They use the branch, evidence-merge and version handoffs in [workflow composition rules](../../workflows/composition-rules.md).

The [CAD-R01 text/dimensions recipe](../../workflows/details/cad-r01.md) describes a simple plate fixture with a centre datum and millimetres. A generic brief records the source job's unit, datum and axes. The fixture convention applies when that fixture is the task. The [DOM-R01 building recipe](../../workflows/details/dom-r01.md) expands DOM-01 into IFC, survey and reconstruction operations; the present point ends at brief intake.

## 2. Proposed reasoning tasks and retained outputs

Every task below is a proposed use of model reasoning. The existing local sources establish the workflow contracts and software operations cited here. A later authorized run can measure a particular model's extraction results against a supplied specimen.

| Action | Text-only reasoning input | Additional VLM action when views are supplied | Retained output |
| --- | --- | --- | --- |
| 1. Name components and features | Resolve named objects, occurrences and references such as a hole in a named plate | Locate the corresponding visible component and feature in each relevant view | Readable name, stable ID, occurrence ID, source spans/regions, candidate correspondences |
| 2. Transcribe explicit dimensions | Copy values, unit symbols, ranges and tolerance statements literally | Read the dimension label, symbol and extension-line endpoints in a cited region; compare OCR candidates with the original pixels | Raw string, parsed candidate, unit, measured feature, reading status |
| 3. Interpret engineering meaning | Resolve radius versus diameter, overall versus local dimensions, quantity, direction and relation wording | Distinguish object edges, hidden lines, centre lines, dimension lines, section marks and annotations where the view supports that reading | Feature meaning and relation claim with its supporting passage/region |
| 4. Associate views | Match repeated names and explicit references between text sections | Propose which projections show the same component, axis or feature; preserve alternative correspondences | Source-view pair, orientation claim and correspondence evidence |
| 5. Compare constraints | Find incompatible statements, duplicate values and dependencies | Compare labels and view relations for the same feature; identify a visible orientation or association conflict | Conflict record containing each candidate and source |
| 6. Identify required decisions | State the exact input needed for a dependent feature | Point to the affected source view and explain the alternative readings | Open question, affected feature IDs and blocked action |
| 7. Assess branch output | Compare each branch's extraction with the original wording and required output | Compare each proposed image reading with the cited full view and crop | Per-row retain, combine, reject or request-input action with evidence |
| 8. Inspect the merged brief | Re-read it for changed meaning, component identity and relations | Check that retained labels and view correspondences still refer to the intended visible features | Semantic review result tied to the brief revision |

The VLM can propose that two visible circles represent the same bore. The evidence matrix must state which views and labels support that interpretation. Software can then check whether the proposed constraints are internally consistent. The feature's source identity remains part of the semantic review.

## 3. Proposed first iterations and branch variants

1. Use a high reasoning setting in the first extraction and first independent evidence review when the selected model exposes that setting. Concentrate those iterations on component identity, controlling dimensions, ambiguity and source correspondence. Record the actual model identifier, exposed reasoning setting, input revision and outcome. This is an experiment proposal; the setting supplies no accuracy guarantee.
2. Begin with a text-only branch when the description and dimension table carry the required meaning. Add a VLM branch for relevant supporting views. A view is relevant when it supplies a feature association, dimension, orientation or conflict check required by the goal.
3. Compare branches on the same source revision, required features, unit/frame record and identity map. Record differences before merging. Parallel execution is an option for a separately authorized run; sequential branches can use the same comparison procedure.

| Proposed branch | Goal and output detail | Source-reading effort | Comparison result to record |
| --- | --- | --- | --- |
| Required-feature branch | Extract the components and parameters that control the requested deliverable | Read all controlling source statements and relevant views | Required-feature coverage, correct source links, conflicts, blocked dependencies |
| Expanded-feature branch | Also extract supported secondary features, annotations and downstream relations | Inspect additional source regions and view correspondences | Added supported features, added interpretation conflicts, review time |
| Independent reading branch | Re-read the same required features with a separate extraction instruction or model call | Inspect the same evidence without adopting the first branch's candidate readings | Agreement by field, source-supported corrections and remaining alternatives |
| Critical-feature branch | Inspect the features whose error affects the requested use most directly | Re-read exact source labels, units, tolerances, axes and interface relations for those features | Exact value/association checks and each dependent operation's readiness |

Detailedness, dimensional accuracy, semantic correctness and execution cost are separate comparison axes. An expanded feature list adds detail. Accuracy is assessed against the source and independent controls appropriate to the feature. Two branches repeating the same inferred value retain one inference with two review results; the duplicate reading adds no independent measurement.

## 4. Proposed evidence matrix and source coordinates

Use one row per feature parameter or semantic relation. The matrix records the following fields; a job fills them from actual inputs.

| Field group | Contents |
| --- | --- |
| Identity | Brief revision, component ID/readable name, occurrence ID, feature ID/readable name, parameter or relation name |
| Original evidence | Source ID, original URL/local path, hash, supplied text span or source image/page identity, raw dimension string |
| Interpretation | Literal source claim, parsed candidate, value/range, unit, datum/frame, feature association, interpretation rationale |
| Evidence class | Supplied instruction, measurement, drawing annotation, manufacturer/source claim, calculated value, inferred interpretation or proposed value |
| Image location | Full-image pixel dimensions and orientation, page identifier, crop bounds, annotation endpoints and associated view |
| Transformation | Source-to-working-image transform and direction, unit conversion factor, source-to-model frame transform when applicable |
| Branch review | Branch/call identity, candidate reading, supporting evidence, conflict, VLM review action and rationale |
| Required check | Quantity/relation to check, source of tolerance or criterion, check tool, feature dependencies |
| State | Ready for the named next operation, or blocked with its exact prerequisite/question; retain other eligible features |

Proposed coordinate procedure:

1. Retain each original image and drawing page unchanged. Record its source identity, file hash, pixel width/height and applied display orientation. For text, record exact lines or character spans against the retained revision.
2. Give a PDF page both a stable page index convention and its displayed page label. If a page is rasterized later, record the raster size, rendering resolution, page rotation, page box and page-to-image transform. This preserves correspondence between page coordinates and pixels.
3. Express a crop as `x_min`, `y_min`, `x_max`, `y_max` in the original oriented image coordinate system. Record the pixel origin and axis directions. Record scaling, deskew, rotation and crop translation so a point in the working crop can be mapped back to the original.
4. Cite the dimension label region and the endpoints/features to which the label applies. A text box around the digits supplies a transcription location; the feature association also needs the leader, extension lines or explicit text relation.
5. Retain a full view beside the crop during review. The crop supplies glyph detail; the full view supplies component and projection context. A proposed crop records intended coordinates; an executed crop additionally records the produced file and transform.

This extends the existing [CAD-R02 raster interpretation procedure](../../workflows/details/cad-r02.md), which retains original pixels, OCR boxes, control points, transformations and feature associations.

## 5. Proposed VLM comparison and merge actions

1. **Prepare:** give the reviewer the original sources, required output, common unit/frame/identity record, branch outputs and feature evidence matrix. Include the cited source passages and views so the reviewer can examine each disagreement.
2. **Compare:** examine rows by component, feature and parameter. Classify a difference as transcription, unit conversion, coordinate transform, feature association, relation interpretation, evidence conflict or added detail.
3. **Retain:** choose a candidate whose reading matches the cited evidence and record why. Preserve the branch candidate and reviewer decision separately. A later correction can then be traced to its original reading.
4. **Combine:** retain complementary dimensions or relations when their feature identities, frames and sources agree. Record each input row and the merged output row. Separate source evidence from a calculated value derived from that evidence.
5. **Resolve explicit corrections:** apply a supplied correction to its stated feature and scope; retain the superseded source and correction relationship. Recency alone supplies no authority for an unrelated component.
6. **Preserve conflicts:** retain incompatible source values and alternative associations. Ask the exact open question needed for the affected feature. Averaging incompatible dimensions or selecting a majority reading would create a new value without source support.
7. **Select by goal:** compare the retained supported features against the requested deliverable. A display layout, an interface model, a robot joint and a house analysis can require different fields and checks. Record the selected branch contents as a proposal unless the supplied task already defines that content.
8. **Publish the merged brief revision:** retain its input source revision, selected rows, excluded candidate rows with reasons, feature states and downstream dependencies. Rerun checks on the merged values and relations.

Common handoff rules come from [composition rules](../../workflows/composition-rules.md) and the OCS model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`): explicit units, right-handed frame, named datum, axis meanings, separate parts, interfaces and motion. Preserve a component's definition separately from an occurrence placement. Store source-to-target transform direction and numerical unit factor. Keep image pixel, drawing plane, local component, assembly and map frames individually identified when present.

## 6. Proposed numerical and semantic checks after merge

1. **Numerical intake checks:** verify that each parsed value reproduces the cited source string, retains its unit and tolerance, and refers to the named parameter. Recompute explicit unit conversions. Check duplicate parameter names, range ordering and dimensional consistency. Record applicable domain constraints; signed offsets can be negative and a source quantity must retain its meaning.
2. **Constraint consistency checks:** compare relations such as sums of explicit dimension chains, shared axes or repeated features when those relations are part of the supplied description. A mismatch creates a conflict row; the check preserves both source values. A satisfied relation records internal consistency for the supplied inputs.
3. **Semantic checks:** inspect component identity, diameter/radius meaning, centre/edge datum, handedness, quantity, host/child relation, separate versus fused parts, joint parent/child and opening host where relevant. Confirm that the numerical check measured the intended feature.
4. **Visual correspondence checks:** compare each retained view assignment, endpoint association and label with its source. Inspect orientation and hidden/visible feature interpretation. A display overlay can expose a mismatch for a further measured check.
5. **Future geometry checks:** when a later authorized modeling operation produces geometry, measure the saved model revision, part IDs/handles, bounds, relevant features and exported artifact hash with the owning application or independent importer. Inspect corresponding orthographic views of that same geometry revision.
6. **Future downstream semantic checks:** compare IFC element identity/containment or robot link/joint records with the brief when those consumers are in scope. Preserve the mapping through any visual derivative.

The OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) prescribes readback tied to the actual document revision and corresponding orthographic views. Its model-contract checker (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) checks supplied point/axis/plane numbers and caller-supplied provenance. A report must name whether its numbers came from an actual CAD query, a declared design input or a synthetic fixture.

## 7. Proposed per-feature tolerance and readiness

1. Record the intended use beside each required feature. A robot joint can require axis location/direction, connection identity, motion range and interface geometry. A house task can require wall/opening dimensions, storey placement, semantic quantities or a visual arrangement according to its goal. The brief selects the relevant fields from that goal.
2. Attach each tolerance to the particular quantity and operation, with units, source and evidence class. Preserve separately a source dimension tolerance, measurement uncertainty, image/reconstruction residual criterion, CAD solver criterion and export comparison tolerance. Their meanings and source evidence differ.
3. Obtain the numerical criterion from supplied requirements, source specifications or an explicit decision within the task. A proposal for a tolerance remains labelled as a proposal. This procedural review assigns no numerical tolerances.
4. Mark a feature **READY — source extraction** when its literal value and source association are recorded; mark **READY — geometry input** when its required values, datum, part boundary and interpretation permit the named geometry action. Record readiness against the intended action and brief revision.
5. Mark an affected feature **BLOCKED — named prerequisite** when a conflict, unreadable label or required interpretation prevents that action. Retain independent eligible features and list dependencies. A blocked opening interpretation can coexist with ready wall dimensions; a blocked joint axis can coexist with ready link names and sourced dimensions.
6. An assembly operation consumes its required feature states. If a blocked feature controls another placement, carry that dependency to the affected placement. A dimensional validation state requires its own criterion and actual measured result.

## 8. Proposed responsibilities and resource axes

| Participant or tool | Concrete work | Evidence/output |
| --- | --- | --- |
| Reasoning language model | Extract wording, identify relations and conflicts, prepare questions, compare text branches | Proposed feature records and source-span links |
| VLM | Read source views, propose label-to-feature correspondence, compare branch evidence, inspect merged semantic meaning | Proposed readings and region-linked review actions |
| OCR software | Return candidate strings and bounding boxes | OCR text, boxes and candidate confidence from the recorded software |
| Image/calibration software | Apply declared crop/rotation/rectification and compute transforms | Working images, source mappings, controls and residuals |
| Deterministic brief-checking software | Check records, identifiers, units, conversions and declared constraints when implemented | Per-check input/output and failure records |
| CAD application and importer | Construct authorized geometry later; read back actual dimensions, topology and revision | Native source, measured result and checked derivative |
| User | Supply the intended goal and required decisions; resolve interpretations requiring new intent, scope or acceptance | Exact response/correction and its affected features |

The software entry points are documented in [CAD-R02](../../workflows/details/cad-r02.md) and the [CAD source records](../../sources/round-02/cad-sources.json). A reusable brief checker and its adapter remain implementation proposals in the [implementation plan](../../implementation-plan.md).

| Resource axis | Local run record | Remote run record |
| --- | --- | --- |
| Model identity | Actual loaded model/revision, exposed reasoning setting, runtime/backend | Actual service/model identifier returned by the service, exposed reasoning setting, service/API revision |
| Input size | Text length, page/image count, pixel dimensions, crops, context size | Same values plus transmitted artifacts/regions |
| Compute and memory | CPU/GPU, RAM/VRAM peak, elapsed time, concurrent calls | Reported usage, latency, queue time and available execution metadata |
| Storage and provenance | Original and derivative paths/hashes, output revision, logs | Uploaded input identity/hash, returned artifact identity/hash, retained local response |
| Cost | Measured resource use and any stated cost basis | Recorded charged units, price source/date and actual billed cost where available |
| Task outcome | Correct value/association checks, supported-feature coverage, conflicts and questions | Same task checks against the same source revision |

Model location, model size, image detail, number of branches and reasoning effort are separate resource choices. Compare observed results for the same goal and specimen. A local VLM needs the hardware/runtime of its actual selected model; a remote service has its own usage and input-transfer conditions. This review supplies recording fields rather than hardware or service prices.

## 9. Proposed validation cases

These are case definitions for a future authorized validation batch. Each case needs retained input evidence and expected outcomes before execution.

1. **Text and explicit dimensions:** extraction preserves the supplied values, units, names and relations; a text-only branch can complete intake without adding a visual branch.
2. **Engineering notation:** a drawing includes diameter/radius, tolerance, decimal and repeated-feature notation; compare parsed readings and feature associations against a checked transcription.
3. **Source conflict:** two sources give different values for one feature; the merged brief retains both and blocks the dependent action with a precise question.
4. **Mixed units and frames:** equivalent dimensions and a supplied axis mapping appear in different source conventions; compare conversions and identity mapping with the declared expected mapping.
5. **Crop context:** a dimension label and its feature endpoints require different parts of the full view; verify original-to-crop correspondence and retained feature identity.
6. **Ambiguous projection:** two view associations satisfy the written numbers; semantic review preserves the alternatives and identifies the source/decision needed to choose.
7. **Independent eligible features:** one feature has a conflict while another supplies complete input; verify separate readiness and dependency propagation.
8. **Robot-joint goal:** compare axis, parent/child, interface and supplied tolerance fields with a checked brief, then reserve geometry readback for the later modeling operation.
9. **House goal:** compare only the wall/opening, level, quantity or visual fields required by the supplied task; preserve its feature-specific criteria.
10. **Branch merge regression:** an expanded branch adds supported details; verify controlling values and identities against the same baseline and preserve each added feature's evidence.
11. **Visualization and metric evidence:** an appearance view suggests a feature while a dimensioned source defines its value; verify the retained evidence class and source association for each claim.

Visualization supplies context, visible correspondence and review findings. Metric claims carry a named measured quantity, units, source controls or supplied dimensions, tolerance/criterion and the checked artifact revision. The [reconstruction assessment](../../reconstruction.md) already separates appearance, scale controls, independent measurements and inferred geometry.

## 10. Local evidence and original-source relationships

All records below were read or registered from local files on 2026-11-12. External links identify original sources already present in those records; this review performs no external inspection.

| Read local evidence | Concrete summary and use in this review | Evidence status |
| --- | --- | --- |
| [Implementation plan](../../implementation-plan.md) | Defines source-linked intake, geometry adapters, representation ownership, staged work and saved-artifact verification | Local proposal inspected |
| [Workflow composition rules](../../workflows/composition-rules.md) | Defines branch, evidence merge, identity, units/frames, dimensional evidence and version/check handoffs | Local proposal inspected |
| [CAD-R01 text/dimensions recipe](../../workflows/details/cad-r01.md) | Connects CAD-01 to source-preserving intake and identifies the plate fixture's example datum convention | Existing local assessment inspected |
| [DOM-R01 building recipe](../../workflows/details/dom-r01.md) | Records DOM-01 and its larger building/IFC route; establishes the separation between generic intake and building operations | Existing local assessment inspected |
| [CAD-R02 raster recipe](../../workflows/details/cad-r02.md) | Records OCR candidates, boxes, original pixels, transforms, view/feature association and review | Existing local assessment inspected |
| OCS Engineering skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) | Defines explicit modeling contract, source-view review, revision-bound measurements and same-model orthographic review | Local skill inspected |
| OCS model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) | Defines units, right-handed frames, separate components, source tolerances and point/axis/plane check limits | Local skill reference inspected |
| [CAD source register, round 2](../../sources/round-02/cad-sources.json) and [round 3](../../sources/round-03/cad-detail-sources.json) | Preserve original sources for Tesseract OCR, OpenCV transforms/calibration, FreeCAD constraints and CAD readback methods | Existing source records inspected; original external pages retained at their recorded status |
| [Domain source register, round 2](../../sources/round-02/domain-sources.json) and [round 3](../../sources/round-03/domain-detail-sources.json) | Preserve IFC and robot identity, unit, placement and semantic source relationships used in the proposed goal examples | Existing source records inspected; original external pages retained at their recorded status |
| [Reconstruction assessment](../../reconstruction.md) and [round-2 source records](../../sources/round-02/reconstruction-sources.json) | Separate visual appearance, image geometry, calibrated controls, scale, independent checks and inferred surfaces | Existing local assessment and source records inspected |

Original links retained through the existing source records:

1. [Tesseract command-line usage](https://github.com/tesseract-ocr/tessdoc/blob/main/Command-Line-Usage.md): OCR/TSV entry point underlying candidate strings and boxes. Existing-record status: `existing_report_registered` in round-3 CAD detail records.
2. [OpenCV geometric image transformations](https://docs.opencv.org/4.13.0/da/d54/group__imgproc__transform.html): image warp/transform operation underlying retained crop/rectification mappings. Existing-record status: `existing_report_registered` in round-3 CAD detail records.
3. [OpenCV camera calibration tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html): known object/image correspondences, intrinsic/distortion estimation and undistortion. Existing-record status: `web_inspected` in round-2 reconstruction records; this review uses that registered summary.
4. [FreeCAD Sketcher scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md): geometry creation and geometric/dimensional constraints. Existing-record status: `web_inspected` in round-2 CAD records; this review uses that registered summary.
5. [IfcOpenShell geometry creation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html): supplied geometry, placements and IFC authoring in the larger building route. Existing-record status: `web_inspected` in round-2 domain records; this review uses that registered summary.
6. [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst): body tree, local frames and model/compiler structure used by the robot-goal example. Existing-record status: `web_inspected` in round-2 domain records; this review uses that registered summary.

## 11. Review result and integration recommendations

1. **DONE — local visual/procedure review.** The written procedure proposals cover text-only reasoning, optional image reasoning, first-iteration effort, feature evidence, branch comparison, merge decisions, source coordinates, numerical/semantic checks, per-feature criteria and resource recording.
2. Add those operations to the point-01 audit as proposals. Keep the merged brief as the point's output and retain geometry construction as its downstream operation.
3. Register this review and the OCS model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) in the coordinating source-documentation batch, with their referring audit documents. The coordinator owns that source-register change and the batch commits.
