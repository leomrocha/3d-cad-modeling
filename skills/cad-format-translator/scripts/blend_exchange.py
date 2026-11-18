"""Run inside Blender in background mode. See the format translation procedure."""
import argparse
import math
import os
from pathlib import Path
import sys
import tempfile

METRES = {"mm": .001, "cm": .01, "m": 1., "in": .0254, "ft": .3048}


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("expected a positive finite length")
    return number


def main(args):
    import bpy
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    stl = parser.add_mutually_exclusive_group(required=True)
    stl.add_argument("--stl-unit", choices=METRES)
    stl.add_argument("--stl-reference", nargs=3, metavar=("STL_DISTANCE", "LENGTH", "UNIT"))
    scale = parser.add_mutually_exclusive_group()
    scale.add_argument("--metres-per-bu", type=positive)
    scale.add_argument("--reference", nargs=3, metavar=("DISTANCE_BU", "LENGTH", "UNIT"))
    parser.add_argument("--scene-system", choices=("METRIC", "IMPERIAL"), help="unit display system for the new Blender scene")
    parser.add_argument("--object", help="source scene mesh object for STL export")
    options = parser.parse_args(args)
    source, target = options.source.resolve(), options.target.absolute()
    pair = source.suffix.lower(), target.suffix.lower()
    if pair not in {(".blend", ".stl"), (".stl", ".blend")} or target.exists():
        parser.error("supply a .blend and an .stl in opposite directions and a new target")
    importing = pair[0] == ".stl"
    if not importing and options.scene_system:
        parser.error("--scene-system applies only to a new Blender scene")
    if importing and not options.scene_system:
        parser.error("select METRIC or IMPERIAL for the new Blender scene")
    if importing and options.object:
        parser.error("--object selects a source Blender mesh only")
    if importing:
        bpy.ops.wm.read_factory_settings(use_empty=True)
    else:
        bpy.ops.wm.open_mainfile(filepath=str(source), load_ui=False, use_scripts=False)
    scene = bpy.context.scene
    settings = scene.unit_settings
    metres = options.metres_per_bu
    def reference_metres(reference):
        distance, length, unit = reference
        if unit not in METRES:
            parser.error("reference unit must be mm, cm, m, in or ft")
        return positive(length) * METRES[unit] / positive(distance)

    if options.reference:
        metres = reference_metres(options.reference)
    if metres is None:
        if importing or settings.system == "NONE":
            parser.error("specify the physical length of one Blender unit or a reference distance")
        metres = settings.scale_length
    if options.stl_reference and not importing:
        parser.error("specify the receiving STL unit with --stl-unit")
    stl_metres = reference_metres(options.stl_reference) if options.stl_reference else METRES[options.stl_unit]
    with tempfile.TemporaryDirectory(dir=target.parent) as temp:
        staged = Path(temp) / target.name
        if importing:
            factor = stl_metres / metres
            op = bpy.ops.wm.stl_import
            settings.system = options.scene_system
            settings.scale_length = metres
            if not math.isclose(settings.scale_length, metres, rel_tol=1e-6):
                parser.error("requested scene scale exceeds Blender's supported range")
        else:
            obj = scene.objects.get(options.object or "")
            if obj is None or obj.type != "MESH" or obj.name not in bpy.context.view_layer.objects:
                parser.error("select one mesh in the active view layer with --object")
            bpy.ops.object.select_all(action="DESELECT")
            obj.select_set(True)
            if list(bpy.context.selected_objects) != [obj]:
                parser.error("could not isolate the requested mesh")
            factor = metres / stl_metres
            op = bpy.ops.wm.stl_export
        prop = op.get_rna_type().properties["global_scale"]
        if not prop.hard_min <= factor <= prop.hard_max:
            parser.error("conversion factor outside Blender STL operator range")
        params = dict(global_scale=factor, use_scene_unit=False, forward_axis="Y", up_axis="Z")
        if importing:
            result = op(filepath=str(source), **params)
            if result != {"FINISHED"} or not any(o.type == "MESH" and len(o.data.polygons) for o in scene.objects):
                parser.error("STL reader produced no mesh")
            result = bpy.ops.wm.save_as_mainfile(filepath=str(staged))
        else:
            result = op(filepath=str(staged), export_selected_objects=True, apply_modifiers=True, **params)
        if result != {"FINISHED"} or staged.stat().st_size == 0:
            parser.error("writer produced no output")
        os.link(staged, target)


if __name__ == "__main__":
    main(sys.argv[sys.argv.index("--") + 1:])
