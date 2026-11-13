# Source-bound toroidal reference solids

Use [`toroidal_reference.py`](../../../scripts/toroidal_reference.py) when a
source defines a circular-section ring by nominal inside diameter and section
diameter. The helper accepts an external source job and derives the circular
profile and torus radii; it contains no component-specific values.

1. Set `geometry_role: reference_torus`, `units: mm`, a readable component
   identity, representation, geometry name, job ID, source metadata application
   and request label. The supported local axis is `+Z`; provide a three-value
   center and explicit frame descriptions.
2. Bind `dimension_features.inside_diameter` and
   `dimension_features.section_diameter` to distinct required source features.
   Each source feature carries its mm value, source locator and SHA-256, source
   location and evidence status. Resolve portable source locators through the
   caller's named-root map before using the component-record readiness check.
3. The helper derives minor radius as section diameter/2 and major radius as
   inside diameter/2 plus minor radius. It creates four exact quarter-circle
   profile arcs using equal LWPOLYLINE bulges, revolves the closed profile
   through 360 degrees with the existing `Geometry.revolve_z` route and applies
   an explicit center translation when requested. The nominal dimensions stay
   separate from readback tolerance.
4. `verify` requires native analytic torus surface observations with the source
   center, `+Z` axis, major radius and minor radius. It checks every torus
   surface patch, rejects extra analytic planes, cylinders, cones, spheres or
   ellipses, and requires one closed connected body. A native SAB reader must
   provide a `tori` collection containing `center`, `axis`, `major_radius` and
   `minor_radius`; seam vertices alone do not establish torus radii.
5. `inspect` binds the saved `Solid3D`, SAB surface observations and source
   metadata to one document and geometry revision. The stored strings use the
   existing `CADTOOLS_SOURCE` application. Reopened geometry and persistence
   evidence remain separate from source readiness and author acceptance.
6. This representation covers nominal circular-section torus geometry. It
   does not add compound, dimensional tolerance, groove, compression, lubricant,
   installed pose or fit data unless separate source features provide them.

Synthetic tests cover dimension binding, radii derivation, exact circular
profile construction, invalid-input rejection before geometry creation,
analytic torus observations, closed-body checks, metadata and document-revision
binding. They do not exercise the installed OCS command or establish physical
seal fit.

## Saved native torus reader

Use `native_acis.sab_features(data, allow_tori=True)` for the observed ACIS700
ring-shaped torus records. The reader traverses the actual body graph and reads
each reachable face surface. The typed record starts with an attribute pointer,
location vector, direction vector, major-radius double, minor-radius double and
reference-direction vector. These slots were inspected in retained native SAB;
the linked SAT implementation review supplies a separate source comparison.

The decoder checks token types, finite vectors/radii, positive major radius
greater than minor radius, and orthonormal axis/reference directions. Existing
rigid-frame mapping transforms the centre and axis. It reports every torus patch;
the component verifier compares every patch with independently sourced dimensions.
The default reader option continues to reject torus surfaces. See the
[decoder execution record](../../../execution/torus-native-reader-2026-11-13.md).
