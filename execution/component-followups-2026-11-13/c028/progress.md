# C028 SimpBMS board — result

State: REFERENCE_DONE. Detailed component geometry: NEEDS_INPUT. Actual model identity: gpt-6-luna.

The source-supported reference is one cuboid in millimetres, 100 × 50 × 15 mm. X is published width, Y published height, and Z published depth without cables, with lower-corner origin (0,0,0). EVShop identifies the selected SIMP BMS V2.4 / Manual V0.29 variant as configured for BMW i3 with its “no balancing” option and lists these overall dimensions. This is a seller-claimed product envelope, not a detailed PCB or case model. The retained product page, manual and upstream repository archive, exact URLs, retrieval metadata, MIME types, hashes and source locators are recorded in the FERME source review.

The native reference file is `${FERME_ROOT}/engineering/module-development/cad/parts/simp-bms-v24-clearance-reference.dwg`. The unchanged job save remains at `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/simp-bms-v24-clearance-reference.dwg`. Both files are 29,947 bytes with SHA-256 `3af1a94e70bab9df78c34b2b59f3e95d10284847b99ace3e5111cdd3b38d8a79`; canonical copy provenance and native evidence are recorded in `c028-build-01/evidence/final-result.json` and `tooling-link.json`.

Native checks PASS: reopened document 98, geometry revision 10602, handle 7F; extrema [(0,100),(0,50),(0,15)] mm at 1e-7 mm tolerance; one closed body/lump/shell, six planar faces and 24 reciprocal closed coedges. The saved audit contains one 3D solid, zero warnings/errors and zero dropped entities. The pre-save SAT and reopened SAB vertex sets match exactly (eight unique vertices).

Generic tooling addition: `${MODELING_ROOT}/scripts/envelope_reference.py`, with eight passing synthetic tests and procedure at `${MODELING_ROOT}/skills/component-cad/references/envelope-reference.md`. Hashes and runtime dependencies are recorded in FERME `c028-build-01/evidence/tooling-link.json`.

Detailed geometry state remains NEEDS_INPUT for the PCB outline, mounting holes, connector locations and connector bodies. The source repository contains documentation and configuration, with no board CAD or mechanical drawing. Continue detailed geometry only from an original mechanical drawing/CAD or a physical sample with measurements and uncertainty. A Python summary wrapper raised a JSON serialization error after the native build evidence was written; the geometry was not replayed, and the saved file, reopened checks and persistence comparison passed independently.
