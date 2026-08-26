#!/usr/bin/env python3
"""Generate a random Chinese-pinyin demo identity for the certificate workflow."""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES_PATH = ROOT / "data" / "names.json"


def generate_identity(
    seed: int | None = None,
    id_prefix: str = "2023",
    student_id_length: int = 8,
    max_name_chars: int = 12,
) -> dict[str, str]:
    """Generate a layout-friendly random identity.

    The certificate's first line is width-constrained, so the default student ID is
    deliberately 8 digits instead of a fixed 10 digits. The caller may request 9
    digits only after rendered QA confirms the first line still fits.
    """
    if student_id_length < len(id_prefix):
        raise ValueError("student_id_length must be >= len(id_prefix)")
    if student_id_length not in (8, 9):
        raise ValueError("student_id_length must be 8 or 9 for the bundled template")

    rng = random.Random(seed)
    data = json.loads(NAMES_PATH.read_text(encoding="utf-8"))

    candidates = [
        (surname, given)
        for surname in data["surnames"]
        for given in data["given_names"]
        if len(surname["pinyin"]) + 1 + len(given["pinyin"]) <= max_name_chars
    ]
    if not candidates:
        raise ValueError("No pinyin name candidates satisfy max_name_chars")

    surname, given = rng.choice(candidates)
    tail_len = student_id_length - len(id_prefix)
    tail = "".join(str(rng.randrange(10)) for _ in range(tail_len))
    student_id = id_prefix + tail

    return {
        "first_name": surname["pinyin"],
        "last_name": given["pinyin"],
        "name": f"{surname['pinyin']} {given['pinyin']}",
        "student_id": student_id,
        "zh_name": f"{surname['zh']}{given['zh']}",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int)
    parser.add_argument("--id-prefix", default="2023")
    parser.add_argument("--student-id-length", type=int, choices=(8, 9), default=8)
    parser.add_argument("--max-name-chars", type=int, default=12)
    args = parser.parse_args()
    print(
        json.dumps(
            generate_identity(
                args.seed,
                args.id_prefix,
                args.student_id_length,
                args.max_name_chars,
            ),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
