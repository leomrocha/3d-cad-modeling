# C014 dimension-limit and datum application

**Component:** C014, Curtis 1243-4303 motor speed controller (input proposal)  
**Source:** Curtis Instruments Model 1243 SepEx drawing, document 50045 Rev F, page 6, downloaded source retained in FERME C014 job.  
**Method state:** source-driven clearance-reference construction completed and saved/reopened with feature checks PASS.

The drawing labels overall height `70 Max` and base thickness `6 Max`. These are upper bounds. A packaging clearance reference may place its upper limit at 70 mm above the base-bottom datum; it must retain the source's 70 Max label. The base thickness remains a ≤6 mm source constraint and is not chosen as a nominal solid thickness. The 51 mm leader begins at the base top plane and refers to the terminal projection shown in the side view.

The proposed frame is millimetres: X starts at the top-view leftmost overall extent and increases to the right; Y=0 follows the inferred drawing symmetry axis across the 114 mm end-view width; Z=0 is the base-bottom plane. Printed dimensions remain distinct from derived/traced locations. The mounting pattern uses printed Ø7.14 mm, 16 mm left-pair axial offset, 98 mm pair pitch and 173 mm from the left-pair axis to the right mounting center. Thus the right center's axial coordinate is calculated as 16+173=189 mm from the selected left-edge datum. Centering the 98 mm pair gives y=±49 mm by symmetry convention. The right center's transverse location is traced against the plan-view symmetry axis with ±1.5 px pick uncertainty and is recorded separately from any printed ordinate.

The source job retains a 198×114×70 mm maximum-clearance reference volume and three separate Ø7.14 mm planar mounting-reference circles at z=0. They are inspection references, not fabricated plate, terminal, or bore solids. The 6 mm upper bound is metadata/check evidence. The visible fin and terminal profiles remain source projections until a separate trace-specific representation is reviewed.

The gate checks maximum-reference extents against 198, 114 and 70 mm; checks the 6 mm upper bound as metadata; independently checks three mounting marker diameters and their 16/98/173 mm source relations; and reports raster-derived transverse centering with uncertainty. The seller's 200×100 mm listing dimensions are retained as a separate source claim and are not substituted for the manufacturer drawing.

The generic procedure is in `skills/component-cad/references/dimension-limits-and-datums.md`. This application documents source callouts and datums for C014; it is not a manufacturer validation of exact-suffix mechanical differences.

The retained manufacturer original is `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c014-build-01/source/curtis-1243-rev-f2.pdf`, SHA-256 `c2fb93c5f3f4aa67882503b91f4e92334f448d283ff520955d147063291800ae`, retrieved 2026-11-13 from [Curtis Instruments Model 1243 datasheet](https://cdn.curtisinstruments.com/assets/uploads/datasheets/50045_1243_RevF2.pdf#page=6). The source job is `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c014-build-01/envelope-reference-job.json`; marker inputs are `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c014-build-01/mounting-marker-inputs.json`; retained result is `${FERME_ROOT}/engineering/module-development/cad/checks/component-results/component-led-2026-11-12/c014-build-01/result.json`.

The resulting native file is `${FERME_ROOT}/engineering/module-development/cad/parts/curtis-1243-4303-maximum-clearance-reference.dwg`, SHA-256 `5deadc16ac4e9f1ae0b36f58c1f01222f7a499a2cd83c2d42347ea6c8ec51674`. Actual execution model: `gpt-6-luna`. The first saved-file open request exceeded the bounded query window; the exact original request later returned `completed`. The reopened source-feature, source-metadata, saved-manifest and cleanup receipts all PASS. The finish status applies to this maximum-clearance/reference-circle representation.


The native model passed pre-save and reopened checks: one closed reference solid spans X=0..198 mm, Y=−57..57 mm and Z=0..70 mm; three native Circle entities retain centers (16,−49,0), (16,49,0), and (189,−0.33,0) mm, radius 3.57 mm, +Z normal, and zero thickness. The −0.33 mm transverse location is raster-traced with ±0.9 mm uncertainty. Saved DWG: `${FERME_ROOT}/engineering/module-development/cad/parts/curtis-1243-4303-maximum-clearance-reference.dwg`, SHA-256 `5deadc16ac4e9f1ae0b36f58c1f01222f7a499a2cd83c2d42347ea6c8ec51674`. Retained numeric result: `${FERME_ROOT}/engineering/module-development/cad/checks/component-results/component-led-2026-11-12/c014-build-01/result.json`. The verified save/reopen manifest is one `3D Solid` and three `Circle` entities with zero dropped entities. OCS documents 128 and 129 were closed after checks; Start document 1 remained. Actual execution model: `gpt-6-luna`.

## Current procedure links

1. `skills/component-cad/references/dimension-limits-and-datums.md` → [dimension limits and datums](../skills/cad-ocs-engineering/references/dimension-limits-and-datums.md)
