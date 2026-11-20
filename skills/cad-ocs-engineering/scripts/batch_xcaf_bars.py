"""Isolate and resize plain rectangular bars in a binary XCAF assembly."""

import math
from pathlib import Path

from batch_creation import TOL
from batch_modification import dimension_target, reviewed_values, solid_difference


def open_document(path):
    from OCP.BinXCAFDrivers import BinXCAFDrivers
    from OCP.PCDM import PCDM_ReaderStatus
    from OCP.TCollection import TCollection_ExtendedString as String
    from OCP.TDocStd import TDocStd_Application
    from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_LengthUnit
    from OCP.TDF import TDF_LabelSequence

    path = Path(path).resolve()
    if path.suffix.lower() != ".xbf":
        raise ValueError("Select a binary XCAF assembly")
    app = TDocStd_Application()
    BinXCAFDrivers.DefineFormat_s(app)
    doc = app.Retrieve(String(str(path.parent), True), String(path.name, True))
    if app.GetRetrieveStatus() != PCDM_ReaderStatus.PCDM_RS_OK:
        raise ValueError("Cannot open XCAF assembly")
    unit = XCAFDoc_LengthUnit()
    root = doc.Main().Root()
    if root.IsAttribute(unit.GetID_s()) and root.FindAttribute(unit.GetID_s(), unit):
        if not math.isclose(unit.GetUnitValue(), 0.001):
            raise ValueError("XCAF length unit differs from the requested millimetres")
    tool = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    roots = TDF_LabelSequence()
    tool.GetFreeShapes(roots)
    if roots.Length() != 1 or not tool.IsAssembly_s(roots.First()):
        raise ValueError("Select a document with one assembly root")
    return app, doc, tool, roots.First()


def children(tool, parent):
    from OCP.TDF import TDF_LabelSequence

    seq = TDF_LabelSequence()
    tool.GetComponents_s(parent, seq)
    return {str(child.Tag()): child for child in seq}


def referred(tool, component):
    from OCP.TDF import TDF_Label

    ref = TDF_Label()
    if not tool.GetReferredShape_s(component, ref):
        raise ValueError("Expected a local component reference")
    return ref


def check_plain(label):
    from OCP.TDF import TDF_AttributeIterator
    from OCP.XCAFDoc import XCAFDoc

    it = TDF_AttributeIterator(label)
    while it.More():
        attr = it.Value()
        kind = attr.DynamicType().Name()
        if kind == "TDataStd_TreeNode":
            plain = attr.ID().IsSame(XCAFDoc.ShapeRefGUID_s())
        elif kind == "TDataStd_UAttribute":
            plain = attr.ID().IsSame(XCAFDoc.AssemblyGUID_s())
        else:
            plain = kind in (
                "TDataStd_Name",
                "TNaming_NamedShape",
                "TDF_TagSource",
                "XCAFDoc_Location",
            )
        if not plain:
            raise ValueError("Attributed variant requires the owning native provider")
        it.Next()


def copy_name(source, target):
    from OCP.TDataStd import TDataStd_Name

    attr = TDataStd_Name()
    if source.IsAttribute(TDataStd_Name.GetID_s()) and source.FindAttribute(
        TDataStd_Name.GetID_s(), attr
    ):
        TDataStd_Name.Set_s(target, attr.Get())


def independent(tool, component):
    """Copy on write along one actual occurrence path; retain component tags."""
    from OCP.TDataStd import TDataStd_TreeNode
    from OCP.TDF import TDF_LabelSequence
    from OCP.XCAFDoc import XCAFDoc

    original = referred(tool, component)
    check_plain(original)
    parts = children(tool, original)
    if original.NbChildren() != len(parts):
        raise ValueError("Subshape attributes require the owning native provider")
    if tool.GetUsers_s(original, TDF_LabelSequence()) == 1:
        return original
    variant = tool.NewShape()
    copy_name(original, variant)
    if parts:
        for tag, old in parts.items():
            check_plain(old)
            if old.NbChildren():
                raise ValueError(
                    "Nested component attributes require the owning provider"
                )
            new = tool.AddComponent(
                variant, referred(tool, old), tool.GetLocation_s(old)
            )
            if str(new.Tag()) != tag:
                raise ValueError(
                    "Sparse component tags require native variant creation"
                )
            copy_name(old, new)
    else:
        tool.SetShape(variant, tool.GetShape_s(original))
    guid = XCAFDoc.ShapeRefGUID_s()
    link = TDataStd_TreeNode.Set_s(component, guid)
    link.Remove()
    TDataStd_TreeNode.Set_s(variant, guid).Append(link)
    return variant


def inventory(tool, root):
    import cadquery as cq

    result = {}

    def collect(parent, path, frame):
        for tag, occurrence in children(tool, parent).items():
            key = "/".join((*path, tag))
            definition = referred(tool, occurrence)
            world = frame * cq.Location(tool.GetLocation_s(occurrence))
            if tool.IsAssembly_s(definition):
                collect(definition, (*path, tag), world)
            else:
                shape = cq.Shape.cast(tool.GetShape_s(definition))
                result[key] = (definition.Tag(), world, shape)

    collect(root, (), cq.Location(tool.GetLocation_s(root)))
    return result


def box_limits(shape, axis):
    if axis not in ("x", "y", "z"):
        raise ValueError("Specify the definition-local x, y or z axis")
    error = "Bar operation requires one axis-aligned rectangular solid"
    while shape.ShapeType() == "Compound":
        members = list(shape)
        if len(members) != 1:
            raise ValueError(error)
        shape = members[0]
    faces = shape.Faces()
    if shape.ShapeType() != "Solid" or not shape.isValid() or len(faces) != 6:
        raise ValueError(error)
    points = [v.toTuple() for v in shape.Vertices()]
    if len(points) != 8:
        raise ValueError(error)
    lo = list(map(min, zip(*points)))
    hi = list(map(max, zip(*points)))
    if any(b - a <= 2 * TOL for a, b in zip(lo, hi)):
        raise ValueError("Bar thickness is unresolved at the linear tolerance")
    sides = set()
    for face in faces:
        edges = face.Edges()
        if (
            face.geomType() != "PLANE"
            or len(edges) != 4
            or any(edge.geomType() != "LINE" for edge in edges)
        ):
            raise ValueError(error)
        corners = set()
        for vertex in face.Vertices():
            point = vertex.toTuple()
            corner = tuple(
                int(abs(p - b) < abs(p - a)) for p, a, b in zip(point, lo, hi)
            )
            nominal = tuple((a, b)[i] for i, a, b in zip(corner, lo, hi))
            if math.dist(point, nominal) > TOL:
                raise ValueError(error)
            corners.add(corner)
        if len(corners) != 4:
            raise ValueError(error)
        planes = [
            (axis_index, coordinates[0])
            for axis_index, coordinates in enumerate(zip(*corners))
            if len(set(coordinates)) == 1
        ]
        if len(planes) != 1 or planes[0] in sides:
            raise ValueError(error)
        sides.add(planes[0])
    return lo, hi


def measurement(shape, frame, axis, anchor):
    import cadquery as cq

    lo, hi = box_limits(shape, axis)
    i = "xyz".index(axis)
    point = [(a + b) / 2 for a, b in zip(lo, hi)]
    if anchor == "start":
        point[i] = lo[i]
    elif anchor == "end":
        point[i] = hi[i]
    elif anchor != "centre":
        raise ValueError("Specify start, centre or end as the fixed bar anchor")
    world = cq.Vertex.makeVertex(*point).moved(frame).Center()
    return dict(length=hi[i] - lo[i], seat=list(world.toTuple()))


def occurrence_name(label):
    from OCP.TDataStd import TDataStd_Name

    attribute = TDataStd_Name()
    if label.IsAttribute(TDataStd_Name.GetID_s()) and label.FindAttribute(
        TDataStd_Name.GetID_s(), attribute
    ):
        return attribute.Get().ToExtString()
    return None


def rename_occurrences(spec, output):
    from OCP.TCollection import TCollection_ExtendedString as String
    from OCP.TDataStd import TDataStd_Name
    from batch_request import prepare

    app, doc, tool, root = open_document(spec["model"])

    def names(tool, parent, path=()):
        found = {}
        for tag, child in children(tool, parent).items():
            child_path = (*path, tag)
            found["/".join(child_path)] = occurrence_name(child)
            found.update(names(tool, referred(tool, child), child_path))
        return found

    before = names(tool, root)
    targets = [
        dict(
            id=r["id"], current={"name": before[r["id"]]}, reference="occurrence label"
        )
        for r in spec["targets"]
    ]
    rows = prepare(
        dict(
            model=spec["model"],
            revision=spec["revision"],
            action="modify",
            entity="XCAF occurrence",
            output="occurrence name",
            model_unit="mm",
            targets=targets,
            **{k: spec[k] for k in ("value", "values") if k in spec},
        ),
        {"operations": []},
    ).read()["rows"]
    expected = dict(before)
    for row in rows:
        key = row["target"]
        name = row["requested"]["name"]
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Specify a nonempty occurrence name")
        if expected[key] == name:
            continue
        parent = root
        *ancestors, tag = key.split("/")
        for ancestor in ancestors:
            parent = independent(tool, children(tool, parent)[ancestor])
        TDataStd_Name.Set_s(children(tool, parent)[tag], String(name, True))
        expected[key] = name
    save_document(app, doc, tool, output)
    saved_app, saved_doc, saved_tool, saved_root = open_document(output)
    if names(saved_tool, saved_root) != expected:
        raise ValueError("Reopened occurrence names differ")
    return [
        dict(id=row["target"], before=row["current"], after=row["requested"])
        for row in rows
    ]


def save_document(app, doc, tool, output):
    from OCP.PCDM import PCDM_StoreStatus
    from OCP.TCollection import TCollection_ExtendedString as String

    tool.UpdateAssemblies()
    if app.SaveAs(doc, String(str(output), True)) != PCDM_StoreStatus.PCDM_SS_OK:
        raise ValueError("XCAF save failed")


def modify_bars(spec, output):
    import cadquery as cq

    app, doc, tool, root = open_document(spec["model"])
    initial = inventory(tool, root)
    targets, before = [], {}
    for row in spec["targets"]:
        key, axis, anchor = row["id"], row["axis"], row["anchor"]
        _, frame, shape = initial[key]
        before[key] = measurement(shape, frame, axis, anchor)
        targets.append(dimension_target(key, anchor, "length", before[key]["length"]))
    lengths = reviewed_values(spec, targets, "length")
    expected = {}
    for row in spec["targets"]:
        key, axis, anchor = row["id"], row["axis"], row["anchor"]
        if abs(lengths[key] - before[key]["length"]) <= TOL:
            continue
        parent = root
        for tag in key.split("/"):
            component = children(tool, parent)[tag]
            parent = independent(tool, component)
        lo, hi = box_limits(initial[key][2], axis)
        i = "xyz".index(axis)
        delta = lengths[key] - before[key]["length"]
        offset = {"start": 0, "centre": 0.5, "end": 1}[anchor]
        lo[i] -= offset * delta
        hi[i] += (1 - offset) * delta
        expected[key] = cq.Solid.makeBox(
            *(b - a for a, b in zip(lo, hi)), cq.Vector(*lo)
        )
        tool.SetShape(parent, expected[key].wrapped)
    save_document(app, doc, tool, output)
    saved_app, saved_doc, saved_tool, saved_root = open_document(output)
    saved = inventory(saved_tool, saved_root)
    if set(saved) != set(initial):
        raise ValueError("Occurrence paths changed")
    result = []
    for key, (definition, frame, shape) in saved.items():
        old_id, old_frame, original = initial[key]
        delta = old_frame.inverse * frame
        transform = delta.wrapped.Transformation()
        if any(
            abs(transform.Value(i, j) - float(i == j)) > TOL
            for i in range(1, 4)
            for j in range(1, 5)
        ):
            raise ValueError(f"Occurrence moved at {key}")
        if key not in expected and old_id != definition:
            raise ValueError(f"Unmodified definition changed at {key}")
        if solid_difference(shape, expected.get(key, original)) > TOL:
            raise ValueError(f"Persisted material differs at {key}")
    for row in spec["targets"]:
        key, axis, anchor = row["id"], row["axis"], row["anchor"]
        definition, frame, shape = saved[key]
        after = measurement(shape, frame, axis, anchor)
        if (
            abs(after["length"] - lengths[key]) > TOL
            or math.dist(before[key]["seat"], after["seat"]) > TOL
        ):
            raise ValueError(f"Reopened bar length or fixed seat differs at {key}")
        peers = []
        for other, (old_id, old_frame, original) in initial.items():
            if old_id == initial[key][0] and other not in lengths:
                _, other_frame, other_shape = saved[other]
                peers.append(
                    dict(
                        id=other, **measurement(other_shape, other_frame, axis, anchor)
                    )
                )
        result.append(
            dict(
                id=key,
                anchor=anchor,
                axis=axis,
                before=before[key],
                after=after,
                original_definition=initial[key][0],
                saved_definition=definition,
                unselected=peers,
            )
        )
    return result
