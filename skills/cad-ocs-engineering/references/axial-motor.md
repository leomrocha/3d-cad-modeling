# Source-bound axial component construction and checks

1. Use [axial_motor.py](../scripts/axial_motor.py) for supported coaxial housing, pilot, shaft, blind mounting groups and keyed-shaft features. Supply exact source dimensions, independent feature expectations, millimetres, local datums and explicit cutting overrun.
2. Inspect section/front views and associate each dimension with its endpoints. Keep nominal thread-designation cylinders and reconstructed keyway end radii separately labeled. parameters rejects invalid dimensions and unsupported feature extents before construction.
3. housing creates stationary coaxial interfaces and blind mounting cuts with independently supplied depths. shaft creates the axial reference, end-thread reference and keyed region. rear constructs a separate source-defined axial region.
4. inspect reads supported native SAT/SAB records; verify compares analytic radii, projected axes, individual blind bottom planes, axial faces and keyway side/floor/end stations. Body closure and source metadata keep their own checks.
5. A full cylindrical surface can have seam vertices with zero transverse span. Use its analytic radius and axial planes for diameter/length; observed vertex extrema retain their vertex-only scope.
6. Save the first meaningful geometry and each bounded batch. Recover pending saves/opens by original request ID. Bind reopened document identity to the exact OPEN response, then compare saved hash, manifest and source-bound geometry.
7. Retain the actual representation and source frame for mounting/keyway handoffs. Supply independently sourced exterior geometry when terminal, cooling or connector clearances are part of the requested task.
