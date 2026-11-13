# Source-bound toroidal reference helper

Observed 13 November 2026. Implementation: `gpt-6-luna`. Coordination, code review and independent test execution: `gpt-6.1-sol`.

1. **Implementation:** `scripts/toroidal_reference.py` accepts externally sourced inside diameter and section diameter in millimetres. It derives major radius as half the inside diameter plus half the section diameter, and minor radius as half the section diameter. The component supplies its source identity, centre, local +Z axis and representation.
2. **Construction route:** four exact circular arcs form the section. The existing OCS Geometry adapter revolves the section through 360 degrees and applies the supplied centre translation. Source metadata uses the installed CADTOOLS_SOURCE application.
3. **Input checks:** pinned source hashes, required dimension features, positive finite dimensions, explicit frame, finite bounds and radius collapse are checked before construction.
4. **Readback contract:** all observed torus surfaces must have the source-derived radii, centre and axis. Extra analytic surface families fail. Body connectivity, exact source metadata and a stable document/geometry revision are checked separately.
5. **Executed tests:** nine synthetic tests passed in the coordinator runtime. They exercise dimension binding, circular profile planning, numerical/source guards, extra or incorrect surfaces, closed-body observations, actual metadata adapter behavior and document-revision binding.
6. **Native integration state:** the helper calls the proposed `native_acis.sab_features(..., allow_tori=True)` extension. The current native reader has no torus option. The component runner preserves the first saved raw record for decoder development and completion of that same model. The synthetic tests substitute analytic reader output; native geometry checks have separate component evidence.
7. **Component applications:** source jobs and native results belong to FERME at `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c071-build-01/` and `c074-build-01/`. Shared code contains no component dimensions.
