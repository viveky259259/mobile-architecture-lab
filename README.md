# MAL — Mobile Architecture Lab

A 5-part, application-only engineering lab that turns senior mobile engineers into
**T-shaped mobile architects** — deep in one stack, fluent across the rest, grounded in
production fundamentals (observability, trade-offs, clean architecture).

Across five labs over three months, each participant builds one real product — a
**hyperlocal marketplace with offline-first, on-device AI** — and leaves with a working
app, a documented set of architecture decisions, and a portfolio.

🔗 **Live site:** https://mobilearchitecturelab.com
🎟️ **Lab 1 — Flutter & Foundations:** July 11, 2026 · Paytm, Mumbai · [Apply on Luma](https://luma.com/iwn39kby)

## Project structure

| Path | Description |
|------|-------------|
| `src/site/pages/` | Source HTML for public pages. `landing.html` becomes both `/` and `/landing.html`. |
| `src/site/pages/` | Canonical source for both `.html` and extension-free public routes. |
| `src/site/assets/` | Public assets grouped by `icons/`, `images/`, `styles/`, `scripts/`, and `logo/`. |
| `src/content/` | Lab briefs, communications, calendar invites, and reports. |
| `src/print/` | Sponsorship template/deck HTML sources and PDF exports. |
| `src/marketing/` | Social copy and promotional artwork. |
| `src/legacy/` | Retained old-site redirect source. |
| `scripts/` | Repeatable project tooling, including the static build and PDF generator. |
| `dist/` | Generated deployable site; never edit it directly. |

## Stack

Static HTML/CSS with a small, dependency-free build script. The hand-rolled brand system
uses Sora, Inter, and JetBrains Mono with a gradient palette across Flutter, Swift, Kotlin,
and React Native accents. The site is deployed on Netlify.

## Local workflow

```bash
bash scripts/build-site.sh
```

The build recreates `dist/` from `src/site/` and preserves every currently published page
and extension-free route. Netlify runs this command automatically and publishes `dist/`.

To refresh print exports on macOS with Google Chrome installed:

```bash
python3 scripts/generate_pdfs.py
```

## The arc

1. **July 11, 2026 — Flutter & Foundations** — architecture skeleton + first on-device AI feature
2. **August 1, 2026 — Native iOS / Swift** — concurrency, modular client design, local LLM, and mobile observability with Measure
3. **August 29, 2026 — Native Android / Kotlin** — modularization, CI/CD, crash analytics
4. **September 5, 2026 — React Native** — deep links, multi-env, growth & attribution
5. **September 26, 2026 — Synthesis & Scale** — observability, resilience, architecture defense

---

Built by practitioners, for practitioners.
