# Reusable modeling-tool improvements

Date: 13 November 2026. Coordinator/reviewer: gpt-6.1-sol. Worker model observed in all three start events: gpt-6-luna.

## Source-defined reference geometry

[envelope_reference.py](../scripts/envelope_reference.py) consumes an external source-pinned job, dimensions, units, frame, origin and representation. It preflights values before loading the geometry adapter, reuses the existing native extrusion/selection guard and verifies the requested handle, solid type, document and stable geometry revision. Eight synthetic tests pass. The applied case result stays in FERME (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c028-build-01/evidence/final-result.json`), with source metadata, geometry observations and the exact shared-code hash. The repeated envelope operation was first exercised in the earlier mounting-reference job; its existing paths remain available for the separately owned split.

## Image calibration and uncertainty

[calibrated_trace.py](../scripts/calibrated_trace.py) accepts source-image points, pixel origin, signed per-axis scales and point/origin/scale uncertainty. Its worst-case coordinate bound includes the product cross-term: abs(scale)*u_delta + abs(delta)*u_scale + u_delta*u_scale. The review identified the missing cross-term in the first implementation; the corrected function includes endpoint-combination tests and rejects nonfinite computed results. Six synthetic tests pass. Actual drawing points, source original and case recipe remain in FERME (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c042-build-01/records/geometry-recipe.json`).

## Assembly drawing units

[assembly_units.py](../scripts/assembly_units.py) plans uniform root transformations from explicit external unit definitions. It scales insertion coordinates and all three scale fields together, preserves orientation/internal geometry and validates every root before returning a plan. It rejects arrays, reflections, nonuniform/nonfinite transforms, duplicate or empty handles and invalid unit ratios. Review added a NaN-transform guard. Six synthetic tests pass. The applied read-only check against a retained actual root and the field-specific historical comparisons stay in FERME (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c027-build-01/shared-tool-check-assembly-units.json`).

## Saved geometry

The existing [SAT/SAB comparator](../scripts/small_bms.py) reuses the native body reader and supported SAT point parser. Three recorded-case tests pass, including an altered coordinate and an unsupported transform. Independent review of the new case compared retained vertex sets and corrected source matrices; the receipt is in FERME (`${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c054-build-01/coordinator-saved-checks.json`). These checks describe point-set persistence and retained topology; curved surfaces have their own measurement requirements. The existing comparator/test paths and pre-existing case fixtures remain intact for the split coordinator.

## Ownership and integration

1. New reusable algorithms, synthetic tests and general procedures are in 3dmodeling. New component sources, recipes, models, measurements, execution records and real-case fixtures are in FERME.
2. Active historical paths are preserved. The preparation documents and proposed migration manifest remain under their current owner. This batch performs no migration or import relocation.
3. The [shared skill](../skills/component-cad/SKILL.md) routes to the three new generic procedures. Each FERME result identifies its actual shared-file hash; the coordinator records the result commit in the component checkpoint.
