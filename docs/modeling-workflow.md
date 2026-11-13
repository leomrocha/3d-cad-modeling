# Modeling workflow

[Documentation](README.md) · [Project](../README.md)

## From an input to a model

1. **Record the job.** Identify the requested component or space, the required features and the output representation. Keep descriptions, drawings and photographs tied to their source revisions.
2. **Find existing geometry.** Check model indexes, supplied files and earlier outputs. Reuse the matching component and its recorded checks.
3. **Establish dimensions.** Record units, origin, axes, measurements and source status. Drawing dimensions, manufacturer values, measured values and proposed inputs retain their labels.
4. **Build the geometry.** Use profiles, extrusions, revolutions, cuts or imported solids according to the source. Keep separately manufactured parts identifiable.
5. **Place the components.** Record each occurrence's position and orientation. Describe joints separately when an assembly will become an articulated simulation model.
6. **Check and save.** Compare required features with source expectations, save the native model, reopen it and check persisted geometry. Tie captures to the actual model revision.

The [wind-generator example](wind-generator.md) shows assembly views and internal transmission geometry produced through native CAD operations.

## Representations and handoffs

1. **Native CAD document:** editable application geometry and component organization.
2. **STEP:** exchanged solid geometry, with the actual exporter and receiving importer checked for dimensions and topology.
3. **Mesh:** vertices and faces for display, reconstruction or simulation geometry.
4. **IFC:** building elements, placements, spatial relationships and properties. See [building models](building-models.md).
5. **URDF or MJCF:** robot links, joints and simulation properties, with explicit visual geometry, collision geometry and mass properties.

A handoff record names the input, output, tool version, units, frame transform, preserved fields, changed fields and checks. [Tools](tools.md) and [source records](sources.md) describe the supporting work.
