import hashlib
import math
import unittest

from translator.bore_check import verify_bytes


def fixture_facets(diameter):
    """Independent synthetic triangulation: four planar fans around each rim."""
    count = 96
    corners = [(0, 0), (60, 0), (60, 40), (0, 40)]
    rim = [(17 + diameter/2 * math.cos(i*math.tau/count),
            23 + diameter/2 * math.sin(i*math.tau/count)) for i in range(count)]
    cap = []
    for i in range(count):
        corner = (2 + i//24) % 4
        j = (i+1) % count
        cap.append((rim[j], rim[i], corners[corner]))
        if j % 24 == 0:
            cap.append((rim[j], corners[corner], corners[(corner+1) % 4]))
    facets = []
    for tri in cap:
        facets.append(tuple((*p, 10) for p in tri))
        facets.append(tuple((*p, 0) for p in reversed(tri)))
    for loop in (corners, list(reversed(rim))):
        for a, b in zip(loop, loop[1:] + loop[:1]):
            facets.extend([((*a, 0), (*b, 0), (*a, 10)), ((*b, 0), (*b, 10), (*a, 10))])
    return facets


def encode(facets):
    lines = ["solid fixture"]
    for triangle in facets:
        lines += ["facet normal 0 0 0", "outer loop"]
        lines += ["vertex " + " ".join(map(str, p)) for p in triangle]
        lines += ["endloop", "endfacet"]
    return ("\n".join(lines) + "\nendsolid fixture\n").encode("ascii")


class BoreFixture(unittest.TestCase):
    def test_accepts_both_native_sizes_with_independent_triangulation(self):
        for diameter in (10, 12):
            with self.subTest(diameter=diameter):
                data = encode(fixture_facets(diameter))
                result = verify_bytes(data, diameter)
                self.assertEqual(result["rim_count"], 2)
                self.assertEqual(result["continuous_bore_panels"], 96)
                self.assertEqual(result["stl_sha256"], hashlib.sha256(data).hexdigest())
                self.assertAlmostEqual(result["vertex_diameter_range_mm"][0], diameter)
                self.assertAlmostEqual(result["across_flats_range_mm"][0],
                                       diameter * math.cos(math.pi/96))

    def test_rejects_open_or_reversed_wall_and_extra_cap(self):
        facets = fixture_facets(12)
        interior_cap = ((17, 23, 7.253), (20, 23, 7.253), (17, 26, 7.253))
        for name, wrong in [
            ("wall gap", facets[:-1]), ("reversed wall", facets[:-1] + [facets[-1][::-1]]),
            ("duplicate cap", facets + [facets[0]]), ("thin obstruction", facets + [interior_cap]),
        ]:
            with self.subTest(name=name), self.assertRaises(ValueError):
                verify_bytes(encode(wrong), 12)

    def test_rejects_invalid_input_and_stale_diameter(self):
        for data in (b"", b"solid x\nendsolid x\n", b"solid x\nfacet normal 0 0\n",
                     encode(fixture_facets(10))):
            with self.assertRaises(ValueError):
                verify_bytes(data, 12)
