# PPT rules

## Allowed replacements

Only these three placeholders may change:

- `{{name}}`
- `{{student_id}}`
- `{{school_name}}`

`{{school_name}}` occurs twice: once in the body and once in the bottom-right signature area.

## Visual invariants

Do not change the slide size, background, theme, shapes, text positions, body copy, date, department, specialty, colors, or demo/non-valid notices.

The primary implementation uses direct replacement inside PPTX slide XML instead of reconstructing text boxes. This minimizes formatting drift.

## First-line fit

The first body line containing the random name and `student ID` must stay on one line.

- Automatically generated student IDs are layout-driven rather than fixed-length.
- Prefer an 8-digit numeric ID by default.
- A 9-digit ID is acceptable only when rendered QA confirms the first line still fits.
- If the first line wraps, first choose a shorter student ID and/or shorter pinyin name.
- Do not let the student ID become an isolated second line.
- Typography changes are a last resort and must be minimal/local.

## Body-flow behavior

From the second body line onward, the certificate must look like a normal continuous paragraph.

- Replacement text must remain inline with the surrounding sentence.
- Do not add hard line breaks before or after a placeholder replacement.
- Longer text should push following words forward naturally through normal wrapping.
- Do not create an obviously isolated field or adjacent word on its own line because of replacement logic.
- Prefer selecting a shorter random identity before making any local spacing/text-box adjustment.

## Bottom-right school name

The bottom-right school name must remain a single line. If a rendered QA pass shows wrapping, make only the smallest local adjustment necessary to the school-name line. Do not alter unrelated text.

## Required rendered QA

Before delivery, render and visually inspect the slide.

Confirm all three:

1. the first line, including the student ID, stays on one line;
2. the remaining body text wraps naturally without abrupt isolated lines introduced by replacement;
3. the bottom-right school name stays on one line.

If any check fails, regenerate with a shorter identity and/or make the smallest permitted local adjustment, then render again.

## Safety marks

Never remove, hide, crop, recolor, or obscure:

- `SAMPLE / NOT VALID`
- `仅供演示，不具效力`
