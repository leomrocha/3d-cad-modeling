"""Swap plain XCAF leaf references using measured rectangular keyed seating faces."""

import math
import subprocess

from batch_creation import TOL, load_solid, selected_part
from batch_modification import solid_difference
from batch_xcaf_bars import (
    check_plain,
    children,
    independent,
    inventory,
    occurrence_name,
    open_document,
    referred,
    save_document,
)
from operation_catalogue import file_digest


def interface(shape, points):
    """Select a planar rectangle by a corner, its keyed neighbour and its other neighbour."""
    import cadquery as cq

    if len(points) != 3 or any(
        len(p) != 3 or not all(math.isfinite(v) for v in p) for p in points
    ):
        raise ValueError("Specify three finite definition-local points in mm")
    origin, along, across = (cq.Vector(*p) for p in points)
    x, y = along - origin, across - origin
    if min(x.Length, y.Length) <= TOL or abs(x.normalized().dot(y.normalized())) > 1e-9:
        raise ValueError("Seat edges must be perpendicular and measurable")
    corners = [origin, along, across, along + y]

    def matches(face):
        vertices = [v.Center() for v in face.Vertices()]
        return (
            face.geomType() == "PLANE"
            and len(vertices) == 4
            and len(face.Edges()) == 4
            and all(e.geomType() == "LINE" for e in face.Edges())
            and all(sum((p - v).Length <= TOL for v in vertices) == 1 for p in corners)
        )

    faces = [face for face in shape.Faces() if matches(face)]
    if not faces:
        footprint = cq.Face.makeFromWires(cq.Wire.makePolygon([origin, along, along+y, across], close=True))
        normal = x.cross(y).normalized()
        pieces = [face for face in shape.Faces()
                  if face.geomType() == "PLANE"
                  and face.normalAt().dot(normal) > 1-1e-9
                  and abs((face.Center()-origin).dot(normal)) <= TOL
                  and face.intersect(footprint).Area() > TOL**2]
        if len(pieces) > 1 and footprint.cut(*pieces).Area() <= TOL**2:
            raise ValueError("Selected seating face ambiguous: several faces cover the keyed footprint")
        raise ValueError("Selected seating face missing at the keyed corners")
    if len(faces) > 1:
        raise ValueError("Selected seating face ambiguous at the keyed corners")
    if faces[0].normalAt().dot(x.cross(y).normalized()) < 1 - 1e-9:
        raise ValueError("Different seating face: normal reversed at the keyed corners")
    return (
        cq.Plane(faces[0].Center(), x, faces[0].normalAt()).location,
        [x.Length, y.Length],
        faces[0],
    )


def matrix(frame):
    trsf = frame.wrapped.Transformation()
    return [[trsf.Value(i, j) for j in range(1, 5)] for i in range(1, 4)]


def same_frame(a, b):
    return all(
        abs(x - y) <= TOL for r, s in zip(matrix(a), matrix(b)) for x, y in zip(r, s)
    )


def occupants(assembly, seat_face):
    """Count occurrences whose same-facing planar contact area overlaps the selected seat."""
    centre, axis = seat_face.Center(), seat_face.normalAt()
    result = []
    for key, (_, placement, shape) in assembly.items():
        if any(
            face.geomType() == "PLANE"
            and abs((face.Center() - centre).dot(axis)) <= TOL
            and face.normalAt().dot(axis) >= 1 - 1e-9
            and sum(f.Area() for f in face.intersect(seat_face).Faces()) > TOL**2
            for face in shape.moved(placement).Faces()
        ):
            result.append(key)
    return result


def check_interference(initial, final, targets):
    """Reject new material common to a pair, even if an old overlap disappeared."""

    def world(assembly, key):
        _, placement, shape = assembly[key]
        return shape.moved(placement)

    for key in targets:
        for peer in final:
            if peer == key or (peer in targets and peer < key):
                continue
            common = world(final, key).intersect(world(final, peer))
            if not common.Solids():
                continue
            previous = world(initial, key).intersect(world(initial, peer))
            introduced = common.cut(previous) if previous.Solids() else common
            volume = sum(s.Volume() for s in introduced.Solids())
            if volume > 1e-9:
                raise ValueError(
                    f"Replacement {key} introduces {volume:.9g} mm³ of interference with {peer}"
                )


def check_partner(peer, corners, opposite, seat, dims, key):
    _, placement, shape = peer
    mount, peer_dims, _ = interface(shape, corners)
    if any(abs(a - b) > TOL for a, b in zip(peer_dims, dims)):
        raise ValueError(
            f"Partner interface dimensions differ at {key}: {peer_dims} vs {dims} mm"
        )
    if not same_frame(placement * mount * opposite, seat):
        raise ValueError(f"Mating faces do not coincide at {key}")


def replace(spec, output):
    import cadquery as cq
    from OCP.TDataStd import TDataStd_Name, TDataStd_TreeNode
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.TDF import TDF_LabelSequence
    from OCP.XCAFDoc import XCAFDoc, XCAFDoc_Location

    if spec["mates"] != ["fixed keyed seat"]:
        raise ValueError("Use the owning native provider for the requested mate types")
    asset = spec["replacement"]
    try:
        path = selected_part(asset)
    except subprocess.CalledProcessError as exc:
        raise ValueError(
            f"Catalogue lookup exited {exc.returncode}: {(exc.stderr or '').strip()[-1000:]}"
        ) from exc
    part = load_solid(path)
    if file_digest(path) != asset["revision"]:
        raise ValueError("Catalogue asset changed while reading")
    mount, dims, _ = interface(part, asset["corners"])
    app, doc, tool, root = open_document(spec["model"])
    initial = inventory(tool, root)
    targets = {}
    partners = {}
    for row in spec["targets"]:
        key = row["id"]
        if key not in initial or key in targets:
            raise ValueError(f"Duplicate or unknown leaf occurrence {key}")
        _, placement, shape = initial[key]
        try:
            old_mount, old_dims, old_face = interface(shape, row["corners"])
        except ValueError as exc:
            raise ValueError(f"{key}: {exc}") from exc
        if any(abs(a - b) > TOL for a, b in zip(dims, old_dims)):
            raise ValueError(f"Mounting interface dimensions differ at {key}")
        seat = placement * old_mount
        if occupants(initial, old_face.moved(placement)) != [key]:
            raise ValueError(f"Expected one initial occupant at {key}")
        if "partner" in row:
            mate = row["partner"]
            partner = mate["id"]
            if partner == key or partner not in initial:
                raise ValueError(f"Invalid mating occurrence for {key}")
            opposite = cq.Location((0, 0, 0), (1, 0, 0), 180)
            check_partner(
                initial[partner], mate["corners"], opposite, seat, old_dims, key
            )
            partners[key] = (partner, mate["corners"], opposite)
        targets[key] = seat
    if not targets:
        raise ValueError("Select at least one occurrence")
    if any(partner in targets for partner, _, _ in partners.values()):
        raise ValueError("Select a retained partner outside the replacement targets")
    planned = dict(initial)
    for key, seat in targets.items():
        planned[key] = (None, seat * mount.inverse, part)
    check_interference(initial, planned, targets)
    definition = tool.NewShape()
    tool.SetShape(definition, part.wrapped)
    catalogue_id = asset["part"]["id"]
    TDataStd_Name.Set_s(definition, TCollection_ExtendedString(catalogue_id, True))
    for key, seat in targets.items():
        parent = root
        frame = cq.Location(tool.GetLocation_s(root))
        *ancestors, tag = key.split("/")
        for ancestor in ancestors:
            component = children(tool, parent)[ancestor]
            frame = frame * cq.Location(tool.GetLocation_s(component))
            parent = independent(tool, component)
        component = children(tool, parent)[tag]
        old = referred(tool, component)
        check_plain(component)
        check_plain(old)
        if component.NbChildren() or old.NbChildren():
            raise ValueError(
                f"Use the owning provider for labelled dependencies at {key}"
            )
        guid = XCAFDoc.ShapeRefGUID_s()
        link = TDataStd_TreeNode.Set_s(component, guid)
        link.Remove()
        TDataStd_TreeNode.Set_s(definition, guid).Append(link)
        XCAFDoc_Location.Set_s(
            component, (frame.inverse * seat * mount.inverse).wrapped
        )
        if not tool.GetUsers_s(old, TDF_LabelSequence()):
            tool.RemoveShape(old)
    save_document(app, doc, tool, output)
    saved_app, saved_doc, saved_tool, saved_root = open_document(output)
    saved = inventory(saved_tool, saved_root)
    if initial.keys() != saved.keys():
        raise ValueError("Reopened occurrence paths differ")
    check_interference(initial, saved, targets)
    results = []
    for key, (identifier, placement, shape) in saved.items():
        old_id, old_placement, original = initial[key]
        if key not in targets:
            if (
                identifier != old_id
                or not same_frame(placement, old_placement)
                or solid_difference(shape, original) > TOL
            ):
                raise ValueError(f"Unselected occurrence changed at {key}")
            continue
        parent = saved_root
        for tag in key.split("/"):
            parent = referred(saved_tool, children(saved_tool, parent)[tag])
        saved_mount, saved_dims, saved_face = interface(shape, asset["corners"])
        verified = placement * saved_mount
        if (
            identifier != definition.Tag()
            or occurrence_name(parent) != catalogue_id
            or solid_difference(shape, part) > TOL
            or not same_frame(verified, targets[key])
            or occupants(saved, saved_face.moved(placement)) != [key]
        ):
            raise ValueError(
                f"Reopened replacement, seating mate or occupant count differs at {key}"
            )
        partner_id = None
        if key in partners:
            partner_id, corners, opposite = partners[key]
            check_partner(
                saved[partner_id], corners, opposite, verified, saved_dims, key
            )
        results.append(
            dict(
                id=key,
                reference_result="matched",
                partner_id=partner_id,
                original_definition=old_id,
                saved_definition=identifier,
                catalogue_id=catalogue_id,
                asset_sha256=asset["revision"],
                seat_frame=matrix(verified),
                interface_mm=saved_dims,
                occupants=1,
            )
        )
    return results
