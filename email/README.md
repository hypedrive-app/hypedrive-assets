# Email Assets

Raster (PNG) brand images for **HTML email** — mail clients (Gmail, Outlook, Apple
Mail) block `data:` URIs and SVG, so emails must reference a hosted `https` PNG.
These are served over jsDelivr and used by the **Logto connector email templates**
(sign-in / register / reset OTP, and organization invitations).

## Files

| File | Use where |
|---|---|
| `wordmark.png` (600w) / `wordmark@2x.png` (1200w) | Header of light-background emails |
| `wordmark-dark.png` / `wordmark-dark@2x.png` | Emails with a dark header band |
| `icon.png` (128) / `icon@2x.png` (256) | Compact mark / footer |

## Usage in an email template
```html
<img src="https://cdn.jsdelivr.net/gh/hypedrive-app/hypedrive-assets@main/email/wordmark.png"
     alt="Hypedrive" width="132" style="display:block;height:auto" />
```
Set an explicit `width` and `alt`; the file is 2× density so it stays sharp on retina.

**Consumer:** backend Logto seed (`internal/platform/logto/email_templates.go`) embeds this URL in every connector email template.
