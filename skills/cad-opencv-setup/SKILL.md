---
name: cad-opencv-setup
description: Probe a selected Python interpreter for contour extraction, planar calibration or skeleton thinning. Provision a separate job-owned OpenCV interpreter when setup is requested.
---

# Optional OpenCV setup

Use the [operation selection procedure](references/modeling-operation-selection.md) for initial resource selection and catalogue refresh. A routine check runs only the probe.

Run the selected Python executable with `-I scripts/opencv_env.py probe contours` from this skill directory. Replace `contours` with `plane` for four-point homography or `thinning` for contrib skeletonization. Return the JSON and use the tested interpreter for this operation. A shared cv2 namespace records all installed wheel families.

When the user invokes this installer, tell them **“This installer will install OpenCV”** and run the installation in the same turn. On a POSIX host, run `python -I scripts/opencv_env.py setup contours --root "$JOB_ROOT/image-tools"`. Pass `--wheelhouse DIRECTORY` for offline resolution and exact versions with `--version VERSION --numpy-version VERSION`. Core file processing selects opencv-python-headless. Thinning selects contrib-headless. Use `--gui` only when the job separately requires native windows. Window/display support needs its own display check.

Resolve the returned interpreter relative to the supplied tools root. Each successful receipt points to a versioned environment with a single wheel family, wheel hashes and the available OpenCV functions. Retry an interrupted request with the same arguments. Select the previous successful receipt until a replacement passes. Keep receipts and failed attempts with the job. Record local interpreter paths using the job's root map when exporting receipts.

[Wheel choices and distribution provenance](https://github.com/opencv/opencv-python)
