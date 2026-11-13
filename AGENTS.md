# Instructions for agents working in ferme

## 3D modeling research, documentation and Git

Standing project instructions from the user on 12 November 2026:

> From now on ALL things all ideas all sources all is REGISTERED WRITTEN DOWN AND DOCUMENTED with real original links and summaries. apply if not done yet, always commit before and after changes

1. Record every project idea, source, finding, workflow, alternative and combination in the repository. Include the readable subject, a concrete summary, original source links, evidence status and relationships to existing work. Apply this to the existing research as well as new findings.
2. This instruction authorizes the project documentation required to register research and discussion. Keep implementation, installation, conversion, simulation, publication and purchases within their separately authorized scope.
3. Keep a source register under `research/sources/`. Every source record needs its original URL or existing local source path, title, summary, observation or registration date, evidence status and referring documents. Preserve exact supplied URLs alongside any canonical source discovered later.
4. Link each workflow operation to its supporting sources. Record inputs, outputs, prerequisites, tool/API, geometry representation, units/frames, metric evidence, preserved/changed information, checks, alternatives and compatible downstream operations. Record proposed combinations explicitly with their handoff conditions.
5. Preserve downloaded originals unchanged with URL, retrieval date, content type, local path and SHA-256. Label web inspection, existing-report registration, downloaded original, source claim, user report, proposal and executed result according to actual evidence.
6. Record ideas and decisions separately. Add alternatives and open research questions to the idea register; mark an item accepted only after the user's explicit `MARK AS ACCEPTED` instruction.
7. Always create a checkpoint commit before an authorized logical change batch and a result commit afterward. If the worktree is clean, an empty checkpoint commit can mark the start. Inspect the worktree and stage only the authorized project files. Preserve unrelated changes. This user instruction authorizes local staging and commits for those batches; pushes remain separately scoped.
8. Parallel research agents contribute to the same documented batch. Give each agent disjoint output paths and require sources and summaries. The coordinating agent owns the before/after commits and final source/graph consistency checks. Existing Luna delegation and external-research rules apply.
9. Preserve the current implementation plan while extending research. Register new workflow possibilities as proposals, with source-backed transitions and explicit experiment questions. Keep source capability claims separate from locally exercised capability.

## Communication with the author

Exact vocabulary, explicit context and unambiguous engineering communication are functional requirements. Apply these rules in the response itself.

1. Answer the question actually asked. State the requested specification, result, price, explanation or link directly. Do not substitute another question, a general lesson or an explanation of something the author already knows.
2. Use simplified technical English, literal wording and stable terminology. Use one term for one concept. Define a technical term when its meaning is needed to understand the answer; do not substitute definitions of individual words for an explanation of the complete engineering statement.
3. Name the component, action, scope and result explicitly. Avoid vague references and verbs such as “manage”, “handle”, “fix” or “continue” without naming their object and the action.
4. Present facts and specifications directly. Avoid definitions and explanations framed as “this is X, not Y”, “not X but Y”, “this is not about…” or equivalent unsolicited contrasts.
5. Omit filler and narrative framing: “why it matters”, “what you want”, “one important point”, “that distinction matters”, “bottom line”, and equivalent formulas. Do not paraphrase the author's request as a preamble.
6. Do not append unsolicited lectures, warnings, procedural commentary, approval reminders, descriptions of inactivity, retrospective explanations, recaps or closing offers. Include a limitation only when it changes the meaning of the requested fact or is necessary for the requested engineering work.
7. When asked what research found, lead with the actual findings: named parts, specifications, prices and direct links. Do not replace the findings with a list of missing information, unqualified candidates or work not performed.
8. When asked for specifications, give the specifications with labels and units. When asked for links, give the links. When asked for one value, answer that value. A report link alone does not replace the requested answer.
9. Use explicit labels and numbered lists for multiple facts, parameters and calculations. Use a table when the author requests one. Do not silently replace a requested format.
10. A question receives its answer and control returns to the author. Reading existing project files and source documents to identify the answer is allowed. A question alone does not authorize new research, calculations, simulations, file changes or the next project phase.
11. A communication instruction receives a response about communication only. Do not repeat technical parameters, calculations or design proposals in that response. Apply the correction immediately rather than substituting a promise for the requested answer or action.
12. Distinguish observed facts, source claims, assumptions, calculated results, proposals, author decisions and executed actions. Never convert a question, complaint, comment or desired outcome into an author decision. Label suggestions as proposals.
13. Preserve the author's wording, scope and evaluations. Do not broaden, narrow or reinterpret them silently. Mark an item as accepted only after the author explicitly instructs “MARK AS ACCEPTED”; preserve other evaluations literally.
14. Think, examine evidence and consequences, and disagree with explicit reasons when warranted. Avoid flattery, automatic agreement, emotional imitation, sarcasm, metaphors and judgments about the author's intentions. Change a conclusion when the evidence changes.
15. Use evaluative or comparative adjectives only with a cited source or an explicit comparison. Prefer the actual measurement, condition, price or result.
16. Ask an open question when a required term, scope or decision is ambiguous. Name the exact ambiguity and wait before the dependent action. Do not prescribe the author's answer or restrict it to closed choices.
17. Pair internal identifiers with readable component names. Use repository-relative paths for file links and named-root locators for external files; use direct URLs for source or seller links.
18. In execution reports, identify the model that actually performed the work when that identity is available. Do not substitute the intended model, model family or an assumed equivalent. State that the actual model is unavailable when it is unavailable.
19. Report status only for the requested work and the observed execution state. Use concrete states such as DONE, RUNNING, BLOCKED, FAILED or UNKNOWN. Separate an individual failed test from the state of the overall task. Do not invent totals, completion percentages or previous counts.
20. Do not describe an output as “ready for your verification” or use an equivalent unsolicited formula. Report automated checks as technical results; record author acceptance separately.
21. **State what the thing IS.** Apply this to chat responses and project documents: give concrete ideas, found products, specifications, arrangements, sources and observed errors directly. Omit negative comparisons, obvious explanations, repeated disclaimers, lists of missing information and statements that something is unspecified, unselected, unverified or deferred to later work. Examples to omit include “No complete assembly has been selected”, “Voltage remains unspecified”, “not a payload rating for this base” and “does not establish compatibility”. Attribute specifications directly to the named product and source. In discussion documents, use direct labels such as “Discussion target”, “Layout idea” and “Clearance requirement”; omit references to “the author” or “Author requirement”. Preserve exact requested notices and concrete errors such as physically impossible geometry. Keep factual attribution and operating conditions beside the values they describe.

## Authorization and scope

1. Discussion is the default for questions, ideas, comparisons and proposals. Discussion does not authorize implementation or design selection.
2. Execute explicit action requests within their stated scope. `APPLY` or `EXECUTE`, case-insensitive, authorizes the specific action discussed. An explicit request to create or edit a named file authorizes that file change. Do not demand another approval for work already authorized.
3. Authorization is bounded by the task. It does not authorize unrelated files, new project phases, new features, purchases, seller contact, installation, publication or changes to external systems.
4. Follow the author's requested order. When a plan is requested before execution, present it before launching agents, research, calculations or implementation. A changed scope requires the author's decision before dependent work.
5. A verification reports findings. It does not silently authorize corrections or removal of existing work. Preserve unrelated and concurrent work, source material and calculation results.
6. Inspect an existing file, model or script before changing it. Prefer a targeted edit that preserves valid content and identifiers. Do not restart research or rebuild an artifact merely because a correction is needed.
7. Use the narrowest current scope. Check the intended work before execution and the delivered result afterward against that scope. An agent assignment or existing document does not expand the author's authorization.
8. Stop when instructed to stop. Do not continue, revert changes or launch replacement work without authorization.
9. Git staging, commits, pushes, worktrees and branch reservations require corresponding authorization for this project. Do not inherit automatic-commit exceptions from another project's AGENTS.md. Never discard unrelated changes or reserve the author's branch elsewhere without permission.

## Research and delegation

1. **All external searches and web research require the author's approval and must be performed by small agent models or free ones unless the user instructs otherwise.** The primary agent must not search or browse the web directly unless explicitly instructed to do so. Reading local project files is separate from external research.
2. An approved research task authorizes Luna delegation for that bounded task. Give each agent the exact question, permitted component categories, exclusions, authorized output paths and required source evidence. Parallel agent work requires the author's authorization; do not infer it from the availability of agents.
3. Keep the primary agent's synthesis within the same scope. Check the returned evidence, links, arithmetic and compatibility claims before presenting them. Delegation does not replace review.
4. Reuse existing findings and source documents before commissioning another search. Do not repeat an entire research pass to answer a narrower question.
5. Prefer component manufacturers, service manuals, engineering documents and documented reuse projects for technical specifications. Use actual dismantler or seller listings for price and included-item claims.
6. For each priced part, record the readable name, manufacturer, donor model/year, part number, included components, condition, price, currency, tax treatment, additional fees, delivery cost if shown, observation date and direct item URL. Label a category/search page as such.
7. Distinguish an advertised matched assembly from separate listings. Check motor/inverter generation and part numbers. Keep seller statements separate from manufacturer specifications and measured test results.
8. A dismantler listing establishes used-part provenance. Claim a crashed or broken donor only when the source states that history. Keep advertised original battery capacity separate from measured remaining capacity.
9. Preserve original source files when acquired, with title, URL, retrieval date, content type, local path and hash. Keep originals unchanged and derived notes separate. Record actual retrieval status; a URL, search snippet or summary is not a downloaded original.
10. Source uncertainty belongs next to the affected claim. Do not let generic caveats displace the requested findings. Do not claim a source, video, test, purchase or agent result was inspected or completed without evidence.
11. Research does not authorize purchases or messages to sellers. Stay within the author's requested component categories and price research.

## Current parts-research scope

1. The current sourcing task is **used electric traction motors, matching controllers/inverters, traction batteries or battery modules, and possibly wheels from broken, crashed or dismantled cars**.
2. Answer this task with actual parts and source links. Do not substitute complete vehicles, new conversion kits, new retail batteries, electric quads, motorbikes, mowing machines, radio equipment, safety-system proposals or general prototype budgets unless the author changes the scope.
3. Report motor and inverter listings separately when sold separately; identify bundled components explicitly. Do not silently include a gearbox, charger, controller or battery in a motor-only price.
4. For batteries, identify individual cells, modules and complete packs explicitly. Use traction-battery listings. State nominal voltage, capacity in Ah, energy in kWh and measured condition only to the extent supported by the source.
5. For motor-power questions, identify the requested operating regime. Report peak and continuous-duty values with their own source labels and operating conditions. A peak value does not supply a continuous-duty value. If the requested value is absent, read the existing sources, then state that exact value as unknown; do not invent a derating factor or launch another research task without authorization.
6. Existing findings are under `research/salvage-car-parts/`. Earlier complete-donor research under `research/prototype-01/` remains preserved but does not broaden the current parts task.

## Farm-robot project context

Use this context only when the task concerns the prototype. It does not expand a parts question into a full engineering project.

1. The first useful prototype is a fully electric, radio-controlled base that can tow a small trailer carrying 100 kg of payload on flat ground and later operate a removable electric cutting tool for light vegetation.
2. Trailer empty mass is additional to payload. A later 500 kg payload is a separate target. The initial cutting tool has no 20 mm wood-cutting requirement.
3. The roughly 20 HP micro-tractor is a comparison class. Size traction and implement motors from the chosen operating requirements and actual components.
4. Obtainable used parts and reuse determine the candidate layouts. Conventional appearance is not a requirement. Existing market wheels are required; wheel and tyre suitability must be assessed for the actual loads and terrain.
5. Differential steering is a candidate for construction simplicity. Existing steering can be retained if the selected hardware makes that practical. No chassis or drivetrain has been selected merely by being described in a report.
6. The cutting attachment is removable and electrically driven. Simple manual attachment is acceptable. Hydraulic equipment, if later required, uses an electric pump.
7. Electronic control interfaces must permit later expansion. ArduPilot Rover is a candidate; Raspberry Pi-class computing, RTK, cameras, lidar and radar belong to later tasks when requested.
8. Safety is a design requirement during authorized engineering work: communication-loss response, accessible physical emergency stops, a separate monitored stop remote, braking/holding and deliberate restart. A pressure-sensitive bumper remains an option. Discuss and size these functions when they are in scope; do not append the whole safety discussion to an unrelated specification question.

## Calculations, implementation and CAD

### Required skill-building completion

After creating, changing or deleting reusable Python helpers, package dependencies or skill instructions in this source repository, run `python3 scripts/build_skill_packages.py --finalize`. Supply existing `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT` directories, or the equivalent CLI options. The operation assigns new generic helpers to the CAD package, follows local imports for the smaller skills, regenerates package files and source/hash manifests, and requires lifecycle and isolated installation checks. Run `--verify` for read-only final validation and record its actual PASS result before reporting the tooling improvement complete. Missing test prerequisites, stale files and failed checks keep that improvement incomplete. Include canonical source and generated copies in the same authorized result batch; preserve unrelated concurrent work. [Completion procedure](skills/cad-ocs-engineering/references/package-completion.md).

1. Reuse existing code, methods, libraries, models and data before implementing replacements. Inspect actual files and document sources and changes. Preserve licences and attribution.
2. Before an authorized calculation or implementation, identify the requirement, inputs, units, source evidence, method, affected files and verification. Do not introduce numerical assumptions silently.
3. Every engineering value needs a component, units, source and status: measured value, manufacturer/seller claim, assumed input or calculated result. Include the operating conditions needed to interpret it.
4. When asked for existing results, report results already present in the project sources. Do not fill a missing result with a new operating point, parameter sweep or calculation.
5. Illustrative calculations remain labelled as illustrations. Tests verify the implementation they exercise; they do not establish physical capacity, stability, braking performance or author acceptance.
6. Run checks appropriate to the authorized change. Do not rerun unchanged expensive calculations without a reason. Run one computational job at a time unless the author explicitly authorizes another arrangement.
7. OpenCADStudio is the CAD application identified for this project. Preserve existing documents. Use explicit units, axes, component boundaries and input provenance. Keep schematic arrangements separate from dimensioned manufacturing geometry.
8. Display an existing requested image directly using its absolute path. Do not regenerate, crop or replace it to answer a display request. Keep explanations in the chat and labels in the image.
9. A file-format conversion needs explicit scope: source, target format, tool and information changes. Preserve the original and identify the derivative. Opening or showing an existing file does not authorize an unrelated conversion.

## Existing-model check before every component start

Standing instruction from 13 November 2026:

1. Check the actual component 3D files before starting each component, including when its work record says NOT_STARTED. Inspect the manifest model links, work-record model/output/native_model paths, input-sheet links, existing CAD index and filesystem inventory.
2. Mark a component with an existing matching 3D model DONE in the current work list, retain its readable name and actual path, and reuse the recorded checks. Move to an unfinished component. Preserve the scope and source attribution of the existing geometry.
3. Repeated routine inspection, geometry checking and capture attempts do not reopen an existing completed model. A specific requested revision has its own scope. File searches must distinguish a 3D component from its 2D interface drawing and from another component used as a reference.
4. Use `scripts/model_inventory.py` and the component skill's existing-model start procedure before native CAD construction. Review filename candidates against the actual component identity before starting geometry.

## Source instructions used for this file

Read on 9 November 2026:

1. `${CASA_ROOT}/AGENTS.md`.
2. `${ENERGY_ROOT}/AGENTS.md`.
3. `${EOLIENNES_ROOT}/AGENTS.md`.
4. `${COCOLECOQ_ROOT}/AGENTS.md`.
5. `${COCOLECOQ_ROOT}/blog/AGENTS.md`.

The communication, scope, evidence, preservation and reuse rules are adapted here together with the author's instructions in this project. Other projects' simulation architecture, territorial datasets, turbine solver settings, blog infrastructure, VPN workflow and project-specific commit authorizations remain scoped to those projects.

## Continuing modeling work: repository separation

Instruction date: 13 November 2026. Preparation and ongoing modeling have separate owners. Preserve ongoing iterations and fixes.

1. For future outputs, place FERME component recipes, source originals, source reviews, measurements, model files, captures, job records, progress and action occurrences in FERME under its applicable instructions. Place reusable functions, generic tests, modeling methods, shared skills and tooling-improvement reports in 3dmodeling.
2. Follow the [modeling-agent instructions](research/repository-split-preparation/modeling-agent-instructions.md). Keep project values and paths as inputs to shared tools; link each component result to the exact shared-tool revision.
3. The preparation agent owns separation documents. The modeling agent continues its authorized component/tool improvements and preserves the preparation files. Current active paths remain intact; the split coordinator migrates historical files in a separately scoped batch at affected component checkpoints.
4. Read the [split preparation](research/repository-split-preparation/README.md) before changing repository ownership, imports or fixture paths. The manifest is a dated proposal; refresh it against concurrent work before migration.

## Confidential wind-generator head assembly

Instruction date: 13 November 2026. The wind-generator head assembly is awaiting a patent.

1. Keep its models, images, geometry descriptions, source copies and derived design records out of this repository, its documentation and Git history. Keep original material in its owning private project.
2. Mast-only models and mast simulation examples retain their separate scope. Review actual example content before staging; a filename alone does not establish that an asset is safe to include.
3. Apply this restriction to ongoing agents and future documentation/modeling iterations until the user explicitly releases the protected material.

## Portable stored paths

Instruction date: 13 November 2026.

1. Store repository-relative paths and page-relative Markdown links for this checkout. Represent external project, tool, user and temporary locations through named root placeholders documented in docs/paths.md.
2. Keep machine-specific workspace locations out of committed text and captured metadata. Normalize paths before registering new job records or examples.
3. Preserve registered source IDs, original-source hashes and numerical results. Mark normalized copies as derivatives with their own hashes.
4. Resolve stored root placeholders with an explicit caller-supplied root map before file access. Runtime-derived absolute paths may be used to open files; stored documentation and source locators use portable roots.

## Close completed OCS documents

Standing instruction from 13 November 2026: close finished CAD models and temporary drawings when their iteration no longer needs them, to release document memory.

1. After saved-model, geometry, metadata and persistence checks are recorded, close the iteration's saved/reopened document and its owned construction or inspection documents.
2. Close a dirty construction copy with `discard:true` only when its ownership is recorded, its geometry revision matches the completed evidence, and its saved result exists with the recorded SHA-256. Record the closure beside that component's result.
3. Preserve ongoing work and unrelated open documents. Each close uses a stable request ID, current document/revision checks and same-ID recovery after uncertain completion. Verify the target ID is removed and other document paths/dirty states remain unchanged.
4. Shared runners and skills include this completion step. Keep model files, source originals, recipes, checks and failed-attempt evidence in their owning repository after closing the editor documents.
