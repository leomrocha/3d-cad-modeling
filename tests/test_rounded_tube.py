import math
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rounded_tube import rounded_profile,verify_features,sat_features,SelectionCheckedClient,inspect


def observations():
    planes=[]
    for axis,positions in [(0,[-20,-17,17,20]),(1,[-20,-17,17,20]),(2,[0,600])]:
        for pos in positions:
            origin=[0,0,0];origin[axis]=pos;normal=[0,0,0];normal[axis]=1
            planes.append(dict(origin=origin,normal=normal))
    return {'planes':planes,'points':[[-20,-20,0],[20,20,600]],
            'cylinders':[dict(origin=[x,y,0],axis=[0,0,1],radius=r)
                         for x in [-14,14] for y in [-14,14] for r in [3,6]]}
P=dict(zip(['section width','section height','wall thickness','cut length','outer corner radius','inner corner radius'],[40,40,3,600,6,3]))

class TubeChecks(unittest.TestCase):
    def test_installed_clear_only_semantics(self):
        class InstalledSelect:
            def mutate(self,label,op,**fields):
                # Recorded installed semantics: clear=True ignores handles.
                return {'state':{'selection':[] if fields.get('clear') else fields['handles']}}
        c=SelectionCheckedClient(InstalledSelect())
        self.assertEqual(c.mutate('pick','select',handles=['7E'],clear=True)['state']['selection'],['7E'])
        self.assertEqual(c.mutate('clear','select',clear=True)['state']['selection'],[])
    def test_selection_mismatch_stops_command(self):
        class BrokenSelect:
            def mutate(self,*args,**fields):return {'state':{'selection':[]}}
        with self.assertRaises(ValueError):SelectionCheckedClient(BrokenSelect()).mutate('pick','select',handles=['7E'])
    def test_reopened_binary_encoding_is_reported(self):
        class BinaryClient:
            def read(self,*args,**kwargs):return {'document_id':71,'revision':0,'geometry_revision':1,'records':[{'properties':{'acis_data':{'sat_data':'','sab_data':[65,67,73,83]}}}]}
        raw,result=inspect(BinaryClient(),'80',{})
        self.assertEqual(result['result'],'UNKNOWN')
        self.assertEqual(result['encoding'],'SAB')
    def test_explicit_arcs(self):
        points,bulges=rounded_profile(40,40,6)
        self.assertEqual(len(points),8)
        self.assertAlmostEqual(4*math.atan(bulges[1]),math.pi/2)
        self.assertEqual(points[0],[-14,-20])
        with self.assertRaises(ValueError):rounded_profile(40,40,20)
    def test_complete_section(self):self.assertEqual(verify_features(observations(),P)['result'],'PASS')
    def test_filled_tube_rejected(self):
        f=observations();f['planes']=[p for p in f['planes'] if all(abs(x)!=17 for x in p['origin'])]
        self.assertEqual(verify_features(f,P)['result'],'FAIL')
    def test_wrong_inner_radius_rejected(self):
        f=observations();f['cylinders'][0]['radius']=4
        self.assertEqual(verify_features(f,P)['result'],'FAIL')
    def test_short_tube_rejected(self):
        f=observations();f['points'][1][2]=260
        self.assertEqual(verify_features(f,P)['result'],'FAIL')
    def test_incomplete_native_record_rejected(self):
        with self.assertRaises(ValueError):sat_features('body foo')
    def test_transform_requires_supported_reader(self):
        with self.assertRaises(ValueError):sat_features('transform foo')

if __name__=='__main__':unittest.main()
