# C001 tyre profile and rim-interface handoff

Date: 13 November 2026, Europe/Paris  
Component: C001 — Trelleborg T539, 18x8.50-8, 6PR, tube type  
Task status: DONE for bounded source research  
Component state: NEEDS_INPUT for a detailed tyre section model  
Actual model identity: unavailable

## Existing-model gate and source reuse

The required C001 start gate returned `NEW_MODEL_REQUIRED`: zero attributed 3D models, zero unlinked candidates, zero 2D references, and 43 project model files inspected. Existing `c001-build-01/readiness-r02.json` remains the active readiness record. It identifies the exact tyre bead and section profile as the blocking input.

The existing source review already checked the exact manufacturer row for 18x8.50-8, 6PR, T539, Farming: Trelleborg Technical Manual, PDF page 111, printed page 221. Manufacturer values are OD 466 mm ±1.5%, section width 222 mm ±2%, rim 7.00I, permitted rim 6.50-8, rolling circumference 1384 mm ±2.5%, maximum pressure 2.8 bar, and maximum load 475 kg at 30 km/h. Existing records identify the construction as tube type and tube 6.00-9TR15. The manual row has no tyre section coordinates, bead profile, bead-seat dimensions, or tread dimensions. The original manual, brochures, T539 family photo, product-page snapshot and retrieval/hash records remain in `c001-build-01/source-review/`; the 4PR tubeless row is excluded.

## Standardized mating rim contour

The Trelleborg manual calls for rim contour 7.00I and permits 6.50-8. Trelleborg therefore supplies the nominal mating contour label for C001.

1. Continental Agricultural Databook, printed page 87, section **5° Drop-Center Symmetric**, row **7.00I**: specified width A = 178 mm; flange height G = 16 mm; minimum flange width Bmin = 10 mm; minimum bead-seat width Pmin = 23 mm. The diagram and field definitions are adjacent to the table. Direct source: [Continental Agricultural Databook PDF](https://www.continental-tyres.co.uk/content/dam/conti-tires-cms/continental/b2b/agriculture/Continental__AG__Databook__A4__EN__copy.pdf.coredownload.pdf).
2. Petlas Industrial & OTR Tire Guide, **Rims / Semi-drop & divided rims** and rim-diameter table: 7.00I width A = 178 mm; G = 16 mm; Pmin = 23 mm; nominal rim code 8 diameter D = 202.4 mm. Direct source: [Petlas Tire Guide](https://www.petlas.com/en/powerguid/).
3. The source convention locates the tyre/rim axis at the centre plane. For a source-ready interface record, use nominal radial seat reference D/2 = 101.2 mm and nominal rim width A/2 = 89 mm each side of the centre plane. These two half-values are arithmetic transformations of cited source values, not additional manufacturer dimensions.
4. The Continental handbook extraction appears in another Continental-hosted databook rendering with Bmin = 8.5 mm. The linked PDF used above states 10 mm on printed page 87. Keep the variant discrepancy in source notes; the directly opened PDF table supplies the 10 mm value for this handoff.

The published 7.00I contour dimensions specify the mating rim profile class and principal dimensions. They do not specify the T539's rubber bead cross-section or the individual rim's complete weld, dish, fastener-seat, bead-flange radii and drop-well details. The rim agent has independently located the same primary manufacturer contour sources and is checking the corresponding C003/C004 rim geometry.

## Geometry contract for the next CAD writer

Component-local frame from the C001 input sheet: millimetres; origin at wheel-axis centre on the tyre mid-plane; local X along the wheel rotation axis. The assembly placement frame remains X forward, Y left, Z up. Do not change this contract.

Source-backed envelope inputs: outside diameter 466 mm ±1.5% gives nominal outer radius 233 mm; section width 222 mm ±2% gives nominal axial half-width 111 mm. Source-backed rim interface: nominal 7.00I-8 diameter 202.4 mm gives a reference radius 101.2 mm; rim specified width 178 mm gives a half-width 89 mm; 5° symmetric drop-centre, G 16 mm, Bmin 10 mm, Pmin 23 mm. Store the named source values and their uncertainty separately. Do not treat rounded D/2 and A/2 coordinates as measured T539 bead points.

The manufacturer data and standard identify no cross-section curve joining the 202.4 mm bead-seat reference to the 466 mm OD / 222 mm section envelope. The current Trelleborg image is a family-level three-quarter product image with no size association; it cannot provide calibrated C001 section coordinates. A toroidal section would add unsupported bead and sidewall radii. Keep the envelope dimensions and rim reference independently checkable; retain `NEEDS_INPUT` for a detailed T539 carcass/bead section pending an exact size-specific dimensioned profile or calibrated side/section image.

## Source records and acquisition status

1. **Existing downloaded original:** Trelleborg Technical Manual; exact URL and supplied URL preserved in `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/acquisition.json`; retrieved 13 November 2026, `application/pdf`, SHA-256 `f9b0296a673b0fe14ca3649953a0feaa57963af88b23a58aa59350dfacf39cec`.
2. **Web inspection:** Continental Agricultural Databook, exact PDF URL above; printed p.87 and web-extracted table/diagram inspected 13 November 2026. Original PDF bytes were not downloaded in this stage.
3. **Web inspection:** Petlas Tire Guide, exact URL above; rim contour and nominal diameter tables inspected 13 November 2026. Original page bytes were not downloaded in this stage.
4. Shell retrieval of the Petlas page failed at DNS resolution (`Could not resolve host`); this report labels the sources as web-inspected and does not claim local original files, content types, retrieval timestamps, or hashes for them.
5. Requested external research model was gpt-6-luna; actual runtime identity unavailable. The actual executing model identity is also unavailable.

## Handoff

The coordinator can now consume the source-backed **7.00I-8 rim contour** when the C003/C004 rim agent delivers its individual wheel geometry and checks. Recommended next CAD operations are: (1) establish the source-defined 7.00I-8 interface from that rim geometry, preserving A/G/Bmin/Pmin and the reference D; (2) set the C001 tyre envelope OD and section-width checks in its existing local frame; (3) leave the rubber bead and section face unresolved in the detailed solid until a size-specific source image/drawing is available. Do not build a toroidal carcass or label an envelope shell as an exact tyre.

## Local records consulted

- `${FERME_ROOT}/engineering/module-development/cad-inputs/c001-trelleborg-t539-tyre.md`
- `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/readiness-r02.json`
- `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/acquisition.json`
- `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c001-build-01/source-review/source-review.md`
- `${MODELING_ROOT}/skills/component-cad/references/existing-model-start-check.md`
- `${FERME_ROOT}/skills/cad-construction/SKILL.md`
