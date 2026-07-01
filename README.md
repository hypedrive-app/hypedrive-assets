# Hypedrive Assets

Central, versioned source of truth for Hypedrive brand + product assets. This repo
is **public** so the files can be served over a CDN (jsDelivr) — required for
places that can't use bundled/`data:` assets, such as **HTML email templates**
(Logto connector emails) and other external surfaces.

## CDN usage (jsDelivr)

Any file here is served at:

```
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/<path>
```

Example — the email wordmark:

```
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/email/wordmark.png
```

Pin a tag/commit instead of `@main` for immutable, long-cached URLs in production.

## Structure

| Folder | What |
|---|---|
| `logos/` | Wordmark + icon SVGs. Neutral (`wordmark.svg`, `icon.svg`) plus per-app variants (`wordmark-<app>.svg`, `icon-<app>.svg`). |
| `favicons/` | `favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, PWA `icon-192/512/maskable.png`. |
| `email/` | Email-safe raster assets (PNG) for `<img>` in HTML emails — SVG/`data:` are blocked by most mail clients. |
| `og/` | Open-Graph / social share images. |
| `avatars/` | Product avatar/illustration assets. |
| `pwa/splash/` | iOS PWA splash screens (per device resolution). |
| `pwa/screenshots/` | PWA manifest screenshots (narrow/wide). |
| `pwa/shortcuts/` | PWA manifest shortcut icons. |

## Notes

- Canonical brand mark = the Hypedrive wordmark (dark `#18181b` text + rose `#e11d48`/`#fb7185` accent).
- App-suffixed variants (`-creator`, `-brand`, `-admin`, `-storefront`) differ only by the `<title>` a11y label; the drawn mark is identical.
- Consumers (FE apps, Logto email templates, backend seeds) should reference these
  via CDN rather than re-committing copies, so the brand can't drift.
