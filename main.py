#!/usr/bin/env python3
"""Copy the rendered poster into /output/entry.png (deterministic, stdlib only)."""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing next to main.py")

    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)

    with open(DST, "rb") as fh:
        size = len(fh.read())
    print("wrote %s (%d bytes)" % (DST, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
