import copy,math,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from step_placements import *

S="""ISO-10303-21; HEADER; FILE_SCHEMA(('AUTOMOTIVE_DESIGN')); ENDSEC; DATA;
#1=CARTESIAN_POINT ( 'o', (1771,659,-1.9));
#2=DIRECTION ( '', (1,0,0)); #3=DIRECTION ( '', (0,0,-1));
#4=AXIS2_PLACEMENT_3D ( '', #1,#2,#3);
#5=CARTESIAN_POINT ( '', (0,0,0)); #6=DIRECTION ( '', (0,0,1));
#7=DIRECTION ( '', (1,0,0)); #8=AXIS2_PLACEMENT_3D ( '',#5,#6,#7);
#9=ITEM_DEFINED_TRANSFORMATION ( '','',#4,#8); ENDSEC; END-ISO-10303-21;"""

class PlacementTests(unittest.TestCase):
    def setUp(self):
        self.p={'normal':dict(x=-1,y=0,z=0),'rotation':math.pi/2,'insert_point':dict(x=659,y=-1771,z=1.9),'x_scale':1,'y_scale':1,'z_scale':1,'block_name':'screw'}
        self.r={'handle':'AA','type':'Insert','properties':self.p}
    def test_source_screw_axes_and_position(self):
        m=identity_target_placements(S)[0]['matrix']
        self.assertEqual(apply(m,[0,0,0]),[1771,659,-1.9])
        self.assertEqual(apply(m,[10,0,0]),[1771,659,-11.9])
    def test_reversed_native_placement_detected_and_round_trips(self):
        plan=reversed_placement_plan([self.r],identity_target_placements(S))
        self.assertEqual(plan[0]['source_id'],9)
        fixed=dict(self.p,**plan[0]['fields']);m=native_matrix(fixed)
        self.assertTrue(near(m,identity_target_placements(S)[0]['matrix']))
        self.assertEqual([round(v,6) for v in apply(m,[0,0,0])],[1771,659,-1.9])
    def test_already_correct_placement_is_not_repaired(self):
        self.p.update(native_fields(identity_target_placements(S)[0]['matrix']))
        with self.assertRaises(ValueError):reversed_placement_plan([self.r],identity_target_placements(S))
    def test_ambiguous_source_match_rejected(self):
        p=identity_target_placements(S)
        with self.assertRaisesRegex(ValueError,'Unique'):reversed_placement_plan([self.r],p+p)
    def test_nonidentity_target_rejected(self):
        with self.assertRaisesRegex(ValueError,'Nonidentity'):identity_target_placements(S.replace("'', (0,0,0)","'', (1,0,0)"))
    def test_nonorthogonal_frame_rejected(self):
        with self.assertRaisesRegex(ValueError,'Nonorthogonal'):identity_target_placements(S.replace('(0,0,-1)','(1,0,-1)'))
    def test_source_and_native_input_boundaries(self):
        with self.assertRaises(ValueError):identity_target_placements(S.replace('AUTOMOTIVE_DESIGN','OTHER'))
        self.p['x_scale']=2
        with self.assertRaises(ValueError):native_matrix(self.p)

    def test_source_frame_transfer_preserves_nested_local_matrix(self):
        root = [[0,-1,0,20],[1,0,0,1],[0,0,1,3],[0,0,0,1]]
        local = [[1,0,0,5],[0,0,-1,7],[0,1,0,2],[0,0,0,1]]
        target = [[0,0,1,11],[1,0,0,13],[0,1,0,17],[0,0,0,1]]
        fitted_root = root_for_leaf_placement(root,multiply(root,local),target)
        self.assertTrue(near(multiply(fitted_root,local),target))
        self.assertEqual(apply(multiply(fitted_root,local),[1,2,3]),[14,14,19])
        with self.assertRaisesRegex(ValueError,'Proper unit-rigid'):
            root_for_leaf_placement(root,multiply(root,local),[[-1,0,0,0],*eye()[1:]])


    def test_world_translation_preserves_local_orientation_under_rotated_parent(self):
        parent = [[0,-1,0,20],[1,0,0,1],[0,0,1,3],[0,0,0,1]]
        original = copy.deepcopy(self.p)
        plan = plan_world_insert_translation(self.p,parent,[0,-40,0],
                                             block_base_point=dict(x=0,y=0,z=0))
        self.assertEqual(plan['update']['path'], '/insert_point')
        self.assertEqual(plan['update']['expected'], original['insert_point'])
        self.assertEqual(plan['update']['value'], dict(x=659,y=-1771,z=41.9))
        self.assertEqual(self.p, original)
        updated = dict(self.p, insert_point=plan['update']['value'])
        self.assertTrue(near(multiply(parent,native_matrix(updated)),plan['expected_world']))
        self.assertEqual([row[:3] for row in plan['world_before']],
                         [row[:3] for row in plan['expected_world']])

    def test_world_translation_under_reflected_parent_and_mirrored_insert(self):
        parent = [[-1,0,0,20],[0,1,0,1],[0,0,1,3],[0,0,0,1]]
        self.p['y_scale'] = -1
        plan = plan_world_insert_translation(self.p,parent,[40,0,-5],
                                             block_base_point=dict(x=0,y=0,z=0))
        self.assertEqual(plan['update']['value'], dict(x=659,y=-1776,z=41.9))
        self.assertEqual(classify_hand(plan['expected_world']), 'SOURCE_HAND')

    def test_world_translation_rejects_unsupported_base_frame_and_array(self):
        origin = dict(x=0,y=0,z=0)
        with self.assertRaisesRegex(ValueError,'Zero block base'):
            plan_world_insert_translation(self.p,eye(),[1,2,3],block_base_point=dict(origin,z=1))
        with self.assertRaisesRegex(ValueError,'Finite world displacement'):
            plan_world_insert_translation(self.p,eye(),[1,True,3],block_base_point=origin)
        with self.assertRaisesRegex(ValueError,'Orthonormal'):
            plan_world_insert_translation(self.p,[[2,0,0,0],*eye()[1:]],[1,0,0],block_base_point=origin)
        with self.assertRaisesRegex(ValueError,'Array inserts'):
            plan_world_insert_translation(dict(self.p,column_count=2),eye(),[1,0,0],block_base_point=origin)


class AssemblyTests(unittest.TestCase):
    def fixture(self):
        def insert(h,name,x,y,angle=0):
            return {'handle':h,'type':'Insert','properties':{'block_name':name,'insert_point':dict(x=x,y=y,z=0),'normal':dict(x=0,y=0,z=1),'rotation':angle,'x_scale':1,'y_scale':1,'z_scale':1}}
        rows=[insert('A','assembly',5,0,math.pi/2),insert('B','part',2,0),insert('C','part',0,3),{'handle':'DD','type':'Solid3D'}]
        blocks=[{'name':n,'properties':{'base_point':dict(x=0,y=0,z=0),'entity_handles':hs}} for n,hs in [('assembly',[11,12]),('part',[221])]]
        return rows,blocks
    def test_repeated_solid_keeps_two_paths_and_nested_transforms(self):
        rows,b=self.fixture();out=solid_instances(rows,b,['A'])
        self.assertEqual([v['path'] for v in out],[['A','B','DD'],['A','C','DD']])
        self.assertEqual([[round(x,6) for x in apply(v['matrix'],[0,0,0])] for v in out],[[5,2,0],[2,0,0]])
    def test_cycles_and_instance_bound_fail(self):
        rows,b=self.fixture()
        with self.assertRaisesRegex(ValueError,'bound'):solid_instances(rows,b,['A'],1)
        b[1]['properties']['entity_handles']=[10]
        with self.assertRaisesRegex(ValueError,'Cyclic'):solid_instances(rows,b,['A'])
    def test_nonzero_base_point_requires_explicit_support(self):
        rows,b=self.fixture();b[0]['properties']['base_point']['x']=2
        with self.assertRaisesRegex(ValueError,'base'):solid_instances(rows,b,['A'])

if __name__=='__main__':unittest.main()
