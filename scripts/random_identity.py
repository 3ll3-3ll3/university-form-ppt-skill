#!/usr/bin/env python3
"""Generate a random Chinese-pinyin demo identity for the certificate workflow."""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES_PATH = ROOT / "data" / "names.json"


def generate_identity(seed: int | None = None, id_prefix: str = "2023") -> dict[str, str]:
    rng = random.Random(seed)
    data = json.loads(NAMES_PATH.read_text(encoding="utf-8"))
    surname = rng.choice(data["surnames"])
    given = rng.choice(data["given_names"])
    tail_len = max(1, 10 - len(id_prefix))
    tail = "".join(str(rng.randrange(10)) for _ in range(tail_len))
    student_id = (id_prefix + tail)[:10]
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
    args = parser.parse_args()
    print(json.dumps(generate_identity(args.seed, args.id_prefix), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
