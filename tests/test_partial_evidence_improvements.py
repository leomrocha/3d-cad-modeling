"""Portable synthetic regressions for partial-work and failed-operation lessons."""
import copy
import hashlib
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from exact_profiles import compare_loops, reversed_edge, signed_extrusion, validate_edge
from source_solid_checks import outward_normal, halfspace_check, convex_cell_check, bilinear_patch_check
from cadtools.captures import verify_capture
from cadtools.verification import owned_audit
from cadtools.runtime import CadError
from component_records import completion_check


def rectangle(x=0,y=0,w=3,h=2):
    pts=[[x,y],[x+w,y],[x+w,y+h],[x,y+h]]
    return {'role':'outer','edges':[dict(kind='Line',start=a,end=b) for a,b in zip(pts,pts[1:]+pts[:1])]}


def cube():
    points=[[x,y,z] for x in (0,1) for y in (0,1) for z in (0,1)];faces=[];halfspaces=[]
    for axis in range(3):
        for level in (0,1):
            ids=[i for i,p in enumerate(points) if p[axis]==level]
            # Order the four corners along the two varying coordinate axes.
            ids=[ids[i] for i in (0,1,3,2)]
            n=[int(i==axis) for i in range(3)];o=[level if i==axis else 0 for i in range(3)]
            edges=[dict(curve_type='straight-curve',endpoints=[points[a],points[b]]) for a,b in zip(ids,ids[1:]+ids[:1])]
            faces.append(dict(surface_type='plane-surface',support=dict(normal=n,origin=o),reversed=level==0,loops=[dict(edges=edges)]))
            halfspaces.append(dict(id=str(axis)+'-'+str(level),normal=n,origin=o,retained_sign=1 if level==0 else -1))
    return dict(points=points,face_boundary_edges=faces,topology=dict(bodies=1,lumps=1,shells=1,reciprocal_closed_partners=True)),halfspaces


class ExactProfiles(unittest.TestCase):
    def compare(self,a,b): return compare_loops(a,b,length_tolerance=1e-8,parameter_tolerance=1e-10)
    def test_cyclic_whole_reversal(self):
        a=rectangle();b=copy.deepcopy(a);b['edges']=[reversed_edge(e) for e in reversed(b['edges'])];b['edges']=b['edges'][2:]+b['edges'][:2]
        self.assertEqual(self.compare([a],[b])['result'],'PASS')
    def nurbs_loop(self):
        e=dict(kind='NURBS',degree=3,control_points=[[0,0],[0,2],[2,2],[2,0]],weights=[1,1,1,1],knots=[3]*4+[7]*4,periodic=False,fit_points=[])
        return dict(role='outer',edges=[e,dict(kind='Line',start=[2,0],end=[0,0])])
    def test_complete_nurbs_reversal_and_parameter_shift(self):
        a=self.nurbs_loop();b=copy.deepcopy(a);b['edges']=[reversed_edge(e) for e in reversed(b['edges'])]
        self.assertEqual(self.compare([a],[b])['result'],'PASS')
    def test_changed_controls_fail_despite_same_endpoints(self):
        a=self.nurbs_loop();b=copy.deepcopy(a);b['edges'][0]['control_points'][1][1]+=0.1
        self.assertEqual(self.compare([a],[b])['result'],'FAIL')
    def test_fit_fallback_and_bad_knots_rejected(self):
        for field,value in [('fit_points',[[0,0]]),('knots',[0,0,0,0,1,1,1]),('periodic',True),('weights',[1,0,1,1])]:
            a=self.nurbs_loop();a['edges'][0][field]=value
            with self.subTest(field=field),self.assertRaises(ValueError): self.compare([a],[a])
    def test_changed_weight_fails(self):
        a=self.nurbs_loop();b=copy.deepcopy(a);b['edges'][0]['weights'][1]=2
        self.assertEqual(self.compare([a],[b])['result'],'FAIL')
    def test_arc_sweep_preserved(self):
        e=dict(kind='Arc',start=[1,0],end=[0,1],center=[0,0],sweep=math.pi/2)
        loop=dict(role='outer',edges=[e,dict(kind='Line',start=[0,1],end=[1,0])]);other=copy.deepcopy(loop);other['edges'][0]['sweep']=-3*math.pi/2
        self.assertEqual(self.compare([loop],[other])['result'],'FAIL')
    def test_open_or_sampled_loop_rejected(self):
        a=rectangle();a['edges'][0]['end']=[2,0]
        with self.assertRaises(ValueError):self.compare([a],[a])
        with self.assertRaises(ValueError):validate_edge({'kind':'Polyline'})
    def test_grouping_roles_and_duplicate_matches(self):
        a,b=rectangle(),rectangle(8)
        self.assertEqual(self.compare([a,b],[b,a])['result'],'PASS')
        self.assertEqual(self.compare([a,a],[a,a])['result'],'FAIL')
        c=copy.deepcopy(a);c['role']='hole';self.assertEqual(self.compare([a],[c])['result'],'FAIL')
    def test_negative_normal_needs_negative_height(self):
        self.assertEqual(signed_extrusion([0,0,-1],[0,0,2],angular_tolerance=1e-10),-2)
        self.assertEqual(signed_extrusion([0,0,1],[0,0,2],angular_tolerance=1e-10),2)
        with self.assertRaises(ValueError):signed_extrusion([0,0,1],[1,0,2],angular_tolerance=1e-10)


class SourceSolids(unittest.TestCase):
    def check_cube(self,f=None,h=None,**kw):
        original,hs=cube();return convex_cell_check(f or original,expected_vertices=original['points'],halfspaces=h or hs,expected_volume=kw.get('volume',1),length_tolerance=1e-8,volume_tolerance=1e-8)
    def test_face_sense_boolean_and_literal(self):
        for sense in (True,'reversed'):self.assertEqual(outward_normal([0,0,2],sense),[0,0,-1])
        for sense in (False,'forward'):self.assertEqual(outward_normal([0,0,2],sense),[0,0,1])
        with self.assertRaises(ValueError):outward_normal([0,0,1],1)
    def test_closed_cube_analytic_volume(self):
        r=self.check_cube();self.assertEqual(r['result'],'PASS');self.assertAlmostEqual(r['analytic_volume'],1)
    def test_reversed_face_normal_fails(self):
        f,h=cube();f['face_boundary_edges'][0]['reversed']=False
        self.assertEqual(self.check_cube(f,h)['result'],'FAIL')
    def test_wrong_halfspace_and_volume_fail(self):
        f,h=cube();h[0]['retained_sign']=-1
        self.assertEqual(self.check_cube(f,h)['result'],'FAIL')
        self.assertEqual(self.check_cube(volume=2)['result'],'FAIL')
    def test_missing_face_fails_closed_boundary(self):
        f,h=cube();f['face_boundary_edges'].pop();self.assertEqual(self.check_cube(f,h)['result'],'FAIL')
    def test_extra_or_curved_faces_rejected(self):
        f,h=cube();f['face_boundary_edges'][0]['loops'].append({'edges':[]})
        with self.assertRaises(ValueError):self.check_cube(f,h)
        f,h=cube();f['face_boundary_edges'][0]['loops'][0]['edges'][0]['curve_type']='ellipse-curve'
        with self.assertRaises(ValueError):self.check_cube(f,h)
    def test_halfspace_normalized_and_crossing(self):
        h=[dict(id='cut',origin=[0,0,0],normal=[0,0,20],retained_sign=1)]
        self.assertEqual(halfspace_check([[0,0,1],[0,0,-1]],h,tolerance=1e-8)['result'],'FAIL')
        h[0]['retained_sign']=True
        with self.assertRaises(ValueError):halfspace_check([[0,0,1]],h,tolerance=1e-8)
    def patch(self,a,b):return bilinear_patch_check(a,b,plane_origin=[0,0,0],plane_normal=[0,0,1],length_tolerance=1e-8,jacobian_tolerance=1e-10)
    def test_ruled_corner_correspondence_and_fold(self):
        a=[[[0,0,0],[0,2,0]],[[3,0,0],[3,2,0]]]
        self.assertEqual(self.patch(a,a)['result'],'PASS')
        b=copy.deepcopy(a);b[1].reverse();self.assertEqual(self.patch(a,b)['result'],'FAIL')
        self.assertEqual(self.patch(b,b)['result'],'FAIL')
    def test_ruled_wrong_support_fails(self):
        a=[[[0,0,0],[0,2,0]],[[3,0,1],[3,2,1]]];self.assertEqual(self.patch(a,a)['result'],'FAIL')


class EvidenceGuards(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def state(self):return dict(ok=True,document_id=7,revision=1,geometry_revision=9,camera_revision=3,documents=[dict(id=7,path='model.dwg')])
    def capture(self):
        from PIL import Image
        p=self.root/'capture.png';Image.new('RGB',(8,6),'white').save(p);s=self.state()
        return p,dict(ok=True,status='completed',state=s,result=dict(document_id=7,revision=1,camera_revision=3,path=str(p),scope='viewport',waited_for_frame=True,width=8,height=6))
    def verify(self,p,r,**kw):return verify_capture(r,self.state(),self.state(),p,expected_document_id=7,expected_model_path='model.dwg',**kw)
    def test_capture_identity_and_stale_image(self):
        p,r=self.capture();result=self.verify(p,r);self.assertEqual(result['result'],'PASS');self.assertEqual(result['pixel_content_review'],'REQUIRED')
        self.assertEqual(self.verify(p,r,previous_sha256=result['sha256'],camera_changed=True)['result'],'FAIL')
    def test_wrong_capture_identity_camera_and_frame_rejected(self):
        for field,value in [('document_id',8),('camera_revision',4),('waited_for_frame',False),('width',9),('revision',2)]:
            p,r=self.capture();r['result'][field]=value
            with self.subTest(field=field),self.assertRaises(CadError):self.verify(p,r)
    def test_capture_state_switch_rejected(self):
        p,r=self.capture();r['state']=dict(self.state(),document_id=8)
        with self.assertRaises(CadError):self.verify(p,r)
    def test_audit_same_counts_wrong_document_rejected(self):
        class Stub:
            document_id=7
            def read(inner,op,**kw):return self.state() if op=='state' else dict(document_id=8,manifest={'by_type':{'3D Solid':1}})
        with self.assertRaises(CadError):owned_audit(Stub())
    def test_audit_wrong_source_hash_rejected(self):
        class Stub:
            document_id=7
            def read(inner,op,**kw):return self.state() if op=='state' else dict(document_id=7,source=dict(path='other.dwg',sha256='b'*64))
        with self.assertRaises(CadError):owned_audit(Stub(),expected_path='model.dwg',expected_sha256='a'*64)
    def completion(self):
        p=self.root/'model.dwg';p.write_bytes(b'synthetic persistence fixture');pin={'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        evidence={k:dict(result='PASS',job_id='fixture',model_sha256=pin['sha256']) for k in ('source_geometry','metadata','persistence','cleanup','reusable_improvement')}
        evidence['reusable_improvement'].update(applied=True,changed_files=[pin],verification=[dict(name='regression',result='PASS')]);return pin,evidence
    def test_completion_requires_applied_verified_improvement(self):
        pin,e=self.completion();self.assertEqual(completion_check('fixture',model=pin,evidence=e)['state'],'DONE')
        e['reusable_improvement']['applied']=False;self.assertEqual(completion_check('fixture',model=pin,evidence=e)['state'],'IN_PROGRESS')
    def test_completion_changed_hash_and_wrong_job_fail(self):
        pin,e=self.completion();e['persistence']['job_id']='other';self.assertEqual(completion_check('fixture',model=pin,evidence=e)['state'],'IN_PROGRESS')
        pin,e=self.completion();Path(pin['path']).write_bytes(b'changed');self.assertEqual(completion_check('fixture',model=pin,evidence=e)['state'],'IN_PROGRESS')

if __name__=='__main__':unittest.main()
