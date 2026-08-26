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

## Long text behavior

- Body school name: must remain inline with the sentence. Do not add a hard line break. Natural text wrapping is acceptable when caused by the existing text box width.
- Bottom-right school name: must remain a single line. If a rendered QA pass shows wrapping, make only the smallest local adjustment necessary to the school-name line. Do not alter unrelated text.

## Safety marks

Never remove, hide, crop, recolor, or obscure:

- `SAMPLE / NOT VALID`
- `仅供演示，不具效力`
