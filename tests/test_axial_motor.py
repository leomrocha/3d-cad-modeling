"""Regression cases for observed motor surface checking and unsafe inputs."""
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from axial_motor import parameters, verify

P={'main case diameter':201,'main case length':107.5,'rear extent':147.5,
   'rear section diameter':164,'pilot diameter':114.3,'pilot projection':3.2,
   'shaft diameter':22.23,'shaft end':47.6,'shaft thread diameter':11.1125,
   'shaft thread depth':30,'keyway width':4.78,'keyway opposite tangent distance':19.58,
   'keyway extent':36,'outer mounting pcd':149.2,'outer mounting diameter':9.525,
   'outer mounting depth':18,'inner mounting pcd':106.4,'inner mounting diameter':7.9375,
   'inner mounting depth':15}

def plane(axis,value):
    o=[0,0,0];n=[0,0,0];o[axis]=value;n[axis]=1
    return {'origin':o,'normal':n}

def cyl(radius,origin=(0,0,0),axis=(0,0,1)):
    return {'origin':list(origin),'axis':list(axis),'radius':radius}

class MotorChecks(unittest.TestCase):
    def setUp(self):
        # Input readiness already has its own source-hash tests. Isolate geometry here.
        self.guard=patch('axial_motor.require_ready');self.guard.start();self.addCleanup(self.guard.stop)
        self.job={'units':'mm','features':[{'name':k,'value':v} for k,v in P.items()],
                  'construction':{'cut_overrun_mm':0.01}}
        self.f={'housing':{'planes':[plane(2,z) for z in [-107.5,-18,-11.8,0,3.2]],
              'cylinders':[cyl(100.5),cyl(57.15)]+
              [cyl(4.7625,(x,y,0)) for x,y in [(74.6,0),(0,74.6),(-74.6,0),(0,-74.6)]]+
              [cyl(3.96875,(x,y,0)) for x,y in [(37.6180807591,37.6180807591),(-37.6180807591,37.6180807591),(-37.6180807591,-37.6180807591),(37.6180807591,-37.6180807591)]]},
              'shaft':{'planes':[plane(2,z) for z in [3.2,17.6,47.6]]+[plane(0,-2.39),plane(0,2.39),plane(1,8.465)],
              'cylinders':[cyl(11.115),cyl(5.55625),cyl(2.39,(0,11.125,13.99),(0,-1,0))]},
              'rear':{'planes':[plane(2,-147.5),plane(2,-107.5)],'cylinders':[cyl(82)],'points':[[82,0,-147.5],[82,0,-107.5]]}}
        # Blind-hole bottom planes retain each hole's actual XY station.
        outer=[(74.6,0),(0,74.6),(-74.6,0),(0,-74.6)]
        inner=[(37.6180807591,37.6180807591),(-37.6180807591,37.6180807591),(-37.6180807591,-37.6180807591),(37.6180807591,-37.6180807591)]
        self.f['housing']['planes']=[plane(2,z) for z in [-107.5,0,3.2]]+[{
            'origin':[x,y,z],'normal':[0,0,1]} for z,points in [(-18,outer),(-11.8,inner)] for x,y in points]
    def test_seam_vertices_do_not_replace_radius_measurement(self):
        self.assertEqual(verify(self.f,self.job)['result'],'PASS')
    def test_missing_hole_fails(self):
        self.f['housing']['cylinders'].pop()
        self.assertEqual(verify(self.f,self.job)['result'],'FAIL')
    def test_wrong_blind_depth_fails(self):
        self.f['housing']['planes'][3]['origin'][2]=-15
        self.assertEqual(verify(self.f,self.job)['result'],'FAIL')
    def test_swapped_mounting_depths_fail(self):
        for v in self.f['housing']['planes']:
            if v['origin'][2]==-18:v['origin'][2]=-11.8
            elif v['origin'][2]==-11.8:v['origin'][2]=-18
        self.assertEqual(verify(self.f,self.job)['result'],'FAIL')
    def test_wrong_keyway_floor_fails(self):
        self.f['shaft']['planes'][-1]=plane(1,8)
        self.assertEqual(verify(self.f,self.job)['result'],'FAIL')
    def test_wrong_rear_diameter_fails_despite_same_seam_vertices(self):
        self.f['rear']['cylinders'][0]['radius']=80
        self.assertEqual(verify(self.f,self.job)['result'],'FAIL')
    def test_invalid_geometry_rejected_before_writes(self):
        for name,value in [('shaft diameter',float('nan')),('shaft thread depth',100),('keyway width',30),('rear extent',100)]:
            j=copy.deepcopy(self.job)
            next(f for f in j['features'] if f['name']==name)['value']=value
            with self.assertRaises(ValueError):parameters(j)
    def test_units_and_overrun_rejected(self):
        self.job['units']='m'
        with self.assertRaises(ValueError):parameters(self.job)
        self.job['units']='mm';self.job['construction']['cut_overrun_mm']=-1
        with self.assertRaises(ValueError):parameters(self.job)

if __name__=='__main__':unittest.main()
