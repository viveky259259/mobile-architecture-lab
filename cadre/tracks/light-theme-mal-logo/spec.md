<!-- cadre:generated from="cadre/tracks/light-theme-mal-logo/spec.json" schema="cadre.spec.v1" hash="aed822a4b43dee18" -->
# Generate light-theme MAL logo asset

## Description

Create a light-theme version of the MAL logo/lockup that matches the existing Mobile Architecture Lab branding assets and can be used in the static site.

## Functional Requirements

- **Light-theme logo asset**: Add a logo asset under the existing logo directory that is legible on light backgrounds and consistent with the current MAL visual identity.
- **Site compatibility**: Use a browser-friendly asset format and preserve existing logo assets without breaking current pages.

## Non-Functional Requirements

- **Scoped visual change**: Keep the work limited to logo assets and any minimal references needed for discoverability.

## Acceptance Criteria

- **Asset exists**: A light-theme MAL logo asset exists on disk in the repo with valid SVG or image structure.
- **Visual validation**: The asset can be rendered locally and inspected for light-background contrast and correct framing.

## Out Of Scope

- **No full redesign**: Do not redesign landing, sponsor deck, or invoice pages.
- **No unrelated content changes**: Do not alter speaker, sponsor, or event copy.

## Canonical Source

Canonical data lives in `cadre/tracks/light-theme-mal-logo/spec.json`. This Markdown is a generated human-readable projection.
