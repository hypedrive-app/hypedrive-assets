# Lead fixes layer (owned by the lead). Appended absolutely last.
XLEAD = r"""
/* tints must read on any surface: selected chip / info badge = 16% accent into the surface, strong text */
.chip.on { background: var(--hd-accent-subtle) !important; color: var(--hd-info-strong) !important; }
[data-theme="dark"] .chip.on { background: color-mix(in oklab, var(--hd-accent) 30%, var(--hd-surface)) !important; color: #dbe6ff !important; }
.badge.info { background: var(--hd-info-subtle) !important; }
.badge.success { background: var(--hd-success-subtle) !important; }
.badge.warning { background: var(--hd-warning-subtle) !important; }
.badge.danger { background: var(--hd-danger-subtle) !important; }
.tbl tr.sel-row td { background: color-mix(in oklab, var(--hd-accent) 9%, var(--hd-surface)) !important; }
/* the -subtle roles themselves are deepened so EVERY tinted surface reads (alerts, tiles, counts, ranges, selected states) */
:root, [data-theme="light"] {
  --hd-accent-subtle: color-mix(in oklab, #2d58ee 18%, #ffffff);
  --hd-info-subtle: color-mix(in oklab, #2d58ee 18%, #ffffff);
  --hd-success-subtle: color-mix(in oklab, #0a8a5c 22%, #ffffff);
  --hd-warning-subtle: color-mix(in oklab, #ffc83c 48%, #ffffff);
  --hd-danger-subtle: color-mix(in oklab, #e04f10 19%, #ffffff);
}
[data-theme="dark"] {
  --hd-accent-subtle: color-mix(in oklab, #2d58ee 30%, #16181d);
  --hd-info-subtle: color-mix(in oklab, #2d58ee 30%, #16181d);
  --hd-success-subtle: color-mix(in oklab, #0a8a5c 32%, #16181d);
  --hd-warning-subtle: color-mix(in oklab, #ffc83c 22%, #16181d);
  --hd-danger-subtle: color-mix(in oklab, #e04f10 28%, #16181d);
}
/* swipe rows, iOS-true: one clipped container, actions flush and full-height behind, the row slides with a soft edge */
.n-swr { border: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; border-radius: 14px !important; overflow: hidden !important; background: var(--hd-surface); }
.n-swr > .row.n-sr { border: 0 !important; border-radius: 0 !important; box-shadow: none !important; margin: 0 !important; position: relative; z-index: 1; background: var(--hd-surface) !important; }
.n-swa { gap: 0 !important; } .n-swa .a { width: 76px !important; border-radius: 0 !important; font-size: 12px; }
.n-sr.off { transform: translateX(76px) !important; box-shadow: -6px 0 12px -6px rgba(16,20,38,.22) !important; }
.n-sr.left { transform: translateX(-152px) !important; box-shadow: 6px 0 12px -6px rgba(16,20,38,.22) !important; }
.n-sw { gap: 10px !important; }
/* device demos never exceed their column; share sheet = header + preview + apps + grouped actions (iOS) */
.n-dev { width: 100%; max-width: 420px; min-width: 0; margin-inline: auto; box-sizing: border-box; }
.n-dev img { max-width: 100%; }
.n-shs { gap: 12px !important; padding: 8px 16px 20px !important; }
.n-shh { display: flex; align-items: center; justify-content: space-between; } .n-shx { width: 32px !important; height: 32px !important; background: var(--hd-control) !important; color: var(--hd-fg-muted); display: grid; place-items: center; border-radius: 50%; }
.n-shp { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; min-width: 0; } .n-shp > div { min-width: 0; } .n-shp span { display: block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-apps { grid-template-columns: repeat(5, minmax(0, 1fr)) !important; } .n-app { width: 52px !important; height: 52px !important; border-radius: 14px !important; }
.n-shg { border-radius: 14px; overflow: hidden; } .n-shg .gi { display: flex; align-items: center; gap: 12px; padding: 0 14px; height: 48px; border-top: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.n-shg .gi:first-child { border-top: 0; } .n-shg .gi b { font-weight: 560; font-size: 15px; } .n-shg .gi .meta { margin-left: auto; font-size: 13px; color: var(--hd-fg-subtle); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }
.n-shg .gi .ic { color: var(--hd-fg-muted); flex: none; }
.n-shg .gi { border: 0 !important; box-shadow: none !important; border-top: 1px solid var(--hd-edge, rgba(16,20,38,.12)) !important; } .n-shg .gi:first-child { border-top: 0 !important; }
/* dividers shown where they do a job */
.n-dvx { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.n-dvc { background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.16)); border-radius: 16px; padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 10px; min-width: 0; }
.n-dvt { font-size: 12px; font-weight: 600; color: var(--hd-fg-muted); }
.n-dvl { margin: 0 -16px; } .n-dvi { display: flex; align-items: center; gap: 12px; height: 48px; padding: 0 16px; position: relative; } .n-dvi .ic { color: var(--hd-fg-muted); flex: none; }
.n-dvi b { font-size: 15px; font-weight: 560; } .n-dvi .m { margin-left: auto; font-size: 13px; color: var(--hd-fg-subtle); } .n-dvi + .n-dvi::before { content: ''; position: absolute; top: 0; left: 48px; right: 0; height: 1px; background: var(--hd-edge, rgba(16,20,38,.12)); }
.n-dvsign { display: flex; flex-direction: column; gap: 12px; }
.n-hrl { display: flex; align-items: center; gap: 12px; font-size: 13px; color: var(--hd-fg-subtle); } .n-hrl i { flex: 1; height: 1px; background: var(--hd-edge, rgba(16,20,38,.12)); } .n-hrl.left span { font-weight: 600; color: var(--hd-fg-muted); }
.n-dvfeed { display: flex; flex-direction: column; gap: 8px; } .n-dvr { display: flex; justify-content: space-between; align-items: center; height: 36px; font-size: 14px; } .n-dvr b { font-weight: 560; } .n-dvr .num { color: var(--hd-success-strong); font-weight: 600; } .n-dvr .m { color: var(--hd-fg-subtle); font-size: 13px; }
.n-dvprof { display: flex; gap: 12px; align-items: center; } .n-dvprof img { width: 48px; height: 48px; border-radius: 50%; object-fit: cover; } .n-dvprof > div > b { display: flex; align-items: center; gap: 4px; font-size: 15px; }
.n-vrow { display: flex; align-items: center; gap: 10px; font-size: 13px; color: var(--hd-fg-muted); margin-top: 4px; } .n-vrow b { color: var(--hd-fg); font-weight: 600; } .n-vr { width: 1px; height: 14px; background: var(--hd-edge, rgba(16,20,38,.16)); }
.n-dvbreak { margin: 0 -16px -16px; border-top: 1px solid var(--hd-edge, rgba(16,20,38,.12)); } .n-dvbreak .n-dvr { padding: 0 16px; height: 44px; } .n-band { height: 8px; background: var(--hd-bg-subtle); border-top: 1px solid var(--hd-edge, rgba(16,20,38,.10)); border-bottom: 1px solid var(--hd-edge, rgba(16,20,38,.10)); }
.n-vrow span { white-space: nowrap; } .n-vrow { flex-wrap: nowrap; }
/* icon containers: white tile, crisp hairline, two-layer soft shadow; the icon carries the meaning colour */
.x-tile, .n-app, .n-shx { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)) !important;
  box-shadow: 0 1px 1px rgba(16,20,38,.05), 0 3px 8px -2px rgba(16,20,38,.08) !important; }
.x-tile.cobalt { color: var(--hd-accent) !important; } .x-tile.mint { color: var(--hd-success) !important; } .x-tile.marigold { color: #c98a00 !important; } .x-tile.vermilion { color: var(--hd-danger) !important; }
[data-theme="dark"] .x-tile, [data-theme="dark"] .n-app, [data-theme="dark"] .n-shx { background: var(--hd-surface-raised) !important; box-shadow: 0 1px 2px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.06) !important; }
[data-theme="dark"] .x-tile.marigold { color: var(--hd-tone-marigold) !important; }
.x-plat { display: inline-flex; align-items: center; gap: 5px; vertical-align: middle; } .x-plat .plat, .x-plat .ic { border-radius: 4px; flex: none; }
/* ===== wallet redesign ===== */
.w-hero { border-radius: 24px; background: var(--hd-inverse); color: var(--hd-inverse-fg); padding: 18px 18px 16px; display: flex; flex-direction: column; gap: 10px; }
.w-hero small { font-size: 13px; color: color-mix(in oklab, var(--hd-inverse-fg) 68%, transparent); }
.w-big { font-family: var(--font-brand); font-size: 46px; line-height: 48px; font-weight: 650; letter-spacing: -0.04em; margin-top: -4px; } .w-big span { font-weight: 500; margin-right: 1px; }
.w-split { display: flex; gap: 3px; height: 8px; } .w-split i { border-radius: 4px; background: var(--hd-accent); } .w-split i.held { background: #ffc83c; }
.w-legend { display: flex; gap: 16px; font-size: 13px; color: color-mix(in oklab, var(--hd-inverse-fg) 72%, transparent); } .w-legend span { display: flex; align-items: center; gap: 6px; } .w-legend b { color: var(--hd-inverse-fg); font-weight: 600; }
.w-legend i { width: 8px; height: 8px; border-radius: 2px; background: var(--hd-accent); } .w-legend i.held { background: #ffc83c; }
.w-next { display: flex; align-items: center; gap: 8px; font-size: 13px; padding: 10px 12px; border-radius: 12px; background: color-mix(in oklab, var(--hd-inverse-fg) 8%, transparent); color: color-mix(in oklab, var(--hd-inverse-fg) 78%, transparent); } .w-next b { color: var(--hd-inverse-fg); font-weight: 600; }
.w-month { padding: 14px 16px 12px !important; display: flex; flex-direction: column; gap: 10px; } .w-mh { display: flex; justify-content: space-between; align-items: flex-start; }
.w-made { font-family: var(--font-brand); font-size: 20px; font-weight: 600; letter-spacing: -0.02em; margin-top: 2px; } .w-made b { font-weight: 650; }
.w-mbars { display: flex; gap: 8px; align-items: flex-end; height: 70px; } .w-mb { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; height: 100%; justify-content: flex-end; }
.w-mb i { width: 100%; border-radius: 6px 6px 3px 3px; background: color-mix(in oklab, var(--hd-accent) 18%, var(--hd-surface)); } .w-mb.on i { background: var(--hd-accent); }
.w-mb span { font-size: 11px; color: var(--hd-fg-subtle); } .w-mb.on span { color: var(--hd-fg); font-weight: 600; }
.w-amt.in { color: var(--hd-success-strong); } .w-amt.out { color: var(--hd-fg); }
/* ===== notifications redesign ===== */
.n-it { align-items: flex-start !important; gap: 12px; padding: 12px 12px 12px 12px !important; }
.n-it.unread { background: color-mix(in oklab, var(--hd-accent) 6%, var(--hd-surface)) !important; border-color: color-mix(in oklab, var(--hd-accent) 22%, var(--hd-edge, rgba(16,20,38,.16))) !important; }
.n-lead { position: relative; flex: none; width: 40px; height: 40px; } .n-lead .x-tile { width: 40px !important; height: 40px !important; } .n-lead .av { width: 40px; height: 40px; }
.n-bdg { position: absolute; right: -4px; bottom: -4px; width: 20px; height: 20px; border-radius: 50%; display: grid; place-items: center; color: #fff; box-shadow: 0 0 0 2px var(--hd-surface); }
.n-bdg.cob { background: var(--hd-accent); } .n-bdg.mint { background: var(--hd-success); } .n-bdg.mar { background: #c98a00; } .n-bdg.ver { background: var(--hd-danger); }
.n-txt { margin: 0; font-size: 14px; line-height: 19px; color: var(--hd-fg); } .n-txt b { font-weight: 600; }
.n-it .tx small { display: block; margin-top: 3px; font-size: 12.5px; color: var(--hd-fg-subtle); }
.n-th { width: 44px; height: 44px; border-radius: 10px; object-fit: cover; flex: none; }
.n-act { display: flex; gap: 8px; margin-top: 10px; }
.n-txt b, .n-it .tx p b { display: inline !important; font-size: inherit !important; }
.n-it .tx { min-width: 0; }
/* multi-select toggle = separate chips; selected = accent tint + accent ring, never a merged slab */
.n-tgm { border: 0 !important; background: transparent !important; overflow: visible !important; gap: 8px; display: inline-flex; flex-wrap: wrap; }
.n-tgm span { height: 40px !important; padding: 0 14px !important; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; color: var(--hd-fg) !important; }
.n-tgm span + span { border-left: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; }
.n-tgm span.on { background: var(--hd-accent-subtle) !important; color: var(--hd-info-strong) !important; border-color: color-mix(in oklab, var(--hd-accent) 45%, transparent) !important; }
.n-it { align-items: center !important; } .n-it .x-tile { width: 40px !important; height: 40px !important; flex: none; }
.n-end { display: flex; flex-direction: column; align-items: flex-end; gap: 8px; align-self: flex-start; padding-top: 2px; }
.n-act { margin-top: 8px; }
/* slim notifications: ~56px rows */
.n-it { padding: 10px 12px !important; gap: 12px !important; min-height: 0 !important; }
.n-it .x-tile { width: 34px !important; height: 34px !important; border-radius: 10px !important; } .n-it .x-tile .ic { width: 18px !important; height: 18px !important; }
.n-it .n-txt { font-size: 14px; line-height: 18px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-it .tx small { margin-top: 1px !important; font-size: 12.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-end { gap: 6px !important; padding-top: 0 !important; align-self: center !important; }
/* secondary + ghost buttons: native, crisp — one 1px hairline, soft contact shadow, no lip, no bevel */
.btn.s:not(.dis):not([disabled]) { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; box-shadow: 0 1px 2px rgba(16,20,38,.06) !important; }
.btn.s.hov:not(.dis), .btn.s:hover:not(.dis) { background: var(--hd-bg-subtle) !important; }
.btn.s.prs:not(.dis), .btn.s:active:not(.dis) { background: var(--hd-control) !important; box-shadow: inset 0 1px 2px rgba(16,20,38,.10) !important; transform: translateY(1px); }
.btn.s.foc:not(.dis):not([disabled]) { box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
[data-theme="dark"] .btn.s:not(.dis):not([disabled]) { background: var(--hd-surface-raised) !important; box-shadow: 0 1px 2px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.05) !important; }
/* button inside a field: concentric (12 - 4 = 8 radius), even 4px inset, flat — never a floating bevelled pill */
.input.n-copy { padding-right: 4px !important; }
.input.n-copy .btn { height: calc(100% - 8px) !important; min-height: 0 !important; margin: 4px 0; border-radius: 8px !important; border: 0 !important;
  background: var(--hd-control) !important; box-shadow: none !important; padding: 0 12px !important; font-size: 14px !important; }
.input.n-copy .btn.n-done { background: var(--hd-success-subtle) !important; color: var(--hd-success-strong) !important; }
.input.n-copy .btn .ic { width: 16px !important; height: 16px !important; }
[data-theme="dark"] .input.n-copy .btn { background: var(--hd-control) !important; }
.input.n-copy .btn.s:not(.dis):not([disabled]) { background: var(--hd-control) !important; border: 0 !important; box-shadow: none !important; }
.input.n-copy .btn.s.n-done:not(.dis):not([disabled]) { background: var(--hd-success-subtle) !important; color: var(--hd-success-strong) !important; }
/* primary + danger: native, same anatomy as secondary — flat fill, faint top highlight, thin contact shadow, no bevel lip */
.btn.p:not(.dis):not([disabled]), .btn.d:not(.dis):not([disabled]) { border: 0 !important; box-shadow: inset 0 1px 0 rgba(255,255,255,.16), 0 1px 2px rgba(16,20,38,.16) !important; }
.btn.p.prs:not(.dis), .btn.d.prs:not(.dis), .btn.p:active:not(.dis), .btn.d:active:not(.dis) { box-shadow: inset 0 1px 3px rgba(0,0,0,.25) !important; transform: translateY(1px); }
.btn.p.foc:not(.dis), .btn.d.foc:not(.dis) { box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
.btngroup.split .btn + .btn { box-shadow: inset 1px 0 0 rgba(255,255,255,.30), inset 0 1px 0 rgba(255,255,255,.16) !important; }
/* FULL-BLEED product card: photo fills the card, a firm bottom scrim carries brand, title, one meta line, a hairline progress and one action */
.card.n-pc { position: relative; padding: 0 !important; overflow: hidden; min-height: 460px; display: flex; flex-direction: column; justify-content: flex-end; border: 0 !important; }
.card.n-pc > .n-ph { position: absolute !important; inset: 0; aspect-ratio: auto !important; height: 100%; }
.card.n-pc > .n-ph img { border-radius: 0 !important; height: 100% !important; width: 100%; object-fit: cover; }
.card.n-pc > .n-ph::after { content: ''; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg, rgba(10,12,18,0) 38%, rgba(10,12,18,.62) 62%, rgba(10,12,18,.92) 100%); }
.card.n-pc .n-pb { position: relative; z-index: 1; display: flex; flex-direction: column; gap: 6px; padding: 18px 18px 18px; margin: 0 !important; }
.n-pc .n-brand { display: inline-flex; align-items: center; gap: 4px; font-size: 13px; color: rgba(255,255,255,.80) !important; }
.n-pc .n-pt { font-family: var(--font-brand); font-size: 24px; line-height: 28px; font-weight: 650; letter-spacing: -0.025em; color: #fff !important; }
.n-pc .n-meta { font-size: 14px; color: rgba(255,255,255,.82) !important; } .n-pc .n-meta b { color: #fff !important; font-weight: 650; }
.n-pc .n-line { height: 3px; border-radius: 2px; background: rgba(255,255,255,.25); margin: 6px 0 10px; overflow: hidden; } .n-pc .n-line i { display: block; height: 100%; background: #fff; border-radius: 2px; }
.n-pc .n-bd { position: absolute; top: 14px; left: 14px; z-index: 2; } .n-pc .n-disc { position: absolute; top: 12px; right: 12px; z-index: 2; color: var(--hd-fg) !important; }
.card.n-pc .btn.s:not(.dis):not([disabled]) { background: rgba(255,255,255,.14) !important; color: #fff !important; border: 1px solid rgba(255,255,255,.32) !important; box-shadow: none !important; }
.panel.x-camp { padding: 0 !important; overflow: hidden; grid-template-columns: 132px 1fr !important; gap: 0 !important; }
.panel.x-camp > img { width: 132px !important; height: 100% !important; min-height: 132px; object-fit: cover; border-radius: 0 !important; }
.panel.x-camp > .stack { padding: 14px 16px; }
/* tactile but crisp, all native: sheen + inner top highlight + inner bottom lip + two-layer contact */
.btn.p:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-accent) 92%, #fff) 0%, var(--hd-accent) 100%) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(0,0,0,.22), 0 1px 1px rgba(16,20,38,.18), 0 2px 5px -1px rgba(45,88,238,.28) !important; }
.btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 92%, #fff) 0%, var(--hd-danger-solid, #c93d00) 100%) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), inset 0 -1px 0 rgba(0,0,0,.22), 0 1px 1px rgba(16,20,38,.18), 0 2px 5px -1px rgba(16,20,38,.16) !important; }
.btn.p.hov:not(.dis), .btn.p:hover:not(.dis) { background: linear-gradient(180deg, var(--hd-accent) 0%, var(--hd-accent-hover) 100%) !important; }
.btn.p.prs:not(.dis), .btn.d.prs:not(.dis) { background: var(--hd-accent-pressed) !important; box-shadow: inset 0 2px 3px rgba(0,0,0,.28) !important; transform: translateY(1px); }
.btn.d.prs:not(.dis) { background: var(--hd-danger-strong) !important; }
.btn.s:not(.dis):not([disabled]) { box-shadow: inset 0 -1px 0 rgba(16,20,38,.07), 0 1px 1px rgba(16,20,38,.06), 0 2px 4px -2px rgba(16,20,38,.08) !important; }
[data-theme="dark"] .btn.s:not(.dis):not([disabled]) { box-shadow: inset 0 1px 0 rgba(255,255,255,.07), inset 0 -1px 0 rgba(0,0,0,.35), 0 1px 2px rgba(0,0,0,.5) !important; }
.card.n-pc .n-pb { flex: 0 0 auto !important; margin-top: auto !important; justify-content: flex-end !important; height: auto !important; }
.card.n-pc .n-pb > * { margin: 0 !important; } .card.n-pc .n-pb > .n-line { margin: 6px 0 10px !important; }
.card.n-pc .n-meta { display: block !important; } .card.n-pc .n-meta b { margin: 0 2px; }
.btn.p.foc:not(.dis):not([disabled]), .btn.d.foc:not(.dis):not([disabled]) { box-shadow: inset 0 1px 0 rgba(255,255,255,.22), 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
.btn.d.hov:not(.dis):not([disabled]) { background: linear-gradient(180deg, var(--hd-danger-solid, #c93d00) 0%, var(--hd-danger-strong) 100%) !important; }
.btngroup.split .btn.p + .btn.p:not(.dis):not([disabled]) { box-shadow: inset 1px 0 0 rgba(255,255,255,.32), inset 0 1px 0 rgba(255,255,255,.22), inset 0 -1px 0 rgba(0,0,0,.22), 0 1px 1px rgba(16,20,38,.18) !important; }
/* inline edit row: label left, value right; editing keeps one 36px line (input + save + cancel) */
.row.n-ier { display: flex !important; align-items: center !important; justify-content: space-between; gap: 12px; min-height: 56px; padding: 10px 14px 10px 16px !important; }
.n-iel { font-size: 14px; color: var(--hd-fg-muted); }
.n-iev2 { display: inline-flex; align-items: center; gap: 8px; height: 36px; padding: 0 6px 0 10px; border-radius: 8px; background: var(--hd-bg-subtle); } .n-iev2 b { font-size: 15px; font-weight: 600; } .n-pen2 { color: var(--hd-fg-subtle); display: inline-flex; }
.n-iee { display: flex; flex-direction: row; align-items: center; gap: 6px; padding: 0; }
.n-iee .input { width: 84px; height: 36px !important; min-height: 0 !important; padding: 0 10px !important; border-radius: 8px !important; font-size: 15px; }
.n-iee .btn { width: 36px !important; min-width: 36px !important; height: 36px !important; border-radius: 8px !important; padding: 0 !important; }
/* product card v3: content on top (badge row, brand, title, earning), progress + action at the bottom; scrims top and bottom */
.card.n-pc { justify-content: space-between !important; }
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(10,12,18,.82) 0%, rgba(10,12,18,.50) 30%, rgba(10,12,18,0) 52%, rgba(10,12,18,0) 66%, rgba(10,12,18,.72) 100%) !important; }
.card.n-pc .n-pb { margin-top: 0 !important; flex: 1 1 auto !important; padding-top: 56px !important; }
.card.n-pc .n-pb > .n-line { margin-top: auto !important; }
/* FINAL primary/danger: flat deep fill, no gradient, no coloured glow; quiet tactile edge = faint top highlight + 1px neutral contact */
.btn.p:not(.dis):not([disabled]) { background: var(--hd-accent) !important; box-shadow: inset 0 1px 0 rgba(255,255,255,.14), 0 1px 1px rgba(16,20,38,.14) !important; }
.btn.d:not(.dis):not([disabled]) { background: var(--hd-danger-solid, #c93d00) !important; box-shadow: inset 0 1px 0 rgba(255,255,255,.14), 0 1px 1px rgba(16,20,38,.14) !important; }
.btn.p.hov:not(.dis):not([disabled]) { background: var(--hd-accent-hover) !important; }
.btn.d.hov:not(.dis):not([disabled]) { background: var(--hd-danger-strong) !important; }
.btn.p.prs:not(.dis):not([disabled]) { background: var(--hd-accent-pressed) !important; box-shadow: inset 0 1px 2px rgba(0,0,0,.22) !important; }
.btn.d.prs:not(.dis):not([disabled]) { background: var(--hd-danger-strong) !important; box-shadow: inset 0 1px 2px rgba(0,0,0,.25) !important; }
.btn.p.foc:not(.dis):not([disabled]), .btn.d.foc:not(.dis):not([disabled]) { box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
.btngroup.split .btn.p + .btn.p:not(.dis):not([disabled]) { box-shadow: inset 1px 0 0 rgba(255,255,255,.30), inset 0 1px 0 rgba(255,255,255,.14), 0 1px 1px rgba(16,20,38,.14) !important; }
/* inline edit demo: editing row spans the card, value stays on one line */
.n-ie.ed { width: 100%; align-self: stretch; } .n-ie.ed .n-iei { flex: 1; min-width: 0; height: 44px !important; display: flex; align-items: center; }
.n-ie.ed .n-iei .t-h2 { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-size: 17px !important; }
.n-ie.ed .btn { width: 44px !important; min-width: 44px !important; height: 44px !important; flex: none; }
/* ===== message thread (calm, iMessage-grade) ===== */
.t-thr { padding: 0 !important; overflow: hidden; display: flex; flex-direction: column; }
.t-head { display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-bottom: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.t-head > div { flex: 1; min-width: 0; } .t-head b { display: block; font-size: 15px; font-weight: 600; } .t-head span { font-size: 13px; color: var(--hd-fg-muted); }
.t-ctx { display: inline-flex; align-items: center; gap: 8px; height: 32px; padding: 0 10px 0 4px; border-radius: 10px; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); font-size: 13px; font-weight: 560; color: var(--hd-fg) !important; flex: none; }
.t-ctx img { width: 24px; height: 24px; border-radius: 6px; object-fit: cover; }
.t-body { padding: 16px; display: flex; flex-direction: column; gap: 4px; background: var(--hd-canvas); }
.t-day { align-self: center; font-size: 12px; font-weight: 600; color: var(--hd-fg-subtle); margin-bottom: 8px; }
.t-m { display: flex; gap: 8px; align-items: flex-end; max-width: 72%; } .t-m.out { align-self: flex-end; justify-content: flex-end; } .t-m.last { margin-bottom: 10px; }
.t-av { width: 28px; flex: none; } .t-c { display: flex; flex-direction: column; gap: 4px; min-width: 0; } .t-m.out .t-c { align-items: flex-end; }
.t-b { margin: 0; padding: 9px 14px; font-size: 15px; line-height: 21px; border-radius: 18px; background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); color: var(--hd-fg); }
.t-m.in.last .t-b { border-bottom-left-radius: 6px; } .t-m.out .t-b { background: var(--hd-accent); border-color: transparent; color: #fff; } .t-m.out.last .t-b { border-bottom-right-radius: 6px; }
.t-meta { font-size: 12px; color: var(--hd-fg-subtle); padding: 0 6px; }
.t-file { display: flex; align-items: center; gap: 12px; padding: 10px 10px 10px 12px; border-radius: 16px; background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); min-width: 280px; }
.t-file > div { flex: 1; min-width: 0; } .t-file b { display: block; font-size: 14px; font-weight: 600; } .t-file span { font-size: 12.5px; color: var(--hd-fg-muted); }
.t-file .x-tile { width: 40px !important; height: 40px !important; }
.t-img { width: 240px; height: 180px; object-fit: cover; border-radius: 16px; display: block; }
.t-comp { display: flex; align-items: center; gap: 8px; padding: 10px 12px; border-top: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.t-field { flex: 1; height: 44px; border-radius: 22px; border: 1px solid var(--hd-border-input); display: flex; align-items: center; gap: 6px; padding: 0 14px 0 6px; box-shadow: inset 0 1px 2px rgba(16,20,38,.05); }
.t-field .ph { color: var(--hd-fg-subtle); font-size: 15px; } .t-ib { width: 32px; height: 32px; border: 0; background: none; color: var(--hd-fg-muted); display: grid; place-items: center; border-radius: 50%; }
.t-comp .btn { width: 44px !important; min-width: 44px !important; height: 44px !important; border-radius: 50% !important; }
[data-theme="dark"] .t-m.in .t-b, [data-theme="dark"] .t-file { background: var(--hd-surface-raised); }
.n-page img { width: 112px !important; height: 112px !important; object-fit: contain; }
.n-code { display: none !important; }
.t-ctxcard { padding: 0 !important; overflow: hidden; } .t-ch { display: flex; align-items: center; gap: 12px; padding: 14px 16px; border-bottom: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.t-ch img { width: 44px; height: 44px; border-radius: 10px; object-fit: cover; } .t-ch > div { flex: 1; min-width: 0; } .t-ch b { display: block; font-size: 15px; font-weight: 600; } .t-ch span:not(.badge) { font-size: 13px; color: var(--hd-fg-muted); }
.t-ctxcard > :not(.t-ch) { padding-left: 16px; padding-right: 16px; }
/* error states: white icon tile (meaning colour on the glyph), no support codes; section errors are a compact row */
.n-state .n-ti { width: 52px !important; height: 52px !important; border-radius: 14px !important; background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)) !important; box-shadow: 0 1px 1px rgba(16,20,38,.05), 0 3px 8px -2px rgba(16,20,38,.08) !important; color: var(--hd-fg-muted) !important; }
.n-state .n-ti.dg { color: var(--hd-danger) !important; }
.card.n-serr { display: flex; align-items: center; gap: 12px; padding: 12px 12px 12px 14px !important; }
.n-serr > div { flex: 1; min-width: 0; } .n-serr b { display: block; font-size: 15px; font-weight: 600; } .n-serr span:not(.x-tile) { font-size: 13px; color: var(--hd-fg-muted); }
.n-serr .x-tile { width: 40px !important; height: 40px !important; flex: none; }
[data-theme="dark"] .n-state .n-ti { background: var(--hd-surface-raised) !important; }
/* ===== uploads, modern: filled drop area, thumbnail rows, hairline progress ===== */
.u-dz { display: flex; align-items: center; gap: 14px; padding: 18px 18px; border-radius: 16px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); transition: background-color 150ms ease, border-color 150ms ease; }
.u-dz .u-ic { width: 40px; height: 40px; border-radius: 12px; display: grid; place-items: center; background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); color: var(--hd-fg-muted); flex: none; box-shadow: 0 1px 1px rgba(16,20,38,.05); }
.u-dz b { display: block; font-size: 15px; font-weight: 600; } .u-dz b u { color: var(--hd-link); text-decoration: none; } .u-dz span:not(.u-ic) { font-size: 13px; color: var(--hd-fg-muted); }
.u-dz.drag { background: var(--hd-accent-subtle); border-color: var(--hd-accent); } .u-dz.drag .u-ic { color: var(--hd-accent); border-color: color-mix(in oklab, var(--hd-accent) 40%, transparent); } .u-dz.drag b { color: var(--hd-info-strong); }
.u-list { display: flex; flex-direction: column; gap: 8px; }
.u-row { position: relative; overflow: hidden; display: flex; align-items: center; gap: 12px; padding: 10px 8px 10px 10px; border-radius: 14px; background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); }
.u-th { width: 40px; height: 40px; border-radius: 8px; object-fit: cover; flex: none; }
.u-tx { flex: 1; min-width: 0; } .u-tx b { display: block; font-size: 14px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; } .u-tx span { font-size: 12.5px; color: var(--hd-fg-muted); }
.u-row.err .u-tx span { color: var(--hd-danger-strong); } .u-row.err .u-th { opacity: .55; }
.u-ok { color: var(--hd-success); display: inline-flex; }
.u-bar { position: absolute; left: 0; bottom: 0; height: 2px; background: var(--hd-accent); }

/* ===== BUTTONS v-final: flat cobalt + quiet tactile finish (owner rule): ~7% top-to-bottom shade, hairline light top, dark bottom lip, 1-2px neutral contact; NO coloured glow ===== */
.btn.p:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-accent) 93%, #fff) 0%, var(--hd-accent) 55%, color-mix(in oklab, var(--hd-accent) 94%, #000) 100%) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.20), inset 0 -1px 0 rgba(0,0,0,.24), 0 1px 1px rgba(16,20,38,.16), 0 2px 3px -1px rgba(16,20,38,.14) !important; }
.btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 93%, #fff) 0%, var(--hd-danger-solid, #c93d00) 55%, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 94%, #000) 100%) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.18), inset 0 -1px 0 rgba(0,0,0,.24), 0 1px 1px rgba(16,20,38,.16), 0 2px 3px -1px rgba(16,20,38,.14) !important; }
.btn.p.hov:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-accent-hover) 93%, #fff) 0%, var(--hd-accent-hover) 100%) !important; }
.btn.d.hov:not(.dis):not([disabled]) { background: linear-gradient(180deg, var(--hd-danger-solid, #c93d00) 0%, var(--hd-danger-strong) 100%) !important; }
.btn.p.prs:not(.dis):not([disabled]), .btn.p:active:not(.dis):not([disabled]) { background: var(--hd-accent-pressed) !important; box-shadow: inset 0 1px 3px rgba(0,0,0,.30), inset 0 0 0 1px rgba(0,0,0,.08) !important; transform: scale(.97); }
.btn.d.prs:not(.dis):not([disabled]), .btn.d:active:not(.dis):not([disabled]) { background: var(--hd-danger-strong) !important; box-shadow: inset 0 1px 3px rgba(0,0,0,.30) !important; transform: scale(.97); }
.btn.p.foc:not(.dis):not([disabled]), .btn.d.foc:not(.dis):not([disabled]) { box-shadow: inset 0 1px 0 rgba(255,255,255,.20), inset 0 -1px 0 rgba(0,0,0,.24), 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
.btngroup.split .btn.p + .btn.p:not(.dis):not([disabled]) { box-shadow: inset 1px 0 0 rgba(255,255,255,.28), inset 0 1px 0 rgba(255,255,255,.20), inset 0 -1px 0 rgba(0,0,0,.24), 0 1px 1px rgba(16,20,38,.16) !important; }
/* white secondary: hairline + 1px bottom lip + soft contact */
.btn.s:not(.dis):not([disabled]) { background: linear-gradient(180deg, #fff 0%, #fbfbfc 100%) !important; box-shadow: inset 0 -1px 0 rgba(16,20,38,.08), 0 1px 1px rgba(16,20,38,.07), 0 2px 3px -1px rgba(16,20,38,.08) !important; }
.btn.s.prs:not(.dis):not([disabled]), .btn.s:active:not(.dis):not([disabled]) { background: #f3f4f6 !important; box-shadow: inset 0 1px 2px rgba(16,20,38,.12) !important; transform: scale(.97); }
[data-theme="dark"] .btn.s:not(.dis):not([disabled]) { background: linear-gradient(180deg, #2a2d35 0%, #23262d 100%) !important; box-shadow: inset 0 1px 0 rgba(255,255,255,.07), inset 0 -1px 0 rgba(0,0,0,.35), 0 1px 2px rgba(0,0,0,.5) !important; }
[data-theme="dark"] .btn.p:not(.dis):not([disabled]), [data-theme="dark"] .btn.d:not(.dis):not([disabled]) { box-shadow: inset 0 1px 0 rgba(255,255,255,.18), inset 0 -1px 0 rgba(0,0,0,.30), 0 1px 2px rgba(0,0,0,.45) !important; }
.btn { transition: transform 90ms cubic-bezier(.23,1,.32,1), background-color 160ms ease, box-shadow 160ms ease; }

/* info popover: compact, anchored (caret), quiet link, small secondary */
.dialog.n-pop { width: 300px !important; padding: 14px 16px 12px !important; gap: 4px !important; border-radius: 14px !important; position: relative; margin-top: 4px; }
.dialog.n-pop::before { content: ''; position: absolute; top: -6px; left: 24px; width: 10px; height: 10px; background: inherit; border-left: 1px solid var(--hd-edge); border-top: 1px solid var(--hd-edge); transform: rotate(45deg); border-top-left-radius: 2px; }
.n-pop > b { font-size: 15px !important; font-weight: 600; line-height: 20px; }
.n-pop > p { font-size: 13.5px !important; line-height: 19px !important; text-wrap: pretty; }
.n-popf { margin-top: 10px !important; padding-top: 10px; border-top: 1px solid var(--hd-edge); }
.n-popl { display: inline-flex; align-items: center; gap: 2px; font-size: 13.5px; font-weight: 560; color: var(--hd-accent-strong, var(--hd-accent)); text-decoration: none; cursor: pointer; }
.n-popl .ic { margin-top: 1px; }
.n-popf .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 12px !important; font-size: 13.5px !important; border-radius: 8px !important; }

/* bank logos (Cashfree CDN): bare inline mark; on a white tile where a row leads with it */
.bankl { display: inline-block; object-fit: contain; flex: none; border-radius: 4px; vertical-align: -3px; }
.x-tile.bankt { display: inline-grid; place-items: center; } .x-tile.bankt .bankl { width: 22px; height: 22px; }
.n-bkv { display: inline-flex; align-items: center; gap: 6px; }
.input .bankl { margin-right: 2px; }
.n-dvsign .btn { gap: 8px; } .n-dvsign .btn .ic { flex: none; }

/* success inline: white tile + solid success glyph (no heavy green discs); small white secondary action */
.n-okrow { display: flex !important; align-items: center !important; gap: 14px !important; min-height: 68px; padding: 12px 14px 12px 14px !important; }
.n-okrow > div { flex: 1; min-width: 0; } .n-okrow b { display: block; font-size: 15px; font-weight: 600; line-height: 20px; }
.n-okrow .t-small { display: block; font-size: 13.5px; line-height: 19px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.x-tile.n-okt { width: 40px !important; height: 40px !important; flex: none; display: grid; place-items: center; color: var(--hd-success, #0a8a4a) !important; border-radius: 12px !important; }
.n-okrow .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 12px !important; font-size: 13.5px !important; border-radius: 8px !important; flex: none; }
/* errors: calm, compact, tile glyph in status colour */
.card.n-state { padding: 28px 24px 24px !important; gap: 0 !important; }
.x-tile.n-errt { width: 44px !important; height: 44px !important; display: grid; place-items: center; flex: none; color: var(--hd-danger-strong) !important; border-radius: 12px !important; }
.card.n-state .x-tile.n-errt { margin-bottom: 14px; color: var(--hd-warning-strong, #8a5a00) !important; }
.card.n-state .t-h2 { font-size: 18px !important; line-height: 24px; }
.n-errp { margin: 6px auto 0; max-width: 320px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); text-wrap: pretty; }
.n-errb { display: flex; gap: 10px; justify-content: center; margin-top: 18px; } .n-errb .btn { height: 40px !important; min-height: 0 !important; }
.card.n-serr { display: flex !important; align-items: center !important; gap: 14px !important; padding: 12px 14px !important; }
.card.n-serr > div { flex: 1; min-width: 0; } .card.n-serr b { display: block; font-size: 15px; font-weight: 600; line-height: 20px; }
.card.n-serr span:not(.x-tile) { display: block; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); }
.card.n-serr .x-tile.n-errt { width: 40px !important; height: 40px !important; }
.card.n-serr .btn.s.sm { height: 32px !important; min-height: 0 !important; padding: 0 12px !important; font-size: 13.5px !important; border-radius: 8px !important; flex: none; }

/* load more v2: one quiet row — count + hairline progress left, small secondary right; same width across states */
.n-more2 { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 12px 12px 12px 16px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; min-width: 0; }
.n-m2t { display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.n-m2t > span { font-size: 13.5px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; } .n-m2t b { color: var(--hd-fg); font-weight: 600; }
.n-m2bar { display: block; width: 140px; height: 3px; border-radius: 3px; background: var(--hd-track, rgba(16,20,38,.10)); overflow: hidden; } .n-m2bar > i { display: block; height: 100%; background: var(--hd-accent); border-radius: 3px; }
.n-more2.done .n-m2bar > i { background: var(--hd-success, #0a8a4a); }
.n-more2 .btn.sm { height: 34px !important; min-height: 0 !important; min-width: 128px; padding: 0 14px !important; font-size: 13.5px !important; border-radius: 9px !important; gap: 8px; justify-content: center; flex: none; }
.n-end2 { display: inline-flex; align-items: center; gap: 6px; height: 34px; font-size: 13.5px; font-weight: 560; color: var(--hd-success-strong, #08703c); flex: none; }
/* hover card actions: lighter — 36 tall, 14px, compact icon */
.n-hca { gap: 8px !important; margin-top: 4px; } .n-hca .btn { height: 36px !important; min-height: 0 !important; font-size: 14px !important; border-radius: 10px !important; padding: 0 12px !important; gap: 6px !important; flex: 1; }
.n-hca .btn .ic { width: 15px; height: 15px; }

/* toast v2: slim ink capsule, bare solid success glyph (no green disc), white action, no light border */
.toast { min-height: 44px; padding: 0 6px 0 14px !important; gap: 10px !important; border-radius: 12px !important; background: #16181d !important; color: #f4f5f7 !important; border: 0 !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.06), 0 1px 2px rgba(10,12,18,.20), 0 8px 24px -6px rgba(10,12,18,.32) !important; font-size: 14px !important; font-weight: 500; }
.toast .ok { width: 18px !important; height: 18px !important; background: none !important; color: #3fcf8e !important; flex: none; display: inline-grid; place-items: center; }
.toast b { margin-left: auto; padding: 0 10px !important; height: 32px; display: inline-flex; align-items: center; border-radius: 8px; color: #fff !important; font-weight: 600; font-size: 14px; }
.toast b:hover { background: rgba(255,255,255,.08); }
.toast:not(:has(b)) { padding-right: 16px !important; }
[data-theme="dark"] .toast { background: #f4f5f7 !important; color: #16181d !important; box-shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px -6px rgba(0,0,0,.6) !important; }
[data-theme="dark"] .toast b { color: #16181d !important; } [data-theme="dark"] .toast .ok { color: #08803f !important; }

/* date range v2 — same language as the approved date picker: 36px circles, continuous band, today = accent text + dot */
.panel.cal2 { width: 300px; max-width: 100%; padding: 14px 14px 12px !important; }
.c2h { display: flex; align-items: center; justify-content: space-between; padding-left: 6px; margin-bottom: 8px; } .c2h b { font-size: 15px; font-weight: 600; }
.c2n { display: inline-flex; gap: 2px; } .c2n .btn.icon { width: 32px !important; height: 32px !important; min-height: 0 !important; border-radius: 8px !important; }
.c2g { display: grid; grid-template-columns: repeat(7, 1fr); row-gap: 2px; text-align: center; }
.c2g .dw { height: 28px; display: grid; place-items: center; font-size: 12px; color: var(--hd-fg-subtle); font-weight: 500; }
.c2g .c { height: 36px; display: grid; place-items: center; position: relative; }
.c2g .c i { font-style: normal; width: 36px; height: 36px; display: grid; place-items: center; border-radius: 50%; font-size: 13.5px; font-variant-numeric: tabular-nums; position: relative; z-index: 1; color: var(--hd-fg); }
.c2g .c.past i { color: var(--hd-fg-subtle); }
.c2g .c.in { background: var(--hd-accent-subtle); } .c2g .c.in i { color: var(--hd-accent-strong, var(--hd-link)); font-weight: 560; }
.c2g .c.rs { background: linear-gradient(90deg, transparent 50%, var(--hd-accent-subtle) 50%); }
.c2g .c.re { background: linear-gradient(90deg, var(--hd-accent-subtle) 50%, transparent 50%); }
.c2g .c.in.l { border-radius: 18px 0 0 18px; } .c2g .c.in.r { border-radius: 0 18px 18px 0; }
.c2g .c.rs.r { background: none; } .c2g .c.re.l { background: none; }
.c2g .c i.sel { background: var(--hd-accent); color: #fff; font-weight: 600; }
.c2g .c i.td { color: var(--hd-accent-strong, var(--hd-link)); font-weight: 600; } .c2g .c i.td::after { content: ''; position: absolute; bottom: 5px; left: 50%; width: 4px; height: 4px; margin-left: -2px; border-radius: 50%; background: currentColor; }
.c2f { margin-top: 8px; padding: 10px 6px 0; border-top: 1px solid var(--hd-edge); font-size: 13px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }

/* platform multi-toggle: on = solid accent-subtle + full-colour glyph + strong text; off = white hairline, glyph greyed. No extra check. */
.n-tgm { display: inline-flex; gap: 8px; flex-wrap: wrap; }
.n-tgm > span { height: 36px !important; padding: 0 14px 0 10px !important; gap: 8px !important; border-radius: 10px !important; font-size: 14px !important; font-weight: 560 !important; display: inline-flex; align-items: center; box-shadow: none !important; }
.n-tgm > span.on { background: var(--hd-accent-subtle) !important; color: var(--hd-accent-strong, var(--hd-link)) !important; border: 1px solid transparent !important; }
.n-tgm > span:not(.on) { background: var(--hd-surface) !important; color: var(--hd-fg-muted) !important; border: 1px solid var(--hd-edge) !important; }
.n-tgm > span:not(.on) svg, .n-tgm > span:not(.on) img { filter: grayscale(1); opacity: .55; }
.n-tgm > span > .ic:first-child:not(:only-child) { display: none; }
/* form section layout: calmer fields */
.n-fgrid .input { height: 44px !important; min-height: 0 !important; font-size: 15px !important; padding: 0 14px !important; border-radius: 10px !important; }
.n-fgrid .n-fl, .n-fgrid label, .n-fgrid .lbl { font-size: 14px !important; }
.n-fgrid .help, .n-fgrid .n-help, .n-fgrid .fhelp { font-size: 13px !important; line-height: 18px !important; }
.n-fgrid .err .ic, .n-fgrid .n-err .ic { width: 14px; height: 14px; flex: none; margin-top: 2px; }
/* upload rows when used outside nw2 */
.u-list { display: flex; flex-direction: column; gap: 8px; }

.n-fgrid .labrow label { font-size: 14px !important; font-weight: 600; } .n-fgrid .labrow span { font-size: 12.5px !important; }
.n-fgrid .help { font-size: 13px !important; line-height: 18px !important; margin-top: 6px; display: flex; gap: 6px; align-items: flex-start; }
.n-fgrid .help.err { color: var(--hd-danger-strong); } .n-fgrid .help .ic { width: 14px; height: 14px; flex: none; margin-top: 2px; }
.n-fgrid .input.err { box-shadow: 0 0 0 3px color-mix(in oklab, var(--hd-danger) 14%, transparent) !important; }

/* menus v2: 34px rows, 14px text, 16px muted glyphs, text-only shortcuts, trailing accent tick, quiet hover */
.menu.n-ctx, .menu.n-sortm { padding: 4px !important; border-radius: 12px !important; min-width: 220px; }
.menu.n-ctx > div, .menu.n-sortm > div { display: flex !important; align-items: center; gap: 10px !important; height: 34px !important; min-height: 0 !important; padding: 0 10px !important; border-radius: 8px !important; font-size: 14px !important; font-weight: 450; background: none !important; }
.menu.n-ctx > div > .ic:first-child { width: 16px; height: 16px; color: var(--hd-fg-muted); flex: none; }
.menu.n-ctx > div.hl, .menu.n-sortm > div:hover { background: color-mix(in oklab, var(--hd-fg) 6%, transparent) !important; }
.menu.n-ctx > div.dg, .menu.n-ctx > div.dg .ic { color: var(--hd-danger-strong) !important; }
.menu .n-t { flex: 1; min-width: 0; white-space: nowrap; }
.menu .n-k { margin-left: auto; display: inline-flex; gap: 2px; } .menu .n-k .kbd, .menu .n-k kbd { border: 0 !important; box-shadow: none !important; background: none !important; padding: 0 !important; min-width: 0 !important; height: auto !important; font-size: 12.5px !important; color: var(--hd-fg-subtle) !important; font-family: var(--font-ui); }
.menu .n-chv { margin-left: auto; color: var(--hd-fg-subtle); display: inline-flex; } .menu .n-chv .ic { width: 14px; height: 14px; }
.menu .n-tk { margin-left: auto; color: var(--hd-accent-strong, var(--hd-link)) !important; display: inline-flex; width: 16px; } .menu .n-tk .ic { width: 16px; height: 16px; }
.menu.n-sortm > div.on { font-weight: 600; }
.menu .n-sep { display: block; height: 1px; margin: 4px 6px; background: var(--hd-edge); }
.menu.n-subm { min-width: 190px; margin-top: 112px !important; }
.menu .n-mh { display: block; padding: 6px 10px 4px; font-size: 12px; font-weight: 560; color: var(--hd-fg-subtle); }
.btn.n-sortb { height: 34px !important; min-height: 0 !important; padding: 0 10px 0 10px !important; gap: 6px !important; font-size: 13.5px !important; border-radius: 9px !important; }
.btn.n-sortb .muted { color: var(--hd-fg-muted); font-weight: 450; } .btn.n-sortb b { font-weight: 600; } .btn.n-sortb .ic { color: var(--hd-fg-muted); }

/* danger v-final: deep vermilion-red, barely-there shade, same quiet tactile edge as primary (was a loud orange gradient) */
.btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-strong, #a3300a) 82%, var(--hd-danger-solid, #c93d00)) 0%, var(--hd-danger-strong, #a3300a) 100%) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.14), inset 0 -1px 0 rgba(0,0,0,.22), 0 1px 1px rgba(16,20,38,.16), 0 2px 3px -1px rgba(16,20,38,.12) !important; }
.btn.d.hov:not(.dis):not([disabled]) { background: color-mix(in oklab, var(--hd-danger-strong, #a3300a) 90%, #000) !important; }
.btn.d.prs:not(.dis):not([disabled]) { background: color-mix(in oklab, var(--hd-danger-strong, #a3300a) 80%, #000) !important; }
[data-theme="dark"] .btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid) 94%, #fff) 0%, var(--hd-danger-solid) 100%) !important; }

.btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 88%, var(--hd-danger-strong, #a3300a)) 0%, color-mix(in oklab, var(--hd-danger-solid, #c93d00) 62%, var(--hd-danger-strong, #a3300a)) 100%) !important; }
.btn.d.hov:not(.dis):not([disabled]) { background: color-mix(in oklab, var(--hd-danger-solid, #c93d00) 45%, var(--hd-danger-strong, #a3300a)) !important; }
[data-theme="dark"] .btn.d:not(.dis):not([disabled]) { background: linear-gradient(180deg, color-mix(in oklab, var(--hd-danger-solid) 94%, #fff) 0%, var(--hd-danger-solid) 100%) !important; }

.btn.d.prs:not(.dis):not([disabled]) { background: var(--hd-danger-strong, #a3300a) !important; }
"""
