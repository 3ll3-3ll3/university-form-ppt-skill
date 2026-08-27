# School research policy

## Automatic institution identification

The workflow may be triggered by a Chinese/English university name, school email, school email domain, college/faculty name, or another obvious university clue. Resolve the institution directly; do not ask the user to explain an already clear clue.

For email/domain input, verify domain ownership through the university's official web presence or authoritative institutional pages. Do not assume a brand-like or acronym-like domain is official merely because it looks plausible.

## Source priority

Use, in order:

1. official university website;
2. official admissions website/pages;
3. official international/exchange website/pages;
4. official contact/information-disclosure pages;
5. reliable maps/geographic databases for coordinates after the official campus/address has been established.

## Required verified fields

Verify:

- official Chinese university name;
- official English full name;
- main/representative campus or campuses;
- Address;
- City;
- State/Province;
- Postal/Zip code;
- campus coordinates.

Never fabricate a field to make the form look complete.

## Official English name

Use the exact English full name officially used by the university. Do not machine-translate it, invent an alternative, abbreviate it, or shorten it for PPT layout.

The same exact official English full name must be used in both `{{school_name}}` positions.

## Campus choice

If the input does not identify a campus, select the main/current/most representative campus supported by official contact/admissions information for the form address.

If the university has multiple campuses:

- do not list every campus;
- select at most the two most important, common, and representative campuses for coordinate output;
- label every coordinate pair with its campus name;
- ensure the form Address corresponds to the selected primary campus.

## Coordinates

Coordinates must correspond to real verified campuses.

Preferred source order:

1. official campus/map page with coordinates;
2. reputable map/geocoding source for the verified official address;
3. secondary geographic database with cross-checking.

Prefer WGS84 output. If a mainland-China map source exposes GCJ-02/BD-09, normalize internally before returning when possible.

## Uncertainty

If an institution, official English name, campus, postal code, or coordinate cannot be reliably verified, say so rather than inventing a plausible-looking value.
