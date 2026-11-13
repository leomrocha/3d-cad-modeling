# Source-bound non-geometric component tasks

Use this classification only when the component input explicitly states that no CAD geometry is required. The classification is a caller-supplied job declaration; the checker does not infer it from a component name, group, prose or feature values.

```json
{
  "geometry_requirement": {
    "kind": "non_geometric_consumable",
    "cad_required": false,
    "source": {
      "path": "${PROJECT_ROOT}/inputs/part.md",
      "sha256": "<64 hexadecimal characters>",
      "location": "Exact section or page that defines the no-CAD scope"
    }
  }
}
```

1. Pin the exact source file and source location that defines the classification. Resolve named path roots through the caller's explicit root map; an unrooted relative path is rejected.
2. `component_records.readiness()` returns `SOURCE_READY_NON_GEOMETRIC` only when the enum, literal boolean, source location and current source hash all validate. `require_ready()` rejects this state, so geometry builders that use that gate cannot construct a solid for the consumable.
3. `model_inventory.start_check()` returns `SKIP_NON_GEOMETRIC` only when no linked matching model or filename candidate exists. Existing models remain `SKIP_EXISTING_MODEL`; candidates remain `REVIEW_EXISTING_CANDIDATES`. A malformed or stale source binding fails closed.
4. A task containing alternative physical and consumable branches cannot receive a whole-task non-geometric classification. Classify a branch separately only when the job schema binds that declaration to the exact alternative.

Example distinction: an applied threadlocker can be a non-geometric consumable; a Belleville washer is physical CAD geometry and requires its own sourced part record. This procedure does not select between those alternatives.
