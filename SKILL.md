---
name: university-form-ppt-skill
description: Identify a university and certification mode from a school name/email/domain or related clue, verify official school/campus data, generate a short random Chinese-pinyin demo identity, fill the matching latest user-approved student or faculty PPT template, render-check the result, and automatically archive the completed record to the correct Google Drive branch.
---

# University Student/Faculty Certificate + Drive Archive Skill

`SKILL.md` is the operational source of truth for this repository.

## 1. Trigger and automatic execution

When the user provides an obvious university clue, execute the full workflow directly without asking whether to proceed. Inputs may include Chinese/English university names, student or faculty email addresses/domains, college/faculty names, or another clear university clue.

The workflow has two certification modes:

- `student` = 学生认证;
- `faculty` = 教师认证.

Determine the mode from the user's wording and verified role/domain evidence. Obvious student addresses select student mode; obvious faculty/staff/teacher addresses select faculty mode. If the institution is clear but the role genuinely cannot be determined, ask only for the certification mode instead of guessing. Never infer a person's real name from an email username/local-part.

## 2. University research and verification

Verify through official university sources first: official Chinese name, official English full name, representative campus/campuses, Address, City, State/Province, Postal/Zip code, and coordinates. Never self-translate, abbreviate, shorten, or invent the official English name. Use the same verified official English full name in every `{{school_name}}` replacement.

Address and coordinates must correspond to real campuses. Prefer WGS84. For multiple campuses, output at most the two most important/common/representative campuses and label them clearly.

## 3. Random identity and numeric ID

For every run, generate a normal two- or three-character Chinese name, transliterate it to pinyin, and prefer short combinations. Project convention: `First name` = surname pinyin; `Last name` = given-name pinyin; PPT `{{name}}` = combined pinyin name.

Generate a fresh numeric ID, normally 7–8 digits, with no fixed institutional prefix unless explicitly requested. The same value is inserted into `{{student_id}}` in student mode or `{{faculty_id}}` in faculty mode. For compatibility with the established chat/form workflow, the returned field label remains `Student ID` in both modes unless the user explicitly requests `Faculty ID` wording.

If the first line wraps, first regenerate a shorter name, then a shorter numeric ID, then render again. Do not solve first-line overflow by changing body font, body font size, line spacing, body text-box geometry, or body position.

## 4. Student and faculty templates

Use the latest user-approved template for the selected mode:

- student: `assets/certificate_template.pptx`
- faculty: `assets/teacher_certificate_template.pptx`

Expected placeholders:

### Student template
- `{{name}}`: 1
- `{{student_id}}`: 1
- `{{school_name}}`: 2

### Faculty template
- `{{name}}`: 1
- `{{faculty_id}}`: 1
- `{{school_name}}`: 2

Only replace approved placeholders for the selected template. Prefer direct PPTX XML replacement so text boxes are not rebuilt.

## 5. PPT format protection and QA

Student and faculty modes use the same strict formatting rules. Preserve slide size, background/images/shapes/theme, body font/size/color, line and paragraph spacing, body text-box geometry, dates, department/specialty text, all other non-placeholder text, and overall layout. Do not rebuild the slide.

The first line containing name + numeric ID must remain one line. Later body text may wrap naturally; never insert artificial hard line breaks or hard-split words. The bottom-right school-name signature must use the official English full name and stay on one line. If necessary, only that local school-name area may receive the smallest width/position/character-spacing/font-size adjustment. Never abbreviate the official school name.

If the selected source template contains `SAMPLE / NOT VALID`, `仅供演示，不具效力`, or another explicit demo/non-valid marking, preserve it visibly.

Every generated PPT must be actually rendered to PNG before delivery. Check first-line fit, natural body flow, official full school name in body/signature, bottom-right single-line fit, non-placeholder integrity, layout, and preservation of source-template demo markings. Failed checks require regeneration/fix and another render.

## 6. Chat delivery order and field schema

Student and faculty modes use the same user-facing field set and ordering:

1. actual PNG rendered from the PPT;
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

Each form field must be in its own copyable code block. Do not output Country/Region, Address line 2, or VAT/GST ID unless explicitly requested.

## 7. Google Drive archive — mandatory, automatic, separated by mode

Every generation must automatically archive in the same workflow. Do not wait for a second user message.

Permanent paths:

- student: `大学PPT生成记录/学生认证/<中文学校名>/`
- faculty: `大学PPT生成记录/教师认证/<中文学校名>/`

Each run stores exactly three matching files: `<record_stem>.md`, `<record_stem>.pptx`, `<record_stem>.png`. The PNG must be rendered from the actual final PPT.

Use local generation time precise to one minute: `YYYY-MM-DD_HH-mm`. If the same school and certification mode receives another record in the same minute, append `_<student_id>` only to prevent collision.

The MD must contain certification type, template used, Chinese university name, official English full name, user original input, First name, Last name, full random pinyin name, Student ID, Address, City, State/Province, Postal/Zip code, selected campus/campuses, coordinates, PPT QA result, and real Google Drive PPT/PNG URLs. Never fabricate Drive URLs.

Google Drive archiving is a hard completion gate: ensure the correct mode folder and school subfolder exist; upload final PPTX; upload final rendered PNG; create/update MD using real returned PPT/PNG Drive URLs; upload MD; read the target school folder back and confirm the expected trio. Do not consider the run fully complete until all succeed. If any external step fails, explicitly state `该步骤当前没有成功完成。`

## 8. REDO

If any generated record is wrong, perform a complete REDO: PPT regenerate -> PNG render -> visual QA -> replace/update Drive PPTX -> replace/update Drive PNG -> update Drive MD -> Drive readback verification. Do not fix only the chat artifact while leaving an incorrect Drive version behind.

## 9. GitHub repository role and rule synchronization

GitHub stores the reusable workflow, docs, scripts, tests, and latest user-approved student/faculty templates. Per-school records belong only in Google Drive.

When the user permanently changes this workflow, synchronize `SKILL.md`, relevant English/Chinese docs, related scripts, related tests, and whichever template was explicitly replaced. If any required repository update cannot be completed, report the unsynchronized part; never pretend a commit occurred.

## 10. Default end-to-end flow

Identify school -> determine student/faculty mode -> verify official Chinese/English names -> choose representative campus/campuses -> verify address/postal code -> verify coordinates -> generate short random pinyin name -> generate 7–8 digit numeric ID -> select matching latest template -> replace only approved placeholders -> verify first line/body/signature -> render PNG -> visual QA -> prepare chat artifacts/fields -> automatically archive MD/PPTX/PNG to the correct Drive mode folder -> read back Drive folder -> only then claim the run is fully complete.
