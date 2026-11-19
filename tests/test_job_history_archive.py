import bz2
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import job_history_archive as history


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.source = self.root / 'revision'
        self.source.mkdir()
        self.output = self.root / 'job-r1.tar.bz2'

    def create(self):
        return history.create(self.source, self.output, 'part', 'r1')

    def test_preserves_verbatim_nested_history_and_reports_identity(self):
        records = {'a/jobs.json': b'{}\n', 'b/jobs.json': b'bad raw json',
                   'nested/journal.jsonl': b'{}\n{}\n',
                   'debug.bin': bytes(range(256)) * 12000, 'empty.log': b''}
        for name, data in records.items():
            path = self.source / name
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(data)
        manifest = self.create()
        self.assertEqual(manifest, history.inventory(self.output))
        self.assertEqual((manifest['job'], manifest['revision']), ('part', 'r1'))
        self.assertEqual(manifest['files'], [
            {'path': name, 'size': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
            for name, data in sorted(records.items())])
        for name, data in records.items():
            self.assertEqual((self.source / name).read_bytes(), data)
        self.assertEqual(set(self.root.iterdir()), {self.output, self.source})

    def test_preserves_existing_archive_on_retry(self):
        (self.source / 'a').write_bytes(b'old')
        self.create()
        before = self.output.read_bytes()
        (self.source / 'a').write_bytes(b'new')
        with self.assertRaises(FileExistsError):
            self.create()
        self.assertEqual(self.output.read_bytes(), before)

    def test_empty_history_links_and_recursive_destination(self):
        with self.assertRaisesRegex(ValueError, 'Empty'):
            self.create()
        (self.source / 'symlink').symlink_to(self.root)
        with self.assertRaisesRegex(ValueError, 'regular file'):
            self.create()
        with self.assertRaisesRegex(ValueError, 'outside'):
            history.create(self.source, self.source / 'job.tar.bz2', 'job', 'r')
        self.assertFalse(self.output.exists())

    def test_changed_inputs_block_publication(self):
        path = self.source / 'steps'
        path.write_text('initial')
        original = history.inventory
        def change_inputs(archive):
            path.write_text('updated')
            return original(archive)
        with patch.object(history, 'inventory', side_effect=change_inputs):
            with self.assertRaisesRegex(ValueError, 'changed'):
                self.create()
        self.assertEqual(set(self.root.iterdir()), {self.source})

    def test_bzip_trailer_and_tar_end_marker(self):
        (self.source / 'a').write_bytes(b'x')
        self.create()
        compressed = self.output.read_bytes()
        tar = bz2.decompress(compressed)
        for damaged in (compressed[:-3], compressed + b'junk',
                        bz2.compress(tar[:2048] + b'X' * 512 + bytes(512)),
                        bz2.compress(tar[:2560])):
            with self.subTest(length=len(damaged)):
                self.output.write_bytes(damaged)
                with self.assertRaises((ValueError, OSError, tarfile.TarError)):
                    history.inventory(self.output)

    def test_unsafe_duplicate_link_and_manifest_mismatch(self):
        def member(name, data=b'x', kind=tarfile.REGTYPE):
            entry = tarfile.TarInfo(name)
            entry.type = kind
            entry.size = len(data)
            return entry, io.BytesIO(data)
        bad_manifest = json.dumps({'schema': 1, 'job': 'part', 'revision': 'r1',
                                   'files': [{'path': 'x', 'size': 1, 'sha256': 'wrong'}]}).encode()
        for items, reason in [
            ([member('history/../x')], 'Unsafe'),
            ([member('history/C:/x')], 'Unsafe'),
            ([member('history/x'), member('history/x')], 'Duplicate'),
            ([member('history/x', b'', tarfile.SYMTYPE)], 'Unexpected'),
            ([member('history/x'), member('manifest.json', bad_manifest)], 'Manifest differs'),
        ]:
            with self.subTest(reason=reason):
                with tarfile.open(self.output, 'w:bz2') as archive:
                    for record, data in items:
                        archive.addfile(record, data)
                with self.assertRaisesRegex(ValueError, reason):
                    history.inventory(self.output)
