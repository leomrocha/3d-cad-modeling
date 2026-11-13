# Point 02 visual, semantic and evidence-merge review

Registration date: 2026-11-12. Status: **DONE — local documentary review**. The procedures, component designs and validation cases below are proposals. Scope: **CAD-12 — Assemble existing CAD or source-library components; DOM-06 — Library asset intake and rights record; DOM-07 — Place reusable component in assembly; DOM-26 — Version and reuse component revision; DOM-38 — Import STEP solid into CAD representation; DOM-39 — Export STEP assembly**.

Requested assignment: `gpt-6.1-sol`, reasoning effort `xhigh`. Actual executing model identity: **unavailable in this agent environment**. Local operation records, reports, source-register entries and the OCS engineering contract were inspected. Original external URLs below are reused from those records. This review's executed result is this document; the examples describe future validation cases.

## 1. Findings for the point-02 procedure

1. **Asset identity and occurrence identity are separate.** A component definition has a source, revision and geometry. An assembly occurrence has its own identity, transform and parent. CAD-12 requires a named base plus a distinct component occurrence; DOM-07 inserts or places a component with its source geometry retained. A repeated component can have one geometry hash and several occurrence paths. The [original operation records](../../workflows/cad-paths.json), [domain operation records](../../workflows/domain-paths.json) and [component assessment](../../domains-and-components.md) establish these roles.
2. **Visual inspection supplies correspondence and arrangement findings.** It can identify a reversed component, a missing occurrence, a different visible bore pattern or a suspicious contact. A dimensional finding carries the named feature, its source value, required criterion and measurement from the particular geometry revision. Use the OCS model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) for the boundary between supplied numbers and application measurements.
3. **Selection depends on the intended use and the affected features.** A component envelope can support a sketch arrangement. A robot joint interface needs its specified mounting and axis evidence. A building task can require opening dimensions, storey placement and semantic identity. The [audit plan](../plan.md) assigns criteria per feature and purpose; its robot and building examples supply no universal dimensional threshold.
4. **STEP inspection records the actual geometry and structure.** Record analytic faces, faceted faces, meshes, valid solids, product definitions and occurrences as returned by the chosen importer. The [local baseline](../../local-baseline.md) records that the inspected OCS STEP writer consumes triangles and writes planar faces. A source component's incoming representation and a derivative's representation each receive their own record.
5. **Candidate substitution and feature combination have different outputs.** Substitution selects an identified component revision and revises its occurrence dependencies. Combining a mounting pattern from one item with an envelope from another creates an authored candidate when those features describe different parts or revisions. Record that candidate's own identity, feature lineage and scoped construction action.
6. **A merge creates its own checked revision.** Matching source frames and passing branch checks are prerequisites. Recheck the merged component/assembly's identities, transforms, controlling interfaces and exported result. A branch's pass belongs to its checked revision. The [composition rules](../../workflows/composition-rules.md) define this handoff.
7. **Export requires an export-specific receipt.** DOM-39 consumes a native assembly revision and pinned component revisions, then creates a new STEP artifact. Its receipt records the output hash, product/occurrence mapping, placements, units, names and changed fields. Reopen that artifact in an independent supported consumer and compare the part tree and controlling geometry. The original DOM-39 record shares import/export prose; the point-02 definition should state the export input and output explicitly.
8. **Aggregate checks and semantic checks complement each other.** Equal bounds, solid count or volume can coexist with a changed bore, wrong occurrence identity or wrong placement. Preserve the aggregate measurements, then check the particular interface and relation required by the brief.

## 2. Proposed inspection evidence package

A **VLM — vision-language model** processes images and language together. For this point, its inputs are source views, component descriptions, geometry-query results and branch records. Its output is a source-linked interpretation or selection proposal. Text-only reasoning can compare structured records when image evidence adds no required information.

| Evidence group | Fields retained for interpretation and comparison |
| --- | --- |
| Job and purpose | Brief revision, intended use, required components/features, requested output, criteria and their sources |
| Component definition | Stable ID/readable name, manufacturer or library identity, part/configuration number, source revision, asset hash, source URL/path, rights record |
| Assembly occurrence | Occurrence ID/readable name, parent path, component revision/hash, occurrence transform, mating/interface relation |
| Geometry | Native representation, imported representation, body/shell/mesh identity, analytic/faceted surface types, importer settings/version, source-to-import mapping |
| Units and frames | Source unit, target unit, numerical conversion factor, source/component/assembly frame IDs, origins, axis directions, handedness, transform direction |
| Required feature | Feature ID/readable name, supporting source claim or measurement, source coordinates, queried geometric entity, value/unit, uncertainty or tolerance meaning |
| Inspection views | Artifact/document ID and revision, source hash, occurrence visibility set, view direction/projection, camera and clipping state, image size, labels and crop-to-full-view mapping |
| Check result | Named quantity/relation, reference value, criterion/source, observed value, method/tool/version, pass/fail/error and checked revision |
| Candidate and merge | Branch ID, candidate revision, selected features or occurrences, evidence links, selection reason, alternative retained, dependent results requiring a new check |

Proposed view procedure:

1. Capture a labelled assembly view for component identity, then corresponding orthographic views of that same revision for orientation and interface inspection. Record which occurrences are hidden, isolated, sectioned or clipped.
2. Use local component views for mounting faces and assembly views for placement. Keep both frame names in every comparison. A camera rotation changes the view record; an occurrence transform changes the assembly record.
3. Link a rendered feature to its component and occurrence IDs and the queried geometric entity. A source thumbnail can illustrate a library record; the actual source asset supplies the imported geometry identity.
4. Show a source/derived overlay only after recording the transform and unit conversion. Keep the numeric transform with the overlay. Compare critical measurements in the application or geometry backend.
5. Convert a visual concern into a bounded query: for example, query the axis direction of the named bore and its offset from the named mounting plane. Retain the concern when the current adapter supports only the view inspection.

The OCS contract requires measurements and corresponding views from the same model revision. Its supplied-number checker accepts point, axis and plane observations with caller-supplied provenance. The proposed inspection package therefore identifies the owning application query separately from a checker that consumes those values.

## 3. Operation-specific procedures and execution options

### 3.1 DOM-06 — Library asset intake and rights record

**Purpose and handoff:** create a component record whose source, identity, geometry role and item terms can be reused by DOM-38, DOM-07 and DOM-26. The original component remains an immutable source artifact.

1. Identify the actual item: record the supplied URL, source-library entry, title, part/configuration number and revision where the source provides them. Preserve the supplied URL alongside the item's canonical URL already held in the source record.
2. Retain the original file and associated terms with their paths, hashes, retrieval/registration dates and evidence states. A local record created from an existing report retains that evidence state. A future retrieval creates its own receipt.
3. Inspect the item's thumbnail, supplied drawing or model preview against its name and configuration. A VLM can propose identity conflicts, such as a preview showing another connector or mounting pattern. Compare the claim against the exact item's source record and asset.
4. Record geometry roles independently: native source, exact/faceted CAD, visual mesh, collision mesh, domain description or procedural generator. Tag source dimensions as manufacturer claims, drawing annotations, measurements or inferred values at the feature level.
5. Preserve item-level terms and dependencies. FreeCAD, KiCad, Menagerie, Poly Haven and the CONTEC example have their own terms in the [round-two domain source register](../../sources/round-02/domain-sources.json). A model can therefore remain a linked source record or enter a permitted local-asset path according to the recorded terms.

| Execution option | Concrete proposed behavior | Required result |
| --- | --- | --- |
| Agent directs work | Read item evidence, identify the intended configuration, inspect supplied views and prepare the component record | Source-linked identity, rights and feature-role interpretation |
| Software and agent work together | Software extracts file metadata and hashes; agent associates item/model identity and records terms | Machine receipt plus reviewed semantic association |
| Software handles ordinary cases | Import a supported, structured catalogue record with known fields; send differing identities, terms or schemas to an agent | Checked record or a named exception with retained original fields |
| Software handles complete action | Validate a supplied manifest against immutable, already reviewed source and rights records | Deterministic identity/hash/dependency result for the supported manifest class |

**Failure/resumption:** preserve the original record and any successfully read metadata when the preview, asset identity or item terms conflict. Resume the affected field from the recorded source revision. Preserve earlier rights and identity records when a new source revision is registered through DOM-26.

### 3.2 DOM-38 — Import STEP solid into CAD representation

**Purpose and handoff:** inspect the supplied STEP file through the selected importer, preserving the source and producing a revision-bound CAD representation for CAD-12 or DOM-07.

1. Read the original source identity and STEP schema, declared units, product structure and external-reference dependencies through the supported parser/importer. Record importer, kernel and settings. A dependency resolved from a separate file retains its identity and terms.
2. Import into a separate derived artifact. Map product definitions and occurrence paths to imported objects. Record names, placements, body/solid/shell counts and geometry types, including faceted faces.
3. Query bounds and valid volume where the imported representation supports them. Query known controlling interfaces from the brief: for example, a bore diameter, mounting-plane separation or door opening. Record source-to-import transforms and measurement entity IDs.
4. Capture corresponding views of the imported revision. A VLM examines component/configuration identity, orientation, missing visible pieces, duplicated occurrences and feature correspondence against supplied source views.
5. Compare the importer result against the source measurements and required representation. Use an independent supported consumer where the agreed check requires it. Record exact comparisons and their reference source.

| Execution option | Concrete proposed behavior | Selection condition |
| --- | --- | --- |
| Agent directs work | Inspect source structure, choose the scoped import settings and examine the report/views | Source conventions or visible feature associations need interpretation |
| Software and agent work together | Importer returns product/geometry measurements; agent associates interfaces and diagnoses differences | Supported import exists; item identity or expected feature mapping varies |
| Software handles ordinary cases | Run a pinned importer on the demonstrated STEP input class and compare declared controls | A fixture-supported schema, representation and unit/frame convention apply |
| Software handles complete action | Import and validate a pinned, supported asset revision against an explicit manifest | All required mappings and criteria are machine-readable for that exact class |

**Failure/resumption:** retain the source, importer log, partial artifact and object mapping under the failed run. Mark the partial artifact with its execution state. Resume from the last valid stage after source hashes and tool versions are checked. A different importer or setting creates a new derivative branch for comparison.

### 3.3 CAD-12 — Assemble existing CAD or source-library components

**Purpose and handoff:** construct an identified assembly from a named base and additional component occurrences, using declared local and assembly frames. Its consumers include DOM-39 and later domain operations.

1. Record the base component and every added component separately, with source revision/hash, representation and local interface frame. Preserve placeholders or simplified envelopes as their declared representation and evidence class.
2. Produce candidate arrangements when several supported source components or mating interpretations fit the requested sketch or interface goal. Each candidate retains its own item identities and required-feature checks.
3. Apply explicit occurrence transforms or supported assembly constraints. Preserve component geometry and source transforms. Record inferred connection geometry as a proposal with its own identity.
4. Query interface agreement and supported interference/clearance checks. Capture views showing the named component boundaries, mounting relationships and orientation. Record bounding-box overlap as a candidate pair for a further geometry check.
5. Compare candidate arrangements against the intended use, source evidence and critical features. Merge compatible occurrences or choose a whole candidate with a recorded reasoning result. Revalidate the resulting assembly revision.

| Execution option | Concrete proposed behavior | Selection condition |
| --- | --- | --- |
| Agent directs work | Interpret source views and interfaces; direct placements and named geometry queries | Arrangement meaning or component correspondence needs reasoning |
| Software and agent work together | Software constructs transforms/constraints and measures interfaces; agent selects correspondence and diagnoses failures | Mating rules exist and source identities vary |
| Software handles ordinary cases | Instantiate checked component families through named interface frames | Pinned component class and demonstrated mating-frame rules apply |
| Software handles complete action | Build an explicitly listed assembly graph with fixed component revisions and transforms | Graph, representations, placement rules and required checks are complete explicit inputs |

**Failure/resumption:** retain each candidate and failed constraint/query result. Inspect the current assembly revision before retrying a mutation. Resume with the component occurrence and constraint IDs that actually exist. A source geometry or frame change invalidates affected placement, clearance and export results through the dependency graph.

### 3.4 DOM-07 — Place reusable component in assembly

**Purpose and handoff:** place a reusable component using named interface frames or measured mounting datums, creating a CAD occurrence and its assembly-graph relation. The original record identifies the source component and measurement set, with an assembly-graph alternative.

1. Resolve the exact component revision, source frame, target assembly frame and placement evidence. Identify the target occurrence or connection rather than relying on a current GUI selection.
2. Associate the source mating feature with its target. A VLM can propose that two named mounting faces correspond by comparing labelled views and source descriptions. The selected correspondence becomes an explicit relation with evidence.
3. Compute or solve the occurrence transform in declared units and frame direction. Record any remaining degrees of freedom where motion or a placement family belongs to the requested output.
4. Read back the resulting transform and required interface measurements. Review the same occurrence in assembly and local interface views. Record connection meaning and geometric check results separately.
5. Update the assembly graph with the occurrence, parent, component revision and connection relation. Preserve the existing graph when registering a failed placement candidate.

| Execution option | Concrete proposed behavior | Required control |
| --- | --- | --- |
| Agent directs work | Choose source/target datums from evidence and direct placement/checks | Reviewed datum correspondence and bounded placement request |
| Software and agent work together | Software computes frame composition or assembly constraints; agent resolves correspondence | Explicit numerical frames plus reviewed feature identity |
| Software handles ordinary cases | Apply a demonstrated mating rule to supported named interfaces | Interface schema, handedness and placement convention match the supported class |
| Software handles complete action | Insert a pinned component at a supplied checked transform and validate readback | Complete occurrence identity, transform and check contract |

**Failure/resumption:** retain unresolved candidate correspondences and identify the exact component/feature conflict. For an interrupted placement request, use the same operation identity to query its state before another mutation, following the OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`). Re-read the document revision and actual occurrences before resuming a partially completed sequence.

### 3.5 DOM-26 — Version and reuse component revision

**Purpose and handoff:** make component reuse reproducible by pinning source assets, derived geometry and relevant metadata to explicit revisions.

1. Compare original bytes, source identity, item terms, geometry derivatives, interface frames and domain metadata separately. A geometry hash is one part of component identity; its frame or applicable terms can change while those bytes remain equal.
2. Create a new revision record for changed source content, terms or derived processing, with its predecessor and changed fields. Preserve earlier component records and assemblies pinned to them.
3. Generate a comparison package for the named changed features. Software reports changed IDs, hashes, measurements and transforms. A VLM can compare source/new views and identify visible correspondence or semantic changes.
4. Classify the effect on dependent occurrences and checks. A changed mounting datum requires placement reassessment; a changed import setting requires geometry/readback comparison; a changed item record receives its own rights review outcome.
5. Resolve a proposed project update by exact revision. Retain the prior assembly candidate and its checks, then create new checks for the updated assembly and its derivatives.

| Execution option | Concrete proposed behavior | Selection condition |
| --- | --- | --- |
| Agent directs work | Interpret a source/update change and its semantic consequences | Revision meaning or identity changes require review |
| Software and agent work together | Software computes field/hash/feature differences; agent chooses the bounded update proposal | Provenance is structured and consequences need interpretation |
| Software handles ordinary cases | Register a content-addressed revision and invalidate explicit dependency edges | Supported schema and dependency rules cover the changed fields |
| Software handles complete action | Resolve an exact pinned manifest and verify all hashes/references | Reuse is a deterministic lookup of immutable reviewed records |

**Failure/resumption:** retain incomplete revision creation as a draft record with its operation state. Resume resolution by the intended component ID and digest. Publish a revision only after its required files and dependency references are present; assemblies keep their existing pins during the draft.

### 3.6 DOM-39 — Export STEP assembly

**Purpose and handoff:** create a STEP exchange artifact from a native assembly revision, preserving the product/occurrence information supported by the actual exporter and consumer.

1. Snapshot the native assembly manifest: component revisions/hashes, product definitions, occurrence paths, parent relationships, transforms, units and required interface features. Record the actual exporter and settings.
2. Export to a new derivative path and retain the output hash, log and completed execution state. Keep the native model/generator as the editable source identified in the [implementation plan](../../implementation-plan.md).
3. Reopen in an independent supported consumer. Compare product-definition/occurrence mappings, units, transformed bounds, valid volumes and the required interface measurements. Two importer routes using the same kernel can still reveal application mapping differences; record their actual shared dependencies.
4. Capture the reopened assembly's labelled views and compare corresponding occurrences with the native snapshot. A VLM examines orientation, omitted/repeated components and tree-to-view correspondence. Software compares the identities, transforms and measured features.
5. Record fields preserved, transformed, approximated or dropped. If individual-solid export is the chosen alternative, retain an explicit external assembly manifest mapping each file to its component occurrence and transform. Produce a new receipt for that route.

| Execution option | Concrete proposed behavior | Selection condition |
| --- | --- | --- |
| Agent directs work | Select a supported export route/settings and inspect tree, views and reports | Receiving-consumer requirements or observed losses need interpretation |
| Software and agent work together | Exporter/consumer compare mapped data; agent reviews correspondence and exceptions | Geometry exchange works and assembly semantics vary |
| Software handles ordinary cases | Export and reopen demonstrated assembly classes with explicit loss/check rules | Input class and exporter/consumer versions match exercised cases |
| Software handles complete action | Export a pinned supported manifest and compare every required mapped field | The input class, field mapping, criteria and output consumer are explicit |

**Failure/resumption:** preserve a failed or partial output with its log and state. Query an interrupted export's state before repeating it. Resume from the frozen native revision or create a new run if source revisions or settings change. Associate a successful reopen receipt only with the output hash it actually inspected.

## 4. Candidate sources and goal-specific alternatives

These are source-backed route proposals from the existing component assessment. Each job selects the particular item and its required features from the brief.

| Intended use | Component/input alternative | Concrete evidence and retained purpose | Selection/handoff check |
| --- | --- | --- | --- |
| Sketch or layout | Labelled primitive envelope or simplified derivative of an identified part | Arrangement, named component boundaries and approximate visual detail; retain source-linked simplification recipe | Overall arrangement dimensions and occurrence orientation required by the sketch brief |
| Mechanical component reuse | Existing native CAD, a manufacturer STEP item, or a FreeCAD Parts Library item | Item identity, configuration, geometry representation and relevant source dimensions | Required mounting features, source/target frames and item-level terms |
| Repeated parametric hardware | Existing procedural source such as BOSL2 or NopSCADlib; a scoped CadQuery/build123d family | Source code revision, input parameters and generated geometry lineage | Generated required-feature measurements and permitted source/derivative reuse |
| Working robot interface geometry | Identified CAD component plus supplied drawing or measured interface evidence | Link/component identity, mounting dimensions, shaft/bore and axis geometry needed by the robot brief | Each critical interface criterion and the measured placement relation |
| Robot simulation-description reference | Exact Menagerie model directory and revision | Named MJCF bodies/joints, visual/collision assets, generation notes and per-model terms | Component-to-body correspondence retained for the later robot-domain operation |
| Building component geometry | Identified vendor/library CAD item or FreeCAD BIM/Parts Library item | Door/window/MEP/component geometry and occurrence placement | Required dimensions, opening/host correspondence and storey/local frame |
| Semantic building reuse | Retained native IFC source alongside its geometric derivatives | Stable element identity, class, spatial relationships, placements and source properties | Map geometric occurrences to the retained semantic elements; consume through the later IFC operation |
| Appearance context | Poly Haven model/material/HDRI or another permitted visual asset | Scene object identity, appearance, lighting and display geometry | View/layout criteria required by the appearance brief; retain the asset's display role |

The [component assessment](../../domains-and-components.md) records the FreeCAD, KiCad, BOSL2, NopSCADlib, Menagerie, Poly Haven and manufacturer-source capabilities. The [implementation plan](../../implementation-plan.md) retains the later robotics and IFC stages. Point 02 records the source and handoff fields consumed by those stages.

## 5. VLM comparison, selection and evidence merge

1. **Freeze comparison inputs.** Give each branch the same brief/source revision and required-feature list. Branches may target a sketch, an interface model or a domain source when the declared goal permits those alternatives. Record the target and its checks beside every candidate.
2. **Prepare common frames.** Map each source/component/occurrence frame to the comparison frame with an explicit unit factor, transform direction, origin and axis convention. Preserve the native source convention. Identify reflections separately from rotation; record whether the item itself is handed.
3. **Establish identity before shape comparison.** Match manufacturer/library item, configuration, revision, product definition, occurrence and feature. A visually similar component becomes a candidate correspondence requiring evidence. Equal hashes can identify reused bytes while occurrence paths remain distinct.
4. **Calculate candidate differences.** Software reports the required dimensions, placements, axis/plane relationships and geometry representation. Associate every difference with a feature/entity ID and criterion. Aggregate bounds/volume remain separate comparison rows.
5. **Give the VLM the evidence.** Provide labelled corresponding views, original source regions, item metadata, measurement receipts, differing field rows and intended use. Include the full-view context for each crop and the artifact revision for each render.
6. **Request an explicit selection record.** For each required feature or occurrence, the VLM proposes retain candidate A, retain candidate B, retain alternatives, combine compatible evidence, or request the exact missing interpretation. Record the supporting source and reason. Model agreement is a review result associated with those inputs.
7. **Preserve conflicting evidence.** Keep conflicting source dimensions or item associations in separate rows and identify the dependent action. Majority agreement between readings and averaging between incompatible item dimensions supply additional interpretations requiring their own evidence.
8. **Choose the correct merge operation.** Compatible observations about the same identified feature can enrich one evidence record. Compatible component occurrences can form an assembly. Substitution replaces a component occurrence's source revision and reassesses its relations. Feature construction across different parts or revisions produces an authored candidate through a separately scoped geometry action.
9. **Record lineage.** The selected/merged output has its own revision, input branch revisions, source-to-feature map, retained alternatives, selection reasons and dependency changes. Keep required-feature criteria attached to their features through simplification or substitution.
10. **Validate the merged revision independently.** Query its required geometry, identities and transforms. Have a separate semantic review compare its source-to-feature associations, component configuration, parent/occurrence mapping and intended use. Capture views from that exact checked revision. Run the agreed exchange/reopen checks on its actual derivative hash.

Proposed feature comparison rows:

| Feature or relationship | Source/reference | Geometry check | Interpretation review |
| --- | --- | --- | --- |
| Robot mounting pattern | Identified part drawing or measured interface record | Named hole diameters, pitch and mounting-plane offsets in declared units | Match the correct part revision, hole set and mating face |
| Robot joint axis | Named interface/joint evidence and required frame | Axis location/direction and any finite-span endpoint checks required by the brief | Match the intended rotating part, parent/child meaning and direction convention |
| Robot contact/clearance feature | Scoped geometry and required contact/clearance criterion | Supported exact distance or interference query at the named pose | Inspect the intended contact pair and retained component boundaries |
| Building opening | Source building record/drawing and required feature criterion | Opening width, height, position and host-local transform | Match the opening, its host wall and the relevant level |
| Building component placement | Source site/storey/component frames | Local and assembly transforms, elevation and required dimensions | Match the intended element/occurrence and its semantic source |
| STEP occurrence preservation | Frozen source assembly manifest | Product/occurrence mapping and transforms, plus controlling interfaces | Confirm tree entries refer to the expected visible components |

A tolerance record names its quantity, units, source, intended use and meaning. Source dimensional tolerance, measurement uncertainty, CAD query precision, solver criterion, tessellation deviation and exchange comparison criterion retain separate fields. The audit's robot-joint and building examples guide the selection of relevant criteria from actual jobs.

## 6. Proposed reusable components and migration from agent work

The retained implementation plan already proposes `component-library`, `model-verification` and geometry adapters. The following components refine those proposals for point 02.

| Proposed component | Inputs → outputs | Existing basis | Demonstration needed before software-led use |
| --- | --- | --- | --- |
| Component intake procedure within `component-library` | Item source/terms + original files → immutable asset record and interpreted component identity | DOM-06; existing component schema and source register | Item-level identity/terms cases, duplicate bytes, differing revisions and linked-only records |
| Asset/revision manifest checker | Structured identity, hashes, dependencies and pins → field/check receipt | DOM-26; existing registry/Git proposal | Repeated occurrences, same bytes with changed metadata, missing dependencies and interrupted revision creation |
| STEP inspection adapter | STEP + importer/settings + required controls → product/occurrence map, representation and measurements | DOM-38; FreeCAD/OCCT candidate; existing CAD import/export records | Analytic/faceted source, mixed units, named instances, transformed repeated components and invalid/partial imports |
| Revision-bound view package | Frozen native/imported revision + labelled occurrence/feature set → corresponding images and view manifest | Existing OCS readback/orthographic-view contract; Blender scene alternative in the CAD record | Same-revision views, hidden/clipped occurrences, mirrored arrangements and visible feature-to-query mapping |
| Candidate comparison and merge record | Branch revisions, frames, sources and measured features → differences, reasoning selection and lineage | Composition rules; existing feature evidence procedure | Conflicting dimensions, different part revisions, whole-candidate substitution and compatible occurrence assembly |
| Placement/dependency adapter | Pinned component + named interfaces/explicit transform → occurrence and graph update | CAD-12, DOM-07; OCS groups/blocks and FreeCAD assembly source candidates | Correct/incorrect datums, repeated occurrences, source-frame change and partial-operation recovery |
| Exchange validation receipt | Native assembly manifest + STEP output + consumer report → mapping/loss/check result | DOM-39; source/consumer verification in implementation plan | Flattened/fused output, wrong units, omitted instance, local bore change and exact output-hash association |

Proposed migration sequence for each component:

1. Record the agent's evidence and ordered actions on an authorized representative case.
2. Identify repeatable parsing, hash, transform, geometry-query and comparison rules. Keep source identity and correspondence judgments explicit.
3. Define the supported input class and expected successful, ambiguous, invalid and interrupted outputs.
4. Implement only within a later authorized batch; compare observed outputs against the retained expected cases.
5. Assign demonstrated ordinary cases to software and send named exceptions with retained artifacts to the agent path. Record the selection rule and actual version supporting that class.

## 7. Failure, retained evidence and bounded resumption

| Failure or conflict | Detection and retained evidence | Next bounded action and invalidation |
| --- | --- | --- |
| Item preview and asset identify different configurations | Item/asset identity rows, original view and distinct hashes | Re-read the exact item's local record; retain candidates and suspend the affected identity-dependent placement |
| Unit/frame interpretation conflicts | Declared source metadata, expected control measurement, transform and observed value | Resolve the named unit/frame input; regenerate affected transforms, measurements and exports |
| Analytic/faceted representation differs between paths | Surface-type/topology report, source/importer/settings | Compare the candidate derivative against the goal's required features; preserve both derivative branches |
| Product structure flattens or occurrence mapping changes | Source and imported trees, definition/occurrence IDs, transforms | Try the explicitly proposed supported route or individual-solid/manifest alternative; recheck downstream tree/placement results |
| Symmetry permits several placements | Candidate frame correspondences, orientation views, query rows | Retain each candidate and identify the source feature or decision that distinguishes them |
| Required interface differs despite aggregate agreement | Required-feature measurement and its reference/criterion, bounds/volume rows | Diagnose that named interface; reassess dependent mating/clearance and any exported result |
| Render and measurements belong to different revisions | Document/revision/hash mismatch in the view/check manifests | Capture/read the named revision again; discard the mismatched association from the comparison result |
| Interrupted mutation or export returns an uncertain state | Stable request/operation ID, target revision, operation log and partial artifact | Query the same operation state, inspect the actual document/output and resume the uncompleted bounded stage |
| Component revision changes after a passed check | Pin/hash comparison and changed feature/frame/terms rows | Preserve the passed historical check; mark affected new-revision placement/geometry/export checks for execution |
| VLM call fails or returns incomplete selection rows | Call identity, input package hash, partial response and completed row IDs | Resume the remaining interpretation rows from frozen evidence; keep earlier completed review results tied to that revision |

## 8. Validation cases for a later authorized run

Each case retains input files, source records, expected mappings/measurements and criteria before execution.

1. **One definition, repeated occurrences:** two occurrences share component bytes and have different transforms. Expected result: one source definition, separate occurrence identities and correct parent paths/placements after import and export.
2. **Mixed units:** the source declares a different length unit from the target. Expected result: preserved source unit, explicit conversion factor, correct control measurement and corresponding frame translations.
3. **Handed component:** two visually similar left/right items share an envelope. Expected result: retained item identity, handedness and mounting-feature differences; separate candidate records.
4. **Analytic and faceted STEP:** both show a curved feature. Expected result: recorded actual face types and per-feature measured comparisons for each import path.
5. **Matching bounds and volume, changed interface:** a bore or mounting pattern differs while aggregate checks pass. Expected result: required-feature comparison detects the changed interface.
6. **Source/preview mismatch:** the preview and supplied asset represent different configurations. Expected result: identity conflict linked to the precise evidence and its dependent placement.
7. **Sketch derivative and interface model:** both derive from the same identified source for different declared purposes. Expected result: retained simplification lineage, separate criteria and source role for each.
8. **Whole-component substitution:** a proposed source revision has changed mating geometry. Expected result: retained previous candidate, changed-feature receipt and new placement/clearance checks for the substituted candidate.
9. **Compatible evidence and incompatible parts:** one branch adds evidence about the same source feature; another copies a feature from a different part. Expected result: evidence enrichment for the first case and a separately identified authored-candidate proposal for the second.
10. **Merged assembly regression:** two branches pass their own checks, then are combined. Expected result: the merged assembly receives new identity, transform, critical-interface and semantic checks.
11. **Flattened exchange:** the receiving importer returns solids while the native source has repeated named instances. Expected result: product/occurrence mapping/loss report and a consumer-specific result for the exact output hash.
12. **Interrupted operation:** a request completes after its response is lost. Expected result: state query by the same operation identity, readback of actual output, and one occurrence/export outcome in the receipt.
13. **Revision-only metadata change:** geometry bytes stay equal while the source frame or item terms change. Expected result: a new metadata revision with targeted dependency effects and preserved earlier pins.
14. **Robot/building source semantics:** CAD geometry is linked to a robot-model body or IFC element. Expected result: retained source identity and frame mapping for later domain processing, with point-02 geometric checks tied to the inspected source.

## 9. Resource comparison axes

These are proposed recording requirements and qualitative dependencies. A run supplies measurements for its actual file, assembly, hardware, tool and model.

| Operation or option | Local CPU, memory and graphics work | Remote model work and manual work | Outcome/refinement evidence |
| --- | --- | --- | --- |
| DOM-06 intake | File read/hash, metadata parsing and preview generation; record file bytes, dependency count and peak RAM | Text or image review of item identity and terms; record input size, calls, latency and interventions | Correct item/source association, complete provenance fields and explicit field exceptions |
| DOM-38 import | Geometry parsing, topology construction, tessellation and queries; record products, occurrences, faces/triangles, peak RAM and elapsed time | Review only the required source/imported views and conflicting features | Representation fidelity, required-feature differences and importer-specific corrections |
| CAD-12/DOM-07 assembly | Frame calculations, constraint solving, geometry queries and rendered views; record unique definitions and occurrences separately | Correspondence/arrangement review, candidate selection and exact decision questions | Placement accuracy, interface checks, branch count and recomputation needed |
| DOM-26 versioning | Hash/field/dependency comparison; record unique asset bytes and reused occurrences | Interpret semantic revision effects when the changed fields require it | Reproducible pins, affected dependencies and review effort per changed field |
| DOM-39 exchange | Export plus independent reopen/query; record file size, product tree, geometry counts, peak RAM and elapsed time | Compare tree/view correspondence and diagnose mapped-field exceptions | Preserved fields, geometry differences, consumer outcome and route changes |
| Agent directs work | Tools perform each explicit operation/query; store their individual resource records | Record reasoning setting, model input/response sizes, calls and review time for each bounded action | Evidence-linked decisions and required checks per action |
| Software and agent work together | Batch the supported parsing/query/construction stages | Review named associations, parameters and exceptions | Software check results plus semantic-review findings |
| Software handles ordinary cases | Run supported input classes and retain exception artifacts | Model/manual work is attached to the actual exception | Ordinary-case result, exception class and next supported path |
| Software handles complete action | Run explicit supported rules and output checks for the defined class | Optional review is separately recorded | Deterministic checked artifact/receipt and actual failure behavior |

Across all options record hardware/runtime, CPU time, wall time, peak RAM, GPU/VRAM where used, input/output bytes, preview/image count and resolution, tool/kernel versions, concurrency and cache reuse. Record local versus remote model location, requested and actual exposed model/effort, transmitted evidence size, latency, returned usage and charged cost with price source/date when available. Separate source reading, geometry computation, render generation, reasoning review and manual decision time. Compare output purpose, required-feature accuracy, semantic correspondence and subsequent refinement work for the same case.

## 10. Local evidence and original URLs reused

All local evidence below was read on 2026-11-12. The evidence states in the external-source rows are those already held in the cited registers; this task reuses their summaries.

| Local record or original link | Concrete summary and use here | Evidence status used |
| --- | --- | --- |
| [Original CAD operations](../../workflows/cad-paths.json) | CAD-12 defines the named base/additional-component requirement, retained identities and transforms, and interface/source checks | Local operation proposal inspected |
| [Original domain operations](../../workflows/domain-paths.json) | DOM-06, DOM-07, DOM-26, DOM-38 and DOM-39 supply the original intake, placement, version and STEP contracts | Local records inspected; DOM-07 is labelled `documented_capability`; the other reviewed records are labelled `proposed_composition` |
| [Existing visual review](visual-review.md) and [audit plan](../plan.md) | Establish feature/source association, VLM evidence review, common frames, per-feature criteria, independent merged checks and resource axes | Existing documentary review and procedure proposals inspected |
| [Composition rules](../../workflows/composition-rules.md) | Defines evidence merge, geometry assembly, component substitution, representation forks, units/frames, identity and revision checks | Local proposal inspected |
| [Component assessment](../../domains-and-components.md) | Describes component definition versus occurrence, source/derived roles, candidate libraries, per-asset terms and adapter validation | Existing report inspected |
| [Implementation plan](../../implementation-plan.md) | Proposes component-library and verification skills, geometry adapters and later robot/IFC consumers; records immutable pins and actual saved-artifact verification | Local proposal inspected and retained |
| [Local baseline](../../local-baseline.md) and [CAD assessment](../../cad-and-skills.md) | Record the inspected OCS triangle-driven STEP writer and candidate FreeCAD/CadQuery/build123d assembly/interchange routes | Existing local assessments inspected |
| OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) | Require explicit parts/frames, revision-bound readback and same-model views; describe supplied-number checker scope and interrupted-operation recovery | Local skill/reference inspected |
| [FreeCAD Assembly Workbench](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md) | Registered summary describes assembly insertion, constraints/joints and assembly structure; supports placement and export-route investigation | `web_inspected`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [CadQuery documentation](https://cadquery.readthedocs.io/en/stable/) | Registered summary describes Python parametric CAD and imports/exports; source code carries parametric construction history | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [CadQuery API reference](https://cadquery.readthedocs.io/en/stable/classreference.html) and [import/export documentation](https://cadquery.readthedocs.io/en/stable/importexport.html) | Registered summaries cover shape validity, bounds, volume, transforms, STEP import/export and units | `web_inspected`, reused from [round-three CAD detail records](../../sources/round-03/cad-detail-sources.json) |
| [build123d stable documentation](https://build123d.readthedocs.io/en/stable/) | Registered summary describes the Python parametric B-rep framework over Open CASCADE; CAD assessment records joints/assembly and exchange capabilities | `web_inspected`, reused from [round-two CAD records](../../sources/round-02/cad-sources.json) |
| [BOSL2 repository](https://github.com/BelfrySCAD/BOSL2), [OpenSCAD library catalogue](https://openscad.org/libraries.html), [NopSCADlib repository](https://github.com/nophead/NopSCADlib) and [usage documentation](https://github.com/nophead/NopSCADlib/blob/master/docs/usage.md) | The component assessment describes BOSL2 parametric shapes and NopSCADlib modeled hardware/procedural source, with their recorded terms; supports the procedural-hardware alternative | Existing [component assessment](../../domains-and-components.md) inspected; its linked original-source findings are reused |
| [FreeCAD Addons](https://www.freecad.org/addons.php?lang=eng_EN) and [Parts Library repository](https://github.com/FreeCAD/FreeCAD-library) | Registered summaries describe Parts Library categories, FCStd/STEP/STL/BREP files and collection metadata; component assessment records item attribution review | `existing_report_registered`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [KiCad library terms](https://www.kicad.org/libraries/license/) | Registered summary records CC-BY-SA 4.0 library terms and the design-use exception | `existing_report_registered`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie) and [model catalogue](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md) | Registered summaries identify model directories, robot identities, MJCF/assets, generation information and per-model licences | Round-two records use `existing_report_registered`; [round-three domain detail records](../../sources/round-03/domain-detail-sources.json) use `web_inspected`; this review reuses those separate records |
| [Poly Haven licence](https://polyhaven.com/license) | Registered summary records CC0 terms for site models, materials and HDRIs; the assessment assigns appearance/context roles | `existing_report_registered`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [CONTEC STEP download terms](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280) | Registered summary records item-download use, adaptation/redistribution restrictions and warranty conditions; illustrates preserving the exact item's terms | `existing_report_registered`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [FreeCAD BIM Library documentation](https://reqrefusion.github.io/FreeCAD-Documentation-html/wiki/BIM_Library.html) | Registered summary describes library insertion from FCStd/STEP/BREP and online/offline library workflow | `existing_report_registered`, reused from [round-two domain records](../../sources/round-02/domain-sources.json) |
| [IfcOpenShell geometry creation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html) and [placement API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html) | Registered summaries describe IFC geometry/placement and the 4×4 local placement API with declared SI translation interpretation; support the retained building-source handoff | `web_inspected`, reused from [round-three domain detail records](../../sources/round-03/domain-detail-sources.json) |
| [MuJoCo modeling guide](https://github.com/google-deepmind/mujoco/blob/main/doc/modeling.rst) | Registered summary describes body/joint/frame and asset semantics; supports retaining the robot-source identity/frame handoff | `web_inspected`, reused from [round-three domain detail records](../../sources/round-03/domain-detail-sources.json) |

## 11. Integration handoff

1. Add the operation-specific options, component-definition/occurrence separation, source-linked candidate selection and new-revision checks to the point-02 procedure as proposals.
2. Register this review in the coordinating audit/source batch with the six readable operation names and referring point document.
3. Preserve the original operation records and implementation plan. The coordinator owns the source/graph consistency checks and the batch checkpoint/result commits.
