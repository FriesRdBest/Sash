"""Design tokens and usage guidelines."""

## Colors

- Primary: `#0b57d0` — primary actions, links
- Success: `#1e7e34` — positive statuses
- Warning: `#b45f06` — cautions, pending states
- Error: `#c62828` — failures, destructive actions
- Background (cards): `#fafafa`
- Border: `#e0e0e0`
- Muted text: `#555555`

## Typography

- Font stack: `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- Headings: 2rem / 1.6rem / 1.2rem for H1/H2/H3
- Body: default Streamlit body text, line-height 1.6

## Spacing

- Use Streamlit's default vertical rhythm.
- For custom blocks, prefer margins: `0.5rem`, `0.75rem`, `1rem`.

## Components

- Cards: `.card` class for grouped content.
- Buttons: default Streamlit buttons; primary for destructive actions in Danger zone.
- Tables: `.dataframe` styles applied globally.
- Metrics: `.metric-card` with `.metric-label` and `.metric-value`.

## Status text

- Use `.status-ok`, `.status-warn`, `.status-error` for inline status labels.
- Avoid emojis; use text labels like "OK", "Failed", "Pending" where needed.

## Tone

- Professional, concise, and precise.
- Avoid casual phrasing and decorative elements.
