# University Form + PPT Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A Codex/ChatGPT skill for a narrow workflow:

- identify a university from a school name, email address, or domain;
- verify the official English name and primary campus contact data;
- return the user's preferred form fields and campus coordinates;
- generate a random Chinese-pinyin student name and layout-friendly numeric student ID;
- replace only `{{name}}`, `{{student_id}}`, and `{{school_name}}` in the bundled PPT template;
- preserve the template's original visual formatting and demo/non-valid markings;
- render-check the first line, natural body flow, and bottom-right single-line school name before delivery.

## Repository layout

- `SKILL.md` — the agent workflow and hard rules.
- `assets/certificate_template.pptx` — current user-approved template.
- `scripts/fill_certificate.py` — conservative PPTX placeholder replacement.
- `scripts/inspect_template.py` — placeholder/layout inspection helper.
- `scripts/random_identity.py` — random pinyin name + layout-friendly student ID helper.
- `data/names.json` — small source list for plausible Chinese names.
- `docs/OUTPUT_SCHEMA.md` — response field contract.
- `docs/PPT_RULES.md` — PPT formatting constraints.
- `docs/RESEARCH_POLICY.md` — school/campus verification policy.
- `docs/MAINTAINER_GUIDE.zh-CN.md` — Chinese maintainer guide for the workflow.
- `tests/test_template.py` — template and identity sanity tests.

Chinese documentation is available in `README.zh-CN.md` and the `docs/*.zh-CN.md` files. The executable agent source of truth remains `SKILL.md` to avoid duplicated operational rules drifting apart.

## Install as a Codex skill

Clone/copy this repository into a Codex skills directory, for example on Windows:

```text
C:\Users\<USER>\.codex\skills\university-form-ppt-skill
```

The folder containing `SKILL.md` is the skill root.

## Local PPT generation

Python 3.10+ is sufficient; the core replacement script uses only the standard library.

```bash
python scripts/fill_certificate.py \
  --school-name "Xi'an Polytechnic University" \
  --output output.pptx
```

Automatic identities default to an 8-digit student ID to protect the first-line layout. A 9-digit ID can be requested, but should only be used after rendered QA confirms the first line still fits:

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --student-id-length 9 \
  --output output.pptx
```

You may also provide a fixed identity:

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --name "Li Feiyu" \
  --student-id 20231234 \
  --output output.pptx
```

The script refuses to proceed if the expected placeholder counts are not present.

## Required visual QA

Before a generated PPT is delivered, render and inspect it. Confirm:

1. the first body line, including the student ID, remains a single line;
2. the second line onward reads as a normal continuous paragraph without abrupt isolated lines introduced by replacement;
3. the bottom-right school name remains on one line.

If any check fails, regenerate with a shorter identity and/or make only the smallest permitted local adjustment, then render again.

## Rule synchronization

When the user changes the workflow rules in an interactive conversation, update this repository immediately as part of the same change. `SKILL.md`, relevant English/Chinese docs, scripts, and tests should stay synchronized with the current workflow.

## Important

The bundled PPT is a demo template and must retain the visible `SAMPLE / NOT VALID` and `仅供演示，不具效力` markings.
