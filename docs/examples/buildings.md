# Buildings

[Examples](README.md) · [Workflow](../../README.md#project) · [Tools](../tools.md)

Status: proposed workflow based on the retained building-model research.

## Inputs and output

A plan, written brief, dimensions and measured controls describe wall positions, levels, openings and room relationships. Reusable door, window, stair and equipment geometry can supply component detail.

The proposed output is a semantic IFC model containing building elements, placements, types, properties and spatial relationships, linked to a display scene for inspection.

## Workflow

1. **Interpret the plan.** Record plan scale, units, axes, levels and wall/opening identities.
2. **Create building elements.** Author walls, slabs and openings with explicit placements and properties using IfcOpenShell or Bonsai.
3. **Check the model.** Compare element dimensions, openings, storey assignments and measured controls against the source plan and dimensions.
4. **Create a display derivative.** Preserve the IFC element mapping and coordinate transform when producing a GLB inspection scene.

IFC retains the building elements and relationships; display meshes represent visible surfaces. Photographs and scans can be registered as additional evidence using calibrated image or scan measurements.
