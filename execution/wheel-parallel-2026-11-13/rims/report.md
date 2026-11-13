# C003/C004 rim geometry source review

**Task state: DONE.** The bounded source review is complete. Runtime model identity is unavailable; the assignment requested `gpt-6-luna`. This output records a partial geometry handoff and the exact component-specific inputs needed before full rim solids can be built.

## Component and model inventory

| ID and readable name | Inventory result | Observed component-specific model |
|---|---|---|
| C003 — Keiyama JA08-700-4T100-02 steel rim | `NEW_MODEL_REQUIRED`; work status `NOT_STARTED`; no attributed model or matching filename candidate among the 43 3D model files scanned | None |
| C004 — Knott 402386.001 steel rim | `NEW_MODEL_REQUIRED`; no attributed model or matching filename candidate among the 43 3D model files scanned | None |

The inventory lists Neugart NGV reducer wheels as different components. Quadboss and HY400 rim DWGs are 2D interface references. No existing model or check was reused for either target rim.

## Source-backed geometry

Continental's agricultural Technical Data Book identifies 7.00I as a **symmetric 5° drop-center rim contour** and gives the section dimensions below. Petlas independently gives the same values and rim diameter.

| Feature | Source value | Definition/status |
|---|---:|---|
| Nominal rim code 8 diameter D | 202.4 mm | Petlas rim-diameter table; source claim |
| Specified section width A | 178 mm | Continental/Petlas 7.00I contour table; source claim |
| Flange height G | 16 mm | Same table; source claim |
| Minimum flange width Bmin | 10 mm | Continental table; source claim |
| Minimum bead-seat width Pmin | 23 mm | Same tables; source claim |
| Contour type | Symmetric 5° drop-center | Continental profile heading and cross-section diagram; source claim |

These dimensions define the published standard contour envelope. They do not define the component's steel gauge, exact radii/curves, rim-well transitions, center-disc shape, welds, bead-seat manufacturing tolerances, or local valve orientation.

The Knott item page identifies product `402386.001` as a steel `7.00I×8` rim and states 4 wheel-bolt holes on 100 mm PCD, ET 0 mm, centre hole 60 mm, D12 stud holes and spherical bolt type. Its listed mass is 3.6 kg. The Keiyama product page identifies `JA08-700-4T100-02` as a 7.00×8 steel rim and states 4 holes, Ø60.0 mm centre, 100.0 mm diagonal centre-to-centre pattern, ET0 with the disc centered, Ø13.5 mm fixing holes, Ø11.3 mm valve hole, and maximum 425 kg at 20 km/h. These are seller-page claims. Keiyama does not name an `I` contour in the inspected product page; applying the generic 7.00I profile to Keiyama is therefore a tyre-contour handoff proposal based on the matching 7.00×8 size, pending rim-source confirmation.

## Construction handoff

Use a wheel-axis local frame in millimetres. Put the origin at the centre of the mounting face; the wheel axis is local Z. Keep the two source sections centered on the ET0 mounting plane when creating the nominal contour envelope. For the 4×100 pattern, place four hole axes at 90° intervals on radius 50 mm in the mounting plane; this radius is calculated from the published 100 mm PCD. Preserve the input sheets' assembly frame X forward, Y left, Z up through an explicit placement transform.

- **C003 Keiyama:** preserve four Ø13.5 mm plain mounting holes, Ø60 mm centre bore, Ø11.3 mm valve aperture, and the separate 7.00×8 section record. The product page does not locate the valve or dimension its mounting disc.
- **C004 Knott:** preserve four D12 holes and spherical bolt-seat side as a distinct fastener-seat variant, plus Ø60 mm centre bore. The product page does not give the spherical-seat radius/profile, countersink depth, or seat-side section.
- **Both:** the standard section values above support the nominal 7.00I contour envelope. The exact pressed steel center disc, weld geometry, gauge, dish transition, and detailed section radii require a dimensioned product drawing/CAD source or measurement from the actual rim. Keep these surfaces as named `NEEDS_INPUT` features; do not replace them with a torus/box or guessed disk.

Source page photographs are visual product evidence only. They do not establish metric section, dish, wall, weld or seat dimensions. No downloaded source originals were created in this pass; inspected web sources are recorded with URL, observation time and content type in `sources.csv`.

## Source records

| Source | URL | Evidence captured |
|---|---|---|
| Continental, *Technical Data Book — Agriculture*, p. 84 | https://prod.continental-tires.com/content/dam/conti-tires-cms/continental/b2b/agriculture/CO_TechnicalDataBook_PDF_EN_CS.pdf.coredownload.pdf | Manufacturer PDF inspected 2026-11-13 08:26 UTC; 7.00I section table and diagram |
| Petlas, *Tire Guide — Industrial & OTR Tires* | https://www.petlas.com/en/powerguid/ | Manufacturer web page inspected 2026-11-13 08:26 UTC; 7.00I contour and code-8 diameter tables |
| Knott, *Rim 7.00Ix8*, item 402386.001 | https://www.knott-trailer-shop.com/rim_7_00ix8.html | Exact product page inspected 2026-11-13 08:26 UTC |
| Keiyama, JA08-700-4T100-02 | https://www.keiyama.eu/jante-nue-agraire-grise-700x8-et0-4-trous-60x100.html | Current exact-product page inspected 2026-11-13 08:26 UTC; supplied historical URL preserved in `sources.csv` |
