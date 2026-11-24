# Rational surfaces, open meshes and bounded recovery

## Evaluate before final coordinate rounding

Use [rational_surface.py](../scripts/rational_surface.py) for bounded rational B-spline point evaluation. Supply rectangular `control_points[u][v][xyz]`, positive `weights[u][v]`, degrees, expanded knot vectors, normalized UV, an affine 4x4 source-to-output transform and two increasing decimal precisions. All inputs are finite binary64 values represented exactly in Decimal. Units and frame belong to the caller. The helper evaluates only the local nonzero basis, performs the rational division and transform at each precision, then rounds the final coordinates once.

Require `result=PASS` before using the returned point: it means the two precisions round to identical binary64 coordinates. Retain the higher-precision reference, precision difference and rounding-error observation. These checks describe numerical convergence on the supplied inputs. Source reconstruction uncertainty, manufacturing tolerance and analytic error certification have separate evidence.

Default normalized bounds are [0,1] on both parameters. A source-derived polynomial fringe needs explicit caller `parameter_bounds`; preserve its source-domain and trim-coverage justification. The helper supplies no STEP parser, trim inversion, polygon clipping, watertightness proof or automatic surface repair. Invalid weights, knots, degrees, UV bounds, output overflow and unknown domains stop the operation.

For a numerical recovery, retain the original coordinates, UV, topology and failed triangles. Re-evaluate only the authorized affected vertices. Verify that protected interior arrays, original source polygons, indices and source hashes remain exact. Compare the full resulting and saved/readback arrays. Never remove positive-area parameter triangles to conceal a numerical collapse. Preserve failed attempts and array copies used as baselines; an aliased array cannot prove preservation.

## Check actual triangle arrays

Use [mesh_checks.py](../scripts/mesh_checks.py) with explicit `minimum_area` in length-unit squared, optional corresponding UV vertices and `minimum_signed_uv_area` in parameter-unit squared. The helper checks finite arrays, integer indices, duplicates, numerical areas, local edge orientation and incidence. It identifies positive-UV triangles whose 3D area is zero. `require_closed=False` permits open meshes; record the open representation. Edge closure alone does not certify a manifold embedded solid or absence of self-intersection.

Select an area criterion from the intended numerical contract. Tiny positive numerical area and physical manufacturing accuracy have separate meanings. Preserve the exact failed triangle indices and source inputs. Report sampled facet deviations with sample positions and numerical criteria; finite samples do not supply a global error bound. Complete trim coverage, outside-domain area and overlaps retain independently pinned checks.

## Declare missing DXF layers in a derivative

Use [mesh_dxf.py](../scripts/mesh_dxf.py) only for an authorized MESH-only DXF rewrite. `declare_mesh_layers` requires exact source SHA-256, explicit DXF units code, a new distinct target and an existing caller-owned directory. It adds missing layer-table declarations, writes a temporary file, then checks complete exported MESH tags, units and format version after readback. It rechecks original bytes and atomically publishes without overwriting a destination. Populated extra layouts/blocks and other entity types require a separately supported conversion.

Record source/derivative hashes, added layers, units, format version and unchanged entity observations. Native import and geometry verification remain separate operations. Preserve source originals and previous outputs after any failed check.

## Verify a recorded INSERT cancellation

The default continuation route remains [guarded insertion recovery](insertion-resume-verification.md). When inspected normal input fails, inspect its completed effects and exact owned prompt. A source claim about command ownership does not establish the event that changed ownership. The public state may omit that owner.

A cancellation needs explicit scoped authorization, a serialized writer, resolved earlier request IDs, the exact owned document/revision/geometry epoch, no active operation and a preceding persistent checkpoint. Record complete root, Insert and block collections first. Send at most the specifically authorized cancellation with a stable ID and recover that same ID after uncertainty. A wrapper exception can accompany an `ok=true`, `status=cancelled` terminal response; inspect the original journal and fresh state.

`verify_cancelled_insert` in [insert_recovery.py](../scripts/insert_recovery.py) checks the recorded request ID/terminal response, unchanged document and geometry epochs, an idle final command state and equality of the supplied complete collections. It sends no request. A cancellation that leaves the command active fails this gate. A subsequent cancellation is a separate scoped decision. Save the recovered idle state immediately. Before reusing an already-loaded block for a new occurrence, verify its full source payload, metadata and nested transforms through the existing transfer/assembly checks.

## Respect the caller's persistence operation

Use the authorized persistence method. When verification reopen is authorized, use the existing save/reopen procedure. When the task explicitly requires save-only verification, use [save_checkpoint](../scripts/cadtools/checkpoints.py), completed request/audit, exact saved-file hash and current owned geometry/metadata checks. Record `verification_reopen=false`, current document/revision and the save evidence. Never label current checks as reopened checks. Close only completed owned documents through [document cleanup](document-cleanup.md) after the task's required persistence gate passes. Retain historical reopen evidence with its original document and date.

## Measure a repaired mesh

Use [mesh_repair_evidence.py](../scripts/mesh_repair_evidence.py) with the original and repaired triangulated OBJ files in the same millimetre frame. Redirect its JSON output to a job evidence file. This operation covers additive patches with retained original triangles. Read `repair.original_boundary_edges_mm` for measurements on the original opening and `repair.saved_triangles` for measurements on added geometry. Triangle indices in the report start at zero.

For a cylindrical source region, supply `--cylinder REGION.json` with `source_triangles` and a known unit `axis` in the same frame. The result records the fitted radius and axis point, the original triangle IDs and maximum radial error sampled at their vertices. Compare that error with the job tolerance before using the fit.
