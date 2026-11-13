# C028 SimpBMS board — progress

State: RUNNING. Actual model identity: gpt-6-luna.

Fresh model start gate: `scripts/model_inventory.py` returned `NEW_MODEL_REQUIRED`; zero matching 3D models, zero 2D candidates, and 48 filesystem model files inspected. Existing C028 record was `NOT_STARTED` with no linked CAD output.

Exact source variant: SIMP BMS V2.4 (manual V0.29, Engovis Ltd, dated 2021-06-24), configured in the seller product page for BMW i3; seller option states “no balancing”. EVShop states overall dimensions 100 × 50 × 15 mm, depth without cables. The product page, linked manual and upstream Tom-evnut repository ZIP are preserved unchanged under the FERME job source directory with retrieval metadata and SHA-256 hashes. The upstream archive contains manuals, CAN configuration and installation overview, with no PCB CAD, mechanical drawing or license file. The related eChook board is a different non-drop-in redesign.

Prepared source-ready job: `/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/job/job.json`. Existing `component_records.py` gate reports `SOURCE_READY`; output is in `c028-build-01/evidence/source-readiness.json`. Source review and source inventory: `/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/source/source-review.md`.

Supported representation: one overall-envelope reference cuboid, X=100 mm, Y=50 mm, Z=15 mm. No PCB outline radii, mounting holes, connector locations, cable insertion geometry, or cover are supported by the retained source.

The generic tooling improvement is implemented in `scripts/envelope_reference.py` and `skills/component-cad/references/envelope-reference.md`. Its eight synthetic tests pass, including pre-write input rejection and document/handle/revision identity failures. Exact shared code/test/skill hashes and runtime dependencies are in FERME `c028-build-01/evidence/tooling-link.json`.

Native construction remains pending because the C027 sibling currently owns the OCS writer. Planned action after release: create an isolated millimetre document, build one named envelope cuboid using `build_envelope(client, job)`, check the native `[100, 50, 15] mm` spans and closed topology, save to `simp-bms-v24-clearance-reference.dwg`, reopen the saved model, repeat readback and persisted-vertex checks, and record hash and actual document identity. Detailed-component geometry remains a separate input-gated state.
