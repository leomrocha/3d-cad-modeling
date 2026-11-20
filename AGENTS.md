# Instructions for agents working in this repository

This repository SCOPE is ONLY GENERIC tasks, procedures, tooling and skills for 2D and 3D modeling.

## Authorization and scope

1. Discussion is the default for questions, ideas, comparisons and proposals. Discussion does not authorize implementation or design selection.
2. Execute explicit action requests within their stated scope. `APPLY` or `EXECUTE`, case-insensitive, authorizes the specific action discussed. An explicit request to create or edit a named file authorizes that file change. Do not demand another approval for work already authorized.
3. Authorization is bounded by the task. It does not authorize unrelated files, new project phases, new features, purchases, seller contact, installation, publication or changes to external systems.
4. Follow the user's requested order. When a plan is requested before execution, present it before launching agents, research, calculations or implementation. A changed scope requires the user's decision before dependent work.
5. A verification reports findings. It does not silently authorize corrections or removal of existing work. Preserve unrelated and concurrent work, source material and calculation results.
6. Inspect an existing file, model or script before changing it. Prefer a targeted edit that preserves valid content and identifiers. Do not restart research or rebuild an artifact merely because a correction is needed.
7. Use the narrowest current scope. Check the intended work before execution and the delivered result afterward against that scope. An agent assignment or existing document does not expand the user's authorization.
8. Stop when instructed to stop. Do not continue, revert changes or launch replacement work without authorization.
9. Git staging, commits, pushes, worktrees and branch reservations require corresponding authorization for this project. Do not inherit automatic-commit exceptions from another project's AGENTS.md. Never discard unrelated changes or reserve the user's branch elsewhere without permission.


## Communication with the user

Exact vocabulary, explicit context and unambiguous engineering communication are MANDATORY functional requirements. Apply these rules in the response itself.

1. Answer the question actually asked. State the requested specification, result, explanation or link directly. Do not substitute another question, a general lesson or an explanation of something the user already knows.
2. ONLY use simplified technical English, literal wording and stable, uniquely identifying and carefully chosen terminology. Use one term for one concept. Define a technical term when its meaning is needed to understand the answer; do not substitute definitions of individual words for an explanation of the complete engineering statement.
3. Name the component, action, scope and result explicitly. Avoid vague references and verbs such as “manage”, “handle”, “fix” or “continue” without naming their object and the action.
4. Present facts and specifications directly. Avoid definitions and explanations framed as “this is X, not Y”, “not X but Y”, “this is not about…” or equivalent unsolicited contrasts.
5. NEVER USE filler and narrative framing: “why it matters”, “what you want”, “one important point”, “that distinction matters”, “bottom line”, and equivalent formulas. Do not paraphrase the user's request as a preamble. DO NOT repeat the users statements, ENGINEER DISCUSS mode by default.
6. Do not append unsolicited lectures, warnings, procedural commentary, approval reminders, descriptions of inactivity, retrospective explanations, recaps or closing offers. Include a limitation only when it changes the meaning of the requested fact or is necessary for the requested engineering work.
7. When asked what research found, lead with the actual findings: findings, measurements, specifications and direct source links. Do not replace the findings with a list of missing information, unqualified candidates or work not performed.
8. When asked for specifications, give the specifications with labels and units. When asked for links, give the links. When asked for one value, answer that value. A report link alone does not replace the requested answer.
9. Use explicit labels and numbered lists for multiple facts, parameters and calculations. Use a table when the user requests one. Do not silently replace a requested format.
10. A question receives its answer and control returns to the user. Reading existing project files and source documents to identify the answer is allowed. A question alone does not authorize new research, calculations, simulations, file changes or the next project phase.
11. A communication instruction receives a response about communication only. Do not repeat technical parameters, calculations or design proposals in that response. Apply the correction immediately rather than substituting a promise for the requested answer or action.
12. Distinguish observed facts, source claims, assumptions, calculated results, proposals, author decisions and executed actions. Never convert a question, complaint, comment or desired outcome into an author decision. Label suggestions as proposals.
13. Preserve the user's wording, scope and evaluations. Do not broaden, narrow or reinterpret them silently. Mark an item as accepted only after the user explicitly instructs “MARK AS ACCEPTED”; preserve other evaluations literally.
14. Think, examine evidence and consequences, and disagree with explicit reasons when warranted. Avoid flattery, automatic agreement, emotional imitation, sarcasm, metaphors and judgments about the user's intentions. Change a conclusion when the evidence changes.
15. Adjectives are FORBIDDEN for most uses. Use evaluative or comparative adjectives only with EXACT MATHEMATICAL OR LOGICAL COMPARISONS. Prefer the actual measurement, condition or result.
16. Ask an open question when a required term, scope or decision is ambiguous. Name the exact ambiguity and wait before the dependent action. Do not prescribe the user's answer or restrict it to closed choices.
17. Pair internal identifiers with readable component names. Use repository-relative paths for file links. Use direct URLs for source links.
18. In execution reports, identify the model that actually performed the work when that identity is available. Do not substitute the intended model, model family or an assumed equivalent. State that the actual model is unavailable when it is unavailable.
19. Report status only for the requested work and the observed execution state. Use concrete states such as DONE, RUNNING, BLOCKED, FAILED or UNKNOWN. Separate an individual failed test from the state of the overall task. Do not invent totals, completion percentages or previous counts.
20. Do not describe an output as “ready for your verification” or use an equivalent unsolicited formula. Report automated checks as technical results; record author acceptance separately.
21. **State what the thing IS.** Apply this to chat responses and project documents: give concrete ideas, found products, specifications, arrangements, sources and observed errors directly. Omit negative comparisons, obvious explanations, repeated disclaimers, lists of missing information and statements that something is unspecified, unselected, unverified or deferred to later work. Examples to omit include “No complete assembly has been selected”, “Voltage remains unspecified”, “not a payload rating for this base” and “does not establish compatibility”. Attribute specifications directly to the named product and source. In discussion documents, use direct labels such as “Discussion target”, “Layout idea” and “Clearance requirement”; omit references to “the user” or “Author requirement”. Preserve exact requested notices and concrete errors such as physically impossible geometry. Keep factual attribution and operating conditions beside the values they describe.


## 3D modeling research, documentation and Git

1. Git records implementation history. Keep skill code, instructions, installers, tests, their inputs and distribution requirements in the repository. Keep implementation narratives, local availability records and trial logs outside the repository.
2. Keep original licences, copyright notices, attribution and source links with reused code and assets. Preserve source originals unchanged. Keep existing research and the implementation plan within their authorized scope.
3. For explicitly requested research, preserve the research plan, source register, idea register and original links. A source entry gives the readable title, original URL or local locator, summary, observation date, evidence status and referring documents. Preserve supplied URLs alongside canonical URLs. An acquired original retains its retrieval date, content type, path and SHA-256.
4. Link each researched workflow to its supporting sources, inputs, outputs, prerequisites, tools, units and frames, preserved information, checks, alternatives and downstream handoff conditions. Keep proposals and source claims separate from locally measured results. Mark an idea accepted only on the explicit instruction `MARK AS ACCEPTED`. A research request does not authorize implementation, installation or publication.
5. Create a checkpoint commit before an authorized logical change batch and a result commit afterward. An empty checkpoint may mark the start. Stage only authorized files. Preserve unrelated changes. Pushes remain separately scoped.
6. The coordinating agent owns the commits and reviews changes from delegated agents. Assign disjoint paths when parallel work is authorized and require sources and summaries for authorized research.


### Skill downloads and the separate OpenCV installer

1. Skills must not download anything during execution. Use only resources already available. This rule includes downloads triggered by a library, installer or subprocess. No skill may download models or model weights.
2. The separate optional OpenCV installer skill is the explicit exception for installing OpenCV. Before installation, it must tell the user that the requested operation needs OpenCV and that the installer will install OpenCV. A modeling skill may point to the installer when OpenCV is missing.
3. Invoking the separate OpenCV installer authorizes that installation in the same run. Other exceptions require a single, simple user message containing `EXECUTE` and requesting only that action.

## Research and delegation

1. External web searches require the user’s approval. Use small agents for every approved web search. The primary agent must not search or browse the web directly unless explicitly instructed to do so. Reading local project files is separate from external research.
2. Give each search agent the exact question, scope, exclusions, authorized output paths and required source evidence. Parallel agent work requires the user's authorization; do not infer it from the availability of agents.
3. Keep the primary agent's synthesis within the same scope. Check the returned evidence, links, arithmetic and compatibility claims before presenting them. Delegation does not replace review.
4. Reuse existing findings and source documents before commissioning another search. Do not repeat an entire research pass to answer a narrower question.
5. Use original technical documentation and engineering drawings for dimensions, interfaces, and operating limits.
9. Preserve original source files when acquired, with title, URL, retrieval date, content type, local path and hash. Keep originals unchanged and derived notes separate. Record actual retrieval status; a URL, search snippet or summary is not a downloaded original.
10. Source uncertainty belongs next to the affected claim. Do not let generic caveats displace the requested findings. Do not claim a source, video, test or agent result was inspected or completed without evidence.

## Calculations, implementation and CAD

### Required skill-building completion

After creating, changing or deleting reusable Python helpers, package dependencies or skill instructions in this source repository, run `python3 scripts/build_skill_packages.py --finalize`. Supply existing `SKILLS_CLI_ROOT` and `NATIVE_READER_ROOT` directories, or the equivalent CLI options. The operation assigns new generic helpers to the CAD package, follows local imports for the smaller skills, regenerates package files and source/hash manifests, and requires lifecycle and isolated installation checks. Register helpers in docs/tools.md and main-skill procedures in skills/README.md. Distribute required licences and notices with their code. Package checks use current sources and fixture inputs. Run `--verify` for read-only final validation and report its actual PASS result before reporting the tooling improvement complete. Missing test prerequisites, stale files, missing registrations and failed checks keep that improvement incomplete. Include canonical source and generated copies in the same authorized result batch; preserve unrelated concurrent work. [Completion procedure](skills/cad-ocs-engineering/references/package-completion.md).

1. Reuse existing code, methods, libraries, models and data before implementing replacements. Inspect actual files and document sources and changes. Preserve licences and attribution. Credit original authors and retain their source links. Before reusing third-party material, check the original terms for the specific use, including adaptation and redistribution in an installable skill. Record the source, applicable terms, conditions and any unresolved permission in the findings list.
2. Before an authorized calculation or implementation, identify the requirement, inputs, units, source evidence, method, affected files and verification. Do not introduce numerical assumptions silently.
3. Every engineering value needs a component, units, source and status: measured value, source-reported value, assumed input or calculated result. Include the operating conditions needed to interpret it.
4. When asked for existing results, report results already present in the project sources. Do not fill a missing result with a new operating point, parameter sweep or calculation.
5. Illustrative calculations remain labelled as illustrations. Tests verify the implementation they exercise; they do not establish physical capacity, stability, braking performance or author acceptance.
6. Run checks appropriate to the userized change. Do not rerun unchanged expensive calculations without a reason. Run one computational job at a time unless the user explicitly authorizes another arrangement.
7. OpenCADStudio is the CAD application identified for this project. Preserve existing documents. Use explicit units, axes, component boundaries and input provenance. Keep schematic arrangements separate from dimensioned manufacturing geometry.
8. Display an existing requested image directly using its absolute path. Do not regenerate, crop or replace it to answer a display request. Keep explanations in the chat and labels in the image.
9. A file-format conversion needs explicit scope: source, target format, tool and information changes. Preserve the original and identify the derivative. Opening or showing an existing file does not authorize an unrelated conversion.

## Select modeling operations by reuse priority

For each modeling decision use the first suitable route in this order: reuse an existing component unchanged, modify an exposed parameter on a compatible existing model, run an existing script or automated service, use an existing guided skill or sub-skill, then perform the uncovered work. Check the CAD Models index and user-supplied local parts sources. Choose providers by the actual deployment's supported inputs and outputs. Within a level consider total effort and cost, including verification. Preserve local evidence from the first operation. Apply the [operation selection procedure](docs/modeling-operation-selection.md).

## Existing-model check before every component start

Standing instruction from 13 November 2026:

1. Check the actual component 3D files before starting each component, including when its work record says NOT_STARTED. Inspect the manifest model links, work-record model/output/native_model paths, input-sheet links, existing CAD index and filesystem inventory.
2. Mark a component with an existing matching 3D model DONE in the current work list, retain its readable name and actual path, and reuse the recorded checks. Move to an unfinished component. Preserve the scope and source attribution of the existing geometry.
3. Repeated routine inspection, geometry checking and capture attempts do not reopen an existing completed model. A specific requested revision has its own scope. File searches must distinguish a 3D component from its 2D interface drawing and from another component used as a reference.
4. Use `scripts/model_inventory.py` and the component skill's existing-model start procedure before native CAD construction. Review filename candidates against the actual component identity before starting geometry.
5. Every execution order and delegated component assignment must start with this instruction: inspect the actual matching component models and all manifest, work-record, input-sheet and CAD-index references, including when the status is NOT_STARTED. If a matching completed model exists, mark that item DONE with its readable name, actual model path and recorded checks, then move to the next unfinished item. Reuse its completed geometry and checks. Construction starts only after this reconciliation establishes that the required model is absent; a script's NEW_MODEL_REQUIRED label alone does not complete the reconciliation.

## Portable stored paths

Instruction date: 13 November 2026.

1. Store repository-relative paths and page-relative Markdown links for this checkout.
2. Keep machine-specific workspace locations out of committed text and captured metadata. Normalize paths before registering new job records or examples.
3. Preserve registered source IDs, original-source hashes and numerical results. Mark normalized copies as derivatives with their own hashes.
4. Each skill finds its bundled files from its installation directory. When the user selects a parts folder during setup or catalogue refresh, save that choice locally and use it for later jobs.

## Close completed 3D model documents

Close finished CAD models and temporary drawings when their iteration no longer needs them, to release document memory.

1. After saved-model, geometry, metadata and persistence checks are recorded, close the iteration's saved/reopened document and its owned construction or inspection documents.
2. Close a dirty construction copy with `discard:true` only when its ownership is recorded, its geometry revision matches the completed evidence, and its saved result exists with the recorded SHA-256. Record the closure beside that component's result.
3. Preserve ongoing work and unrelated open documents. Each close uses a stable request ID, current document/revision checks and same-ID recovery after uncertain completion. Verify the target ID is removed and other document paths/dirty states remain unchanged.
4. Shared runners and skills include this completion step. Keep model files, source originals, recipes, checks and failed-attempt evidence in their owning repository after closing the editor documents.
