# Source-bound toroidal reference helper

Observed 13 November 2026. Implementation: `gpt-6-luna`. Coordination, code review and independent test execution: `gpt-6.1-sol`.

1. **Implementation:** `scripts/toroidal_reference.py` accepts externally sourced inside diameter and section diameter in millimetres. It derives major radius as half the inside diameter plus half the section diameter, and minor radius as half the section diameter. The component supplies its source identity, centre, local +Z axis and representation.
2. **Construction route:** four exact circular arcs form the section. The existing OCS Geometry adapter revolves the section through 360 degrees and applies the supplied centre translation. Source metadata uses the installed CADTOOLS_SOURCE application.
3. **Input checks:** pinned source hashes, required dimension features, positive finite dimensions, explicit frame, finite bounds and radius collapse are checked before construction.
4. **Readback contract:** all observed torus surfaces must have the source-derived radii, centre and axis. Extra analytic surface families fail. Body connectivity, exact source metadata and a stable document/geometry revision are checked separately.
5. **Executed tests:** nine synthetic tests passed in the coordinator runtime. They exercise dimension binding, circular profile planning, numerical/source guards, extra or incorrect surfaces, closed-body observations, actual metadata adapter behavior and document-revision binding.
6. **Native integration:** decoder revision `61f3dc4` supplies `native_acis.sab_features(..., allow_tori=True)`. The G-140 application used helper `a359449` and this decoder on its existing saved model. Four analytic surface patches, source metadata, connected topology and recovered save/reopen checks passed; owned documents 146 and 147 closed after those checks. The component result is retained in FERME at `c071-build-01/final-readback-check-r01.json`.
7. **Component applications:** source jobs and native results belong to FERME at `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c071-build-01/` and `c074-build-01/`. Shared code contains no component dimensions.

**Executed application:** The AS568-261 nominal O-ring application passed its analytic surface, source metadata, connected topology and recovered persistence checks. Its saved and construction documents closed; helper `a359449` and decoder `61f3dc4` were applied. Evidence: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c074-build-01/result.json`.
