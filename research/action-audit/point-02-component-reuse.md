# Point 02 — Existing components and CAD files to inspected reusable inputs

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 12 November 2026. Status: proposed procedures and development specifications. The executed work is documentation and source inspection. Requested designer dispatch: `gpt-6-astra`, `xhigh`; actual runtime model identity: unavailable.

## 1. Scope and source basis

1. **CAD-12 — Assemble existing CAD or source-library components:** combine named component definitions and explicit occurrences into the requested native assembly representation.
2. **DOM-06 — Library asset intake and rights record:** record exact item/file identity, terms, representation and feature evidence.
3. **DOM-07 — Place reusable component in assembly:** apply a sourced interface transform to one occurrence in an identified target assembly.
4. **DOM-26 — Version and reuse component revision:** retain immutable originals, metadata/rights revisions, dependencies and consumer pins.
5. **DOM-38 — Import STEP solid into CAD representation:** inspect and import a supplied STEP file with actual unit, shape and product-structure checks.
6. **DOM-39 — Export STEP assembly:** derive a new STEP artifact from a frozen native assembly and check it in the receiving consumer.

The [structured action specification](point-02-operations.json) contains all fifteen required fields for each of the 24 actions: purpose, intended use, inputs, outputs, accuracy, evidence, software, agent, user decisions, dependencies, proposed development, procedure, validation, failure/resume and resources. The numbered actions below expose the concrete sequence, outputs and checks. Original records remain in [CAD operations](../workflows/cad-paths.json) and [domain operations](../workflows/domain-paths.json); the [implementation plan](../implementation-plan.md) retains its existing content.

The [component assessment](../domains-and-components.md), [composition rules](../workflows/composition-rules.md), OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and OCS model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) supply identity, frame, source, representation and check requirements. [Software review](reviews/point-02-software.md), [visual review](reviews/point-02-visual.md) and [Luna source inspection](reviews/point-02-sources.md) supply the supporting interface and source findings.

## 2. Representation and execution conventions

1. **Component definition:** one identified source component and revision. **Occurrence:** one use of that definition at a particular parent path and placement. Repeated occurrences can share geometry bytes and retain separate identities.
2. **B-rep:** boundary representation, describing shape through surfaces, edges and vertices. **Analytic surface:** an explicitly represented plane, cylinder or similar mathematical surface. **Faceted geometry:** a surface represented by planar faces. Record actual shape and topology types after import/export.
3. **VLM:** vision-language model, reading source images and language together. A VLM may select a source-supported item, interface mapping or candidate within the existing task requirements. New geometry intent or an unresolved controlling-source conflict requires its exact user decision.
4. **Placement:** a map from component coordinates to assembly coordinates. Use named transform direction, source/target units, origin, axis directions and handedness. Apply explicit unit/convention conversion before rigid placement. For column vectors, the DOM-07 calculation is **T_A_C = T_A_I × T_I_J × inverse(T_C_J)**. A is assembly, C component, I target interface and J component interface; each operand has a source.
5. **Per-feature criteria:** record engineering allowance, source measurement uncertainty, solver stopping criterion and import/export comparison threshold separately, with units and sources. The supplied task determines the features, values and permitted differences.
6. **Independent validation:** numerical checks bind to actual artifact/document revision and source handles; a reviewer separate from the producing/merging interpretation checks item, feature, datum and occurrence meaning. Record actual model/software identities and shared-kernel/model dependencies.
7. **Source-preserving merge:** select whole component candidates, combine compatible metadata/evidence for the same identified feature, or assemble separate occurrences. Cross-part/revision feature copying creates a new authored hybrid with its own identity and scoped modeling action. Preserve conflicting dimensions as alternatives.
8. **Proposal and decision:** apply explicit supplied requirements and corrections within their scope. `MARK AS ACCEPTED` assigns acceptance to a proposal; it does not gate processing of an already supplied requirement.
9. **Residual:** the measured difference between a transformed or imported feature and its reference after alignment. **Topology:** how the shape's vertices, edges and faces connect. **Pinned revision:** an explicitly fixed component or artifact revision/hash used by a consumer.
10. **OCCT:** Open CASCADE Technology, the CAD geometry and exchange libraries referenced here. Its STEPCAFControl APIs transfer document structure and geometry; the actual adapter/version determines the exercised behavior.

A dependency-led execution begins with the DOM-06-A01/A02 identity/rights receipt. That partial receipt feeds DOM-38 directly when STEP inspection/import is required; DOM-38 returns checked representation evidence to DOM-06-A03/A04, which completes the component record for its named use. DOM-26 publishes/pins after those required references exist. CAD-12 then uses DOM-07 for individual placement, and DOM-39 performs the requested exchange. Partial intake retains its draft status and action-specific readiness. CAD-12 consumes each completed DOM-07 placement receipt once; new derivatives enter a new DOM-26 revision.

## 3. Source-supported tool choices

1. OCS API-SPEC (`${OCS_ROOT}/docs/automation/API-SPEC.md`) describes `block_define`, which moves source entities into a block definition and creates an Insert, and `group_create`, which groups existing handles. Use those operations for their stated drawing representations. The OCS control reference (`${CODEX_HOME}/skills/ocs-engineering/references/ocs-control.md`) establishes the state/revision/request protocol and records the limits of observed assembly and clearance support.
2. [FreeCAD Assembly documentation](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md) describes assemblies, source links and joints. [Import/export preferences](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md) describe STEP structure/instance-name settings, export units and AP203/AP214 choices. Luna inspected these pages in the archived FreeCAD documentation repository; actual installed support is a future run finding.
3. [OCCT STEPCAFControl_Reader](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___reader.html) documents assembly-shape, name/color and root transfer into a DECAF document. [STEPCAFControl_Writer](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___writer.html) documents document/label/root-assembly transfer, names/colors and root-label length-unit or Cascade fallback. Luna's source inspection followed these original URLs to the OCCT 8.0.1 manual. The proposed adapter must establish its actual version and exercised preservation.
4. The inspected OCS STEP writer body (`${OCS_ROOT}/src/io/step.rs`) collects triangles across meshes and emits one shell, solid and representation with planar faces. It formats coordinates to six decimals, skips invalid triangle indices and emits an SI millimetre entity without attaching it to the geometric representation context. Its body and opening comments describe different organization. A future consumer fixture must establish units, topology and usable output. Assembly hierarchy and curved-surface preservation require the selected assembly-aware route and actual readback.
5. [KiCad library terms](https://www.kicad.org/libraries/license/) state the collection licence and design-use exception. [Menagerie](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md) directs users to each model directory's LICENSE for XML/assets. Attach actual item/model terms, attribution and revisions separately from application-software terms.

## 4. Resources and goal-specific detail

| Operation | Proposed local-work comparison and scaling basis | Remote inference and manual effort | Detail/accuracy choice |
| --- | --- | --- | --- |
| DOM-06 intake | Begin with file/terms reading and hashing; geometry inspection adds entity/triangle memory and query work | Item/configuration and terms interpretation; record calls, source subset, latency and active review time | Labelled appearance/layout asset or source-backed interface geometry |
| DOM-26 versioning | Hash and dependency checks depend on unique bytes and reference edges; existing geometry is reused | Semantic revision/terms impact and consumer selection | Independently version layout, precision and semantic derivatives |
| DOM-38 import | Header/structure inspection precedes geometry transfer/healing; face/product count drives CPU/RAM | Source-unit interpretation and actual representation review | Inspected faceted layout geometry or required source surfaces/interfaces |
| CAD-12 assembly | Definition/occurrence graph and matrix checks precede shape interference queries; record both counts | Mating/component interpretation and candidate comparison | Arrangement representation or measured constrained/interface assembly |
| DOM-07 placement | Bounded matrix work precedes native placement and feature measurement | Datum/mating interpretation, symmetry questions and failed-interface diagnosis | Layout anchors or sourced mating frames and critical dimensions |
| DOM-39 export | Frozen manifest precedes export and consumer reopen; faces/products/output bytes drive work | Export-field mapping, source-to-output correspondence and exception diagnosis | Faceted display exchange or required analytic/product structure with per-feature checks |

These are conditional work classifications, with no runtime measurements assigned. Each future action records input bytes, relevant definitions/occurrences/faces/triangles, CPU time, wall time, peak memory, graphics-device use when present, software/kernel versions and storage. Remote reasoning/VLM usage, latency, reported cost and manual interventions are independent records. Begin with metadata and required-feature queries; run broader geometry/consumer checks when the requested use requires them.

## 5. Operation procedures

### CAD-12 — Assemble existing CAD or source-library components

**CAD-12-A01 — Pin source definitions and assembly roles.** Identify the base and additional component definitions before creating occurrences.

Input: Base cad-solid; distinct additional cad-solid or source-library item; brief; original files, hashes, units and rights records.

1. Read base and additional source identities.
2. Map each required component to its exact source revision.
3. Record every proposed occurrence and its source definition.

Output: Component-definition manifest with base/additional roles, consumed by CAD-12-A02.

Validation: Recompute source hashes; check a distinct additional input exists; independent semantic review compares configuration/part identity to the brief.

Failure/resume: Retain every candidate on identity conflict; block dependent occurrences and resume after the precise part/configuration decision.

**CAD-12-A02 — Define interface frames and placement relations.** Translate the assembly brief into explicit component-to-assembly placement requirements.

Input: Pinned definitions; sourced component frames; target assembly frame; interface measurements; allowed placements and motion.

1. Name the assembly datum and each component's mating frame.
2. Separate source-unit conversion from rigid placement.
3. Build a rooted occurrence tree and record declared connection/constraint relations.

Output: Named interface correspondence and placement plan, consumed by CAD-12-A03 or DOM-07.

Validation: Check frame direction, units, right-handed rigid rotation after explicit convention mapping, and graph parent identities; reviewer rereads semantic correspondences.

Failure/resume: Preserve competing frame/constraint plans; a missing datum blocks only dependent transforms; restart from changed interface records.

**CAD-12-A03 — Create bounded native occurrences.** Instantiate the planned component occurrences while preserving source definitions.

Input: Checked placement plan; source definitions; chosen native representation; authorized document/revision and save scope.

1. Inspect current document and operation schemas.
2. Create occurrences in dependency order using named frames/constraints.
3. Read back each completed occurrence before creating dependants.

Output: Native occurrence tree with definition references and transforms, consumed by CAD-12-A04.

Validation: Verify source component hashes remain unchanged; read occurrence IDs/counts/transforms; inspect same-revision views and connection relations.

Failure/resume: On timeout reconcile request/operation identity; retain completed_steps and next_step; refresh after stale-state rejection and resume only the incomplete bounded action.

**CAD-12-A04 — Validate and preserve assembly structure.** Confirm the created assembly matches source identities, placements and required interfaces.

Input: Created assembly; placement plan; source definitions; per-feature criteria; supported geometry measurement API.

1. Measure named interfaces and inspect hierarchy.
2. Save the native derivative within scope and reopen it.
3. Recheck identities, placements and affected features on the reopened revision.

Output: Revision-bound assembly validation and native artifact, consumed by DOM-26/DOM-39 or a named downstream operation.

Validation: Numerical checks and independent semantic review both reference the saved revision; report actual solid/shell/mesh status and shared-kernel dependencies of the second reader.

Failure/resume: Preserve failed output and logs; return to the owning placement/definition action; invalidate only dependent transforms/exports.

**Execution options.**

1. **Agent-led:** High-reasoning agent interprets unfamiliar component/interface evidence and directs installed native tools; software records identity and geometry checks.
1. **Hybrid:** Software imports pinned definitions and solves explicit transforms; agent/VLM associates interfaces and chooses evidence-supported candidate arrangements.
1. **Software-first:** A checked component/frame family is assembled automatically; ambiguous identities, unsupported constraints or failed clearances enter agent review.
1. **Deterministic:** Replay an explicitly pinned occurrence tree and tested placement rules with the same source/configuration revisions; validate native save/reopen.

**Representation alternatives.**

1. OCS blocks/groups for a drawing arrangement with their supported entity semantics.
2. FreeCAD Assembly for documented joint/constraint authoring through an independently tested adapter.
3. CadQuery assembly source for explicit scripted instances where that artifact is requested.
4. Blender visual assembly when the task requests appearance/layout, with its own mesh/frame checks.
5. A sketch arrangement may use clearly identified envelopes/display representations with layout criteria; a precision assembly requires measured mating interfaces, actual shape representation and supported clearance queries.

**Parallel comparison and merge.** Pinned component candidates or placement interpretations may run separately with the same controlling brief; record each use/detail/accuracy target, source subset and resources. A VLM compares sourced interface views and numerical measurements; select supported part/placement interpretation within task constraints. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Combine whole definitions with occurrence transforms; keep placeholder and sourced geometry identities separate. Retain conflicting interfaces and required decisions. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Revalidate the merged occurrence tree, source hashes, transformed interfaces and supported clearance checks; independent semantic reviewer is separate from producing/merging interpretation.

**Migration to software.** Capture successful agent-selected interface mappings as checked cases; implement only stable definition/frame/constraint families; test mirrored frames, repeated instances, stale revisions and incompatible interfaces before moving that family to software-first.

**Future test cases.**

1. A base and two occurrences of one definition preserve one source identity and distinct occurrence IDs/transforms.
2. Mixed declared units normalize without changing source geometry; an ambiguous unit blocks its dependent placement.
3. A reflected frame and a mistaken axis association produce distinct numerical/semantic failures.
4. A failed sequential create resumes from recorded committed steps and preserves existing user work.
5. Native reopen retains occurrence count and interfaces; a visual overlap is checked using the supported geometry query.

**Sources:** [1](../workflows/cad-paths.json), [2](../domains-and-components.md), [3](../workflows/composition-rules.md), 4 (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), 5 (`${OCS_ROOT}/docs/automation/API-SPEC.md`), [6](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [7](https://cadquery.readthedocs.io/en/stable/importexport.html).

### DOM-06 — Library asset intake and rights record

**DOM-06-A01 — Identify the exact library item and retained files.** Bind a reusable component to an exact item/configuration and source revision.

Input: Supplied source-library item; exact URL/local original; configuration/part number; retrieved files and dates where already acquired.

1. Read the exact selected item page/local record.
2. List original files and their actual retention state.
3. Record hashes only for retained original bytes.

Output: Item/file inventory and source identity, consumed by DOM-06-A02.

Validation: Check every inventoried file against its recorded digest/type; semantic review checks part/configuration names and supplied corrections.

Failure/resume: Retain conflicting source identities; resume when the exact item is clarified or an authorized source becomes accessible.

**DOM-06-A02 — Attach item-level terms and permitted operations.** Associate each retained asset and derivative plan with its actual terms.

Input: Item inventory; actual asset LICENSE/terms text and URL/revision; attribution; requested usage operations.

1. Identify the terms applying to each file.
2. Quote or locate the applicable clause and record its operation scope.
3. Attach notices and a permitted-use conclusion with evidence status.

Output: Per-file identity/terms receipt with intake-draft status, consumed directly by DOM-38-A01 when STEP inspection is required, then by DOM-06-A03.

Validation: Independent source-reading reviewer checks clause/file applicability and notices; verify each proposed derivative has a recorded terms basis.

Failure/resume: Keep an external item link and precise question when the terms prevent or leave the requested operation unclear; resume that operation after a supported resolution.

**DOM-06-A03 — Classify component representations and interface evidence.** Describe what each asset contains and which named uses its evidence supports.

Input: DOM-06-A01/A02 identity/rights receipt; actual assets and source evidence; DOM-38 checked representation receipt when STEP transfer is required for the requested use.

1. Classify each retained representation and its role.
2. Attach declared/measured units and frames.
3. Link required interface features to their source evidence and criteria.

Output: Representation and feature-evidence records, consumed by DOM-06-A04 and DOM-38/DOM-07. Preserve source IFC element or MJCF body identities and frame links when supplied; later domain operations own their semantic transformations.

Validation: Check representation labels against actual reader findings; independent reviewer verifies the feature/source mapping and intended-use fit.

Failure/resume: Preserve an unreadable/unsupported file and reader error; route another supported representation or obtain the exact required source evidence.

**DOM-06-A04 — Register the component record and handoff conditions.** Publish a traceable component record referencing preserved originals and item terms.

Input: Identity/rights receipt plus required representation/feature evidence, including DOM-38 verification when the target use requires imported STEP geometry.

1. Assemble identity, terms and representation records.
2. Validate each required reference and source digest.
3. Mark readiness for the specific import/placement/version action.

Output: Component-record with source/terms/geometry references, consumed by DOM-26, DOM-38 and DOM-07.

Validation: Reopen the record and resolve every retained file/terms reference; independent semantic check compares it with the original selected item. Keep intake-draft/readiness per target action until its required representation evidence exists.

Failure/resume: Preserve failed record as a draft; fix the owning source/terms/representation entry and revalidate dependent handoffs.

**Execution options.**

1. **Agent-led:** Agent reads an unfamiliar item's identity, terms and representations; software hashes and inventories retained assets.
1. **Hybrid:** Software extracts known catalogue fields and file metadata; agent checks item-level terms and feature associations.
1. **Software-first:** A tested source family imports explicit item metadata and known terms revision; changed terms, configuration conflicts and unsupported geometry enter review.
1. **Deterministic:** Re-register the exact checked item/file/terms revisions using fixed rules and digest checks; new terms or use conditions trigger reassessment.

**Representation alternatives.**

1. Retain an external link with source/terms summary where the intended route uses remote reference only.
2. Preserve vendor native file and a separately identified authorized derivative.
3. Use a specifically licensed library alternative matching sourced interfaces when the task authorizes component choice.
4. Layout/appearance reuse can select a labelled envelope or display mesh with item provenance; precision/interface reuse requires sourced interface geometry and per-feature criteria. Retain original IFC/MJCF identities and frames for later domain operations.

**Parallel comparison and merge.** Separate candidates by exact item/configuration and intended use; record terms/geometry evidence and resource observations per candidate. Agent/VLM compares visible identity/features against source labels and dimensions; rights conclusion comes from the applicable terms passage. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Combine complementary metadata only for the same identified item/revision; preserve differing part/configuration and licence records as separate candidates. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Recheck identity, byte hashes, terms applicability and each feature-source association using a separate reviewer.

**Migration to software.** Retain checked intake examples per catalogue/item family; automate stable metadata/terms attachment and duplicate hashing; exercise configuration changes, mixed asset licences and restricted derivatives before software-first promotion.

**Future test cases.**

1. One package contains models with different applicable terms; every file retains its own association.
2. Two names contain identical bytes; digest deduplication preserves both source provenance records.
3. Changed vendor terms creates a new rights review without rewriting retained originals.
4. A visual mesh and analytic CAD representation receive distinct roles and feature evidence.
5. A configured item whose preview resembles another model remains associated with its actual part/configuration ID.

**Sources:** [1](../workflows/domain-paths.json), [2](../domains-and-components.md), [3](../implementation-plan.md), [4](https://www.kicad.org/libraries/license/), [5](https://github.com/google-deepmind/mujoco_menagerie), [6](https://polyhaven.com/license), [7](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280).

### DOM-07 — Place reusable component in assembly

**DOM-07-A01 — Resolve source and target interface identities.** Bind a component occurrence to the intended assembly interface.

Input: Component-record; required assembly-graph; measurement-set; source/target datum IDs, geometry revisions and stated mating relation.

1. Resolve the component definition and target occurrence.
2. Read the exact interface observations.
3. Associate the supplied mating relation with the intended feature pair.

Output: Interface correspondence and placement prerequisites, consumed by DOM-07-A02.

Validation: Verify all measurement references belong to pinned revisions; separate semantic reviewer checks centre/edge, axis sign and component occurrence.

Failure/resume: Retain candidate datums on ambiguity; block dependent transform and resume after the exact correspondence is established.

**DOM-07-A02 — Compute the occurrence transform.** Compose the sourced frames into one explicit placement transform.

Input: Checked source and target interface frames; declared mating offset; source-unit conversion; per-interface criteria.

1. Normalize explicit length units and coordinate conventions.
2. Compose the three named transforms in the stated direction.
3. Apply the result to interface control observations and compare the target relation.

Output: Component-to-assembly transform with derivation and residual checks, consumed by DOM-07-A03.

Validation: Verify inverse/round-trip consistency, orthonormal rigid rotation and determinant +1 after explicit convention conversion; test independent control points and named axes within their sourced criteria.

Failure/resume: Reject singular/incompatible frame mappings and preserve operands; resume from the corrected frame/offset and invalidate dependent placements.

**DOM-07-A03 — Insert the component occurrence and connection edge.** Apply the checked transform while preserving reusable source geometry.

Input: Pinned component definition; checked transform; target document/revision; assembly-graph; native API capabilities.

1. Create or reference the definition without editing its original.
2. Insert one occurrence with the checked transform.
3. Record its connection edge and read back both identities.

Output: Occurrence plus graph edge and actual transform readback, consumed by DOM-07-A04.

Validation: Check exactly one intended occurrence was added, graph endpoints resolve and source hash is unchanged; compare actual and intended transforms.

Failure/resume: On uncertain completion query the same request; reconcile native occurrence and graph before retry; preserve partial results and avoid duplicate instances.

**DOM-07-A04 — Measure placed interfaces and preserve the result.** Validate the occurrence's actual position and assembly relation.

Input: Placed occurrence, graph edge, source measurements, saved revision and feature-specific validation criteria.

1. Read back placed interface features.
2. Compare numerical and semantic relations with the source.
3. Reopen the saved assembly and recheck occurrence identity/placement.

Output: Placement verification and pinned assembly update, consumed by CAD-12/DOM-26/DOM-39.

Validation: Require both revision-bound numerical checks and separate semantic review; bounding-box intersection remains a candidate pair classification.

Failure/resume: Retain the failed placement; return to correspondence, calculation or insertion as indicated; invalidate only dependent occurrence checks.

**Execution options.**

1. **Agent-led:** Agent/VLM interprets unfamiliar interfaces and directs measured placement; software supplies explicit transform arithmetic and readback.
1. **Hybrid:** Agent selects sourced datums/mating relation; software composes and applies the transform and checks residuals.
1. **Software-first:** Known component/interface families use tested placement rules; missing or inconsistent frames enter evidence review.
1. **Deterministic:** Pinned source/target frames, mating offset and occurrence graph drive repeatable insertion and validation with stable request identities.

**Representation alternatives.**

1. Manual datum selection followed by explicit transform calculation and numeric readback.
2. Constraint-driven native assembly for sourced mating relations; solver result retains actual constraints and degrees of freedom.
3. Explicit placement for a static arrangement when that is the requested use.
4. For a sketch arrangement, place the sourced envelope using declared layout anchors; for a working interface, require sourced mating frames, axis identity and feature tolerances.

**Parallel comparison and merge.** Candidate datum correspondences share pinned component/assembly revisions; each records intended pose, feature accuracy and resources. VLM compares source views, feature names and numerical residuals to select a supported correspondence; model agreement is recorded separately. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Merge complementary measured datums only when their identities/frames agree; preserve conflicting transforms and source evidence. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Recalculate the merged transform, reapply to named control features, then independently check actual placed geometry and graph.

**Migration to software.** Automate frame composition first; retain semantic datum selection until checked family cases support it. Promote only mappings tested with mirrored axes, repeated occurrences, unit changes, stale sources and partial commits.

**Future test cases.**

1. Known source/target frames and mating offset yield the checked occurrence transform and preserved source geometry.
2. Swapped transform direction fails named control-point checks.
3. Unit conversion and a coordinate reflection are recorded separately from rigid placement.
4. Repeated component definitions produce distinct occurrence and graph IDs.
5. Native insertion succeeds but graph update fails; resume reconciles the existing occurrence instead of duplicating it.
6. Component plus measurements with an absent, stale or wrong target assembly revision/graph blocks placement before any mutation; source and target identities must match the declared graph prerequisites.

**Sources:** [1](../workflows/domain-paths.json), [2](../domains-and-components.md), [3](../workflows/composition-rules.md), [4](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), 5 (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`), 6 (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), 7 (`${OCS_ROOT}/docs/automation/API-SPEC.md`).

### DOM-26 — Version and reuse component revision

**DOM-26-A01 — Classify the component change and identify new bytes.** Determine which source, metadata, terms or derived artifact changed.

Input: Component-record whose required intake/representation references exist; prior revisions; changed source/terms/metadata; original and derivative byte hashes. Preliminary file digests remain intake evidence until component publication prerequisites pass.

1. Compare candidate and previous source/terms digests.
2. List changed fields and affected feature checks.
3. Assign a candidate revision linked to its predecessor.
4. Create a new metadata/rights revision for changed terms or frame meaning even when geometry bytes are equal.

Output: Change classification and candidate revision identity, consumed by DOM-26-A02.

Validation: Recompute digests and confirm earlier revisions resolve unchanged; independent reviewer checks revision-versus-new-component classification.

Failure/resume: Retain the candidate change and original records on conflict; resume after exact identity or source correction.

**DOM-26-A02 — Resolve the complete dependency and rights set.** Find every pinned input required to reproduce and reuse the candidate revision.

Input: Candidate revision; referenced source assets, child components, terms, adapter versions, parameters and derivative manifests.

1. Traverse all source and derivative dependencies.
2. Verify each immutable target and applicable terms record.
3. List downstream assemblies/exports affected by each changed edge.

Output: Closed dependency manifest and impacted-consumer list, consumed by DOM-26-A03.

Validation: Every referenced artifact resolves to the recorded bytes; independent reviewer checks semantic dependency completeness and terms scope.

Failure/resume: Preserve unresolved edge names and affected consumers; resume from repaired pins or restored originals, then repeat closure.

**DOM-26-A03 — Publish a new immutable revision and explicit reuse pins.** Make the checked revision addressable without changing earlier consumers.

Input: Closed candidate manifest; storage policy; existing revision namespace; explicitly requested consumer updates.

1. Persist the new revision under a new identity.
2. Verify its bytes and manifest.
3. Update only the explicitly selected consumers and record their new revisions.

Output: New component revision and separately updated consumer pins, consumed by DOM-26-A04.

Validation: Old pins still resolve unchanged; new pins resolve the new digest; compare the intended and actual consumer change set.

Failure/resume: On partial publication retain temporary/new artifacts and old authoritative pins; reconcile actual state before completing metadata or consumer updates.

**DOM-26-A04 — Reopen pinned artifacts and check reuse reproducibility.** Verify that the revision can be resolved with its original dependency identities.

Input: Published revision, dependency manifest, consumers and existing validation reports.

1. Reopen all pinned metadata/artifact references.
2. Compare hashes and check-report revision identities.
3. Record which downstream placements/exports need new checks.

Output: Revision resolution report and downstream test obligations, consumed by DOM-07/DOM-39.

Validation: All pins resolve correctly; source/terms closure holds; changed geometry has explicit pending validation for its named use.

Failure/resume: Preserve unresolved/corrupt artifact evidence; restore exact bytes from permitted retained originals or create a new corrected revision; recheck dependent pins.

**Execution options.**

1. **Agent-led:** Agent interprets unfamiliar revision/identity and terms changes; software computes digests and dependency differences.
1. **Hybrid:** Software builds change/dependency manifests; agent classifies semantic impacts and selects task-authorized consumer updates.
1. **Software-first:** Known immutable record families publish through checked rules; identity changes, terms changes and broken references enter review.
1. **Deterministic:** Resolve and republish exact pinned inputs/configurations under a tested content-addressed policy with collision and integrity checks.

**Representation alternatives.**

1. Git-tracked metadata and small licensed sources under the established repository policy.
2. Git LFS for versioned binaries when the repository supports it and use is authorized.
3. Content-addressed asset storage with immutable digests and readable retrieval manifests.
4. Version layout and precision derivatives separately with their purpose, lineage and feature criteria; a source revision change selectively invalidates the affected derivative checks.

**Parallel comparison and merge.** Candidate revisions retain separate source/terms/dependency identities and intended consumer targets. Agent compares source changes and actual geometry evidence; VLM may compare source-linked previews for semantic change while hashes identify bytes. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Merge compatible metadata/lineage contributions into a new revision; retain geometry and terms identities explicitly; earlier pinned revisions remain addressable. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Repeat digest, dependency, rights and impacted-check closure; independent reviewer verifies consumer pin changes.

**Migration to software.** Start with agent-reviewed revision classifications; automate digest and dependency closure; promote publication rules after checked terms-only changes, dependency loss, partial writes, corrupt files and unchanged consumer pin cases.

**Future test cases.**

1. A source-byte change creates a new revision while an existing assembly keeps its old pin.
2. A terms-only change produces a new rights/revision record with unchanged geometry bytes.
3. Missing derivative dependency fails closure with exact edge/consumer identification.
4. Interrupted metadata publication leaves the previous revision readable and resumes without overwriting it.
5. A changed interface invalidates its placement/export checks while unrelated feature evidence stays linked to its original revision.

**Sources:** [1](../workflows/domain-paths.json), [2](../domains-and-components.md), [3](../implementation-plan.md), [4](../workflows/composition-rules.md).

### DOM-38 — Import STEP solid into CAD representation

**DOM-38-A01 — Inspect STEP identity, structure and unit evidence.** Determine the supplied STEP file's representation and the import requirements.

Input: Original STEP bytes plus DOM-06-A01/A02 identity/rights receipt or equivalent retained source record; schema/header, declared units/product structure and known interface dimensions. A completed component-record is not an import prerequisite.

1. Preserve original bytes and hash.
2. Inspect schema, product structure and actual unit references.
3. Record expected part/interface/representation checks from the source.

Output: STEP intake manifest and expected invariants, consumed by DOM-38-A02.

Validation: Validate header/entity references and control dimensions; classify analytic, faceted and mixed data from actual entities, retaining uncertainty on unsupported entities.

Failure/resume: Preserve parser diagnostics and source bytes; pause dependent import on ambiguous units or unsupported schema and resume with a supported reader/source decision.

**DOM-38-A02 — Choose and configure an isolated importer.** Bind import to an actual tool/version and the source information it must preserve.

Input: STEP preflight manifest; target native representation; importer capabilities/settings; authorized destination.

1. Record importer/version and supported schema.
2. Select target representation and preservation requirements.
3. Create the bounded import destination and record settings.

Output: Import plan and isolated target context, consumed by DOM-38-A03.

Validation: Check the plan accounts for every required identity/shape/frame field; preserve existing document state and explicit source-to-target unit rule.

Failure/resume: Unsupported field/schema returns to importer choice; stale or occupied destination requires a fresh state read without overwriting unrelated work.

**DOM-38-A03 — Transfer geometry and classify actual output.** Create the CAD derivative and record what the importer produced.

Input: Isolated import context; original STEP; configured importer; expected invariants.

1. Execute import into the isolated destination.
2. Capture diagnostics and actual resulting structure.
3. Classify representation and map source products to imported objects.

Output: Imported native geometry and transfer mapping/diagnostics, consumed by DOM-38-A04.

Validation: Detect empty result, invalid/open topology and dropped products; validate finite bounds and actual scale; compare expected occurrence identities.

Failure/resume: Retain failed/partial target and logs; reconcile operation state before retry; a healing or remodel proposal creates a separately identified derivative.

**DOM-38-A04 — Measure and independently reopen imported geometry.** Check the actual imported representation against source controls and requested use.

Input: Imported revision; original STEP; known source/control dimensions; feature tolerances; independent reader route.

1. Measure source controls on imported geometry.
2. Save and reopen the derivative within the named scope.
3. Compare independent reader observations and investigate discrepancies.

Output: Import verification and native artifact identity, returned to DOM-06-A03/A04 for component-record completion and then consumed by CAD-12/DOM-07/DOM-26.

Validation: Report identity/scale/feature residuals, topology and face types; valid-solid volume comparisons use comparable closed shapes; same-kernel agreement records that dependency. Match product definitions and occurrences by stable mapping/parent path, including local and world placements; equal bounds/volume still require critical-interface checks.

Failure/resume: Preserve both reader results and artifacts; classify importer, unit, topology or source discrepancy and resume the owning step.

**Execution options.**

1. **Agent-led:** Agent inspects unfamiliar schema/units and chooses a supported importer; software records transfer and geometry measurements.
1. **Hybrid:** Importer performs transfer; agent interprets representation/semantic losses and VLM compares source-linked geometry views.
1. **Software-first:** Tested STEP schema/exporter families use pinned importer settings; ambiguous units, failed solids and hierarchy losses enter review.
1. **Deterministic:** A checked input/exporter family and explicit target contract drive repeatable import and invariant checks with pinned tool/settings.

**Representation alternatives.**

1. Receiving CAD application's native STEP importer with its actual representation report.
2. FreeCAD/Open CASCADE assembly-aware import when product/occurrence preservation is required.
3. Geometry-only STEP import for a task explicitly requiring individual shape geometry; retain original product metadata separately.
4. A layout consumer may use inspected faceted/display geometry with its declared approximation; an interface consumer requires the relevant source surface/edge identity and measured feature criteria.

**Parallel comparison and merge.** Independent importers retain separate targets, tool/settings, intended use, source hash and resource records. VLM compares source product identity and views while numerical readers compare dimensions, placements, topology and representation; source controls govern selection. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Select a checked complete import or combine separately identified product records only through explicit source-object mapping; retain original source and all candidate reports. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Recheck the selected/combined artifact's product identities, unit/frame mapping, shape validity, feature controls and independent semantic associations.

**Migration to software.** Automate preflight/invariants for exercised STEP producer/schema families; retain source/semantic exceptions. Test analytic/faceted/mixed solids, assembly products, unit variants, invalid shells and healing changes before expanding support.

**Future test cases.**

1. An analytic curved-face STEP retains the expected surface types and sourced dimensions.
2. A faceted STEP is reported with planar facets after import.
3. Repeated product occurrences preserve separate placements when the target contract requires hierarchy.
4. A missing or unreferenced unit entity triggers a source-control/unit decision instead of an inferred scale.
5. Invalid/open shell input yields an explicit result and preserved source; healing is a new derivative.
6. Two readers with a shared kernel record that dependency beside matching results.

**Sources:** [1](../workflows/domain-paths.json), [2](../local-baseline.md), [3](../workflows/details/dom-r02.md), [4](../domains-and-components.md), [5](https://cadquery.readthedocs.io/en/stable/importexport.html), 6 (`${OCS_ROOT}/src/io/step.rs`), [7](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md), [8](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___reader.html).

### DOM-39 — Export STEP assembly

**DOM-39-A01 — Freeze the native assembly and export contract.** Define the assembly revision and information that the STEP derivative must carry.

Input: Native assembly revision; component pins; output schema/consumer; item terms; required names, occurrence hierarchy, units and geometry properties.

1. Freeze source revision and all component pins.
2. List required product tree, placements, geometry and names.
3. Attach consumer/schema and feature-comparison criteria.

Output: Export manifest and per-field preservation requirements, consumed by DOM-39-A02.

Validation: Check manifest matches the native assembly and every required component has rights/provenance; independent reviewer checks occurrence versus definition meaning.

Failure/resume: Source changes invalidate the frozen export plan; retain old manifest and resume on the selected new revision.

**DOM-39-A02 — Select the assembly-aware exporter and settings.** Choose an exporter whose exercised behavior can satisfy the required STEP structure.

Input: Frozen export contract; actual exporter/version capabilities; target schema; unit/healing/tessellation settings.

1. Inspect actual installed exporter capabilities.
2. Choose schema and geometry/product preservation mode.
3. Record unit, precision and representation settings against the export contract.

Output: Exporter configuration and capability mapping, consumed by DOM-39-A03.

Validation: Trace every required invariant to an actual exporter capability or future fixture check; unit declaration must be referenced and verified by consumer readback.

Failure/resume: Retain the contract and rejected route evidence; select another supported exporter or obtain the exact changed-deliverable decision.

**DOM-39-A03 — Write the STEP derivative and preservation mapping.** Create a new STEP artifact from the frozen assembly revision.

Input: Frozen source; selected exporter/configuration; authorized derivative path; preservation contract.

1. Recheck the frozen source hashes/revision.
2. Export the assembly to the named derivative path.
3. Record output digest, diagnostics and preserved/transformed/dropped fields.

Output: STEP bytes/hash, export log and native-to-STEP mapping, consumed by DOM-39-A04.

Validation: Verify nonempty readable STEP, unchanged native source and completed output bytes; inspect schema/unit/product entities before consumer import.

Failure/resume: Retain partial artifact/logs; reconcile completion using output identity and tool state; retry to a separately identified candidate after diagnosis.

**DOM-39-A04 — Reopen and compare the exported assembly.** Verify the STEP artifact in the actual receiving path.

Input: Exported STEP/hash; frozen native manifest; feature criteria; actual consumer and optional second reader.

1. Read STEP through the actual consumer.
2. Compare native and imported product trees and named feature measurements.
3. Record preserved, changed and lost fields and retain the checked output hash.

Output: Export verification, checked derivative and field-loss report, consumed by the intended receiver/DOM-26.

Validation: Numerical invariants and independent semantic mapping must both pass for the named use; compare per-part closed-shape volume only where applicable and distinguish union from occurrence totals. Compare parent paths and both local and composed world transforms; identical geometry hashes and aggregate counts cannot identify repeated occurrences alone.

Failure/resume: Preserve both native and imported results; locate exporter/importer/unit/representation fault and reopen the owning action; rerun affected checks on a new derivative.

**Execution options.**

1. **Agent-led:** Agent interprets unfamiliar consumer/assembly requirements and selects an exporter; software exports and measures actual readback.
1. **Hybrid:** Agent maps required semantics and settings; software performs assembly export and structural/numerical comparisons.
1. **Software-first:** A tested source/exporter/consumer pair exports known assembly classes; changed schema, warnings or failed invariants enter review.
1. **Deterministic:** Pinned native tree, exporter configuration and consumer contract drive export and readback checks; output bytes may include timestamps, so compare semantic invariants alongside recorded hashes.

**Representation alternatives.**

1. Assembly-aware STEP export preserving named definitions/occurrences when exercised for the target consumer.
2. Individual-solid STEP files plus explicit placement/identity manifest when that deliverable is requested.
3. Native assembly delivery plus a separately labeled faceted display derivative when both artifacts serve the requested use.
4. Layout exchange can carry an explicitly labelled faceted derivative with its approximation criteria; precision exchange retains required analytic/other source geometry and per-feature consumer checks.

**Parallel comparison and merge.** Exporter/consumer candidates use the same frozen native assembly and required feature set; each records representation/detail target and resources. VLM checks product/feature meaning against native views while software compares tree/transform/surface invariants; select the source-supported route meeting the consumer contract. Compare the common required features even when branch detail differs; retain per-branch purpose, criteria, input subset, local/remote resource and manual review records. Combine separately exported components only through an explicit manifest with preserved source identities/placements and a requested deliverable; retain each candidate artifact and loss report. Evidence enrichment of the same item/feature differs from whole-component substitution. Copying geometry features across parts/revisions creates a new authored hybrid requiring its own identity and scoped modeling action. Conflicting dimensions remain explicit; they are not averaged. Reopen the combined/selected deliverable in its actual consumer and repeat structural, per-feature numerical and independent semantic checks.

**Migration to software.** Capture agent-chosen export settings and failures per source/exporter/consumer pair; automate only checked mappings. Test repeated parts, nested occurrences, mixed units, mirrored placement, analytic versus faceted geometry and dropped names before promotion.

**Future test cases.**

1. Repeated and nested occurrences retain required definition/occurrence distinction and transforms after target import.
2. An analytic assembly export preserves required curved surfaces; faceted output reports its planar representation.
3. The OCS mesh writer is tested separately for actual unit and single-shell structure; it cannot be assumed to preserve an assembly tree.
4. A consumer dropping names or flattening hierarchy produces an explicit required-field failure.
5. A changing source during export invalidates the frozen revision and yields a distinct retry artifact.
6. Semantically equal exports with different timestamp bytes retain separate hashes while passing declared invariants.

**Sources:** [1](../workflows/domain-paths.json), [2](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md), [3](https://cadquery.readthedocs.io/en/stable/importexport.html), [4](../cad-and-skills.md), [5](../domains-and-components.md), 6 (`${OCS_ROOT}/src/io/step.rs`), [7](../workflows/composition-rules.md), [8](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md), [9](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___writer.html).

## 6. Shared interruption and revision protocol

For remote reasoning/VLM work, preserve request/call identity, input package and source hashes, partial/raw response, parser/evaluation error and last complete validated record. Reconcile uncertain completion through available provider response state before retry; associate every retry with the earlier identity. Recheck source digests at resume; validate remaining selection rows against the frozen evidence, and publish one identified completed review result. Malformed or partial responses remain retained evidence and do not alter the current merged artifact. CAD document mutation uses its separate native request/document/revision reconciliation protocol.

**Future shared test.** Shared remote-review interruption case: lose a remote/VLM response, receive malformed selection rows on a linked retry, and change one source before resuming. Expected result: retain raw request/response evidence and retry lineage, reconcile completion, recheck source digests, preserve the current merged artifact until complete valid rows exist, and invalidate only records dependent on the changed source.

At every resume, compare source and target revision/hash records with the saved boundary. A changed source creates a new candidate revision and invalidates its dependent mappings, checks and exports. Preserve failed artifacts, actual error text, completed steps, source evidence and prior successful results on their original revisions.

## 7. Development and verification status

| Operation | Proposed helper development and input/output responsibility |
| --- | --- |
| CAD-12 assembly | Definition intake → source/occurrence manifest; interface mapping → placement plan; occurrence adapter → native tree; assembly invariant reporter → revision-bound feature/structure findings |
| DOM-06 library intake | Item intake → exact source/file inventory; rights attachment → per-file operation evidence; representation inspector → role/feature records; component validator → specific downstream prerequisites |
| DOM-07 placement | Datum resolver → checked correspondence; frame composition → sourced transform/residuals; placement adapter → occurrence/graph update; occurrence reporter → actual interface/readback results |
| DOM-26 revision reuse | Revision diff → source/terms/metadata changes; dependency closure → immutable pins and impacted consumers; revision publisher → recoverable new revision; resolution reporter → reproducibility and affected-check findings |
| DOM-38 STEP import | STEP preflight → actual schema/unit/product evidence; importer adapter → isolated configured transfer; transfer recorder → shapes/entity mappings; invariant report → per-feature and semantic readback findings |
| DOM-39 STEP export | Export contract builder → frozen tree/feature requirements; capability adapter → tested route/settings; export wrapper → derivative and preservation mapping; exchange comparator → actual consumer tree/transform/interface findings |

1. Each action's proposed helper specifies its input/output role in the [structured action specification](point-02-operations.json). They are development proposals; the existing tool sources establish only their documented or inspected behavior.
2. Future tests require retained input sources, checked expected identities/measurements, per-feature criteria and actual tool/model versions. Compare deterministic measurements and independent semantic findings separately.
3. Migration is per operation and input family: record agent actions; define stable rules; retain successful, ambiguous, failed and interrupted checked cases; implement the scoped helper; test on held-out cases; promote only the demonstrated family and route exceptions to source review.
4. [Designer notes](reviews/point-02-designer.md) record local sources, review integration and document checks. The coordinator owns source/idea registers and batch commits.
