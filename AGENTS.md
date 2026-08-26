# AGENTS.md

This repository is a single-purpose skill. Follow `SKILL.md` as the source of truth.

Key invariants:

- Keep the bundled PPT's `SAMPLE / NOT VALID` and `仅供演示，不具效力` text visible and unchanged.
- Replace only `{{name}}`, `{{student_id}}`, and `{{school_name}}`.
- Do not rebuild the slide or casually reformat it.
- Bottom-right school name must remain on one line after rendered QA.
- Body replacements must remain inline and must not introduce hard line breaks.
- Do not output Country/Region, Address line 2, or VAT/GST ID unless explicitly requested.
