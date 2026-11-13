# Procedure-design review notes — Point 01 model brief

Date: 12 November 2026. Scope: CAD-01 — Extract a model brief from text and dimensions; DOM-01 — Normalize model brief. Work: local evidence inspection and procedure design.

## 1. Output and identity

1. Created [Point 01 — Descriptions and explicit dimensions to a model brief](../point-01-model-brief.md).
2. Requested dispatch: `gpt-6-astra`, reasoning effort `xhigh`, procedure designer. Actual executing model: unavailable in the exposed runtime identity.
3. The procedure records ten actions; four execution modes; per-feature tolerance, uncertainty and numerical-check requirements; isolated candidate branches; source-based VLM evaluation; selection/merge and post-merge checks; resource observations; failure/resume behavior; development specifications; future tests; migration of checked actions to software.
4. The [implementation plan](../../implementation-plan.md) retains its existing content. All procedure, helper and experiment choices in the new document have proposal status.

## 2. Original local sources read

These are local source inspections on 12 November 2026. Original local sources remain at the linked paths. Referring documents for each source are this review and [Point 01](../point-01-model-brief.md). Existing external links encountered in reports remain existing-report registrations; this role performed local reading.

| Original source and title | Concrete summary | Evidence status and contribution |
| --- | --- | --- |
| [Project agent instructions](../../../AGENTS.md) | Require complete source/idea registration, scoped execution, before/after coordinator commits, disjoint parallel outputs, exact model identity reporting and source-linked engineering values. | Local source inspected; controls scope, evidence and coordination. |
| [CAD workflow records — CAD-01 brief extraction](../../workflows/cad-paths.json) | Accepts text, dimensions or both; produces model-brief; preserves source text/value associations and unresolved choices; requires units, datums, parts and intended output. Uses `assisted` and `proposed_composition` labels. | Local record inspected; intake input alternatives and record-level checks. |
| [Domain workflow records — DOM-01 brief normalization](../../workflows/domain-paths.json) | Requires text plus dimensions or a measurement set; preserves wording, measurements, units/frames/status; normalizes names and units; cites existing OCS skill and a proposed structured schema. | Local record inspected; measurement-input branch and normalization requirements. |
| [Proposed implementation plan](../../implementation-plan.md) | Proposes source intake, geometry adapters, model-brief skill, component records, reproducibility and verification. Declares dimensions and allowed errors as brief inputs. | Local source inspected; existing plan is the development basis and is preserved. |
| OCS engineering skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) | Establishes scope, source views, units, axes, datums, separate parts and motion; requires source-based measured checks, revision awareness, readback and actual model reporting. | Local skill read as source; supplies contract and handoff requirements. |
| OCS model contract and checks (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) | Lists source/correction records, units/frames, parts/connections, selected dimensions/tolerances and measurable invariants. Describes supplied point/axis/plane checks and their evidence interface. | Local reference inspected; tolerance/source duties and later check mapping. |
| OCS numerical contract checker (`${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py`) | Reads caller-supplied observations, evidence labels, one length/angular tolerance pair and supported point/axis/plane checks; computes results and validates basic input conditions. | Source inspected; global tolerance limitation and downstream adapter requirement. |
| [CAD-R01 — Text and explicit dimensions to an editable engineering part](../../workflows/details/cad-r01.md) | Combines brief extraction with actual-model and STEP checks under a simple engineering-part condition. Its datum example is a plate centre at a bottom face with mm and X/Y/Z meanings. | Existing dossier inspected; identifies example-specific frame assumptions to keep scoped to that recipe. |
| [DOM-R01 — Raster plan and site survey to registered IFC](../../workflows/details/dom-r01.md) | Combines brief normalization with plan semantics, survey/photo/depth processing and IFC operations; describes source identities, dimensions, frames and controls for the broader route. | Existing dossier inspected; route context and source-handling requirements. |
| [Workflow representation definitions](../../workflows/representations.json) | Defines model-brief, dimensions, measurement-set, geometry and verification-report artifact meanings. | Local record inspected; brief representation and downstream boundaries. |
| [Detailed workflow README](../../workflows/details/README.md) | Defines ordinal manual/setup/compute ratings as analyst estimates under route-specific conditions; describes evidence and document checks. | Local source inspected; resource observations in point-01 use actual-run measurements separately from these estimates. |
| [Documentation policy](../../documentation-policy.md) | Registers sources, operations, ideas, originals and discussion; assigns before/after commits and aggregate checks to the coordinator. | Local source inspected; source-register and coordinator follow-up requirements. |
| [CAD and skills assessment](../../cad-and-skills.md) | Records existing OCS skill as the baseline and discusses source-intake/CAD alternatives and future skill adaptation from observed usage gaps. | Existing-report reading; reusable skill context. |
| [Software review](software-review.md) | Records source-level Python parsing/hashing/arithmetic primitives, the proposed project intake, OCS checker scope and future helper requirements. | Parallel local-source review read; exact original local library paths and official-document links remain in that record. |
| [Visual interpretation review](visual-review.md) | Specifies source label/endpoint correspondence, original/crop coordinates, branch difference classes, evidence-based selection/merge and per-feature readiness. | Parallel local-source review read; incorporated in action requirements. |
| [Luna official-source lookup](source-check.md) and [source records](../../sources/round-04/intake-sources.json) | Records official JSON/CSV/hashlib/decimal/Tesseract behavior; identifies duplicate-name/default nonfinite JSON handling and Decimal source-string requirements. | Delegated web-inspection result reused; procedure designer read the local report and attributes web inspection to the lookup role. |
| [Action-audit plan](../plan.md) | Defines fifteen action-record duties, alternatives, candidate selection/merge, source-linked per-feature accuracy and migration through checked cases. | Coordinator document inspected; action-specific dependency/resource table added for complete action coverage. |

## 3. Findings requiring coordinator review

1. **Input contract difference:** CAD-01 accepts text alone, dimensions alone or both; DOM-01 requires text plus dimensions or measurement-set. The new point preserves these alternatives and explicitly records intake coverage. Any graph change should retain the meaning of the existing branches and record its decision.
2. **Intake execution evidence:** CAD-01 uses `proposed_composition`; DOM-01 uses `local_source_inspected`; their broad automation labels differ. Those labels describe registered source/proposal state. The new point specifies what an executed intake record must contain before a workflow receives an exercised-capability claim.
3. **Example-specific frame:** CAD-R01 contains a plate-centre/bottom-face/mm/X-length datum example. The generic procedure instead requires each task's sourced unit, datum and frame. Preserve the existing recipe as an example with its stated conditions.
4. **Per-feature tolerance versus checker interface:** the OCS checker uses one global length/angular tolerance pair per input and checks supplied point/axis/plane observations. Point-01 requires a per-feature tolerance source, applicability, measurement uncertainty and numerical rule. Future adapter groups must preserve each feature's rule; unsupported forms need an appropriate implementation.
5. **Local source-register coverage:** register the source inspections and new procedure/alternative ideas in the coordinator-owned source/idea registers, including model-contract.md (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) and check_contract.py (`${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py`) if their present entries do not cover this use.
6. **New proposal records:** register the four execution modes, isolated candidate branches, source-based VLM evaluation, row-level merge/post-merge checks, measured resource comparison and tested migration to software. Their status is proposal; the standing explicit `MARK AS ACCEPTED` rule controls acceptance.
7. **Software source support:** the procedure now links the official JSON/CSV/hashlib/decimal documentation inspected by Luna and records its version separately from the local Python 3.14 source reviewed by the software role. The proposal includes strict duplicate-name/nonfinite JSON handling, source-string Decimal conversion and CSV dialect preservation. A future run records its actual runtime/version and exercises the listed cases.
8. **Action scope:** later geometry/OCS checks appear as handoff requirements and future test specifications. Current output consists of the two assigned Markdown files.

## 4. Integration with parallel review

1. The software reviewer independently identified the proposed intake status and the OCS checker's global tolerance interface. The procedure incorporates those findings as explicit action and adapter requirements.
2. The visual reviewer recommended separate source interpretation, evidence merge and later model readback; common branch revisions/frames; cited image regions; preserved conflict records; and source-defined generic frames. The procedure incorporates these distinctions in Actions 03, 05 and 07–10.
3. Coordinator checks should confirm that the final source/idea register entries, operation links, review findings and point-01 terminology agree after all assigned contributions arrive.
4. The independent reviewer was notified when the complete draft existed. Focused additions incorporate source-loss parser cases, signed-offset preservation, explicit evidence-supported VLM selection and direct processing of already supplied user requirements.
5. Independent-review additions specify branch-specific use, coverage/detail, accuracy, source subset and resource records; a source reviewer separate from the producing/merging interpretation; and request/response reconciliation, partial-write recovery and source-digest rechecks during resumption.

## 5. Executed document checks

1. **PASS — local link targets:** every absolute local Markdown target in the two assigned files existed when checked.
2. **PASS — action sequence:** the procedure contains Actions 01–10 in order. Each action includes explicit goal/inputs, software work, reasoning work, user decision, output, resumption and source basis. The adjacent action-specific table supplies intended use, accuracy/evidence, dependencies/development and resource responsibilities.
3. **PASS — whitespace:** neither assigned document contains trailing whitespace.
4. These checks read the two Markdown documents and local path metadata. The described intake procedure, helper components and engineering test cases retain proposal status.
