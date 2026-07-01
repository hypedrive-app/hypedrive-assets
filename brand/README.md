# Brand Tokens

Machine-readable brand constants + a sample PWA manifest. Import these instead of
hardcoding hex/gradients so colour can't drift across apps.

| File | Use where |
|---|---|
| `brand.json` | Colour ramp (`ink`, `surface`, `accent.from/mid/to`), the canonical CSS gradient, type family, app-icon radius ratio. Read by design tooling / theme setup. |
| `manifest.webmanifest` | Drop-in PWA manifest referencing the CDN icons (`icon-192/512` + maskable). |

## Colours
- Ink `#18181b` · Surface `#09090b` · White `#ffffff`
- Accent gradient `#fb7185 → #f43f5e → #e11d48` (135°)

## CDN
```
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/brand/brand.json
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/brand/manifest.webmanifest
```
