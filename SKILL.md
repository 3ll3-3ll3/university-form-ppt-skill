---
name: university-form-ppt-skill
description: Identify a university from a school name/email/domain or related clue, verify official school/campus data, generate a short random Chinese-pinyin demo identity, fill only the approved placeholders in the latest user-approved PPT template, render-check the result, and automatically archive the completed record to Google Drive.
---

# University Information + PPT + Drive Archive Skill

`SKILL.md` is the operational source of truth for this repository.

## 1. Trigger and automatic execution

When the user provides any obvious university clue, execute the full workflow directly without asking whether to proceed. Supported clues include:

- Chinese university name;
- English university name;
- school email address;
- school email domain, including a bare domain such as `@stu.scu.edu.cn`;
- college/school/faculty name;
- another clear clue tied to one university.

Do not infer a student's real identity from an email username.

## 2. University research and verification

Identify the institution and verify, in priority order, through:

1. the university's official website;
2. official admissions pages;
3. official international/exchange pages;
4. official contact/information-disclosure pages;
5. reliable map/geographic sources for coordinates after the campus/address has been verified.

Verify:

- official Chinese university name;
- official English full name;
- main/representative campus or campuses;
- Address;
- City;
- State/Province;
- Postal/Zip code;
- campus coordinates.

Never self-translate, abbreviate, shorten, or invent the official English university name. The same verified official English full name must be used in every `{{school_name}}` replacement.

## 3. Campus and coordinate rules

- Address and coordinates must refer to real, corresponding campuses.
- Prefer WGS84 output. Normalize GCJ-02/BD-09 internally when necessary.
- If the university effectively has one relevant campus, output one Latitude/Longitude pair.
- If it has multiple campuses, do not dump every campus. Select at most the two most important, common, and representative campuses and clearly label each coordinate pair with its campus name.
- If one address is used for the form fields, ensure it corresponds to the selected primary campus.
- Never fabricate an address, postal code, campus, or coordinate.

## 4. Random Chinese name

For every run:

- generate a normal two- or three-character Chinese name;
- transliterate it to pinyin;
- prefer shorter combinations to protect the first PPT line;
- use the project-specific field convention:
  - `First name` = surname pinyin;
  - `Last name` = given-name pinyin;
- PPT `{{name}}` = `SurnamePinyin GivenNamePinyin`, e.g. `Li Feiyu`.

Never derive the name from the user's email/local-part.

## 5. Random Student ID

Generate a fresh numeric Student ID for every run.

- Length is layout-driven, not fixed.
- Normally prefer 7–8 digits.
- Do not use a fixed institutional prefix unless the user explicitly requests one.
- The certificate first line must remain completely on one line.
- If it wraps: first regenerate a shorter name, then regenerate a shorter Student ID, then render-check again.
- Do not solve first-line overflow by changing body font, body font size, body line spacing, body text-box geometry, or body position.

## 6. Latest template

Use the latest template that the user explicitly approved. Repository path:

`assets/certificate_template.pptx`

Only replace these placeholders:

- `{{name}}`
- `{{student_id}}`
- `{{school_name}}`

Expected template counts for the current workflow:

- one `{{name}}`;
- one `{{student_id}}`;
- two `{{school_name}}`.

Prefer direct replacement inside PPTX XML so text boxes are not rebuilt.

## 7. PPT format protection

Except for approved placeholder text, preserve the template exactly as far as practical, including:

- slide/page size;
- background and images;
- shapes;
- theme;
- body font, font size, color;
- line spacing and paragraph spacing;
- body text-box size and position;
- date;
- school/department text;
- specialty/program text;
- all other non-placeholder text;
- overall layout.

Do not rebuild the slide from scratch.

## 8. Natural body flow

- The first line containing the name and Student ID must remain a single line.
- From the second line onward, longer text may wrap naturally.
- Never insert artificial hard line breaks before/after a replacement.
- Never hard-split words or deliberately force a replacement field onto its own line.
- Subsequent English text must flow naturally as a normal paragraph.

## 9. Bottom-right school name

The bottom-right school-name signature must:

1. use the official English full university name;
2. remain on one line.

First preserve the original formatting. If the full official name cannot remain on one line, only this bottom-right school-name area may receive the smallest necessary local adaptation, such as:

- a very small text-box width adjustment;
- a very small position adjustment;
- a very small character-spacing adjustment;
- if truly necessary, a very small font-size reduction.

Do not change the body or overall slide layout, and never substitute an abbreviation.

## 10. Demo/non-valid markings

If the current template contains either or both of these markings:

- `SAMPLE / NOT VALID`;
- `仅供演示，不具效力`;

they must remain visible and must not be deleted, hidden, cropped, covered, or weakened to invisibility.

Do not assume a newly approved template necessarily contains them; preservation is conditional on their presence in the source template.

## 11. Required rendering and visual QA

Every generated PPT must be actually rendered to PNG before delivery. AI-generated images are never a substitute for the PPT preview.

Check all applicable items:

1. name + Student ID stay on the first line;
2. Student ID is not stranded on a new line;
3. later body text flows naturally;
4. body school name is the verified official English full name;
5. bottom-right school name is the same verified official English full name;
6. bottom-right school name remains one line;
7. non-placeholder content was not unintentionally changed;
8. layout/formatting remains normal;
9. `SAMPLE / NOT VALID` is preserved if it existed in the source template;
10. `仅供演示，不具效力` is preserved if it existed in the source template.

If any applicable check fails, regenerate/fix and render again before delivery.

## 12. Chat delivery order and field schema

After successful generation, chat delivery order is:

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

Each school/form field must be placed in its own copyable code block.

Do not output these unless explicitly requested:

- Country/Region;
- Address line 2;
- VAT/GST ID.

## 13. Google Drive archive — mandatory and automatic

Every generation must automatically archive the final record to Google Drive in the same workflow. Do not wait for a second user message such as “complete it” or “archive it”.

Permanent root:

`大学PPT生成记录/<中文学校名>/`

Each run stores exactly three matching files:

- `<record_stem>.md`
- `<record_stem>.pptx`
- `<record_stem>.png`

The PNG must be rendered from the actual final PPT.

### Record naming

Use the local generation date/time precise to one minute:

`YYYY-MM-DD_HH-mm`

Example:

- `2026-08-27_09-37.md`
- `2026-08-27_09-37.pptx`
- `2026-08-27_09-37.png`

If the same school receives another record in the same minute, append `_<student_id>` only to prevent collision.

### MD content

The Markdown record must contain at least:

- Chinese university name;
- official English full name;
- user's original input;
- First name;
- Last name;
- full random pinyin name;
- Student ID;
- Address;
- City;
- State/Province;
- Postal/Zip code;
- selected campus/campuses;
- coordinate pair(s);
- PPT QA result;
- real Google Drive PPT URL;
- real Google Drive PNG URL.

Never fabricate or pre-compose Drive URLs.

### Completion gate

Google Drive archiving is a hard completion gate:

- upload final PPTX;
- upload final rendered PNG;
- create/update MD using the real returned PPT/PNG Drive URLs;
- upload MD;
- read the target school folder back and confirm the expected MD/PPTX/PNG files exist.

Do not consider the run fully complete until all of the above have succeeded.

If any external step fails, explicitly state:

`该步骤当前没有成功完成。`

Never claim an upload, deletion, replacement, render, GitHub write, commit, or readback succeeded unless it actually did.

## 14. REDO

If any generated record is wrong (official English name, abbreviation, first-line wrap, body formatting, signature wrap, template version, Drive artifact, etc.), perform a complete REDO:

PPT regenerate -> PNG render -> visual QA -> replace/update Drive PPTX -> replace/update Drive PNG -> update Drive MD -> Drive readback verification.

Do not fix only the chat artifact while leaving an incorrect Drive version behind.

## 15. GitHub repository role

GitHub stores the reusable workflow, not school generation records. Maintain here:

- `SKILL.md`;
- English/Chinese README/docs;
- research/PPT/output/archive rules;
- name and Student ID generation code;
- PPT generation code;
- archive helper code;
- tests;
- latest user-approved template.

Per-school MD/PPTX/PNG records belong only in Google Drive.

## 16. Rule synchronization invariant

When the user says “以后增加规则”, “修改规则”, “记住以后”, or otherwise changes this workflow permanently, treat it as a repository change, not a chat-only preference.

Synchronize, as applicable:

1. `SKILL.md`;
2. relevant English docs;
3. relevant Chinese docs;
4. related scripts;
5. related tests;
6. latest template when the user explicitly replaces it.

If any required repository update cannot be completed, explicitly report the unsynchronized part. Never pretend a commit occurred.

## 17. Default end-to-end flow

Identify school -> verify official Chinese/English names -> choose representative campus/campuses -> verify address/postal code -> verify coordinates -> generate short random pinyin name -> generate 7–8 digit layout-friendly Student ID -> use latest template -> replace only three approved placeholders -> verify first line/body/signature -> render PNG -> visual QA -> prepare chat artifacts/fields -> automatically archive MD/PPTX/PNG to Drive -> read back Drive folder -> only then claim the run is fully complete.