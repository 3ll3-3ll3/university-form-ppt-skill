# Google Drive record archive policy

## Permanent destination

All per-school generation records belong in Google Drive:

```text
大学PPT生成记录/<Chinese university name>/
```

GitHub stores the reusable workflow, template, scripts, docs, and tests only.

## Archive is mandatory and automatic

Every PPT generation must perform the Drive archive automatically in the same workflow. It must never wait for the user to send a second “complete/archive it” message.

Completion chain:

```text
generate PPT
-> render actual PNG
-> visual QA
-> prepare user-facing artifacts/fields
-> upload final PPTX
-> upload final PNG
-> write MD with the real returned PPT/PNG Drive URLs
-> upload MD
-> read target school folder back
-> confirm the expected three files exist
-> only then claim full completion
```

If any external step fails, explicitly report:

```text
该步骤当前没有成功完成。
```

Never fabricate an upload, URL, replacement, deletion, render, commit, or readback result.

## Three-file bundle and naming

Each run uses one matching record stem:

```text
<record_stem>.md
<record_stem>.pptx
<record_stem>.png
```

The PNG must be rendered from the final PPTX, never AI-generated.

Use local generation time precise to one minute:

```text
YYYY-MM-DD_HH-mm
```

If the same school receives another record in the same minute, append `_<student_id>` only to prevent collision. Student ID is not the normal record stem.

## Markdown minimum content

- Chinese university name
- official English full name
- original user input
- First name
- Last name
- combined random pinyin name
- Student ID
- Address
- City
- State/Province
- Postal/Zip code
- selected campus/campuses
- corresponding coordinates
- PPT visual QA result
- real Google Drive PPT URL
- real Google Drive PNG URL

Only URLs actually returned by successful Drive writes may be recorded.

## REDO

Any error in school name, abbreviation use, first-line wrapping, body formatting, signature wrapping, template version, or Drive artifact requires a full redo:

PPT regenerate -> PNG render -> visual QA -> replace/update Drive PPTX -> replace/update Drive PNG -> update Drive MD -> folder readback verification.

Do not leave a wrong Drive version behind while fixing only the chat artifact.
