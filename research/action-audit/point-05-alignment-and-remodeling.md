# Point 05 — Alignment and parametric remodeling

Date: 2026-11-12. Status: **procedure proposal**. Scope: 14 operations and 42 actions. Requested procedure-design dispatch: `gpt-6-astra`, `xhigh`; actual executing model identity: **unavailable**.

[Structured records](point-05-operations.json) contain all 15 fields for each action, four operation modes, alternatives, source URLs, merging, migration and future cases. This document supplies the readable actions and concrete frame/output conditions. The [audit plan](plan.md), [CAD records](../workflows/cad-paths.json), [reconstruction records](../workflows/reconstruction-paths.json), [domain records](../workflows/domain-paths.json), OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`), model contract (`${CODEX_HOME}/skills/ocs-engineering/references/model-contract.md`) and [retained implementation plan](../implementation-plan.md) remain the original contracts. Helpers and procedures are proposals; acceptance labels use `MARK AS ACCEPTED`.

## 1. Terms and shared evidence

1. **Camera intrinsics** describe image projection, including focal scale and image centre; lens distortion has its own model/coefficients. **Extrinsics** describe camera pose relative to a named object/world frame. **PnP**, perspective-n-point, estimates pose from known 3D points and corresponding 2D image points.
2. **Rigid transform:** rotation and translation. **Similarity transform:** rotation, translation and uniform scale. **Handedness** specifies the orientation of a coordinate-axis system. A **datum** is a named reference point, axis or plane. **Observable freedoms** are position, orientation or scale components that the supplied geometry can constrain.
3. **FPFH**, Fast Point Feature Histogram, summarizes local surface shape around a cloud point for matching. **RANSAC**, Random Sample Consensus, tests models from subsets and checks supporting correspondences. **ICP**, Iterative Closest Point, refines an initialized alignment using a chosen closest-point objective.
4. A **residual** is a difference measured by a stated comparison. **RMSE**, root mean square error, summarizes squared residuals through their mean and square root. It retains the residual's units. **Normals** are directions perpendicular to a surface. **Tessellation** approximates surfaces with facets.
5. **Ray intersection** is a calculated hit where a directed line meets the selected geometry. A hit records the queried geometry and view; independent controls supply physical measurement evidence.
6. **CRS**, coordinate reference system, defines coordinates in a named geographic/projected reference. Local CAD/building coordinates, units, placement chains, survey datum and map conversion are separate records.
7. **Parametric source** retains editable construction parameters and their generation relationships. **Constrained sketch** contains explicit geometric/dimensional relations. A **B-rep**, boundary representation, stores surfaces, edges and connections. An **idealized model** uses explicitly chosen regular geometry to express the task's design intent.
8. A **VLM**, vision-language model, reads images and language together. It compares source-feature associations and alternatives using original views, located regions and actual numerical reports. A **pinned revision** is an explicitly fixed revision or content hash.

The [point03 shared protocol](point-03-operations.json) supplies source/request identity, separate producing/reviewing executions, uncertain native/remote completion and changed-source invalidation. The [point04 mapping protocol](point-04-operations.json) supplies original pixels, crop/resize/warp/lens coordinate mapping and valid-domain records. This point's `common_protocol` adds camera, cloud, fit and frame conditions.

1. Preserve raw photos/depth/clouds/meshes, CAD and drawing revisions. Identify exact source and target roles, feature IDs, selected regions, fit/check controls and preprocessing/sampling lineage.
2. Name every transform's source/destination, units, axes, handedness, direction, inverse and composition order. Unit conversion and numerical origin shift remain separate operations. A similarity scale needs explicit evidence; it cannot silently absorb physical deformation.
3. Record source engineering allowance, sensor/control/measurement uncertainty, fitting threshold, parameter uncertainty and numerical/export threshold separately for each feature. Fitted values, drawing nominal values and authored idealizations retain distinct source/status and intended use.
4. Keep fit observations separate from evaluated controls. Same-target or same-capture withheld samples retain their shared dependence. Separate semantic reviewer execution checks actual source identity and interpretation; numerical checks name artifact/query/reader and shared kernels.
5. Each branch retains source subset, intended use, detail/coverage, required features, criteria and local/remote/manual resources. A context overlay or mesh can satisfy its declared arrangement purpose while a working interface requires further metrology.
6. VLM selection can choose supported associations or compatible contributions within the current task. Preserve conflicting nominal/observed meanings; merge creates a new revision with repeated metric, semantic and saved-output checks.

## 2. Camera, metric and output conditions

1. Calibration belongs to the exact camera/lens/focus state and actual image grid. Cropping/resizing/undistortion has a recorded pixel map and compatible intrinsic/distortion convention. OpenCV PnP maps object/world coordinates into camera coordinates, with X right, Y down and Z forward. Translation uses the object-point units. Its inverse is separately identified for camera-to-world rays.
2. Held-out calibration images require a target-to-camera pose. Keep intrinsics/distortion frozen; use an externally known pose or fit that pose from a designated subset and evaluate separate reserved points. Report shared target uncertainty and test whether pose fitting masks a distortion error.
3. Open3D registration maps the named source cloud into the named target cloud. Record permitted rigid/similarity freedoms, normal/sampling settings, masks and whether the selected API returns a full or incremental transform. Partial overlap, repeated surfaces and planar geometry retain alternate or unobservable states.
4. The inspected [Open3D 0.20.0 ICP tutorial](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) defines fitness as inlier correspondences divided by source point count and inlier RMSE in coordinate-length units. Each actual adapter/version records its own definition and denominator. [CloudCompare](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode) uses explicit compared/reference ordering for its directed cloud/cloud or cloud/mesh fields; preserve sampling, search limits and excluded counts.
5. REC-12's photo route has camera evidence; its scan-only route has spatial registration evidence. The original broad camera-solution output is recorded as a conditional-output finding. DOM-19's actual outputs remain registration-transform and point-cloud.
6. REC-14 requires constrained-sketch, parametric-source and cad-solid together. Native OCS body capability alone supplies only its actual representation. DOM-23's original literal record combines point-cloud, measurement-set and model-brief with a mesh alternative entry, requiring all four artifacts under that contract. Its title's true cloud-or-mesh interpretation is a separate proposed correction. Explicit source conversion retains scope and lineage.
7. Parametric source is materialized into actual geometry before landmark/surface query or geometric comparison. REC-16's original output is measurement-set; its scoped edited model/source is retained as an ancillary revision. Baseline scan, transform, regions, masks and check rules stay fixed for comparable edit results.

### Cylinder-fitting candidate

The [PCL cylinder tutorial](https://pointclouds.org/documentation/tutorials/cylinder_segmentation.html), [SACSegmentationFromNormals API](https://pointclouds.org/documentation/classpcl_1_1_s_a_c_segmentation_from_normals.html) and [cylinder-model header](https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/sample_consensus/include/pcl/sample_consensus/sac_model_cylinder.h) supply the proposed cylinder adapter's contract. The API documentation identifies PCL 1.15.1-dev; the header uses mutable master. A future execution pins the selected installed release and binding.

1. Input: metric point cloud, corresponding normal cloud, original point IDs, normal-estimation neighborhood and the same index mapping after filtering/downsampling. Configure `SACSegmentationFromNormals<PointXYZ, Normal>` with `SACMODEL_CYLINDER`, the consensus method, coefficient optimization, normal-distance weight, iterations/probability, distance threshold, radius limits and any sourced axis/angle constraint.
2. Output: `segment(inliers, coefficients)` supplies inlier point indices and seven coefficients: axis point x/y/z at indices 0–2, axis direction x/y/z at 3–5, radius at 6. Point coordinates and radius use cloud length units; threshold/radius settings use the same unit convention. The tutorial's numeric settings remain examples. Retain the raw vector and named fields.
3. Check: validate point-normal correspondence, finite coefficients, nonzero normals/axis and positive bounded radius. Preserve normal weighting as part of the selected implementation's fit criterion; independently measure geometric residuals. Compare angular/axial coverage, region density, normal neighborhoods, radius-bound clipping and held-out controls. A short visible arc can leave radius or axis uncertain.
4. Handoff: retain fitted evidence, physical feature identity, finite extent, source allowance and uncertainty separately. Compare equivalent axis lines using a common datum and explicit direction convention; an arbitrary axis reference point supplies no finite part ends. REC-09 publishes sampled candidates; CAD-11 applies the checked feature evidence before supported solid construction.

## 3. CAD-02B — Calibrate camera poses from photographs and known controls

**Entry points.** [OpenCV calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) and [PnP](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html) compose state-matched intrinsic and pose records.

1. **CAD-02B-A01 — Bind photographs, target evidence and camera state.** Preserve originals/state. Separate target-calibration and pose/check controls. Select applicable calibration receipt or calibration action. Output: Camera/image/control manifest selecting REC-01 and REC-02 prerequisites. Check: Calibration covers the actual image/lens state; transformed images retain compatible intrinsics/distortion mapping.
2. **CAD-02B-A02 — Compose intrinsic calibration and per-image pose solutions.** Reuse matching intrinsics. Solve supported image poses. Retain alternatives and transform directions. Output: Per-camera intrinsic/distortion and per-image pose candidates with subaction receipts. Check: Each pose uses matching image coordinates/intrinsics; source length units determine translation scale.
3. **CAD-02B-A03 — Validate and publish camera solution.** Check withheld correspondences. Review residual coverage and pose alternatives. Publish only supported per-image solution states. Output: Camera-solution including camera model, image mapping, pose direction and check results. Check: Camera model/resolution and independent evidence match intended alignment use.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent identifies target/camera state and directs calibration/pose checks. |
| Software and agent | Software solves parameters; agent interprets controls and alternate poses. |
| Software handles ordinary cases | Checked target/capture classes run subactions; mismatched state or ambiguity enters review. |
| Deterministic supported case | Explicit matched camera state, target geometry and controls produce checked camera-solution. |

**Alternatives and target quality.** Target-based calibration plus per-image known-point pose. Reuse state-matched manufacturer/measured calibration with source identity. Documented photogrammetric camera solution with independent metric controls. Context overlay and precision feature alignment retain separate required pose/scale criteria.

**Proposed helpers.** calibration intake emits camera groups, target roles and per-image prerequisites. camera-solution composer links versioned calibration and pose receipts without rerunning valid stages. camera package checker emits per-image/control readiness for named consumers. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews source point identity; software compares independent projection and metric checks. Select coherent camera model/pose per image; retain conflicting control interpretations. Reproject all required controls and check shared frame/calibration consistency.

**Migration condition.** Automate checked camera/target classes after state mismatch, bad target units, pose ambiguity and withheld-check fixtures.

## 4. REC-01 — Calibrate camera intrinsics and distortion

**Entry points.** [OpenCV calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) documents target-image fitting; the held-out view needs its own target pose evidence.

1. **REC-01-A01 — Select calibrated target observations and hold-out views.** Group state-compatible images. Detect/review target points. Reserve independent views/controls. Output: Target/image-point sets with fit/hold-out roles and coverage report. Check: Poor spatial/orientation coverage or wrong target order is diagnosed before parameter fitting.
2. **REC-01-A02 — Estimate intrinsic and distortion parameters.** Fit selected camera model. Record all parameters/options and residuals. Compare justified model alternatives with unchanged check evidence. Output: Intrinsic matrix, distortion model/coefficients, fit poses and residual diagnostics. Check: Finite parameters and fit consistency accompany coverage/conditioning checks; unavailable diagnostics remain unresolved.
3. **REC-01-A03 — Check held-out distortion behavior and publish intrinsics.** Freeze intrinsic/distortion candidate and define held-out view pose evidence. Use known pose or estimate pose from its designated subset, preserving distinct evaluated points. Evaluate reserved controls/edge behavior and publish calibration scope and dependence. Output: Checked calibration with scope, residual maps and optional undistorted derivative/mapping. Check: Intrinsics remain tied to camera state and actual pixel grid; undistorted images use their recorded new matrix/distortion convention. Record shared target/calibration uncertainty and pose-fitting dependence; pose-fit points cannot count as independent validation points.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent reviews target/state and chooses justified model, software solves. |
| Software and agent | Detection/calibration automated; agent resolves coverage/outliers/model meaning. |
| Software handles ordinary cases | Checked camera-target class calibrates with explicit exception diagnostics. |
| Deterministic supported case | Fixed target correspondences/model/state and check criteria produce a calibration receipt. |

**Alternatives and target quality.** Known target calibration. Source-specific manufacturer calibration matched to state and checked. Documented self-calibration retained as its own estimate with independent controls. Context imagery may use lower-detail regional coverage; precision image measurement requires feature-region checks.

**Proposed helpers.** target-observation collector returns point identities, coverage and exclusions. intrinsic fitter emits candidates, residual distribution and declared observability findings. calibration validator emits region/state validity and derivative metadata. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** Software compares residual patterns and independent checks; VLM checks target evidence. Select one compatible model per physical state; preserve alternative models and source uncertainty. Rerun withheld tests and invalidate dependent poses if model changes.

**Migration condition.** Demonstrate target ordering, field coverage, state changes, held-out distortion and image-grid cases before routine automation.

## 5. REC-02 — Solve camera pose from known 3D-to-2D correspondences

**Entry points.** [OpenCV 4.13 PnP](https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html) documents method-specific point layouts, object-to-camera transforms and alternative solutions.

1. **REC-02-A01 — Bind 3D landmarks to calibrated image coordinates.** Match named 3D and image landmarks. Separate fitting/withheld correspondences. Check selected solver requirements and image state. Output: Pose input record with point IDs, units, image model, fit/check roles and geometric sufficiency. Check: Point configuration meets actual method rules; correspondences derive from exact CAD/image revisions.
2. **REC-02-A02 — Estimate object-to-camera pose candidates.** Solve declared model. Retain valid hypotheses/inliers. Record direction, units and inverse separately. Output: Candidate object-to-camera rotation/translation, inlier mask and residuals. Check: Check rotation/handedness, finite translation and required positive depths; solver success is a candidate result.
3. **REC-02-A03 — Validate independent reprojection and publish pose.** Reproject withheld landmarks. Compare alternatives and source identity. Publish checked pose/calibration package. Output: Camera-solution pose/check records with supported features and ambiguity status. Check: Wrong but low-fit-residual pose fails independent controls; output supplies pose, not reconstructed surfaces.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent resolves landmark correspondence and directs pose alternatives. |
| Software and agent | Software solves/checks; agent reviews ambiguous landmarks and visibility. |
| Software handles ordinary cases | Demonstrated fiducial/landmark classes run PnP; degeneracy or inconsistent state enters review. |
| Deterministic supported case | Explicit compatible correspondences/model/method and check criteria produce pose evidence. |

**Alternatives and target quality.** Surveyed fiducial pose. Known CAD landmarks with calibrated camera. Documented photogrammetric pose with separate metric anchors. Context pose and precision interface projection retain feature-specific accuracy and ambiguity requirements.

**Proposed helpers.** PnP preflight returns compatible correspondences and ambiguous/unobservable components. pose solver emits transform candidates, objective diagnostics and source-to-camera convention receipt. pose verifier returns per-landmark residual and feature-level readiness. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews landmark meaning; software compares independent reprojections and depth consistency. Select coherent pose; never average incompatible symmetry solutions. Reproject checks under selected pose and validate all downstream frame conversions.

**Migration condition.** Automate checked point/model classes after planar ambiguity, collinearity, outliers, wrong revision and camera-axis fixtures.

## 6. REC-07 — Estimate coarse transform between point clouds

**Entry points.** [Open3D global registration](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html) documents downsampled normals, FPFH descriptors, RANSAC correspondences and source-to-target transforms.

1. **REC-07-A01 — Bind both clouds and declare transform freedoms.** Bind source and target revisions. Select permitted freedoms and static overlap. Reserve controls and derive source-mapped coarse samples. Output: Registration manifest with source-to-target direction, rigid or justified similarity model and fit/check regions. Check: A planar/repetitive region cannot silently constrain all pose freedoms; source and target remain distinct.
2. **REC-07-A02 — Generate coarse alignment hypotheses.** Compute supported features or use identified landmarks. Estimate candidate transforms under permitted model. Record inliers, coverage and alternative poses. Output: Transform candidates, correspondence/inlier records and coarse fit diagnostics. Check: Check transform rotation/scale/handedness and spatial distribution of supporting matches.
3. **REC-07-A03 — Test withheld controls and publish initialization.** Measure withheld controls. Inspect spatial residuals and alternate poses. Publish selected transform or unresolved candidates. Output: Source-to-target transform/check records and alternatives with REC-08 readiness. Check: Low matching error cannot pass a wrong symmetry pose that fails controls.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent identifies overlap/datums and directs candidate generation. |
| Software and agent | Software proposes transforms; agent judges source regions and symmetry. |
| Software handles ordinary cases | Checked cloud/overlap classes use fixed preprocessing; degeneracy or scale mismatch enters review. |
| Deterministic supported case | Explicit correspondences/model/settings and independent controls produce coarse transform evidence. |

**Alternatives and target quality.** Surveyed targets or known CAD datums. Manual landmark initialization with numerical checks. FPFH/RANSAC global feature registration. Lower-detail context pose and working-interface alignment retain different controls/coverage and criteria.

**Proposed helpers.** cloud preflight emits role/frame/model manifest, masks and observability prerequisites. coarse registrar outputs hypotheses and exact source/target correspondences. coarse-check report emits control residuals and permitted downstream refinement state. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews region/landmark identity; software compares independent controls and coverage. Select coherent transform; retain symmetry/scale alternatives without matrix averaging. Recheck controls and source-to-target convention before refinement.

**Migration condition.** Demonstrate overlap, symmetry, scale error, dynamic-region and geometric-degeneracy fixtures before routine registration.

## 7. REC-08 — Refine registration and compare point-cloud surfaces

**Entry points.** [Open3D ICP](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) and [CloudCompare CLI](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode) document refinement and ordered surface comparisons.

1. **REC-08-A01 — Freeze initialization and comparison objective.** Bind initialization and roles. Select objective/normals/masks. Freeze fit and check regions. Output: Refinement specification with source-to-target initialization, objective and check configuration. Check: ICP initialization lies within supported convergence conditions; missing normals or degeneracy creates a named exception.
2. **REC-08-A02 — Refine transform and retain correspondence evidence.** Execute bounded refinement. Read returned full transform and diagnostics. Compare expected allowed motion and fit distribution. Output: Final source-to-target transform, iterations/status, correspondences and objective diagnostics. Check: Check rigid/similarity properties and original-to-final mapping; reject silent double-application of initialization.
3. **REC-08-A03 — Measure independent and directional surface differences.** Compare withheld controls. Measure fixed regional surfaces and non-overlap. Publish fit and independent evidence separately. Output: Regional distance maps, control residuals, non-overlap masks and transform readiness. Check: Empty/low-overlap regions cannot pass through summary statistics; dense patches cannot conceal failing interfaces.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects source-supported objective/regions and diagnoses convergence. |
| Software and agent | Software refines/measures; agent evaluates surface meaning and ambiguity. |
| Software handles ordinary cases | Demonstrated registration classes use fixed settings; low overlap/degeneracy/outliers enter review. |
| Deterministic supported case | Explicit initialization, samples, objective and check rules produce repeatable transform/comparison records. |

**Alternatives and target quality.** Point-to-point or point-to-plane ICP according to evidenced normals/geometry. Documented robust objective with separately recorded settings. Control-target transform retained without surface refinement when source intent requires it. Context alignment uses declared regional detail; precision interfaces require independent metrology/coverage.

**Proposed helpers.** refinement preflight emits supported objective, overlap and observability diagnostics. refinement adapter emits transform lineage, convergence and correspondence receipt. comparison reporter emits direction-specific residual/coverage and control checks. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** Software compares independent controls and regional coverage; VLM reviews corresponding physical surfaces. Select one justified alignment; preserve incompatible transforms/residual interpretations. Recompute fixed directional distances and controls under selected transform.

**Migration condition.** Demonstrate wrong initialization, partial overlap, density imbalance, symmetry, unreliable normals and non-overlap statistics before automation.

## 8. REC-09 — Segment point clouds and fit candidate primitive evidence

**Entry points.** [Open3D point clouds](https://www.open3d.org/docs/latest/tutorial/geometry/pointcloud.html) documents segment_plane and DBSCAN, a density-based point-clustering method. The PCL cylinder candidate in section 2 adds matched point/normal input, consensus controls, inliers and seven axis/radius coefficients. Candidate labels retain physical-feature interpretation as a separate action.

1. **REC-09-A01 — Select observed regions and preserve point membership.** Identify feature regions. Record masks/density and exclusions. Preserve sample-to-original links. Output: Region masks and original-point index mapping with sampling/coverage description. Check: Region includes stated surface evidence without silently removing inconvenient samples.
2. **REC-09-A02 — Generate plane, cluster and cylinder candidates.** Validate region and point-normal index correspondence; select plane, cluster or PCL cylinder model and record sourced settings without inheriting tutorial numeric examples. Run the declared estimator and retain inlier/outlier indices, raw coefficients and exact settings; decode cylinder axis point, direction and radius in the recorded frame/unit. Compare justified threshold/radius/normal-neighborhood alternatives and held-out geometric residuals; preserve partial-arc or mixed-surface candidates for the independent support check. Output: Segmented point-cloud with original indices; plane/cluster candidates or cylinder inlier indices and seven coefficients: axis point x,y,z [0–2], axis direction x,y,z [3–5], radius [6]; fit residuals and coverage records. Check: Check point-normal alignment, finite seven-value cylinder output, nonzero axis direction, positive radius and configured bounds. Independently measure sample-to-cylinder geometric residuals and axial/angular coverage; a threshold/bound-clipped candidate retains that state, and low residual alone cannot resolve radius or axis uncertainty.
3. **REC-09-A03 — Check sampling bias and publish primitive evidence.** Measure held-out residuals. Compare parameter sensitivity and spatial coverage. Publish candidates with feature-specific readiness. Output: Point labels and measurement records with parameter source, support, residual distribution and readiness. Check: Low residual on a narrow patch does not resolve unconstrained radius/axis/extent; required parameter checks remain unresolved.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects feature evidence and directs candidate segmentation. |
| Software and agent | Software proposes plane, cluster and supported PCL cylinder candidates; agent interprets physical surfaces and parameter support. |
| Software handles ordinary cases | Checked surface classes segment automatically; mixed/partial/unstable fits enter review. |
| Deterministic supported case | Explicit regions, model/settings and checked criteria produce candidate evidence. |

**Alternatives and target quality.** Manual region segmentation with original indices. Open3D plane/DBSCAN candidates. PCL normal-assisted cylinder candidate with matched point/normal indices, explicit consensus controls, coefficient contract and source-specific radius/axis constraints. Context clusters and precision analytic interfaces retain different required support/uncertainty.

**Proposed helpers.** region selector emits immutable point-membership and coverage manifests. primitive candidate adapter accepts immutable point/normal IDs, original-index mapping and typed model settings; it emits memberships, raw seven-value cylinder coefficients, named parameters, coverage and residual diagnostics. It rejects invalid normal correspondence and coefficients before publication. fit evidence checker emits parameter confidence basis and source-dependent limitations. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews surface identity; software compares held-out residuals and parameter stability. Merge compatible region evidence by original point ID; retain conflicting primitive interpretations. Refit/check changed support and independently review resulting feature identity.

**Migration condition.** Demonstrate mixed planes, narrow arcs, uneven density, outliers, threshold sensitivity, stale normal ordering, zero normals, radius-bound clipping and missing coverage before routine primitive classification. Future fixtures preserve equivalent axis lines and require separately sourced finite ends.

## 9. CAD-11 — Fit analytic features to scans or image-derived point clouds

**Entry points.** [Original CAD record](../workflows/cad-paths.json) and [reconstruction research](../reconstruction.md) define fitting on metric registered evidence. Open3D planes and section 2's PCL cylinder adapter supply specific candidate estimators. [Point03](point-03-operations.json) defines actual supported solid construction.

1. **CAD-11-A01 — Verify metric evidence and select functional features.** Verify metric/frame evidence. Select required features and sampled regions. Retain observed/occluded boundaries and fit/check roles. Output: Feature fit plan with sample membership, observation coverage and dimension provenance. Check: Unregistered or scale-ambiguous data cannot support metric feature dimensions.
2. **CAD-11-A02 — Estimate analytic parameters and uncertainty.** Validate the declared estimator input, including matched point/normal indices for PCL cylinders; fit with source-backed threshold/radius constraints in cloud units and retain raw coefficients. Decode axis point/direction/radius, retain sample masks and normal-neighborhood provenance, and measure geometric residuals and parameter sensitivity on declared region/setting alternatives. Compare independent controls and alternate models; record observable parameter components, axis reference/sign convention and separately supported finite extent before CAD construction. Output: Parameters, units/frame, support indices, residual distribution and sensitivity/uncertainty records. PCL cylinder output retains raw seven coefficients plus named axis point [0–2], direction [3–5] and radius [6]; finite extent and feature identity have separate evidence. Check: Verify finite supported coefficients and axis/radius conventions, then compare independent feature distances and axial/angular coverage. Narrow arcs, short spans, normal errors, radius-bound clipping or biased samples leave affected parameters unresolved despite low residual; an infinite fitted cylinder supplies no finite end locations.
3. **CAD-11-A03 — Construct and validate supported CAD feature geometry.** Construct source-linked supported features. Check actual solid and functional dimensions. Compare withheld samples and saved readback. Output: Measurement-set plus actual valid cad-solid, source/fit mapping and native readback; incomplete surfaces retain typed intermediate state. Check: A plane or open surface alone does not fulfill cad-solid; every solid-defining assumption is explicit and required features checked.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent identifies interfaces and fit/model meaning, directs construction. |
| Software and agent | Software fits/measures; agent interprets coverage and authored feature choices. |
| Software handles ordinary cases | Demonstrated sampled-feature classes fit/build with exception diagnostics. |
| Deterministic supported case | Explicit metric regions, estimator, complete feature plan and checks produce typed measurements/solid. |

**Alternatives and target quality.** Direct independent interface measurements with scan context. Source-linked analytic surface/axis fits. Keep sampled mesh as declared context/collision reference. Lower-detail context versus working interface receives distinct observation/uncertainty and closure requirements.

**Proposed helpers.** analytic-fit intake emits feature/support/criteria manifest and unresolved prerequisites. analytic estimator accepts feature/model/support/normal/settings/criteria records and emits raw and named parameters, inlier IDs, coverage, diagnostics and observable components. Its PCL cylinder dependency follows section 2, including installed-release checks and normal-index correspondence; axis comparison and separately sourced finite extent precede CAD construction. fitted-feature builder emits native solid and feature-measurement/uncertainty ledger. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM checks physical feature identity/source interpretation; software checks support, uncertainty and held-out differences. Select sourced parameter meaning per feature; never average nominal and measured values without an explicit justified rule. Rebuild new feature revision and repeat solid/interface/source/held-out/readback checks.

**Migration condition.** Demonstrate partial coverage, biased sampling, mixed surfaces, uncertain radius/axis, invalid point-normal mapping, bound clipping, missing finite extent/closure and independent interface fixtures.

## 10. REC-12 — Register existing CAD to calibrated photographs or scan points

**Entry points.** [PnP](https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html), [global registration](https://www.open3d.org/docs/latest/tutorial/pipelines/global_registration.html) and [ICP](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) supply separate photo and scan routes.

1. **REC-12-A01 — Bind exact CAD and observation-route evidence.** Pin CAD/observation revisions. Obtain actual CAD geometry and named landmarks. Choose photo or surface branch and reserve controls. Output: Route manifest with materialized CAD revision, observation identities, units/frame and fit/check landmarks. Check: Source text alone cannot provide queried CAD landmarks; photo intrinsics match actual preprocessing.
2. **REC-12-A02 — Estimate route-specific CAD alignment candidates.** Run selected route with explicit roles. Retain candidate transforms and diagnostics. Check actual scale/handedness and matched component identity. Output: Photo CAD-to-camera pose candidates or scan-to-CAD spatial transform candidates with receipts. Check: Rigid CAD alignment preserves geometry; scan route creates no camera parameters from absent observations.
3. **REC-12-A03 — Validate alignment and publish conditional outputs.** Evaluate withheld route-specific checks. Review symmetry/identity and fit coverage. Publish measured transform and actual camera evidence when present. Output: Measurement-set with spatial registration/controls; photo branch also emits camera-solution. Scan-only branch records original camera-output mismatch explicitly. Check: Original REC-12 output list is preserved as a finding; scan-only spatial records cannot satisfy a camera-consuming handoff.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects route/landmarks and directs evidence-based registration. |
| Software and agent | Software estimates/checks transforms; agent interprets CAD-observation identity. |
| Software handles ordinary cases | Checked CAD/capture classes register; wrong revision, symmetry or insufficient controls enters review. |
| Deterministic supported case | Explicit actual geometry, correspondences/surfaces and fixed checks produce route-specific output. |

**Alternatives and target quality.** Surveyed CAD fiducials with calibrated photo pose. Known datum alignment to metric scan. Global/ICP surface registration of declared CAD tessellation. Context overlay versus working interface uses individual control/uncertainty requirements; conditional scan output is a proposal correcting the original broad output list.

**Proposed helpers.** CAD observation binder emits route-specific geometry/control manifests. route registrar preserves native CAD and emits conditional pose/spatial records. conditional registration exporter emits supported branch artifacts and unmet original output labels. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews visible feature identity; software compares independent projection/surface evidence. Select coherent route transform; combine complementary checks without inventing missing camera data. Recheck control/interface alignment and all requested image/world conversions.

**Migration condition.** Demonstrate stale CAD source, wrong assembly state, tessellation error, partial overlap, photo-grid mismatch and scan-only output cases.

## 11. REC-13 — Anchor a screen sketch to a 3D surface

**Entry points.** Fresh official [Blender Scene RNA source](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_scene_api.cc) describes world-space Scene.ray_cast; [Object RNA source](https://raw.githubusercontent.com/blender/blender/main/source/blender/makesrna/intern/rna_object_api.cc) describes object-space Object.ray_cast. Both query evaluated geometry. Pin the selected installed release.

1. **REC-13-A01 — Bind sketch view, camera and hit surface.** Pin source stroke/camera/geometry. Select target surface and stroke interpretation. Check actual ray interface and view mapping. Output: Anchor manifest with camera/view/geometry revision, target components and stroke meaning. Check: View or geometry mismatch invalidates anchor prerequisites; a screenshot alone cannot establish intended depth.
2. **REC-13-A02 — Cast rays and record hit alternatives.** Map stroke sample to camera ray. Intersect declared evaluated geometry. Retain all supported candidate/miss/occlusion evidence. Output: Hit/miss/ambiguous records with world/local position, object/primitive ID, depth and source pixel. Check: A hit is calculated from selected geometry; no-hit intervals are not bridged as measured surfaces.
3. **REC-13-A03 — Reproject anchors and publish measurement evidence.** Reproject and compare source strokes. Check target/primitive identity and curve continuity. Publish calculated anchors and named sketch prerequisites. Output: Anchor measurement-set with pixel/object/primitive lineage, residuals and downstream sketch prerequisites. Check: Anchors do not themselves become independent physical measurements or constrained sketch; remeshing invalidates unstable primitive references.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent chooses surface/stroke meaning and directs ray queries. |
| Software and agent | Software casts/reprojects; agent resolves target/occlusion ambiguity. |
| Software handles ordinary cases | Checked camera/target classes anchor ordinary strokes; misses/multiple surfaces enter review. |
| Deterministic supported case | Explicit calibrated view, target geometry, stroke samples and intersection rules produce calculated anchors. |

**Alternatives and target quality.** Draw on an explicit CAD datum plane. Known orthographic view with declared scale/plane. Calibrated perspective ray-to-surface trace. Appearance annotation and working-feature anchor use distinct physical evidence and downstream constraint requirements.

**Proposed helpers.** anchor intake emits camera/ray conventions, surface selection and feature prerequisites. ray-anchor adapter emits full ray/hit provenance, candidate ordering and validity states. anchor verifier emits view residuals and explicit planar/nonplanar feature states. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews full-view target meaning; software compares ray/target/reprojection evidence. Select supported anchor segments by source sample; preserve depth/surface alternatives without averaging hits. Reproject all merged anchors and recheck target identities, continuity and intended plane.

**Migration condition.** Demonstrate occlusion, no-hit, multiple-depth, perspective/orthographic, preprocessing and remesh-index cases before routine anchoring.

## 12. REC-14 — Remodel segmented scan evidence as parametric CAD

**Entry points.** [Original reconstruction record](../workflows/reconstruction-paths.json) requires all three outputs. [Point03](point-03-operations.json) supplies native constraint, source-generation and solid capability boundaries.

1. **REC-14-A01 — Define feature evidence and all required editable outputs.** Map measured/drawing/fitted values to features. Declare hidden-feature decisions and required constraints. Select backend route fulfilling all three representations. Output: Feature/parameter provenance plan and backend combination capable of all three outputs. Check: Source evidence and output capability are explicit; unsupported editable artifact blocks full operation readiness.
2. **REC-14-A02 — Author constrained source and materialize geometry.** Author source-linked constraints and parameters. Generate supported features/solid. Read actual output types and retain source/native identities. Output: Constrained-sketch, parametric-source and actual cad-solid candidates with linked feature IDs. Check: CadQuery/source+solid without native constrained sketch remains partial; OCS native body without feature/source outputs remains partial.
3. **REC-14-A03 — Verify editability, interfaces and fixed scan comparisons.** Measure interfaces and fixed held-out regions. Reopen saved native/source/solid artifacts. Check supplied variant and publish each output's readiness. Output: Validated constrained-sketch, parametric-source and cad-solid with regional residual and saved-readback reports. Check: All required outputs exist and retain intended editability; low scan error cannot replace interface/source checks.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent chooses source-supported feature interpretation and directs editable authoring. |
| Software and agent | Software fits/builds/checks explicit features; agent resolves nominal/observed meaning. |
| Software handles ordinary cases | Demonstrated feature families produce all required outputs; missing evidence/capability enters review. |
| Deterministic supported case | Explicit evidence choices, supported source/sketch/solid generation and checks produce the three artifacts. |

**Alternatives and target quality.** FreeCAD source creating native constraints and solid with retained source. Compatible evidenced composition of fit, sketch and procedural-solid adapters. Actual partial native body or reference mesh as separately typed derivative. Context remodeling and precision functional model have distinct source/coverage/editability requirements.

**Proposed helpers.** remodeling planner emits feature dependencies and required artifact/output capability matrix. editable remodel composer emits three artifacts plus dependency and source mapping. editable-output verifier emits each representation's checks and cross-artifact lineage. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM compares source intent; software compares interfaces, fixed residuals and actual editable artifacts. Select coherent parameter meaning per feature; combined source creates a new authored revision. Regenerate all three outputs and repeat source, interface, editability and saved checks.

**Migration condition.** Demonstrate feature-source mapping, hidden geometry, three-output completeness, unstable selectors, saved constraints and supplied variants before routine generation.

## 13. REC-15 — Reconcile scan surfaces with dimensioned drawings

**Entry points.** [REC-R04](../workflows/details/rec-r04.md) preserves drawing and scan evidence; [CloudCompare](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode) and [ICP](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) supply measured comparisons.

1. **REC-15-A01 — Bind source revisions, datums and discrepancy purpose.** Pin drawing and scan revisions. Identify corresponding features/datums. State comparison purpose and reserve independent checks. Output: Feature correspondence and datum/control manifest with nominal/observed evidence classes. Check: Revision/configuration mismatch is explicit; raster pixel estimates do not replace printed dimension values.
2. **REC-15-A02 — Align evidence under fixed datum choices and measure differences.** Apply declared datum alignment. Measure paired features and withheld dimensions. Report regional coverage, excluded data and uncertainty. Output: Transform receipt and per-feature nominal-versus-observed differences with coverage. Check: Optimizer adjustment cannot silently remove a required nominal-versus-observed deviation.
3. **REC-15-A03 — Publish reconciliation choices and preserved conflicts.** Review conflict causes and evidence. Record supported selection or retained alternatives. Publish measurement-set and owning next action. Output: Reconciled measurement-set with nominal, measured, fit and authored candidates, selected-use reason and open conflicts. Check: Unresolved controlling choice blocks only dependent feature; source revision discrepancies remain visible.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets source revisions/datums and discrepancy meaning. |
| Software and agent | Software aligns/measures; agent decides evidence-supported association. |
| Software handles ordinary cases | Checked datum/feature classes compare automatically; conflicts enter review. |
| Deterministic supported case | Explicit paired features, datum, target meaning and criteria produce a reconciliation ledger. |

**Alternatives and target quality.** Drawing-nominal and observed variants retained separately. Independent direct interface metrology. Calibrated photo-to-CAD comparison for supported features. Context mismatch map versus working-interface reconciliation retains distinct accuracy and intent requirements.

**Proposed helpers.** reconciliation intake emits paired feature sources, datum choices and separate fit/check roles. paired-feature comparator emits direction/method/uncertainty-specific discrepancies. reconciliation exporter emits source-separated values, reasons and downstream readiness. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM compares source meaning; software quantifies independent discrepancies. Merge complementary evidence by feature ID while retaining nominal/observed alternatives. Recompute affected comparisons and independently review value meaning.

**Migration condition.** Demonstrate wrong revision, datum bias, printed-versus-pixel value, physical variation, missing coverage and conflicting target intent.

## 14. REC-16 — Iterate CAD edits against registered evidence

**Entry points.** OCS automation (`${OCS_ROOT}/docs/automation/API-SPEC.md`) supplies revision/request/readback interfaces; [CloudCompare](https://cloudcompare.org/doc/wiki/index.php?title=Command_line_mode) and [ICP](https://www.open3d.org/docs/latest/tutorial/pipelines/icp_registration.html) supply source-ordered comparison evidence.

1. **REC-16-A01 — Freeze comparison baseline and bounded edit scope.** Bind baseline/source revisions. Measure fixed controls/regions. Specify exact edit and expected dependent changes. Output: Baseline CAD/scan/configuration receipt and exact edit/check dependencies. Check: No changed registration/mask/threshold can silently enter the before/after comparison.
2. **REC-16-A02 — Apply scoped edit and read actual resulting geometry.** Verify target revision. Apply declared edit/regeneration. Read actual result and preserve prior artifact. Output: New CAD/source revision and readback/operation receipt; prior revision preserved. Check: Successful command requires expected valid geometry and preserved intended interfaces.
3. **REC-16-A03 — Compare fixed evidence and publish revision deltas.** Repeat identical regional/control checks. Compare dimension and residual deltas. Publish measurement-set and retained artifacts. Output: Per-region/feature delta report, affected invariants, saved-readback evidence and next bounded action. Check: Geometry fit reduction cannot pass an interface violation; refitting alignment creates a separately labelled branch.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent selects supported edit and interprets fixed-evidence deltas. |
| Software and agent | Software edits/regenerates/checks; agent diagnoses meaning and dependencies. |
| Software handles ordinary cases | Checked edit families compare automatically; stale revisions or unintended changes enter review. |
| Deterministic supported case | Explicit edit, revisions, fixed scan/transform and criteria produce comparable deltas. |

**Alternatives and target quality.** Cross-section and direct functional metrology. Bounded native edit or source parameter edit with regeneration. Read-only comparison of supplied revisions when no edit is requested. Context surface improvement and working-interface compliance keep distinct success criteria.

**Proposed helpers.** edit-baseline binder emits immutable comparison inputs and bounded feature plan. revision edit executor emits actual changed geometry and dependency receipt. revision comparator emits comparable deltas, invariants and failed dependencies. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM checks source/feature meaning; software compares fixed regional/functional results. Select candidate or author compatible feature combination as new revision; preserve all prior results. Rerun identical comparisons, invariants and saved readback on merged revision.

**Migration condition.** Demonstrate stale revision, partial mutation, selector drift, hidden alignment change, interface regression and baseline retention cases.

## 15. DOM-19 — Register scan to building frame

**Entry points.** [IfcOpenShell placement](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/edit_object_placement/index.html), [units](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/unit/assign_unit/index.html) and [georeference](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/georeference/index.html) define distinct coordinate records.

1. **DOM-19-A01 — Resolve scan, building and survey frame definitions.** Pin IFC/scan/control revisions. Resolve local placements, units and target datum. Separate survey CRS/map conversion and test control geometry. Output: Frame manifest naming scan, IFC local/building and survey/map frames with transform dependencies. Check: Blank georeference entities supply no coordinates; one datum plus insufficient control geometry cannot determine all pose freedoms.
2. **DOM-19-A02 — Estimate supported scan-to-building transform.** Build explicit target/control reference. Estimate permitted transform and refine when supported. Retain hypotheses, scale and normalization transforms. Output: Source-scan-to-building transform candidates with control/surface receipts. Check: Local numerical shift has recorded inverse; no CRS, floor elevation or camera pose is inferred from fit.
3. **DOM-19-A03 — Validate controls and publish aligned derivative.** Measure withheld controls and regional residuals. Create separately identified aligned cloud. Read back coordinates and publish both original output types. Output: Registration-transform plus transformed point-cloud derivative with original-index/source mapping and check report. Check: Outputs are exactly registration-transform and point-cloud; IFC semantics and raw scan remain preserved.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets building/survey datums and directs control alignment. |
| Software and agent | Software resolves placements/registers; agent reviews source correspondences. |
| Software handles ordinary cases | Checked frame/control classes align; unknown units/CRS, symmetry or low coverage enters review. |
| Deterministic supported case | Explicit frame chains, controls, permitted model and check criteria produce aligned derivative. |

**Alternatives and target quality.** Surveyed target transformation. Coarse control alignment followed by justified surface refinement. Local building-frame registration without geographic claim when that is the supplied target. Context scene versus precise opening/interface registration has distinct regional evidence requirements.

**Proposed helpers.** building-frame resolver emits explicit unit/placement/map chains and control sufficiency. building registrar returns transform candidates and source/target sampling/normalization receipts. building-registration publisher emits aligned cloud, transform chain and source/readback checks. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews physical building features; software checks independent controls and frame chain. Select coherent datum/transform; preserve alternate geographic interpretations and source-model discrepancies. Reapply selected chain to fresh derivative and repeat regional/unit/datum/readback checks.

**Migration condition.** Demonstrate nested placement, metre/millimetre difference, wrong vertical datum, blank CRS, large coordinate shift, partial façade and wrong symmetry fixtures.

## 16. DOM-23 — Scan or mesh to parametric CAD remodeling

**Entry points.** [Original domain record](../workflows/domain-paths.json) retains its literal inputs and outputs. [Point03](point-03-operations.json) and OCS skill (`${CODEX_HOME}/skills/ocs-engineering/SKILL.md`) supply construction and evidence contracts.

1. **DOM-23-A01 — Audit literal input contract and target remodeling meaning.** Check exact original input roles. Bind cloud/mesh provenance and target brief. Record complete literal route or named proposed contract/conversion dependency. Output: Input/lineage manifest, target use/interface criteria and explicit route status; proposed true cloud-or-mesh interpretation recorded separately. Check: Title 'scan or mesh' does not erase mandatory fields; each conversion retains original source and explicit information changes.
2. **DOM-23-A02 — Author parametric source and actual feature geometry.** Select source-supported parameter meaning. Author retained parametric construction source. Generate/read actual solid and feature IDs. Output: Parametric source and actual solid candidates with feature/source mapping and generation receipt. Check: Both required output representations exist; arbitrary mesh wrapper is not a parametric feature family.
3. **DOM-23-A03 — Validate functional interfaces and saved parametric output.** Measure independent interfaces and held-out regions. Read back saved solid and source-driven result. Publish both outputs with per-feature readiness. Output: Checked source/solid with held-out regional distances, interface measurements and saved/rebuild receipts. Check: Appearance agreement or aggregate fit cannot pass a failing functional interface; source reproduces intended geometry.

| Execution option | Action and selection condition |
| --- | --- |
| Agent directs work | Agent interprets target function/source evidence and directs parametric reconstruction. |
| Software and agent | Software fits/builds/checks; agent resolves parameter meaning and contract exceptions. |
| Software handles ordinary cases | Demonstrated input/feature families generate outputs; missing literal inputs/coverage/capability enters review. |
| Deterministic supported case | Explicit complete input contract, source choices, backend and checks produce source and solid. |

**Alternatives and target quality.** Literal original four-input route with linked cloud and mesh. Proposal: true cloud-or-mesh contract retaining measurement-set and brief; original record stays unchanged. Explicitly scoped mesh-to-cloud sampling with lineage before the literal cloud role; missing mesh remains its own prerequisite. Reference mesh/context derivative or analytic surface route has separately declared outputs; working interfaces require parametric/metric checks.

**Proposed helpers.** remodeling intake distinguishes literal four-input route from separately proposed true alternative or explicit sampled-cloud route. remodeling composer emits parameter/source dependency graph and actual CAD output. remodel verifier emits output-specific editability/geometry/source reports. Action fields specify the complete input/output/dependency/check contract.

**Selection and merge.** VLM reviews source/feature intent; software checks interfaces, held-out residuals and source persistence. Select compatible source meanings or author a new combined source revision; preserve conflicts. Regenerate required outputs and repeat functional, fixed-evidence, editability and saved checks.

**Migration condition.** Demonstrate literal versus proposed input route, sampling lineage, hidden geometry, missing interfaces, parameter persistence and source-rebuild cases.

## 17. Resource order and meaningful future cases

1. Begin with metadata, known controls and required interfaces. Camera point fitting precedes dense image processing; coarse/static cloud regions precede full-resolution matching and distances. Preserve original indices and declared approximation when downsampling.
2. Local CPU/RAM estimates name image size, point/normal/feature count, candidate count, faces, iterations and sample density. Local GPU use belongs to the actual selected display or processing backend. Remote inference calls/tokens/latency/cost and manual landmark, segmentation, tracing and metrology effort have separate records.
3. Small known-point camera problems, bounded ray queries, regional analytic fits and large-cloud comparisons receive different resource estimates. Actual performance claims require hardware, versions, source size, settings and run evidence. Learned reconstruction is a separate upstream point; it is not an implicit prerequisite for every alignment.
4. Initial ambiguous source/correspondence work can use higher reasoning effort. Explicit checked correspondences, source regions, models and criteria support software paths. Migration occurs per demonstrated action/input class after expected success, ambiguity, invalidity and interruption cases have been tested under implementation scope.
5. Camera fixtures include wrong target units, camera-state change, stale cropped intrinsics, pose direction error, planar/symmetric alternatives and held-out pose leakage. Cloud fixtures include low overlap, repeated/planar geometry, unknown scale, dynamic regions, bad normals, uneven density and directed-distance ordering.
6. Fit fixtures include mixed surfaces, incomplete angular/axial coverage, low residual with uncertain radius and nominal/observed disagreement. Ray fixtures include occluders, multiple depths, no hit, near-tangent rays, world/object-space confusion and evaluated-mesh index changes.
7. Remodeling fixtures include incomplete required outputs, lost native constraints, source-only geometry, literal DOM-23 missing inputs, functional-interface regression, fixed-baseline violation and source rebuild. Building fixtures include nested placements, unit versus `is_si` convention, blank map metadata, vertical datum mismatch and preserved numerical origin shifts.
8. Interruption fixtures retain raw/model request IDs and partial responses, reconcile completion, reject malformed selection rows and recheck source hashes before resumption. A changed calibration invalidates dependent poses/rays; changed scan masks/fits invalidate affected features; changed CAD revision invalidates its dependent comparisons. Independent checked regions remain usable.

[Software review](reviews/point-05-software.md), [visual review](reviews/point-05-visual.md) and [source review](reviews/point-05-sources.md) retain source conditions and findings. [Designer notes](reviews/point-05-designer.md) record source summaries and static documentary checks.
