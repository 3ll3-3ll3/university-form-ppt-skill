# Template asset

The current user-approved PowerPoint template is stored at:

`assets/certificate_template.pptx`

Expected SHA-256 for the latest approved template:

`7c2b39b0e29a0771ddc909ce9341c2d8eb5a47f9f925ee30239650452bf04147`

Current template contract:

- one `{{name}}`
- one `{{student_id}}`
- two `{{school_name}}`

The latest approved template currently does **not** contain `SAMPLE / NOT VALID` or `仅供演示，不具效力` text in its PPTX XML. The workflow rule is conditional: if a future/current approved source template contains either marking, generation must preserve it visibly and must not delete, hide, crop, cover, or weaken it.

When the user explicitly approves a newer template, replace this binary asset, update the SHA-256 above, and run the template tests.
