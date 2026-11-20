import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from planar_profiles import bounded_extrusion, revolve_profile_y


class NativeDrawing:
    def __init__(self):
        self.entities = {'stock': '3D Solid'}
        self.events = []

    def read(self, operation, **fields):
        if operation != 'query':
            raise AssertionError(operation)
        return {'entities': [
            {'handle': handle, 'type': kind} for handle, kind in self.entities.items()
        ]}

    def mutate(self, label, operation, **fields):
        self.events.append((label, operation))
        if operation == 'entities_create':
            handle = label
            self.entities[handle] = 'Polyline'
            return {'result': {'handles': [handle]}}
        if operation == 'select':
            return {'state': {'selection': []}}
        if operation == 'run' and fields['cmd'].startswith('PRESSPULL '):
            self.entities['body'] = '3D Solid'
            return {'request_id': 'extrusion'}
        if operation == 'entities_delete':
            for handle in fields['handles']:
                del self.entities[handle]
            return {}
        raise AssertionError(operation)


class BoundedExtrusionCheckpointTests(unittest.TestCase):
    boundaries = [
        {'points': [[0, 0], [5, 0], [5, 5], [0, 5]]},
        {'points': [[2, 2], [2, 3], [3, 3], [3, 2]]},
    ]

    def build(self, drawing, **kwargs):
        return bounded_extrusion(
            drawing, self.boundaries, [1, 1, 0], 3, label='example', **kwargs,
        )

    def test_callback_sees_each_stage_and_only_owned_handles(self):
        drawing = NativeDrawing()
        stages = []

        def checkpoint(stage, handles):
            self.assertEqual(set(handles), drawing.entities.keys() - {'stock'})
            stages.append(stage)

        result = self.build(drawing, checkpoint=checkpoint)
        self.assertEqual(stages, [
            'example-boundary-0', 'example-boundary-1',
            'example-solid', 'example-profiles-cleared',
        ])
        self.assertEqual(result['body'], 'body')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_uncertain_save_stops_before_deleting_profiles(self):
        drawing = NativeDrawing()

        def checkpoint(stage, handles):
            if stage == 'example-solid':
                raise RuntimeError('Save completion unknown')

        with self.assertRaisesRegex(RuntimeError, 'Save completion unknown'):
            self.build(drawing, checkpoint=checkpoint)
        self.assertEqual(len(drawing.entities), 4)
        self.assertNotIn('entities_delete', [operation for _, operation in drawing.events])

    def test_existing_call_without_callback_still_removes_only_owned_profiles(self):
        drawing = NativeDrawing()
        result = self.build(drawing)
        self.assertEqual(result['request_id'], 'extrusion')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

class RevolveDrawing(NativeDrawing):
    def __init__(self, consume):
        super().__init__()
        self.consume = consume

    def mutate(self, label, operation, **fields):
        if operation == 'select':
            self.events.append((label, operation))
            return {'state': {'selection': fields['handles']}}
        if operation == 'run':
            self.events.append((label, operation))
            if fields['cmd'] != 'REVOLVE Y 360':
                raise AssertionError(fields['cmd'])
            self.entities['body'] = '3D Solid'
            if self.consume:
                del self.entities['ring-section-profile']
            return {
                'changes': [{'kind': 'Added', 'handle': 'body'}],
                'request_id': label,
            }
        return super().mutate(label, operation, **fields)


class RevolveProfileCheckpointTests(unittest.TestCase):
    section = [[3, -2], [5, -2], [5, 2], [3, 2]]

    def build(self, drawing, checkpoint):
        return revolve_profile_y(drawing, self.section, label='ring', checkpoint=checkpoint)

    def test_consumed_sketch_checkpoints_only_live_handles(self):
        drawing = RevolveDrawing(consume=True)
        saves = []
        result = self.build(drawing, lambda stage, handles: saves.append((stage, handles)))
        self.assertEqual(saves, [
            ('ring-section', ('ring-section-profile',)), ('ring-solid', ('body',)),
        ])
        self.assertEqual(result['request_id'], 'ring-revolve')
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_retained_sketch_checked_before_owned_cleanup(self):
        drawing = RevolveDrawing(consume=False)
        saves = []
        def checkpoint(stage, handles):
            saves.append(stage)
            self.assertEqual(set(handles), drawing.entities.keys() - {'stock'})
        self.build(drawing, checkpoint)
        self.assertEqual(saves, ['ring-section', 'ring-solid', 'ring-section-cleared'])
        self.assertEqual(drawing.entities, {'stock': '3D Solid', 'body': '3D Solid'})

    def test_failed_solid_save_preserves_owned_sketch(self):
        drawing = RevolveDrawing(consume=False)
        def checkpoint(stage, handles):
            if stage == 'ring-solid':
                raise RuntimeError('Save unknown')
        with self.assertRaisesRegex(RuntimeError, 'Save unknown'):
            self.build(drawing, checkpoint)
        self.assertIn('ring-section-profile', drawing.entities)
        self.assertIn('body', drawing.entities)
        self.assertNotIn('entities_delete', [operation for _, operation in drawing.events])
