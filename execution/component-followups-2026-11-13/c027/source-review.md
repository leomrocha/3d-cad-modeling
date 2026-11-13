# C027 — Orion Jr 2 BMS mechanical source review

**State:** source geometry is available for a manufacturer assembly import; native construction has not started. **Model:** gpt-6-luna. **Date:** 2026-11-13.

## Local gate and retained evidence

The fresh `scripts/model_inventory.py` start gate returned `NEW_MODEL_REQUIRED`; it inspected 45 existing model files and found no C027 model. The input sheet identifies `J2BMS16C`, one BMS per six-module string, and calls for the exact case and connector geometry. Existing battery research records the per-string arrangement; it did not contain a dimensioned BMS case.

The official Orion Jr 2 product page links both the mechanical drawing and model. I downloaded the linked PDF and ZIP unchanged.

- Product page: https://www.orionbms.com/products/orion-jr-2-bms/
- Drawing original: https://www.orionbms.com/downloads/drawings/orionbms_jr_mechanical.pdf
- STEP archive original: https://www.orionbms.com/downloads/drawings/orionbms_jr_mechanical.zip
- PDF: `source/orionbms_jr_mechanical.pdf`, `application/pdf`, 883394 bytes, SHA-256 `584390f934247dd836c753cd70f224f0c7ad0a05a57a480f1025d038b4a7d0b8`, retrieved 2026-11-13 09:46:18 +0100.
- ZIP: `source/orionbms_jr_mechanical.zip`, `application/zip`, 210234 bytes, SHA-256 `0f033e8b79162b6a7dac12e7238bdb07ee0de31fae05ae987506dc94a421a052`, retrieved 2026-11-13 09:46:19 +0100.
- ZIP member `orionjr2_mechanical.step`: 1196380 bytes, CRC-32 `652aa39c`, SHA-256 `80f88a81abee073536f00d28020fd773a552f88810bfd698192e44e9e405fabc`. The exact named member was extracted without archive path traversal.

## Source observations

The member is STEP AP214, file name `11930A.STEP`, authored by SolidWorks 2016. It declares conversion-based `INCH` length units. The existing parser `scripts/step_placements.py::identity_target_placements` successfully parses six explicit placements. Its product representations include `11930A`, `11930AB_J-11930AB`, `11930AC_J-11930AC` and `SCREWS-HL5-8-BR_default`. Solid labels identify `11930A-MASTER` bodies for `SL-64B` and `SL-64C`, plus `Cut-Revolve1`.

The three-page manufacturer drawing is a Polycase product-detail drawing. Its sheets label enclosure alternatives `SL-64`, `SL-64B` and `SL-64C`; their hole and mounting details differ. The drawing uses inch dimensions. Preserve these exact alternatives and compare source labels with imported shape names before feature measurement. Do not silently choose one case.

The official product page establishes the mechanical-file association with the Orion Jr 2 family. The retained model/drawing evidence does not label an internal PCB, external plug coordinates, latches or harness exits. Do not create those from an assumed connector layout.

## Bounded import job and checks

`source-job.json` pins the original files, source identities, inch units and alternatives. Import the manufacturer geometry as source solids; do not rebuild the enclosure. Keep original source frames, read native drawing `INSUNITS`, and apply any uniform conversion scale only after verifying the source inch unit against the native document unit. The existing `step_placements.py` reader supports explicit conversion traversal via `allow_uniform_scale=True` after unit review.

Required native checks: source member and product identity; instance and solid counts; placements against the six STEP frames; case variant labels; drawing-linked envelope and hole geometry for each identifiable case; saved and reopened geometry; component view identity. Record import conversion separately from any later assembly pose. Native import, geometric readback, save/reopen and visual checks have not run because the sole OCS writer slot remains held by C054.

## Alternatives and downstream handoff

1. Preserve the exact manufacturer assembly with every provided case alternative and source placement.
2. Select a case variant only when the exact `J2BMS16C` mapping is supported by source evidence. No individual variant is selected in this record.

Once imported, the enclosure assembly can provide external placement and mounting geometry to the battery layout. Connector, tap harness and temperature/current sensor details require their own exact source surfaces or drawings. This model is not a board-level internal reconstruction.
