# First implementation task: Record source files, revisions and job scope

Date: 12 November 2026. Status: **implementation proposal**. Planning model: **gpt-6.1-sol**.

## 1. Exact action and selection

1. Implement the existing **Preserve the input revision and state the job boundary** action, shared by **Extract a model brief from text and dimensions (CAD-01)** and **Normalize model brief (DOM-01)**. The queue reference `INTAKE-A01` points to Action 01 in the [existing procedure](../point-01-model-brief.md). The display title above describes the proposed deliverable; original action names and identifiers remain unchanged.
2. Its direct inputs are the current request, supplied source files/text, explicit source identities and corrections. Its outputs are a source index and a scope statement. Those outputs feed the separate **Select the execution mode and define candidate branches** action. The full original operation input contracts remain in the [queue](queue.json).
3. Selection basis: this action has no earlier action dependency, uses file/text bookkeeping and hashing, and produces the revision identity needed by every later intake action. It reuses the source-record conventions already in the project. The queue records its exact original-route reuse count. Local work is proportional to retained bytes and record count; remote reasoning reviews the scope and correction relationships.
4. This first implementation task packages one source-index procedure. Component interpretation, quantity normalization, tolerance assignment, candidate merging and downstream CAD construction keep their existing action boundaries.

## 2. Reuse and specific change

1. Reuse the inspected [source register builder](../../tools/build_workflow_register.py) conventions: `sid` uses a locator digest, records preserve exact URLs/local paths, and observations carry evidence and dates. The existing builder operates on project-global research records. The proposed addition is a per-job adapter with explicit inputs/output paths and retained revisions.
2. Reuse ferme's construction skill (`${FERME_ROOT}/skills/cad-construction/SKILL.md`), sections **Build the source and parameter record** and **Establish the deliverable and inspect existing work**, for original/derivative attribution and task boundaries.
3. Reuse the installed OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) modeling-contract instructions for exact scope and correction preservation. OCS construction and session mutations belong to their documented downstream actions.
4. Proposed implementation files, relative to this project: `scripts/source_intake.py`, `tests/test_source_intake.py`, and `skills/source-intake/SKILL.md`. The script performs source bookkeeping; the skill supplies scope/evidence instructions. These paths specify future implementation work.

## 3. Proposed input contract

1. A job input record supplies a readable job name, exact request text and source location, requested output type, authorised output paths and any explicit source-priority instruction.
2. Each source entry supplies an ID, readable title, source kind, original locator, observation date and optional parent/derivative relationship. Source kinds are local file, supplied message/text and URL reference. A URL reference preserves its supplied URL and inspection status. Network acquisition remains its own action.
3. Explicit corrections name the source/statement they revise and preserve the correction wording. A source-priority conflict is retained with its affected scope.
4. The agent reads the original request and supplies the scope statement, identifying requested actions and output artifacts. Software verifies record structure and reference resolution; it preserves the exact supplied wording.
5. Proposed example input: a retained local drawing, a supplied description and a correction changing the intended component identity. The output records all three and the correction link. Geometry values remain in their source records for the later extraction action.

## 4. Proposed output contract

1. One immutable intake directory per completed revision: a JSON source index, a Markdown scope statement and an execution receipt. Existing originals are referenced in place; an explicitly requested retained copy records its original and derivative relationship.
2. Each file observation includes source ID, exact locator, SHA-256, byte count and observed revision metadata. Hash identity and source identity have separate fields: an existing source can acquire new bytes while retaining its readable identity.
3. Supplied text is retained exactly with its source/message location and text digest. URL-only entries have a URL-registration evidence label. Existing external source claims retain their original evidence label and locator.
4. The index records source/derivative and correction relationships, prior intake revision where supplied, scope-statement path and the observation status of every source entry.
5. The receipt records actual script/runtime version, input identity, output paths/hashes, failures and measured processing time/memory method where collected. Completion requires a complete parseable output set and preserved source observations.

## 5. Implementation sequence

1. Freeze input/output examples and expected results from Action 01's contract. Inspect the selected existing provenance conventions and preserve their exact source records.
2. Add strict JSON input reading: reject duplicate keys and nonfinite numeric tokens; validate source IDs, kinds, required text fields and correction/derivative references before output publication. Reuse the [intake source review](../reviews/source-check.md) for existing JSON/hashlib evidence.
3. Add streaming file hashing. Record file identity before/after reading; classify observed changes during capture and preserve the failed attempt. Resource use is bounded by the streaming buffer plus record count.
4. Add exact text preservation and URL-reference registration. Validate prior-revision and correction links, and keep source-priority conflicts beside their affected scope.
5. Write the output set in a staging directory, validate all references and hashes, then publish a new completed revision directory without replacing an earlier revision. A failed publication leaves a named incomplete attempt.
6. Add the agent skill instructions for scope statements, source classifications and correction review. Interpretation decisions remain attributed to that agent and its cited evidence.
7. Execute the test cases below, then run a read-only intake on selected existing source files in this checkout. Record actual results and check source hashes before/after.
8. Document the command, input/output examples, failure status and resumption procedure; create the result commit after the checks pass.

## 6. Proposed commands and expected results

Commands below describe the future interface. Input fixtures and output directories are supplied to that future implementation.

```sh
python3 scripts/source_intake.py --input <job-input.json> --output <new-intake-directory>
python3 -m unittest discover -s tests -p test_source_intake.py
```

1. The first command emits the source index, scope statement and receipt. Proposed exit codes: `0` completed; `1` source observation/reference conflict; `2` invalid input or I/O failure. Each failure identifies its source and affected output.
2. The second command exercises record correctness and source preservation using temporary fixture files. It requires no OCS session or model download.
3. A corrected input or changed source creates another intake revision referring to the prior record. Complete earlier records remain readable.

## 7. Proposed test cases and independent review

1. **Unchanged file:** independently computed fixture SHA-256 and byte count match the record; original bytes remain identical.
2. **Source revision:** changed bytes create a new observation and intake revision while preserving the earlier observation and source ID.
3. **Text fidelity:** Unicode, line breaks and explicit corrections survive roundtrip exactly; every correction resolves to a retained source statement.
4. **Locator versus bytes:** identical content at two supplied locators retains both source references; source-content equality remains explicit.
5. **Input validation:** duplicate source IDs/JSON keys, nonfinite numbers and broken parent/correction references produce named failures.
6. **Read failure or concurrent source change:** the affected source observation fails and the attempt is retained; completion is withheld for that record.
7. **Output protection:** an existing completed revision remains byte-identical after a conflicting output-path request or interrupted publication.
8. **URL registration:** an exact supplied URL is retained with its actual inspection status; the test transport records zero network calls.
9. **Scope review:** an independent reader compares the exact request, scope statement and correction chain. It checks that each requested action/output is represented and that proposed additions retain proposal status.
10. **Completion criteria for this implementation task:** all required software cases pass, scope review records its findings, output references resolve and input source hashes are preserved. Per-job design acceptance follows the project's existing decision records.

## 8. Recorded boundary and dependencies

1. The authorised current batch produces the implementation queue and this plan. The code paths, interface and tests above are implementation proposals.
2. First-task dependencies are Python standard-library file, JSON and hashing operations plus the existing source/authorisation rules. Model reasoning supplies the scope statement and evidence associations. Input file size and model usage are recorded separately when executed.
3. Shared intake Action 02 consumes this record next. The queue retains each original action's individual implementation contract, existing assets and conditional route dependencies.
