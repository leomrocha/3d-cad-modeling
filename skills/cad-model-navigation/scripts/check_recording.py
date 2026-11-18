"""Decode a constant-frame-rate CAD recording and check its operation chapter times."""
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess


def inspect(movie, chapters):
    probe = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
        "-show_entries", "stream=avg_frame_rate,time_base,duration:frame=best_effort_timestamp",
        "-of", "json", str(movie),
    ])
    media = json.loads(probe)
    stream, = media["streams"]
    interval = 1 / Fraction(stream["avg_frame_rate"])
    tick = Fraction(stream["time_base"])
    frames = media["frames"]
    if interval <= 0 or tick <= 0 or not frames:
        raise ValueError("Expected a positive frame rate and a nonempty video stream")
    previous = int(frames[0]["best_effort_timestamp"])
    for frame in frames[1:]:
        timestamp = int(frame["best_effort_timestamp"])
        if timestamp <= previous or abs((timestamp - previous) * tick - interval) > tick:
            raise ValueError(f"Unexpected frame interval at presentation timestamp {timestamp}")
        previous = timestamp
    duration = float(stream["duration"])
    previous_time = -1
    if not chapters:
        raise ValueError("Expected at least one chapter")
    for chapter in chapters:
        seconds = chapter["seconds"]
        if (not isinstance(chapter["title"], str) or not chapter["title"].strip()
                or type(seconds) not in (int, float) or not math.isfinite(seconds)
                or not 0 <= seconds < duration or seconds <= previous_time):
            raise ValueError(f"Invalid chapter: {chapter!r}")
        previous_time = seconds
    subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(movie),
                    "-map", "0:v:0", "-f", "null", "-"], check=True)
    return dict(result="PASS", frames=len(frames), seconds=duration, chapters=len(chapters))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("movie", type=Path)
    parser.add_argument("receipt", type=Path, help="JSON containing chapters with title and seconds")
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.movie.resolve(), json.loads(args.receipt.read_text())["chapters"])))
    except (ValueError, TypeError, KeyError, ZeroDivisionError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Recording check failed: {error}\n")
