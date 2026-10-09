# Live baseline and visual design tokens

## Baseline checkpoint

- Deployment: `https://sash-4-sinch.streamlit.app/`
- Hosting: Streamlit Community Cloud
- Repository: `FriesRdBest/Sash`
- Branch: `main`
- Entrypoint: `app.py`
- Baseline commit before this documentation: `76c68577c400a002a1725d627a68baeb0ad725aa`
- The production baseline is the live Phase 18 application. Preserve its copy, navigation labels, ordering, widgets, information sequence, and behavior during the visual refresh.
- The Phase 20 recovery branch is not the production baseline and must not be transplanted as part of this visual-only work.
- The approved palette is committed on `main`; the initial styling is live. This record is documentation only and does not change application behavior.

## Evidence status

- Deployment logs supplied by the owner confirm Community Cloud starts `main` / `app.py` and redeploys after the palette commit.
- The owner confirmed the palette is visible in the live app.
- Before/after screenshots for every page and interaction state have not yet been captured or attached. Mark visual comparison and responsive review as pending until that evidence exists.
- No baseline wording or behavior changes are in scope.

## Approved palette

| Role | Color | Use |
|---|---|---|
| Periwinkle | `#CED5E8` | Soft borders, subtle selection surfaces, quiet accents |
| Deep indigo | `#1D2240` | Primary text, headings, high-contrast controls |
| Clear blue | `#3A6FF3` | Focused accents and links; avoid small white-on-blue text unless verified |
| Muted plum | `#564957` | Secondary text and restrained accents |
| White | `#FFFFFF` | Main surfaces and cards |
| Black | `#000000` | Strong neutral/brand anchor when appropriate |
| Page neutral | `#F6F7FB` | Light page canvas used by current implementation |

## Sinch system reference

Public Nectary Docs tokens at the Base Light theme document a separate semantic system: `neutral-900` default text, `neutral-700` caption text, `neutral-100` canvas, white primary surface, `tropical-700` primary controls, `ocean-400` focus, ocean info feedback, and distinct success/warning/danger feedback tokens. The public token reference lists DM Sans as the main typeface and DM Mono for code, with 16px/24px body text, 14px/22px small body, and 12px/20px extra-small body; documented shape sizes are 6px/10px/14px and elevation uses restrained shadows. These are reference findings only. They do not override the user-approved Sash palette. Current private Brandfolder logo assets and usage rules could not be inspected.

## Visual behavior

- Keep the overall interface light, professional, modern, and legible.
- Use glass styling only on cards: near-white translucent surface, faint periwinkle border, gentle shadow, and restrained blur.
- Keep text opaque and high contrast; never put body text on translucent/variable backgrounds.
- Retain existing semantic success, warning, and error colors and their meanings.
- Preserve responsive spacing and avoid horizontal clipping at narrow widths.
- Do not add decorative UI, new features, or altered copy as part of this refresh.

## Contrast findings

Calculated using WCAG relative-luminance contrast:

| Foreground on background | Ratio | Finding |
|---|---:|---|
| Indigo `#1D2240` on white `#FFFFFF` | 15.50:1 | Passes normal text |
| Plum `#564957` on white `#FFFFFF` | 8.45:1 | Passes normal text |
| Blue `#3A6FF3` on white `#FFFFFF` | 4.42:1 | Below 4.5:1 normal-text criterion; use as non-text accent or pair with approved dark text only after verifying that pairing |
| Blue `#3A6FF3` on page `#F6F7FB` | 4.13:1 | Below 4.5:1 normal-text criterion |
| Indigo `#1D2240` on blue `#3A6FF3` | 3.50:1 | Not suitable for normal-size text |
| Indigo `#1D2240` on periwinkle `#CED5E8` | 10.56:1 | Passes normal text |
| Plum `#564957` on page `#F6F7FB` | 7.89:1 | Passes normal text |

Use at least 4.5:1 for normal text and 3:1 for large text and meaningful non-text controls, following WCAG 2.2 AA. Focus indication should be visible and maintain the applicable focus contrast. Check actual rendered combinations including muted text, selected/hover navigation, buttons, links, statuses, focus rings, borders, and charts. Approved individual colors do not automatically make every pairing accessible.

## Phase tracking

- Phase 0: production baseline coordinates and commit recorded; screenshot and complete interaction inventory pending.
- Phase 1: palette approved; public Nectary system tokens reviewed as reference; private Brandfolder assets/usage remain unavailable.
- Phase 2: palette and initial styling specified here; full rendered token/component audit remains.
- Phases 3-5: review and style the live pages without changing navigation, copy, or behavior.
- Phase 6: screenshot, keyboard, contrast, zoom, and responsive verification pending.
- Phase 7: post-refresh CI/startup review, visual diff, limitations, and rollback handoff pending.

## Rollback

The pre-theme production checkpoint is commit `ea7d82b54d574e0fad7bbb1a132d026497766f90`. To inspect/recover that source in a local clone, first create a backup branch and then use a normal reviewed revert or restore workflow; do not force-push protected `main`.

The theme commit is `76c68577c400a002a1725d627a68baeb0ad725aa`. Review its two-file diff to revert only the theme if needed. Keep the previous version of `.streamlit/config.toml` and `src/styles.py` available through Git history.