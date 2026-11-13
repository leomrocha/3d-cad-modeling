# Three parallel component implementation workflows

Date: 13 November 2026. Coordinator: gpt-6.1-sol. Worker execution models observed in their start events: gpt-6-luna. Before checkpoints: root `070ad83`; FERME `0fd65d1`.

1. **Holybro Pixhawk 6C hardware (C052):** worker `/root/wheel_tyre_profile`. Owns local-first source review, exact variant/source gate, implementation, native model checks and a verified reusable improvement. Source and job records belong to FERME `cad/work/component-led-2026-11-12/c052-build-01/`; implementation report belongs in this directory's `c052/` subdirectory. Proposed code paths, consumed only if the actual job requires new code: `scripts/pixhawk.py`, `tests/test_pixhawk.py`, `skills/component-cad/references/pixhawk.md`.
2. **Victron smallBMS NG BMS400100300 (C054):** worker `/root/wheel_rim_geometry`. Owns the same complete workflow for the exact BMS. Official STEP and Rev00 drawing have been acquired. This worker holds the first native OCS writer slot. Job records belong to FERME `cad/work/component-led-2026-11-12/c054-build-01/`; implementation report belongs to `c054/`. Proposed reusable paths when required by the actual case: `scripts/small_bms.py`, `tests/test_small_bms.py`, `skills/component-cad/references/small-bms.md`.
3. **Holybro PM02V3 power module (C055):** worker `/root/wheel_hub_interfaces`. Finishes its bounded wheel-interface source followups, then performs the complete module implementation workflow. The module stays a separately identified component from the Pixhawk. Job records belong to FERME `cad/work/component-led-2026-11-12/c055-build-01/`; implementation report belongs to `c055/`. Proposed reusable paths when required: `scripts/power_module.py`, `tests/test_power_module.py`, `skills/component-cad/references/power-module.md`.

## Coordination and completion

1. Three worker slots operate concurrently on source interpretation, implementation preparation, code and checks. The coordinator grants exactly one native OCS writer slot at a time, with an explicit release after the current native job. Current holder: C054 smallBMS worker. Other workers prepare their source-bound work while awaiting that slot.
2. Each worker first checks actual component files and current local evidence. An existing matching completed model is reused with its recorded checks. Required source values retain units, frames, exact variant, source revision and evidence status. Model construction uses existing native CAD and current Python helpers.
3. An iteration produces a source-attributed real component artifact, supported geometric observations, save/readback results and an applied verified skill/procedure/script improvement. Source review completion and complete component implementation are separately reported states.
4. The coordinator reviews original source hashes, source/model identity, numerical observations, affected code checks and actual output files before integrating shared manifest, source register, skill routing and action records. Workers write only their assigned component/code/report paths and perform no commits.
5. CAD and parts data remain in FERME. Reusable Python, skills and usage guidance remain in 3dmodeling. Current concurrent input-index changes and all previously completed models are preserved.
6. The full remaining component plan remains [Component-led CAD and tooling development plan](../../COMPONENT_DEVELOPMENT_PLAN.md). Individual source-gated parts retain their precise feature questions while other unfinished parts progress through the available workers.

## Current procedure links

1. `skills/component-cad/references/pixhawk.md` → [pixhawk](../../skills/cad-ocs-engineering/references/pixhawk.md)
2. `skills/component-cad/references/small-bms.md` → [small bms](../../skills/cad-ocs-engineering/references/small-bms.md)
