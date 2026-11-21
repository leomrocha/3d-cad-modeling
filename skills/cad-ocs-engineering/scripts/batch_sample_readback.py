"""Read native results for the retained engineering batch qualification sample."""

import math

from batch_creation import (
    TOL,
    load_solid,
    measure_cut,
    patterns,
    needs_disk_clearances,
    measure_disk_clearances,
)
from operation_catalogue import file_digest


def close(actual, expected):
    if isinstance(expected, (list, tuple)):
        return len(actual) == len(expected) and all(
            close(x, y) for x, y in zip(actual, expected)
        )
    if isinstance(expected, dict):
        return actual.keys() == expected.keys() and all(
            close(actual[k], v) for k, v in expected.items()
        )
    if type(expected) in (int, float):
        return math.isclose(actual, expected, rel_tol=1e-9, abs_tol=TOL)
    return actual == expected


def require(actual, expected, field):
    if not close(actual, expected):
        raise ValueError(f"Saved sample {field} differs from its request or readback")


def target_ids(spec):
    if "rows" in spec:
        ids = [r["target"] for r in spec["rows"]]
    elif "pattern" in spec:
        from planar_positions import generate

        ids = [r["id"] for r in generate(spec["pattern"])["positions"]]
    else:
        ids = [r["id"] for r in spec["targets"]]
    if (
        not ids
        or any(not isinstance(k, str) or not k.strip() for k in ids)
        or len(ids) != len(set(ids))
    ):
        raise ValueError("Expected unique, nonempty reviewed target IDs")
    return ids


def measured_ids(elements):
    ids = []
    for element in elements:
        key = element.get("id", element.get("after", {}).get("id"))
        if not key or key in ids:
            raise ValueError("Missing or duplicate readback target ID")
        ids.append(key)
    return ids


def value(spec, key, field):
    record = spec["value"] if "value" in spec else spec["values"][key]
    item = record[field]
    if isinstance(item, dict):
        from batch_request import normalize

        return normalize(
            item, spec.get("unit", spec.get("pattern", {}).get("unit", "mm"))
        )["value"]
    return item


def verified_clearances(pattern, actual, recorded):
    measure_disk_clearances(pattern, actual, "centre")
    result = {}
    for row, receipt in zip(actual, recorded, strict=True):
        fields = {
            k: row[k]
            for k in ("outer_clearance", "minimum_cutout_clearance")
            if k in row
        }
        for key, measured in fields.items():
            if key in receipt:
                require(receipt[key], measured, key)
        result[row["id"]] = fields
    return result


def verify_creation(spec, source, output, elements):
    operation = spec["operation"]
    _, rows, normal = patterns(spec)
    footprint = needs_disk_clearances(spec)
    disks = []
    require(measured_ids(elements), [r["id"] for r in rows], "target order")
    if operation == "circle":
        from batch_dxf_lines import drawing
        from batch_insert_recovery import baseline

        before, after = (
            drawing(path, spec["pattern"]["unit"]) for path in (source, output)
        )
        handles = [e["handle"] for e in elements]
        if len(set(handles)) != len(rows) or baseline(before) != baseline(
            after, handles
        ):
            raise ValueError("Saved sample circle membership differs")
        for r, e in zip(rows, elements):
            item = after.entitydb[e["handle"]]
            if (
                item.dxftype() != "CIRCLE"
                or before.entitydb.get(e["handle"]) is not None
            ):
                raise ValueError("Expected a new sample circle")
            centre = list(item.ocs().to_wcs(item.dxf.center))
            disks.append(dict(id=r["id"], centre=centre, diameter=item.dxf.radius * 2))
            for actual, expected, label in [
                (centre, r["xyz"], "centre"),
                (centre, e["centre"], "recorded centre"),
                (item.dxf.radius * 2, value(spec, r["id"], "diameter"), "diameter"),
                (item.dxf.radius * 2, e["diameter"], "recorded diameter"),
                (list(item.dxf.extrusion), normal, "normal"),
                (list(item.dxf.extrusion), e["normal"], "recorded normal"),
            ]:
                require(actual, expected, label)
        return (
            verified_clearances(spec["pattern"], disks, elements) if footprint else None
        )
    import cadquery as cq

    shape = load_solid(source)
    if operation == "cut":
        saved = load_solid(output)
        axis = cq.Vector(*normal) * (1 if spec["direction"] == "+normal" else -1)
        removed = 0
        for r, e in zip(rows, elements):
            r["value"] = {
                k: value(spec, r["id"], k) for k in ("diameter", "depth", "end")
            }
            actual = measure_cut(saved, r, axis)
            disks.append(
                dict(id=r["id"], centre=actual["entry"], diameter=actual["diameter"])
            )
            for k, v in actual.items():
                require(e[k], v, k)
            removed += math.pi * (r["value"]["diameter"] / 2) ** 2 * r["value"]["depth"]
        require(shape.Volume() - saved.Volume(), removed, "cut volume")
        return (
            verified_clearances(spec["pattern"], disks, elements) if footprint else None
        )
    from batch_modification import solid_difference

    assembly = cq.Assembly.load(str(output))
    children = {c.name: c for c in assembly.children}
    require(sorted(children), sorted(r["id"] for r in rows), "occurrences")
    shared = assembly.children[0].obj
    require(solid_difference(shared, shape), 0, "catalogue solid")
    from batch_replacement import matrix

    for r, e in zip(rows, elements):
        child = children[r["id"]]
        if not child.obj.wrapped.IsPartner(shared.wrapped):
            raise ValueError("Saved occurrences require a shared definition")
        require(matrix(child.loc), r["matrix"][:3], "occurrence frame")
        require(matrix(child.loc), e["frame"], "recorded frame")
        require(e["definition"], spec["part"]["id"], "part identity")


def verify_bores(spec, source, output, elements):
    import cadquery as cq
    from batch_modification import retained_bores

    before, after = load_solid(source), load_solid(output)
    changes = []
    for row, element in zip(spec["targets"], elements):
        axis = cq.Vector(*row["direction"])
        measured = dict(
            id=row["id"],
            xyz=row["entry"],
            value={k: row[k] for k in ("diameter", "depth", "end")},
        )
        original = measure_cut(before, measured, axis)
        measured["value"]["diameter"] = value(spec, row["id"], "diameter")
        result = measure_cut(after, measured, axis)
        require(original, element["before"], "original bore")
        require(result, element["after"], "saved bore")
        changes.append(not close(original["diameter"], result["diameter"]))
    if not any(changes):
        raise ValueError("Sample bore diameter did not change")
    peers = retained_bores(before, after, [r["entry"] for r in spec["targets"]])
    for e in elements:
        if "unselected" in e:
            require(peers, e["unselected"], "retained bores")


def verify_assembly(spec, root, source, output, elements):
    from batch_xcaf_bars import (
        children,
        inventory,
        measurement,
        occurrence_name,
        open_document,
        referred,
    )
    from batch_replacement import interface, matrix, occupants
    from batch_modification import solid_difference

    # Keep both document owners alive while evaluating the shape tools.
    docs = [open_document(path) for path in (source, output)]
    original, saved = [inventory(doc[2], doc[3]) for doc in docs]
    require(sorted(original), sorted(saved), "occurrence paths")
    operation = spec["operation"]
    changed = False
    for row, e in zip(spec["targets"], elements):
        key = row["id"]
        if operation == "occurrence name":
            names = []
            for _, _, tool, parent in docs:
                for tag in key.split("/"):
                    item = children(tool, parent)[tag]
                    parent = referred(tool, item)
                names.append(occurrence_name(item))
            require(
                names, [e["before"]["name"], e["after"]["name"]], "occurrence names"
            )
            require(names[1], value(spec, key, "name"), "requested name")
            changed |= names[0] != names[1]
            continue
        old, old_frame, old_shape = original[key]
        new, frame, shape = saved[key]
        if operation == "bar length":
            for geometry, location, label in [
                (old_shape, old_frame, "before"),
                (shape, frame, "after"),
            ]:
                require(
                    measurement(geometry, location, row["axis"], row["anchor"]),
                    e[label],
                    label,
                )
            require(e["after"]["seat"], e["before"]["seat"], "fixed seat")
            require(
                e["after"]["length"], value(spec, key, "length"), "requested length"
            )
            changed |= not close(e["before"]["length"], e["after"]["length"])
        else:
            asset = spec["replacement"]
            path = root / asset["model"]
            require(file_digest(path), asset["revision"], "asset revision")
            require(solid_difference(shape, load_solid(path)), 0, "replacement shape")
            require(e["catalogue_id"], asset["part"]["id"], "catalogue ID")
            require(
                [old, new],
                [e["original_definition"], e["saved_definition"]],
                "definition IDs",
            )
            old_seat, _, _ = interface(old_shape, row["corners"])
            seat, dims, face = interface(shape, asset["corners"])
            require(matrix(frame * seat), matrix(old_frame * old_seat), "keyed seat")
            require(matrix(frame * seat), e["seat_frame"], "recorded seat")
            require(dims, e["interface_mm"], "seat dimensions")
            require(occupants(saved, face.moved(frame)), [key], "seat occupants")
            changed |= old != new
    if not changed:
        raise ValueError("Sample did not change the selected assembly property")


def verify_native(spec, root, source, output, elements):
    ids = target_ids(spec)
    keys = measured_ids(elements)
    if set(keys) != set(ids):
        raise ValueError("Sample readback target IDs differ from the request")
    indexed = dict(zip(keys, elements))
    elements = [indexed[k] for k in ids]
    if "pattern" in spec:
        verify_creation(spec, source, output, elements)
    elif spec["operation"] == "bore diameter":
        verify_bores(spec, source, output, elements)
    else:
        verify_assembly(spec, root, source, output, elements)
