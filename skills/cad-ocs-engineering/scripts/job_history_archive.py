"""Create and inspect a verified archive of one frozen CAD job revision."""
import argparse
import bz2
import hashlib
import io
import json
import os
from pathlib import Path, PureWindowsPath
import stat
import tarfile
import tempfile

CHUNK = 1024 * 1024
MANIFEST = 'manifest.json'


def _name(value):
    parts = value.split('/')
    if (any(part in ('', '.', '..') for part in parts) or '\\' in value
            or PureWindowsPath(value).drive or any(ord(ch) < 32 for ch in value)):
        raise ValueError(f'Unsafe relative path: {value!r}')
    return value


def _identity(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 4096:
        raise ValueError('Job and revision must have nonempty labels of at most 4096 characters')
    return value


def _signature(info):
    return (info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def _snapshot(root):
    result = {}
    def visit(directory):
        for path in sorted(directory.iterdir()):
            info = path.lstat()
            if stat.S_ISDIR(info.st_mode):
                visit(path)
            elif stat.S_ISREG(info.st_mode):
                result[_name(path.relative_to(root).as_posix())] = _signature(info)
            else:
                raise ValueError(f'Expected regular file or directory: {path}')
    visit(root)
    if not result:
        raise ValueError('Empty history directory')
    return result


class _HashReader:
    def __init__(self, stream):
        self.stream = stream
        self.digest = hashlib.sha256()

    def read(self, size):
        block = self.stream.read(size)
        self.digest.update(block)
        return block


class _BzipReader(io.RawIOBase):
    """Read one bzip2 stream, validating the trailer and limiting each allocation."""
    def __init__(self, stream):
        self.stream = stream
        self.decoder = bz2.BZ2Decompressor()

    def readable(self):
        return True

    def readinto(self, target):
        size = len(target)
        while not self.decoder.eof:
            block = self.stream.read(65536) if self.decoder.needs_input else b''
            if not block and self.decoder.needs_input:
                raise ValueError('Truncated bzip2 stream')
            result = self.decoder.decompress(block, max_length=size)
            if result:
                target[:len(result)] = result
                return len(result)
        if self.decoder.unused_data or self.stream.read(1):
            raise ValueError('Trailing data after bzip2 stream')
        return 0


class _TarReader:
    def __init__(self, stream):
        self.stream = stream
        self.last_block = None

    def read(self, size):
        block = self.stream.read(size)
        self.last_block = block
        return block


def _row(name, size, digest):
    return {'path': name, 'size': size, 'sha256': digest}


def _write(root, snapshot, job, revision, output):
    rows = []
    with tarfile.open(fileobj=output, mode='w|bz2') as archive:
        for name, signature in sorted(snapshot.items()):
            path = root / name
            with path.open('rb') as source:
                if _signature(os.fstat(source.fileno())) != signature:
                    raise ValueError(f'Source changed: {name}')
                reader = _HashReader(source)
                member = tarfile.TarInfo('history/' + name)
                member.size = signature[2]
                archive.addfile(member, reader)
                rows.append(_row(name, member.size, reader.digest.hexdigest()))
        manifest = {'schema': 1, 'job': job, 'revision': revision, 'files': rows}
        data = json.dumps(manifest, ensure_ascii=True, sort_keys=True).encode()
        member = tarfile.TarInfo(MANIFEST)
        member.size = len(data)
        archive.addfile(member, io.BytesIO(data))
    return manifest


def inventory(path):
    """Return verified paths, sizes, hashes and identity without extracting files."""
    rows = []
    names = set()
    manifest = None
    with Path(path).open('rb') as compressed:
        reader = _TarReader(io.BufferedReader(_BzipReader(compressed), buffer_size=CHUNK))
        # One tar block per refill leaves the second end marker accessible.
        with tarfile.open(fileobj=reader, mode='r|', bufsize=512) as archive:
            for member in archive:
                if manifest is not None or member.type not in (tarfile.REGTYPE, tarfile.AREGTYPE):
                    raise ValueError(f'Unexpected member: {member.name}')
                with archive.extractfile(member) as source:
                    if member.name == MANIFEST:
                        # The expected rows bound manifest size except for its identity labels.
                        size_limit = len(json.dumps(rows, ensure_ascii=True)) + 100000
                        if member.size > size_limit:
                            raise ValueError('Manifest exceeds expected inventory size')
                        manifest = json.load(source)
                        if not isinstance(manifest, dict):
                            raise ValueError('Invalid manifest')
                    else:
                        if not member.name.startswith('history/'):
                            raise ValueError(f'Unexpected member: {member.name}')
                        name = _name(member.name[len('history/'):])
                        if name in names:
                            raise ValueError(f'Duplicate member: {name}')
                        names.add(name)
                        digest = hashlib.sha256()
                        size = 0
                        while block := source.read(CHUNK):
                            digest.update(block)
                            size += len(block)
                        if size != member.size:
                            raise ValueError(f'Size mismatch: {name}')
                        rows.append(_row(name, size, digest.hexdigest()))
            # tarfile accepts a missing/invalid first end block. Its offset
            # points just past the last payload, even on permissive EOF.
            if archive.fileobj.tell() != archive.offset + 512 or reader.last_block != bytes(512):
                raise ValueError('Missing tar end marker')
        padding = 0
        while block := reader.read(CHUNK):
            if any(block):
                raise ValueError('Unexpected data after tar members')
            padding += len(block)
        if padding < 512 or padding % 512:
            raise ValueError('Incomplete tar end padding')
    if not rows or not manifest:
        raise ValueError('Missing history or manifest')
    expected = {'schema': 1, 'job': _identity(manifest.get('job')),
                'revision': _identity(manifest.get('revision')), 'files': rows}
    if json.dumps(manifest, sort_keys=True) != json.dumps(expected, sort_keys=True):
        raise ValueError('Manifest differs from archive inventory')
    return manifest


def create(root, output, job, revision):
    """Archive every regular file in a dedicated source revision, preserving originals."""
    job, revision = _identity(job), _identity(revision)
    root = Path(root).resolve(strict=True)
    output = Path(output)
    if not output.name.endswith('.tar.bz2') or output.resolve().is_relative_to(root):
        raise ValueError('Place the .tar.bz2 archive outside the source directory')
    snapshot = _snapshot(root)
    with tempfile.NamedTemporaryFile(dir=output.parent) as temp:
        manifest = _write(root, snapshot, job, revision, temp)
        temp.flush()
        os.fsync(temp.fileno())
        if inventory(temp.name) != manifest or _snapshot(root) != snapshot:
            raise ValueError('Source or archive changed during creation')
        # Atomic, same-filesystem, exclusive publication, including concurrent retries.
        os.link(temp.name, output)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    build = commands.add_parser('create')
    build.add_argument('source')
    build.add_argument('archive')
    build.add_argument('--job', required=True)
    build.add_argument('--revision', required=True)
    check = commands.add_parser('inventory')
    check.add_argument('archive')
    args = parser.parse_args()
    result = (inventory(args.archive) if args.command == 'inventory'
              else create(args.source, args.archive, args.job, args.revision))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
