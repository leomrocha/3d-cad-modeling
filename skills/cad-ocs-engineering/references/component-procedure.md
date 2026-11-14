# Component source and action records

1. Use [part_index.py](../scripts/part_index.py) with explicit --index paths. A component list or dictionary with entries retains its original record fields and source hash. Select an exact ID with --id or supplied text with --query.
2. Supply job_id, part_id, readable part_name, representation, units, frame and required features to [component_records.py](../scripts/component_records.py). Each value carries its source file, digest, location and evidence status. Each unresolved required feature carries its exact question.
3. readiness returns SOURCE_READY or NEEDS_INPUT; require_ready rejects incomplete requirements or changed source bytes before dependent construction.
4. append_occurrence writes locked append-only action evidence with unique occurrence ID, readable action/component names, inputs, outputs, prerequisites, representations, units/frames, software, changes, checks and result. Preserve failed attempts.
5. Job inputs and results remain in caller-owned storage. [Model reuse](existing-model-start-check.md) precedes construction. Use the [bundled runtime](ocs-runtime.md), [incremental saves](../SKILL.md#save-work-in-progress) and [retained artifact checks](retained-artifact-checks.md).
