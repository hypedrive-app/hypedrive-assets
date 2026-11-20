# Hypedrive brand and design system: handoff for the next agent

The owner gave a lot of direction over one long session (2026-11-19 to 11-20). This file collects all of it. **Read it fully before you change anything.** Where an older instruction conflicts with a newer one, the newer one wins; both are listed so you can see how the decision moved.

The owner writes in Hinglish and checks everything by eye in **Zen** (a Firefox-engine browser with the pdf.js viewer). Their recurring complaints were regressions, breaking stated rules, and "slop". Go one component at a time, look at it, and never batch-change things blindly.

---

## 1. Where everything is

| What | Path |
|---|---|
| Brand book (HTML + PDF, 25 pages) | `BRAND/Hypedrive-Brand-Guidelines.html` / `.pdf` |
| Logo system (lockups, mark, wordmark, app icons, favicons) | `BRAND/assets/logo/` (built from `FINAL/`) |
| Illustrations, patterns, social, print, splash | `BRAND/assets/…` |
| Design tokens | `BRAND/tokens/colors.css`, `tokens.json`, `tailwind.preset.js`, `type.css` |
| UI kit (light + dark) | `BRAND/ui/hypedrive-ui-kit.html`, `hypedrive-ui-kit-dark.html` (+ `.png`) |
| Mobile screens (12) | `BRAND/ui/hypedrive-screens-mobile.html`; each screen in `BRAND/ui/screens/NN-*.html/png` |
| Desktop screens (4: overview, campaigns, review queue, overview dark) | `BRAND/ui/hypedrive-desktop-N.html/png` |
| Stock photos, platform favicons, tight UI logo | `BRAND/ui/assets/stock/…`, `BRAND/ui/assets/logo/lockup-tight-*.svg` |
| **All generator source** | `BRAND/source/` (a copy of `/tmp/hdwm`, which may get wiped) |

### Source files (`BRAND/source/`)

| File | What it does |
|---|---|
| `final.py` | Logo system: parcel mark, wordmark (Bricolage + optical spacing + hexagon i-dot), lockups, app icons, pixel-snapped favicons |
| `isofam.py` | Isometric illustration family |
| `palette.py` | OKLCH colour maths |
| `brand.py` | Brand book, tokens, application assets. **It is the source of the colour scales and semantic tokens.** |
| `uikit.py` | Base component CSS, icon helpers (`ic` = Nucleo Sharp outline, `ics`/`icf` = Nucleo UI Fill solid, `soc` = Nucleo social), tokens are read from `tokens/` |
| `uikit2.py` | Charts, stat cards, progress bars, shell/sidebar CSS, extra components |
| `kit_build.py` | UI kit page and mobile screens |
| `kit2.py` | Kit sections (charts, shell, more components, interaction) and desktop screens |
| `render_ui.sh` | Renders everything in Zen headless |
| `contrast.js` | DOM text-contrast audit, run with the chrome-devtools MCP `evaluate_script` |
| `audit2.js` | DOM audit for non-text contrast, clipped text, tap targets, tiny text, inline hex |
| `audit.py` | Static SVG audit (parses, refs, clipping, colours present, visible at 16 px) |

### Build order

These used a venv in `/tmp/hdwm/venv` (packages: fonttools, uharfbuzz, numpy, pillow). Fonts are in `source/fonts/` and the scripts expect them at `/tmp/hdwm/fonts/`. Icon JSON is in `source/icons/` and the scripts expect it at `/tmp/hdwm/`. **Fix the paths if `/tmp` is gone.**

```
python -I final.py   ~/Downloads/hypedrive-wordmark/FINAL      # logo system
python -I brand.py   ~/Downloads/hypedrive-wordmark/BRAND      # tokens + book + assets (prints "contrast issues: []")
cp -rT FINAL BRAND/assets/logo
python -I kit_build.py > build.log 2>&1 && bash render_ui.sh   # NEVER pipe the build into tail: a failed build then renders stale files
google-chrome --headless=new --no-pdf-header-footer --print-to-pdf=… BRAND/Hypedrive-Brand-Guidelines.html
```

Before each change, save baseline PNGs and compare before and after side by side.

---

## 2. Logo and brand identity (owner decisions)

- **Origin:** "PostHog wordmark se inspired", "sirf PostHog ka styling", fresh concept. The owner picked the **isometric parcel**: yellow top, blue left, orange right, black tape over the lid and down the right face, white label dot on the left face. That parcel is the mark.
- Mark: true 30° isometric cube, two-stop gradient per face, rounded silhouette (radius 1.45 iso units), smooth continuous-curvature corners (`rpoly` with `SMOOTH = 0.6`), soft tape end, rim light on the lid edges. Dark mode: white tape, dark dot.
- **Do not use SVG `<mask>`.** It broke in Zen's pdf.js. Build knockouts from geometry.
- One-colour mark: separate faces with seam gaps, the tape as a notch, the dot as an even-odd hole.
- **Wordmark:** Bricolage Grotesque 700, opsz 96, optical letter-spacing. The **i-dot is a hexagon**: the parcel's silhouette, 5% larger than a round dot.
- Lockups: horizontal, stacked, parcel-only. Brand-book files include clear space (half the cap height); **UI uses the "tight" lockup** with no baked-in padding (`ui/assets/logo/lockup-tight-*.svg`).
- Logo sizes in UI (owner said "logo looking so damn small"): sidebar 24 px, phone top bar 22 px, welcome 30 px.
- App icon: squircle-ish smooth corners (`rpoly` square, radius s·0.19), soft gradient tile, contact shadow, no filters. On the Cobalt tile, use the one-colour white mark (the blue face disappears otherwise).
- Favicons: pixel-snapped. 16 px shows faces only; 32 and 48 px use thicker tape and no dot.
- Tagline (written by me, **not confirmed by the owner**): "Products in. Hype out."
- **Open:** the owner asked to "brand identity bhi improve karo". The brand book is now **behind the UI system** (Bricolage only, old radius, old components, no new tokens). Next step: regenerate the book's type, colour, layout, components and "brand in UI" pages from the kit's CSS and tokens.

---

## 3. Colour system (final)

- Built in OKLCH. Scales 50–950 for **Cobalt, Vermilion, Marigold, Ink, Mint** (Mint is for success only).
- Brand colours **are** scale steps: Cobalt = 600, Vermilion = 500, Marigold = 300, Ink = 900. Warm darks shift toward amber and red, never olive.
- Ink scale was rebalanced so `fg-subtle` (Ink 500) is **≥ 4.5:1 on every light surface**.
- Semantic tokens (light and dark):
  - surfaces: `canvas` → `surface` → `surface-raised` → `surface-sunken` → `overlay`
  - text: `fg`, `fg-muted`, `fg-subtle`
  - borders: `border`, `border-strong`, `border-input`, `border-input-hover`
  - action: `accent`, `accent-hover`, `accent-pressed`, `accent-subtle`, `accent-fg`, `link`
  - focus: `focus`, `focus-ring`, `indicator` (tab underline)
  - status: `success`, `warning`, `danger`, `info`, each with `-subtle` and `-strong`
  - controls: `control*` (grey secondary), `track`, `track-strong`
  - inverse and skeleton: `inverse*`, `skeleton*`
  - solids: `danger-solid*`, `success-solid`
  - data: `star`, `data-1`, `data-hl`
  - tones: `tone-cobalt`, `tone-vermilion`, `tone-marigold`, `tone-mint`, `tone-ink`
  - shadows: `shadow-e1/e2/e3`, defined per theme
- `brand.py` `check_semantic()` asserts every pair: text 4.5:1, non-text 3:1. It must print `contrast issues: []`.
- **Owner preference: solid over tinted.** Badges, selected chips, avatars, delta pills (now gone), active tab counts and banner icons are solid. **Tint only where it reads better: alerts/notices**, tinted with `-strong` text at perfect contrast.

---

## 4. Typography

- **Bricolage Grotesque** is the brand voice: display, headings, hero numbers (opsz axis).
- **Geist** is all interface text. **Geist Mono** is for IDs and codes only, not inside small body text.
- UI scale: Display 32 · Title 1 24 · Title 2 19 (Bricolage) · Title 3 15 · Body 15 · Small 13 · Caption 12 (Geist).
- Weights: titles 650, labels and buttons ~560, body 400. Never weight 700 everywhere; the owner called that crude.
- Sentence case everywhere. **No uppercase, letter-spaced labels.**

---

## 5. Rules the owner stated (do not break)

Older ones also live in memory (`~/.claude/projects/-home-shivam-gupta-Documents-hypedrive/memory/`).

**Look and feel**
- "Mature", high fidelity, like modern AI products (Linear, Vercel, Claude). Use Emil Kowalski's `emil-design-eng` skill principles.
- **No slop, no bloat.** Banned:
  - emoji in UI
  - sparkles as decoration
  - glows behind products
  - gradient text
  - uppercase tracked labels
  - captions/subscripts in stat cards
  - lone "↑ 42%" lines
  - pills or chips inside stat cards
  - placeholder data ("A B C" avatars)
  - mismatched numbers across a screen
- **Soft UI is liked, but never invisible.** The workspace switcher once vanished. Every surface must separate from its background: white card on the grey canvas, with a hairline border.
- **Shadows subtle.** In-flow surfaces (cards, rows, panels, stat cards, banner, search) get **no shadow**, only a hairline. Only floating things get shadows: menus, toasts, dialogs, sheets, tooltips, command palette.
- **Radius by maths**, consistently:
  - concentric where an inner element sits near a corner: inner = max(outer − gap, 4)
  - otherwise radius ≈ height × 0.27: button 12 · sm 8 · chip 8 · tag 8 · badge 6 · checkbox 6 · input 12 · card/panel 16 · dialog/sheet 24 · phone 52/42
- **Use real estate**, especially in empty states: show suggestions and related items, not a lone illustration.

**Buttons**
- Flat deep Cobalt primary, no glow, a 1px darker edge, `scale(0.97)` press.
- **Grey secondary with no border** (owner rule; I broke it once with white + hairline).
- Ghost and danger variants. Disabled is solid grey (control bg, subtle text), not a faded colour.
- Optical padding: 14 px on the icon side.
- **Icons on buttons only where they help recognition:** `+ New`, Upload, Export, Filter, icon-only buttons. "Don't overuse icons."

**Icons**
- **Nucleo Sharp** (licensed) is the outline set.
- **Solid versions for active and selected states:** active tab bar item, active sidebar item, active underline tab. Solid icons on alerts. Use Nucleo UI Fill 18 from the repo (`packages/icons/node_modules/nucleo-ui-fill-18`).
- **Tabs and chips DO carry icons**: coloured by meaning (memory rule "Tabs U1"). Don't strip them when reducing icons elsewhere.

**Tabs, top bar, search, lists**
- Tabs: underline tabs, coloured icons by meaning, an `indicator` underline (≥ 3:1 in both themes). No pill tabs.
- Phone top bar: bare icons, no discs, 44 px hit areas.
- Search: 44 px on phone (40 in the filled style).
  - solid grey filled field, focus turns it white with a 2px accent ring
  - small round clear button; "Cancel" outside the field on phone; `⌘K` on desktop
  - suggestions dropdown: recent searches, typed part in bold, product thumbnails, keyboard hints
- Lists: every item is its own rounded card with gaps. Exceptions: tables, and nav or settings menus, which may be grouped lists with inset dividers.
- Product images sit bare, with no plate or tile behind them.

**Stat cards**
- One family, customised per data type: trend (area sparkline) · counts (mini bars) · rating (stars, half star) · compare (Now vs Before bars) · split (segmented bar + legend) · goal (value / total + segmented bar).
- The delta sits **on the label row, top right**, as coloured text with no arrow and no pill. No captions under the value.

**Focus**
- One ring everywhere: a 2px gap in the surface colour (`--ring-gap`) plus 2px `focus`.
- Inputs show focus as a 2px accent border (inset), with no glow.

**Contrast**
- Fix by eye, not only by numbers. Earlier, secondary buttons vanished even though every token check passed.
- Run `contrast.js` and `audit2.js` on light kit, dark kit, mobile and desktop. Target 0 failures. Only gradient-background false positives on the wallet card are allowed.

**Process**
- Verify everything in **Zen** headless: `~/.local/share/zen/zen --headless --no-remote --profile <dir> --screenshot …`.
- Show before asking: for visual A/B choices, render both, then ask.
- Ask through AskUserQuestion with the explanations inside the dialog.
- Max 4 concurrent agents, Sonnet only.

---

## 6. Licences and keys

- **Nucleo Sharp:** the licence was verified through Nucleo's `account-check.js`, with a key the owner pasted in chat. That key isn't saved anywhere; the owner was asked to put `NUCLEO_LICENSE_KEY` in their own `~/.profile`. The extracted glyphs are in `source/icons/nucleo_sharp.json`. Licensed for the owner's use; don't redistribute.
- `/tmp/nucleo-pkg` is an **unlicensed** copy, installed with scripts skipped. Never use it. The owner was asked to delete it (my `rm` was blocked).
- Stock product photos come from the repo's `docs/design-references`. Platform favicons come from Google's s2 favicon service.
- Creator portraits are **not** used: the free stock faces didn't match the Indian names, so avatars are initials.

---

## 7. Still to do (as of the end of this session)

1. **Sync the brand book with the UI system** (see section 2, "Open").
2. **Move about 280 inline `style=""` attributes into classes.** This is a prerequisite for React.
3. **Remaining components:** select menu, multi-select, segmented filter (not pill tabs), stepper navigation, table row actions, date input, each with empty, error and loading states.
4. Then the owner's plan: **rebuild the UI kit in React** ("phele fully refine kar lo, fir react se banayenge ui kit").
5. After every change: compare against the baseline, run the DOM audits in both themes, and check by eye in Zen. Watch for my past failure modes:
   - CSS slices that silently deleted blocks
   - generic class collisions (`.up`)
   - regex edits that shifted function arguments
   - builds piped into `tail`

---

## 8. Additions on 2026-11-20 (second session)

These rules extend the earlier sections. Where they conflict, these win.

**Icons**
- A solid icon is always the exact Nucleo twin of its outline (same name + `Fill18`). `uikit.FILL` is derived from `NMAP`, and `ics()` raises an error when no twin exists.
- Icons in a tab row are all solid and coloured by meaning. The active tab is shown by the underline and the text colour.
- Fixed icon meanings, the same on every screen:
  - Drops and Campaigns: `Box3`
  - Creators: `Users2`
  - Home: `House6`
  - Overview: `GridLayout`
  - Payouts: `MoneyBill`
  - Live / Paused: play / pause
  - For you: `Compass`

**Tint**
Tint is used only for:
- alerts
- repeated statuses in tables and lists
- selected table rows
- notification icon tiles

A lone status stays solid.

**The "after" standard**
- This applies to all mobile screens and the desktop page heads. The CSS lives in `source/xcss.py` (an appended layer).
- What it includes:
  - 32–44px Bricolage headlines, with a two-tone variant
  - full-bleed product photos, with discs over the photo
  - inline icon + value meta rows between hairlines, instead of stat tiles
  - real photo avatars
  - left-rule tips
- The owner said: adopt only genuine improvements from reference screenshots, never copy blindly.
- Floating pill tab bar was rejected: hiding the labels hurts recognition. Keep the labelled 4-item bar.
- The Wallet hero is flat Ink, not Cobalt. Cobalt stays the action colour.

**Stat cards**
- One anatomy for every card: label row, then the value, then a fixed visual zone pinned to the bottom.
- The owner said "fatter" was wrong, so keep them compact.

**Desktop**
- The sidebar logo row has the same height as the top bar (56) and shares its hairline.
- There is no duplicate search: the sidebar's ⌘K is the global search.

**Illustrations**
- `source/isoill.py`, built from chunky volumes in the signature faces.
- Physical parts (tyres, handles) stay Ink in both themes.

**Squircles**
- Only the app icon is a true squircle.
- The UI uses circular `border-radius`.
- Plan: `corner-shape: squircle` as progressive enhancement in React (Chromium only; Zen ignores it).

**Uizze skills**
- Installed in `~/.claude/skills`: `ui-design`, `anti-ui-slop`, `image-to-ui`, `ui-radar`, `uizze-ui`.

**Reverted on the owner's word (2026-11-20):**
- Inline icon+value meta rows were copied from a reference screenshot and used in the wrong places. Stats are back to the stat card, compact stat tiles and statbar.
- Stacked "deck" layers behind the hero are removed; the pager dots stay.
- Left-rule tips are back to info notices.
- Rule: never lift a pattern from a reference unless it genuinely fits the place it is used.
## ADDENDUM 2026-11-20 (late) — the approved language. The owner flags anything off it as "ugly".
Everything the owner called "ugly" today shared the same faults:
- controls that were oversized
- states signalled three ways at once (tint + border + coloured text + check)
- grey slabs used as backgrounds
- bordered keyboard chips
- decorative extras such as histograms
- tick marks placed inconsistently
- heavy discs
- dead space
- duplicated information

Apply this language everywhere:

- **Sizes**
  - Controls are 36, 40 or 44 tall.
  - Menu rows are 34 tall with 14px text, 16px muted glyphs, and an 8-radius inset hover at fg 6%.
  - List rows are 48–68 tall.
- **Selected states**: use ONE signal.
  - Chips and toggles: accent-subtle fill, no border, strong text.
  - When a toggle is off, show a white surface with a hairline, muted text and a greyed glyph.
- **Ticks**: always trailing (on the right), never leading, in menus and lists.
- **Shortcuts in menus**: plain text, fg-subtle at 12.5px, with no keycap borders.
- **Status glyphs**:
  - Use the solid twin (ics) bare, or on a WHITE 40px tile with a hairline.
  - Never use a big solid coloured disc.
- **Buttons**
  - Use the tactile cobalt finish (xlead "BUTTONS v-final") and the white secondary. Never override their shadows.
  - Use a small secondary for row actions.
  - Use link-text only for "learn more" style links.
- **Photo cards**: full-bleed, as in product card v5 in xd.py.
  - The photo stays full colour.
  - Text sits at the bottom on one scrim.
  - Status chips are solid.
  - No top wash.
- **Dates**
  - Use 36px circles.
  - Today is shown as accent text with a dot.
  - Out-of-month cells are blank.
  - A range is one continuous band.
- **Counters and progress**: use a hairline 3px bar plus "N of M" in tabular numerals, and say it once.
- **Text sizes**
  - Titles: 15/600 in rows, 17–20 on cards.
  - Body: 14/20.
  - Meta: 13–13.5 muted.
- **Dark mode**
  - Every edge stays visible.
  - Tints come from the tokens.
  - Text on a tint uses the -strong colour.

## 9. Decisions and lessons, 2026-11-20 (end of day). Read before touching anything.

### Final, owner-approved
- **Brand book = the "colourful" version.** Keep the colourful hero slides, cobalt bands, cube motifs and Bricolage display. It was debugged and refined (49 pages, fixes only).
  - Approved snapshot: `BRAND/versions/current-colourful/` (PDF + page PNGs) and `versions/source-current/`.
  - Rejected calm version, kept for reference: `versions/calm-0711/` and `versions/source-calm/`.
  - Pre-pass baseline: `versions/original-baseline.pdf`.
  - Side-by-side comparison: `versions/compare.html`.
- **Mobile / kit / desktop = the earlier standard.**
  - Type: Bricolage Grotesque for display, Geist for UI.
  - Canvas: white app canvas and the kit's original canvas.
  - The active tab is cobalt. On Welcome, "Hype out." is blue.
- **Direction A ("warm editorial") is REJECTED.** It used Geist-only display and a warm `#f7f4ef` canvas. It was rolled out without approval and fully reverted (the `xw*.py` layers are removed from `_late()`). Never re-introduce it.
- **The p79 sample creator email `hello@riyaglows.in` is approved.**

### Rules learned the hard way
1. **"Decide yourself" / "tu khud fix kar" covers fixing ugly and broken things only.** It never covers changing brand fundamentals: typeface, canvas or background colour, accent usage, logo, or any rule the owner already approved. For those, render the options side by side in ONE file, open it in Zen, and ask with the AskUserQuestion dialog.
2. **Keep a running list of every unrequested change** and disclose it before the owner has to ask "what else did you change?".
3. **Back up before any multi-page pass.** Snapshot sources and renders, then compare old vs new page by page. Revert anything that got plainer, emptier, lost real data or lost a motif. ("Regression" = worse than before, even if "cleaner".)
4. **Never delete exported asset files.** Add new variants alongside the originals.
5. **No bloat, ever.** A redesign = clearer, not busier. Never copy extra sections from a reference mock. Never invent filler rows or data to fill space.
6. **No tinted borders, no tinted glows.** Tinted surfaces are fill-only. The only coloured edges allowed: focus rings and an input's error or focus edge.
7. **One signal per state.**
   - Selected = a fill, or the radio, never fill + border + colour + tick.
   - Ticks trail.
   - Shortcuts are plain text.
8. **Verify by eye every time.** Agents' "done" reports overstate. Read the render at 2× (light + dark) before telling the owner. Watch for CSS specificity: a later or stronger rule silently winning has caused several "fixes" that never rendered.

### Build notes
- CSS layer order, last wins: `CSS → CSS2 → PAGE_CSS → XPASS → XSTEPS → xlead → xa → xb → xc → xd → xe → xf → xg → xm1 → xm2 → xm3 → xs → xy → xq1 → xq2 → xz`.
  - `xz.py` = the lead's final layer: button interaction, dialogs, danger red, logo tiles, overflow guard.
  - `xs.py` = the standard scale.
- Hook new layers by **matching the `_late()` lines by text**, never by line number. Line numbers shift and broke the hook twice.
- Bank and courier logos are cached in `BRAND/ui/assets/banks/` (Cashfree CDN: `cashfreelogo.cashfree.com/assets_images/pg/nb/128/<bank>.png`). Use them through `bank(code, size, tile=True)` in `uikit.py`.

### In progress at the end of this session
- Brand book: redrawing the hand-drawn UI specimens (p28, 36, 40, 42) to the current kit, in the colourful style.
- Mobile screens: a critical pass in the earlier standard (layer `xq1.py`).
- UI kit + desktop: a final pass (layer `xq2.py`).
