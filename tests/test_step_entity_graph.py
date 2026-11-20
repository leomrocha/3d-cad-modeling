"""Synthetic Part 21 dependency graphs."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from step_entity_graph import step_entity_graph


def data(rows):
    return 'ISO-10303-21;HEADER;ENDSEC;DATA;' + rows + 'ENDSEC;END-ISO-10303-21;'


class StepGraph(unittest.TestCase):
    def test_renumber_reorder_and_protect_string_comment(self):
        a = data("#8=ITEM('x'' #987; DATA;',(#10,#10)); #10=PAIR(.T.,3.0); #90=UNUSED();")
        b = data("#2=PAIR(.T., 3.0);/*#999;*/ #1=ITEM('x'' #987; DATA;',(#2,#2));")
        left = step_entity_graph(a, [8])
        self.assertEqual(left['source_ids'], [8, 10])
        self.assertEqual(left['ordered_graph_sha256'], step_entity_graph(b.encode(), [1])['ordered_graph_sha256'])

    def test_preserve_order_sharing_cycle_and_numeric_spelling(self):
        def graph(body):
            return step_entity_graph(data(body), [1])['ordered_graph_sha256']
        baseline = graph('#1=A(#2,#2,1.); #2=B(#1);')
        for other in [
            '#1=A(#2,#3,1.); #2=B(#1); #3=B(#1);',
            '#1=A(1.,#2,#2); #2=B(#1);',
            '#1=A(#2,#2,1.0); #2=B(#1);',
            '#1=A(#2,#2,1.); #2=B(#2);',
        ]:
            self.assertNotEqual(baseline, graph(other))

    def test_bad_inputs_fail_explicitly(self):
        for body in ['#1=A(#3);', '#1=A();#1=B();', '#1=(A() B());',
                     '#1=A(#2,); #2=B();', '#1=A(B(1.),2. 3.);',
                     '#1=A(1.;', '#1=A("00FF");', '#1=A();ENDSEC;DATA;#2=B();']:
            with self.subTest(body=body), self.assertRaises(ValueError):
                step_entity_graph(data(body), [1])

    def test_multiple_roots_typed_parameters_and_deep_closure(self):
        rows = ''.join(f'#{i}=A(WRAP((#{i+1},$,*)));' for i in range(1, 1400))
        result = step_entity_graph(data(rows + '#1400=A();'), [1, 1400])
        self.assertEqual(result['source_ids'][:3], [1, 1400, 2])
        self.assertEqual(result['entity_count'], 1400)


class CopySourceAssignments(unittest.TestCase):
    def test_opaque_complex_repeated_cycle_and_protected_literals(self):
        from step_entity_graph import copy_step_closure
        originals = {13: "(A(#4) B('#77; ''#4',/*#19*/#4,1.00D0))", 4: 'C(#13)', 1: 'UNUSED()'}
        result = copy_step_closure(originals, [13, 4], first_id=501)
        self.assertEqual(result['roots'], [501, 502])
        self.assertEqual(result['entities'], {501: "(A(#502) B('#77; ''#4',/*#19*/#502,1.00D0))", 502: 'C(#501)'})
        self.assertEqual(result['source_to_target'], {13: 501, 4: 502})

    def test_nonlocal_and_incomplete_input(self):
        from step_entity_graph import copy_step_closure
        for rhs in ['B(#2)', 'B(#)', 'B(#0)', 'B(1);#2=C()', 'B(@2)', 'B(' + chr(34) + 'ab' + chr(34) + ')']:
            with self.subTest(rhs=rhs), self.assertRaises(ValueError):
                copy_step_closure({1: rhs}, [1], first_id=10)
