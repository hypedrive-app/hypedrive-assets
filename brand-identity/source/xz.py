# Button interaction layer (lead) — loads LAST. Hover/press are an overlay (::after) so they animate smoothly over the
# gradient finish; press = scale .97 + darker overlay + inset; hover gated to fine pointers; demo .hov/.prs mirror the real states.
XZ = r"""
.btn { position: relative; isolation: isolate; -webkit-tap-highlight-color: transparent; user-select: none; cursor: pointer;
  transition: transform 160ms cubic-bezier(.23,1,.32,1), box-shadow 160ms ease, color 120ms ease, opacity 120ms ease !important; }
.btn::after { content: ''; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; z-index: 0; background: var(--btn-ov, transparent); opacity: 0; transition: opacity 140ms ease, background-color 90ms ease; }
.btn > * { position: relative; z-index: 1; }
.btn.p, .btn.d { --btn-ov: rgba(255,255,255,.12); --btn-ov-press: rgba(0,0,0,.14); }
.btn.s { --btn-ov: rgba(16,20,38,.035); --btn-ov-press: rgba(16,20,38,.07); }
.btn.g, .btn.link { --btn-ov: color-mix(in oklab, var(--hd-fg) 6%, transparent); --btn-ov-press: color-mix(in oklab, var(--hd-fg) 10%, transparent); }
[data-theme="dark"] .btn.s { --btn-ov: rgba(255,255,255,.05); --btn-ov-press: rgba(0,0,0,.18); }
[data-theme="dark"] .btn.p, [data-theme="dark"] .btn.d { --btn-ov: rgba(255,255,255,.10); --btn-ov-press: rgba(0,0,0,.18); }

/* hover — real (fine pointers only) and the kit's .hov demo look identical */
@media (hover: hover) and (pointer: fine) { .btn.btn:hover:not(.dis):not([disabled]):not(:active)::after { opacity: 1; } }
.btn.btn.hov:not(.dis):not([disabled])::after { opacity: 1; }

/* press — one motion everywhere: scale .97, 90ms in / 160ms out, darker overlay + inner shadow */
.btn.btn:active:not(.dis):not([disabled]), .btn.btn.prs:not(.dis):not([disabled]) { transform: scale(.97) !important; transition-duration: 90ms !important; }
.btn.btn:active:not(.dis):not([disabled])::after, .btn.btn.prs:not(.dis):not([disabled])::after { opacity: 1; background: var(--btn-ov-press, transparent); }
.btn.p:active:not(.dis):not([disabled]), .btn.p.prs:not(.dis):not([disabled]), .btn.d:active:not(.dis):not([disabled]), .btn.d.prs:not(.dis):not([disabled]) { box-shadow: inset 0 1px 3px rgba(0,0,0,.28) !important; }
.btn.s:active:not(.dis):not([disabled]), .btn.s.prs:not(.dis):not([disabled]) { box-shadow: inset 0 1px 2px rgba(16,20,38,.12) !important; }

/* keep the resting fill on hover/press so the overlay is the only change (no gradient snap) */
.btn.p.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-accent) 93%, #fff) 0%, var(--hd-accent) 55%, color-mix(in oklab, var(--hd-accent) 94%, #000) 100%) !important; }
.btn.d.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 88%, var(--hd-danger-strong, #a3300a)) 0%, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 62%, var(--hd-danger-strong, #a3300a)) 100%) !important; }
[data-theme="dark"] .btn.d.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid) 94%, #fff) 0%, var(--hd-danger-solid) 100%) !important; }
.btn.s.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: linear-gradient(180deg, #fff 0%, #fbfbfc 100%) !important; }
[data-theme="dark"] .btn.s.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: linear-gradient(180deg, #2a2d35 0%, #23262d 100%) !important; }
.btn.g.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]) { background: transparent !important; }

/* focus — keyboard only, same ring as the .foc demo */
.btn:focus { outline: none; }
.btn.btn:focus-visible:not(.dis):not([disabled]) { outline: none; box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }

/* disabled — no motion, no overlay */
.btn.dis, .btn[disabled] { cursor: not-allowed; transform: none !important; }
.btn.dis::after, .btn[disabled]::after { display: none; }

@media (prefers-reduced-motion: reduce) { .btn, .btn::after { transition: opacity 120ms ease !important; } .btn.btn:active, .btn.btn.prs { transform: none !important; } }

/* owner: no tinted glows/rings on fields — error = solid 1px danger edge, focus = 1.5px accent edge; no halos */
.input.err, .n-fgrid .input.err, textarea.err, .input.err:focus-within { box-shadow: none !important; border-color: var(--hd-danger) !important; }
.input.foc, .input:focus, .input:focus-within, textarea:focus, .input.focus { box-shadow: inset 0 0 0 0.5px var(--hd-accent) !important; border-color: var(--hd-accent) !important; }
.input.foc.err, .input.err:focus-within { box-shadow: inset 0 0 0 0.5px var(--hd-danger) !important; }

/* swipe actions: solid action colours with white glyph + label (iOS convention); no tints */
.n-swa .a { color: #fff !important; font-weight: 600 !important; }
.n-swa .a .ic, .n-swa .a svg { color: #fff !important; }
.n-swa .a.ok { background: var(--hd-success-solid, #0a8a4a) !important; }
.n-swa .a.mu { background: #5d6270 !important; }
.n-swa .a.dg { background: var(--hd-danger-solid, #c93d00) !important; }

/* composer send: solid paper-plane twin, optically centred (the glyph points up-right) */
.t-comp .btn.t-send svg { width: 20px; height: 20px; transform: translate(-1px, 1px); }
.t-comp .btn.t-send[disabled] svg { opacity: .9; }

/* platform favicons keep their brand colour wherever they identify a platform */
.n-cc .n-plat svg, .n-ch .n-plat svg, [data-theme="dark"] .n-cc .n-plat svg, [data-theme="dark"] .n-ch .n-plat svg { filter: none !important; opacity: 1 !important; }

.m-lr small svg { vertical-align: -2px; margin-right: 5px; }
.input > .bankl { margin-right: 10px; flex: none; }
.input .addon svg { display: block; }

.n-sw .n-swa .a, .n-sw .n-swa .a *, .n-swa span.a, .n-swa span.a > * { color: #fff !important; -webkit-text-fill-color: #fff; }
.n-sw .n-swa .a { font-size: 12.5px !important; gap: 4px !important; }

.n-swp { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; flex: none; }

/* dialogs v3 — one calm pattern: UI-font title, consequence in bold body, hairline footer, 36px actions */
.dialog.n-dlg2 { width: 420px; max-width: 100%; padding: 0 !important; border-radius: 16px !important; overflow: hidden; display: block !important; }
.dialog.n-dlg2.sm { width: 380px; }
.n-dlg2 .d2b { padding: 20px 20px 18px; display: flex; flex-direction: column; }
.n-dlg2 .d2t { font: 600 16px/22px var(--font-ui); letter-spacing: -.01em; color: var(--hd-fg); }
.n-dlg2 .d2p { margin: 6px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); text-wrap: pretty; } .n-dlg2 .d2p b { color: var(--hd-fg); font-weight: 600; }
.n-dlg2 .d2l { margin-top: 16px; font-size: 13.5px; font-weight: 500; color: var(--hd-fg-muted); } .n-dlg2 .d2l b { color: var(--hd-fg); font-weight: 600; }
.n-dlg2 .d2i { margin-top: 6px; height: 40px !important; min-height: 0 !important; font-size: 14.5px !important; border-radius: 10px !important; }
.n-dlg2 .d2f { display: flex; justify-content: flex-end; gap: 8px; padding: 12px 16px; border-top: 1px solid var(--hd-edge); }
.n-dlg2 .d2f .btn { height: 36px !important; min-height: 0 !important; padding: 0 14px !important; font-size: 14px !important; border-radius: 10px !important; }
/* danger = a true red (was reading orange) */
:root { --btn-red: #d92d20; --btn-red-strong: #b42318; --btn-red-press: #9b1c14; }
[data-theme="dark"] { --btn-red: #e5484d; --btn-red-strong: #cd2b31; --btn-red-press: #b42318; }
.btn.d:not(.dis):not([disabled]), .btn.d.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]), [data-theme="dark"] .btn.d.btn:is(.hov,.prs,:hover,:active):not(.dis):not([disabled]), [data-theme="dark"] .btn.d:not(.dis):not([disabled]) {
  background: linear-gradient(180deg, color-mix(in oklab, var(--btn-red) 94%, #fff) 0%, var(--btn-red) 100%) !important; }
.btn.d.btn:is(.prs,:active):not(.dis):not([disabled]) { background: var(--btn-red-strong) !important; }

.dialog.n-dlg2 { align-self: flex-start !important; margin-left: 0 !important; margin-right: auto !important; }

/* sheet demo: real page behind a light scrim instead of grey placeholder blocks */
.sd-ghost.sd-photo { padding: 0 !important; display: block !important; background: var(--hd-surface) !important; }
.sd-ghost.sd-photo > i { display: none !important; }
.sd-photo img { display: block; width: 100%; height: 190px; object-fit: cover; }
.sd-photo .sd-pt { padding: 14px 16px; display: flex; flex-direction: column; gap: 2px; } .sd-photo .sd-pt b { font-size: 17px; font-weight: 650; } .sd-photo .sd-pt span { font-size: 13px; color: var(--hd-fg-muted); }
.sheetdemo .scrim { background: rgba(10,12,18,.34) !important; }
.sd-sheet { border-radius: 24px 24px 0 0 !important; }
.sd-sheet .t-h2 { font: 650 19px/24px var(--font-brand) !important; }
.btn.sd-cta { margin-top: 10px; height: 48px !important; min-height: 0 !important; }

/* empty state v2: centred, compact, one illustration, one next step, quiet link */
.card.eb-empty2 { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 28px 24px 24px !important; gap: 0; }
.eb-empty2 img { width: 96px; height: 96px; object-fit: contain; margin-bottom: 14px; }
.eb-empty2 .e2t { font: 600 17px/22px var(--font-ui); color: var(--hd-fg); }
.eb-empty2 .e2p { margin: 6px 0 0; max-width: 320px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); text-wrap: pretty; }
.eb-empty2 .e2b { margin-top: 18px; height: 40px !important; min-height: 0 !important; gap: 8px; }
.eb-empty2 .e2l { margin-top: 10px; font-size: 13.5px; font-weight: 560; color: var(--hd-accent-strong, var(--hd-link)); cursor: pointer; }

/* progress: one family. Labelled bars 6px, segmented slots = discrete 6px cells with 3px gaps (slots are countable) */
.sec .segs, .segs { display: flex !important; gap: 3px !important; height: 6px !important; background: none !important; overflow: visible !important; border-radius: 0 !important; }
.sec .segs i, .segs i { flex: 1; height: 6px !important; border-radius: 3px !important; background: var(--hd-track) !important; }
.sec .segs i.on, .segs i.on { background: var(--hd-accent) !important; }
[data-theme="dark"] .segs i.on { background: var(--hd-chart, var(--hd-accent)) !important; }
.bar, .sx .bar { height: 6px !important; border-radius: 3px !important; } .bar > i, .bar > b { border-radius: 3px !important; }
.stackbar, .bar.stack { height: 6px !important; gap: 2px; }
/* upload rows: progress hairline clipped by the row's own radius */
.u-row { position: relative !important; overflow: hidden !important; }
.u-row .u-bar { height: 2px !important; left: 0; bottom: 0; border-radius: 0 !important; }
/* banner with action: white icon tile (no solid slab), secondary action */
.banner .bi { background: var(--hd-surface) !important; color: var(--hd-accent) !important; border: 1px solid var(--hd-edge) !important; box-shadow: 0 1px 2px rgba(16,20,38,.06) !important; }
[data-theme="dark"] .banner .bi { background: var(--hd-surface-raised) !important; color: var(--hd-link) !important; }
.banner .btn.p.sm { background: linear-gradient(180deg, #fff 0%, #fbfbfc 100%) !important; color: var(--hd-fg) !important; box-shadow: inset 0 0 0 1px var(--hd-edge), inset 0 -1px 0 rgba(16,20,38,.08), 0 1px 1px rgba(16,20,38,.07) !important; height: 34px !important; min-height: 0 !important; }
[data-theme="dark"] .banner .btn.p.sm { background: linear-gradient(180deg, #2a2d35 0%, #23262d 100%) !important; color: var(--hd-fg) !important; }

/* form section layout v2: settings anatomy — 260 label column, fields in a 2-up grid (max 640), 40px fields, help 6px under */
.card.n-form { padding: 0 !important; }
.n-form .n-fs { display: grid !important; grid-template-columns: 260px minmax(0, 640px) !important; gap: 40px !important; padding: 24px 28px !important; border-bottom: 1px solid var(--hd-edge); align-items: start; }
.n-form .n-fsh .t-h3 { font: 600 15px/20px var(--font-ui) !important; margin: 0; }
.n-form .n-fsh p { margin: 4px 0 0 !important; font-size: 13.5px !important; line-height: 19px; max-width: 240px; }
.n-form .n-fgrid { display: grid !important; grid-template-columns: repeat(2, minmax(0, 1fr)) !important; gap: 20px 16px !important; }
.n-form .n-fgrid .field { display: flex; flex-direction: column; gap: 6px; margin: 0 !important; }
.n-form .n-fgrid .labrow { display: flex; justify-content: space-between; align-items: baseline; margin: 0 !important; }
.n-form .n-fgrid .labrow label { font-size: 13.5px !important; font-weight: 600; }
.n-form .n-fgrid .labrow span { font-size: 12.5px !important; color: var(--hd-fg-subtle); }
.n-form .n-fgrid .input { height: 40px !important; font-size: 14.5px !important; padding: 0 12px !important; border-radius: 10px !important; }
.n-form .n-fgrid .help { margin: 0 !important; font-size: 12.5px !important; line-height: 17px !important; }
.n-form .n-fgrid .input.dis { background: var(--hd-bg-subtle) !important; }
.n-form .n-fgrid .input .badge { height: 22px; font-size: 12px; }
.n-form .n-togl { min-height: 40px !important; }
.n-form .n-ffoot { padding: 14px 28px !important; display: flex; align-items: center; gap: 8px; }
.n-form .n-ffoot .btn { height: 36px !important; min-height: 0 !important; padding: 0 14px !important; font-size: 14px !important; }
.n-form .n-ffoot .t-small { font-size: 13px; }

/* small drop cards: photo flush to the card edges (no plate), clear earn line, slots left */
.card.eb-near2 { padding: 0 !important; overflow: hidden; display: flex; flex-direction: column; }
.eb-near2 > img { display: block; width: 100%; aspect-ratio: 4 / 3; height: auto; object-fit: cover; border-radius: 0; border-bottom: 1px solid var(--hd-edge); }
.eb-near2 .en-b { padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 2px; }
.eb-near2 .en-b > b { font-size: 14px; font-weight: 600; line-height: 19px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.eb-near2 .en-b > span { font-size: 13px; color: var(--hd-fg-muted); } .eb-near2 .en-b > span b { color: var(--hd-fg); font-weight: 600; }
.eb-near2 .en-b > small { font-size: 12.5px; color: var(--hd-fg-subtle); }

/* table v2: photo avatars, status as glyph + text (no pills), quiet header, 52 rows */
.eb-tbl th { font-size: 12.5px !important; font-weight: 560 !important; color: var(--hd-fg-subtle) !important; background: none !important; height: 40px; padding: 0 16px !important; border-bottom: 1px solid var(--hd-edge) !important; text-transform: none; letter-spacing: 0; }
.eb-tbl td { height: 52px; padding: 0 16px !important; font-size: 14px; border-bottom: 1px solid var(--hd-edge) !important; }
.eb-tbl tr:last-child td { border-bottom: 0 !important; }
.eb-tbl .tcell { display: flex; align-items: center; gap: 10px; } .eb-tbl .tcell b { font-weight: 560; }
.eb-tbl .tav { width: 28px; height: 28px; border-radius: 50%; object-fit: cover; flex: none; }
.eb-tbl .tst { display: inline-flex; align-items: center; gap: 6px; font-size: 13.5px; font-weight: 500; color: var(--hd-fg); }
.eb-tbl .tst.success svg { color: var(--hd-success, #0a8a4a); } .eb-tbl .tst.warning svg { color: var(--hd-warning-solid, #c27a00); }
.eb-tbl .tst.danger svg { color: var(--hd-danger-solid, #d92d20); } .eb-tbl .tst.neutral svg { color: var(--hd-fg-muted); }
.eb-tbl .tpay { text-align: right; font-weight: 600; } .eb-tbl .tpay.nil { color: var(--hd-fg-subtle); font-weight: 400; }

/* spinner v2: one comet arc (conic sweep + ring cut-out), no grey track; same in buttons, rows, banners */
.n-spin, .btn .spin { border: 0 !important; border-radius: 50%; color: var(--hd-accent); --sw: 2.5px;
  background: conic-gradient(from 0deg, transparent 0 8%, color-mix(in oklab, currentColor 30%, transparent) 30%, currentColor 92%, transparent 92.1%) !important;
  -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - var(--sw) - .5px), #000 calc(100% - var(--sw))); mask: radial-gradient(farthest-side, transparent calc(100% - var(--sw) - .5px), #000 calc(100% - var(--sw)));
  animation: spin 720ms linear infinite; display: inline-block; flex: none; }
.n-spin { width: 24px; height: 24px; } .n-spin.sm, .btn .spin, .btn .n-spin { width: 16px !important; height: 16px !important; --sw: 2px; } .n-spin.lg { width: 40px; height: 40px; --sw: 3.5px; }
.btn .n-spin, .btn .spin, .n-banner .n-spin { color: currentColor !important; }
[data-theme="dark"] .n-spin { color: var(--hd-link, var(--hd-accent)); }
.n-spins { align-items: center !important; gap: 40px !important; } .n-spins > div { height: 64px; justify-content: space-between !important; } .n-spins small { font-size: 12px; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
/* loading rows: centred spinner slot, calm text, white Cancel, hairline progress */
.row.n-lr { align-items: center !important; gap: 12px !important; padding: 12px 14px !important; min-height: 64px; }
.row.n-lr > .n-spin { margin: 0 !important; width: 20px; height: 20px; --sw: 2.25px; }
.row.n-lr .tx b { font-size: 14.5px; font-weight: 600; } .row.n-lr .tx small { font-size: 13px; color: var(--hd-fg-muted); }
.row.n-lr .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 12px !important; font-size: 13.5px !important; }
.n-lr .tape.n-t4 { height: 3px !important; margin-top: 8px; border-radius: 3px; background: var(--hd-track); overflow: hidden; } .n-lr .tape.n-t4 i { border-radius: 3px; background: var(--hd-accent); }
.n-lmore { display: flex; align-items: center; justify-content: center; gap: 8px; height: 36px; } .n-lmore .t-small { font-size: 13px; }

.n-spins > div { height: auto !important; justify-content: flex-start !important; gap: 10px !important; }
.n-spins > div > .n-spin.sm { margin: 12px 0; } .n-spins > div > .n-spin:not(.sm):not(.lg) { margin: 8px 0; } .n-spins > div > .n-spin.lg { margin: 0; }

/* profile v2: root-tab title, identity + stats in one card, bank logo, log out as its own row, tab bar always visible */
.phone:has(.xz-prof) .scr { display: flex !important; flex-direction: column !important; }
.phone:has(.xz-prof) .body.xz-prof { flex: 1 1 auto; min-height: 0; overflow: hidden; padding-bottom: 8px !important; gap: 12px !important; display: flex; flex-direction: column; }
.phone:has(.xz-prof) .tabbar { flex: none; margin-top: auto; }
.xz-ptop { height: 52px !important; } .xz-ptop .ttl { font: 700 28px/34px var(--font-brand) !important; letter-spacing: -.02em; color: var(--hd-fg); }
.xz-idc { background: var(--hd-surface-raised, #1b1d23); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 14px 14px 0; }
.xz-idc .xm3-id { display: flex; align-items: center; gap: 12px; margin: 0 !important; }
.xz-idc .xm3-id img { width: 52px !important; height: 52px !important; border-radius: 50%; object-fit: cover; }
.xz-idc .xm3-id > div { flex: 1; min-width: 0; } .xz-idc .xm3-nm { font: 650 17px/22px var(--font-ui) !important; display: flex; align-items: center; gap: 4px; } .xz-idc .xm3-id span { font-size: 13px; color: var(--hd-fg-muted); }
.xz-idc .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 12px !important; font-size: 13.5px !important; }
.xz-idc .xm3-stats { display: grid !important; grid-template-columns: repeat(3, 1fr); margin: 14px -14px 0 !important; border-top: 1px solid var(--hd-edge); padding: 0 !important; gap: 0 !important; }
.xz-idc .xm3-stats > div { padding: 10px 14px 12px; display: flex; flex-direction: column; gap: 1px; } .xz-idc .xm3-stats > div + div { border-left: 1px solid var(--hd-edge); }
.xz-idc .xm3-stats b { font-size: 17px !important; font-weight: 650; } .xz-idc .xm3-stats small { font-size: 12.5px !important; color: var(--hd-fg-muted); }
.xz-prof .xm3-grp { margin: 0 !important; }
.xz-prof .xm3-gi { min-height: 48px !important; } .xz-prof .xm3-gi b { font-size: 15px !important; font-weight: 500 !important; }
.xz-bk { display: inline-flex !important; align-items: center; gap: 6px; } .xz-bk .bankl { border-radius: 4px; }
.xz-outg .xm3-out { display: flex; align-items: center; gap: 12px; height: 48px; padding: 0 14px; margin: 0 !important; color: #ff8a80 !important; }
.xz-outg .xm3-out b { font-size: 15px; font-weight: 500; color: #ff8a80 !important; } .xz-outg .xm3-out .ic { color: #ff8a80 !important; }

/* welcome v2: mosaic bleeds off top + sides, equal tiles, offset columns, one full-width fade; logo sits on a top scrim */
.phone .xm1-wel .xm1-mos { top: -30px !important; left: -28px !important; right: -28px !important; height: 520px !important; padding: 0 !important; gap: 10px !important; overflow: hidden; }
.phone .xm1-wel .xm1-mos div { gap: 10px !important; margin-top: 0 !important; }
.phone .xm1-wel .xm1-mos div:nth-child(1) { margin-top: -20px !important; } .phone .xm1-wel .xm1-mos div:nth-child(2) { margin-top: 36px !important; } .phone .xm1-wel .xm1-mos div:nth-child(3) { margin-top: -60px !important; }
.phone .xm1-wel .xm1-mos img { height: 168px !important; border-radius: 18px !important; opacity: .92; }
.phone .xm1-wel .xm1-fade { top: 0 !important; height: 520px !important; background:
  linear-gradient(180deg, rgba(13,14,18,.78) 0px, rgba(13,14,18,0) 110px, rgba(13,14,18,0) 250px, rgba(13,14,18,.86) 400px, #0d0e12 480px) !important; z-index: 1; }
.phone .xm1-wel .xm1-logo { position: relative; z-index: 2; }
.phone .xm1-wel .xm1-copy { z-index: 2; }
.phone .xm1-wel .xm1-h { font-size: 44px !important; line-height: 46px !important; }

.phone .xm1-wel .xm1-fade { background: linear-gradient(180deg, rgba(13,14,18,.92) 0px, rgba(13,14,18,.55) 70px, rgba(13,14,18,0) 140px, rgba(13,14,18,0) 250px, rgba(13,14,18,.86) 400px, #0d0e12 480px) !important; }

/* success: content column keeps 20px side padding; payout card never overflows */
.phone .body.xm3-succ { padding-left: 20px !important; padding-right: 20px !important; box-sizing: border-box; }
.phone .xm3-succ .xy-pay { width: 100% !important; max-width: 100% !important; margin-left: 0 !important; margin-right: 0 !important; align-self: stretch !important; box-sizing: border-box !important; }
/* person avatars are circles everywhere (a snap turned some into rounded squares) */
.phone .xm3-id img, .phone .xz-idc img, .tav, .n-swp, .xa-photo { border-radius: 50% !important; }

/* global guard: nothing in a phone screen spills past its padding */
.phone .scr .body > *, .phone .scr .sheet > *, .phone .scr .body .stack > * { max-width: 100%; box-sizing: border-box; }
.phone .scr .radio.on { background: var(--hd-accent) !important; border-color: var(--hd-accent) !important; box-shadow: inset 0 0 0 6px var(--hd-accent), inset 0 0 0 10px #fff !important; }

/* bank/brand logo tiles: logo exactly centred, 56% of the tile, no stray padding/line-height */
.x-tile.bankt { display: grid !important; place-items: center !important; padding: 0 !important; line-height: 0 !important; font-size: 0 !important; overflow: hidden; }
.x-tile.bankt > .bankl, .x-tile.bankt > img { display: block !important; width: 56% !important; height: 56% !important; margin: 0 !important; vertical-align: 0 !important; object-fit: contain; border-radius: 3px; }

.x-tile.bankt > .bankl, .x-tile.bankt > img { width: 70% !important; height: 70% !important; }

/* empty search: a quiet inline result, not a hero — tile + text + small action in one row card */
.phone .xm3-nil.xz-nil { display: flex !important; flex-direction: row !important; align-items: center !important; text-align: left !important; gap: 12px !important; padding: 14px !important; margin: 4px 0 8px !important;
  background: #fff; border: 1px solid var(--warm-edge, var(--hd-edge)); border-radius: 16px; }
.xz-nil .xz-nt { width: 40px !important; height: 40px !important; flex: none; display: grid !important; place-items: center; color: var(--hd-fg-muted); border-radius: 12px !important; }
.xz-nil .xz-ntx { flex: 1; min-width: 0; } .xz-nil .xz-ntx b { display: block; font: 600 15px/20px var(--font-ui); letter-spacing: -.01em; color: var(--hd-fg); }
.xz-nil .xz-ntx p { margin: 2px 0 0 !important; font-size: 13px !important; line-height: 18px !important; color: var(--hd-fg-muted); }
.xz-nil .btn.s.sm { flex: none; height: 34px !important; min-height: 0 !important; padding: 0 12px !important; gap: 6px; font-size: 13.5px !important; margin: 0 !important; }

.phone .xm3-nil.xz-nil2 { display: block !important; text-align: left !important; padding: 6px 2px 4px !important; margin: 0 0 6px !important; background: none !important; border: 0 !important; }
.xz-nil2 > b { display: block; font: 600 17px/22px var(--font-ui); letter-spacing: -.015em; color: var(--hd-fg); }
.xz-nil2 > p { margin: 4px 0 0 !important; font-size: 14px !important; line-height: 20px !important; color: var(--hd-fg-muted); }
.xz-nil2 .xz-al { display: inline-flex; align-items: center; gap: 4px; margin-left: 2px; color: var(--hd-accent-strong, var(--hd-link)); font-weight: 600; white-space: nowrap; cursor: pointer; } .xz-nil2 .xz-al .ic { width: 15px; height: 15px; }

/* bottom action bars: same surface as the screen, all the way to the bottom edge (no white band + warm strip) */
.phone .scr[data-theme="light"] :is(.cta, .xm1-bar, .xm3-cta, [class*="xm2-"][class*="bar"], [class*="xw1-"][class*="bar"], [class*="xw2-"][class*="bar"]) { background: var(--warm, #f7f7f8) !important; box-shadow: none !important; }
.phone .scr[data-theme="light"] :is(.cta, .xm1-bar, .xm3-cta) { border-top: 1px solid var(--warm-edge, rgba(16,20,38,.09)) !important; }
.phone .scr[data-theme="light"] .home-ind { background: var(--warm, #f7f7f8) !important; }
.phone .scr[data-theme="light"]:has(.tabbar) .home-ind { background: rgba(247,247,248,.94) !important; }
/* bottom-bar buttons: one height (48), consistent radius */
.phone .scr :is(.cta, .xm1-bar, .xm3-cta) .btn { height: 48px !important; min-height: 0 !important; border-radius: 12px !important; }

/* campaign card: photo flush to the card's left/top/bottom edges, clipped by the card radius — no inner rounding, no inset */
.panel.x-camp2 { overflow: hidden !important; padding: 0 !important; align-items: stretch !important; }
.panel.x-camp2 > img { border-radius: 0 !important; margin: 0 !important; height: 100% !important; min-height: 148px; object-fit: cover; align-self: stretch !important; border: 0 !important; border-right: 1px solid var(--hd-edge) !important; box-shadow: none !important; }
.x-camp2 .cbody { padding: 16px 18px !important; }

html body .sec .panel.x-camp2 > img.x, html body .sec .panel.x-camp2 > img:not(#zz) { border-radius: 0 !important; -webkit-mask: none !important; mask: none !important; clip-path: none !important; }

/* avatar upload: every avatar state is a true circle; ring sits concentric */
.n-av, .n-av img, .n-av.up, .n-av.up img { border-radius: 50% !important; -webkit-mask: none !important; mask: none !important; clip-path: none !important; }
.n-av { position: relative; width: 64px !important; height: 64px !important; flex: none; }
.n-av img { width: 100% !important; height: 100% !important; object-fit: cover; display: block; }
.n-av.up img { opacity: .55; }
.n-av svg, .n-av .ring, .n-av > :not(img) { position: absolute !important; inset: 0 !important; width: 64px !important; height: 64px !important; }
.n-avt .btn, .n-avt button { height: 32px !important; min-height: 0 !important; }

img.sfav { display: inline-block; width: 14px; height: 14px; border-radius: 3px !important; vertical-align: -2px; margin-right: 4px; }

/* button heights: 44 everywhere (lg included); 48 only for a phone screen's bottom action bar */
html body .btn.lg:not(.sm), html body .btn.block:not(.sm), .btn.sd-cta { height: 44px !important; min-height: 0 !important; font-size: 15px !important; }
html body .phone :is(.cp-bar, .jf-act, .cta, .xm1-bar, .xm3-cta, .xy-bar) .btn:not(.sm) { height: 48px !important; }
html body .btn.prs:not(.sm) { height: 44px !important; }

/* progress v3: three calm bars, one meaning each */
.pg3 { display: flex; flex-direction: column; gap: 18px; }
.pg3 .barlab { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px; font-size: 14px; } .pg3 .barlab b { font-weight: 600; } .pg3 .barlab span { color: var(--hd-fg-muted); font-size: 13.5px; } .pg3 .barlab span b { color: var(--hd-fg); }
.pg3-bar { height: 6px; border-radius: 3px; background: var(--hd-track); overflow: hidden; } .pg3-bar i { display: block; height: 100%; border-radius: 3px; background: var(--hd-accent); }
.pg3-i > small { display: block; margin-top: 6px; font-size: 12.5px; color: var(--hd-fg-subtle); }
.pg3-stack { display: flex; gap: 2px; height: 6px; border-radius: 3px; overflow: hidden; } .pg3-stack i { display: block; height: 100%; }
.pg3 i.pgpd { background: var(--hd-success, #0a8a4a); } .pg3 i.pgrv { background: var(--hd-accent); } .pg3 i.pgfx { background: var(--hd-warning-solid, #c27a00); }
.pg3-leg { display: flex; gap: 14px; margin-top: 8px; font-size: 12.5px; color: var(--hd-fg-muted); } .pg3-leg i { display: inline-block; width: 8px; height: 8px; border-radius: 2px; margin-right: 6px; } .pg3-leg b { color: var(--hd-fg); font-weight: 600; }
.pg3-seg { display: flex; gap: 4px; } .pg3-seg i { flex: 1; height: 6px; border-radius: 3px; background: var(--hd-track); } .pg3-seg i.on { background: var(--hd-accent); }
"""
