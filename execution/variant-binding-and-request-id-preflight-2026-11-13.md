# Source variant binding and request-ID preflight

Date: 2026-11-13. Coordinator model: gpt-6.1-sol. Component execution model: gpt-6-luna.

1. **Applied source procedure:** `skills/component-cad/references/source-variant-tables.md` now records source-family identity, revision, view and optional configuration beside each dimension. The Albright contactor case supplied the concrete distinction between two manufacturer drawing revisions and a separate optional configuration. Its source packet is `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c034-build-01/envelope-reference-job.json`.
2. **Applied image association:** the same procedure now records a multi-product page's exact dimension row separately from its gallery image association. The Altec bracket case used the existing exact-cell selector and retained page variant data plus inspected image pixels. Evidence is `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c039-build-01/source/variant-row-selection.json`. No HTML parser was added.
3. **Observed runtime error:** the Altec case created its isolated document and reference solid, then reached the installed client's request-ID byte limit before sending its complete-source-metadata request. The component agent retained that document and its journal for completion through the same geometry. Component failure/recovery receipts belong in FERME.
4. **Applied Python improvement:** `scripts/envelope_job_runner.py` checks the full generated metadata request ID during job resolution. The limit is 128 UTF-8 bytes, as read in `${FERME_ROOT}/skills/cad-construction/scripts/cadtools/runtime.py`. The checked suffix is the longest geometry-name-based suffix used by the rectangular-envelope route. The caller receives a preflight error before OCS discovery or document creation.
5. **Verification:** the new regression test allows a generated ID of exactly 128 bytes and rejects an equal-character-count name containing a two-byte character that exceeds the byte limit. It asserts that the fake OCS helper receives no calls on rejection. The first test invocation used the fixture's default job path instead of its oversized alternate path and failed; the test was corrected to pass the alternate path. The final runner suite passed all 11 tests. These are synthetic software tests.
6. **Skill validation:** the component skill validator passed after the variant procedure additions. The source association was inspected from retained component evidence. The running Altec job retains its original execution history and uses its component recovery route.

The generic procedure contains source association rules and the runner contains a label-length check. Product dimensions, original downloads, geometry and native receipts remain in FERME.

## Current procedure links

1. `skills/component-cad/references/source-variant-tables.md` → [source variant tables](../skills/cad-ocs-engineering/references/source-variant-tables.md)
