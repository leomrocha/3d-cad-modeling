"""Synthetic numerical, topology, DXF preservation and cancellation regressions."""
import copy
import hashlib
import math
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rational_surface import evaluate_rational_surface
from mesh_checks import triangle_mesh_check
from mesh_dxf import declare_mesh_layers,mesh_signature
from insert_recovery import verify_cancelled_insert
from cadtools.runtime import CadError
from step_placements import eye


def plane():
    return dict(control_points=[[[0,0,0],[0,1,0]],[[1,0,0],[1,1,0]]],
                weights=[[1,1],[1,1]],degree_u=1,degree_v=1,
                knots_u=[0,0,1,1],knots_v=[0,0,1,1])


def evaluate(surface,uv=(.25,.5),**kw):
    return evaluate_rational_surface(surface,uv,transform=kw.get('transform',eye()),
        precisions=kw.get('precisions',(65,100)),parameter_bounds=kw.get('parameter_bounds',((0,1),(0,1))))


class RationalSurface(unittest.TestCase):
    def test_plane_endpoints_and_transformed_frame(self):
        for uv in ([0,0],[1,1],[0,1],[1,0],[.25,.5]):
            m=eye();m[2][3]=7
            r=evaluate(plane(),uv,transform=m)
            self.assertEqual(r['result'],'PASS');self.assertEqual(r['point'],[uv[0],uv[1],7])

    def test_cancellation_avoided_by_transform_before_rounding(self):
        s=plane()
        for row in s['control_points']:
            for p in row:p[0]+=2**50
        m=eye();m[0][3]=-2**50
        result=evaluate(s,(2**-20,.5),transform=m)
        self.assertEqual(result['point'],[2**-20,.5,0])
        self.assertEqual(float(2**50+2**-20)-2**50,0)

    def test_rational_weights(self):
        s=plane();s['weights']=[[1,1],[2,2]]
        self.assertAlmostEqual(evaluate(s,(.5,.5))['point'][0],2/3)

    def test_repeated_internal_knot(self):
        s=plane();s.update(control_points=[[[x,0,0],[x,1,0]] for x in [0,.5,.5,1]],weights=[[1,1]]*4,knots_u=[0,0,.5,.5,1,1])
        self.assertEqual(evaluate(s,(.5,.5))['point'],[.5,.5,0])

    def test_precision_disagreement_is_explicit(self):
        s=plane();s['weights']=[[1,1],[2,2]]
        import rational_surface
        actual=rational_surface._basis
        def unstable(knots,degree,x):
            from decimal import getcontext
            indices,weights=actual(knots,degree,x)
            if getcontext().prec==32:weights=[v*2 if i else v for i,v in enumerate(weights)]
            return indices,weights
        with patch.object(rational_surface,'_basis',side_effect=unstable):
            self.assertEqual(evaluate(s,precisions=(32,64))['result'],'PRECISION_DISAGREEMENT')

    def test_extrapolation_requires_explicit_bounds(self):
        with self.assertRaises(ValueError):evaluate(plane(),(1.01,.5))
        r=evaluate(plane(),(1.01,.5),parameter_bounds=((0,1.02),(0,1)))
        self.assertEqual(r['point'],[1.01,.5,0])

    def test_invalid_surface_contracts(self):
        for key,value in [('degree_u',True),('degree_v',2),('knots_u',[0,1,0,1]),('weights',[[0,1],[1,1]]),('control_points',[[[0,0,0]]])]:
            with self.subTest(key=key):
                s=plane();s[key]=value
                with self.assertRaises(ValueError):evaluate(s)
        with self.assertRaises(ValueError):evaluate(plane(),(math.nan,0))
        with self.assertRaises(ValueError):evaluate(plane(),precisions=(65,65))

    def test_does_not_mutate_source(self):
        s=plane();old=copy.deepcopy(s);evaluate(s);self.assertEqual(s,old)


class MeshGate(unittest.TestCase):
    def test_open_mesh_and_required_closure(self):
        p=[[0,0,0],[1,0,0],[0,1,0]];f=[[0,1,2]]
        self.assertEqual(triangle_mesh_check(p,f,minimum_area=0)['result'],'PASS')
        self.assertEqual(triangle_mesh_check(p,f,minimum_area=0,require_closed=True)['result'],'FAIL')

    def test_closed_oriented_tetrahedron(self):
        r=triangle_mesh_check([[0,0,0],[1,0,0],[0,1,0],[0,0,1]],[[0,2,1],[0,1,3],[1,2,3],[2,0,3]],minimum_area=0,require_closed=True)
        self.assertEqual(r['result'],'PASS');self.assertTrue(r['oriented_edge_closed'])

    def test_positive_uv_zero_world_failure(self):
        r=triangle_mesh_check([[0,0,0],[0,0,0],[1,0,0]],[[0,1,2]],minimum_area=0,uv_vertices=[[0,0],[1,0],[0,1]])
        self.assertEqual(r['result'],'FAIL');self.assertEqual(r['positive_uv_zero_3d_triangles'],[0])

    def test_small_positive_area_is_retained_under_caller_criterion(self):
        p=[[0,0,0],[1e-15,0,0],[0,1e-15,0]]
        self.assertEqual(triangle_mesh_check(p,[[0,1,2]],minimum_area=0)['result'],'PASS')
        self.assertEqual(triangle_mesh_check(p,[[0,1,2]],minimum_area=1e-29)['result'],'FAIL')

    def test_duplicate_and_inconsistent_orientation(self):
        p=[[0,0,0],[1,0,0],[0,1,0],[1,1,0]]
        self.assertEqual(triangle_mesh_check(p,[[0,1,2],[2,1,0]],minimum_area=0)['duplicate_triangles'],[1])
        self.assertEqual(triangle_mesh_check(p,[[0,1,2],[1,2,3]],minimum_area=0)['result'],'FAIL')

    def test_negative_uv_and_invalid_indices(self):
        p=[[0,0,0],[1,0,0],[0,1,0]]
        self.assertEqual(triangle_mesh_check(p,[[0,1,2]],minimum_area=0,uv_vertices=[[0,0],[0,1],[1,0]])['result'],'FAIL')
        for face in [[0,1,True],[0,1,3],[0,1]]:
            with self.assertRaises(ValueError):triangle_mesh_check(p,[face],minimum_area=0)


class MeshDerivative(unittest.TestCase):
    def setUp(self):
        import ezdxf
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.source=Path(self.temp.name)/'source.dxf';self.target=Path(self.temp.name)/'target.dxf'
        d=ezdxf.new('R2018');d.units=4;m=d.modelspace().add_mesh(dxfattribs={'layer':'SURFACE','color':3})
        m.dxf.subdivision_levels=0
        with m.edit_data() as data:data.vertices=[[0,0,0],[1,0,0],[0,1,0]];data.faces=[[0,1,2]]
        d.saveas(self.source)
        self.hash=hashlib.sha256(self.source.read_bytes()).hexdigest()

    def run_derivative(self,**kw):
        return declare_mesh_layers(self.source,self.target,source_sha256=kw.get('sha',self.hash),units_code=kw.get('units',4))

    def test_missing_declaration_preserves_every_entity_tag(self):
        import ezdxf
        old=mesh_signature(ezdxf.readfile(self.source));r=self.run_derivative()
        self.assertEqual(r['layers_added'],['SURFACE']);self.assertEqual(r['result'],'PASS')
        self.assertEqual(mesh_signature(ezdxf.readfile(self.target)),old)
        self.assertEqual(hashlib.sha256(self.source.read_bytes()).hexdigest(),self.hash)

    def test_existing_output_is_preserved(self):
        self.target.write_bytes(b'keep')
        with self.assertRaises(ValueError):self.run_derivative()
        self.assertEqual(self.target.read_bytes(),b'keep')

    def test_source_hash_and_unit_mismatches_create_no_output(self):
        for kw in [dict(sha='0'*64),dict(units=1)]:
            with self.assertRaises(ValueError):self.run_derivative(**kw)
            self.assertFalse(self.target.exists())

    def test_changed_readback_is_rejected(self):
        import mesh_dxf
        actual=mesh_dxf.mesh_signature
        count=0
        def changed(d):
            nonlocal count
            count+=1
            return actual(d) if count==1 else []
        with patch.object(mesh_dxf,'mesh_signature',side_effect=changed):
            with self.assertRaises(ValueError):self.run_derivative()
        self.assertFalse(self.target.exists())

    def test_source_change_during_write_is_rejected(self):
        import ezdxf.document
        actual=ezdxf.document.Drawing.saveas
        def write(d,path,*a,**kw):
            actual(d,path,*a,**kw);self.source.write_bytes(b'changed by another writer')
        with patch.object(ezdxf.document.Drawing,'saveas',write):
            with self.assertRaises(ValueError):self.run_derivative()
        self.assertFalse(self.target.exists())

    def test_extra_entity_or_populated_block_is_rejected(self):
        import ezdxf
        for kind in ('line','block'):
            d=ezdxf.readfile(self.source)
            if kind=='line':d.modelspace().add_line((0,0),(1,1))
            else:d.blocks.new('PART').add_line((0,0),(1,1))
            d.saveas(self.source);self.hash=hashlib.sha256(self.source.read_bytes()).hexdigest()
            with self.assertRaises(ValueError):self.run_derivative()
            self.assertFalse(self.target.exists())


class CancelledInsert(unittest.TestCase):
    def setUp(self):
        self.before=dict(ok=True,document_id=9,revision=3,geometry_revision=4,command={'name':'-INSERT'},modal=None,operation=None)
        self.after=dict(self.before,command=None)
        self.response=dict(ok=True,status='cancelled',request_id='job:cancel',state=self.after)
        self.snapshots=dict(roots=[{'handle':'A','value':1}],inserts=[{'handle':'A','value':1}],blocks=[{'handle':'B','value':2}])

    def check(self,**kw):
        return verify_cancelled_insert(self.before,kw.get('after',self.after),kw.get('response',self.response),expected_request_id='job:cancel',before_snapshots=self.snapshots,after_snapshots=kw.get('snapshots',self.snapshots))

    def test_successful_recorded_cancel(self):self.assertEqual(self.check()['result'],'PASS')

    def test_terminal_status_and_request_identity(self):
        for values in [dict(status='accepted'),dict(ok=False),dict(request_id='different')]:
            with self.assertRaises(CadError):self.check(response=dict(self.response,**values))

    def test_cancel_that_leaves_prompt_is_rejected(self):
        with self.assertRaises(CadError):self.check(after=self.before)

    def test_changed_epoch_or_records_is_rejected(self):
        with self.assertRaises(CadError):self.check(after=dict(self.after,geometry_revision=5))
        new=copy.deepcopy(self.snapshots);new['blocks'][0]['value']=3
        with self.assertRaises(CadError):self.check(snapshots=new)

    def test_session_change_is_rejected(self):
        self.before['session_id']='original'
        with self.assertRaises(CadError):self.check(after=dict(self.after,session_id='different'))

    def test_missing_or_duplicate_snapshot_coverage(self):
        for change in ('missing','duplicate'):
            new=copy.deepcopy(self.snapshots)
            if change=='missing':new.pop('blocks')
            else:new['roots']*=2
            with self.assertRaises(CadError):self.check(snapshots=new)


if __name__=='__main__':unittest.main()
