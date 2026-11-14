# Assembly scale and mirrored placements

1. Read declared source units and native drawing units before interpreting instance matrices. Translation is expressed in the declared drawing unit; scale is dimensionless and native insert rotation is radians.
2. [native_matrix and solid_instances](../scripts/step_placements.py) support positive unit scale by default. allow_uniform_scale=True explicitly permits positive uniform unit conversion. allow_unit_reflection=True permits signed unit scales. Choose one scale mode.
3. Traversal composes parent*child matrices, preserves every occurrence path, rejects cycles, arrays and nonzero block bases, and enforces an instance bound. Finite coordinates and a supported OCS basis are required.
4. classify_hand validates a finite affine orthonormal matrix and reports SOURCE_HAND or MIRRORED. Determinant magnitude alone also admits shears; verify the complete basis.
5. Retain source unit conversion independently of source-placement corrections. Check saved placements, definition geometry and view identity separately using the [assembly procedure](manufacturer-assembly.md).
