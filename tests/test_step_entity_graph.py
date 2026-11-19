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
