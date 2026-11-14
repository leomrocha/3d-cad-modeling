"""Offline viewport identity and frame checks against retained capture responses."""
from pathlib import Path
from component_records import observe_file
from .records import identity
from .runtime import CadError


def verify_capture(response, before, after, path, *, expected_document_id,
                   expected_model_path, previous_sha256=None, camera_changed=False):
    """Validate capture identity/file; retain stale-image and pixel-review states.

    Caller supplies states taken immediately around capture. A serialized writer
    interval is required for live use. This function sends no native request.
    """
    baseline = identity(before)
    if baseline != identity(after) or baseline[0] != expected_document_id:
        raise CadError('Capture document or geometry/revision changed')
    for state in (before, after, response.get('state', {})):
        docs = [d for d in state['documents'] if d['id'] == expected_document_id]
        if len(docs) != 1 or docs[0].get('path') != str(expected_model_path):
            raise CadError('Capture model path differs')
        if state.get('command') or state.get('modal') or state.get('operation'):
            raise CadError('Capture requires an idle document')
    result = response.get('result', {}); state = response.get('state', {})
    if response.get('ok') is not True or response.get('status') != 'completed':
        raise CadError('Completed capture response required')
    if identity(state) != baseline:
        raise CadError('Capture response document/revision differs')
    camera = before.get('camera_revision')
    if type(camera) is not int or after.get('camera_revision') != camera or state.get('camera_revision') != camera or result.get('camera_revision') != camera:
        raise CadError('Capture camera revision differs')
    target = Path(path)
    if (result.get('document_id') != expected_document_id or result.get('revision') != baseline[1]
            or result.get('path') != str(target) or result.get('scope') != 'viewport'
            or result.get('waited_for_frame') is not True):
        raise CadError('Capture target or rendered frame differs')
    if any(type(result.get(k)) is not int or result[k] <= 0 for k in ('width','height')):
        raise CadError('Positive capture dimensions required')
    pin = observe_file(target)
    from PIL import Image
    with Image.open(target) as image:
        if image.format != 'PNG' or image.size != (result['width'], result['height']):
            raise CadError('Capture image dimensions/format differ')
        image.verify()
    if observe_file(target) != pin: raise CadError('Capture image changed during verification')
    stale = camera_changed and previous_sha256 == pin['sha256']
    return dict(result='FAIL' if stale else 'PASS', sha256=pin['sha256'],
                bytes=pin['bytes'], document_id=baseline[0], revision=baseline[1],
                geometry_revision=baseline[2], camera_revision=camera,
                stale_image_diagnostic='FAIL' if stale else 'UNKNOWN',
                pixel_content_review='REQUIRED', method='bound document, revision, rendered frame and PNG hash')
