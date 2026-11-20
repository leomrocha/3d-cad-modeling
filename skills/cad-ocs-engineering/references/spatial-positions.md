# Position and orient occurrences in 3D

Run `python scripts/spatial_positions.py REQUEST.json > POSITIONS.json` from the engineering skill. Use the measured reference name, revision and coordinate system from the owning job. Each output row identifies one position, its local coordinates, its world origin, its transform in the parent and its world transform. Matrix columns 1, 2 and 3 are the placed part’s X, Y and Z directions. Column 4 is the origin. Distances use the declared unit throughout (`mm`, `cm`, `m`, `in` or `ft`).

This cylinder request places four occurrences on each of two rings. Local Z is the cylinder axis. The meridian fixes local positive X. Positive longitude turns from X toward Y. The host origin and directions are expressed in the parent. Supply an orthonormal affine `parent_to_world` matrix for a transformed parent. Its default is identity. A mirrored parent produces a mirrored world frame and preserves the supplied part frame within that parent.

```json
{
  "reference": "fixture revision 1, cylindrical face A", "unit": "mm",
  "frame": {"origin": [10,0,0], "axis": [0,1,0], "meridian": [0,0,1]},
  "kind": "cylinder", "radius": 5, "height": 10,
  "levels": [0,10], "angles_deg": [0,90,180,270,360],
  "orientation": {"mode":"normal", "x":"azimuth", "roll_deg":0},
  "checks": [{"pair":["P0001","P0002"], "metric":"cylinder_surface",
              "distance":7.853981634, "tolerance":0.000001}]
}
```

1. **Prism or box.** Set `kind` to `prism`. Give the base polygon's ordered XY `vertices` (four corners for a box), its extrusion `height`, and the selected axial `levels` measured from the base. In `mode: "volume"` supply X `columns` and Y `rows`. Each selected level uses the polygon to filter the row and column intersections, including boundary points. Use `cap` for the end faces at zero or full height. For `side` give its zero-based edge index `side` and physical `stations` measured along that edge from its first vertex. Use `rim` for the same edge on an end face. Use `upright` for the vertical edge at the indexed vertex.
2. **Cylinder.** Supply angular coordinates and axial levels in the required order. Use one angle for an axial row or one level for a ring. Each level uses the same angles. Equivalent angles at a level emit one position.
3. **Sphere.** Supply `kind: "sphere"`, `radius` and `rings` in output order. Each ring has a `latitude_deg` from −90 to +90 and its own `angles_deg`, or uses the shared request angles. A ring with one longitude supplies one angular position. This distribution uses the specified angles. Latitude-ring distance varies with the cosine of latitude. Both poles use the zero-meridian frame, with one position per pole.
4. **Orientation.** The occurrence’s positive Z is its mounting axis. Choose `fixed` with a local direction `z`, `normal` on a selected face, `tangent` along a selected path, `toward_axis`, `away_axis`, `toward_centre` or `away_centre`. Centre modes accept a local `centre` (default local origin). Axis modes use the local Z axis. For a curved tangent set `path` to `azimuth` (increasing longitude), `axial` (increasing cylinder level), or `meridian` (increasing sphere latitude). A prism side or rim follows the indexed edge, an upright follows positive Z, and cap/volume rows follow positive X. Set `x` to the part's second direction in host coordinates. It is projected perpendicular to mounting Z. On a cylinder or sphere, `x: "azimuth"` follows the positive longitude tangent across the closing meridian. Supply a local `fallback_x` when the chosen second direction becomes parallel. Positive `roll_deg` turns the part’s X toward its Y about mounting Z.
5. **Physical distances.** Pair the intended neighbour IDs in `checks`, including the closing pair for a complete ring. Supply a target `distance` and absolute `tolerance` in the declared unit. `chord` measures straight-line distance. `great_circle` measures the shortest sphere surface distance. `latitude_arc` measures the shorter arc on a single latitude. `cylinder_surface` measures the shortest distance in the unwrapped cylinder surface including axial offset. A failed measurement stops the preview. Candidate enumeration is limited to 20,000 per request and the prism base to 512 vertices.
6. **Readback.** Use each reviewed parent transform for its assigned occurrence. After reopening the assembly, compare origin, three directions and handedness to the world transform by occurrence identity. Check the selected neighbour distances using reopened origins, the original frame and the specified metric.
