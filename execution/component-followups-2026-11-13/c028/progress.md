# C028 SimpBMS board — progress

State: RUNNING. Actual model identity: gpt-6-luna.

Fresh model start gate: `scripts/model_inventory.py` returned `NEW_MODEL_REQUIRED`; zero matching 3D models, zero 2D candidates, and 48 filesystem model files inspected. Existing C028 record was `NOT_STARTED` with no linked CAD output.

Exact source variant: SIMP BMS V2.4 (manual V0.29, Engovis Ltd, dated 2021-06-24), configured in the seller product page for BMW i3; seller option states “no balancing”. EVShop states overall dimensions 100 × 50 × 15 mm, depth without cables. The product page, linked manual and upstream Tom-evnut repository ZIP are preserved unchanged under the FERME job source directory with retrieval metadata and SHA-256 hashes. The upstream archive contains manuals, CAN configuration and installation overview, with no PCB CAD, mechanical drawing or license file. The related eChook board is a different non-drop-in redesign.

Prepared job: `/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/job/job.json`.
Source review and source inventory: `/home/leo/projects/ferme/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/source/source-review.md`.

Supported representation: one overall-envelope reference cuboid, X=100 mm, Y=50 mm, Z=15 mm. No PCB outline radii, mounting holes, connector locations, cable insertion geometry, or cover are supported by the retained source. Native construction is pending because the C027 sibling currently owns the OCS writer. After writer release, create one isolated document, construct one named source-envelope extrusion, check native readback extents against [100, 50, 15] mm, save and reopen, then compare persisted geometry and verify the canonical file hash.

Generic tooling improvement is now implemented and tested at script SHA-256 `8a0b026e218b3a2199dc6e3f3624eb0cbc1b23b03eff747315e476789ce37abf`: parameterized source-pinned envelope preflight and construction, native extrema/topology checking, and SAT/SAB readback. Four synthetic tests pass, including pre-write rejection of invalid zero extent and detailed-body role. Shared code/test/skill paths and hashes are recorded in the FERME `evidence/tooling-link.json`; coordinator commit remains pending.
