# Match a drawing dimension to the measured CAD feature

Use this procedure when a drawing dimension is compared with imported or reconstructed geometry.

1. Inspect the drawing view and both extension-line endpoints. Record the source file revision/hash, page, view, feature name, units and what the dimension measures: overall extent, hole-axis pitch, wall thickness, radius, depth or another explicit feature. A matching number supports the comparison only after the feature has been identified.
2. Select the corresponding native measurement. Hole pitch uses identified hole axes or centres; radius uses the identified analytic surface or curve; overall dimensions use extrema of the complete represented surfaces in the stated frame. Keep the component's local frame and any assembly transform in the measurement record.
3. Label reachable vertex/point extrema as point extrema. A curved face can extend beyond its recorded vertices. Use an analytic curve/surface method supported for the actual geometry when an overall bound is required. A point-set persistence comparison retains its own scope and remains useful independently of a drawing-dimension comparison.
4. Verify assembly membership from the supplied source hierarchy. Record base, cover, screws and repeated instances as their evidenced roles. Distinct solid labels alone do not establish mutually exclusive product alternatives.
5. Before construction, compare the source-derived input profile with an independent direct drawing callout when that callout measures its extent. Check the image size and coordinate frame used for every point and calibration endpoint. Then verify native output against both the source expectation and the supplied profile. Reproducing an erroneous input profile can pass an output-to-input check.
6. Record each result against its feature-specific expectation, tolerance and evidence. Numeric tolerance describes the comparison arithmetic; manufacturer tolerance, trace uncertainty and measurement uncertainty remain separate named values.
7. When a comparison used the wrong drawing feature, preserve the original executed record and add a source-review finding identifying the affected comparison. Keep independently supported persistence, unit and placement results. Reuse completed CAD geometry unless the actual geometry requires an authorized revision.

Component drawings, actual measurements and review findings stay in the component project. The reusable procedure stays in this skill. The applied source-review record is linked from the tooling-improvement report.
