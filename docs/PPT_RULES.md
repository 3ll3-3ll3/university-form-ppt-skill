# PPT rules

## Allowed replacements

Only these three placeholders may change:

- `{{name}}`
- `{{student_id}}`
- `{{school_name}}`

Current template contract:

- one `{{name}}`;
- one `{{student_id}}`;
- two `{{school_name}}` occurrences, one in the body and one in the bottom-right signature area.

Both school-name replacements must use the same verified official English full university name.

## Implementation principle

Prefer direct replacement inside PPTX slide XML. Do not rebuild the slide or recreate text boxes unless there is no other viable way to preserve the template.

## Protected formatting/content

Do not modify, except where explicitly allowed for the bottom-right school-name line:

- slide size;
- background/images;
- theme;
- shapes;
- body font/family;
- body font size;
- body font color;
- body line spacing;
- body paragraph spacing;
- body text-box size;
- body text-box position;
- date;
- department/school/faculty text;
- specialty/program text;
- any other non-placeholder text;
- overall layout.

## First-line fit

The first body line containing the random name and Student ID must remain entirely on one line.

- Generate a fresh numeric Student ID for each run.
- Normally prefer 7–8 digits.
- Do not use a fixed prefix unless explicitly requested.
- If the first line wraps, first choose a shorter random pinyin name.
- If it still wraps, choose a shorter Student ID.
- Render again after every retry.
- Do not solve first-line overflow by altering body typography or body text-box geometry.
- Never deliver a PPT where `student ID:` or the ID value is stranded on a new line.

## Body-flow behavior

From the second line onward, the body must read like a normal continuous English paragraph.

- Replacement text remains inline with the surrounding sentence.
- Longer official school names may wrap naturally.
- Do not insert hard line breaks before or after replacements.
- Do not hard-split words.
- Do not deliberately force a replacement field or adjacent word onto its own line.

## Bottom-right official school name

The bottom-right school name must always use the official English full university name and remain one line.

First preserve the original formatting. If the verified full name cannot stay on one line, only this signature area may receive the smallest necessary local adaptation:

- tiny text-box width increase;
- tiny position adjustment;
- tiny character-spacing adjustment;
- only if necessary, tiny font-size reduction.

Do not alter the body or overall layout, and never replace the full name with an abbreviation.

## Demo/non-valid markings

If the source template contains either or both of:

- `SAMPLE / NOT VALID`;
- `仅供演示，不具效力`;

they must remain visible and must not be removed, hidden, cropped, covered, or weakened to invisibility.

This preservation rule is conditional on the marking being present in the approved source template; do not assume every future template necessarily contains both.

## Required rendered QA

Every generated PPT must be rendered to PNG and visually inspected before delivery. An AI-generated image is not an acceptable preview.

Check all applicable items:

1. name + Student ID remain on the first line;
2. Student ID is not isolated on a new line;
3. later body text flows naturally;
4. body school name is the verified official English full name;
5. bottom-right school name is the same verified official English full name;
6. bottom-right school name remains one line;
7. no unrelated visible text changed;
8. layout/formatting looks normal;
9. `SAMPLE / NOT VALID` remains visible if it existed in the source template;
10. `仅供演示，不具效力` remains visible if it existed in the source template.

If any applicable check fails, fix/regenerate and render again before delivery.

## Output file

Always save a new `.pptx`; never overwrite the user's source template.
