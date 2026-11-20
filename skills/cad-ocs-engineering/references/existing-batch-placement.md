# Place existing occurrences at reviewed destinations

The [DXF placement helper](../scripts/batch_dxf_placement.py) moves individual INSERT entities in a job copy of an R2000 or later drawing with declared length units. Each occurrence retains its handle, parent and block definition. The placement anchor is the block base point. The three axes are the block definition’s local axes.

1. Obtain positions in the drawing unit from [planar positions](planar-positions.md), [spatial positions](spatial-positions.md) or [row spacing](row-spacing.md). Retain the source geometry, measured reference and generator request with the job. Inspect the block base and local axes against the intended mounting interface. A spatial position supplies its world transform. For a planar position, local +Z follows the plane normal and local +X follows the supplied tangent or the plane's X axis when the position has no tangent.
2. Supply the source drawing, SHA-256 revision, unit, selection and assignments. Identify nested INSERTs by slash-separated handles from modelspace through the parent to the target. Example input for two measured nested paths follows.

   ```json
   {
     "model": "assembly.dxf",
     "revision": "SHA-256 of assembly.dxf",
     "model_unit": "mm",
     "selection": {"scope": ["51"], "paths": [["51","32"], ["51","33"]]},
     "assignments": {"51/32": "P2", "51/33": "P1"}
   }
   ```

   The selection also accepts a saved drawing group or a measured condition. For ordered assignment use `"order_by":"increasing measured distance"` or `"decreasing measured distance"` in place of `assignments`. Supply a selection measurement with its reference path, direction, side and anchors. A per-position reference, when supplied, must match the group reference. Use `target_anchor: "block base"` and `measure_to: "anchor"` for an INSERT. The helper pairs targets in that measured order with positions in generator order. Tied distances within 0.00000001 drawing units need explicit assignments.

3. Configure an approved guided catalogue method with `name=move-existing-insert`, `action=place`, `input=DXF INSERT`, `output=existing occurrence world base frame` and the installed `ezdxf/VERSION` backend. Use the helper path as the local guided resource. Prepare the preview with the installed helper. Review every occurrence, reference, position ID and current and requested world base frame. The right column of the frame contains world coordinates in drawing units. The first three columns contain the axis directions.

   ```sh
   python scripts/batch_dxf_placement.py prepare REQUEST.json POSITIONS.json --catalogue OPERATIONS.json > PREVIEW.json
   sha256sum PREVIEW.json
   python scripts/batch_dxf_placement.py sample PREVIEW.json NEW_SAMPLE_DIR --preview-sha256 REVIEWED_DIGEST --resource RESOURCE
   ```

4. Register the sample's `evidence.json` as the method's `readback_file` and refresh the approved catalogue. Prepare and review the execution preview against that catalogue. Start a separate job directory.

   ```sh
   python scripts/batch_dxf_placement.py execute PREVIEW.json NEW_JOB_DIR --preview-sha256 REVIEWED_DIGEST --resource RESOURCE --catalogue OPERATIONS.json
   python scripts/batch_dxf_placement.py resume NEW_JOB_DIR
   ```

5. Each write converts the world base point and axes to the owning parent frame, updates that existing INSERT, saves a staged drawing and reopens it before replacing the job copy. `results.json` reports the status and request ID for each target. Resume uses the original job and request IDs. An independent job supplies a separate namespace for later moves of the same handle. A saved starting frame permits the original pending move. A saved destination with matching intent confirms the applied move. A third frame records an unknown effect on that target and permits the remaining independent moves.
6. Read `readback.json` for each reopened block base, orientation, named reference, assigned position ID and direct distance to the preceding assigned position's base in generator order. The verifier compares entity identities, block definitions, group membership and independent layout geometry with the source. Retain the saved result and receipts with the job. Measure along-path pitches, face gaps and border margins from the placed geometry using the specified spacing measure.
7. Use this operation for rigid individual occurrences with unchanged handedness under independently editable parent blocks. For a shared parent definition, select a native occurrence-specific transformation that preserves every sibling. For an existing array member, use a native array operation that identifies that member and preserves its array relationships. For sketch elements or constrained geometry, inspect driving dimensions, coincident points, fixed points and solver constraints in the native editor, apply the supported native edit, solve, reopen and measure selected and retained geometry. Route locked, attributed, externally referenced or constrained occurrences to a provider that preserves those properties.

## Guided native placement when the DXF writer is unavailable

1. Select the available CAD provider from the saved operation catalogue. Confirm its native edit can address an existing occurrence by path and set its placement while retaining the occurrence identity. Open a job copy using the source format and inspect the native document revision, units, parent transform, block base, current frame and layer or constraint state.
2. For OpenCADStudio native inserts, inspect the current `records` and `set_properties` schemas. Use the [guarded native placement helper](../scripts/assembly_repair.py) for individually addressable source placements. Its `apply_source_placements(client, changes, original_records)` interface expects one change per handle with `before`, `expected`, `fields` and `source_id`. Supply the current native insert and solid records. Allocate a new job namespace for the guarded client, keeping it across retries.
3. For a zero-base native insert, compute the requested local frame as the inverse of the parent world transform multiplied by the reviewed world base frame. Use `native_fields(expected)` from the [placement reader](../scripts/step_placements.py) for rotation, normal and insertion point. Inspect the supported reflection mode before submitting a mirrored frame. For a nonzero base or a native array, use the provider's measured block-base transformation and member-specific edit only after its sample readback reproduces the requested anchors and retains the siblings. For constrained sketches, select the driving constraint in the native editor, apply its reviewed value and solve.
4. Save the owned document in native format, reopen it and compare occurrence paths, block-base coordinates, all three axis directions, assigned-order spacing, unselected placements and definition geometry. Use the original guarded request ID to recover an interrupted edit. Record the provider and the measured result for each selected path.
