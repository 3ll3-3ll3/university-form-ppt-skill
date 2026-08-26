# Output schema

Return these fields for each resolved school. Each field should be in its own copyable code block in chat.

1. `First name` — surname pinyin, e.g. `Li`
2. `Last name` — given-name pinyin, e.g. `Feiyu`
3. `Address`
4. `City`
5. `State/Province`
6. `Postal/Zip code`
7. `Latitude`
8. `Longitude`
9. `Student ID` — include when a PPT is generated

Removed by default:

- Country/Region
- Address line 2
- VAT/GST ID

The school/campus used for the form fields and coordinates must be the same one.
