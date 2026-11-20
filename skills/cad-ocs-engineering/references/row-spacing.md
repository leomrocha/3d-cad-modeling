# Resolve row spacing and measure surface gaps

Run `python scripts/row_spacing.py REQUEST.json`. The result identifies ordered positions in the measured plane, stations from the start, all adjacent pitches, and both actual border margins. Review these values before creating or moving elements. Lengths use the declared unit. Scalar widths, pitches, gaps, margins and tolerances also accept a quantity such as `{"value":1,"unit":"cm"}`.

```json
{
  "reference":"plate revision 1, lower edge", "unit":"mm", "tolerance":0.000001,
  "frame":{"origin":[0,0,0],"x":[1,0,0],"y":[0,1,0]},
  "segment":{"kind":"line","points":[[0,0],[60,0]]},
  "count":3, "width":[4,8,12], "gap":10, "margin_reference":"face",
  "margins":[0,0], "include_endpoints":[true,true], "remainder":"split",
  "containment":"complete"
}
```

This example gives centre stations 10, 26 and 46 mm, neighbour pitches 16 and 20 mm, face gaps 10 and 10 mm, and outside-face margins 8 and 8 mm. Supply measured widths along the straight row for parallel bars with centres halfway between their faces. Each centre pitch equals half of each adjacent width plus the face gap.

1. Give one directed line, circular arc or Bézier segment using the [planar position format](planar-positions.md). Pitch follows segment length. Specify a fixed count and pitch, omit count to repeat a shared pitch or gap, or give a count with `remainder: "fit"` and omit pitch to calculate it. With both pitch and count, `fit` checks that both fit the available span. A full circular arc or a Bézier with coincident ends has one interval per centre including the closing interval. Its seam uses zero centre margins and `[true,false]`.
2. Give the requested start and end margins and choose `centre` or `face`. Endpoints refer to eligibility at the resulting anchor limits. In pitch mode, each excluded open endpoint reserves one pitch. For a face-gap row, specify both border offsets explicitly and use `[true,true]`. For a single centre choose `anchor` as `start`, `centre` or `end`.
3. Choose `end` to leave the residual span at the end or `split` to divide it equally between the ends. Both preserve the specified open-row pitch. On a closed path, the seam station stays at zero. With `end`, residual length extends the closing interval. With `split`, half extends the first interval and half extends the closing interval. A one-centre loop has one full-length interval. Choose `fit` for equal intervals throughout a complete ring. For straight bars use `containment: "complete"` to check each full width against both row borders. For transverse borders and cutouts check the entire placed footprint using [planar containment](planar-positions.md).
4. For angled or curved elements, measure actual outlines after applying the placement. Use a second request with `kind: "surface_check"`, the geometry and revision in `reference`, a length `unit`, `tolerance`, a `profiles` map keyed by element ID, and a `checks` list. Each check supplies `pair`, `metric` and `expected`. For `shortest`, the measured value is the minimum distance between the filled profiles (zero on contact or overlap). For `directed`, supply a `direction` vector from the first toward the second. The measured value is the travel of the second profile toward the first along the opposite vector until first contact.
5. Use `{"kind":"polygon","vertices":[...]}` or `{"kind":"circle","centre":[x,y],"radius":r}` in the same measured plane. Polygon checks use local Shapely. If Shapely is unavailable, measure the placed profiles in the CAD provider along the same direction or by shortest distance and record the pair and measurement. Directed polygon checks use convex outlines. Circle pairs and sphere pairs use the Python standard library. Each request supports up to 4,096 checks and 100,000 vertex pairs summed across those checks. Use `{"kind":"sphere","centre":[x,y,z],"radius":r}` for pairs of spheres in the same world frame. For sphere centres on [spatial position rows](spatial-positions.md), use the measured world coordinates of the sphere centres. Measure other solid surfaces with the CAD provider’s placed geometry. Preserve the named direction, element IDs and measured values with the job.
