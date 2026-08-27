---
name: university-form-ppt-skill
description: Identify a university from a school name/email/domain, return verified campus form fields and coordinates, generate a random Chinese-pinyin student name and student ID, and fill the bundled PowerPoint certificate template while preserving the original layout.
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
   - Official English university name. Never invent or self-translate it.
   - Address (single line; no Address line 2).
   - City.
   - State/Province.
   - Postal/Zip code.
   - Latitude and Longitude for the same campus/address.
   - Coordinates should preferably be WGS84. If the source is a China map service using GCJ-02/BD-09, convert or clearly normalize before returning coordinates.
   - Never fabricate an address, postal code, campus, or coordinates.

3. Generate a random student identity for this run.
   - Generate a plausible two- or three-character Chinese name and transliterate it to pinyin/English letters.
   - Follow the user's field convention: First name = surname pinyin; Last name = given-name pinyin.
   - PPT `{{name}}` is the combined form, e.g. `Li Feiyu`.
   - Generate a fresh random numeric student ID for the same run.
   - The student ID length is layout-driven, not fixed. Prefer 7–8 digits.
   - If the first line would wrap, choose a shorter random name first, then a shorter student ID, then render again.
   - Do not infer the student's real identity from a numeric email username.

4. Return fields in this order, each in its own copyable code block:
   - Chinese university name
   - Official English Name
   - First name
   - Last name
   - Student ID
   - Address
   - City
   - State/Province
   - Postal/Zip code
   - Latitude/Longitude last

   Do NOT output these removed fields unless explicitly requested:
   - Country/Region
   - Address line 2
   - VAT/GST ID

5. Generate the PPT when the user-approved template is available.
   - Default template: `assets/certificate_template.pptx`.
   - Always use the latest user-approved template.
   - Replace exactly these placeholders and nothing else:
     - `{{name}}`
     - `{{student_id}}`
     - `{{school_name}}`
   - `{{school_name}}` must use the verified official English university name in both body and bottom-right signature.
   - Preserve all other text, including date, school/department name, program/specialty, `SAMPLE / NOT VALID`, and `仅供演示，不具效力`.

## Strict PPT formatting rules

- Preserve slide size, theme, fonts, font sizes, colors, positions, shapes, line spacing, paragraph spacing, body text-box size/position, and all non-placeholder content.
- Do not rebuild the slide from scratch.
- Prefer raw PPTX XML text replacement so only placeholder text changes.
- The first body line containing name and student ID must remain one line.
  - First try a shorter random name.
  - Then try a shorter student ID.
  - Do not change body font, size, spacing, text-box geometry, or body position to make it fit.
- The body text from the second line onward must read as a normal continuous paragraph.
  - Longer school names may wrap naturally.
  - Do not insert hard line breaks or split words manually.
- The bottom-right official English school name must always remain one line.
  - First preserve the original formatting.
  - If necessary, only this bottom-right school-name area may receive the smallest local adjustment in width, position, character spacing, or font size.
  - Never replace the official full name with an abbreviation.
- Save to a new `.pptx`; never overwrite the user's source template.

## Validation before delivery

Before returning a generated PPT:

1. Confirm placeholder counts in the template: one `{{name}}`, one `{{student_id}}`, and two `{{school_name}}` occurrences.
2. Confirm all placeholders are gone in the output.
3. Confirm no other visible text changed.
4. Render the actual PPT to PNG and visually inspect it. If rendering is unavailable, do not claim visual QA is complete.
5. Confirm the first line, including name and student ID, remains one line.
6. Confirm body text wraps naturally with no replacement-created abrupt isolated line.
7. Confirm the bottom-right official English school name is one line.
8. Confirm `SAMPLE / NOT VALID` and `仅供演示，不具效力` remain visible.
9. If any check fails, regenerate and re-render before delivery.

## Google Drive record archive — mandatory completion gate

Every successful generation MUST be automatically archived to Google Drive. This is not optional and must not wait for a follow-up request.

Permanent root folder:

```text
大学PPT生成记录/<中文学校名>/
```

For every generation, create and upload all three files:

```text
<timestamp>.md
<timestamp>.pptx
<timestamp>.png
```

The record stem must be the local generation date/time precise to one minute, using the filesystem-safe format:

```text
YYYY-MM-DD_HH-mm
```

Example:

```text
2026-08-27_09-37.md
2026-08-27_09-37.pptx
2026-08-27_09-37.png
```

If a second record for the same school is created in the same minute, append `_<student_id>` only to avoid collision.

The PNG must be rendered from the actual generated PPT, never AI-generated.

The Markdown record must contain at least:
- Chinese university name;
- official English full name;
- user's original input;
- First name;
- Last name;
- combined random name;
- Student ID;
- Address;
- City;
- State/Province;
- Postal/Zip code;
- campus name(s);
- coordinates;
- PPT QA result;
- the real Google Drive URL for the uploaded PPT;
- the real Google Drive URL for the uploaded PNG.

### Mandatory archive completion behavior

- The Google Drive archive is a hard completion gate for every generation.
- After the user-facing PNG/PPT and fields are prepared, automatically perform the Drive archive in the same run.
- Do not end the workflow with a normal completion response while Drive archive is still pending.
- Do not ask the user to say “complete it” or otherwise trigger archiving manually.
- A generation is fully complete only after MD, PPTX, and PNG have all uploaded successfully and a Drive folder readback confirms the three expected files are present.
- If any upload or verification fails, explicitly state `该步骤当前没有成功完成。` and do not claim the generation is fully complete.
- Never fabricate Drive URLs, upload success, or readback results.

## Delivery order

When replying after generation:

1. rendered PNG from the actual PPT;
2. PPTX file;
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

The Drive archive must run automatically as part of the same generation workflow and be verified before claiming the run fully complete.

## REDO

If a generated record is later found wrong, perform a full REDO:

regenerate PPT -> render PNG -> visually re-check -> replace/update the Drive PPT -> replace/update the Drive PNG -> update the Drive MD.

Do not leave an incorrect Drive version behind while only fixing the chat artifact.

## Repository role

This GitHub repository stores the Agent/Skill workflow, template, scripts, docs, and tests. It does NOT store per-school generation records; those belong in Google Drive.

## Safety / data integrity

- The bundled template is an explicit demo/non-valid certificate template.
- Preserve `SAMPLE / NOT VALID` and `仅供演示，不具效力` permanently.
- Do not remove, hide, crop, cover, or weaken those markings.

## Rule synchronization invariant

When the user changes this workflow's rules during an interactive conversation, the change is not considered complete until the GitHub repository is updated as applicable.

Update:
- `SKILL.md` first;
- relevant English and Chinese docs;
- related scripts;
- related tests.

If repository write access is unavailable or a write fails, explicitly say the synchronization is incomplete. Never pretend a commit happened.

## Chinese documentation / 中文文档

`SKILL.md` remains the single operational source of truth. Human-readable Simplified Chinese documentation is provided in `README.zh-CN.md` and `docs/*.zh-CN.md`.
