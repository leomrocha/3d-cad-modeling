# Building models

[Documentation](README.md) · [Project](../README.md)

Status: documented workflow proposal, based on the retained architecture and component research.

## Inputs and building elements

1. A floor plan supplies room outlines, wall positions, openings and dimension annotations.
2. Written requirements and measurements supply storey heights, levels, wall thicknesses and element types.
3. Existing component geometry supplies doors, windows, stairs, furniture and equipment with recorded dimensions, interfaces and source terms.
4. Photographs and scans supply surface observations registered to the building coordinate frame. See [reconstruction](reconstruction.md).

## Proposed plan-to-building route

1. Record the plan revision, scale, units, origin and elevation references.
2. Identify walls, slabs, roofs, doors and windows; retain each interpretation beside its source.
3. Create those elements with their placements, types, properties and spatial relationships in IFC using IfcOpenShell or Bonsai.
4. Check dimensions, openings, element identities and storey assignments against the plan and measurements.
5. Derive a display scene for visual inspection while retaining a mapping to the IFC elements.
6. Prepare a consumer-specific handoff with its required materials, boundaries and physical properties when an analysis task requires them.

## Geometry and building information

IFC carries the building's semantic elements and relationships. A display mesh carries the visible surfaces. Keep both representations linked by element identity and a recorded coordinate transform.

Building reuse depends on component dimensions, placement frames and source evidence. The same [modeling workflow](modeling-workflow.md) supplies source intake, geometry checks and revision tracking.

Supporting sources: [IfcOpenShell introduction](https://docs.ifcopenshell.org/introduction.html), [geometry creation](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_creation.html) and [Bonsai](https://docs.ifcopenshell.org/bonsai.html), registered in the existing research. [Source status](sources.md).
