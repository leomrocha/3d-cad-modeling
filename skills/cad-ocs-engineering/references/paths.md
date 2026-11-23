# Installed package and job paths

1. Load bundled code from the installed skill's `scripts` directory. `${SKILL_ROOT}/path` refers to that skill's installation directory.
2. In a source job, use a path relative to the job file for a selected input beside that file. The job can also select an existing source by its absolute path at runtime. Runners use `${JOB_ROOT}` for the source job directory, `${EVIDENCE_ROOT}` for the receipt directory and `${OUTPUT_ROOT}` for the directory of the selected output. A selected external source directory can be recorded as `${INPUT_n_ROOT}`, where `n` is its source position in the job record.
3. Where an operation accepts a project, CAD directory, input index or work index, those selections define `PROJECT_ROOT`, `CAD_ROOT`, `INDEX_ROOT` and `WORK_INDEX_ROOT`. The index roots identify the directories that contain the index files. Existing model links keep their established CAD-directory or input-sheet context.
4. Use the [saved parts catalogue](modeling-operation-selection.md#set-up-and-refresh-the-local-operation-catalogue) to look up reusable parts. A single selected catalogue directory resolves `${PARTS_ROOT}/path`. Candidate lookup from saved catalogues reports a source-specific locator for each asset when multiple catalogues are selected.
5. An unknown origin or a path that escapes a named origin fails resolution. When reopening an older record with a custom origin, its compatibility override supplies the original mapping. Keep original source hashes and record separate derivative hashes when normalizing stored paths.

## Bind successive saved models for a replay

1. Keep each original save receipt and the separate fit or geometry evidence. Resolve an evidence-root saved path beside its own receipt. Check that it stays inside that directory and that the saved bytes match the receipt hash.
2. Walk from the selected saved model back to the requested baseline. At each step require the preceding model's exact path and hash in the child's source pins, a passing save with no dropped objects and the relevant geometry result. Compare the exact parent and child bytes. A save can have the same hash under more than one path. Use the path explicitly pinned by the next step to select the intended input.
3. If a replay consumes absolute paths, write a separate normalized reference to the unchanged receipt. Record the original receipt path and hash. Retain each stage's actual result label and scope. Recheck affected interfaces and neighbours on the selected model after the lineage passes.
