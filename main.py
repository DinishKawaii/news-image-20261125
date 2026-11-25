#!/usr/bin/env python3
"""Entry point for the 25 Nov 2026 world-news image.

Copies the entry.png shipped beside this file to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only: no network, no dependencies.
"""
import os
import struct
import sys

MAX_BYTES = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(src):
        print(f"missing {src}", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print(f"entry.png too big: {len(data)} bytes", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        print(f"entry.png is {width}x{height}, want 1024x1024",
              file=sys.stderr)
        return 1

    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        if f.read() != data:
            print("output differs from source", file=sys.stderr)
            return 1
    print(f"wrote {dst} ({len(data)} bytes, 1024x1024)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
