# Implementation queue: batch record

Date: 12 November 2026. Coordinator/model: **gpt-6.1-sol**. Starting checkpoint: `c6eeb94`.

## 1. Authorisation and method

1. Request: **execute that now**, referring to the proposed implementation queue, existing-code/evidence links, required changes, ordering and detailed first-action plan. Scope: local source inspection and implementation-design documentation.
2. Read the project instructions, original operation/action records, original route conditions/classifications, the ferme skills/findings and existing OCS/helper source. Reuse the prior source inspection records for third-party tools. External research and CAD/control connections are separate from this batch.
3. The 235 structured action definitions are preserved directly. The ten shared first-point Markdown actions are referenced once through local queue aliases INTAKE-A01–A10; their original CAD-01/DOM-01 operation IDs and headings remain preserved.
4. The dependency-respecting queue selects eligible actions by their proposed action resource band, proposed implementation effort band, descending exact original-route reuse and original audited order. Preceding action links are proposed implementation/test sequencing; full original operation inputs/prerequisites remain explicit. Original-route predecessors apply only when executing that route.

## 2. Findings from existing implementations

1. OCS transport (`${CODEX_HOME}/skills/ocs-engineering/scripts/ocs_control.py`) already provides revision/document preflight, exactly one mutation send and caller-stable uncertain-result identity. Reuse those functions for matching control actions.
2. Component wrapper (`${TEMP_ROOT}/opencode/ngv064_ocs.py`) selects a fixed session descriptor during import, uses temporary state/log locations and a fixed prefix allowlist. Its write/step loops poll accepted/running responses without a total deadline. `write` rejects waiting_input, while `step` permits command continuation. These are precise integration findings for bounded-control and recovery actions.
3. SAT feature reader (`${TEMP_ROOT}/opencode/check_ngv064_wheel.py`) imports that wrapper and supports selected fixed SAT fields, one body transform and unit scale. Reopened SAB data and unsupported transforms require their own reader path before the corresponding feature check can be exercised.
4. Existing supplied-measurement checker (`${CODEX_HOME}/skills/ocs-engineering/scripts/check_contract.py`) validates finite point/axis/plane observations, source identities and numerical comparisons. Its functions can be reused where those observations are available; the geometry acquisition action supplies them separately.
5. Profile script (`${TEMP_ROOT}/opencode/build_item_profile_segment.py`) already reads the retained contour text, samples curves, normalizes coordinates, extrudes/cuts geometry, verifies and saves/reopens the component. Its input is extracted contour text. Generic DXF entity parsing is a different adapter in the vector inspection action.
6. The retained wheel, bracket, profile, Leaf and BMW native JSONs contain 14, 21, 11, 14 and 13 PASS observations respectively. These are inspected historical component checks, linked to their original documents/revisions. Pre-save feature observations and reopened audit/display results retain their stage and method.
7. Ferme's improvement text remains a proposed extension in that repository, paired with the installed OCS skill as instructed by its README. The queue records repository instructions, installed skill source, component code and results as separate assets.

## 3. First-task selection proposal

1. **Record source files, revisions and job scope** supplies the source index/scope statement consumed by the other shared intake actions. Its direct input is a request and retained sources, and its local computation is file/text bookkeeping.
2. Its existing precedents are the project's locator/hash source register and ferme's source/derivative/scope rules. The proposed addition is a per-job adapter and the action-specific agent instructions/tests, with explicit inputs/output locations and preserved source revisions.
3. The drawing inspection proposal remains its own action in the queue. Component construction, image interpretation, numerical normalization, candidate selection and merging retain separate definitions and dependencies.
4. This is a proposed implementation order and first-task design. User decisions and design acceptance retain the original project rules.

## 4. Registration and checks

1. Every inspected asset and authored queue document has an exact local source locator, date, summary, evidence status and SHA-256 in the batch source manifest. Original third-party URLs remain in the copied action/operation records and project register.
2. New queue/first-task ideas are registered with proposal status. The document receipt records actual action/operation coverage, dependency ordering, asset references, source snapshots, links, preserved baseline files/graphs and reproducible generation checks.
3. The final result commit closes this documentation batch. Modeling/helper implementation results use their respective future execution records.

4. The first coverage check failed because shared intake Action 10 labels its output as **Output and resume condition**, with a separate **Handoff checks** field. The temporary extraction adapter initially expected **Output and check** for every intake action. The adapter now preserves both actual fields and stops the last action at the next section heading. The original procedure is preserved. The check receipt records the failed attempt and subsequent rerun.

5. Mermaid count review found that the unanchored word-boundary pattern also matches a quoted regex example in the earlier verification method. The final check retains that raw-pattern comparison and adds line-anchored fence comparisons for the two actual diagrams. The final receipt reports actual diagrams and raw pattern matches separately.
