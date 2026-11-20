# Generate positions in a measured plane

Run `python scripts/planar_positions.py REQUEST.json > POSITIONS.json` from the engineering skill. Each request gives one length unit (`mm`, `cm`, `m`, `in` or `ft`), a geometric tolerance in that unit, a reference identifying the measured source and an oriented plane. Supply its world origin and two orthogonal unit directions. Positive angles run from the plane's x axis toward its y axis. Carry the source revision in the reference or its owning job record.

For example, this request places points at 5 mm distances measured along a 90-degree arc in a YZ plane.

```json
{
  "kind": "path", "reference": "sample profile, revision 1, edge A",
  "unit": "mm", "tolerance": 0.000001,
  "frame": {"origin": [10,0,0], "x": [0,1,0], "y": [0,0,1]},
  "measure": "path", "pitch": 5, "orientation": "tangent",
  "segments": [{"kind":"arc", "centre":[0,0], "radius":10, "start_deg":0, "sweep_deg":90}]
}
```

The four stations are 0, 5, 10 and 15 mm. The resulting world positions start at [10,10,0] mm and end at approximately [10,0.707372,9.974950] mm. Each row carries an ID, source reference, plane coordinates `xy`, world coordinates `xyz` and, when requested, the world unit tangent `direction_xyz`. Pair rows by ID with the selected holes, bars, sketch elements or assembly occurrences. Preserve the positions file and selection with the job. Pass the position and direction to the batch action in the action's required frame.

| Pattern | Request fields |
|---|---|
| Explicit | Set `kind: "explicit"`. Supply `positions` in the intended order, each with a unique string `id`, an `xy` coordinate pair and optionally a nonzero in-plane `direction`. |
| Directed path | List connected `segments` in travel order. A `line` takes two `points` in start-to-end order. An `arc` takes `centre`, `radius`, `start_deg` and signed `sweep_deg`. A `bezier` takes three or four ordered control `points`, including both endpoints. For reverse travel reverse the segment list and control points, or start the arc at its former end and negate the sweep. |
| Pitch and tangent | Set `measure` to `path` for distance along the curve or `chord` for direct distance to the first subsequent point at the requested `pitch`. The start is included. The end is included if a station falls there within tolerance. A closed path emits its seam once unless `duplicates` is true. At a Bézier endpoint with repeated control points the tangent follows the first distinct control point in the travel direction. For tangent orientation, set `orientation: "tangent"` and choose `corner_tangent: "incoming"` or `"outgoing"` at a corner. Bézier length integration and distance inversion use local SciPy and NumPy. |
| Triangle, rectangle or polygon | Set `kind: "polygon"` with cyclic `vertices`. Supply each vertex once. Set `mode: "vertices"` or `mode: "sides"`. Side mode accepts all sides by default or an ordered `sides` list of zero-based indices. Each side starts at its indexed vertex. With `spacing: "continuous"` select connected sides. With `spacing: "restart"` restart the pitch at each chosen side. Set `duplicates: true` to retain repeated shared-vertex stations. The standard-library profile validator checks the boundary. Each selected side index must be unique. An endpoint with one selected incident side uses that side’s tangent. |
| Bolt circle | Set `kind: "circle"`, `centre`, `radius`, `start_deg`, and `order` (`cw` or `ccw`). Supply one of `count`, `increment_deg` or `angles_deg` (increasing offsets from the start in the chosen direction). An explicitly repeated closing angle is emitted once. |
| Interior rows | Set `kind: "interior"`, `layout: "rows"`, a grid `origin` and positive `pitch_xy`. Enumeration proceeds by increasing y and then increasing x within each row. Row tangents follow positive plane x. Candidate bounds include the offset of a footprint from its anchor. |
| Interior rings | Set `kind: "interior"`, `layout: "rings"` and an ordered `rings` list. Each entry takes bolt-circle fields and inherits the interior request’s orientation unless the entry sets its own orientation. Use the same centre for concentric rings. |
| Boundary and footprint | Supply `outer` and optional `cutouts` as circle (`kind`, `centre`, `radius`) or polygon (`kind`, `vertices`) objects. Set `clearance` and `containment: "centre"` or `"footprint"`. For footprint containment supply a circle or polygon `footprint` relative to the element anchor. Footprint coordinates use the plane axes for fixed placements. On a ring with tangent orientation, the footprint rotates so its local x axis follows the tangent. Use the oriented outline of a bar, or a circle centred at [0,0] with the hole radius. At zero clearance boundary contact is permitted. Interior checks use local Shapely and analytic circle radii. |

Explicit points, line and arc paths, polygon vertices and sides, and bolt circles run with the standard library. For Bézier or interior requests, use an existing local interpreter with the listed libraries. If one is unavailable, use the selected CAD provider’s existing curve measurements or footprint and cutout checks, record the measured ordered positions, and send them through `kind: "explicit"`. Preserve the requested distance tolerance and measured orientations.

The producer limits a request to 20,000 positions or grid/ring candidates, 2,048 positions on an individual circle, and 512 vertices for a polygon perimeter. Each candidate count applies before interior filtering.

Check the position count, first and last coordinates, consecutive pitches, chosen corner tangents and closing station against the selected source geometry. For a row with cutouts, inspect the positions omitted by the full-footprint check. Preserve the reported unit, plane and position order when transforming or consuming these results.
