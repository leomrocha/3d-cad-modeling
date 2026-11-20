"""Revision-bound BOM checks for a nested package snapshot."""
from hashlib import sha256
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'scripts'))
from assembly_occurrences import rollup_embedded_parts


def digest(key):
    return sha256(key.encode()).hexdigest()


def reference(key, labels, dependency='embedded'):
    return dict(id=key, revision=1, sha256=digest(key), dependency=dependency, occurrences=labels)


class EmbeddedPartRollup(unittest.TestCase):
    def setUp(self):
        self.records={key:dict(id=key,revision=1) for key in ('root','module','cover','washer')}
        self.records['root']['model_references']=[reference('module',['left','right']),
                                                 reference('cover',['guard'])]
        self.records['module']['model_references']=[reference('washer',['upper','lower'])]
        self.records['cover']['model_references']=[reference('unavailable-tool',['tool'],dependency='derived')]

    def run_check(self, **kwargs):
        return rollup_embedded_parts('root',self.records,asset_sha256=lambda row:digest(row['id']),**kwargs)

    def test_nested_parts_repeat_and_ignore_derived(self):
        result=self.run_check()
        self.assertEqual(result['total_occurrences'],5)
        self.assertEqual({row['id']:row['quantity'] for row in result['quantities']},{'cover':1,'washer':4})

    def test_bytes_and_revision_are_independently_checked(self):
        self.records['module']['model_references'][0]['sha256']=digest('changed')
        with self.assertRaisesRegex(ValueError,'bytes'):
            self.run_check()
        self.records['module']['model_references'][0]['revision']=2
        with self.assertRaisesRegex(ValueError,'revision'):
            self.run_check()

    def test_duplicate_labels_across_distinct_components(self):
        self.records['root']['model_references'][1]['occurrences']=['left']
        with self.assertRaisesRegex(ValueError,'duplicate'):
            self.run_check()

    def test_cycles_fail(self):
        self.records['washer']['model_references']=[reference('root',['cycle'])]
        with self.assertRaisesRegex(ValueError,'Cyclic'):
            self.run_check()

    def test_occurrence_and_depth_bounds(self):
        with self.assertRaisesRegex(ValueError,'Occurrence bound'):
            self.run_check(max_occurrences=4)
        with self.assertRaisesRegex(ValueError,'depth'):
            self.run_check(max_depth=2)
