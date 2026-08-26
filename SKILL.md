---
name: university-form-ppt-skill
description: Identify a university from a school name/email/domain, return verified campus form fields and coordinates, generate a random Chinese-pinyin student name and student ID, fill the bundled PowerPoint certificate template while preserving the original layout, and archive each completed generation to Google Drive.
---

# University Form + PPT Certificate Skill

Use this skill when the user sends a university name, school email address/domain, or related school clue and wants the school form fields and/or a PPT certificate generated from the bundled template.

## Core workflow

1. Identify the university from the user's input.
   - For email input, resolve the domain to the institution.
   - Prefer the university's own official website for the institution name and campus address.
   - If the school has multiple campuses and the input does not resolve a campus, choose the current main/primary campus used by the official contact/admissions page and explicitly name that campus.

2. Research and verify the campus data.
   - Official Chinese university name.
   - Official English university name; never invent or self-translate it.
   - Address (single line; no Address line 2).
   - City.
   - State/Province.
   - Postal/Zip code.
   - Latitude and Longitude for the same campus/address.
   - Coordinates should preferably be WGS84. If the source is a China map service using GCJ-02/BD-09, convert or clearly normalize before returning coordinates.
   - Never fabricate an address, postal code, campus, or coordinates.

3. Generate a random student identity for this run.
   - Generate a plausible two- or three-character Chinese name and transliterate it to pinyin/English letters.
   - Follow the user's field convention: First name is the surname pinyin and Last name is the given-name pinyin.
   - Example: `Li` then `Feiyu`.
   - PPT `{{name}}` should be the combined form: `Li Feiyu`.
   - Generate a fresh random numeric student ID for the same run.
   - The student ID length is layout-driven, not fixed. Prefer 7–8 digits by default.
   - If the first line would wrap, first choose a shorter random name, then a shorter student ID. Do not change the body font, size, line spacing, text box, or body position to make the first line fit.
   - Do not infer the student's real identity from a numeric email username.

4. Return the fields in this order, each in its own copyable code block:
   - Chinese university name
   - Official English Name
   - First name
   - Last name
   - Student ID
   - Address
   - City
   - State/Province
   - Postal/Zip code
   - Latitude / Longitude last

   Do NOT output these removed fields unless the user explicitly asks:
   - Country/Region
   - Address line 2
   - VAT/GST ID

5. Generate the PPT when a template is available.
   - Default template: `assets/certificate_template.pptx`.
   - Always use the most recently user-approved template.
   - Replace exactly these placeholders and nothing else:
     - `{{name}}`
     - `{{student_id}}`
     - `{{school_name}}`
   - `{{school_name}}` must use the verified official English university name in both body and bottom-right signature.
   - Preserve all other text, including date, school/department name, program/specialty, `SAMPLE / NOT VALID`, and `仅供演示，不具效力`.

## Strict PPT formatting rules

- Preserve the original slide size, theme, fonts, font sizes, colors, positions, shapes, line spacing, paragraph spacing, and all non-placeholder content.
- Do not rebuild the slide from scratch.
- Prefer raw PPTX XML text replacement so only placeholder text changes.
- The first body line containing `student ID: {{student_id}}` must remain a single line.
  - The automatically generated name and student ID must be chosen to fit that line.
  - Prefer a shorter random identity rather than changing typography.
  - Do not deliver a PPT where the student ID is stranded on a new line.
- The body text from the second line onward must read as a normal continuous paragraph.
  - Longer replacement text may wrap naturally.
  - Do not insert hard line breaks before or after any replacement.
  - Do not hard-split words or force replacement fields onto isolated lines.
- The bottom-right school name must always remain on one line and must remain the full official English name.
  - First try to preserve the original font and position.
  - If it would wrap, make only the smallest local adjustment necessary to that bottom-right school-name line: tiny width/position adjustment and, only if necessary, a tiny font-size reduction.
  - Never shorten or abbreviate the school name to solve layout.
  - Do not change the body or slide's overall layout.
- Save to a new `.pptx`; never overwrite the user's source template.

## Validation before delivery

Before returning a generated PPT:

1. Confirm placeholder counts in the template: one `{{name}}`, one `{{student_id}}`, and two `{{school_name}}` occurrences.
2. Confirm all placeholders are gone in the output.
3. Confirm no other visible text changed.
4. Render the actual PPT slide to PNG and visually inspect it before delivery. If no renderer is available, do not claim visual QA is complete.
5. Confirm the first line, including name and student ID, remains one line.
6. Confirm the body from the second line onward has natural continuous wrapping and no replacement-created abrupt isolated line.
7. Confirm the body school name is the verified official English full name.
8. Confirm the bottom-right school name is the same official English full name and remains one line.
9. Confirm `SAMPLE / NOT VALID` and `仅供演示，不具效力` remain visible and unobstructed.
10. If any check fails, regenerate and render again before delivery.

## Google Drive record archive

Specific generation records are NOT stored in this GitHub repository. This repository stores only the reusable Agent/Skill workflow, documentation, scripts, tests, and current template.

Every successful generation must be automatically archived to Google Drive as part of the same workflow without waiting for a separate user request.

Drive root folder:

```text
大学PPT生成记录
```

School folder:

```text
大学PPT生成记录/<中文学校名>/
```

For each generation, the Markdown, PPTX, and rendered PNG must use the same record stem based on the generation date/time precise to one minute.

Required default stem format:

```text
YYYY-MM-DD_HH-mm
```

Example:

```text
2026-08-27_01-11.md
2026-08-27_01-11.pptx
2026-08-27_01-11.png
```

Use the user's current local/session timezone for the timestamp. The stem is minute-precise; do not use the student ID as the normal filename stem anymore. If a record with the same minute stem already exists for the same school, append `_<student_id>` only to avoid overwriting an existing record.

The PNG must be rendered directly from that generated PPT, never AI-generated.

The Markdown record must contain at least:

- Chinese university name
- official English full name
- user's original input/clue
- First name
- Last name
- full random pinyin name
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- campus name
- coordinates
- generation timestamp/timezone
- PPT visual-QA result

The Markdown footer must store the real Google Drive links returned after upload, including the matching PPT and PNG links. Never invent Drive URLs.

A generation is not considered fully archived until all three files have been uploaded successfully and the destination folder is read back/verified when the connector supports it.

## REDO rule

If the user reports an error in a generated record, perform a full REDO: regenerate PPT -> render PNG -> re-check -> replace the Google Drive PPT -> replace the Google Drive PNG -> update the Markdown record. Do not fix only the chat copy while leaving an incorrect Drive version.

## Delivery order

When replying to the user after generation, provide the actual rendered PPT image first, then the PPTX, then the school fields in the required order, and coordinates last. Google Drive archiving is automatic as the final workflow step and must not require the user to ask again.

## Safety / data integrity

- The bundled template is an explicit demo/non-valid certificate template. Preserve its `SAMPLE / NOT VALID` and `仅供演示，不具效力` markings.
- Do not remove, hide, crop, weaken, or cover those markings.
- Any external action such as rendering, Google Drive upload/replacement, or GitHub update may only be claimed as complete after the action actually succeeds.

## Rule synchronization invariant

When the user changes this workflow's rules during an interactive conversation, the change is not considered complete until the GitHub repository is updated immediately as well.

Update, as applicable:

- `SKILL.md` first;
- relevant English and Chinese documentation;
- implementation scripts;
- tests.

Do not leave a conversation-only rule that contradicts the repository. Specific school-generation records remain in Google Drive, not GitHub.

## Chinese documentation / 中文文档

`SKILL.md` remains the single operational source of truth so duplicated translations do not drift. Human-readable Simplified Chinese documentation is provided in `README.zh-CN.md` and `docs/*.zh-CN.md`.

为避免中英文执行规则长期维护后产生偏差，`SKILL.md` 仍作为唯一正式执行规范。面向人工阅读和维护的简体中文说明见 `README.zh-CN.md` 与 `docs/*.zh-CN.md`。
