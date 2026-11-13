# Mast physics for a wind generator

[Examples](README.md) · [Workflow](../../README.md#project) · [Tools](../tools.md)

I'm working on a wind generator idea, so I started to check how to model and see how a mast support would behave for the particular geometry I'm trying to get on the top part, many of the thigns I did there for the 3d modeling came ata good port so I add them here as examples of what the predating things allowed me to do (with a lot of interaction and effort)

## Example results

[Square mast 3D model (DWG)](models/square-mast.dwg).

![Calculated mast displacement at scale one for 0 and 45 degree wind](../images/mast/mast-displacement.png)

The displacement image uses actual deformation scale 1 and colours in metres.

![Assigned yield strength divided by calculated member stress](../images/mast/mast-yield.png)

The dimensionless colour coefficient is assigned yield strength divided by calculated stress. Values below 1 identify yield-input exceedance; grey elements are outside that comparison.
