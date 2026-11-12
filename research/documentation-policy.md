# Research registration and change checkpoints

Instruction date: 12 November 2026. Status: user instruction applied to this project.

> From now on ALL things all ideas all sources all is REGISTERED WRITTEN DOWN AND DOCUMENTED with real original links and summaries. apply if not done yet, always commit before and after changes

## Records

1. **Source register:** `sources/source-register.json` and its readable counterpart record original URLs/local paths, titles, summaries, evidence status, dates and referring documents. The original supplied URL and a discovered upstream source each receive a record.
2. **Workflow operations:** `workflows/workflow-map.json` records inputs, outputs, tools, prerequisites, changed information, preserved information, checks, alternatives and supporting sources. A representation name describes the artifact; the unit/frame and measurement conditions describe what the artifact can establish.
3. **Combined workflows:** recipes in the same map record input combinations, operation sequences and explicit handoffs. A branch can supply measurements, library parts or camera calibration to another branch. Iterative edits create a new model revision and retain the source evidence.
4. **Ideas and research questions:** `ideas-register.json` records new possibilities and retained earlier proposals, with summaries, source references and next checks. Source-backed capabilities, proposed combinations, user instructions and observed execution have separate status labels.
5. **Original evidence:** downloaded sources have a preserved file, content type and SHA-256. An existing research report can register a source without promoting its evidence status to a new inspection. Existing local originals remain at their recorded paths.
6. **Discussion:** relevant ideas and sources from project discussion are registered under the standing documentation instruction. Modeling or installation work follows its own task scope.

## Checkpoint procedure

1. Inspect current files and Git status. Identify the authorized batch and preserve unrelated work.
2. Commit the starting checkpoint. For a clean worktree, an empty checkpoint can record the boundary.
3. Perform the authorized batch; keep agent output paths disjoint and let the coordinator own Git operations.
4. Check source references, original links, summaries, workflow inputs/outputs, recipe dependencies and document links. Retain actual check results.
5. Commit the resulting changes. Record both commit identifiers in the execution report. Use the following batch's starting checkpoint to bracket subsequent work.

## Current research batch

1. Starting checkpoint: `f50c6f2`, `docs: checkpoint initial modeling research`.
2. Scope: preserve existing research; backfill its source and idea registers; extend individual/combined workflow research; update documentation and indexes.
3. Research assignments: CAD and 2D inputs; reconstruction and mixed inputs; architecture/robotics/component handoffs. Existing research agents are reused through their previously requested `gpt-6-luna` configurations. The agents report that exact runtime model identities are unavailable.
4. Existing execution finding: earlier research-document edits and creation of `research/verification.json` were reported as exceeding the preceding link-discussion scope. This checkpoint preserves that existing state. The current instruction expressly authorizes project research registration and local before/after commits.
5. Initial checkpoint inspection found an extra blank line at the end of `research/reconstruction.md`; the documentation batch includes removal of that whitespace and retains the report's substantive content.
