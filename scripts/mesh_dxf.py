"""Caller-authorized MESH-only DXF layer-declaration derivatives.

No native connection or source modification. Preserve exact exported entity
tags, declared units and version through readback before publishing a new file.
"""
import hashlib
import os
from pathlib import Path
import tempfile


def _sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()


def mesh_signature(document):
    """All model-space MESH tags, including arrays and common properties."""
    from ezdxf.lldxf.tagwriter import TagCollector
    entities=list(document.modelspace())
    if not entities or any(e.dxftype()!='MESH' for e in entities):
        raise ValueError('Nonempty MESH-only model space required')
    if any(len(block) for block in document.blocks if block.name != '*Model_Space'):
        raise ValueError('Additional nonempty blocks/layouts require separate handling')
    return [(e.dxftype(),list(TagCollector.dxftags(e,dxfversion=document.dxfversion))) for e in entities]


def declare_mesh_layers(source,target,*,source_sha256,units_code):
    """Create a distinct DXF derivative after exact source and readback checks.

    Explicit units_code is a DXF INSUNITS integer. Existing destinations are
    preserved. The caller owns target.parent and authorizes this format rewrite.
    """
    import ezdxf
    source=Path(source);target=Path(target)
    if source.resolve()==target.resolve() or target.exists() or target.is_symlink():
        raise ValueError('New distinct derivative path required')
    if source.suffix.lower()!='.dxf' or target.suffix.lower()!='.dxf' or not target.parent.is_dir():
        raise ValueError('DXF source/target and existing caller directory required')
    if type(units_code) is not int or units_code<=0 or units_code>24:
        raise ValueError('Explicit supported non-unitless DXF units code required')
    if _sha(source)!=source_sha256: raise ValueError('Source hash differs')
    doc=ezdxf.readfile(source);before=mesh_signature(doc)
    if doc.units!=units_code: raise ValueError('Source units differ from caller contract')
    used={e.dxf.layer for e in doc.modelspace()}
    missing=sorted(name for name in used if name not in doc.layers)
    for name in missing: doc.layers.add(name)
    fd,name=tempfile.mkstemp(prefix=target.stem+'.',suffix='.dxf',dir=target.parent)
    os.close(fd);temporary=Path(name)
    try:
        doc.saveas(temporary)
        read=ezdxf.readfile(temporary)
        if read.dxfversion!=doc.dxfversion or read.units!=units_code or mesh_signature(read)!=before:
            raise ValueError('Derivative changed entity data, units or format version')
        if any(e.dxf.layer not in read.layers for e in read.modelspace()):
            raise ValueError('Derivative retains undeclared layers')
        if _sha(source)!=source_sha256: raise ValueError('Source changed during derivative creation')
        digest=_sha(temporary)
        with temporary.open('rb') as stream: os.fsync(stream.fileno())
        # Atomic publication refuses a destination concurrently created by others.
        os.link(temporary,target)
        directory=os.open(target.parent,os.O_RDONLY)
        try: os.fsync(directory)
        finally: os.close(directory)
        return dict(result='PASS',source_sha256=source_sha256,target_sha256=digest,
                    units_code=units_code,dxfversion=doc.dxfversion,layers_added=missing,
                    mesh_count=len(before),entity_tags_unchanged=True,source_preserved=True,
                    scope='MESH-only model-space derivative with layer table declarations')
    finally:
        temporary.unlink(missing_ok=True)
