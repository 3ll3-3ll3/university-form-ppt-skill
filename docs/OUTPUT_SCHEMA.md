# Output schema

For every resolved school, chat output must follow this order. Each school/form field goes in its own copyable code block.

1. Chinese university name
2. Official English Name
3. First name — surname pinyin, e.g. `Li`
4. Last name — given-name pinyin, e.g. `Feiyu`
5. Student ID
6. Address
7. City
8. State/Province
9. Postal/Zip code
10. coordinates last

Do not output these by default:

- Country/Region
- Address line 2
- VAT/GST ID

## Identity convention

The project intentionally uses:

- First name = surname pinyin
- Last name = given-name pinyin

PPT `{{name}}` is the combined form, e.g. `Li Feiyu`.

Do not infer the user's real name from a school email username.

## Coordinate output

- If one relevant campus is used, output one clearly identified Latitude/Longitude pair.
- If the university has several campuses, output at most the two most important and representative campus coordinate pairs, each labeled with the campus name.
- Form address and primary coordinates must correspond to the same real campus.

## Artifact order

For a generated PPT, the user-facing artifact order is:

1. PNG rendered from the actual PPT;
2. PPTX;
3. the fields above.

Google Drive archiving is automatic in the same workflow and must be verified before full completion is claimed.
