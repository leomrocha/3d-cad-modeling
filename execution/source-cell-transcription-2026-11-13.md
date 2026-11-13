# Preserve malformed dimension cells and reviewed ordered values

1. Applied case: Tyro Indus1S handheld stop remote (C056). The retained manufacturer table labels its dimensions L × W × H, while the cell reads `120 x 60 30 mm`. The reviewed interpretation supplies length 120 mm, width 60 mm and height 30 mm. The raw text, header and ordered interpretation remain separate in the FERME source record.
2. Shared improvement: `skills/component-cad/references/source-variant-tables.md` now requires raw-cell preservation, its header/location and the evidence for each interpreted value before geometry. This is a procedure change; the existing envelope constructor and table selector are reused.
3. Applied result: the existing native reference envelope uses local X=length, Y=width and Z=height, with origin [-60,-30,0] mm. Its retained geometry/metadata/persistence checks and saved file are reused. Source review and native execution: gpt-6-luna; source-table interpretation review and procedure integration: gpt-6.1-sol.
4. Source: https://www.tyroremotes.no/wp-content/uploads/2016/12/Productblad-Indus-1S-EN-1.1.pdf . Retained original `${FERME_ROOT}/engineering/module-development/cad/work/component-led-2026-11-12/c056-build-01/source/Productblad-Indus-1S-EN-1.1.pdf`, SHA-256 `a0b08500d3e3f86f525cbe3e6c85e88dc2a3dff084b8ff2bded384869c722f3c`. Its table/header evidence supports the ordered reference-envelope input, with manufacturing tolerances separate from numerical CAD check tolerance.

## Current procedure links

1. `skills/component-cad/references/source-variant-tables.md` → [source variant tables](../skills/cad-ocs-engineering/references/source-variant-tables.md)
