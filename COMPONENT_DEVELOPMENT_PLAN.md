# Component-led CAD and tooling development plan

Date: 12 November 2026. Status: **proposal**. Planning/documentation model: **gpt-6.1-sol**. Starting checkpoint: `b663715`.

## 1. Objective and existing work

1. Produce the actual ferme component CAD models one at a time. Each component iteration also applies and verifies an improvement to the current skill instructions, documented procedure or Python helpers/scripts.
2. Use the 103-part input index (`${FERME_ROOT}/engineering/module-development/cad-inputs/README.md`), part manifest (`${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json`), geometric dependency list (`${FERME_ROOT}/engineering/module-development/cad-inputs/dependency-order.tsv`) and existing model/check index (`${FERME_ROOT}/engineering/module-development/cad/README.md`) as the component work sources.
3. Reuse ferme's construction skill (`${FERME_ROOT}/skills/cad-construction/SKILL.md`), OCS improvements (`${FERME_ROOT}/skills/ocs-skill-improvements.md`), success/failure findings (`${FERME_ROOT}/skills/cad-workflow-findings.md`), the installed OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) and [inspected implementation assets](research/action-audit/implementation-queue/assets.md).
4. The [existing action graph and route map](research/action-audit/workflow-to-actions.md) and [245-action implementation queue](research/action-audit/implementation-queue/queue.json) supply action boundaries, inputs, outputs, software/agent roles, source evidence and proposed integrations. Component requirements determine which eligible action receives implementation work next. Preserve the original graph, queue, rankings and [implementation plan](research/implementation-plan.md).
5. This document consolidates the discussion into an execution proposal. The current batch writes the plan, component coverage reference, idea/source registrations and document checks. Actual CAD, code and catalogue execution follows the individual work packages below.

## 2. Three linked records and required file locations

1. **Component work record:** one job per distinct component/geometry revision, with input sheet, intended use, required features, source values, representation, dependencies, native file, measured results, views and iteration state. CAD model destination required by the user: `${FERME_ROOT}/engineering/module-development/cad/parts/`. Component-specific checks and per-iteration work records belong beside the existing ferme CAD checks.
2. **Action registry:** reusable action definitions and individual occurrences. Reusable action definitions, procedures and tooling-improvement records belong to this project. Component-specific action occurrences and raw build evidence belong to ferme beside their component records, with links back to the reusable action and exact skill/script revision. An action can recur across components without merging the different action definitions in the graph.
3. **Parts catalogue:** permanent part identities, readable/formal names, descriptions, manufacturer/supplier/project codes, standards and file/source/physical-location relationships. The parts index, catalogue records and eventual database belong to the FERME project. This project supplies reusable Python interfaces, skills and documentation for consuming those records when they exist; the data path is an explicit input. Purchased components, custom part definitions, stock specifications, cut pieces and assembly occurrences retain explicit relationships.
4. Ferme retains project geometry, source evidence and component-specific parameters. This project retains reusable skill/procedure changes, Python helpers, tests, action definitions and instructions for reading the ferme index/catalogue/database. FERME owns the parts data and component-specific execution records. Both records link to exact artifact and tool revisions.
5. The user requires the main plan in the 3dmodeling project folder, CAD models and the parts catalogue/database in ferme, and reusable scripts/skills plus catalogue-use instructions here. This main document is `${MODELING_ROOT}/COMPONENT_DEVELOPMENT_PLAN.md`. Proposed interface filenames are implementation design choices in this plan. Existing documents remain the source of their current facts; proposed new fields/files retain proposal status until implemented.

## 3. Work package 1 — Establish the minimum records

1. Read the ferme manifest into a component work index preserving all 103 identities, names, input-sheet links, dependencies, routes and existing CAD references. Record existing models as reuse candidates and inspect them for the particular job before assigning a construction task.
2. Use the [component coverage reference](research/component-development-coverage.md) to keep every listed part visible. It preserves input-manifest order; actual build order follows satisfied geometric inputs, selected route, source readiness and construction effort.
3. Keep the reusable action-definition index here referencing the existing graph, and append component action-occurrence records in ferme. Start with the actions actually used by the first component. A new observed action gets a readable name, input/output description and relationship to existing actions before adding a graph extension proposal.
4. Use the existing FERME `parts.json` and input-sheet index immediately. The proposed richer catalogue, when implemented in FERME, uses linked CSV records plus a Markdown view, the recommended alternative in the [catalogue proposal](research/action-audit/parts-catalogue-proposal.md). Proposed data files under a ferme catalogue directory: `parts.csv`, `part-aliases.csv`, `part-files.csv` and `part-standards.csv`. Its directory is selected within ferme when implemented. Reusable readers/search/validation scripts and usage documentation belong here. Preserve the other registered storage alternatives as proposals.
5. Populate catalogue identities from the existing manifest, with manufacturer/formal/standard details attributed to the existing sources when available. A catalogue ID and a project reference have separate fields. Seed data retains proposal/source status and exact variant distinctions.
6. Use manual structured text/CSV entry and existing source-record methods for the first job. Introduce Python validation/search helpers when required by concrete record handling. Proposed first checks: unique IDs, valid references, existing artifact paths and explicit evidence labels.
7. Completion: the first component has a work record and an identity in the existing FERME index, its required actions reference the existing graph, and every record resolves to its source. Map that project identity to a catalogue identity when the richer catalogue exists. The remaining component entries remain in the work index with their existing dependencies.

## 4. Work package 2 — First component: Main frame longitudinal rail (P01)

1. Read the rail input sheet (`${FERME_ROOT}/engineering/module-development/cad-inputs/p01-main-frame-longitudinal-rail.md`), its linked fabrication/frame sources and any existing geometry. The sheet specifies **proposed** 40 × 40 × 3 mm square steel tube, 600 mm cut length, quantity two. Preserve that proposal attribution and the source's actual stock/shape details.
2. Define this iteration's exact required geometry: hollow tube section, sourced wall and cut length, end faces, orientation and referenced connection features. Carry section corner geometry and connection details from their actual source or explicit task decision. Record the rail's local datums and its eventual assembly transform separately.
3. Write the bounded construction/check steps using the existing native extrusion, cavity/Boolean, metadata and save/readback procedures where applicable. Map each step to its own named action in the graph.
4. Bind the actual OCS build/session/document and current revisions using the installed control procedure. Run one CAD writer for that document. Perform bounded operations with stable request IDs and read back their actual effects.
5. Check section dimensions, wall thickness, cut length, hollow topology, end orientation and each required source-defined feature. Record method, units, reference frame, numerical criterion, source evidence and observed result for each check. Save/reopen and verify the required persisted geometry and valid model-derived views.
6. Record successful steps, failures, recovery and actual repeated actions. Apply the first evidence-supported improvement to the current skill/procedure or Python helper. Examples are a source-labelled hollow-section procedure or a configured existing extrusion/check wrapper; choose the actual change from this build's observations.
7. Update the catalogue artifact/check links and component record. Verify the improvement and close the iteration with component and tool result commits. The two identical rail instances reference the same distinct part definition.

## 5. Work package 3 — Second component: Main frame crossmember (P02)

1. Read the crossmember input sheet (`${FERME_ROOT}/engineering/module-development/cad-inputs/p02-main-frame-crossmember.md`) and rail results. The sheet specifies **proposed** 40 × 40 × 3 mm tube, 260 mm cut length, quantity three, with the rail as a geometry dependency.
2. Reuse the rail's section-construction procedure and supported functions with the crossmember's own parameters and local datums. Retain part-specific source and placement records.
3. Compare the two action histories. Identify actual repeated operations, their common inputs and the differing length/datum/output fields. Check that the procedure applies to both cases.
4. If the repeat has explicit rules and no suitable existing function, extract a parameterised Python function. If a suitable function exists, extend/configure it and test the specific change. Preserve dimensions and source ownership as parameters; discover session/document state at execution time.
5. Check the crossmember geometry, saved-file persistence and rail-interface observations required by its sheet. Assembly position and joining features follow the particular assembly evidence.
6. Apply and verify a further skill/script improvement based on this iteration. Test affected shared code against both rail and crossmember cases. Update the action registry and catalogue, then commit the iteration results.

## 6. Standard procedure for every later component

1. **Choose the job:** identify component, exact variant/route, required output, prior model and the geometric inputs that are ready. A source conflict affects the particular dependent feature; retain independent work and name the specific question requiring a task decision.
2. **Freeze the sources:** retain originals and exact locators, hashes, revisions, source classifications and corrections. Separate manufacturer/seller values, measured values, drawing/photo reconstructions and proposed design inputs.
3. **Define required features:** record component boundaries, representation/detail, functional interfaces, datums, units, frames and feature-specific dimensional/positional/angular criteria. Identify the source/decision for each criterion.
4. **Plan only this job's steps:** use the existing graph to select interpretation, import, profile, construction, measurement, save and recovery actions. State each action's actual inputs, outputs, software/agent owner and downstream conditions. Reuse prior records and functions.
5. **Construct in bounded groups:** execute one dependent feature group at a time, retain requests/results, refresh handles/revisions and checkpoint actual geometry. Keep separately manufactured parts and repeated instances identifiable.
6. **Reconcile failures:** query the original request identity after uncertain completion; distinguish entity effects and interactive command state. Preserve partial effects and the failed attempt before applying a bounded recovery.
7. **Check the geometry:** compare observed source-linked features, topology, units and transformed interface coordinates. Record actual checks against the exact model revision, with independent expectations derived from the sources.
8. **Check persistence and views:** save the specified native artifact; inspect audit/data-loss results; reopen and repeat supported required feature checks. Verify capture contents against the intended document and geometry. Pre-save, reopened, mesh-estimate and visual results have separate observations.
9. **Apply an improvement:** make a concrete skill/procedure/script change justified by the observed work. Verify that change and affected earlier cases. Log additional future ideas separately.
10. **Publish iteration records:** connect component, part revision, action occurrences, source evidence, improvement revision and checks. Commit the bounded changes and select the next eligible part.

## 7. Action registry and repetition detection

1. Proposed reusable definition record, held here: readable action name plus existing graph reference, purpose, prerequisites, supported input classes, output, compatible next actions and handoff conditions. The definition identifies the current procedure/function and its version.
2. Proposed component occurrence record, held in ferme: component job/part revision, action reference, input/source revisions, intended and actual output, geometry representation, units/frames, software/function/request identity, agent role/model where exposed, preserved/changed/inferred information, alternatives, result, failure/recovery and evidence locations.
3. Record validation method, expected/observed values, numerical criterion and its source, actual model/document/geometry revision and downstream readiness. Include local elapsed time/memory method where measured, remote model usage separately and manual interventions.
4. Match repetition by action purpose, supported input/output contract and conditions. Several parts using extrusion can share its construction function while retaining different profile interpretation and feature-check actions.
5. Track occurrence counts and links, supported variants, exceptions, active procedure version, code coverage and candidate additions. A repeated command is evidence for investigating reuse; its semantic inputs and effects determine the reusable action.
6. Implement record/reference checking and readable summaries in Python as those operations are needed. Keep result classification as proposal, source claim, observed failure, executed success or other actual evidence status.

## 8. Mandatory improvement and software extraction rule

1. Every CAD design iteration delivers an applied and verified improvement to the current skills/procedures or scripts. A registered future task or confirmation of existing behavior supplies evidence supporting that improvement.
2. First write the actual successful step-by-step procedure: inputs, supported conditions, numbered commands/decisions, output, verification and recovery. Link the component cases that established it.
3. On a repeated action, compare source/geometry conditions and record variations. For explicit repeatable rules, reuse an existing function or extract the common part into Python with explicit parameters and returned identities/results.
4. Retain source interpretation with a reasoning agent where input meaning requires it. A function can produce geometry or measurements while an agent decides between evidence-supported alternatives; each keeps its own action and result.
5. Add cases covering the observed success, actual failure/recovery, supported variation and rejected/unsupported inputs. Compare the resulting source-linked geometric properties with the independently stated expectations.
6. Promote only the tested input subset to software execution. Route its exceptions to the named interpretation/recovery action. State supported conditions beside the function and skill instructions.
7. Parameterise output/source paths, sessions, document bindings and request namespaces. Reuse the inspected one-send/revision checks and fix observed polling/state/reader integration issues within the affected action. Store the reusable code and required dependencies durably in this project.
8. Tests support the improvement's verification; the iteration includes the actual skill/procedure/script change they exercise.

## 9. Reasoning, software options and evidence merges

1. A high-reasoning agent interprets unfamiliar descriptions, dimension associations, component boundaries or alternative constructions. A **vision-language model** reads source images/drawings together with text and compares them with actual model views when needed.
2. Software performs explicit parsing, unit/frame calculations, known geometry operations and numerical checks for its supported inputs. Hybrid execution keeps agent review at the particular decisions requiring evidence interpretation.
3. Each action can retain agent-led, software-plus-agent, software-first with exceptions and deterministic supported-input options. Record their actual supported conditions and results as they are exercised.
4. Parallel candidate interpretations, import/reconstruction alternatives and differing detail levels can contribute to a job. Each branch keeps source revision, intended use, accuracy/detail, outputs and its own observations. Parallel execution follows the current job's scope; one writer owns a target CAD document.
5. Selection/merge is an explicit graph action: the reasoning/vision agent compares evidence and explains compatible contributions or competing interpretations. Software checks units, transforms, identity and dimensional conflicts. Validate the combined artifact again and retain per-feature provenance.
6. Per-feature requirements reflect the job: sketch/layout, architecture, mechanical fit, robot motion or manufacturing. Measurement uncertainty, engineering allowance, numerical solver/check thresholds and representation approximation remain separately attributed values.
7. For bounded specialist contributions, the existing role plan names Astra/xhigh for procedure reasoning, Terra/xhigh for software, Sol/xhigh for visual review, Luna/high for approved external research, and separate Sol/xhigh for independent review. These are requested dispatch choices; actual executing identities are recorded when exposed. Role use scales to the job's concrete questions and current delegation scope.

## 10. FERME parts catalogue and reusable search interface here

1. The authoritative catalogue/index/database data belongs to FERME. Proposed core fields: stable catalogue ID, readable name, formal industry name where evidenced, description, manufacturer, manufacturer part number, variant/revision, source reference and evidence status.
2. Aliases retain project IDs and supplier codes. File records retain native model/source/check locations, representation, revision and hashes. Physical storage location and installed assembly occurrence have separate relationships.
3. Standards records retain designation, name/title, edition, applicable feature/component and evidence. Manufacturer conformity statements retain their attribution. The user named ISO, IEC, ANSI and EU/European references in the catalogue discussion; populate actual designations from their cited sources.
4. Seed identity candidates from the existing ferme manifest, check duplicates/variants and enrich records during each component iteration. Link a part to its component jobs, action history and tool versions.
5. The reusable Python search interface lives here and receives the FERME catalogue path/configuration explicitly. Initial search uses exact fields, aliases and case-insensitive text over names/descriptions/codes/standards. Proposed Python helper behavior: readable matches with stable identity, variant, source and CAD links; filtering and result ordering are explicit and tested.
6. Catalogue checks cover ID uniqueness, valid relationship targets, standards attribution, source/artifact existence and revision consistency. Keep physical/specification facts distinct from discussion proposals.

## 11. Work order after the first pair

1. Evaluate eligible parts against the original geometric dependency list and actual incoming interfaces. Among eligible jobs, prioritise lower local processing, available source evidence, fewer unresolved construction decisions and repeated actions useful to upcoming parts. Record the selection reason.
2. Begin with explicit sections/lengths and other dimensioned profiles where their inputs are ready. Progress into holes/patterns, turned features, plates/brackets and interface placement as required by the selected component sheets. Compare actual complexity per job rather than assigning a whole component family an unconditional rank.
3. Inspect the purchased drive, rim and bearing interfaces before forming their motor plates, supported shafts, carriers, brake mounts and route-specific adapters.
4. Inspect caster head, pins and retainers before forming the matching arm, cheeks, spacers, mounting plate and doublers.
5. Reuse/inspect battery cases and terminal/restraint geometry before their individual rails, cassettes, trays, shelves, covers and hold-downs.
6. Inspect hitch/attachment pin interfaces before supports and gussets; inspect electrical cases and connector/gland cutouts before their panels, brackets and thermal mounts.
7. Use actual interfaces to complete frame support details, deck/access panels and guards. Preserve distinct part definitions for route/side geometries and instances for identical repeated parts.
8. The component source-coverage reference links to the authoritative FERME manifest containing all 103 inputs. Alternative routes stay distinguishable; a manifest dependency collecting alternatives is resolved to the actual branch for a particular assembly rather than summing alternative quantities.
9. Photogrammetry, learned geometry and trained visual scenes enter the active work only when a component requires those inputs and the corresponding action is selected. Their documented methods/resources remain in the original graph and queue.

## 12. Per-iteration completion and verification

1. Native CAD contains the component's required physical features and actual representation. Source values, reconstructed features and proposal values retain their evidence labels.
2. Required geometry/interface checks have actual observations; saved-file and view checks identify the same artifact. Concrete failures retain their affected features and recovery state.
3. The action registry records the used actions, results, alternatives, repetition and downstream conditions.
4. The FERME part index, and the richer catalogue when present, has the correct identity/variant and links to source, model, checks and project references.
5. A skill/procedure/script improvement has been applied and verified against the current case and affected earlier cases. Its supported conditions, failure handling and exact version are recorded.
6. Component-specific and reusable-code dependencies, parameters and reproduction instructions are retained with the job. A replay result is attributed to the run that produced it.
7. Checkpoint/result commits preserve the bounded work in each affected repository. Cross-repository records retain the corresponding commit references. Preserve unrelated work, originals and unsaved CAD documents.

## 13. Explicit future work

1. Add catalogue material and resistance properties, with units, source and applicability/conditions when that extension is defined. Existing values required to construct a component retain their current source records.
2. Add classification by kind of work, including wood, metal, architecture, mechanical and industrial; define how multi-domain items are represented.
3. Consider SQLite/DuckDB storage in FERME and separately specified vector similarity search, with reusable access code and usage instructions here, after text-based identity/relationship/search requirements have been exercised.
4. Extend automation and additional reconstruction methods from observed component needs and recorded action cases. These future extensions retain their idea-register status.

## 14. Proposed first execution batch

1. Establish the minimum work/action/catalogue records and bind the rail's source and task revisions.
2. Produce the rail model and required checks using the current OCS skill/helpers, recording individual actions.
3. Apply and verify the first concrete skill/procedure/Python improvement, update catalogue references and commit the rail iteration.
4. Proceed to the crossmember using that procedure; test the repeated action at its 260 mm proposed length, apply the next improvement and commit its iteration.
5. Use those actual results to select and prepare the next dependency-ready component from the coverage list. New helper implementation is tied to the observed job/action need.

## 15. Registration and execution state of this document

1. Requested work: a complete plan consolidating the discussions, components, CAD iterations, improvements and catalogue/future-work boundaries. The standing instruction registers those ideas and sources with before/after commits.
2. This batch reads existing local sources, writes the plan and component source-coverage reference, registers new proposal relationships and validates document/source consistency. CAD builds, new helpers and catalogue data execution remain the proposed work packages described above.
3. Planning decisions are proposals; existing part-sheet proposal notices and the project's explicit acceptance rules remain attached to their records.
4. [Source snapshots](research/sources/round-08/component-plan-sources.json) identify original local files, summaries, dates, evidence statuses and hashes. [Plan checks](research/component-plan-checks.json) record actual coverage, dependency, preservation, link and rebuild results.

5. Coverage-generation history: the first temporary writer interpreted an existing `parts/skf-sy20tf.dwg` reference against the project/input roots and failed its path check before writing the coverage file. Existing CAD references are relative to the ferme CAD directory. The writer now uses that source-specific base; original manifest values are preserved, and the check receipt retains the failure/rerun history.

6. Latest ownership instructions: the CAD models, parts index and eventual parts database belong to FERME. This project improves reusable scripts/skills and documents how they consume the FERME data when it exists. Those instructions refine the earlier catalogue-location proposal; the earlier discussion record is retained as its historical proposal.
