# Dimension limits and source datums

Use a source callout as a dimensional limit when its label includes `Max`, `Min`, or another explicit bound. Preserve the bound in metadata and checks. A clearance-reference volume may use the bound as its limit surface, but its solid thickness or envelope is not a claim that the manufactured part equals that bound.

Keep the source leader endpoints with the dimension. A height from a base top plane differs from a height from the base bottom plane by the base thickness. Do not move a dimension to a more convenient datum. Record any datum transform as a calculated or traced relationship, separate from printed dimensions.

For drawing-derived mounting references, keep three records separate: printed dimensions, arithmetic relationships between printed dimensions, and image-traced coordinates. Record the view, original image frame, point-pick uncertainty, calibration dimensions and resulting coordinate uncertainty. A symmetry-derived centerline is a coordinate convention supported by view geometry; it is not an additional printed ordinate.

Independent checks compare the resulting geometry with source callouts and leader endpoints. Repeating the same recipe values in a construction check does not independently validate a source feature.
