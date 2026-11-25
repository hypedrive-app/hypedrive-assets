# Evolve every page (owner, 2026-11-26)

The owner's words:
- "Why did you design the apps as they are? Design the best possible apps at your discretion. I feel you regressed everything to fit the existing UI."
- "Evolve everything based on the mockups and the design system, fully polished."
- "Evolve and improve all pages, but don't make everything busy."

The maturity pass made pages correct but flat and samey, shaped like the existing app. Pages must now be DESIGNED, evolved from the original kit mockups and the design system, while staying calm.

## The two approved references (study the PNG and the code before touching anything)
- **Creator Home:** ~/Downloads/hypedrive-wordmark/BRAND/ui/screens/03-home.png (code /tmp/hdwm/scr_home.py, CSS /tmp/hdwm/xcv.py).
  - Ink wallet card (money is the hero, the PAN step built in).
  - Big photo action cards for "Your turn" (deadline, progress, one action).
  - A live shipment card with the brand's isometric illustration.
  - One editorial photo pick.
- **Brand Home:** ~/Downloads/hypedrive-wordmark/BRAND/ui/hypedrive-desktop-1.png (code /tmp/hdwm/desk_home.py, CSS /tmp/hdwm/xbd.py).
  - The original mockup's analytics craft: KPI cards with sparklines and deltas, a period-over-period chart with tooltip, a platform donut.
  - Real logic.
  - Submissions shown as content thumbnails.
  - Compact Ink wallet, Inbox, campaigns as photo cards.
- **Original mockups for craft only:** git history of ~/Documents/hypedrive-assets (`git show d1e1ded~1:brand-identity/wordmark/BRAND/ui/<file>.png`). They had richer craft but wrong concepts. Take the craft, never the concepts.

## How to evolve a page
1. **One or two signature moments per page, the rest calm.** A signature moment is one of:
   - an Ink card for the key money figure
   - a big photo or content card
   - an informative chart (only when the data deserves it)
   - an isometric illustration for a state (empty, success, shipping, waiting)
   - an editorial photo with one scrim
   Never more than two per screen. Everything else stays in the calm language of MATURITY.md.
2. **Show the real thing.** Prefer the product photo, the creator's post, the store or platform logo and the bank logo over generic icon tiles. Content is the product.
3. **Hierarchy over density.**
   - One clear title. Under it, one insight sentence that says what matters now ("Glow serum drove 31 of 52 posts…"), not a generic subtitle.
   - The primary action sits where the thing is.
4. **Brand assets are available** in ~/Downloads/hypedrive-wordmark/BRAND/ui/assets/brand/ (CSS paths: assets/brand/…):
   - isometric illustrations hypedrive-ill-{tracking,payout,approved,parcel,review,gift,growth}-{light,dark}.svg
   - parcel patterns and hexagon motifs (don't use them as busy backgrounds; the owner disliked the pattern behind the wallet)
   More illustrations are in ~/Downloads/hypedrive-wordmark/BRAND/assets/illustrations (bag, bell, calendar, camera, chat, content, inbox, lock, search, shield). Copy any you need into ui/assets/brand/.
5. **Not busy.**
   - No new blocks for their own sake.
   - Each block must earn its place with real information or the page's one job. When in doubt, remove it.
   - The owner already rejected a "Top creators" block as too much.
6. **Fundamentals are fixed.** Parcel logo, cobalt accent, Allo UI text, Bricolage display, the --hd-* tokens, no tinted borders or glows, real data from the specs (CREATOR-SPEC.md, BRAND-SPEC.md, MEDIATOR-SPEC.md), and data that agrees across screens.

## Craft checks (the owner catches every one of these)
- **Class clashes.** Global classes like `.ph`, `.av`, `.side`, `.tabs` and `.sec` already exist, so prefix all your classes. `.ph` broke a whole card.
- **Image rules.** A rule like `.x img` also hits the logos inside; use `.x > img`.
- **Explicit sizes.** Render with Zen (Firefox) via render_one.sh / render_desk.sh, and use explicit pixel sizes. Percentage heights and aspect-ratio inside flex/grid can collapse in Firefox even when Chromium is fine.
- **Flex shrink.** Flex column screens with `overflow: hidden` squash their children; set `> * { flex: none; }`.
- **Text fit.** No truncation mid-word, no lines that wrap onto two lines in small cards, no dead space in stretched cards.
- **Top bars.** Top bars take the screen background (the global rule is fixed); don't paint them white.
- **Read every PNG yourself.** Do a full-page look and a 2× crop of each block, in light and dark.

## USE THE DESIGN SYSTEM, FULLY (owner, 2026-11-26: "properly and fully use our design system")
Pages must be assembled from the kit's own components, not from new page-specific look-alikes.
- **Where the components are:**
  - Visible: ~/Downloads/hypedrive-wordmark/BRAND/ui/hypedrive-ui-kit.html (sections: form controls, fields, flow and navigation, menus/sheets/filters, feedback/states/dialogs, cards, media, conversation/lists, Campaign &amp; enrollment, Money).
  - Markup and classes: kit_build.py `kit()`, kit2.py `kit_more()`, kit3.py, kit4.py (domain: campaign card `_cc`, payout, CTAs, hold, receipt, apply sheet, tasks, submit, next step, journey, shipment, money), kit5.py (money: hero, movements, flow, statuses, blockers, methods, PAN, statements).
  - Helpers: uikit.py and uikit2.py (ic/ics icons, soc, plat, bank, av, phone, tabbar, line_chart, bar_chart, donut, spark, stat, goal, segs, ring).
- **Reuse their classes and markup:**
  - btn p/s/g + sizes, chip, badge, tabs, input/field, row/lead/tx, x-tile, switch, notice, sheet, dialog, progress, stat, and the domain components.
  - Where a kit component is scoped to its section (e.g. `.sec.dm .dm-cc`), widen the selector so it also works in screens (add a `.phone` / `.pg` scope in your layer), instead of re-drawing a copy with a new prefix.
- **Only page layout gets new CSS:** grids, spacing, page-level arrangement. A new visual component is allowed only when the kit has nothing for it. Then:
  - name it after what it is
  - note it in your report so it can be added to the kit
- **One component, one look everywhere.** The same button, chip, badge, row, card and money figure must look identical on creator, mediator and brand pages.
