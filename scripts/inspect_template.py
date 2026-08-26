#!/usr/bin/env python3
"""Inspect placeholder counts and basic slide XML text without modifying the PPTX."""
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

TOKENS = ("{{name}}", "{{student_id}}", "{{school_name}}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    args = parser.parse_args()

    counts = {t: 0 for t in TOKENS}
    with zipfile.ZipFile(args.pptx, "r") as zf:
        for info in zf.infolist():
            if info.filename.startswith("ppt/slides/slide") and info.filename.endswith(".xml"):
                text = zf.read(info.filename).decode("utf-8")
                for token in TOKENS:
                    counts[token] += text.count(token)
    for k, v in counts.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
