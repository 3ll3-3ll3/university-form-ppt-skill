# AGENTS.md

This repository is a single-purpose university information + PPT + Google Drive archive skill. Follow `SKILL.md` as the operational source of truth.

Key invariants:

- A university name, school email/domain, college name, or clear university clue triggers the full workflow without asking whether to proceed.
- Verify the official Chinese name and the university's own official English full name; never self-translate, abbreviate, or shorten the school name for layout.
- First name = surname pinyin; Last name = given-name pinyin. Do not infer the real student name from an email username.
- Generate a fresh numeric Student ID for each run, normally 7–8 digits, with no fixed prefix unless explicitly requested.
- Use the latest user-approved template at `assets/certificate_template.pptx`.
- Replace only `{{name}}`, `{{student_id}}`, and `{{school_name}}`; the current template contract is 1/1/2 occurrences respectively.
- Do not rebuild the slide or casually reformat it. Preserve body typography, body text-box geometry, background, date, department/specialty, and all non-placeholder content.
- The first line containing name + Student ID must remain one line; solve overflow by choosing a shorter name, then a shorter ID, not by reformatting the body.
- Later body text must flow naturally with no inserted hard line breaks.
- The bottom-right official English school name must stay on one line; only that local area may receive the smallest necessary adjustment.
- If `SAMPLE / NOT VALID` and/or `仅供演示，不具效力` exist in the source template, preserve them visibly.
- Render the actual PPT to PNG and visually inspect it before delivery.
- Chat order: rendered PNG, PPTX, school/form fields, coordinates last; each field goes in its own code block.
- Do not output Country/Region, Address line 2, or VAT/GST ID unless explicitly requested.
- Google Drive archiving is mandatory and automatic for every generation: save MD/PPTX/PNG under `大学PPT生成记录/<中文学校名>/`, use minute-precision `YYYY-MM-DD_HH-mm` stems, then read the folder back to confirm all three files.
- Per-school generation records belong in Google Drive, not GitHub.
- Never claim an external upload, render, GitHub update, commit, or verification succeeded unless it actually did.
