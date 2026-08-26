# University Form + PPT Skill

A Codex/ChatGPT skill for a narrow workflow:

- identify a university from a school name, email address, or domain;
- verify the official English name and primary campus contact data;
- return the user's preferred form fields and campus coordinates;
- generate a random Chinese-pinyin student name and numeric student ID;
- replace only `{{name}}`, `{{student_id}}`, and `{{school_name}}` in the bundled PPT template;
- preserve the template's original visual formatting and demo/non-valid markings.

## Repository layout

- `SKILL.md` — the agent workflow and hard rules.
- `assets/certificate_template.pptx` — current user-approved template.
- `scripts/fill_certificate.py` — conservative PPTX placeholder replacement.
- `scripts/inspect_template.py` — placeholder/layout inspection helper.
- `scripts/random_identity.py` — random pinyin name + student ID helper.
- `data/names.json` — small source list for plausible Chinese names.
- `docs/OUTPUT_SCHEMA.md` — response field contract.
- `docs/PPT_RULES.md` — PPT formatting constraints.
- `docs/RESEARCH_POLICY.md` — school/campus verification policy.
- `tests/test_template.py` — template sanity test.

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

Optionally provide a fixed identity:

```bash
python scripts/fill_certificate.py \
  --school-name "Soochow University" \
  --name "Li Feiyu" \
  --student-id 2023123456 \
  --output output.pptx
```

The script refuses to proceed if the expected placeholder counts are not present.

## Important

The bundled PPT is a demo template and must retain the visible `SAMPLE / NOT VALID` and `仅供演示，不具效力` markings.
