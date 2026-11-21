# Source-bound axial component construction and checks

1. Use [axial_motor.py](../scripts/axial_motor.py) for supported coaxial housing, pilot, shaft, blind mounting groups and keyed-shaft features. Supply exact source dimensions, independent feature expectations, millimetres, local datums and explicit cutting overrun.
2. Inspect section/front views and associate each dimension with its endpoints. Keep nominal thread-designation cylinders and reconstructed keyway end radii separately labeled. parameters rejects invalid dimensions and unsupported feature extents before construction.
3. housing creates stationary coaxial interfaces and blind mounting cuts with independently supplied depths. shaft creates the axial reference, end-thread reference and keyed region. rear constructs a separate source-defined axial region.
4. inspect reads supported native SAT/SAB records; verify compares analytic radii, projected axes, individual blind bottom planes, axial faces and keyway side/floor/end stations. Body closure and source metadata keep their own checks.
5. A full cylindrical surface can have seam vertices with zero transverse span. Use its analytic radius and axial planes for diameter/length; observed vertex extrema retain their vertex-only scope.
6. Save the first meaningful geometry and each bounded batch. Recover pending saves/opens by original request ID. Bind reopened document identity to the exact OPEN response, then compare saved hash, manifest and source-bound geometry.
7. Retain the actual representation and source frame for mounting/keyway handoffs. Supply independently sourced exterior geometry when terminal, cooling or connector clearances are part of the requested task.


## Finite blind drill point

Build a cylindrical drill tool and a cone at the cylinder's terminal plane with the same radius. Use `Geometry.cone` in [geometry.py](../scripts/cadtools/geometry.py) for a right circular cone with a +Z apex. For an included drill angle A, the point height is radius / tan(A/2). Save the independently checked tools, join their shared base plane, then subtract the joined cutter from the owned shaft. Verify the cylindrical trim stations, cone half-angle, apex depth and closed-body topology. Keep the drill geometry, nominal thread clearance and finished thread form separate in the job.


## Round-ended keyway pockets

Use `round_ended_slot_profile(width, first, last)` in [planar_profiles.py](../scripts/planar_profiles.py). It gives the transverse X / axial Y outline and exact semicircle bulges from the specified width and axial end stations. Extrude the profile into a tool with the job's specified floor level, rotate it into the shaft frame and save the tool before cutting. Read back the floor, both end extrema and the retained circular shaft stations. Bound the pocket against bearing seats and adjacent bores in the part frame.

### Verify successive axial datums

Supply independently observed axial stations and signed drawing offsets to `feature_checks.axial_datum_chain`. Start with the drawing's first datum and retain each intervening face. A shaft extension measured from a pilot face uses that pilot face as its start. Record the absolute placement datum separately when translating local stations into an assembly.
