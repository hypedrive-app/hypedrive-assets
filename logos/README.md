# Logos

Vector brand marks. **Prefer SVG** everywhere it's supported (crisp at any size).
For raster contexts (email, favicons) use the PNGs in `email/` and `favicons/`.

## Files

| File | What | Use where |
|---|---|---|
| `wordmark.svg` | Full "Hypedrive" wordmark — dark text + rose arrow | Light backgrounds: site headers, docs, decks |
| `wordmark-dark.svg` | White text + rose arrow | Dark backgrounds / dark-mode headers |
| `wordmark-mono.svg` | Solid `#18181b` (arrow included) | One-colour print, watermarks, stamps |
| `wordmark-white.svg` | Solid white | Over photos / coloured fills |
| `wordmark-{creator,brand,admin,storefront}.svg` | Per-app wordmark (same mark, app a11y title) | Each app's own header |
| `icon.svg` | Bare rose arrow mark | Compact spots, avatars, spinners |
| `icon-mono.svg` / `icon-white.svg` | Single-colour arrow | Monochrome UI |
| `app-icon-dark.svg` | Rounded dark tile + centred arrow | App/launcher icon, favicon source (light UI) |
| `app-icon-light.svg` | Rounded white tile + arrow | Launcher icon on dark UI |
| `app-icon-maskable.svg` | Full-bleed, safe-zone padded | Android PWA maskable icon source |

## Brand
Dark `#18181b` (text) · rose gradient `#fb7185 → #e11d48` (arrow). Keep clear space ≈ the arrow's width around the wordmark.

## CDN
```
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/logos/wordmark.svg
```

## Added
- `favicon-tile.svg` — dark tile with a **larger** chevron, tuned to stay legible at 16px (source for `favicons/`).
- `icon-dark.svg` — bare dark chevron for light UIs.
- `wordmark.png` / `wordmark-dark.png` / `icon.png` — raster fallbacks (SVG preferred).

## Per-app accent colours
The neutral `wordmark.svg` / `icon.svg` use the **rose** (creator/flagship) accent.
Per-app variants carry that app's own accent gradient:

| App | Accent | Family |
|---|---|---|
| creator | `#e11d48` | rose |
| brand | `#10b981` | emerald |
| admin | `#2563eb` | indigo / blue |
| storefront | `#10b981` | emerald |

Files: `wordmark-<app>.svg`, `icon-<app>.svg`, `app-icon-<app>.svg`. Machine-readable in `brand/brand.json` → `apps`.
