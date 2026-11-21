# Create drawing elements, solid cuts and occurrences

1. Inspect the existing model, units, working plane, references and source revision. For assembly components, reconcile the part manifest, work records, input sheets, actual files and selected local catalogue using the [component reuse procedure](modeling-operation-selection.md). For variant requests, inspect the indexed definition's exposed parameter and permitted range. Reuse the requested variant or adjust a compatible exposed parameter in an owned copy, reopen, measure and index the variant before placing its occurrences.
2. Select the native pattern command when its driver supports the specified spacing, orientations and individual dimensions. In the owning native document, establish a seed on the selected sketch plane, host face or assembly seat. Set the driving path or axis, count, spacing or angles and per-member overrides. Recompute, save, reopen, inspect the driving references and match the generated member IDs to position IDs. For a new plate built from its recipe reuse the existing [plate builder](../scripts/plate_reference.py) and its grouped hole operation. For an insertion into an existing native assembly use [insertion recovery](insertion-resume-verification.md), then apply and check each additional [orientation](existing-batch-placement.md). Keep constraint-bearing sketches and multibody or attributed assemblies in a provider that preserves those relationships.
3. For individually created members, the [batch creation helper](../scripts/batch_creation.py) accepts a source file, its SHA-256, a [planar position request](planar-positions.md), an operation and shared or indexed dimensions. Run the command with a local interpreter containing ezdxf for DXF or CadQuery with XCAF import/export support for solids and assemblies. Paths for the model, catalogue snapshot and search script resolve from the request file’s directory. Keep the request, catalogue selection and result with the job.

   ```sh
   python scripts/batch_creation.py REQUEST.json NEW_JOB_DIRECTORY
   ```

   Example request for individually identified holes in one existing STEP solid follows. The selected plane origin lies on the entry face. The through-hole depth is the measured distance to the exit along the specified direction. A blind bore uses the requested bottom depth. Bare lengths use the pattern unit. A length also accepts a quantity such as `{"value":0.4,"unit":"cm"}`.

   ```json
   {
     "operation": "cut", "relationship": "individual",
     "model": "plate.step", "revision": "SHA-256 of plate.step", "direction": "-normal",
     "pattern": {
       "kind": "explicit", "unit": "mm", "tolerance": 0.001,
       "reference": "plate top face", "frame": {"origin":[0,0,10],"x":[1,0,0],"y":[0,1,0]},
       "positions":[{"id":"H1","xy":[10,10]},{"id":"H2","xy":[25,10]}]
     },
     "values": {
       "H1":{"diameter":4,"depth":10,"end":"through"},
       "H2":{"diameter":3,"depth":4,"end":"blind"}
     }
   }
   ```

4. For `circle`, supply a DXF R2000 or later drawing with declared units and `value: {"diameter": ...}` or one diameter per position. The group contains modelspace CIRCLE entities on the specified plane. The readback maps position IDs to entity handles, diameter, world centre and normal. For a circular pattern the helper checks each centre's pitch radius from the named axis. For an interior pattern with footprint containment, the helper checks every requested circle or bore diameter against the outer border, cutouts and required clearance in the selected plane. Readback records edge clearances measured from the reopened centre and diameter. For occurrence footprints use a provider that checks the projected part outline. For other drawing entities use the provider's native sketch tool on the selected plane and verify entity type, coordinates, dimensions and constraints after reopening.
5. For `cut`, the selected STEP must contain one solid. The result is a geometric STEP derivative in millimetres. Use the native feature editor when material properties, presentation attributes, mates or editable feature history must survive. Inspect the cut direction, entry, bottom or exit, depth, wall diameter and host volume after reopening. A blind bore retains material below its flat floor. The through-hole opens at both ends. Each opening requires a complete circular inner wire incident to a planar host face and an empty opening disk. A flat blind bottom requires a complete material disk bounded by the wall rim.
6. For `occurrence`, supply a single-solid STEP definition as `model` and a `part` object with `data` (selected local catalogue snapshot directory), `search_cli` (the local CAD Models search script), `query` and the reviewed record `id`. Omit `value` and `values`. The result is a new XCAF assembly in millimetres. Each position names a separate occurrence of one shared shape. The part origin defines the seat. Local Z follows the plane normal. Local X follows the generated tangent or the plane X axis. Inspect the source datum and use a native placement with the measured datum offset when the seat differs from the part origin. Reopened occurrence readback checks names, count, shared shape identity and the three axis directions.
7. The helper stages the complete result in a temporary job directory. It reopens and measures the output before publishing the job directory. Retrying the same request checks the request, model and readback against the published SHA-256 manifest. For an earlier footprint job whose saved receipt lacks clearance fields, the writer reopens the source and result. Delivery returns the original readback and a separate `footprint_verification` mapping position IDs to measured clearances. Sample qualification applies the same boundary checks to reopened CAD geometry. An interrupted unpublished job starts from the original source. A changed request or result requires a separate job directory.
