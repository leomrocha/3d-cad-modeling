"""Reusable native OCS geometry operations.

Input units are millimetres/degrees. Geometry remains native to OCS; this module
plans or sends known commands and does not substitute a geometry kernel.
"""

from collections.abc import Mapping
import math

from .records import identity, iter_records
from .runtime import CadError


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise CadError("Finite numeric input required")
    return value


def positive(value):
    if finite(value) <= 0:
        raise CadError("Positive dimension required")
    return value


def vector(values, size=3):
    if len(values) != size:
        raise CadError("Wrong coordinate dimension")
    return [finite(v) for v in values]


def pattern(pcd, angles_deg):
    positive(pcd)
    if not angles_deg:
        raise CadError("An explicit nonempty angle list is required")
    angles = [finite(a) % 360 for a in angles_deg]
    if any(min(abs(a-b), 360-abs(a-b)) < 1e-9
           for i, a in enumerate(angles) for b in angles[:i]):
        raise CadError("Duplicate angular position")
    return [[pcd / 2 * math.cos(math.radians(a)),
             pcd / 2 * math.sin(math.radians(a))] for a in angles]


def added(response: Mapping) -> str:
    """Extract the one added handle from a raw native command response."""
    if not isinstance(response, Mapping):
        raise CadError("Expected a raw native command response; use a geometry helper's returned handle directly")
    handles = [v["handle"] for v in response.get("changes", []) or [] if v["kind"] == "Added"]
    if len(handles) != 1:
        raise CadError("Expected one added entity; inspect the operation result")
    return handles[0]


class Geometry:
    def __init__(self, client):
        self.client = client

    def run(self, label, command):
        return self.client.mutate(label, "run", cmd=command)

    def select(self, label, handles):
        return self.client.mutate(label, "select", handles=handles, clear=True)

    def profile(self, label, points, bulges=None, closed=True):
        points = [vector(p, 2) for p in points]
        if len(points) < (3 if closed else 2):
            raise CadError("Insufficient profile points")
        if any(a == b for a, b in zip(points, points[1:])) or (closed and points[0] == points[-1]):
            raise CadError("Remove duplicate profile vertices before construction")
        updates = []
        for index, value in (bulges or {}).items():
            if type(index) is not int or not 0 <= index < len(points):
                raise CadError("Bulge vertex index outside profile")
            updates.append({"path": f"/vertices/{index}/bulge", "value": finite(value)})
        response = self.client.mutate(label + "-profile", "entities_create", entities=[
            {"type": "LwPolyline", "vertices": points, "closed": closed}])
        handle = response["result"]["handles"][0]
        if bulges:
            self.client.mutate(label + "-arcs", "set_properties", collection="entities",
                               handle=handle, updates=updates)
        return handle

    def move(self, label, handles, displacement):
        return self.client.mutate(label, "entities_transform", handles=handles,
                                  action="move", vector=vector(displacement))

    def rotate(self, label, handles, axis, degrees):
        if axis not in {"X", "Y", "Z"}:
            raise CadError("Rotation axis must be X, Y or Z")
        finite(degrees)
        self.select(label + "-selection", handles)
        return self.run(label, f"3DROTATE 0,0,0 {axis} {degrees}")

    def extrude(self, label, points, z, height, bulges=None) -> str:
        finite(z)
        positive(height)
        handle = self.profile(label, points, bulges)
        if z:
            self.move(label + "-z", [handle], [0, 0, z])
        self.select(label + "-selection", [handle])
        return added(self.run(label + "-extrude", "EXTRUDE " + str(height)))

    def revolve_z(self, label, points, bulges=None) -> str:
        handle = self.profile(label, points, bulges)
        self.select(label + "-selection", [handle])
        solid = added(self.run(label + "-revolve", "REVOLVE Y 360"))
        self.rotate(label + "-axis-z", [solid], "X", 90)
        return solid

    def cylinder(self, label, centre, radius, height) -> str:
        x, y, z = vector(centre)
        positive(radius)
        positive(height)
        return added(self.run(label, f"CYLINDER {x},{y},{z} {radius} {height}"))

    def cone(self, label, base_centre, radius, height) -> str:
        """Create a right circular cone with its apex along +Z from the base."""
        x, y, z = vector(base_centre)
        positive(radius)
        positive(height)
        return added(self.run(label, f"CONE {x},{y},{z} {radius} {height}"))

    def sphere(self, label, centre, radius) -> str:
        x, y, z = vector(centre)
        positive(radius)
        return added(self.run(label, f"SPHERE {x},{y},{z} {radius}"))

    def subtract(self, label, base, cutters):
        if not cutters or base in cutters or len(set(cutters)) != len(cutters):
            raise CadError("Subtraction requires distinct base and cutter handles")
        steps = [
            ("clear", "select", {"clear": True}),
            ("start", "start", {"cmd": "SUBTRACT"}),
            ("base", "select", {"handles": [base], "clear": True}),
            ("base-pick", "input", {"kind": "selection"}),
            ("base-end", "input", {"kind": "enter"}),
            ("tools", "select", {"handles": cutters, "clear": True}),
            ("tools-pick", "input", {"kind": "selection"}),
            ("end", "input", {"kind": "enter"}),
        ]
        for suffix, op, fields in steps:
            response = self.client.mutate(label + "-" + suffix, op,
                                          allow_wait=suffix != "end", **fields)
            if suffix != "end" and response.get("status") == "waiting_input":
                command = response.get("state", {}).get("command")
                if command and command.get("name") != "SUBTRACT":
                    raise CadError("Unexpected interactive command; inspect before resuming")
        return base

    def combine(self, label, handles):
        if len(handles) < 2 or len(set(handles)) != len(handles):
            raise CadError("Union requires distinct handles")
        inputs = set(handles)
        selection = self.client.mutate(label + "-selection", "select", handles=handles, clear=False)
        selected = selection.get("state", {}).get("selection")
        if selected is None:
            selected = self.client.read("state").get("selection")
        if sorted(selected or []) != sorted(handles):
            raise CadError("Union selection differs from requested inputs")
        response = self.run(label, "UNION")
        revision = identity(response.get("state", {}))
        if revision[0] != self.client.document_id or identity(self.client.read("state")) != revision:
            raise CadError("Union result state changed; inspect before resuming")
        changes = response.get("changes") or ()
        added_handles = {change["handle"] for change in changes if change["kind"] == "Added"}
        removed_handles = {change["handle"] for change in changes if change["kind"] == "Removed"}
        modified_handles = {change["handle"] for change in changes if change["kind"] == "Modified"}
        candidates = inputs | added_handles
        rows = list(iter_records(self.client, "entities", handles=sorted(candidates)))
        if identity(self.client.read("state")) != revision:
            raise CadError("Union result state changed; inspect before resuming")
        live = {row["handle"] for row in rows}
        if (len(rows) != 1 or not live <= candidates or not added_handles <= live
                or removed_handles != inputs - live or not modified_handles <= live
                or not live <= added_handles | modified_handles or rows[0]["type"] != "Solid3D"):
            raise CadError("Union result ambiguous; inspect before resuming")
        return rows[0]["handle"]

    def holes(self, label, pcd, angles, radius, z, depth):
        return [self.cylinder(f"{label}-{i}", [x, y, z], radius, depth)
                for i, (x, y) in enumerate(pattern(pcd, angles))]

    def sweep(self, label, profile_handle, path_handle):
        # Both inputs must be constructed before the interactive command starts.
        self.select(label + "-clear", [])
        self.client.mutate(label + "-start", "start", cmd="SWEEP", allow_wait=True)
        self.client.mutate(label + "-profile", "select", handles=[profile_handle],
                           clear=True, allow_wait=True)
        self.client.mutate(label + "-pick", "input", kind="selection", allow_wait=True)
        self.client.mutate(label + "-done", "input", kind="enter", allow_wait=True)
        state = self.client.read("state")
        command = state.get("command") or {}
        if command.get("name") != "SWEEP" or "selection" not in command.get("accepts", []):
            raise CadError("SWEEP path-selection prompt differs; inspect current schema")
        self.client.mutate(label + "-path", "select", handles=[path_handle],
                           clear=True, allow_wait=True)
        return added(self.client.mutate(label + "-finish", "input", kind="selection"))

    def metadata(self, label, handles, lines):
        if not lines or any(not isinstance(line, str) or not line for line in lines):
            raise CadError("Source metadata requires nonempty text")
        chunks = [line[i:i+100] for line in lines for i in range(0, len(line), 100)]
        return self.client.mutate(label, "xdata_set", handles=handles, app="CADTOOLS_SOURCE",
                                  data=[{"code": 1000, "value": line} for line in chunks])
