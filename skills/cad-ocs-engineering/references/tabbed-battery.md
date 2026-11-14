# Check named exterior solids and repeated planar recesses

1. Supply the exact component source job, required native part names and independently sourced dimensions to [battery_module.check_tabbed_case](../scripts/battery_module.py). Keep source claims and reconstructed details separately labeled.
2. Select named measurement groups for support extent, body extent, overall height and repeated recess boundaries. Read actual saved SAB records and metadata through the supported native reader.
3. Coplanar Boolean fragments may share internal edges. The native reader cancels shared edges and groups the remaining outer/hole boundaries. [planar_boundary_pattern](../scripts/feature_checks.py) compares supplied plane level, closed-boundary centres and spans.
4. Check required body closure, mounting cylinders, named measurement groups, recess count/positions and source metadata. Vertex extrema describe measured vertices; a general curved exterior may need analytic measurements.
5. Preserve the exact source/model revision and actual failed observations. Save requested derivatives incrementally and verify final persisted geometry and view identity separately.
