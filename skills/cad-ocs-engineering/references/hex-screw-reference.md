# Source-bound regular-hex head and axial-shaft reference

Use the bundled [hex_screw_reference.py](../scripts/hex_screw_reference.py) when the external job defines a nominal regular-hex head joined to a cylindrical shaft. The helper reuses the [hexagonal prism helper](hexagonal-reference.md), guarded cylinder and union operations, and native source metadata.

1. **Inputs:** four distinct required source features in millimetres: head across-flats, head height, shaft diameter and under-head length. Supply source-file locators and hashes, explicit datum origin, shaft axis, radial frame, metadata and comparison tolerance. Use the selected source files and [job paths](paths.md) to resolve the runtime paths. Grade and thread designations retain their source/proposal labels; the represented shaft is a nominal cylinder.
2. **Prerequisites:** run source readiness and the [existing-model check](existing-model-start-check.md). All dimensions and placement values remain external. The helper checks finite positive dimensions, source pins, an orthonormal frame and shaft containment within the head inradius before constructing geometry.
3. **Construction:** the regular-hex head terminates at the under-head datum; the cylinder extends from that datum along the shaft axis. The existing Geometry adapter joins the solids and writes whole-body source metadata. Native execution uses the component project's guarded client and original request journal.
4. **Readback:** the source-driven check inspects six side planes and three axial planes at the head bottom, exposed shoulder and shaft tip, the nominal cylindrical surface, one connected closed solid and stored source metadata. Its inspection brackets the native record read with document/revision/geometry observations. Retain raw native records before decoding, then use the existing save/reopen and owned-document cleanup methods.
5. **Current evidence:** nine synthetic tests and the external source-job preflight passed. The tests include rejection of an omitted shoulder plane. The integrated helper's native saved-model application is recorded separately in the component project. The existing successful bolt recipe supports the extracted method; it retains its own component source and geometry attribution.

## Shorten a retained nominal shaft

Use this operation when the head and shoulder of a checked model match the requested part and its shaft is a plain cylindrical envelope. Pin the source CAD hash, under-head datum, head-base station, nominal shaft diameter and old tip station. Define the new tip as a separate source value or design proposal.

Open a job-owned copy and verify the source stations and shaft axis. Save the copy before the edit. Make a coaxial cylindrical cutter that starts at the requested tip plane, extends beyond the old tip and has a radius larger than the source shaft. Confirm the cutter's axial interval separates it from the shoulder and head. Save the cutter checkpoint, subtract it from the one intended body and save the result before readback. Retrieve uncertain operations by their original request ID.

Check closure, the three axial stations, the retained head vertices and the shaft radius at the original axis. Inspect the new tip plane and confirm one solid remains. Label the result as a nominal shaft envelope. Rolled ends, thread run-out, chamfers and usable thread length need their own source and geometry checks.

### Check a live SAT body when plane readback is absent

The live SAT reader can return valid topology, native cylinder supports and trimmed vertices without the analytic plane list required by the full screw verifier. If the part contract permits a nominal fit envelope, retain the checked saved geometry revision and compare the live SAT body against the required shape below. Use the full analytic verifier if the job requires plane evidence.

1. Confirm one connected closed body and one cylindrical support on the specified shaft axis and radius. Check the shaft trim endpoints at the under-head datum and tip.
2. Generate the six expected hex vertices from the specified across-flats dimension and frame. Match all six at both head stations in the live boundary readback. Compare the complete axial station set and overall extent. Record measured quantities, tolerance, native handle, representation and exact saved checkpoint hash.
3. Verify source metadata separately. Label the check as SAT boundary and cylinder evidence. Preserve the original owned document and checkpoint if any comparison fails.
