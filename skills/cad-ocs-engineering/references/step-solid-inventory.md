# STEP solid-definition inventory

Use `scripts/step_solid_inventory.py::inventory_step_solids` before comparing
STEP solid definitions with native imported solids.

1. Pass the original Part 21 bytes or decoded text. The reader scopes entity
   records to the `DATA` section and returns entity IDs as well as counts.
2. Count each `MANIFOLD_SOLID_BREP`, `BREP_WITH_VOIDS`, and `FACETED_BREP`
   entity once by its STEP ID. Nested `CLOSED_SHELL`,
   `ORIENTED_CLOSED_SHELL`, faces, and other topology records are reported as
   non-solid definitions and do not increase the solid-definition count.
3. The reader reports complex STEP entities separately. Their component type
   names and solid-related flag are evidence for a separate parser decision;
   complex entities are not included in the supported solid count.
4. Compare the supported count with native solid definitions only after
   retaining the source hash, schema, units, and actual native entity types.
   A matching count does not prove matching geometry, placements, or product
   instances. Retain independent source-linked feature checks and save/reopen
   checks for those claims.
5. This reader handles entity inventory. It does not interpret STEP geometry,
   assemblies, placements, schema semantics, or units. A new solid-bearing
   entity type requires an explicit parser extension and a synthetic test.

Synthetic tests cover the three supported entity types, nested shell records,
comment/string text, complex entities, duplicate IDs, and a missing `DATA`
section.
