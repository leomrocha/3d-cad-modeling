import copy
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from native_views import render_views


class UprightViewTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.edges = [{'points': [[0, 0, 0], [0, 0, 2]], 'endpoints_only': False},
                      {'points': [[2, 0, 0], [0, 2, 0]], 'endpoints_only': True}]

    def render(self, stem, **options):
        return render_views(self.edges, self.root, stem=stem, title='Datum axes', **options)

    def test_optional_upright_view_preserves_existing_projections_and_input(self):
        original = copy.deepcopy(self.edges)
        default = self.render('original')
        extended = self.render('extended', include_top_isometric=True)
        self.assertEqual([r['projection'] for r in default], ['XY', 'XZ', 'YZ', 'isometric'])
        self.assertEqual([r['sha256'] for r in default],
                         [r['sha256'] for r in extended[:4]])
        upright = extended[-1]
        self.assertEqual(upright['projection'], 'top-isometric')
        xml = ET.parse(upright['path'])
        line = xml.find('{*}polyline').attrib['points'].split()
        start, top = [[float(x) for x in pair.split(',')] for pair in line]
        self.assertEqual(start[0], top[0])
        self.assertLess(top[1], start[1])  # positive world Z is upward in the SVG
        x_tip, y_tip = xml.findall('{*}circle')
        self.assertGreater(float(x_tip.get('cx')), start[0])
        self.assertLess(float(y_tip.get('cx')), start[0])
        self.assertEqual(x_tip.get('cy'), y_tip.get('cy'))
        self.assertGreater(float(x_tip.get('cy')), start[1])
        self.assertEqual(self.edges, original)

    def test_preflight_includes_new_target(self):
        target = self.root / 'fixture-top-isometric.svg'
        target.write_bytes(b'original')
        with self.assertRaisesRegex(ValueError, 'Retain existing'):
            self.render('fixture', include_top_isometric=True)
        self.assertEqual(list(self.root.iterdir()), [target])
        self.assertEqual(target.read_bytes(), b'original')
