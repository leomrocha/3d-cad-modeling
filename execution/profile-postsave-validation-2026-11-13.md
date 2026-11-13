# Validate saved profile topology through structured features

1. Observed caller failure: the Kelly KLS7240N reference (C015) was saved and reopened, but its case driver compared descriptive `encoding` text with the literal `SAB`. The shared reader returned `SAB native body graph` together with topology. The failure was preserved; read-only recovery checked the existing saved document and completed closure, geometry, marker, metadata and file checks.
2. Applied shared procedure: `skills/component-cad/references/profile-reference.md` now uses the returned `features.topology` and existing `feature_checks.closed_body` result for the post-save requirement. Pre-save SAT point checks and reopened body checks have distinct capability requirements. The completed artifact and original request identity are reused after a caller failure.
3. Related prewrite review: the Pilz PNOZ X3 relay (C048) caller initially required SAB before saving. Its reviewed driver uses pre-save point/extent checks and the mandatory structured topology gate after reopen.
4. Case evidence remains in `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c015-build-01/evidence/result-r02.json` and `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c048-build-02/`. Native C015 execution and case-driver correction: gpt-6-luna. Shared procedure integration and caller review: gpt-6.1-sol.

## Current procedure links

1. `skills/component-cad/references/profile-reference.md` → [profile reference](../skills/cad-ocs-engineering/references/profile-reference.md)
