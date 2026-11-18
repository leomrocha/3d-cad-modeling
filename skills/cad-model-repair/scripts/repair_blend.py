"""Apply evidence-backed Blender mesh naming and collection assignments to a derivative."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile


def fingerprint(obj):
    digest = hashlib.sha256()
    def add(value):
        digest.update(repr(value).encode())
        digest.update(b"\n")
    add(obj.type)
    add(tuple(tuple(row) for row in obj.matrix_world))
    if obj.type == "MESH":
        for vert in obj.data.vertices:
            add(tuple(vert.co))
        for edge in obj.data.edges:
            add(tuple(edge.vertices))
        for face in obj.data.polygons:
            add((tuple(face.vertices), face.material_index))
        add(tuple(slot.material.name if slot.material else None for slot in obj.material_slots))
    return digest.hexdigest()


def repair(source, mapping, target):
    import bpy
    config = json.loads(mapping.read_text())
    if source.suffix.lower() != ".blend" or target.suffix.lower() != ".blend" or target.exists():
        raise ValueError("expected native Blender input and a new .blend destination")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if config["source_sha256"] != digest:
        raise ValueError("mapping belongs to another source revision")
    bpy.ops.wm.open_mainfile(filepath=str(source), load_ui=False, use_scripts=False)
    resource_paths = set(bpy.utils.blend_paths(absolute=True, packed=False))
    if any(not Path(p).exists() for p in resource_paths):
        raise ValueError("resolve missing external resources before repair")
    rows = config["objects"]
    if not isinstance(rows, list) or not rows:
        raise ValueError("nonempty object mapping required")
    for field in ("id", "label", "source_name", "role", "layer"):
        values = [r[field] for r in rows]
        if any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError(f"missing {field}")
        if field in ("id", "label", "source_name") and len(set(values)) != len(values):
            raise ValueError(f"ambiguous {field}")
    renamed = {r["source_name"]: r["label"] for r in rows}
    before = {}
    for obj in bpy.data.objects:
        name = renamed.get(obj.name, obj.name)
        parent = renamed.get(obj.parent.name, obj.parent.name) if obj.parent else None
        before[name] = (fingerprint(obj), parent, {c.name for c in obj.users_collection})
    for row in rows:
        obj = bpy.context.scene.objects.get(row["source_name"])
        if obj is None or obj.type != "MESH" or obj.library:
            raise ValueError(f"expected local mesh: {row['source_name']}")
        if any(other != obj and (other.name == row["label"] or other.get("navigation_id") == row["id"])
               for other in bpy.data.objects):
            raise ValueError(f"conflicting label or identity: {row['id']}")
        if obj.get("navigation_id", row["id"]) != row["id"]:
            raise ValueError("existing identity differs from proposed identity")
        obj.name = row["label"]
        obj["navigation_id"] = row["id"]
        obj["navigation_role"] = row["role"]
        layer = bpy.data.collections.get(row["layer"])
        if layer is None:
            layer = bpy.data.collections.new(row["layer"])
            bpy.context.scene.collection.children.link(layer)
        if layer not in bpy.context.scene.collection.children_recursive:
            raise ValueError("collection is outside the active scene")
        if obj.name not in layer.objects:
            layer.objects.link(obj)
        before[row["label"]][2].add(row["layer"])
    # Keep relative asset references valid when the staged file receives its final name.
    bpy.context.preferences.filepaths.save_version = 0
    with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".blend") as temporary:
        staged = temporary.name
        bpy.ops.wm.save_as_mainfile(filepath=staged)
        bpy.ops.wm.open_mainfile(filepath=staged, load_ui=False, use_scripts=False)
        after = {o.name: (fingerprint(o), o.parent.name if o.parent else None,
                          {c.name for c in o.users_collection}) for o in bpy.data.objects}
        if set(bpy.utils.blend_paths(absolute=True, packed=False)) != resource_paths:
            raise ValueError("external resource bindings changed")
        if before != after:
            raise ValueError("geometry, placement, parenting, membership or inventory changed")
        for row in rows:
            obj = bpy.data.objects[row["label"]]
            if (obj.get("navigation_id"), obj.get("navigation_role")) != (row["id"], row["role"]):
                raise ValueError(f"reopened identity/role differs for {row['label']}")
        if hashlib.sha256(source.read_bytes()).hexdigest() != digest:
            raise ValueError("original changed during repair")
        os.link(staged, target)


if __name__ == "__main__":
    repair(*(Path(v).absolute() for v in sys.argv[sys.argv.index("--") + 1:]))
