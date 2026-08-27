#!/usr/bin/env python3
"""Inspect the approved PPTX template without modifying it."""
from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path

TOKENS = ("{{name}}", "{{student_id}}", "{{school_name}}")
MARKINGS = ("SAMPLE / NOT VALID", "仅供演示，不具效力")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    args = parser.parse_args()

    counts = {t: 0 for t in TOKENS}
    all_xml_parts: list[str] = []
    with zipfile.ZipFile(args.pptx, "r") as zf:
        for info in zf.infolist():
            if info.filename.endswith(".xml"):
                text = zf.read(info.filename).decode("utf-8", errors="ignore")
                all_xml_parts.append(text)
                if info.filename.startswith("ppt/slides/slide"):
                    for token in TOKENS:
                        counts[token] += text.count(token)

    all_xml = "\n".join(all_xml_parts)
    print(f"sha256: {hashlib.sha256(args.pptx.read_bytes()).hexdigest()}")
    for token, count in counts.items():
        print(f"{token}: {count}")
    for marking in MARKINGS:
        print(f"marking_present[{marking!r}]: {marking in all_xml}")


if __name__ == "__main__":
    main()
