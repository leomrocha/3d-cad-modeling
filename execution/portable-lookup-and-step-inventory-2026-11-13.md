# Portable model lookup and STEP solid inventory

1. Model lookup now resolves stored named roots through an explicit caller map. A missing root raises an error before a new-model decision. Relative job paths use the supplied CAD root; sheet links use the sheet directory.
2. STEP inventory counts MANIFOLD_SOLID_BREP, BREP_WITH_VOIDS and FACETED_BREP once per entity ID, with complex entities listed separately. Shell records retain their topology role.
3. Verification: 15 model-inventory synthetic tests and 5 STEP-inventory synthetic tests passed. These exercise the software contracts.
4. Applied case: `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c036-build-01/` records the SurLok plug source with two manifold solids and one solid containing voids, followed by native import and saved-model checks. Component measurements and evidence remain in FERME.
5. Coordinator: gpt-6.1-sol. STEP helper author: gpt-6-luna. Model-path resolver author: gpt-6.1-sol.
6. Inputs: original STEP bytes or text for entity inventory; external manifest, work records, CAD root, filesystem scan and explicit root map for model lookup. Outputs: read-only inventory records. Geometry, units and original files remain unchanged. Downstream native construction starts only after existing-model identity review; imported-solid count comparison retains independent geometry and placement checks.
