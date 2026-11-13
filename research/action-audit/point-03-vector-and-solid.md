# Point 03 — Confirmed dimensions and vector drawings to small CAD models

Date: 2026-11-12. Status: **procedure proposal**. Scope: ten operations and 31 actions. Requested procedure-design dispatch: `gpt-6-astra`, `xhigh`; actual executing model identity: **unavailable**.

[Structured action records](point-03-operations.json) contain all 15 required fields for every action: purpose, intended use, inputs, outputs, accuracy, evidence, software, agent, user decisions, dependencies, proposed development, procedure, validation, failure/resumption and resources. This document supplies the readable sequence and concrete representation boundaries. The [execution plan](plan.md), [original CAD records](../workflows/cad-paths.json), [original domain records](../workflows/domain-paths.json), OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) and [retained implementation plan](../implementation-plan.md) supply the governing contracts. Procedures, proposed helpers and future cases describe work to execute under its own authorized task. Acceptance labels use the explicit `MARK AS ACCEPTED` instruction.

## 1. Sequence, representations and feature criteria

1. A vector source follows **CAD-08** for inspected/cleaned geometry, then **CAD-09** for source-linked constraints when required. **DOM-03** composes those actions into its declared profile output and reuses their checked receipts.
2. Confirmed dimensions, a compatible profile or parameter source follow **CAD-10** for kernel construction. **DOM-04** provides the native artifact handoff. **DOM-40** supplies the source-authoring and generation route when script parameters are the editing representation.
3. **CAD-15** evaluates source-defined CSG to a mesh. **CSG**, or constructive solid geometry, forms shapes through combinations, subtractions and intersections of solids. **DOM-05** exports a declared solid representation to STEP through a supported adapter. **CAD-13** verifies the actual geometry and saved output. **CAD-14** returns the bounded recovery brief to the owning failed action.

A **B-rep**, or boundary representation, stores surfaces, edges and their connections. Surfaces can be analytic, such as a plane or cylinder, or represented by splines or facets; the artifact records its actual surface types. A **mesh** stores facets and their connections. **Topology** describes how vertices, edges and faces connect. A **pinned revision** is an explicitly fixed revision or content hash. A **residual** is a measured difference after a constraint or geometric comparison, recorded with method and units.

Each required feature retains source locator, source value/status, units, datum and axis/frame. Its engineering allowance, measurement uncertainty, solver criterion and saved/export comparison threshold have separate fields and sources. Source-supported loop closure, repair distance, curve approximation, extrusion direction, hole axis and component boundary receive their own checks. Source dimensions are preserved through entity → loop → constraint/parameter → native feature → saved/exported feature mappings.

A lower-detail arrangement branch can retain named envelopes, datums and interfaces. A precision branch adds the required detailed features and their individual criteria. For example, a task may require bore/axis/interface checks or opening/elevation checks; the actual values come from that task's sources. Detail and use are recorded per branch, and every readiness result names the consuming operation and features. A **VLM**, or vision-language model, processes source images and language together for evidence-based interpretation and candidate selection.

## 2. Supported entrypoints and source status

1. [ezdxf](https://ezdxf.readthedocs.io/en/stable/tasks/query.html) documents entity queries, while [unit documentation](https://ezdxf.readthedocs.io/en/stable/concepts/units.html) records unitless coordinates, declared document units and explicit block scaling. [SVG 2](https://www.w3.org/TR/SVG2/coords.html) defines viewport/viewBox and nested coordinate transforms.
2. [FreeCAD Sketcher documentation](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md) demonstrates geometry/constraint construction and recompute. The archived example supplies API guidance; the selected build must expose the required diagnostics before a diagnostic check can pass.
3. [build123d](https://build123d.readthedocs.io/en/latest/operations.html) documents Sketch/Face extrusion to Part. [CadQuery](https://cadquery.readthedocs.io/en/stable/importexport.html) documents DXF wires, downstream extrusion and STEP exchange. Its [Shape API](https://cadquery.readthedocs.io/en/stable/classreference.html) documents kernel shape validity.
4. Local OCS host enum (`${OCS_ROOT}/crates/ocs_plugin_api/src/host.rs`), implementation (`${OCS_ROOT}/src/app/plugin_host.rs`) and Python binding (`${OCS_ROOT}/plugins/opencad-python/src/document_model.py`) provide native create/transform/profile/extrude/Boolean evidence. The kernel note (`${OCS_ROOT}/docs/cadkernel-body-path.md`) contains earlier proposals followed by implemented status and historical tests. Native operations and the faceted STEP writer (`${OCS_ROOT}/src/io/step.rs`) have separate capability records.
5. [OpenSCAD documentation](https://openscad.org/documentation) and the [previous manual source record](../sources/source-register.md#src-ce92c7f02e89) support source-defined CSG/mesh work. The fresh source role inspected the documentation index; its manual evidence comes from the prior record.

The [software review](reviews/point-03-software.md), [visual review](reviews/point-03-visual.md) and [source review](reviews/point-03-sources.md) identify the inspected evidence and version conditions. The following procedures are proposed compositions of those capabilities.

## 3. CAD-08 — Read and clean vector drawing geometry

Entry points and evidence: [ezdxf queries](https://ezdxf.readthedocs.io/en/stable/tasks/query.html), [DXF units](https://ezdxf.readthedocs.io/en/stable/concepts/units.html), [SVG coordinates](https://www.w3.org/TR/SVG2/coords.html), [CAD-R04](../workflows/details/cad-r04.md).

1. **CAD-08-A01 — Inspect source entities, units and drawing contexts.** Read the original DXF/SVG and hash; inventory entities by type, layer, model/paper space and block occurrence. Record DXF declared units and nested transforms, or SVG viewport, physical dimensions, viewBox and transforms. Associate selected profile entities with their source component and plane.
2. **CAD-08-A02 — Create a mapped and explicitly cleaned derivative.** Apply the recorded unit/frame transform to a derivative; classify open ends, duplicates, crossings and nonplanarity. Apply only source-supported repairs within individual feature criteria. Preserve source-to-result IDs and before/after geometry, including curve-type changes from nonuniform scale.
3. **CAD-08-A03 — Validate curve fidelity and publish the vector handoff.** Compare controlling dimensions and analytic-curve fidelity; check actual closure, intersections and outer/hole/island roles. Publish checked vector geometry, source map and explicit unsupported/dropped entities to CAD-09/DOM-03.

DXF coordinates have unit declarations and explicit block scale behavior. SVG display coordinates require the complete viewport transform chain. Importer-specific SVG flattening and fallback scale are recorded beside the resulting geometry. A closed flag alone cannot pass the geometric loop check.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets unfamiliar drawing structure and selects source-supported entities/repairs; tools measure and preserve source mappings. |
| Software and agent | Parser handles units/entities/transforms; agent/VLM chooses profile associations and repair meaning. |
| Software handles ordinary cases | Known exporter/layer/entity families use checked normalization; unsupported entities or geometry-changing repairs enter review. |
| Deterministic supported case | Explicit entity selection, transforms and tested repair rules replay against pinned source/importer revisions. |

**Alternatives.** Keep native source curves unchanged when the intended use needs no cleanup. Layout profiles may use a labelled approximation with its deviation record; precision profiles preserve required curves and feature criteria. Choose FreeCAD native/legacy DXF importer, OCS drawing workflow or ezdxf parser according to exercised entity coverage.

**Branch selection and merge.** VLM compares full source views and curve labels; software compares entity maps, critical dimensions and deviations. Combine compatible mapped loops from the same source meaning; retain conflicting repairs and dimensions without averaging. Recheck merged loop nesting, source mapping, units, critical dimensions and independent semantic correspondence.

**Proposed development.** drawing preflight retaining entity IDs, nested transforms, unit evidence and importer option receipt. curve mapping/repair helper with reversible source transform and per-edit change ledger. source-to-curve fidelity reporter with feature-specific readiness and lost-entity findings. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Retain failed derivative and exact missing/changed entity; resume the owning normalization/repair step. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 4. CAD-09 — Build and constrain an editable planar sketch

Entry points and evidence: [FreeCAD Sketcher scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md), OCS contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`).

1. **CAD-09-A01 — Map curves and sourced constraints to a sketch plan.** Map each source curve to sketch geometry and each source dimension/relation to a named constraint. Record support plane, datum, units, nominal value, source status and intended remaining freedom. Resolve radius/diameter, edge/centre, hole and symmetry associations before applying constraints.
2. **CAD-09-A02 — Create the sketch and solve bounded constraint groups.** Create geometry and add bounded constraint groups with the selected version's supported API; recompute and read actual solver diagnostics. Record remaining degrees of freedom, conflicts, residuals and geometry displacement where supported. An unavailable required diagnostic leaves its dependent check unresolved.
3. **CAD-09-A03 — Measure and reopen the constrained sketch.** Measure solved geometry against source values and loop meaning, then save/reopen the sketch. Independently review constraint-to-feature associations. Publish the actual constrained-sketch revision and supported diagnostics for the named downstream feature.

A degree of freedom is an independent movement remaining in the sketch. Intended free movement can remain. The archived FreeCAD example demonstrates addGeometry, addConstraint and recompute; the required diagnostic APIs must be discovered in the selected build. Solver consistency, source correspondence and profile closure receive separate results.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent chooses source-backed geometry/constraints and inspects each solve group. |
| Software and agent | Software creates and solves mapped constraints; agent reviews source associations and residual/conflict meaning. |
| Software handles ordinary cases | Checked sketch families use established constraint templates; unsupported curve/freedom/conflict cases enter review. |
| Deterministic supported case | Pinned curves, source values and explicit constraints solve and validate using a fixed supported backend/version. |

**Alternatives.** Keep nonparametric vector curves when that is the requested editable artifact; label their output separately. Use a native constraint-bearing FreeCAD sketch for editable dimensions. Use a code-defined profile where procedural source is requested, with that output representation explicit.

**Branch selection and merge.** VLM/source review compares geometric associations; software compares actual constraint values, residuals and remaining freedoms. Merge compatible relation records only after checking duplicate/redundant/contradictory constraints; preserve competing interpretations. Solve again and independently review merged source associations, loops, remaining freedom and saved sketch.

**Proposed development.** source-to-sketch constraint mapper with stable geometry IDs and intended freedom records. incremental constraint adapter and conflict reporter preserving source-to-constraint relationships. sketch evidence validator linking solver, geometry and native parameter behavior. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Preserve failed sketch/variant; return to owning mapping or solve step and invalidate dependent solids. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 5. CAD-10 — Create a kernel solid and native model document from confirmed parameters

Entry points and evidence: OCS host operations (`${OCS_ROOT}/crates/ocs_plugin_api/src/host.rs`), host implementation (`${OCS_ROOT}/src/app/plugin_host.rs`), Python solids interface (`${OCS_ROOT}/plugins/opencad-python/src/document_model.py`), REVOLVE command (`${OCS_ROOT}/src/app/command_driver/solid3d.rs`), [build123d extrusion](https://build123d.readthedocs.io/en/latest/operations.html).

1. **CAD-10-A01 — Select a supported solid feature route.** Choose a supported primitive, extrusion, revolution or Boolean sequence from the confirmed parameters/profile. Bind signed direction, axis, sweep and part boundary to sources. Check the actual backend input and result types before construction.
2. **CAD-10-A02 — Construct features with revision-bound readback.** Execute one bounded feature against named operands and target revision, retaining request and readback evidence. For profile preservation explicitly pass delete_source=False; for OCS Boolean operand preservation explicitly pass keep_operands=True. Read resulting handles and representation before the next dependent feature.
3. **CAD-10-A03 — Verify native solid and saved construction record.** Check solid/shell counts, actual face types, required holes/axes/dimensions and kernel validity; save/reopen native geometry. Retain native feature data or parametric source according to the chosen route, then hand the exact revision to CAD-13/DOM-04/DOM-05.

OCS plugin Extrude accepts one curve-profile handle and rejects Region. Closed profile produces Solid3D; open profile produces Surface. A solid requirement with open input blocks construction until sourced closure or a supported alternative exists. Outer/inner loops need an evidenced construction sequence. REVOLVE belongs to the separate command path. The Python Boolean default keep_operands=False consumes operands; preservation uses explicit flags and handle checks.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent chooses source-backed feature sequence and drives supported native operations with readback. |
| Software and agent | Software constructs explicit features; agent interprets source intent and diagnoses Boolean/profile exceptions. |
| Software handles ordinary cases | Checked feature families execute with explicit parameters; unsupported curves, refusal or history mismatch enter review. |
| Deterministic supported case | Pinned feature sequence, backend and parameters regenerate named bodies and validate native save/readback. |

**Alternatives.** OCS native kernel body via the actually exposed command/plugin interface. FreeCAD feature-history model when native editable feature dependencies are required. CadQuery/build123d source and B-rep when procedural parameters are the chosen editable record. Simplified layout geometry may be a separate declared derivative; OpenSCAD CSG mesh uses CAD-15 and its own output type.

**Branch selection and merge.** Source/VLM review compares feature meaning; kernel checks compare surfaces, critical dimensions and topology. Select a checked body or compose separately intended parts; cross-branch feature copying creates a new authored revision with explicit lineage. Recheck resulting body validity, component boundaries, interfaces, source correspondence and native reopen; separate reviewer evaluates semantics.

**Proposed development.** feature capability planner with explicit profile, operand and representation prerequisites. bounded feature executor with stable request IDs, operand lineage and explicit result representation. native-body invariant report with source-to-feature IDs and editability classification. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Keep failed saved/variant artifact; return to the owning feature and invalidate its downstream exports/checks. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 6. CAD-13 — Verify model geometry and saved output

Entry points and evidence: [Original CAD verification operation](../workflows/cad-paths.json), [CadQuery Shape API](https://cadquery.readthedocs.io/en/stable/classreference.html), OCS measurement contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`).

1. **CAD-13-A01 — Bind checks to actual artifacts and source criteria.** Bind every check to an exact artifact revision, required feature, source reference, unit/frame and individual criterion. Identify actual geometry available for measurement. A source-only script can receive source/provenance review; its geometry checks require a generated artifact or retained executed generation receipt.
2. **CAD-13-A02 — Read actual geometry and compare required features.** Query actual geometry for controlling dimensions, axes, parts, holes and structural validity. Compare independent source controls and record measured differences with the query method. Report unsupported queries individually; broad bounds/volume checks accompany critical-feature checks.
3. **CAD-13-A03 — Reopen saved artifacts and issue the verification report.** Reopen the supplied saved artifact read-only; a separately authorized save uses its named path and format scope. Repeat the artifact's required checks. An independent semantic reviewer inspects source-to-feature correspondence using the same revision. Publish check results, evidence and affected readiness, including failed checks.

CadQuery Shape.isValid() uses OCCT shape-defect checks. It supplies kernel-integrity evidence. OCS SAT/SAB validation shares OCS's kernel; retain that dependency. Native editability, exchange representation, physical dimensions and source meaning have separate checks.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent builds a use-specific check plan and directs actual measurements; software records and compares values. |
| Software and agent | Software runs planned geometry checks; agent reviews feature correspondence and exceptions. |
| Software handles ordinary cases | Supported artifact/check families run automatically; unsupported queries, missing source criteria and semantic changes enter review. |
| Deterministic supported case | Pinned artifact, criteria and supported queries produce a repeatable result; independent semantic evidence remains linked to its reviewed case. |

**Alternatives.** Native-only readback for the requested native artifact, recording its actual scope. Neutral-file roundtrip through the intended consumer with source-to-output mapping. Mesh-specific checks for a declared mesh deliverable; source-only verification for a supplied script until geometry evidence exists.

**Branch selection and merge.** Reasoning/VLM review evaluates source-feature meaning; numerical results compare named quantities rather than model votes. Combine compatible check findings by feature and exact revision; preserve conflicting measurements and query conditions. Validate report references, units, criteria and source-to-feature associations; a different artifact requires its own measurements.

**Proposed development.** representation-aware validation planner with per-claim evidence requirements. measured-check recorder with supported-query classification and independent semantic association. saved-artifact verification receipt with shared-kernel dependency record and explicit per-check status. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Retain failed file/reader diagnostics; route to CAD-14 with the failed transition and affected feature IDs; rerun only affected checks after correction. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 7. CAD-14 — Recover from failed interpretation or geometry construction

Entry points and evidence: [Original recovery operation](../workflows/cad-paths.json), OCS automation API (`${OCS_ROOT}/docs/automation/API-SPEC.md`), [composition rules](../workflows/composition-rules.md).

1. **CAD-14-A01 — Reconcile the failed operation and preserve its evidence.** Reconcile the failed or uncertain action against request identity, document revision, actual state and partial outputs. Preserve the failure report and last checked revision; establish which mutation or export completed.
2. **CAD-14-A02 — Diagnose the earliest invalid source-to-geometry transition.** Trace failed checks back through source interpretation, transforms, loop roles, constraints, feature operations and export. Identify the earliest invalid transition and affected descendants; retain independent valid branches.
3. **CAD-14-A03 — Revise the brief and issue a bounded retry plan.** Produce a revised source-linked brief and bounded retry plan naming the owning action, changed inputs and required rechecks. Preserve the failed revision. The named construction/interpretation/export operation performs any subsequently authorized geometry change.

CAD-14 outputs the recovery brief and retry plan. Kernel refusal, ambiguous evidence and unsupported API diagnostics produce different next actions. Remote reasoning uncertainty follows the separate shared protocol below.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets a novel failure from preserved sources and tool state, then issues a bounded correction brief. |
| Software and agent | Software reconciles states and localizes failed checks; agent identifies source/geometry meaning and recovery action. |
| Software handles ordinary cases | Known refusal/state/constraint patterns produce checked diagnoses; uncertain causes or new design intent enter review. |
| Deterministic supported case | A verified recovery rule for exact failure/input conditions emits the bounded retry plan and required rechecks. |

**Alternatives.** Obtain the exact missing source/reference and preserve the current artifact. Retain checked vector/profile output when the requested next shape route needs further input. Propose an explicitly scoped supported backend when the original operation refuses the required feature.

**Branch selection and merge.** VLM/source review compares evidence associations; software verifies actual request state and failed predicates. Combine compatible causal findings; retain competing source/design interpretations without changing values by consensus. Review the revised brief/retry graph independently; rerun geometry only through the owning operation and validate the new revision.

**Proposed development.** failure-state collector linking request state, artifact revisions and affected feature IDs. causal transition map linking failed predicates to source/constraint/feature/export actions. recovery-plan emitter with per-action prerequisites, restart boundary and required rechecks. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** On failed correction retain its revision and return to diagnosis; stop retries at the named unresolved source/backend condition. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 8. CAD-15 — Render source-defined CSG as a mesh

Entry points and evidence: [OpenSCAD documentation](https://openscad.org/documentation), [registered manual evidence](../sources/source-register.md#src-ce92c7f02e89), [CAD-R10](../workflows/details/cad-r10.md).

1. **CAD-15-A01 — Inspect CSG source, parameters and mesh criteria.** Bind the CSG source, included assets, parameter values, units/frame and required features to a fixed source revision. Specify final render/export mode and feature-specific tessellation criteria. Record the chosen OpenSCAD version/backend and output mesh format.
2. **CAD-15-A02 — Evaluate final CSG and export the mesh derivative.** Evaluate the final CSG and export a new mesh; retain process results, settings and input/output hashes. Distinguish any preview from the final evaluated artifact. Inspect actual output presence and representation before measurement.
3. **CAD-15-A03 — Measure the mesh and check declared parametric behavior.** Inspect saved mesh components, boundary edges, orientation, degenerate elements and required dimensions/holes. Compare surface approximation against its sourced criterion and inspect an explicitly supplied parameter variant when required. Publish mesh plus editable source and verification.

CSG means constructive solid geometry: shape operations combine or subtract source-defined forms. Tessellation approximates surfaces with facets. STL needs explicit unit interpretation; source parameters and mesh quality criteria stay in the receipt.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets supplied CSG and chooses source-backed resolution/consumer checks; software renders and measures. |
| Software and agent | Software evaluates explicit source/settings; agent reviews warnings and feature correspondence. |
| Software handles ordinary cases | Checked CSG/source families render with known mesh criteria; unsupported syntax, invalid output or feature loss enter review. |
| Deterministic supported case | Pinned source, dependencies, parameters and renderer/settings regenerate mesh and supported invariants. |

**Alternatives.** Lower-detail layout mesh with explicitly sourced approximation target and retained original source. Precision mesh consumer uses local-feature deviation and required topology criteria. A B-rep output requirement uses a compatible CAD-10/DOM-40 backend or a separately scoped modeling route.

**Branch selection and merge.** VLM compares source feature meaning; software compares critical dimensions, approximation and topology. Select a checked mesh or assemble explicitly separate source-defined components; geometry edits create a new derivative with lineage. Recheck units, connected parts, holes, normals, required closure and local feature deviation on the merged output hash.

**Proposed development.** source/render manifest and parameter/dependency validator. resumable render wrapper with source/settings digest and explicit mesh result type. source-to-mesh feature validator and variant comparison report. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Retain failed mesh and localized feature/error; return to render settings or sourced CSG correction as the evidence indicates. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 9. DOM-03 — DXF/SVG drawing to constrained profile

Entry points and evidence: [Original domain profile operation](../workflows/domain-paths.json), [DXF import](https://cadquery.readthedocs.io/en/stable/importexport.html), [Sketcher scripting](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Sketcher_scripting.md).

1. **DOM-03-A01 — Choose the profile target and source entity mapping.** Declare whether the requested profile needs editable native constraints, clean curves or a direct CSG profile. Select the required regions and map source entities, dimensions, plane and intended loop roles to that contract.
2. **DOM-03-A02 — Normalize curves and construct the constrained profile.** Consume CAD-08's checked curve derivative. For a constrained-sketch target, apply CAD-09 with explicit source-linked constraints and retain both action receipts; reuse a valid existing receipt for the same revision.
3. **DOM-03-A03 — Verify profile semantics and constrained editability.** Validate source-to-sketch mapping, profile topology, actual constraint data and saved editability. Hand off only the representation actually produced, with readiness for the named next operation.

CadQuery DXF import supplies wires and a downstream extrusion route; OpenSCAD supplies a profile/CSG route. A native constrained-sketch output requires actual constraint data and supported diagnostics. These routes retain separate typed handoffs.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets entity/loop/constraint meaning and selects an evidenced native sketch route. |
| Software and agent | Parser and sketch solver perform defined steps; agent reviews semantic associations and exceptions. |
| Software handles ordinary cases | Known vector export families and source-constraint mappings run automatically; unsupported geometry or target mismatch enters review. |
| Deterministic supported case | Pinned vector selection, transformations and explicit constraints produce and validate a native sketch through tested adapters. |

**Alternatives.** OCS-native drawing edit for a vector output with its stated semantics. FreeCAD native constraint-bearing sketch for the constrained-profile contract. CadQuery DXF wire or OpenSCAD profile extrusion as explicitly changed-output routes. Layout approximation retains source curves and deviation; precision profile preserves required curve/constraint evidence.

**Branch selection and merge.** VLM evaluates source loops and feature labels; software checks geometry/constraint values and native object type. Merge mapped compatible loops/constraints; retain unsupported or conflicting source relations and exact alternatives. Recheck actual constraint graph, loop semantics, source dimensions and native reopen on the merged revision.

**Proposed development.** profile route selector exposing actual output type and required source/constraint inputs. composed profile adapter joining existing curve and sketch receipts by stable feature IDs. profile handoff validator that distinguishes constrained-sketch from clean-wire or mesh outputs. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Retain failed profile and return to its owning mapping/constraint action; invalidate dependent solid features. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 10. DOM-04 — Brief/profile to native CAD solid

Entry points and evidence: [Original native-solid operation](../workflows/domain-paths.json), OCS kernel note (`${OCS_ROOT}/docs/cadkernel-body-path.md`), [build123d operations](https://build123d.readthedocs.io/en/latest/operations.html).

1. **DOM-04-A01 — Define native artifact and solid prerequisites.** Define native editability, required solid representation, selected application and source-linked feature inputs. Check actual backend capabilities and consuming operations; choose feature history, native body document or parametric source as the explicit retained record.
2. **DOM-04-A02 — Construct or reuse the checked native body.** Construct through CAD-10 or consume a matching checked solid receipt; preserve source geometry and intended component boundaries. Record actual geometry type and native/source lineage, including any supported feature-history changes.
3. **DOM-04-A03 — Save and validate the native model contract.** Save/reopen the chosen native artifact and check its required features and retained editing representation with CAD-13. Publish native model and actual solid with revision-bound readiness for further modeling or DOM-05 export.

OCS native primitives/profile operations/Boolean operations are present in local source. A chosen native body document and a parametric feature-history document have different editing records. OpenSCAD uses CAD-15's mesh branch when that output fits the goal.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets input and native editability needs, then drives supported CAD construction/save. |
| Software and agent | Software performs features and saves; agent reviews source/native capability and geometry exceptions. |
| Software handles ordinary cases | Known native-model families execute with explicit inputs; history, source or shape mismatches enter review. |
| Deterministic supported case | Pinned native construction/save rules and supported parameters produce a checked native document/solid pair. |

**Alternatives.** OCS native document and supported kernel bodies. FreeCAD native constrained/feature document when that editing model is required. Procedural source and generated geometry via DOM-40; create any required native document through an explicit adapter. OpenSCAD source/mesh via CAD-15 as a separately identified output route; layout derivatives have declared approximation criteria.

**Branch selection and merge.** VLM/source review checks feature meaning; software checks native object content, shape and required dimensions. Select a supported native artifact or compose separate parts with lineage; merging history/geometry creates a new revision with explicit mapping. Reopen merged native artifact and independently validate editability, part identities, features and solid classification.

**Proposed development.** native-artifact contract mapper separating native document, parametric source, B-rep and mesh. construction-to-native adapter that preserves source associations and labels actual editability. native-delivery receipt tying solid validity, source record and actual editable content. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Preserve failed native output; return to construction or save adapter and repeat affected checks only. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 11. DOM-05 — Export STEP solid

Entry points and evidence: [Original STEP export operation](../workflows/domain-paths.json), [CadQuery STEP exchange](https://cadquery.readthedocs.io/en/stable/importexport.html), OCS STEP writer (`${OCS_ROOT}/src/io/step.rs`).

1. **DOM-05-A01 — Bind the solid export to representation and consumer criteria.** Freeze the source solid/native revision and required feature manifest; choose exporter, STEP representation/schema, units, frame and consumer. Specify retained geometry and metadata and identify expected information changes.
2. **DOM-05-A02 — Write a separate STEP derivative with actual settings.** Export a separate STEP derivative and record actual output hash, source revision, adapter version/settings and representation/loss map. Preserve the native source. Inspect actual export types and unit declarations.
3. **DOM-05-A03 — Reopen STEP and compare critical geometry.** Reopen the exact output in a named independent consumer; compare interpreted units/frame, actual solids, surfaces, critical holes/interfaces, part boundaries and sourced dimensions. Retain reader dependencies and report readiness for the specified downstream use.

The inspected OCS writer converts triangle meshes into one planar-faced shell/solid representation with six-decimal coordinates; its emitted millimetre entity is detached from the geometric context. A consumer fixture must establish interpreted scale. An analytic-surface requirement selects an evidenced B-rep exporter. CadQuery exchange settings and generated assembly names are recorded per version. Existing STEP bytes are preserved only when they actually occur in the source lineage.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects source-supported export route/criteria and directs independent readback. |
| Software and agent | Software exports and measures; agent reviews actual surface preservation and source-to-output meaning. |
| Software handles ordinary cases | Tested source/exporter/consumer families run automatically; unit, topology and required-field failures enter review. |
| Deterministic supported case | Pinned source, exporter settings and consumer contract produce a reproducible semantic result with actual file hashes. |

**Alternatives.** Analytic/B-rep STEP through a checked capable exporter. Explicitly faceted STEP for a declared layout/display use with its own measured criteria. Native document for editable source/history; mesh exchange uses its own representation and consumer checks.

**Branch selection and merge.** VLM compares source/output feature association; software compares units, surface types and critical geometry. Select a checked complete derivative; any combination of separately exported parts has explicit identity/placement mapping. Reopen the selected/combined artifact and repeat independent semantic and per-feature numerical checks on its exact hash.

**Proposed development.** solid-export capability/criteria planner with source-to-output field mapping. solid export wrapper retaining actual representation and source/output lineage. solid exchange comparator with named-feature, unit and representation checks. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Retain consumer/source artifacts and diagnostics; return to exporter settings or source construction and recheck affected features. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 12. DOM-40 — Script-parametric CAD authoring

Entry points and evidence: [Original script authoring operation](../workflows/domain-paths.json), [CadQuery API](https://cadquery.readthedocs.io/en/stable/classreference.html), [build123d operations](https://build123d.readthedocs.io/en/latest/operations.html), [OpenSCAD](https://openscad.org/documentation).

1. **DOM-40-A01 — Define sourced parameters and the executable model contract.** Map the brief to named parameters, source values, units/frame, required features and target representation. Select a supported backend/environment and explicit permitted parameter domain; preserve component boundaries and dependencies.
2. **DOM-40-A02 — Author readable parametric source with stable feature references.** Author readable source with stable feature references and recorded parameter provenance. Inspect expression units, feature order and selectors against the brief; preserve libraries and asset attribution. Changes to the source receive their own revision.
3. **DOM-40-A03 — Generate geometry in the declared environment.** Evaluate the source in the declared environment through the supported kernel or CAD-15 mesh route. Capture exact inputs, version/build, process results and actual generated artifact types and hashes.
4. **DOM-40-A04 — Validate generated geometry and a supplied parameter variant.** Measure generated and saved features with CAD-13; evaluate only a supplied authorized parameter variant and compare intended changes and unchanged invariants. A changed face selector that produces the wrong feature fails source correspondence even if the shape remains valid.

CadQuery/build123d or FreeCAD source can produce the declared kernel geometry through their supported APIs. OpenSCAD source has the separate mesh handoff. A successful process exit must accompany the required actual geometry and measured features.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | High-reasoning agent derives source-supported parameters/features and authors reviewed source; software generates and measures. |
| Software and agent | Software supplies parameter/dependency checks and geometry construction; agent reviews feature meaning and selector exceptions. |
| Software handles ordinary cases | Checked parametric families use fixed generators; out-of-range conditions, unsupported features and semantic changes enter review. |
| Deterministic supported case | Pinned source/environment/parameters produce actual supported geometry and declared invariant/variant checks. |

**Alternatives.** CadQuery/build123d Python source with actual B-rep output. FreeCAD Python source producing a declared native feature document and shape. OpenSCAD parametric CSG source feeding CAD-15 mesh; this alternative has explicitly changed geometry output. Lower-detail layout family and precision interface family retain separate parameters, purpose and criteria.

**Branch selection and merge.** VLM/source review evaluates geometry intent; software compares actual generated features, topology and parameter responses. Combine compatible source modules only with explicit dependency/feature lineage; new combined source is a new authored revision. Regenerate from merged source and repeat actual shape, source correspondence, selector/variant and saved-output checks with separate reviewer.

**Proposed development.** parametric model-brief skill and contract validator with actual output-type gate. source-authoring skill with parameter provenance, dependency locking and explicit selector checks. reproducible generation adapter with bounded paths, source/configuration identity and resumable receipts. parametric family validator with source-feature mapping and variant dependency checks. Inputs, outputs, source fields, dependencies and action-specific checks are defined under the corresponding IDs in the structured records.

**Failure and resumption.** Preserve failed variant/source and return to the owning expression/selector; invalidate dependent outputs only. The shared protocol in section 13 applies to interrupted calls and changed sources.

## 13. Branch execution, validation and resumption

1. Create isolated branch artifacts with a common source/brief revision, units, frame, component/feature IDs and required-use record. Each branch records its detail/coverage, source subset, individual accuracy criteria, expected output type and local/remote/manual resource observations.
2. Compare source entity/feature mappings and measured differences. Classify disagreement as source interpretation, unit/frame transform, constraint association, construction, representation or export. Retain each candidate and its evidence.
3. A **VLM**, or vision-language model, reads source views and language together. Give it full source views, located annotations, candidate overlays and actual measurement/solver reports. It may select a source-supported whole candidate or compatible contributions within the existing task goals. New design intent and unresolved controlling-source conflicts require the specific user decision.
4. Preserve every selected feature's branch, source and reason. Merge compatible evidence or geometry into a new revision; preserve conflicting values and their alternatives without averaging. Recompute actual topology, constraints where applicable, feature dimensions, part boundaries and saved-output checks.
5. Use a semantic reviewer execution distinct from the producer/merger. Record requested/actual identities and shared model/source dependencies. Numerical checks name the query implementation, actual reference artifact and shared kernel when present. Same-kernel roundtrip and independent-consumer checks remain separate results.
6. On native mutation/export failure, retain the last checked revision, stable request identity, logs, actual partial artifacts and completed-step evidence. Reconcile actual request/document state before retry; resume the first uncompleted action and retain independent completed work.
7. On interrupted reasoning/VLM calls, retain provider/request identity when exposed, exact input/source hashes, settings and raw/partial responses. Reconcile provider completion where supported; otherwise record uncertainty and retry lineage. Validate feature IDs, citations, units and required fields before publishing merged changes. A malformed response retains the last validated artifact.
8. Recheck source digests at resumption. Changed sources invalidate their dependent interpretations, geometry and checks. A required unsupported diagnostic receives an unresolved result, with the affected downstream operation named.

## 14. Resources and development transfer

1. Start with source metadata, entity inventory and required feature checks. Transform cost depends on curve/entity count; intersection tests additionally depend on candidate pairs. Constraint solve cost depends on graph size and relations. Kernel Boolean cost depends on faces and intersection complexity. Mesh rendering/checking depends on tessellation and triangle count. These are qualitative conditions for the proposed path.
2. Record local processor/memory, storage and actual graphics role separately. CPU geometry work and display acceleration retain their own records. Remote inference records include actual provider/model when exposed, call/token count, latency and cost; manual records include selection, diagnosis and correction effort.
3. Ambiguous initial evidence can use higher reasoning effort for source interpretation, feature association and competing construction plans. Explicit checked inputs can use software parsing, transformations, solver calls, kernel construction and numerical readback. Each operation's four modes state the switch condition.
4. The historical OCS timing and Boolean-refusal observations belong to their cited geometry, revision/build and host. This documentation batch supplies no measured resource benchmark.
5. Preserve the agent's action/source/decision trace. Extract repeatable rules into the named proposed helpers, specify supported input classes and expected results, implement only under implementation scope, then run checked representative cases. Migrate the demonstrated action class to software; retain bounded agent review for semantic ambiguity and unsupported cases. Every operation's `software_migration` record supplies its specific fixture gate.

## 15. Future validation cases

The [structured records](point-03-operations.json) contain operation-specific cases and expected outcomes. Fixture values, dimensions and criteria must be supplied with sources before execution.

1. **Vector/constraint cases:** nested DXF blocks, model/paper-space selection, mixed entity coverage, SVG nested viewBox/transforms and explicit physical controls; expected source/entity maps survive. Open/self-crossing loops and ambiguous hole roles stop dependent construction. Contradictory/redundant constraints and intentional free movement have explicit expected solver outcomes. Wrong-but-consistent feature associations fail source comparison. A missing required diagnostic remains unresolved.
2. **Kernel cases:** OCS Region input is rejected by plugin extrusion; open input produces a Surface and blocks a required-solid route; a supported closed/hole sequence preserves the required void. Explicit delete_source and keep_operands flags produce the recorded handle retention/deletion. Revolution axis/sign and Boolean refusals retain source operands and bounded recovery evidence.
3. **Native/export cases:** save/reopen preserves required geometry and actual editing representation. SAT/SAB encoding changes keep separate hashes and measured invariant results. OCS faceted STEP and an evidenced analytic exporter receive distinct expected face types, interpreted units and precision-sensitive coordinate checks. Required holes and interfaces are checked beyond global bounds/volume.
4. **Source/mesh cases:** final CSG output and preview retain separate identities; two supplied tessellation settings receive measured approximation and feature-preservation checks. A source edit or parameter variant invalidates and regenerates descendants. A valid solid with the wrong selected face fails source correspondence. Empty/surface-only output fails a solid requirement.
5. **Interruption/merge cases:** lost remote response, malformed selection rows and changed source on resume preserve raw/request evidence and retry lineage. The last validated merged artifact remains unchanged until valid source-linked rows arrive; changed sources invalidate affected descendants. A lower-detail branch retains layout readiness while a precision-interface check remains blocked.

The [designer evidence notes](reviews/point-03-designer.md) record source summaries, retained original-record findings and documentary checks.
