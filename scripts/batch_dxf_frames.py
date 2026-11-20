"""Measure and verify rigid DXF INSERT placement at its named block base."""
import hashlib
import math

from batch_dxf_lines import UNIT_CODES, backend, drawing
from step_placements import apply, classify_hand, eye, multiply, near

INPUT = "DXF INSERT"
OUTPUT = "existing occurrence world base frame"
METHOD = "move-existing-insert"
FIELDS = ("insert", "extrusion", "rotation", "xscale", "yscale", "zscale")
TOL = 1e-8


def resolve_frame(doc, path):
    """Follow native ownership, including nonzero block bases in every parent matrix."""
    layout = doc.modelspace()
    parent = eye()
    keys = path.split("/")
    for i, handle in enumerate(keys):
        entity = doc.entitydb.get(handle)
        if (entity is None or entity.dxftype() != "INSERT"
                or entity.dxf.owner != layout.block_record_handle
                or entity.dxf.row_count != 1 or entity.dxf.column_count != 1):
            raise ValueError(f"{path} requires individually addressable INSERTs")
        layout = doc.blocks[entity.dxf.name]
        matrix = [list(col) for col in entity.matrix44().columns()]
        classify_hand(matrix)
        if i < len(keys) - 1:
            parent = multiply(parent, matrix)
    world = multiply(parent, matrix)
    base = apply(world, layout.block.dxf.base_point)
    for i in range(3):
        world[i][3] = base[i]
    return entity, parent, world


def check_document(doc, unit, version):
    if doc.units != UNIT_CODES[unit] or doc.dxfversion != version or version < "AC1015":
        raise ValueError("Drawing version or declared units differ from the placement contract")
    if any("CONSTRAINT" in e.dxftype() or "ASSOC" in e.dxftype() for e in doc.entitydb.values()):
        raise ValueError("Drawing contains association or constraint data; use its native constraint editor")


def check_editable(doc, path):
    for handle in path.split("/"):
        entity = doc.entitydb[handle]
        if (entity.dxftype() != "INSERT" or entity.attribs or entity.has_extension_dict
                or doc.blocks[entity.dxf.name].block.dxf.flags
                or doc.layers.get(entity.dxf.layer).is_locked()
                or any(doc.entitydb.get(h) is None or doc.entitydb[h].dxftype() != "GROUP"
                       for h in entity.get_reactors())):
            raise ValueError(f"{path} requires a native edit preserving attached or locked data")


def signatures(doc, targets):
    """Hash layout membership, block bases, definitions and all non-placement INSERT data."""
    from ezdxf.lldxf.tagwriter import TagCollector
    handles = {path.split("/")[-1] for path in targets}
    result = {}
    for block in doc.blocks:
        digest = hashlib.sha256()
        for entity in (block.block, *block):
            saved = {}
            if entity.dxf.handle in handles:
                if entity.dxftype() != "INSERT" or entity.attribs:
                    raise ValueError("Selected occurrence requires an attribute-preserving native edit")
                for field in FIELDS:
                    if entity.dxf.hasattr(field):
                        saved[field] = entity.dxf.get(field)
                for field in FIELDS:
                    entity.dxf.discard(field)
                entity.dxf.insert = (0, 0, 0)
            try:
                writer = TagCollector(dxfversion=doc.dxfversion, optional=False)
                entity.export_dxf(writer)
                digest.update(repr(writer.tags).encode())
            finally:
                if entity.dxf.handle in handles:
                    entity.dxf.discard("insert")
                    entity.dxf.update(saved)
        result[block.name] = digest.hexdigest()
    return {"blocks": result, "groups": [(name, list(group.handles())) for name, group in doc.groups]}


def verify_result(source, result, writer, *, require_change=False):
    if (writer["backend"], writer["name"], writer["input"], writer["output"], writer["action"]) != (
            backend(), METHOD, INPUT, OUTPUT, "place"):
        raise ValueError("Placement receipt differs from the installed operation")
    expected = writer["expected"]
    before, after = (drawing(path, writer["unit"]) for path in (source, result))
    for doc in (before, after):
        check_document(doc, writer["unit"], writer["version"])
    if signatures(before, expected) != signatures(after, expected):
        raise ValueError("Occurrence membership, independent geometry or part definitions changed")
    observed = {}
    previous = None
    changed = False
    sequence = sorted(expected, key=lambda target: expected[target]["position_index"])
    if [expected[t]["position_index"] for t in sequence] != list(range(len(expected))):
        raise ValueError("Invalid reviewed position sequence")
    for target in sequence:
        row = expected[target]
        for doc in (before, after):
            check_editable(doc, target)
        old = resolve_frame(before, target)[2]
        new = resolve_frame(after, target)[2]
        classify_hand(row["world_frame"])
        classify_hand(row["before"])
        if not near(old, row["before"], TOL) or not near(new, row["world_frame"], TOL):
            raise ValueError(f"Reopened base anchor or orientation differs at {target}")
        changed |= not near(old, new, TOL)
        point = [new[i][3] for i in range(3)]
        destination = [row["world_frame"][i][3] for i in range(3)]
        measured = dict(world_frame=new, block_base=point, reference=row["reference"],
                        position_id=row["position_id"])
        if previous:
            other, anchor, other_destination = previous
            pitch = math.dist(anchor, point)
            if abs(pitch - math.dist(other_destination, destination)) > 4 * TOL:
                raise ValueError(f"Reopened base-to-base distance differs for {other} and {target}")
            measured.update(previous_target=other, distance_from_previous_base=pitch)
        observed[target] = measured
        previous = target, point, destination
    if require_change and not changed:
        raise ValueError("Qualification requires a measured occurrence displacement or rotation")
    return observed
