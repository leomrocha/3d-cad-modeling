"""Shape rankings preserve variant ambiguity; sketch constraints require explicit approval."""

import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from shape_match import match, mate_check, pose_from_anchors, rigid  # noqa: E402
from shape_recover import classify_ring  # noqa: E402
from shape_sketch import proposals, solve, vectorize  # noqa: E402


@unittest.skipUnless(importlib.util.find_spec("numpy"), "optional NumPy")
class ShapeChecks(unittest.TestCase):
    def test_rigid_transform_rejects_scale_and_mirror(self):
        import numpy as np

        for bad in (2, -1):
            m = np.eye(4)
            m[0, 0] = bad
            with self.assertRaises(ValueError):
                rigid(m)
        with self.assertRaises(ValueError):
            pose_from_anchors(
                {
                    "candidate_mm": [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
                    "world_mm": [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
                }
            )

    @unittest.skipUnless(importlib.util.find_spec("open3d"), "optional Open3D")
    def test_matching_counts_distinct_poses_per_asset(self):
        import hashlib
        import numpy as np

        root = Path(__file__).resolve().parent / "fixtures/mesh-position"
        path = root / "plate-10.stl"
        identity = np.eye(4)
        points = [[0, 0, 0], [60, 0, 0], [0, 40, 0]]
        near = identity.copy()
        near[0, 3] = 0.5e-6
        row = dict(
            id="plate",
            path=path.name,
            sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            unit="mm",
            poses=[identity.tolist(), near.tolist()],
            anchors=[dict(candidate_mm=points, world_mm=points)],
        )
        job = dict(
            candidates=[row],
            world_check_points_mm=[[0, 0, 0], [60, 0, 0], [60, 40, 0]],
            max_point_error_mm=0.001,
        )
        result = match(job, root)
        self.assertEqual(result["status"], "one-tested-pose")
        self.assertEqual([x["hypothesis_count"] for x in result["ranked"]], [3])
        half_turn = np.diag([-1.0, -1.0, 1.0, 1.0])
        half_turn[:2, 3] = [60, 40]
        row["poses"].append(half_turn.tolist())
        result = match(job, root)
        self.assertEqual(result["status"], "ambiguous")
        self.assertEqual(
            sorted(x["hypothesis_count"] for x in result["ranked"]), [1, 3]
        )

    def test_mating_bounds_and_hand(self):
        import numpy as np

        target = dict(
            kind="bore",
            diameter_mm=8,
            axis=[0, 0, -1],
            center_mm=[0, 0, 0],
            direction="opposed",
            diametral_clearance_mm=[0.05, 0.15],
            axial_limit_mm=0.01,
            lateral_limit_mm=0.01,
            angle_limit_deg=0.5,
        )
        model = dict(kind="pin", diameter_mm=7.9, axis=[0, 0, 1], center_mm=[0, 0, 0])
        self.assertTrue(mate_check(model, target, np.eye(4))["passed"])
        model["center_mm"] = [0.1, 0, 0]
        self.assertFalse(mate_check(model, target, np.eye(4))["passed"])
        target["diametral_clearance_mm"] = [0.2, -0.1]
        with self.assertRaises(ValueError):
            mate_check(model, target, np.eye(4))

    @unittest.skipUnless(importlib.util.find_spec("shapely"), "optional Shapely")
    def test_ellipse_preserves_polygon(self):
        import numpy as np

        theta = np.linspace(0, np.pi * 2, 33)
        self.assertEqual(
            classify_ring(np.transpose([2 * np.cos(theta), 3 * np.sin(theta)]), 0.001)[
                "kind"
            ],
            "polygon",
        )
        self.assertEqual(
            classify_ring(np.transpose([2 * np.cos(theta), 2 * np.sin(theta)]), 0.001)[
                "kind"
            ],
            "faceted-circle",
        )

    @unittest.skipUnless(importlib.util.find_spec("scipy"), "optional SciPy")
    def test_approved_relations_only(self):
        graph = dict(vertices_px=[[0, 0], [30, 1], [29, 20]], lines=[[0, 1], [1, 2]])
        items = proposals(graph, 8, None)
        self.assertEqual(
            solve(graph, items, [], 3)["vertices_px"], graph["vertices_px"]
        )
        got = solve(graph, items, ["horizontal-0"], 3)
        self.assertLess(
            abs(got["vertices_px"][0][1] - got["vertices_px"][1][1]), 0.0001
        )
        with self.assertRaises(ValueError):
            solve(graph, items, ["horizontal-0"], 0.01)

    @unittest.skipUnless(importlib.util.find_spec("cv2"), "optional OpenCV")
    def test_stale_external_pixel_mask(self):
        import numpy as np
        import cv2

        raw = cv2.imencode(".png", np.full((20, 20), 255, np.uint8))[1].tobytes()
        with self.assertRaisesRegex(ValueError, "another sketch"):
            vectorize(raw, 100, None, 1, 5, {"source_sha256": "changed", "mask": []})
