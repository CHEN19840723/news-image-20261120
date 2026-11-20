#!/usr/bin/env python3
"""news-image-20261120 entry (Python 3.13, standard library only).

The image is entry.png beside this file; the program copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when run outside the grader).
Deterministic: the same input bytes are copied on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print(f"error: {src} is missing", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy: a failed or partial copy must fail loudly,
    # never silently ship a broken entry.
    if not os.path.isfile(dst) or os.path.getsize(dst) != os.path.getsize(src):
        print(f"error: copy to {dst} is incomplete", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
