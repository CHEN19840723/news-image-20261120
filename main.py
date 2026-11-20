#!/usr/bin/env python3
"""news-image-20261120 entry (Python 3.13, standard library only).

The image is entry.png beside this file; the program copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when run outside the grader).
Deterministic: the same input bytes are copied on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
