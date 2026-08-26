#!/usr/bin/env python3
"""Fill only the three approved placeholders in the bundled PPTX template.

The implementation edits slide XML text in-place inside the PPTX zip package rather
than rebuilding slides. This intentionally minimizes formatting drift.
"""
from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

from random_identity import generate_identity

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "assets" / "certificate_template.pptx"
EXPECTED = {"{{name}}": 1, "{{student_id}}": 1, "{{school_name}}": 2}


def count_tokens(pptx: Path) -> dict[str, int]:
    counts = {k: 0 for k in EXPECTED}
    with zipfile.ZipFile(pptx, "r") as zf:
        for info in zf.infolist():
            if info.filename.startswith("ppt/slides/slide") and info.filename.endswith(".xml"):
                text = zf.read(info.filename).decode("utf-8")
                for token in counts:
                    counts[token] += text.count(token)
    return counts


def fill(template: Path, output: Path, name: str, student_id: str, school_name: str) -> None:
    counts = count_tokens(template)
    if counts != EXPECTED:
        raise SystemExit(f"Unexpected placeholder counts: {counts}; expected {EXPECTED}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / output.name
        with zipfile.ZipFile(template, "r") as zin, zipfile.ZipFile(tmp, "w") as zout:
            for info in zin.infolist():
                payload = zin.read(info.filename)
                if info.filename.startswith("ppt/slides/slide") and info.filename.endswith(".xml"):
                    text = payload.decode("utf-8")
                    text = text.replace("{{name}}", name)
                    text = text.replace("{{student_id}}", student_id)
                    text = text.replace("{{school_name}}", school_name)
                    payload = text.encode("utf-8")
                # Preserve the original zip entry metadata where possible.
                zout.writestr(info, payload)
        shutil.move(tmp, output)

    remaining = count_tokens(output)
    if any(remaining.values()):
        raise SystemExit(f"Output still contains placeholders: {remaining}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--school-name", required=True)
    parser.add_argument("--name")
    parser.add_argument("--student-id")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--id-prefix", default="2023")
    args = parser.parse_args()

    identity = generate_identity(args.seed, args.id_prefix)
    name = args.name or identity["name"]
    student_id = args.student_id or identity["student_id"]
    fill(args.template, args.output, name, student_id, args.school_name)
    print(f"name={name}")
    print(f"student_id={student_id}")
    print(f"school_name={args.school_name}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
