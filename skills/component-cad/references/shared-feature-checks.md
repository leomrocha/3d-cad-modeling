# Reuse a measured-feature check across components

Executed evidence: [driver iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c012-driver.md), [Leaf module iteration](https://github.com/leomrocha/3d-cad-modeling/blob/master/execution/c021-leaf-module.md). Code: [feature_checks.py](../scripts/feature_checks.py).

1. **Choose the action:** identify what repeats, such as comparing mounting-hole centres. Keep the source interpretation, native measurement, numerical comparison and visual inspection as separate actions with their own evidence.
2. **Bind independent expectations:** the component job supplies source-backed dimensions, expected axes/positions, units and a numerical comparison threshold. Record the source/hash/location beside every expectation before reading measured geometry. Project dimensions stay in FERME.
3. **Read actual geometry:** use the existing native reader on the selected saved component. Retain its document and geometry revisions, handles, actual surface observations and raw record. A component name or successful command response supplies identity; measured surfaces/vertices supply geometry.
4. **Select the supported function:** `comparison` compares finite numbers or nested numeric lists; `closed_body` checks one body/lump/shell with reciprocal closed coedges; `vertex_extrema` compares observed vertex coordinate ranges; `cylinder_pattern` compares circular-cylinder axes of a supplied diameter parallel to a supplied Cartesian axis, after deduplicating coincident patches. Callers provide expected values and component names.
5. **Keep measurement scope explicit:** vertex coordinate ranges describe actual vertices. A general curved surface may extend beyond them. The driver loft uses a separate native graph/vertex route and source-outline visual comparison; its surface equations remain outside the analytic reader. A closed graph check describes body connectivity. Nominal terminal cylinders retain their source representation labels.
6. **Check failure behaviour:** use the original driver connector-span failure, an incorrect mounting pitch and the corrected saved derivative. Reuse the same mounting-pattern function on actual Leaf and driver records with their different dimensions. Run affected earlier component tests after extraction.
7. **Record the improvement:** connect the observed repetition, previous procedure, extracted function, supported inputs, two exercised component cases, actual results and regression checks. Update component action occurrences and the shared action record; preserve original action graph boundaries.
8. **Use the improvement on later jobs:** software performs the supported comparison after source interpretation and geometry reading. The agent interprets unfamiliar drawings, selects applicable features/methods, reviews exceptions and inspects source/model views. Add another supported case only with its own evidence and checks.

## Exercised transfer

1. **Driver mounting plate:** four Ø13 mm bores,168×98 mm centres, axes parallel to local Z.
2. **Leaf module shells:** four Ø9.1 mm bores per shell at reconstructed X±138/Y±99 mm, axes parallel to local Z.
3. **Shared software:** both use `cylinder_pattern` with their own expected dimensions and native measurements. Both use the shared numerical comparator, closed-body check and vertex-extrema check.
4. **Agent work:** matching dimensions to physical features, retaining source/reconstruction labels, interpreting the driver116.7 mm connector-span dimension, choosing the bounded X2 correction and inspecting actual model/source views.
