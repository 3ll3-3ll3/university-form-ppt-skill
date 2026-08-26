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
   - Official English university name.
   - Address (single line; no Address line 2).
   - City.
   - State/Province.
   - Postal/Zip code.
   - Latitude and Longitude for the same campus/address.
   - Coordinates should preferably be WGS84. If the source is a China map service using GCJ-02/BD-09, convert or clearly normalize before returning coordinates.
   - Never fabricate an address, postal code, campus, or coordinates.

3. Generate a random student identity for this run.
   - Generate a plausible two- or three-character Chinese name and transliterate it to pinyin/English letters.
   - Follow the user's field convention: the first returned name field is the surname pinyin and the second returned name field is the given-name pinyin.
   - Example: `Li` then `Feiyu`.
   - PPT `{{name}}` should be the combined form: `Li Feiyu`.
   - Generate a fresh random numeric student ID for the same run. Default to 10 digits unless the user requests another format.
   - Do not infer the student's real identity from a numeric email username.

4. Return only the requested form fields, each in its own copyable code block:
   - First name
   - Last name
   - Address
   - City
   - State/Province
   - Postal/Zip code
   - Latitude
   - Longitude
   - Student ID when a PPT is generated

   Do NOT output these removed fields unless the user explicitly asks:
   - Country/Region
   - Address line 2
   - VAT/GST ID

5. Generate the PPT when a template is available.
   - Default template: `assets/certificate_template.pptx`.
   - Replace exactly these placeholders and nothing else:
     - `{{name}}`
     - `{{student_id}}`
     - `{{school_name}}`
   - `{{school_name}}` must use the verified official English university name.
   - Preserve all other text, including date, school/department name, program/specialty, SAMPLE/NOT VALID marks, and Chinese safety text.

## Strict PPT formatting rules

- Preserve the original slide size, theme, fonts, font sizes, colors, positions, shapes, line spacing, paragraph spacing, and all non-placeholder content.
- Do not rebuild the slide from scratch.
- Prefer raw PPTX XML text replacement so only placeholder text changes.
- The bottom-right school name must always remain on one line.
  - First try to preserve the original font and position.
  - If it would wrap, make the smallest local adjustment necessary to that bottom-right school-name line only (for example reduce leading padding/spacing or slightly reduce that line's font size).
  - Do not change the slide's overall layout.
- In the body paragraph, longer replacement fields must flow naturally inline. Do not insert a hard line break before or after a replacement. Let subsequent text continue naturally.
- Save to a new `.pptx`; never overwrite the user's source template.

## Validation before delivery

Before returning a generated PPT:

1. Confirm placeholder counts in the template: one `{{name}}`, one `{{student_id}}`, and two `{{school_name}}` occurrences.
2. Confirm all placeholders are gone in the output.
3. Confirm no other visible text changed.
4. Render/inspect the slide if a renderer is available.
5. Confirm the bottom-right school name is one line.
6. Confirm the body text did not gain an artificial line break around replacements.
7. Return the generated PPT file and the exact random name/student ID used.

## Safety / data integrity

- The bundled template is an explicit demo/non-valid certificate template. Preserve its `SAMPLE / NOT VALID` and `仅供演示，不具效力` markings.
- Do not remove or hide those markings.

## Chinese documentation / 中文文档

`SKILL.md` remains the single operational source of truth so duplicated translations do not drift. Human-readable Simplified Chinese documentation is provided in `README.zh-CN.md` and `docs/*.zh-CN.md`.

为避免中英文执行规则长期维护后产生偏差，`SKILL.md` 仍作为唯一正式执行规范。面向人工阅读和维护的简体中文说明见 `README.zh-CN.md` 与 `docs/*.zh-CN.md`。
