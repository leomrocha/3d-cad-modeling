# Model contract and checks

Record project-specific facts, not an invented design:

1. Source sketches/files, explicit corrections, rejected references, authorized scope/exclusions.
2. Units, right-handed coordinate frame, datum, axis signs and meanings of upwind/side/above. Below is not sideways.
3. Named separate parts, intended connections/motion, structure vs rotating parts, contact vs clearance, shared structure vs manufactured pieces.
4. Author-selected dimensions/tolerances; unresolved stays unresolved. Illustrative proportions need authorization and labels.
5. Display color/layer/render material separately from physical properties, condition/orientation and evidence.
6. Required measurable invariants: centered bodies, shaft directions/termination, support attachment targets. Do not make universal design rules from one example.

## `check_contract.py` input

The script takes one JSON file with:

- `length_unit`: nonempty unit label;
- `tolerance`: explicit nonnegative `length` and `angle_deg`;
- `observations`: named objects with `kind` (`point`, `axis`, `plane`), `origin` 3-vector; an axis has nonzero `direction`, a plane nonzero `normal`;
- `checks`: nonempty list of objects with unique `id`, `kind` and references below;
- `evidence`: object with `kind` (`cad_measurement`, `declared_design`, `synthetic_fixture`) and descriptive `source`. CAD measurements also require integer `document_id`, `revision` and nonempty string `handles`. This is caller-supplied provenance, not independent source authentication.

Checks:

1. `on_plane`: references `point`, `plane`; perpendicular distance within length tolerance.
2. `before_plane`: `point`, `plane`, nonnegative `minimum_clearance`; signed distance at most minus clearance, with length tolerance. Plane normal defines positive side. Tests endpoint, not whole solid.
3. `parallel`: `a`, `b` axes; smallest unoriented angle within angle tolerance.
4. `perpendicular`: `a`, `b` axes; within angle tolerance of 90 degrees.
5. `coaxial`: `a`, `b` axes; direction-angle and origin-to-axis separation within tolerances. Does not test divergence along finite shaft spans or bearing fit; use measured endpoints/span-specific checks for those.
6. `axes_intersect`: `a`, `b` infinite-axis distance within length tolerance. Combine with perpendicular for right-angle axes. Not a bevel tooth, finite reach or meshing test.

Run `python "$SKILL_ROOT/scripts/check_contract.py" CONTRACT_JSON`.

Exit 0: all supplied checks pass; 1: some fail; 2: invalid input/calculation. Missing/empty checks fail input validation. Output preserves evidence and units, and states these are checks of supplied numbers, not direct CAD queries or physical validation. Do not label manually asserted numbers as measurements.

Use supported OCS measurements for checks, then inspect orthographic views of the same geometry. AABB overlap only identifies candidate collision pairs. Gear axes at 90 degrees do not prove tooth engagement, shaft support or clearance. A line/circle belt depiction does not prove tangent spans and wrap geometry. See [computational-engineering.md](computational-engineering.md) for solver-specific data.
