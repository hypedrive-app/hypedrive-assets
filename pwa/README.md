# PWA Assets

Progressive Web App install assets: iOS splash screens, manifest screenshots, and
shortcut icons.

## Structure

| Folder | Use where |
|---|---|
| `splash/` | iOS launch images, one per device resolution (`<link rel="apple-touch-startup-image" media="...">`). Filenames are `WxH.png`. |
| `screenshots/` | PWA manifest `screenshots` (`narrow.png` = mobile, `wide.png` = desktop) — shown in the install prompt. |
| `shortcuts/` | PWA manifest `shortcuts` icons (`default.png`). |

## CDN
```
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/pwa/splash/1290x2796.png
https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/pwa/screenshots/wide.png
```
