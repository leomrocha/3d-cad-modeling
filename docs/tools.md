# Tools

[Documentation](README.md) · [Workflow](workflow.md) · [Examples](examples/README.md)

## Implemented shared helpers

1. **Source intake and component records:** the agent identifies sources and required features; Python records hashes, revisions and source readiness. [Code](../scripts/source_intake.py) · [Operation](reference/operations.md#job-01).
2. **Model inventory:** the agent confirms component identity; Python inspects manifests and actual existing model files. [Code](../scripts/model_inventory.py) · [Operation](reference/operations.md#job-02).
3. **DXF inspection:** Python records entities, units, layouts, layers and transforms; the agent identifies the intended profile. [Code](../scripts/dxf_inspect.py) · [Operation](reference/operations.md#cad-08).
4. **Calibrated tracing:** Python maps supplied pixel points through explicit scale/origin inputs and reports uncertainty bounds. [Code](../scripts/calibrated_trace.py) · [Operation](reference/operations.md#job-03).
5. **Native geometry and placement checks:** Python reads supported solids and assembly transforms; the agent binds expected dimensions to their sources. [Solid reader](../scripts/native_acis.py) · [Placement reader](../scripts/step_placements.py).
6. **Construction helpers:** parameterized tube and motor routines use source jobs and a supplied CAD runtime. [Tube](../scripts/rounded_tube.py) · [Motor](../scripts/axial_motor.py).

## Applications used by the examples

1. **OpenCADStudio:** native component and assembly construction, measurements and DWG saves in the wind-generator and FERME records.
2. **Code_Aster 17.4.0:** existing mast equilibrium calculations and saved-field extraction. The example identifies the actual structural representation and load cases.
3. **ParaView:** existing side-by-side displacement and yield-comparison captures from the retained mast results.

## Researched integrations

1. **FreeCAD, CadQuery and build123d:** parametric and solid-modeling routes.
2. **Blender:** mesh, scene and rendering workflows.
3. **IfcOpenShell and Bonsai:** proposed building-element and IFC authoring.
4. **OpenCV, COLMAP, OpenMVS and Open3D:** proposed camera calibration, reconstruction and surface processing.
5. **MuJoCo and URDF:** proposed articulated simulation handoffs.

[Operation contracts](reference/operations.md) give the supported sources and interfaces. [Source register](reference/sources.md) distinguishes existing execution records from researched capabilities.
