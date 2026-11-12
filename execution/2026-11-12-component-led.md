# Component-led execution: initial records and source gate

Date: 12 November 2026. Executing model: **gpt-6.1-sol**. State: **setup implemented; rail NEEDS_INPUT**. Tooling checkpoint: `8dbd49f`; FERME checkpoint: `cfcb62d`.

## 1. Executed scope and ownership

1. User instruction: execute the [component development plan](/home/leo/projects/3dmodeling/COMPONENT_DEVELOPMENT_PLAN.md) after it is written. The current work implements initial data access, action/source records and the first rail's source-readiness check.
2. FERME retains the existing [103-component input index](/home/leo/projects/ferme/engineering/module-development/cad-inputs/parts.json), [eight-entry parts/standards dictionary](/home/leo/projects/ferme/skills/dictionaries/parts-and-standards.json), native models and new [component work/action evidence](/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/README.md).
3. This project supplies [part-index access](/home/leo/projects/3dmodeling/scripts/part_index.py), [source-readiness and action-occurrence records](/home/leo/projects/3dmodeling/scripts/component_records.py), [component iteration skill](/home/leo/projects/3dmodeling/skills/component-cad/SKILL.md) and [tests](/home/leo/projects/3dmodeling/tests/test_component_tools.py).
4. The newly inspected [FERME automation modules](/home/leo/projects/ferme/skills/cad-automation-and-reuse.md) already implement Client/Journal/Geometry/recipes/verification. Reuse those functions rather than the earlier temporary fixed-session wrappers. Their actual source files are registered in this batch.

## 2. Actual results

1. Index search executed against FERME's component index: **Main frame longitudinal rail (P01)** returns its exact source record and hash. Search against the actual dictionary for `ISO 730` returns its two attributed Category 1/1N interface records with their retained edition fields. Search preserves source namespaces and does not merge equal IDs across data sources.
2. Existing dictionary validation: **PASS, eight entries**. Existing FERME offline suite: **66 tests PASS**, using synthetic transport/geometry and retained recorded feature observations according to that suite's scope.
3. New helper suite: **18 tests PASS**. Cases cover source identity and content preservation, standards/edition search, duplicate identities and JSON keys, supported data shapes, pinned-source changes, unresolved feature questions, concurrent-source change detection and append-only occurrence behavior.
4. New skill format validation: **PASS** using the skill-creator validator. Its behavior is supported by the actual index/readiness commands and helper tests described above.
5. FERME job index: **103 component references**, rail `NEEDS_INPUT`, crossmember `WAITING_FOR_P01`, remaining 101 `NOT_STARTED`. Two rail action occurrences record successful source capture and the feature-readiness input condition. Individual action names and graph references remain distinct.
6. Rail source values: **proposed** 40 x 40 x 3 mm nominal section and 600 mm cut length. Crossmember source values: same proposed section, 260 mm length and rail dependency. Source/proposal labels and file revisions are preserved in FERME job records.
7. Required input question: **What corner profile should the 40 x 40 x 3 mm rail and crossmember use: a specified supplier profile/radii, or an explicitly authorised nominal square-corner representation?** The inspected sheets, fabrication requirements and frame-stock report supply nominal section/lengths. The named corner input is required by the plan before dependent geometry construction.
8. No CAD iteration has met the plan's component-plus-applied-improvement completion criteria. The new source gate and skill instructions implement the observed source-readiness action; component geometry/persistence/view checks remain attached to their future native execution.

## 3. OCS connection and preservation

1. Applied the installed [OCS skill](/home/leo/.codex/skills/ocs-engineering/SKILL.md) and its control/model-contract references. Default-sandbox discovery returned socket permission errors. The authorised escalated discovery found one live session, **OCS 2026.42**; other descriptor endpoints refused connection.
2. State and capabilities reads reported active document **52**, revision **2**, dirty **true**, Neugart NGV064 wheel path, with command/modal empty. This run sent read/discovery requests only. Existing document contents and unsaved work were preserved.
3. Both projects received empty starting checkpoint commits. FERME's unrelated untracked source/research and OCS lock/autosave files remain outside the staged work.

## 4. Failure and test history

1. First new-suite attempt: 17 tests passed and the concurrent-source-change fixture raised `StopIteration` because mocking `Path.stat` also intercepted a call during `Path.resolve`. The fixture now isolates resolution and checks the actual pre/post hash-capture stat comparison.
2. Second attempt: the stronger occurrence-field validation correctly rejected a fixture that still used empty arrays for representation/units/frame. The fixture now supplies explicit readable fields. No domain validation was relaxed.
3. Final suite: all 18 tests pass. The real rail command exits **1** with `NEEDS_INPUT`, which is its documented source-readiness result. It preserves the exact question and supplies no default geometry value.
4. The batch check receipt records source/record consistency, actual helper results, tracked model preservation and the state of the original plans/graph. Source snapshots retain their individual observation revisions.
