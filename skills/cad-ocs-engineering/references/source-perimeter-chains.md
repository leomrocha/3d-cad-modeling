# Source-vector perimeter reconstruction

1. Retain source bytes, hash, page/view, path index, path-local subpath ordinal and segment ordinal. Verify every stored label resolves in the exact source before construction.
2. [source_vector_paths.py](../scripts/source_vector_paths.py) parses supported SVG M/L/C/Z segments and retains source identities. Supply the explicit six-term page transform, unit conversion, local origin and Y-axis sign.
3. Select the intended perimeter by inspected source geometry. Record each segment's transformed endpoints/control points and the exact join order. Compare endpoint continuity and independently printed spans before constructing a profile.
4. Keep cubic evaluation/sampling and simplification error distinct from source dimensions and manufacturing tolerances. A source identifier from another revision remains its own failed binding; preserve the failed label and corrected source association.
5. Use [profile validation](../scripts/profile_reference.py), [calibrated tracing](calibrated-trace.md) and [bounded native extrusion](generic-integration.md) for the supported downstream representation. Retain source references in caller-owned job records.
