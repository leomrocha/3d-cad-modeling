# Reusable measured-feature checks

1. Supply independently sourced expectations, units, frame and positive finite numerical tolerance to [feature_checks.py](../scripts/feature_checks.py). Native measurements retain document, revision, geometry epoch and handle identity.
2. comparison checks finite values; closed_body checks one body/lump/shell and reciprocal coedges; vertex_extrema compares observed vertices in each coordinate. Curved surfaces may extend beyond observed vertices.
3. cylinder_pattern selects the supplied diameter and Cartesian axis, projects centres onto the other coordinates and deduplicates coincident patches. Each expected centre must have exactly one remaining candidate within the inclusive coordinate tolerance. Missing, extra and ambiguous matches fail. matched_pairs preserves assignments. Sorting alone is insufficient for nearly equal coordinates.
4. cylinder_wall_checks consumes decoded face supports and actual boundary endpoints. Supply axis, projected centre, radius, side, outer surface and inner-region limit. Each wall requires radial agreement and vertices reaching both regions. A projected axis alone describes the axis; the wall check measures material boundaries.
5. Keep source interpretation, native geometry, numerical comparison and visual identity as separate evidence. Use [stable reads](generic-integration.md), [circular boundaries](circular-boundary-checks.md) and [retained artifacts](retained-artifact-checks.md).
6. For a Boolean seat or notch, pass the receiving solid's reopened points and its independently expected corners to `feature_vertices`. The report gives each nearest position and Euclidean error in mm. A common nearby vertex cannot satisfy two distinct corners. Use face or topology checks as well when the intervening surface matters.

7. For SAT curves without decoded support planes, `circular_trim_stations` checks distributed native boundary samples at source-bound entries and blind-end stations. Pair it with cylinder-axis checks, closed-body topology and an independent check of backing stock. A ring confirms its observed trim station. Use decoded planes or face loops when the cap surface itself must be established.

## Preserve openings after a remote edge cut

1. Read the original solid in its installation frame. Record the through-bore diameters and projected centres, the cylindrical supports for slots and reliefs, and the native boundary edges of those openings. Bind the comparison to the original model hash. Use the same stable reader before and after the cut.
2. Locate the cutting plane and the retained side. Establish that the protected opening boundaries lie entirely beyond the cut using analytic curve extrema or an independent source-bound dimension. Compare edges wholly on the retained side. Use the same sampler settings and coordinate precision for both reads, compare each edge in either traversal direction, and preserve duplicate counts. If an uninterrupted boundary is represented by different edge splits, compare its joined analytic curves. Sample agreement is a separate check from full curve equivalence. The native curve sampler keeps the interval count stable when the requested density differs from an integer by floating-point roundoff. Check analytic supports and trim endpoints independently of this display sampling.
3. After the Boolean, verify that the result is one closed solid, that the expected cut-face corners lie on the cutting plane and that the retained thickness and extent match the stock. Compare the measured opening axes, radii and retained edges with the recorded baseline. Equal cylinder supports alone cannot establish that slot endpoints or wall trims survived.

## Widen stock around a fixed circular opening

Keep the bore centre referenced to the mating interface when altering stock width. Record both new side planes individually. The midpoint of the stock can move while the bore axis stays fixed. Verify the placement against the mating part's independent axes and the new support limits.

Use `circular_opening_edge_land` for a circular rim between two parallel sides. Feed the measured opening centre and side plane coordinates along the same transverse axis. On a countersink use the rim radius at the mouth. Check the signed land to each side. Zero is tangency and a negative value is breakout. Use the measured ring, planar side geometry and the specified acceptance limits separately. The returned length measures edge land.


## Check material between parallel bores

1. Before cutting an index row or other group of separate circular bores, project the centres into one plane perpendicular to their axes. Use one group for the bores that pass through the same material wall. Use `planar_bore_ligaments` from [feature_checks.py](../scripts/feature_checks.py) with each centre and diameter, the required material thickness between hole edges, and the numeric tolerance. A zero requirement checks separation only.
2. Repeat the calculation with centres and diameters read from the native part. Observing several cylinder axes can still leave one connected opening. Check a full circular rim on both wall faces for every bore intended to be separate. Use [saved circular boundaries](circular-boundary-checks.md) for that check. Verify load-based ligament and edge distances against the applicable design requirement.

## Check a through-keyway in a concentric bore

Use `concentric_through_keyway_section` to derive the two mouth corners on the bore and the two floor corners from independent dimensions. The circular bore is centred at the origin and the slot opens toward +Y. Radial depth is measured at the centreline from the bore radius to the floor. The minimum radial wall is the outer radius minus the distance to either floor corner. A negative result indicates breakout for the declared concentric section.

Use native cylinders to check the bore and outer diameter. Verify the mouth and floor corners separately at both end faces. Identify the continuous longitudinal edges or faces of the keyway so matching end sections cannot hide a blind obstruction. Record the axial span and its relation to the mating shaft pocket independently of the radial section.
