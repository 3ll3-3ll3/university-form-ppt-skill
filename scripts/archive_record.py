#!/usr/bin/env python3
"""Archive one generated university record into records/<中文学校名>/.

This helper copies an already-generated PPTX and its rendered PNG into the
repository and writes a Markdown record whose footer links both artifacts.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", default=".")
    p.add_argument("--school-cn", required=True)
    p.add_argument("--school-en", required=True)
    p.add_argument("--first-name", required=True)
    p.add_argument("--last-name", required=True)
    p.add_argument("--student-id", required=True)
    p.add_argument("--address", required=True)
    p.add_argument("--city", required=True)
    p.add_argument("--province", required=True)
    p.add_argument("--postal-code", required=True)
    p.add_argument("--latitude", required=True)
    p.add_argument("--longitude", required=True)
    p.add_argument("--ppt", required=True)
    p.add_argument("--png", required=True)
    p.add_argument("--campus", default="")
    p.add_argument("--source-clue", default="")
    p.add_argument("--qa", default="第一行单行；正文自然顺排；右下角校名单行")
    args = p.parse_args()

    repo = Path(args.repo_root).resolve()
    folder = repo / "records" / args.school_cn
    folder.mkdir(parents=True, exist_ok=True)
    stem = args.student_id
    ppt_dst = folder / f"{stem}.pptx"
    png_dst = folder / f"{stem}.png"
    md_dst = folder / f"{stem}.md"

    shutil.copy2(args.ppt, ppt_dst)
    shutil.copy2(args.png, png_dst)

    lines = [
        f"# {args.school_cn}生成记录 — {stem}",
        "",
        f"- 中文校名：{args.school_cn}",
        f"- 英文校名：{args.school_en}",
    ]
    if args.campus:
        lines.append(f"- 采用校区：{args.campus}")
    lines += [
        f"- First name：{args.first_name}",
        f"- Last name：{args.last_name}",
        f"- Student ID：{args.student_id}",
        f"- Address：{args.address}",
        f"- City：{args.city}",
        f"- State/Province：{args.province}",
        f"- Postal/Zip code：{args.postal_code}",
        f"- Latitude：{args.latitude}",
        f"- Longitude：{args.longitude}",
    ]
    if args.source_clue:
        lines.append(f"- 来源线索：{args.source_clue}")
    lines += [
        f"- PPT 视觉验收：{args.qa}",
        "",
        "> 注意：必须保留模板中的 `SAMPLE / NOT VALID` 与 `仅供演示，不具效力` 标识。",
        "",
        f"[下载 PPT](./{stem}.pptx)",
        "",
        f"![PPT 预览](./{stem}.png)",
        "",
    ]
    md_dst.write_text("\n".join(lines), encoding="utf-8")
    print(md_dst)


if __name__ == "__main__":
    main()
