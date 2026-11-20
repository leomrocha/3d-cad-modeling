"""Read DXF geometry and reachable rigid block references for batch selection."""

from batch_dxf_lines import drawing
from operation_catalogue import file_digest
from step_placements import classify_hand, cross, unit


def read_inventory(model, model_unit):
    revision = file_digest(model)
    doc = drawing(model, model_unit)
    definitions = {}

    def inspect(layout):
        name = layout.name
        if name in definitions:
            return
        rows = definitions[name] = []
        for e in layout:
            kind = e.dxftype()
            if kind not in ("LINE", "CIRCLE", "POINT", "INSERT", "LWPOLYLINE"):
                continue
            d = e.dxf
            row = dict(id=d.handle, name=d.layer, kind=kind, anchors={}, directions={}, reference_kinds=[])
            if kind == "INSERT":
                row.update(name=d.name, geometry={"block": d.name})
                try:
                    if e.mcount != 1:
                        raise ValueError("Multiple INSERT arrays require individual occurrence IDs")
                    matrix = [list(col) for col in e.matrix44().columns()]
                    classify_hand(matrix)
                except ValueError as exc:
                    row["unsupported"] = str(exc)
                else:
                    row.update(definition=d.name, matrix=matrix)
                    row["anchors"]["block base"] = list(doc.blocks[d.name].block.dxf.base_point)
                    inspect(doc.blocks[d.name])
            elif kind == "LINE":
                start, end = d.start, d.end
                direction = list(end - start)
                row.update(geometry=dict(start=list(start), end=list(end), normal=list(d.extrusion)),
                           anchors=dict(start=list(start), end=list(end)), reference_kinds=["edge", "axis", "centreline"],
                           current=dict(value=(end-start).magnitude, unit=model_unit))
                if (end-start).magnitude:
                    row["directions"]["along"] = unit(direction)
                    left = cross(unit(d.extrusion), unit(direction))
                    if any(left):
                        row["directions"]["left"] = unit(left)
            elif kind == "CIRCLE":
                centre = list(e.ocs().to_wcs(d.center))
                row.update(geometry=dict(centre=centre, radius=d.radius, normal=list(d.extrusion)),
                           anchors=dict(centre=centre), directions=dict(normal=list(d.extrusion)),
                           current=dict(value=d.radius, unit=model_unit), reference_kinds=["existing feature"])
            elif kind == "POINT":
                row.update(geometry=dict(point=list(d.location)), anchors=dict(vertex=list(d.location)),
                           reference_kinds=["vertex"])
            else:
                vertices = [list(v) for v in e.vertices_in_wcs()]
                row.update(geometry=dict(vertices=vertices, profile=[list(v) for v in e.get_points("seb")],
                                         closed=e.closed, normal=list(d.extrusion)),
                           anchors={str(i): v for i, v in enumerate(vertices)}, reference_kinds=["vertex"])
            for axis, vector in zip(("frame-x", "frame-y", "frame-z"), ((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                row["directions"][axis] = list(vector)
            rows.append(row)
    inspect(doc.modelspace())
    if file_digest(model) != revision:
        raise ValueError("DXF changed while reading selection")
    return dict(model=str(model), model_unit=model_unit, revision=revision, root=doc.modelspace().name,
                definitions=definitions, named={name: [[e.dxf.handle] for e in group]
                                                for name, group in doc.groups})
