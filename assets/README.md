# Template asset

The user-approved template path is:

`assets/certificate_template.pptx`

Latest user-approved source-template SHA-256:

`7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147`

Current template contract:

- one `{{name}}`
- one `{{student_id}}`
- two `{{school_name}}`

## Binary synchronization status

The rules/docs/scripts in this repository target the latest approved template above. If `assets/certificate_template.pptx` still hashes to the legacy value below, the binary replacement itself is pending and must not be falsely reported as synchronized:

`05ff6bcd78cd0b59cc38b7fd6c13550e74543e51be6b48ea339822e1ee0482eb`

`tests/test_template.py` marks that legacy-binary state as an expected pending sync (`xfail`) rather than pretending it is the latest file.

The latest approved source template currently does **not** contain `SAMPLE / NOT VALID` or `仅供演示，不具效力` text in its PPTX XML. The workflow rule is conditional: if a current/future approved source template contains either marking, generated outputs must preserve it visibly and must not delete, hide, crop, cover, or weaken it.

When the user explicitly approves a newer template, replace the binary asset, update the latest SHA-256 here, inspect placeholder counts/marking presence, and run the template tests.
