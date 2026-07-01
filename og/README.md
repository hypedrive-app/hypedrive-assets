# Open Graph / Social Share

1200×630 share cards (the standard OG/Twitter image ratio). Dark branded background,
centred wordmark, tagline.

## Files

| File | Use where |
|---|---|
| `og.svg` / `og.png` | Default share card — `og:image` / `twitter:image` for the marketing site |
| `og-creator.svg` / `og-creator.png` | Creator app / creator landing shares |
| `og-brand.svg` / `og-brand.png` | Brand app / brand landing shares |

## Usage
```html
<meta property="og:image" content="https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/og/og.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/og/og.png" />
```
Always reference the **PNG** for OG (SVG is not supported by most scrapers).
