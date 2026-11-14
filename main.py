"""Food-picture entry: emit the staged ramen photograph.

The repository ships one finished picture, entry.png (JPEG bytes,
1024x1024). This program's only job is to place an exact copy of it at
the path the grader reads, $MAKEFUN_OUTPUT_DIR/entry.png, and to refuse
to run if the picture is missing, oversized, or not a real JPEG.

Standard library only. No network, no randomness, no arguments: run it
twice and the two outputs are byte-identical.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
MAX_BYTES = 1024 * 1024
JPEG_START = b"\xff\xd8\xff"
JPEG_END = b"\xff\xd9"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_source():
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        fail(f"bundled picture {SOURCE_NAME} not found next to main.py")
    blob = source.read_bytes()
    if len(blob) > MAX_BYTES:
        fail(f"picture is {len(blob)} bytes, over the {MAX_BYTES} cap")
    if len(blob) < 4 or blob[:3] != JPEG_START or blob[-2:] != JPEG_END:
        fail("picture does not start with the JPEG magic and end with FF D9")
    return blob


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    blob = read_source()
    with open(target, "wb") as handle:
        handle.write(blob)

    copied = target.read_bytes()
    if len(copied) != len(blob):
        fail(f"written copy is {len(copied)} bytes, expected {len(blob)}")
    if hashlib.sha256(copied).hexdigest() != hashlib.sha256(blob).hexdigest():
        fail("written copy does not match the bundled picture")

    print(f"wrote {target} ({len(copied)} bytes, sha256 "
          f"{hashlib.sha256(copied).hexdigest()[:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
