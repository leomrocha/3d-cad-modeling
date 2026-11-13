"""Source-recorded smallBMS assembly persistence checks.

This module compares the existing OCS SAT point records with saved native SAB
body graphs. It creates no geometry and makes no OCS requests.
"""

from native_acis import sab_structure
from step_placements import apply, identity_sat_vertices, near, solid_instances


def _canonical_points(points, decimals=7):
    if type(decimals) is not int or decimals < 0:
        raise ValueError("Nonnegative point-comparison precision required")
    return sorted(set(tuple(round(float(value), decimals) for value in point)
                      for point in points))


def compare_sat_sab(sat_data, sab_data, decimals=7):
    """Compare one pre-save SAT body's observed vertices with saved SAB vertices."""
    if not isinstance(sat_data, str) or not sat_data:
        raise ValueError("Nonempty pre-save SAT data required")
    if not isinstance(sab_data, (bytes, bytearray)) or not sab_data:
        raise ValueError("Nonempty reopened SAB data required")
    before = identity_sat_vertices(sat_data)
    after = sab_structure(bytes(sab_data), allow_rigid=True)
    old = _canonical_points(before, decimals)
    new = _canonical_points(after["points"], decimals)
    return {
        "result": "PASS" if old == new else "FAIL",
        "method": "canonical reachable SAT/SAB vertex sets; native body graph",
        "coordinate_unit": "mm as recorded by the source STEP/import job",
        "rounding_decimals": decimals,
        "pre_save_vertex_count": len(before),
        "pre_save_unique_vertex_count": len(old),
        "reopened_vertex_count": len(after["points"]),
        "reopened_unique_vertex_count": len(new),
        "topology": after["topology"],
        "surface_types": after["surface_types"],
        "reopened_body_transform": after.get("body_transform"),
    }


def compare_assembly_instances(before_records, before_blocks, before_roots,
                              after_records, after_blocks, after_roots):
    """Compare placed-solid traversal paths and rigid transforms before/after save."""
    before = solid_instances(before_records, before_blocks, before_roots)
    after = solid_instances(after_records, after_blocks, after_roots)
    checks = []
    if len(before) != len(after):
        checks.append({"check": "placed solid instance count", "before": len(before),
                       "after": len(after), "result": "FAIL"})
    else:
        for index, (old, new) in enumerate(zip(before, after)):
            passed = old["path"] == new["path"] and near(old["matrix"], new["matrix"])
            checks.append({"check": "placed solid instance " + str(index + 1),
                           "before_path": old["path"], "after_path": new["path"],
                           "result": "PASS" if passed else "FAIL"})
    return {"result": "PASS" if checks and all(c["result"] == "PASS" for c in checks) else "FAIL",
            "method": "existing block traversal and rigid-transform comparison",
            "before_instance_count": len(before), "after_instance_count": len(after),
            "checks": checks}


def assembly_point_extrema(records, block_records, root_handles):
    """Return placed point extrema with an explicit point-set measurement label."""
    by_handle = {record["handle"]: record for record in records}
    instances = solid_instances(records, block_records, root_handles)
    placed = []
    for instance in instances:
        data = by_handle[instance["handle"]]["properties"]["acis_data"]
        points = identity_sat_vertices(data["sat_data"])
        placed.extend(apply(instance["matrix"], point) for point in points)
    if not placed:
        raise ValueError("No placed solid point records found")
    ranges = [[min(p[axis] for p in placed), max(p[axis] for p in placed)]
              for axis in range(3)]
    return {"measurement": "placed native vertex-point ranges",
            "coordinate_unit": "mm", "instances": len(instances),
            "vertex_point_count": len(placed), "ranges": ranges,
            "spans": [high - low for low, high in ranges],
            "curved_surface_extrema": "not established by vertex points"}
