# Replace selected occurrences or features

For a plain rigid XCAF assembly with one root, run
`python scripts/batch_modification.py request.json job-directory`. The command
publishes the reopened model as `result.xbf` with per-occurrence measurements.
It swaps the referenced definition on the selected occurrence label and isolates
shared ancestors before changing their children. All selected occurrences in
one request receive the same indexed STEP solid.

The request uses `operation: "replace occurrence"`, `unit: "mm"`, `model`
(source XBF), `revision` (source SHA-256) and `mates: ["fixed keyed seat"]`.
Under `replacement`, supply the indexed STEP `model`, its `revision`, and
`part` with `data`, `search_cli`, `query` and the reviewed catalogue `id`.
Resolve file paths relative to the request. In `replacement.corners` identify
three vertices of the catalogue part's rectangular seat in definition-local
millimetres. Give the first corner, its neighbour along the key direction,
and its neighbour across the width. Their cross product points out of the
solid. The face centre is the mounting-axis origin.

Each entry in `targets` supplies the stable slash-separated component-tag
`id` and the original part's ordered `corners`. For an opposing mating
occurrence, also supply `partner` with its `id` and its ordered `corners`.
Select the partner's key along the same physical direction and its normal
toward the selected part. Check each partner entry before submitting.
The operation measures both interfaces, requires matching key length and
width, and compares the complete seating frame after reopening. A fixed
seat without a partner retains its measured world frame. The partner's contact rectangle must have the same dimensions. Exactly one
occurrence may have a same-facing coplanar face overlapping the seat area.
The proposed and reopened solids are checked for new interference volume
against every other occurrence, including the partner and other replacements.
The source, request and result hashes identify the published batch.
After interruption, run the same command with the same request and directory.
Publication exposes the entire verified assembly in one filesystem operation.

For native solver mates, nonrectangular interfaces, assembly replacements or
features with dependents, use the owning CAD application's reference-swap
or replace-feature operation. Record the host ID, original feature ID,
replacement definition, support face or sketch, dimensional references,
mate identifiers and the expected values and units. Bind each dependent to
its corresponding replacement reference in a separate native revision.
Regenerate and reopen. Check the host solid and feature count, replacement
dimensions and seat, each retained constraint's attachment and solved value,
each downstream dimension and an independent feature. If the provider
cannot preserve an attachment, record its target and the unresolved reference
before publishing the revision.
