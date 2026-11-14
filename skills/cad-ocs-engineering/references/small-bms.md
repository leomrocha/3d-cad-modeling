# Saved body and assembly persistence

1. [small_bms.py](../scripts/small_bms.py) retains its legacy import name and exposes generic SAT/SAB body-vertex and assembly-instance comparison functions.
2. compare_sat_sab requires pre-save identity-frame SAT points and saved reachable SAB vertices, with an explicit comparison precision. Record vertex equality, body topology, surface families and the supported body transform separately.
3. compare_assembly_instances compares native occurrence paths and rigid matrices before/after saving. assembly_point_extrema reports placed observed vertices. [native_geometry.py](../scripts/native_geometry.py) adds explicit positive-uniform and mirrored traversal modes.
4. A point-set comparison describes the vertices read. Curved-surface extrema and unsupported surface equations require their own method. Retain exact source/saved hashes and the model's representation.
