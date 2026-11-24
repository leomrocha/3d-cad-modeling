# Modify selected dimensions and properties

1. Reopen the source revision. Resolve each feature or occurrence within its owning part and parent occurrence path. Inspect its driving field, orientation, current value, units, users of the definition or expression, and requested fixed anchor. Record the source SHA-256 and selected IDs. Apply the [operation selection procedure](modeling-operation-selection.md) when a compatible variant already exists.
2. For a named driving sketch dimension, inspect the constraint type, solver state, dimensional freedom, expression binding and dependent features in the native editor. For a shared expression, trace every consumer, including indirect dependents. Update the expression once when all its consumers need the same change. For a selected subset, copy the owning part or parent assembly and bind the selected dimensions to an independent parameter. A coincident, equal or symmetric constraint may couple selected and unselected geometry. Identify the constrained entities and request the intended edit scope before changing a constraint that drives both sets. Recompute the sketch and its complete dependent feature chain. Save a separate native revision, reopen it, read the driving fields and measure selected geometry, the retained anchor and an unselected peer.
3. For a single imported STEP solid with complete cylindrical bores, select the entry centre, inward unit direction, original diameter, depth and end type. The direct solid edit supports enlargement of through and flat-bottom blind bores. Use the native editor for reduction, intersecting holes, editable history or attributed assemblies. For a plain rectangular XCAF bar select its definition-local length axis and the end or centre that stays fixed. The helper supports nested occurrences and rotated parents. It isolates each shared parent along the selected occurrence path and the selected leaf definition before editing. A named XCAF occurrence also supports a display-name change within its owning parent.
4. Run the installed helper using an existing Python environment with CadQuery and OCP. The request identifies the source and all selected targets. The job directory must have an existing parent. The helper publishes a separate result after saving and reopening. The request hash identifies a retry. A completed retry reads the hash-checked receipt, and an interrupted unpublished request starts from its original source.

   ```sh
   python scripts/batch_modification.py REQUEST.json JOB_DIRECTORY
   ```

   XCAF paths are slash-separated component label tags beneath the single assembly root. Read the tags beside the selected occurrences in the XCAF document tree. The example keeps the low-X end of one bar and the high-X end of another. The fixed seat is the centre of the corresponding end face in world coordinates. For a centre anchor the seat is the solid centre. A unitless XBF requires a source-confirmed millimetre convention.

   ```json
   {
     "model": "frame.xbf", "revision": "SHA-256 of frame.xbf", "unit": "mm",
     "operation": "bar length",
     "targets": [
       {"id":"1/1","axis":"x","anchor":"start"},
       {"id":"2/1","axis":"x","anchor":"end"}
     ],
     "values": {
       "1/1":{"length":{"value":32,"unit":"mm"}},
       "2/1":{"length":{"value":14,"unit":"mm"}}
     }
   }
   ```

   For a shared length use `"value":{"length":{"value":32,"unit":"mm"}}` in place of `values`. The bar readback includes the original and resulting length, seat, definition tags and the lengths and seats of unselected occurrences that shared the original leaf. Reopened leaf paths, transforms and material volumes are checked throughout the assembly. Use the native feature or assembly editor for profiled bars, constraints, tagged faces, or metadata-bearing definitions that need duplication.

   For `bore diameter`, a target is `{"id":"H1","anchor":"entry centre","entry":[5,7,5],"direction":[0,0,-1],"diameter":2,"depth":5,"end":"through"}`. Coordinates and original dimensions use millimetres. Supply `"value":{"diameter":{"value":4,"unit":"mm"}}` or one diameter per ID. The helper identifies the wall and both rims before editing, checks removed volume, then measures the entry, diameter, depth and exit or bottom in the reopened solid.

   For `occurrence name`, select named components with targets such as `{"id":"1/1"}` and supply `"value":{"name":"Left rail"}` or one name per occurrence path. The helper verifies the complete occurrence-name map after reopening.

## Resume related corrections

Run [correction_sequence.py](../scripts/correction_sequence.py) with a JSON plan and a job-owned cache directory. Supply an ordered `steps` array. Each step has a unique `id` and an `edit` containing a bore diameter, bar length or occurrence name request as described above. For an independent source supply its `model` relative to the plan and its `revision` hash. For a later edit of the same model set `after` to the earlier step ID and omit `model` and `revision`; its input is the verified output of that step. Use the diameter or dimensions present at that stage.

On failure read the reason beside the step ID. Dependent steps identify the failed predecessor; independent steps continue. A repeated run verifies saved requests, model hashes and readback before returning a cached output. The source hash, settings, predecessor and writer identity determine reuse.
