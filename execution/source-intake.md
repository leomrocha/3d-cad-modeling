# Source-intake implementation

Date: 12 November 2026. Executing model: gpt-6.1-sol. Checkpoint: `e6bd1c5`. Action: **Record source files, revisions and job scope (INTAKE-A01)**.

1. **New implementation:** [source_intake.py](/home/leo/projects/3dmodeling/scripts/source_intake.py), [source-intake skill](/home/leo/projects/3dmodeling/skills/source-intake/SKILL.md) and [tests](/home/leo/projects/3dmodeling/tests/test_source_intake.py) implement the existing [first-action plan](/home/leo/projects/3dmodeling/research/action-audit/implementation-queue/first-action-plan.md). Source inspection established that these paths were absent before this batch. Existing `part_index.parse_json` and `component_records.observe_file` are reused.
2. **Software work:** validate source IDs, dates, correction/parent references, source cycles and scope fields; preserve exact text and URL locators; hash local files; compare pinned bytes; link new revisions to checked prior artifacts; publish the output set; preserve failed attempts and earlier revisions. The script makes zero network requests and imports no CAD client.
3. **Agent work:** interpret authorization, write the scope statement, identify source meanings, preserve correction wording and review attributed conflicts. Software records those statements and checks references and byte identities. Design interpretation retains the next action's boundary.
4. **Actual execution:** [input](/home/leo/projects/3dmodeling/execution/source-intake/job-input.json) records the current implementation instruction, the preceding no-redo instruction, project rules and existing first-action plan. The [published source index](/home/leo/projects/3dmodeling/execution/source-intake/live-01/revision/source-index.json), [scope](/home/leo/projects/3dmodeling/execution/source-intake/live-01/revision/scope.md) and [receipt](/home/leo/projects/3dmodeling/execution/source-intake/live-01/revision/receipt.json) retain four actual sources. Original local source bytes are preserved. The receipt records its captured tool SHA and runtime.
5. **Tests:** all12 source-intake cases PASS. They exercise exact Unicode/text/corrections, changed source bytes, equal bytes at distinct locators, URL registration with blocked network calls, invalid references/cycles, duplicate keys/overflowing numbers, pinned-source conflicts, read/change failures, interrupted publication and prior-output protection. The final reference-validation test additionally rejects a conflict that repeats one source identity twice. That guard was added after the local capture; the final targeted suite passed with it.
6. **Publication procedure:** the explicit output directory is exclusively reserved. Its `incomplete` subdirectory receives the validated artifact set and is atomically renamed to `revision`. A reserved attempt is preserved after failure. This implements the plan's staging/publication requirement using a reserved parent directory rather than replacing any earlier revision.
7. **Scope review:** the coordinating agent compared the exact request, source/correction fields and recorded scope. The recorded deliverables are the unfinished intake script, skill, tests and execution documentation. Completion of source bookkeeping hands its revision to **Select the execution mode and define candidate branches (INTAKE-A02)**.

Run the implemented command with a new output path:

```sh
python3 /home/leo/projects/3dmodeling/scripts/source_intake.py \
  --input /absolute/path/job-input.json \
  --output /absolute/path/new-intake-directory
```

The [skill](/home/leo/projects/3dmodeling/skills/source-intake/SKILL.md) documents the input fields, output paths, exit codes and recovery.
