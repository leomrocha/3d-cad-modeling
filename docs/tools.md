# Tools and usage

[Documentation](README.md) · [Project](../README.md)

## Implemented helpers

1. **Source intake:** records exact requests, source identities, file hashes and protected revisions. [Source](../scripts/source_intake.py).
2. **Part-index access and model inventory:** reads explicit external indexes and locates existing attributed models before construction. [Index reader](../scripts/part_index.py) and [inventory](../scripts/model_inventory.py).
3. **DXF inspection:** records units, drawing spaces, layers, source entities and nested block transforms. [Source](../scripts/dxf_inspect.py).
4. **Native solid and assembly checks:** reads supported ACIS records, compares geometric features and checks component placement matrices. [Solid reader](../scripts/native_acis.py) and [placements](../scripts/step_placements.py).
5. **Calibrated image tracing:** converts supplied image points to coordinates with explicit scale and uncertainty. [Source](../scripts/calibrated_trace.py).
6. **Parameterized construction:** supported tube and motor procedures bind geometry to an external source job and native CAD runtime. [Tube helper](../scripts/rounded_tube.py) and [motor helper](../scripts/axial_motor.py).

## Local inspection commands

Run commands from the repository root. Replace each uppercase path with the actual source or project path.

```sh
python3 scripts/part_index.py --index INDEX.json --id COMPONENT_ID
python3 scripts/model_inventory.py --index INDEX.json --work-index WORK.json --cad-root CAD_ROOT --project-root PROJECT_ROOT
python3 scripts/dxf_inspect.py DRAWING.dxf --space Model --output NEW_INVENTORY.json
```

The first two commands print JSON. DXF inspection writes a new inventory file. [Pinned reader dependencies](../requirements-native.txt) identify the Python packages used by native readers. CAD construction also requires the `cadtools` runtime and installed OCS control skill; the construction caller supplies the runtime directory and exact session, document, journal and output paths.

## Researched integrations

1. **OpenCADStudio:** native drafting, solid construction and document automation; used for the [wind-generator captures](wind-generator.md).
2. **FreeCAD, CadQuery and build123d:** candidate dimensioned-solid and parametric modeling routes.
3. **Blender:** candidate scene, mesh, rendering and display-export workflows.
4. **IfcOpenShell and Bonsai:** proposed building-element and IFC authoring route.
5. **Photogrammetry and point-cloud tools:** proposed capture, reconstruction and fitting routes.
6. **MuJoCo and URDF:** proposed articulated-model and simulation handoffs with explicit frames, joints and physical properties.

The [modeling workflow](modeling-workflow.md) describes the common contracts. [Sources](sources.md) links the assessments and original upstream documentation.
