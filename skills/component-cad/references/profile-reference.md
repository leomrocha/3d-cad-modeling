# Source-traced profile reference extrusion

Use `scripts/profile_reference.py` when an external project supplies a closed, straight-segment profile trace and a source-defined extrusion depth for a reference volume. This representation can preserve a manufacturer-view silhouette for packaging or clearance work. It does not infer curved edges, hidden features, wall thickness or manufacturing construction.

## External job input

The caller supplies one job object with these fields:

1. `job_id`, `part_id`, `part_name`, `representation`, `geometry_role`, `geometry_name`, `units="mm"`, `frame`, `local_frame`, and a concrete `geometry_scope` statement.
2. A supported projected-reference `geometry_role` (`source_traced_projected_profile_reference`, `source_view_projected_clearance_reference`, or `source_traced_packaging_clearance_reference`); detailed product-body roles are rejected.
3. `profile_points_2d`, a closed polygon point list in order, without repeating the first point at the end.
4. `origin=[x,y,z]`, where `x` and `y` translate profile coordinates and `z` is the extrusion start plane.
5. `depth_mm`, plus `depth_feature_name` that points to a required pinned source feature with the same finite numeric value and unit `mm`.
6. A positive finite `readback_tolerance_mm` when the default comparison threshold is unsuitable.
7. `features` that pass `component_records.require_ready(job)` and a nonempty `source_files` list. Every listed source file must be pinned by a required feature.
8. `profile_extent_features` mapping both `x` and `y` to required source features in mm, `profile_extent_bounds_mm` for both axes, and a written `profile_extent_basis` for each interval. Each interval must contain its mapped source value; the helper compares the polygon's measured spans directly to those source-bound intervals before construction. Use printed source tolerances only when the source gives them; otherwise derive and label a measurement interval from trace uncertainty.
9. Optional `source_dimension_expectation=true` flags on dimension features whose source claims should be retained separately from output-geometry checks.

Stored source locators use repository-relative paths or named roots as described in [portable paths](../../../docs/paths.md). The caller resolves external locators with its explicit root map before passing runtime file paths and pinned hashes to this helper. Source-page dimensions remain source expectations. Native output bounds are computed from the supplied polygon coordinates, origin and extrusion depth; source-dimension fields supply the independent comparison.

Resolve both `features[].source` and `source_files[].path` in the runtime copy to the same absolute file path. Source readiness returns canonical absolute observations; comparing those with unresolved relative strings causes a source-pinning preflight failure. Preserve the stored portable job and its hashes. Supply the portable metadata payload separately when writing native source records, and compare that exact payload after reopen. The component job retains the runtime transformation and original/derivative hashes.

## Preflight and construction

`parameters(job)` validates source readiness and all construction inputs before the OCS Geometry adapter loads or any write is attempted. It rejects non-mm jobs, unsupported roles, missing frame/scope labels, malformed or nonfinite values, booleans used as numbers, repeated vertices, zero-area profiles, nonadjacent edge crossings/touches/retraces, nonpositive depth, depth lost to floating-point precision, invalid tolerance, a nonrequired or mismatched depth feature, missing source files or sources not pinned by required features, source extent mappings that are not positive required mm features, profile extents outside the explicit source-bound intervals, translated-profile collapse, and coordinate arithmetic overflow.

`build_profile_reference(client, job)` reuses the existing guarded `Geometry.extrude` path from `cadtools.geometry`; it does not duplicate selection or command execution. It creates one straight-sided solid and attaches the supplied component, role, units, local frame, job, scope, depth-feature and pinned source-file metadata. Caller retains the local-to-assembly transform and every product-specific trace point in the external component project.

The supported construction frame is an XY profile at `[origin.x, origin.y, origin.z]` extruded along positive local Z. Map the component axes explicitly before choosing this frame. The helper applies no scale, rotation, pose or unit conversion.

## Readback and evidence

`inspect(client, {"solid": handle}, job)` checks the bound active document, exact returned handle, `Solid3D` entity type, SAT/SAB geometry, and stable document and geometry revisions around the read. `verify(features, job)` reports separately:

1. native vertex extrema against bounds derived from the supplied profile and depth;
2. bidirectional point-set comparison between actual native vertices and the expected vertices of the supplied straight polygon at both extrusion planes;
3. a single closed connected body when native topology is available; and
4. source dimensions selected by `source_dimension_expectation`, copied as source claims without using them as native output bounds.

The numeric comparison threshold is a software readback threshold. It is not a drawing tolerance or manufacturing tolerance. Keep raster-trace point uncertainty and source dimensional uncertainty in the owning component record.

For a saved-model completion gate, require actual `features["topology"]` and a passing `feature_checks.closed_body()` result after reopen. The `encoding` field is descriptive text such as `SAB native body graph`; it is not the structural topology contract. Before save, a construction document can expose SAT point records, so point and extent checks run before the mandatory reopened body check. If a caller check fails after a successful save/reopen, preserve that failure and resume read-only checks against the recorded document and handles using the original request journal. Reuse the saved artifact.

Check actual pre-save and reopened `CADTOOLS_SOURCE` records with the [source-metadata procedure](source-metadata.md). Preserve the complete expected metadata payload in the component job; `verify()` compares geometry and retains source expectations, while the metadata comparator reads the stored native strings.

`tests/test_profile_reference.py` uses synthetic temporary source records and fake native readers. It covers guarded extrusion arguments and metadata, independent source-bound profile extent gates (including a wrong-scale profile rejected before geometry creation), source-dimension separation, exact profile vertex readback, stable document binding, malformed/self-intersecting/retraced profiles, booleans, invalid depth/tolerance, source pinning, huge numeric inputs, and coordinate/depth overflow. These tests establish helper behavior only; they do not validate a physical component or an OCS native session.
