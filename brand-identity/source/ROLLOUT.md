# Rollout: improve and polish every page (owner, 2026-11-26)

The owner's words: "improve and polish all apps, all pages". Their recurring complaints were: ugly, cluttered, busy, regressed to the old UI, bugs, dark cards everywhere, and "use our design system fully".

## The approved reference language ("v5")
Study these first: /tmp/hdwm/scr_v5.py and /tmp/hdwm/xv5.py. Renders are in ~/Downloads/hypedrive-wordmark/BRAND/ui/screens/14,15,16,17,07-*.png.
- WHITE page (var(--hd-surface)). Top bar on the same white, bare icons.
- An inline page title in Bricolage (var(--font-brand)), 28–30/700.
- One muted lead line that says what matters now.
- Section headings 19/650 (brand font), with an optional muted count on the right.
- Lists are SEPARATE rounded cards (1px var(--hd-edge), radius 16, 8–10 gap): 52px photo thumb or 44px x-tile, title 15.5/600, ONE muted meta line, optional chevron. No badges for normal states. Warning colour only for something due or wrong.
- Imagery first: product photo, store/platform logo, bank logo. No icon tiles that only repeat the label.
- Money: one big brand-font number, a quiet breakdown (dl rows, green only for money in), one muted sentence. WHITE, never dark/Ink cards.
- Filter/status tabs: the kit `.tabs` underline tabs with coloured 16px solid icons (ics) and a grey `.tc` count (see s_browse in scr_v5). No pill chips for status filters.
- One primary button per screen, full width in a bottom bar (`w5-bb` pattern). Row actions are quiet text links.
- Phone horizontal padding is 16 (the top bar is forced to 16, so content must match). Desktop pages use their existing shell grid.
- Calm: at most 1–2 signature moments per page (a photo card, a money figure, one illustration). Cut every block that carries no information.

## Hard rules (also read MATURITY.md, EVOLVE.md, CRITIQUE.md in /tmp/hdwm)
- Reuse kit components and classes: btn p/s/g, tabs, x-tile, plat(), soc(), bank(), ic/ics, PH photos, and the w5-* classes (you may reuse w5-* classes on your pages). Only page layout gets new CSS. Prefix any new class with your layer prefix.
- Data must agree across screens (CRITIQUE.md "Data consistency"). Never invent concepts.
- Firefox (Zen) renders: use explicit px sizes, set `> * { flex: none }` in flex columns, and use `.x > img`, never `.x img`, near logos.
- Must work in light AND dark: no hard-coded light colours.
- No dark/Ink cards. No grey slabs. No glows. No tinted borders.

## Mechanics
- Build: `cd /tmp/hdwm && flock /tmp/hdwm/.build.lock venv/bin/python -I kit_build.py` (other agents build too; always use the lock).
- Render a mobile page: `flock /tmp/hdwm/.render-<you>.lock ./render_one.sh <idx> <yourprofile> /tmp/e5/<you>-<idx>.png`. Render a desktop page: `./render_desk.sh <n> <yourprofile> <out>`. Use a profile name unique to you.
- Read EVERY render yourself at full size, and also as 2× crops (`convert x.png -crop WxH+X+Y -resize 200%`). Fix, re-render, repeat until the page is clean and calm.
- Edit ONLY the files assigned to you. Put new CSS in your assigned layer file only. Never edit kit_build.py's `_late()`, xv5.py, scr_v5.py or another agent's files.
- At the end, copy your final renders over the matching files in ~/Downloads/hypedrive-wordmark/BRAND/ui/screens/ (mobile) or BRAND/ui/hypedrive-desktop-N.png (desktop).
- Report: per page, what changed (1 line), plus any new component the kit should absorb.
