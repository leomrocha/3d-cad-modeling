# 40 × 40 × 3 mm square tube corner research — P01 and P02

**Observation date:** 12 November 2026
**Scope:** Corner profile and applicable product-standard evidence for FERME proposed main-frame longitudinal rail P01 (600 mm) and crossmember P02 (260 mm). Research only; no CAD edit or material-grade selection.

## Finding

For a 40 × 40 × 3 mm **cold-formed welded structural hollow section using the EN 10219-2:2019 corner and property conventions**, the standard distinguishes two corner values. The applicable delivery-condition requirements belong to the corresponding Part 1; the corner evidence below combines the readable [EN 10219-2:2019 sample](https://cdn.standards.iteh.ai/samples/38063/99682514fcf94faabd079f41b1a7854e/SIST-EN-10219-2-2019.pdf) for Clause 6.2 and Table 3 with the indexed Annex A.3 excerpt of the [supplier-hosted standard PDF](https://www.botopsteelpipes.com/wp-content/uploads/2024/08/EN-10219-2-2019.pdf) for the calculation radii:

| Quantity | Standard basis | Calculation at T = 3 mm | Meaning |
|---|---|---:|---|
| External corner profile tolerance | EN 10219-2:2019 Table 3, T ≤ 6 mm: 1.6T–2.4T | 4.8–7.2 mm | Permitted measured external profile range; the standard says sides need not be tangent to the corner arcs. It is not one exact manufactured radius. |
| External radius used for nominal section properties | EN 10219-2:2019 Annex A.3, T ≤ 6 mm: rₒ = 2.0T | 6.0 mm | Nominal calculation convention. |
| Internal radius used for nominal section properties | EN 10219-2:2019 Annex A.3, T ≤ 6 mm: rᵢ = 1.0T | 3.0 mm | Nominal calculation convention. |
| Manufactured internal corner | EN 10219-2:2019 Clause 6.2 | Profile not numerically set | Internal corners shall be rounded; the note says the internal corner profile is not specified. |

For a 40 × 40 × 3 mm **hot-finished structural hollow section using the EN 10210-2:2019 corner and property conventions**, the nominal section-property values differ. The applicable delivery-condition requirements belong to the corresponding Part 1; the corner evidence below is from [EN 10210-2:2019](https://cdn.standards.iteh.ai/samples/38061/b2cb736a37f94d2f8a72c739a042aa44/SIST-EN-10210-2-2019.pdf):

| Quantity | Standard basis | Calculation at T = 3 mm | Meaning |
|---|---|---:|---|
| External corner profile tolerance | EN 10210-2:2019 Table 2: 3T maximum at each corner | 9.0 mm maximum | Permitted measured external profile limit. Optional order condition 2.2 allows a maximum of 2T at each corner; it is not stated as the default. |
| External radius used for nominal section properties | EN 10210-2:2019 Annex A.3: rₒ = 1.5T | 4.5 mm | Nominal calculation convention. |
| Internal radius used for nominal section properties | EN 10210-2:2019 Annex A.3: rᵢ = 1.0T | 3.0 mm | Nominal calculation convention. |
| Manufactured internal corner | EN 10210-2:2019 Clause 6.2 | Profile not numerically set | Internal corners shall be rounded, with the stated exception for the corner containing a weld in certain EW sections; note says profile is not specified. |

The different external values are not contradictory within either edition: a tolerance limit describes permitted manufactured geometry; Annex A defines a representative nominal geometry for section-property calculation. The same nominal inside radius of 3 mm appears in both calculation bases, but the standards do not thereby certify the supplier's actual inner radius.

The current supplier record identifies Perrin / Fers & Métaux item **040819**, sold as “TUBE CARRE 40X40X3”. The [seller page](https://www.fers-metaux.com/mes-produits/fer/tubes-carres/3004g-tube-carre) lists exterior dimensions and stock/cut information but does not state a manufacturing process, EN product standard, steel grade, or measured corner radius. These EN 10219/EN 10210 values therefore provide standards-based reference conventions; supplier conformity and actual product geometry remain unestablished by the listing.

## Standard scope and edition evidence

- The AFNOR catalogue identifies [NF EN 10219-2](https://www.boutique.afnor.org/fr-fr/norme/nf-en-102192/profils-creux-de-construction-soudes-formes-a-froid-en-aciers-partie-2-tole/fa177343/83616), May 2019, as “Norme en vigueur”, with EN 10219-2:2019 as its European parent. It says Annex A provides section-property calculation formulas and Annex B tabulates a limited set of common sizes. The delivery-condition requirements are in the corresponding Part 1; this report's corner calculations cite Part 2 only.
- [EN 10210-2:2019](https://cdn.standards.iteh.ai/samples/38061/b2cb736a37f94d2f8a72c739a042aa44/SIST-EN-10210-2-2019.pdf) contains hot-finished section tolerances, dimensions and section properties. It applies to the section-property branch here; delivery-condition requirements are in the corresponding Part 1. The inspected Part 2 text says it supersedes EN 10210-2:2006.
- The catalogue entries viewed for the delivery-condition Parts 1 showed 2026 draft texts, not evidence that either Part 1 was edition 2019. [NEN's EN 10210-1:2026 draft entry](https://www.nen.nl/nen-en-10210-1-2026-ontw-en-350480) is dated 1 April 2026 and says the scope includes hot-formed product and cold-formed product subsequently heat-treated above 580 °C. [AENOR's DIN EN 10210-1:2026-03 entry](https://tienda.aenor.com/p/norma-din-en-10210-1-2026-03-399626373) identifies a German/English prEN text intended to replace DIN EN 10210-1:2006 and DIN EN 10210-3:2020. These Part 1 records do not change the corner calculations from the 2019 Part 2 documents above. No evidence was found that a replacement Part 2 edition was in force on 12 November 2026.
- NEN's [2026 draft catalogue note](https://www.nen.nl/nen-en-10210-1-2026-ontw-en-350480) says cold-formed and hot-finished section properties in EN 10219-2 and EN 10210-2 are not equivalent even where grades have equivalent mechanical properties. This supports keeping the Part 2 property bases separate.
- The seller page calls the item tube carré and gives dimensions outside, price, mass and cut/stock details. Those seller statements do not identify whether the product is structural, welded or seamless, cold formed or hot finished, standard-conforming, or a particular grade. Do not infer those attributes from the square form or listed mass.

## CAD registration routes supported by this research

1. **Proposed nominal calculation/reference model:** A CAD representation labelled **“EN 10219 nominal section-property geometry, Rₒ 6 mm / Rᵢ 3 mm; supplier dimensions source, process/conformity not asserted”** is a defensible proposed reference representation. EN 10219-2:2019 Annex A.3 provides this calculation basis; the label states that basis and does not claim item 040819 was manufactured to EN 10219. Keep the 4.8–7.2 mm external tolerance evidence separate from the 6 mm nominal calculation radius. Keep Rᵢ=3 mm labelled as the calculation convention because Clause 6.2 leaves the manufactured inner profile unspecified. This remains a research proposal, not an author decision or CAD change.
2. **Supplier-neutral reference geometry:** If the intended drawing is meant to depict measured/known product geometry, retain each outside corner as a named unknown/profile parameter until measurement rather than treating a nominal calculation convention as actual. Keep the inside-corner profile separately unidentified. The seller page alone cannot provide that product-detail geometry.
3. **Cold-formed structural nominal model:** If stock documentation or the supplier confirms the applicable EN 10219 delivery-condition standard, use EN 10219-2 Annex A nominal section-property profile, **rₒ = 6.0 mm and rᵢ = 3.0 mm**. Record the separate external permitted profile interval **4.8–7.2 mm** as tolerance evidence, not as a guaranteed actual value. The inner 3 mm remains a calculation convention, not an acceptance limit.
4. **Hot-finished structural nominal model:** If procurement evidence instead confirms the applicable EN 10210 delivery-condition standard, use **rₒ = 4.5 mm and rᵢ = 3.0 mm** from EN 10210-2 for the nominal section-property profile. Record the default external maximum as 9 mm and record Option 2.2's 6 mm maximum only if the order explicitly invokes that option.
5. **Measured product model:** For actual-product fit or detailed fabrication geometry, obtain a piece from the identified supply batch and measure its section at a location meeting the relevant standard's method; preserve measurement locations and results as measured evidence. Under EN 10219-2 Clause 7.7, the manufacturer can measure external profile with a radius gauge or corner offsets C1/C2. The seller's current item page does not provide these measurements.

These routes provide a source-backed way to define a nominal CAD shape without treating aesthetic preference as the rule. The structural-standard routes remain conditional on identifying the supplied process/standard. The nominal radii should not be used as manufacturing inspection limits. P01 and P02 have the same proposed cross-section, so the same cross-section evidence applies to both; their cut lengths remain separate inputs from their existing CAD sheets.

## Calculation record

- Input: nominal wall thickness **T = 3 mm**, from the P01/P02 proposal and seller item designation.
- EN 10219-2:2019 tolerance: Table 3 says for **T ≤ 6 mm**, external profile = **1.6T to 2.4T**. Arithmetic: 1.6 × 3 = **4.8 mm**; 2.4 × 3 = **7.2 mm**.
- EN 10219-2:2019 nominal section calculation: Annex A.3 gives **rₒ = 2.0T**, **rᵢ = 1.0T** when **T ≤ 6 mm**. Arithmetic: 2.0 × 3 = **6.0 mm**; 1.0 × 3 = **3.0 mm**.
- EN 10210-2:2019 nominal section calculation: Annex A.3 gives **rₒ = 1.5T**, **rᵢ = 1.0T**. Arithmetic: 1.5 × 3 = **4.5 mm**; 1.0 × 3 = **3.0 mm**.
- EN 10210-2:2019 external profile tolerance: Table 2 gives **3T maximum** = **9.0 mm**. Option 2.2 is a purchaser-specified maximum **2T** = **6.0 mm**.
- Units are millimetres throughout. All calculated radii above are calculations from standard formulas and nominal T, not measured product results.

## Existing project records consulted

- [Main frame longitudinal rail input sheet (P01)](/home/leo/projects/ferme/engineering/module-development/cad-inputs/p01-main-frame-longitudinal-rail.md) — P01 proposed 40 × 40 × 3 mm tube, 600 mm cut length; grade follows actual stock record.
- [Main frame crossmember input sheet (P02)](/home/leo/projects/ferme/engineering/module-development/cad-inputs/p02-main-frame-crossmember.md) — P02 proposed 40 × 40 × 3 mm tube, 260 mm cut length between rails.
- [Frame, hitch and supports research](/home/leo/projects/ferme/research/base-component-completion-2026-11-12/02-frame-hitch-supports.md) and [frame source manifest](/home/leo/projects/ferme/research/base-component-completion-2026-11-12/sources-frame/manifest.tsv) — identify the supplier page/item 040819 as prior seller-page observation and list the original URL; do not contain process or standard evidence for the tube.
- The frame source manifest records the seller page's 19.8 kg listing for a 6 m bar. This mass listing is not used to identify a standard or process.

## Source/claim status

Direct observations from the supplier and AFNOR/NEN catalogue pages are source claims. EN 10219-2 Clause 6.2 and Table 3 were visible in readable sample-PDF output; its Annex A.3 formulas were visible in indexed standard excerpts. EN 10210-2 Annex A.3 formulas were visible in the sample-PDF search-result excerpt. The source manifest identifies each observation method and the PDF-access outcomes. The equations above are calculations from those formulas. CAD routes are proposals. No tube was physically measured, no conformity certificate was inspected, and no CAD/control operation was performed. Actual model identity: unavailable in this execution context.

## Research execution

1. **Research agent:** requested model `gpt-6-luna`; actual runtime identity unavailable to the agent.
2. **Coordinator:** `gpt-6.1-sol`; reviewed returned source observations, source locations, arithmetic and supplier applicability.
3. **Related action:** [Select a supported solid feature route (CAD-10-A01)](/home/leo/projects/3dmodeling/research/action-audit/point-03-operations.json). The section evidence applies to the proposed main frame longitudinal rail and crossmember.
4. **Registered alternatives:** [Cold-formed, hot-finished and measured-stock geometry proposals](/home/leo/projects/3dmodeling/research/action-audit/ideas.json), COMP-I08–COMP-I10.
