# Template assets

The workflow uses two current user-approved templates.

## Student

Path: `assets/certificate_template.pptx`

Expected SHA-256:
`7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147`

Expected placeholders: one `{{name}}`, one `{{student_id}}`, two `{{school_name}}`.

## Faculty

Path: `assets/teacher_certificate_template.pptx`

Expected SHA-256:
`e2d645a79677ba69a1c648c8e542812c48b30e841af62ce76fec3b5c866b6720`

Expected placeholders: one `{{name}}`, one `{{faculty_id}}`, two `{{school_name}}`.

If either template is replaced by the user, update the matching SHA, scripts/tests, and workflow docs in the same change. Any demo/non-valid markings present in the source template must remain visible.

If the repository binary does not match the expected SHA, template synchronization is incomplete and must not be reported as complete.
