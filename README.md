# University Form + PPT Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A Codex/ChatGPT skill for a fixed workflow:

- identify a university from a school name, email address, domain, college name, or related clue;
- verify the official Chinese name, official English full name, representative campus data, postal code, and coordinates;
- generate a short random Chinese-pinyin student name and layout-friendly numeric student ID;
- replace only `{{name}}`, `{{student_id}}`, and `{{school_name}}` in the latest user-approved PPT template;
- preserve the original slide formatting and all demo/non-valid markings;
- render the actual PPT to PNG and visually validate it before delivery;
- automatically archive every completed run to Google Drive as MD + PPTX + rendered PNG.

## Repository role

This repository stores the workflow only:

- `SKILL.md` — operational source of truth;
- `assets/certificate_template.pptx` — latest user-approved template;
- `scripts/` — identity, PPT, archive-preparation helpers;
- `docs/` — English/Chinese rules;
- `tests/` — workflow tests.

**Per-school generation records are not stored in GitHub.** They are stored in Google Drive.

## Google Drive archive

Every successful generation must be archived automatically under:

```text
大学PPT生成记录/<中文学校名>/
```

Each run saves exactly three matching files:

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

The timestamp is the local generation date/time precise to one minute. If the same school gets a second record in the same minute, append `_<student_id>` only to avoid collision.

The PNG must be rendered from the actual generated PPT. The MD must contain the school data, generated identity, student ID, campus/coordinates, QA result, and real Google Drive links for the PPT and PNG.

### Mandatory completion gate

Google Drive archiving is **mandatory and automatic**. It must not depend on the user asking again.

A run is fully complete only after:

1. PPTX upload succeeds;
2. rendered PNG upload succeeds;
3. MD upload succeeds;
4. a Drive folder readback confirms all three expected files are present.

If any of those steps fail, the Agent must explicitly report `该步骤当前没有成功完成。` and must not claim that the generation is fully complete.

## PPT rules

- Use the official English full university name; never abbreviate it for layout.
- Keep the first certificate line with name + Student ID on one line by choosing a shorter random name/ID, not by altering body typography.
- Let later body text wrap naturally; never insert artificial line breaks.
- Keep the bottom-right official English school name on one line; only that local area may receive the smallest necessary adaptation.
- Preserve `SAMPLE / NOT VALID` and `仅供演示，不具效力` permanently.

## Delivery order

In chat, provide the rendered PNG first, then PPTX, then the requested school fields, with coordinates last. Google Drive archiving runs automatically as part of the same workflow and must be verified before the run is considered fully complete.

## Rule synchronization

When the user changes the workflow rules, update `SKILL.md`, relevant English/Chinese docs, related scripts, and related tests. Never claim synchronization succeeded unless the GitHub writes actually succeeded.
