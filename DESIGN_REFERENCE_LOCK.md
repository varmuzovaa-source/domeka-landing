# DOMEKA — Design reference lock

## Research conducted
Refero live style search and detailed inspection of three styles, 23 Nov 2026:

| Source | URL | Unique role |
|---|---|---|
| Aker — landscapes and ledgers | https://akercompanies.com | **Primary** architecture-first composition, white canvas, documentary imagery, clean rules, restrained deep ocean/forest chapters, credible numerical ledger. |
| Public — editorial meets machinery | https://public.com | Secondary: intelligent financial explanation and sharply legible CTA architecture; avoid copying speculative glows, dark technical panels, UI cards or their cyan accents. |
| Titan — lived-in institutional theatre | https://titan.com | Secondary: unhurried institutional rhythm, light/ink alternation, regular-weight readable sans, compact actions; avoid corporate artwork and beige-overload. |

## Locked direction
**Architecture-led investment editorial:** An investor page that looks rooted in real residential buildings and a clearly explained financial contract, not a generic fintech app.

Preserve:
1. White or very light cool-neutral page with near-black readable type.
2. Authentic architecture photography, not a CSS drawing, as the single hero object; if licensing unavailable, deliberately labeled asset placeholder instead of unlicensed imagery.
3. Dark ocean/forest accent reserved for primary actions and one conversion/explanation chapter; never gradients in every section.
4. Thin grid rules and information-as-design, especially four investment facts; proof numbers are *terms*, not invented historic performance.
5. Larger body copy for 50+ and first-screen clarity on mobile.

Borrow narrowly:
- From Public: ordered explanation, restrained buttons and intentional contrast.
- From Titan: calm spacing and pill/soft-rounded button treatment; do not mimic its entire appearance.

No go:
- warm-beige + olive + random serif-italic one-word emphasis;
- pastel fintech card grid, gradient blobs, glassmorphism, shadows everywhere;
- ornate pseudo-house in CSS as main hero image;
- green icons or shields that visually imply guaranteed safety;
- fabricated people/projects/reviews/company numbers.

## Proposed tokens, subject to rendering QA
- canvas `#FFFFFF`; support `#F4F6F6`; text `#16242A`; muted `#56646A`; lines `#DCE3E3`.
- primary dark ocean `#123D44` for CTA and one dark content chapter; accent strictly contextual `#C4E4DE` for small signals only.
- sans body: Inter or system sans, >=16px preferably 17–18px on long explanatory content; head display with mature grotesk personality.
- padding desktop 64–96px between section groups, mobile 48–64px; gutters mobile 20–24px, maximum content width 1160–1240px.
- buttons >=48px high, clear focus-visible; 8px or restrained pill radius chosen consistently.

## Funnel composition
1. Short high-clarity hero, actual terms and CTA above fold.
2. Financial terms as clean typographic ledger, not dashboard stats.
3. How the model works + specific evidence gap clearly identified.
4. Transparent risks and difference from savings account.
5. Useful 1–2 page educational lead magnet + qualified form.
6. FAQ + closing CTA.

Research source caveat: these are UI references, not investment evidence or compliance guidance.
