"""Independent geometry controls for the new DXF inspection branch."""
import json
from pathlib import Path
import sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from dxf_inspect import inspect,main
try:
    import ezdxf
    from ezdxf.math import Matrix44
except ImportError:ezdxf=None


@unittest.skipUnless(ezdxf,'Requires pinned native-reader ezdxf dependency')
class DrawingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name);self.path=self.root/'drawing.dxf'
    def save(self,doc):doc.saveas(self.path);return self.path
    def test_units_curve_bulges_and_original_bytes_preserved(self):
        doc=ezdxf.new();doc.units=4;doc.modelspace().add_lwpolyline([(0,0,0),(10,0,1),(10,10,0)],format='xyb',close=True)
        self.save(doc);before=self.path.read_bytes();r=inspect(self.path)
        self.assertEqual(r['units']['label'],'mm');self.assertEqual(r['counts']['by_type'],{'LWPOLYLINE':1})
        self.assertTrue(r['entities'][0]['closed']);self.assertEqual(r['entities'][0]['vertices_xy_start_end_width_bulge'][1][-1],1)
        self.assertEqual(before,self.path.read_bytes())
    def test_nested_transform_and_layer_inheritance(self):
        doc=ezdxf.new();doc.layers.new('part');inner=doc.blocks.new('inner');inner.add_line((1,0),(2,0))
        outer=doc.blocks.new('outer');outer.add_blockref('inner',(0,3))
        doc.modelspace().add_blockref('outer',(10,0),dxfattribs={'rotation':90,'xscale':2,'yscale':2,'layer':'part'})
        r=inspect(self.save(doc),layers=['part']);line=next(e for e in r['entities'] if e['type']=='LINE')
        matrix=Matrix44([x for row in line['world_from_block_rows'] for x in row]);point=matrix.transform(line['source_attributes']['start'])
        self.assertAlmostEqual(point.x,4);self.assertAlmostEqual(point.y,2)
        self.assertEqual(line['effective_layer'],'part');self.assertTrue(line['selected']);self.assertEqual(len(line['occurrence_path']),4)
    def test_model_and_paper_spaces_remain_separate(self):
        doc=ezdxf.new();doc.modelspace().add_line((0,0),(1,1));doc.layouts.get('Layout1').add_circle((0,0),2)
        self.save(doc);self.assertEqual(inspect(self.path)['counts']['by_type'],{'LINE':1})
        self.assertEqual(inspect(self.path,space='Layout1')['counts']['by_type'],{'CIRCLE':1})
    def test_unitless_source_and_annotation_roles_are_retained(self):
        doc=ezdxf.new();doc.units=0;doc.modelspace().add_text('dimension note');r=inspect(self.save(doc))
        self.assertEqual(r['units']['state'],'NEEDS_UNIT_EVIDENCE');self.assertEqual(r['entities'][0]['role'],'annotation')
    def test_cyclic_block_is_reported_without_recursion(self):
        doc=ezdxf.new();block=doc.blocks.new('cycle');block.add_blockref('cycle',(0,0));doc.modelspace().add_blockref('cycle',(0,0))
        r=inspect(self.save(doc));self.assertEqual(r['issues'][0]['kind'],'cyclic_block');self.assertEqual(r['counts']['occurrences'],2)
    def test_explicit_limits_and_existing_outputs(self):
        doc=ezdxf.new();doc.modelspace().add_line((0,0),(1,1));doc.modelspace().add_line((1,0),(0,1));self.save(doc)
        with self.assertRaisesRegex(ValueError,'entity limit'):inspect(self.path,max_entities=1)
        with self.assertRaisesRegex(ValueError,'byte limit'):inspect(self.path,max_bytes=1)
        out=self.root/'protected.json';out.write_text('preserved');self.assertEqual(main([str(self.path),'--output',str(out)]),2);self.assertEqual(out.read_text(),'preserved')
    def test_array_occurrences_have_distinct_paths_and_offsets(self):
        doc=ezdxf.new();b=doc.blocks.new('p');b.add_line((0,0),(1,0))
        doc.modelspace().add_blockref('p',(0,0),dxfattribs={'row_count':2,'column_count':2,'row_spacing':3,'column_spacing':5})
        r=inspect(self.save(doc));lines=[e for e in r['entities'] if e['type']=='LINE'];self.assertEqual(len(lines),4)
        self.assertEqual(len({tuple(e['occurrence_path']) for e in lines}),4)
        self.assertEqual(sorted((e['world_from_block_rows'][3][0],e['world_from_block_rows'][3][1]) for e in lines),[(0,0),(0,3),(5,0),(5,3)])
    def test_large_array_stops_before_expansion(self):
        doc=ezdxf.new();b=doc.blocks.new('p');b.add_line((0,0),(1,0))
        doc.modelspace().add_blockref('p',(0,0),dxfattribs={'row_count':200,'column_count':200,'row_spacing':1,'column_spacing':1})
        with self.assertRaisesRegex(ValueError,'array exceeds'):inspect(self.save(doc),max_entities=10)


if __name__=='__main__':unittest.main()
