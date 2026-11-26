# "after" standard layer: bigger type, one hero surface, inline meta rows. Appended to uikit.CSS.
XCSS = r"""
.x-head { font-family: var(--font-brand); font-size: 34px; line-height: 38px; font-weight: 650; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; text-wrap: balance; }
.x-head span { color: var(--hd-fg-muted); }
.x-title { font-family: var(--font-brand); font-size: 32px; line-height: 35px; font-weight: 650; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; }
.x-who { display: flex; align-items: center; gap: 10px; } .x-who img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; display: block; }
.x-who b { display: flex; align-items: center; gap: 4px; font-size: 15px; font-weight: 600; } .x-who small { display: block; font-size: 13px; color: var(--hd-fg-muted); }
.x-hero { position: relative; z-index: 1; border-radius: 24px; overflow: hidden; height: 300px; flex: none; margin-top: 10px; }
.x-stack { position: relative; } .x-stack > i { display: block; height: 22px; margin: 0 24px -14px; border-radius: 16px 16px 0 0; background: var(--hd-accent); opacity: .28; }
.x-stack > i + i { margin: 0 12px -14px; opacity: .55; }
.x-deck { display: flex; justify-content: center; gap: 6px; margin-top: 10px; } .x-deck i { width: 6px; height: 6px; border-radius: 4px; background: var(--hd-track-strong); } .x-deck i.on { width: 18px; background: var(--hd-accent); }
.x-hero > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; border-radius: 0 !important; }
.x-hero .sh { position: absolute; inset: auto 0 0 0; height: 62%; background: linear-gradient(to top, rgba(9,11,18,.86), rgba(9,11,18,0)); }
.x-hero .top { position: absolute; top: 14px; left: 14px; right: 14px; display: flex; justify-content: space-between; align-items: center; }
.x-pill { height: 30px; padding: 0 12px; border-radius: 999px; display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; background: rgba(255,255,255,.92); color: #121417; }
.x-hero .bt { position: absolute; left: 18px; right: 18px; bottom: 18px; color: #fff; display: flex; align-items: flex-end; gap: 12px; }
.x-hero .bt .t { flex: 1; } .x-hero .bt b { display: block; font-family: var(--font-brand); font-size: 26px; line-height: 29px; font-weight: 650; letter-spacing: -0.03em; white-space: nowrap; }
.x-hero .bt small { display: block; font-size: 14px; color: rgba(255,255,255,.78); margin-top: 4px; }
.x-go { width: 56px; height: 56px; border-radius: 50%; background: #fff; color: #121417; display: flex; align-items: center; justify-content: center; flex: none; }
.x-meta { display: flex; justify-content: space-between; padding: 14px 2px; border-top: 1px solid var(--hd-border); border-bottom: 1px solid var(--hd-border); }
.x-meta div { display: flex; align-items: center; gap: 6px; font-size: 14px; color: var(--hd-fg-muted); } .x-meta b { color: var(--hd-fg); font-weight: 650; }
.x-meta .ic { color: var(--hd-fg-muted); }
.x-bar { position: absolute; left: 18px; right: 18px; bottom: 30px; height: 64px; border-radius: 999px; background: var(--hd-surface); box-shadow: var(--hd-shadow-e3), 0 0 0 1px var(--hd-border); display: flex; align-items: center; justify-content: space-between; padding: 0 8px; z-index: 3; }
.x-bar .on { height: 48px; padding: 0 18px 0 14px; border-radius: 999px; background: var(--hd-accent); color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 15px; }
.x-bar .d { width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--hd-fg-muted); }
.x-photo { position: relative; height: 410px; flex: none; margin: -50px 0 0; }
.x-photo img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.x-photo .tb { position: absolute; top: 58px; left: 16px; right: 16px; display: flex; justify-content: space-between; }
.x-disc { width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,.92); color: #121417; display: flex; align-items: center; justify-content: center; }
.x-sheet { position: relative; margin-top: -28px; border-radius: 24px 24px 0 0; background: var(--hd-canvas); padding: 22px 20px 0; display: flex; flex-direction: column; gap: 16px; flex: 1; }
.x-chips { display: flex; gap: 8px; } .x-chip { height: 36px; padding: 0 14px; border-radius: 10px; background: var(--hd-control); display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 560; }
.x-avs { display: flex; } .x-avs img { width: 30px; height: 30px; border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 2px var(--hd-canvas); margin-left: -8px; } .x-avs img:first-child { margin-left: 0; }
.x-cta { display: flex; gap: 10px; padding: 12px 20px 30px; margin-top: auto; } .x-cta .btn { flex: 1; } .x-cta .sq { width: 52px !important; height: 52px; flex: none !important; padding: 0; border-radius: 14px; }
.x-row { display: flex; align-items: center; gap: 12px; }
.x-tip { padding: 2px 0 2px 14px; border-left: 3px solid var(--hd-accent); font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); } .x-tip b { display: block; color: var(--hd-link); font-weight: 600; margin-bottom: 2px; }
.topbar.x-large { height: 60px; } .topbar.x-large .ttl.x-page { font-size: 32px; font-weight: 650; }
.x-page { font-family: var(--font-brand); font-size: 32px; line-height: 36px; font-weight: 650; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; }
.x-money { border-radius: 24px; background: var(--hd-inverse); color: var(--hd-inverse-fg); padding: 20px; display: flex; flex-direction: column; gap: 4px; }
.x-money small { font-size: 14px; color: color-mix(in oklab, var(--hd-inverse-fg) 72%, transparent); }
.x-money .v { font-family: var(--font-brand); font-size: 48px; line-height: 52px; font-weight: 650; letter-spacing: -0.04em; font-variation-settings: 'opsz' 96; }
.x-money .v span { font-size: 40px; letter-spacing: 0; margin-right: 1px; font-weight: 500; }
.x-money .btn.t { background: color-mix(in oklab, var(--hd-inverse-fg) 14%, transparent); color: var(--hd-inverse-fg); box-shadow: none; }
.x-tile { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex: none; }
.x-tile.cobalt { background: var(--hd-accent-subtle); color: var(--hd-tone-cobalt); } .x-tile.mint { background: var(--hd-success-subtle); color: var(--hd-success-strong); }
.x-tile.marigold { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); } .x-tile.vermilion { background: var(--hd-danger-subtle); color: var(--hd-danger-strong); }
.x-otp { display: flex; gap: 10px; } .x-otp span { width: 48px; height: 58px; border-radius: 14px; background: var(--hd-surface); box-shadow: 0 0 0 1px var(--hd-border-input) inset; display: flex; align-items: center; justify-content: center; font: 650 26px var(--font-brand); }
.x-otp span.on { box-shadow: 0 0 0 2px var(--hd-accent) inset; }
.x-tl { display: flex; flex-direction: column; } .x-tl .s { display: flex; gap: 14px; min-height: 58px; } .x-tl .k { width: 24px; display: flex; flex-direction: column; align-items: center; flex: none; }
.x-tl .k i { width: 24px; height: 24px; border-radius: 50%; background: var(--hd-track); display: flex; align-items: center; justify-content: center; color: #fff; flex: none; }
.x-tl .k em { flex: 1; width: 2px; background: var(--hd-track); margin: 4px 0; } .x-tl .s.done .k i, .x-tl .s.done .k em { background: var(--hd-accent); }
.x-tl .s.now .k i { background: var(--hd-surface); box-shadow: 0 0 0 2px var(--hd-accent) inset; } .x-tl .s.now .k i::after { content: ''; width: 10px; height: 10px; border-radius: 50%; background: var(--hd-accent); }
.x-tl b { display: block; font-size: 15px; font-weight: 600; } .x-tl small { display: block; font-size: 13px; color: var(--hd-fg-muted); margin-top: 2px; }
.x-ava { width: 60px; height: 60px; border-radius: 50%; object-fit: cover; display: block; }
/* ---- search + buttons refinement */
.phone .search, .phone .searchbar .search { height: 44px; border-radius: 12px; font-size: 16px; }
.searchbar .btn.link { font-weight: 560; }
.suggest .sg-x { margin-left: auto; color: var(--hd-fg-subtle); display: inline-flex; } .suggest .sg .sub .kbd { margin-left: 6px; }
.suggest .sg-logo { display: inline-flex; } .suggest .sg-logo .av { border-radius: 8px; }
.seg { display: inline-flex; padding: 3px; gap: 2px; border-radius: 12px; background: var(--hd-control); height: 44px; align-items: stretch; }
.seg span { display: flex; align-items: center; padding: 0 14px; border-radius: 10px; font-size: 14.5px; font-weight: 560; color: var(--hd-fg-muted); }
.seg span.on { background: var(--hd-surface); color: var(--hd-fg); box-shadow: 0 1px 2px rgba(16,20,38,.08), 0 0 0 1px var(--hd-border); }
.btn { white-space: nowrap; flex-shrink: 0; } .btn.block, .x-cta .btn:not(.sq) { flex-shrink: 1; }
.btn.icon { width: 44px; min-width: 44px; padding: 0; justify-content: center; } .btn.icon.sm { width: 32px; min-width: 32px; }
.btn.p { box-shadow: inset 0 1px 0 rgba(255,255,255,.14), inset 0 -1px 0 rgba(0,0,0,.18); }
.btn.p:active, .btn.p.prs { box-shadow: inset 0 1px 2px rgba(0,0,0,.22); }
.btngroup.split .btn.icon { width: 40px; min-width: 40px; }
.btngroup.split .btn + .btn { box-shadow: inset 1px 0 0 rgba(255,255,255,.30), inset 0 1px 0 rgba(255,255,255,.14), inset 0 -1px 0 rgba(0,0,0,.18); }
/* input prefix: inline inside the one field border (no inner box, no divider) */
.input .addon { align-self: center; margin: 0 -2px 0 0; padding: 0; border: 0 !important; background: none !important; border-radius: 0 !important; color: var(--hd-fg-muted); font-weight: 500; }
/* verification code: white fields, one clear active cell with a caret, 3 + 3 grouping */
.otp2 { display: flex; align-items: center; gap: 6px; }
.otp2 span { width: 48px; height: 48px; flex: none; border-radius: 12px; background: var(--hd-surface); box-shadow: inset 0 0 0 1px var(--hd-border-input); display: flex; align-items: center; justify-content: center; font: 600 24px/1 var(--font-brand); letter-spacing: -0.02em; color: var(--hd-fg); }
.otp2 span.f { box-shadow: inset 0 0 0 1px var(--hd-border-strong); }
.otp2 span.on { box-shadow: inset 0 0 0 2px var(--hd-focus), 0 0 0 3px var(--hd-focus-ring); }
.otp2 span.on::after { content: ''; width: 2px; height: 22px; border-radius: 1px; background: var(--hd-accent); }
.otp2 i { width: 8px; height: 2px; border-radius: 1px; background: var(--hd-border-strong); margin: 0; flex: none; }
.sb .sbsearch { background: var(--hd-surface) !important; box-shadow: 0 0 0 1px var(--hd-border) !important; color: var(--hd-fg-subtle); }
.sb .sbsearch .q { flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.row .tx small, .row .tx b, .x-tip, .t-body, p { text-wrap: pretty; }
[data-theme="dark"] .tabbar .on { color: var(--hd-link); }
.stars .ic { color: var(--hd-star) !important; } .stars .ic:last-child[style*="track"] { color: var(--hd-track-strong) !important; }
/* compact stat tiles: one-line label, value pinned to a shared bottom baseline */
.stat.compact { min-height: 76px; justify-content: space-between; }
.stat.compact .sl { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.stat.compact .sv { margin-top: auto; align-items: baseline; } .stat.compact .su { font-size: 13px; }
/* page header: every control is 44 tall and centred on the title line (title line-height 34 -> offset -5) */
.pg .ph { align-items: flex-start !important; }
.pg .ph > :not(.t) { height: 44px !important; margin-top: -5px; flex: none; box-sizing: border-box; display: inline-flex; align-items: center; }
.pg .ph > .search { width: 280px; }
/* device frame: brushed-titanium rim (gradient border), black bezel, concentric radii 60 / 57.5 / 48, Dynamic Island, metal side keys */
.pf .phone { position: relative; width: 390px; height: 844px; box-sizing: border-box; padding: 7.5px; border: 2.5px solid transparent; border-radius: 60px !important;
  background: linear-gradient(#050506, #050506) padding-box, linear-gradient(150deg, #9a9da4 0%, #4a4c52 22%, #7b7e85 48%, #34363b 74%, #8c8f96 100%) border-box !important;
  box-shadow: 0 1px 2px rgba(16,20,38,.10), 0 18px 36px -14px rgba(16,20,38,.30), 0 40px 80px -30px rgba(16,20,38,.22) !important; }
.pf .phone .scr { border-radius: 48px !important; }
.pf .phone .scr::after { content: ''; position: absolute; top: 11px; left: 50%; transform: translateX(-50%); width: 124px; height: 36px; border-radius: 24px; background: #000; z-index: 30; pointer-events: none; box-shadow: inset 0 0 0 1px #111; }
.pf .phone::before { content: ''; position: absolute; left: -5px; top: 166px; width: 3px; height: 32px; border-radius: 2px 0 0 2px; background: linear-gradient(90deg, #3a3c41, #8a8d94); box-shadow: 0 58px 0 0 #6b6e75, 0 122px 0 0 #6b6e75; }
.pf .phone::after { content: ''; position: absolute; right: -5px; top: 250px; width: 3px; height: 100px; border-radius: 0 2px 2px 0; background: linear-gradient(90deg, #8a8d94, #3a3c41); }
.pf .phone .sbar { padding: 6px 32px 0 42px; height: 54px; position: relative; z-index: 25; font-size: 16px; font-weight: 600; letter-spacing: -0.01em; }
.sbar .r { gap: 7px !important; }
/* ===== ONE button system: sizes sm 36 / md 44 / lg 52 · radius 10 / 12 / 14 · icon 16 / 18 / 20 · same anatomy for every variant ===== */
.btn { height: 44px !important; padding: 0 18px; border-radius: 12px !important; font-size: 15px !important; font-weight: 560 !important; gap: 8px; letter-spacing: -0.01em; line-height: 1; }
.btn .ic { width: 18px !important; height: 18px !important; }
.btn.sm { height: 36px !important; padding: 0 14px; border-radius: 10px !important; font-size: 14px !important; gap: 6px; } .btn.sm .ic { width: 16px !important; height: 16px !important; }
.btn.lg { height: 52px !important; padding: 0 22px; border-radius: 14px !important; font-size: 16px !important; gap: 10px; } .btn.lg .ic { width: 20px !important; height: 20px !important; }
.btn.icon { width: 44px !important; min-width: 44px !important; padding: 0 !important; } .btn.icon.sm { width: 36px !important; min-width: 36px !important; } .btn.icon.lg, .x-cta .sq { width: 52px !important; min-width: 52px !important; height: 52px !important; border-radius: 14px !important; }
.btn.icon .ic { width: 20px !important; height: 20px !important; }
.btn.link { height: auto !important; padding: 0 !important; min-width: 0 !important; border-radius: 4px !important; }
.btn.g:not(.dis) { background: transparent; color: var(--hd-link); box-shadow: none; } .btn.g.hov:not(.dis), .btn.g:hover:not(.dis) { background: var(--hd-bg-subtle); }
.btn.g.prs:not(.dis) { background: var(--hd-control); }
.btn.dis, .btn[disabled] { background: var(--hd-control) !important; color: var(--hd-fg-subtle) !important; box-shadow: none !important; }
.x-money .btn { height: 44px !important; }
.shell .toolbar .btn.sm, .shell .toolbar .chip { height: 36px !important; border-radius: 10px !important; }
.pg .ph .chip { border-radius: 12px !important; font-size: 15px; font-weight: 560; padding: 0 16px; gap: 8px; }
/* ---- desktop shell: sidebar header row matches the top bar (same 56px height, one shared hairline) */
.hdr { height: 56px !important; }
.sb { padding-top: 0 !important; } .sb > img:first-child { height: 24px !important; margin: 0 -12px 12px !important; padding: 16px 20px 15px; box-sizing: content-box; border-bottom: 1px solid var(--hairline); align-self: stretch !important; object-fit: contain; object-position: left center; }

/* ===== restored after an accidental overwrite (append-only from here) ===== */
/* secondary button = white (owner): surface fill + hairline so it stays visible on the canvas */
.btn.s:not(.dis):not([disabled]) { background: var(--hd-surface); color: var(--hd-fg); box-shadow: inset 0 0 0 1px var(--hd-border-strong), 0 1px 1px rgba(16,20,38,.04); }
.btn.s.hov:not(.dis) { background: var(--hd-bg-subtle); }
.btn.s.prs:not(.dis) { background: var(--hd-control); box-shadow: inset 0 0 0 1px var(--hd-border-strong); }
.btn.s.foc { box-shadow: inset 0 0 0 1px var(--hd-border-strong), 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
[data-theme="dark"] .btn.s:not(.dis):not([disabled]) { background: var(--hd-surface-raised); }
/* layered shadows (owner): in-flow surfaces e1 (ring + contact + ambient), floating e2/e3 */
.card, .row:not(.sel), .panel, .group, .banner, .stat, .x-money { box-shadow: var(--hd-shadow-e1) !important; }
.shell .rc2.open { box-shadow: 0 0 0 2px var(--hd-accent), var(--hd-shadow-e1) !important; }
.menu, .toast, .suggest, .tooltip, .dialog { box-shadow: var(--hd-shadow-e2) !important; } .sheet { box-shadow: var(--hd-shadow-e3) !important; }
/* bottom bars run through the home-indicator safe area */
.tabbar + .home-ind, .cta + .home-ind { background: var(--hd-surface); }
.cta[style*="transparent"] + .home-ind { background: transparent; }
.tabbar { border-bottom: 0 !important; } .cta { padding-bottom: 8px !important; }
/* split button keeps one continuous shape */
.btngroup .btn { border-radius: 0 !important; } .btngroup .btn:first-child { border-radius: 12px 0 0 12px !important; } .btngroup .btn:last-child { border-radius: 0 12px 12px 0 !important; }
/* avatar stacks: overlap 8px max, ring in the surface colour, initials never cut */
.avs .av { margin-left: -4px !important; -webkit-mask: none !important; mask: none !important; box-shadow: 0 0 0 2px var(--hd-surface) !important; } .avs .av:first-child { margin-left: 0 !important; }
/* ===== stat cards as craft ===== */
.stat:not(.compact) .sv b { font-family: var(--font-brand) !important; font-weight: 600 !important; font-size: 32px !important; letter-spacing: -0.035em !important; line-height: 1 !important; }
.stat:not(.compact) .sv .su { font-size: 15px; color: var(--hd-fg-subtle); font-weight: 500; }
.stat .sl { font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); }
.stat .vz .spk { position: relative; }
.spk-dot { position: absolute; right: -4px; width: 9px; height: 9px; margin-top: -4.5px; border-radius: 50%; background: var(--hd-chart, var(--hd-accent)); box-shadow: 0 0 0 3px var(--hd-surface), 0 0 0 4px color-mix(in oklab, var(--hd-accent) 25%, transparent); }
.mbars { gap: 5px !important; } .mbars i { border-radius: 5px !important; background: color-mix(in oklab, var(--hd-accent) 16%, var(--hd-surface)) !important; }
.mbars i.hl { background: var(--hd-accent) !important; }
.segs { display: flex; gap: 4px; height: 10px; } .segs i { flex: 1; border-radius: 3px; background: var(--hd-track); position: relative; overflow: hidden; }
.segs i.on { background: var(--hd-accent); } .segs i b { position: absolute; inset: 0 auto 0 0; background: var(--hd-accent); }
.ringcard { display: flex; align-items: center; gap: 16px; padding: 16px 18px !important; } .ringcard > div:last-child { min-width: 0; } .ringcard .t-h3, .ringcard span { white-space: normal !important; }
.legend i { border-radius: 3px !important; }
/* ===== badges: high-contrast tint, solid status icon, no border ===== */
.badge { height: 22px; padding: 0 8px 0 6px !important; border-radius: 6px !important; font-size: 12px !important; font-weight: 600 !important; gap: 4px !important; box-shadow: none !important; border: 0 !important; line-height: 1; }
.badge .ic { width: 13px !important; height: 13px !important; flex: none; }
.badge.success { background: var(--hd-success-subtle) !important; color: var(--hd-success-strong) !important; }
.badge.warning { background: var(--hd-warning-subtle) !important; color: var(--hd-warning-strong) !important; }
.badge.danger { background: var(--hd-danger-subtle) !important; color: var(--hd-danger-strong) !important; }
.badge.info { background: var(--hd-accent-subtle) !important; color: var(--hd-link) !important; }
.badge.neutral:not([style]) { background: var(--hd-control) !important; color: var(--hd-fg) !important; }
.badge.solid { background: var(--hd-accent) !important; color: #fff !important; padding: 0 7px !important; }
.bdot { display: none !important; }
/* ===== chips: tinted fill, icon always, no border; selected = accent tint + solid icon ===== */
.chip { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; box-shadow: none !important; color: var(--hd-fg) !important; font-weight: 560; }
.chip .ic { color: var(--hd-fg-muted); } .chip .plat, .chip img { border-radius: 5px; }
.chip.on { background: var(--hd-accent-subtle) !important; border-color: transparent !important; color: var(--hd-link) !important; } .chip.on .ic { color: var(--hd-accent) !important; }
.chip.foc { box-shadow: 0 0 0 2px var(--ring-gap, var(--hd-surface)), 0 0 0 4px var(--hd-focus) !important; }
/* photo under the status bar: a soft top scrim so time and icons stay legible (iOS pattern) */
.x-photo::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 120px; z-index: 1; pointer-events: none;
  background: linear-gradient(180deg, rgba(244,245,248,.86) 0%, rgba(244,245,248,.55) 45%, rgba(244,245,248,0) 100%); }
.x-photo .tb { z-index: 2; }
/* product detail: photo pager + buy bar (price/earning left, CTA right) */
.x-dots { position: absolute; left: 0; right: 0; bottom: 40px; display: flex; justify-content: center; gap: 6px; z-index: 2; }
.x-dots i { width: 6px; height: 6px; border-radius: 3px; background: rgba(255,255,255,.6); box-shadow: 0 0 0 1px rgba(16,20,38,.08); } .x-dots i.on { width: 18px; background: #fff; }
.x-buy { align-items: center; gap: 16px !important; border-top: 1px solid var(--hd-border); background: var(--hd-surface) !important; padding: 12px 20px 10px !important; }
.x-buy .x-earn { display: flex; flex-direction: column; } .x-buy .x-earn small { font-size: 12px; color: var(--hd-fg-muted); }
.x-buy .x-earn b { font-family: var(--font-brand); font-size: 22px; font-weight: 600; letter-spacing: -0.03em; color: var(--hd-success-strong); }
.x-buy .btn { flex: 1; } .x-buy + .home-ind { background: var(--hd-surface); }
.x-day { font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); margin-bottom: -6px; }
/* ===== tinted surfaces: text always on the -strong role (light 7.8-8.5:1, dark >11:1); icons keep the mid tone as the colour cue ===== */
.notice.info, .badge.info, .chip.on, .x-tile.cobalt { color: var(--hd-info-strong) !important; }
.notice.success, .badge.success, .x-tile.mint { color: var(--hd-success-strong) !important; }
.notice.warning, .badge.warning, .x-tile.marigold { color: var(--hd-warning-strong) !important; }
.notice.danger, .badge.danger, .x-tile.vermilion { color: var(--hd-danger-strong) !important; }
.notice.info > .ic, .chip.on .ic { color: var(--hd-accent) !important; } .notice.success > .ic { color: var(--hd-success) !important; }
.notice.warning > .ic { color: var(--hd-warning) !important; } .notice.danger > .ic { color: var(--hd-danger) !important; }
.notice b { color: inherit; font-weight: 650; }
.tbl tr.sel-row td, .rc2.sel, .rc2.on { color: var(--hd-fg) !important; }
.stat.compact .sv b { font-family: var(--font-brand) !important; font-weight: 600 !important; letter-spacing: -0.03em !important; }
/* crisp in-flow surfaces: native 1px ring + contact + faint ambient (no SVG) */
.card, .row:not(.sel), .panel, .group, .stat, .banner, .rc2, .ws { border: 1px solid var(--hd-edge, rgba(16,20,38,.12)) !important; box-shadow: 0 1px 1px rgba(16,20,38,.04), 0 2px 4px -1px rgba(16,20,38,.04) !important; }   /* real borders snap to device pixels: always one crisp line */
.x-money { box-shadow: 0 1px 2px rgba(16,20,38,.08) !important; }
[data-theme="dark"] .card, [data-theme="dark"] .row:not(.sel), [data-theme="dark"] .panel, [data-theme="dark"] .group, [data-theme="dark"] .stat, [data-theme="dark"] .banner, [data-theme="dark"] .rc2 { border-color: var(--hd-edge, rgba(255,255,255,.10)) !important; box-shadow: 0 1px 2px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.05) !important; }
.menu, .toast, .suggest, .dialog { box-shadow: var(--hd-shadow-e2) !important; }
/* ===== inset shadows: things you type into or that hold a value sit slightly recessed ===== */
.input:not(.foc):not(.err):not(.ok):not(.dis), .otp2 span:not(.on), .x-otp span:not(.on) { box-shadow: inset 0 1px 2px rgba(16,20,38,.06) !important; }
.search:not(.foc), .sbsearch { box-shadow: inset 0 1px 2px rgba(16,20,38,.05) !important; }
.bar, .tape, .segs i:not(.on), .switch:not(.on), .seg, .slider .rail, .x-tl .k em { box-shadow: inset 0 1px 1px rgba(16,20,38,.08); }
.switch.on { box-shadow: inset 0 1px 2px rgba(0,0,0,.18); }
.btn.prs:not(.dis) { box-shadow: inset 0 2px 3px rgba(0,0,0,.18) !important; }
[data-theme="dark"] .input:not(.foc):not(.err):not(.ok):not(.dis), [data-theme="dark"] .search:not(.foc), [data-theme="dark"] .otp2 span:not(.on) { box-shadow: inset 0 1px 2px rgba(0,0,0,.35) !important; }
[data-theme="dark"] .bar, [data-theme="dark"] .tape, [data-theme="dark"] .switch:not(.on), [data-theme="dark"] .seg { box-shadow: inset 0 1px 2px rgba(0,0,0,.4); }
"""
