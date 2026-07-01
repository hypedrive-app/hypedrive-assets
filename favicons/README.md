# Favicons & App Icons

Rastered from `logos/app-icon-dark.svg` (dark rounded tile + rose arrow). Regenerate
with the repo's build step if the source changes — do not hand-edit PNGs.

## Files

| File | Size | Use where |
|---|---|---|
| `favicon.ico` | 16/32/48/64 multi | Classic browser tab icon (`<link rel="icon">`) |
| `favicon.svg` | vector | Modern browsers (`<link rel="icon" type="image/svg+xml">`) |
| `apple-touch-icon.png` | 180 | iOS home-screen (`<link rel="apple-touch-icon">`) |
| `icon-192.png` / `icon-512.png` | 192 / 512 | PWA manifest `icons` (`purpose: any`) |
| `icon-maskable.png` | 512 | PWA manifest `icons` (`purpose: maskable`) |
| `icon-{16..1024}.png` | various | Any fixed-size need (og fallbacks, tiles) |

## Manifest snippet
```json
"icons": [
  { "src": "https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/favicons/icon-192.png", "sizes": "192x192", "type": "image/png" },
  { "src": "https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/favicons/icon-512.png", "sizes": "512x512", "type": "image/png" },
  { "src": "https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/favicons/icon-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
]
```
