# Point 02 — Procedure designer notes

Current execution package: [OCS engineering (`cad-ocs-engineering`)](../../../skills/cad-ocs-engineering/SKILL.md). External OCS skill locators below identify the original inspected sources.

Date: 12 November 2026. Scope: CAD-12 — assemble existing components; DOM-06 — library intake; DOM-07 — occurrence placement; DOM-26 — component revisions; DOM-38 — STEP import; DOM-39 — STEP assembly export.

## 1. Deliverables and identity

1. [Readable procedures](../point-02-component-reuse.md).
2. [Structured action specification](../point-02-operations.json): six operations, four concrete actions per operation, all fifteen required fields per action; four execution modes; alternatives; candidate evaluation/merge; migration and future test cases.
3. Requested dispatch: `gpt-6-astra`, reasoning effort `xhigh`. Actual runtime model identity: unavailable.
4. Procedure and helper status: proposal. Executed work: local source reading, review synthesis and the three assigned documentation files. Original operation records, dossiers and implementation plan retain their content.

## 2. Local sources read and contribution

All local observations below were made on 12 November 2026. Referring documents are this note and both point-02 deliverables. Original paths remain their existing source locations.

| Source | Concrete summary and use | Evidence status |
| --- | --- | --- |
| [AGENTS.md](../../../AGENTS.md) and [audit plan](../plan.md) | Establish scope, fifteen action duties, source-linked evidence, alternatives, reviewed merging and software migration through checked cases. | Local instructions/planning records inspected. |
| [CAD operation records](../../workflows/cad-paths.json) | CAD-12 requires a named base plus distinct additional source input, source identity/terms, units/frames, interface checks and occurrence preservation. | Original operation proposal inspected. |
| [Domain operation records](../../workflows/domain-paths.json) | DOM-06/07/26/38/39 describe rights intake, target-assembly placement, version pins and STEP interchange. DOM-07 requires its assembly-graph input alternative. | Original records inspected; source capability and proposal labels retained as historical evidence. |
| [Component assessment](../../domains-and-components.md) | Separates original assets, component definitions, assembly occurrences and derived representations; records libraries, item terms, immutable revisions, frame/geometry and downstream checks. | Existing report inspected; external claims retain their registered status. |
| [Composition rules](../../workflows/composition-rules.md) | Defines source/target roles, evidence merge, geometry assembly, whole-component substitution, representation forks, units/frames and pinned revision handoffs. | Local proposal inspected. |
| [Implementation plan](../../implementation-plan.md) | Supplies component-library, geometry-adapter and verification development basis, with measured feature criteria and source/derivative ownership. | Existing proposal reused from point-01 inspection and preserved. |
| [CAD-R08 — Known library parts to placed assembly](../../workflows/details/cad-r08.md) | Records library identity, native/STEP import, interface placement, clearance and save checks; source citation for its FreeCAD entrypoint points to OCS API-SPEC. | Existing dossier inspected; citation mismatch recorded for coordinator review. |
| [DOM-R02 — Manufacturer STEP component to robot link](../../workflows/details/dom-r02.md) | Records supplier identity/terms, STEP units/product structure, measured mounting datums and later domain semantics. Its component registry is described as proposed and also labeled an existing entrypoint. | Existing dossier inspected; registry-status mismatch recorded. |
| [Local baseline](../../local-baseline.md) | Records historical tool/source observations and the mesh-derived OCS STEP finding. Historical runtime/version values remain dated observations. | Local report inspected. |
| OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) | Require explicit source/part/frame contracts, revision-bound edits, actual measured checks and same-revision views; numerical helper accepts supplied point/axis/plane data with global tolerances. | Local skill/reference reused from direct point-01 reading. |
| OCS automation guide (`${OCS_ROOT}/docs/automation/README.md`), API-SPEC (`${OCS_ROOT}/docs/automation/API-SPEC.md`) and control notes (`${CODEX_HOME}/skills/ocs-engineering/references/ocs-control.md`) | Describe revision/request handling, sequential batches, block definition/Insert creation and groups. Control notes record constrained mechanical assembly and general solid-clearance query as unestablished by the earlier inspection. | Local source text inspected; actual operation execution belongs to future runs. |
| OCS STEP writer (`${OCS_ROOT}/src/io/step.rs`) | Writer body gathers triangles, emits one shell/solid/representation and planar faces, and emits a millimetre unit entity outside the referenced geometric context. Software review additionally records six-decimal formatting and skipped invalid indices. | Local source body inspected; comments and body differ. Runtime validity and consumer units require a fixture. |
| [Point-02 software review](point-02-software.md) | Documents actual source/API distinctions, proposed adapter/helper responsibilities, recovery and source citation/status findings. | Parallel local-source review read and incorporated. |
| [Point-02 visual review](point-02-visual.md) | Defines definition/occurrence identity, critical-interface checks, goal/detail alternatives, source-supported selection, authored-hybrid boundary and post-merge validation. | Parallel local-source review read and incorporated. |
| [Point-02 Luna source review](point-02-sources.md) and [registered web sources](../../sources/round-05/point-02-web-sources.json) | Records six inspected primary pages covering archived FreeCAD assembly/preferences, OCCT 8.0.1 reader/writer APIs and asset-level KiCad/Menagerie terms. | Delegated web-inspection evidence reused from local report; procedure designer performed local reading. |

## 3. Original source links used through delegated evidence

1. [FreeCAD Assembly Workbench](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Assembly_Workbench.md): assemblies, component links and joint choices. Luna records the documentation repository as archived on 1 April 2026.
2. [FreeCAD import/export preferences](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md): import document/product organization, instance naming, STEP export units and AP203/AP214 choices. A future adapter records the selected runtime and actual settings.
3. [OCCT STEPCAFControl_Reader](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___reader.html): documented assembly-shape, name/color and root-transfer operations into a DECAF document. Luna's source record preserves the original URL and its redirect to OCCT 8.0.1 documentation.
4. [OCCT STEPCAFControl_Writer](https://dev.opencascade.org/doc/refman/html/class_s_t_e_p_c_a_f_control___writer.html): document/label/root-assembly transfer, configurable names/colors and root-label length-unit/Cascade fallback.
5. [KiCad library terms](https://www.kicad.org/libraries/license/): collection licence and design-use exception; preserve applicable file attribution and terms.
6. [MuJoCo Menagerie model catalogue](https://github.com/google-deepmind/mujoco_menagerie/blob/main/README.md): model-directory LICENSE applies to its XML/assets, with top-level terms for other repository content.
7. [CadQuery import/export](https://cadquery.readthedocs.io/en/stable/importexport.html), [Poly Haven licence](https://polyhaven.com/license) and [CONTEC item terms](https://www.contec.com/en/download/contract/contract3/?downloaditemid=b1063f2d-146f-4ca4-b8d2-b54c4388c265&itemid=f9a4d3e0-9ca3-4466-9b3d-cffac9355280): existing registered capability/terms evidence reused through the component and workflow reports; this role performed no fresh inspection of these pages.

## 4. Design and review integration

1. Every operation has agent-led, hybrid, software-first and deterministic options. The input family and checked cases determine a future route; actual model identity and requested configuration are separate observations.
2. Metadata/identity work precedes required geometry queries. Local CPU/memory/storage, optional graphics work, remote inference and manual review have separate recording duties with explicit scaling conditions.
3. A labelled envelope or display derivative serves a declared layout use; a precision/interface use carries source-backed features, frames and criteria. Original domain identities, including supplied IFC/MJCF references, remain available for later domain operations.
4. CAD-12 orchestrates a component assembly. DOM-07 places one occurrence with a required target assembly revision/graph. A combined route consumes the placement receipt once.
5. Evidence enrichment, whole-component substitution and authored cross-part geometry combinations have explicit meanings. The procedure selects source-supported candidates; new authored hybrids retain their own identity and scope.
6. Numerical feature/placement checks and a reviewer separate from the producing/merging interpretation validate the resulting revision. Repeated product instances require parent/occurrence mappings and local/world transforms in addition to counts and shape hashes.
7. **P02-IR01 applied:** DOM-07 includes a future case with absent, stale or wrong target-assembly revision/graph; expected result is blocked placement before mutation.
8. **P02-IR02 applied:** the structured specification and readable document contain a shared remote reasoning/VLM interruption protocol retaining request/input/response identities, frozen source hashes, malformed/partial results and the validated publication boundary. CAD mutation reconciliation retains its own native protocol.

9. **P02-IR03 applied:** DOM-06 identity/rights receipt feeds STEP import before component-record completion; checked DOM-38 representation evidence returns to DOM-06, and DOM-26 publishes after required intake references exist. Partial intake retains draft/action-readiness status.
10. **P02-IR02 test applied:** a shared future case covers lost remote response, malformed selection rows and a changed source on resume, with raw evidence retention, retry lineage, validated publication and affected-only invalidation.

## 5. Findings for coordinator integration

1. Register both deliverables, this note, the three role reviews and their source/idea relationships. All procedure/helper/migration choices retain proposal status.
2. Preserve the CAD-R08 FreeCAD-to-OCS source citation mismatch and DOM-R02 proposed-registry/existing-entrypoint mismatch as findings for the owning records.
3. Preserve DOM-07's target-assembly prerequisite when updating the workflow inventory. The new action inputs and failure fixture explicitly require it.
4. The OCS STEP body provides the faceted/flattened/orphan-unit finding; an API or comment label alone supplies no executed compatibility result. The proposed OCCT adapter has separate source/version and future fixture evidence.
5. Source changes, source-frame changes and rights changes produce new metadata/revision evidence even when geometry hashes match. Earlier assembly pins and check reports retain their original revision association.

## 6. Executed document checks

1. **PASS — structured coverage:** JSON parses; exactly the six assigned operations are present; all 24 action IDs are unique; every action contains all fifteen nonempty required fields.
2. **PASS — operation alternatives:** every operation contains all four required execution-mode keys, source URLs, alternatives, merge, migration and future tests.
3. **PASS — cross-references:** the readable procedure contains all 24 action identifiers; local source paths and Markdown link targets existed at check time.
4. **PASS — formatting:** the three assigned files have one final newline, no extra EOF blank line and no trailing whitespace.
5. These checks inspect documentation structure, references and formatting. The future engineering and runtime test cases retain their proposal status.
