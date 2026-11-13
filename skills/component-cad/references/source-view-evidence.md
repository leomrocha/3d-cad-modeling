# Source-view evidence for drawing-derived geometry

Use this procedure when a manufacturer drawing is available as a retained raster image or as a rendered page from a retained original PDF. It records how a source view supports dimensions, a traced outline, or both.

## Preserve and identify the source

1. Keep the original PDF or image unchanged. Record its original URL or local source path, acquisition or observation time, content type, byte count and SHA-256.
2. Record derived page renders and extracted images separately, with their source PDF page, render or extraction command, pixel dimensions, content type and SHA-256. A rendered or extracted image is inspection evidence; it is not the original source.
3. Bind each dimension and geometry feature to the exact source revision, product caption, page, figure, view, leader endpoints and measurement kind. Keep manufacturer callouts, raster measurements and calculated coordinates labelled separately.
4. Label evidence as extracted source text, a tool-generated visual description, or inspected source-image pixels. Bind a drawing leader to an inspected source view or explicit numerical source text; a generated description does not establish which source pixels its leader reaches.
5. Record inaccessible alternate revisions as failed retrieval attempts with the actual response. Do not transfer dimensions between revisions without inspecting the exact product view.

## Bind a view to metric geometry

1. Set drawing axes and the local datum from visible source features. State whether the datum is directly printed, measured from the raster, or calculated from source dimensions.
2. Calibrate each raster axis from a source dimension whose extension lines are visible in that same view. Preserve the selected endpoint pixels, direct dimension value, pixel-span uncertainty and resulting scale interval.
3. Retain source pixel coordinates for the traced points. Record the pixel edge-pick uncertainty, polygon simplification method and allowance, pixel origin and uncertainty, signed per-axis scales and scale uncertainty.
4. Propagate those values through the calibrated-trace procedure. Keep the direct printed dimensions as source claims and compare traced spans against them with a derived raster interval. Do not label a raster interval as a manufacturing tolerance.
5. Validate the resulting point order and polygon before native writes. If a busy line drawing produces a self-crossing outline, use a documented projected clearance representation such as a convex hull only when the intended result is an outer clearance volume. Record which concavities and details the representation removes.
6. Keep mounting circles, axes, slots and datums as separate reference features where the source establishes them. A printed diameter and pitch do not establish a hole depth or a through-cut.
7. State what the resulting solid represents: a traced external surface, projected clearance volume, packaging envelope or another named representation. Preserve unresolved body construction, walls, feature depths and hidden geometry as separate source requirements.

## Evidence and result records

The component job retains the original-source identity, derived-image provenance, per-feature source locators, trace points, calibration inputs, uncertainty bounds, native frame and geometry role. The result records source-readiness separately from native construction, numerical readback and saved-file checks. A pixel-perfect visual resemblance alone does not establish dimensional correctness; a numerical source-bound comparison alone does not establish detailed product construction.
