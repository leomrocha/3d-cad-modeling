# C052 — Holybro Pixhawk 6C mechanical reference

**Overall C052 state: NEEDS_INPUT.** The source-dimensioned reference model is DONE. The detailed case exterior and connector geometry remain NEEDS_INPUT. **Actual model identity: gpt-6-luna.**

## Delivered model

Canonical native file: ${FERME_ROOT}/engineering/module-development/cad/parts/holybro-pixhawk-6c-mechanical-reference.dwg (`${FERME_ROOT}/engineering/module-development/cad/parts/holybro-pixhawk-6c-mechanical-reference.dwg`)

SHA-256: `1431c006fa758a4978533b52c398e6f4a9e5d52113d713fd14ebbd75e491de6f` (31,483 bytes). The source save is retained at ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/holybro-pixhawk-6c-mechanical-reference.dwg (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/holybro-pixhawk-6c-mechanical-reference.dwg`). The canonical file is a byte-identical copy of that already saved and reopened file.

The model contains one rectangular source-dimension clearance envelope and four blind nominal M2 mounting-thread reference cylinders. Its local frame places the rear mounting-face center at origin, X along the 84.8 mm length, Y along the 44 mm width, and +Z through the 12.4 mm thickness. The four holes are centered at (X,Y)=(±30,±16) mm and extend 6 mm into +Z. The 2 mm cylinders represent the nominal M2 designation; they do not model thread form, tap-drill size, or thread capacity. C055 PM02 V3 is a separate component.

The cutters start 0.01 mm outside the mounting face to cross the source face during the Boolean cut; this is an explicit CAD construction allowance, not a Holybro dimension. The measured bottom planes remain at the source-defined 6.00 mm depth.

## Source evidence

Holybro’s [Pixhawk 6C Dimensions drawing](https://docs.holybro.com/autopilot/pixhawk-6c/dimensions) was downloaded unchanged to ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/source/holybro-pixhawk-6c-dimensions.jpg (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/source/holybro-pixhawk-6c-dimensions.jpg`). MIME type `image/jpeg`; retrieval `2026-11-13 08:34:50 UTC`; SHA-256 `5797024d092cb8bb4f429412c5c84e179a4b65cb2799b848b9d9e56772956453`.

The drawing labels the case 84.8±0.1 × 44±0.1 × 12.4±0.1 mm. It shows four M2 threaded holes on a 60±0.1 × 32±0.1 mm pattern, with 6 mm thread depth. Holybro’s [Pixhawk 6C Technical Specification](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) lists aluminum-case mass 59.3 g and plastic-case mass 34.6 g. The dimension drawing does not identify the case material or SKU.

Holybro’s [Pixhawk 6C Download page](https://docs.holybro.com/autopilot/pixhawk-6c/download) lists “Pixhawk 6C Case CAD 3D File.” The published file endpoint redirected and returned HTTP 404; response headers are retained in ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/source/holybro-pixhawk-6c-case.headers.txt (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/source/holybro-pixhawk-6c-case.headers.txt`). No CAD original was acquired. Holybro’s [Pixhawk 6C product page](https://holybro.com/products/pixhawk-6c?variant=42420293533885) lists both Plastic and Aluminum controller variants. Pixhawk 6C Mini geometry was excluded because it is a separate product.

The original drawing also depicts edge bevels, stepped profiles, and connector-window outlines. Those visual details are not included in the reference envelope. A detailed case model requires the manufacturer CAD file or additional dimensioned case and connector geometry. The present model makes no claim about internal PCB geometry, connector internals, shell construction, or case material.

## Checks and implementation

The actual component start gate was run before construction: `NEW_MODEL_REQUIRED`; zero matching 3D models, zero unlinked candidates, zero 2D references across 43 CAD-root files.

OCS created an isolated working document 93, saved the model, and reopened it as document 94. Active document 92 was preserved. The reopened audit reports one 3D Solid, zero errors, and zero warnings. Independent post-reopen checks pass for:

- Envelope extrema: X [−42.4,42.4], Y [−22,22], Z [0,12.4] mm.
- Four nominal M2 axes at (±30,±16) mm.
- Four blind-hole bottom planes at Z=6 mm.
- One closed connected body.

The final SAB read used the already-present `${NATIVE_READER_ROOT}` environment; no package was installed. The first post-reopen parser invocation used the system Python without `ezdxf` and stopped before reading geometry. The next read used the existing SAB-reader environment and all saved-model checks passed; no CAD operation was replayed.

The implementation is [${MODELING_ROOT}/scripts/pixhawk.py](../../../scripts/pixhawk.py). Its preflight rejects duplicate required features, a mount pattern outside the envelope, missing or invalid construction overrun, and invalid inputs before creating any geometry. The nine tests in [${MODELING_ROOT}/tests/test_pixhawk.py](../../../tests/test_pixhawk.py) pass. The applied component-specific procedure is [${MODELING_ROOT}/skills/component-cad/references/pixhawk.md](../../../skills/component-cad/references/pixhawk.md). The exact build driver and native records are retained in the C052 job directory; the component work index was not changed.

Detailed records: ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/result.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/result.json`), ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/save-reopen.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/save-reopen.json`), and ${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/progress.json (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c052-build-01/progress.json`).
