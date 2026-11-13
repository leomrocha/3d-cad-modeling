# Component source coverage and ownership

Date: 12 November 2026. Status: **planning reference**. Model: gpt-6.1-sol.

1. The authoritative part index (`${FERME_ROOT}/engineering/module-development/cad-inputs/README.md`), 103-part manifest (`${FERME_ROOT}/engineering/module-development/cad-inputs/parts.json`) and geometric dependency order (`${FERME_ROOT}/engineering/module-development/cad-inputs/dependency-order.tsv`) remain in FERME.
2. The [component-led development plan](../COMPONENT_DEVELOPMENT_PLAN.md) references those existing records. Parts catalogue data, future databases, component CAD and build evidence belong to FERME.
3. This project owns reusable skills, Python helpers/tests, action definitions and instructions/interfaces for accessing FERME data when it exists. It records tooling improvements linked to the actual FERME component cases.
4. Proposed first jobs: Main frame longitudinal rail (P01), then dependent Main frame crossmember (P02). Each iteration produces the checked CAD artifact and an applied verified improvement here.

## Source groups

| Existing FERME input group | Sheets |
| --- | ---: |
| drive | 25 |
| caster | 10 |
| frame | 7 |
| battery | 10 |
| hitch | 4 |
| attachments | 6 |
| electrical | 28 |
| connectors | 12 |
| guards | 1 |

## Coverage procedure

1. Read all 103 unique source identities and input-sheet paths from the original FERME manifest; preserve original names, routes, quantities, dependencies and CAD references in that owning source.
2. Check each linked sheet, dependency target and existing CAD path using the FERME CAD directory for relative CAD locations.
3. Keep all inputs visible through the original part index; select actual build jobs using dependencies, route, source readiness and construction effort.
4. Update the component and part records in FERME and reusable action/skill/script records here after every iteration.
