"""Select existing model files and user-supplied inference endpoints."""

import os
from urllib.parse import urlsplit


def offline_model_libraries():
    """Set library offline modes before importing a model or processor."""
    os.environ.update(
        HF_HUB_OFFLINE="1",
        HF_HUB_DISABLE_TELEMETRY="1",
        TRANSFORMERS_OFFLINE="1",
        PIP_NO_INDEX="1",
        UV_OFFLINE="1",
        PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK="True",
    )


def inference_endpoint(endpoint):
    """Accept a user-supplied HTTP(S) destination without embedded credentials."""
    url = urlsplit(endpoint)
    if (
        url.scheme not in ("http", "https")
        or not url.hostname
        or url.username is not None
        or url.password is not None
        or url.fragment
    ):
        raise ValueError(
            "Specify an HTTP(S) inference endpoint without userinfo or fragment"
        )
    return url
