# University Information + PPT + Drive Archive Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A single-purpose Codex/ChatGPT workflow that:

- recognizes a university from its Chinese/English name, school email/domain, college name, or another clear clue;
- verifies the official Chinese name, the university's own official English full name, representative campus data, address, postal code, and coordinates;
- generates a short random Chinese-pinyin demo name and a fresh layout-friendly numeric Student ID;
- fills only `{{name}}`, `{{student_id}}`, and `{{school_name}}` in the latest user-approved PPT template;
- protects the source template's layout and non-placeholder content;
- renders the actual PPT to PNG and visually checks the first line, body flow, signature line, and any source-template demo/non-valid markings;
- automatically archives every completed run to Google Drive as MD + PPTX + rendered PNG;
- treats Google Drive upload + folder readback as a mandatory completion gate.

## Repository role

This repository stores only the reusable workflow:

- `SKILL.md` — operational source of truth;
- `AGENTS.md` — concise invariant list;
- `assets/certificate_template.pptx` — latest user-approved template;
- `scripts/` — identity/PPT/archive helpers;
- `docs/` — research, output, PPT, archive, and maintainer rules;
- `tests/` — workflow regression tests.

Per-school generated records do **not** belong in GitHub. They are archived to Google Drive.

## University research

Source priority:

1. official university site;
2. official admissions pages;
3. official international/exchange pages;
4. official contact/information-disclosure pages;
5. reliable maps/geographic databases for coordinates after the campus/address is verified.

Never machine-translate or invent an English university name. The PPT body and bottom-right signature must use the exact same official English full name.

If the school has multiple campuses, return no more than the two most important and representative coordinate pairs, each clearly tied to its campus.

## Random identity

Project-specific field convention:

- `First name` = surname pinyin;
- `Last name` = given-name pinyin;
- PPT name = `SurnamePinyin GivenNamePinyin`.

Prefer short two- or three-character Chinese names. Never infer the real student name from an email username.

Student IDs are fresh numeric values with layout-driven length. Normally use 7–8 digits and no fixed prefix. If the first certificate line wraps, choose a shorter name first, then a shorter Student ID, then render again.

## PPT rules

- Current template contract: one `{{name}}`, one `{{student_id}}`, two `{{school_name}}` placeholders.
- Replace only those placeholders.
- Prefer direct PPTX XML replacement rather than rebuilding text boxes.
- Do not change body font, body size, line spacing, paragraph spacing, body text-box geometry, date, department, specialty, background, or unrelated layout.
- The first name + Student ID line must remain one line.
- Later body text may wrap naturally, but do not insert hard line breaks or hard-split words.
- The bottom-right official English full name must remain one line; only that local signature area may receive the smallest necessary adjustment.
- If `SAMPLE / NOT VALID` and/or `仅供演示，不具效力` exist in the current source template, they must remain visible.

Every output PPT must be rendered to PNG and visually inspected before delivery.

## Chat output order

1. actual PNG rendered from the PPT;
2. PPTX;
3. Chinese university name;
4. Official English Name;
5. First name;
6. Last name;
7. Student ID;
8. Address;
9. City;
10. State/Province;
11. Postal/Zip code;
12. coordinates last.

Each school/form field is returned in its own copyable code block. Country/Region, Address line 2, and VAT/GST ID are omitted unless explicitly requested.

## Google Drive archive

Every generation is automatically archived under:

```text
大学PPT生成记录/<中文学校名>/
```

Each run uses a local timestamp precise to one minute:

```text
YYYY-MM-DD_HH-mm.md
YYYY-MM-DD_HH-mm.pptx
YYYY-MM-DD_HH-mm.png
```

If the same school gets another record in the same minute, append `_<student_id>` only to avoid collision.

The Markdown record stores school/campus fields, generated identity, Student ID, coordinates, QA result, the original user clue, and the **real returned Google Drive URLs** for the PPT and PNG.

### Mandatory completion gate

A run is fully complete only after:

1. final PPTX upload succeeds;
2. final rendered PNG upload succeeds;
3. MD with real Drive URLs uploads successfully;
4. the target school folder is read back and all expected three files are confirmed present.

Archiving must happen automatically in the same workflow and must not wait for the user to ask again. If any external step fails, report `该步骤当前没有成功完成。` and do not claim full completion.

## REDO

If a generated record is wrong, redo the whole chain: regenerate PPT -> render PNG -> visual QA -> replace/update Drive PPTX -> replace/update Drive PNG -> update Drive MD -> Drive readback verification.

## Rule synchronization

Permanent workflow changes from the user must be synchronized to `SKILL.md`, relevant English/Chinese docs, related scripts, related tests, and the latest template when applicable. Never claim synchronization succeeded unless the GitHub writes actually succeeded.
