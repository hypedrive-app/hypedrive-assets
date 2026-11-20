XG = r"""
/* ===== XG: nw1-nw9 pass onto the approved language ===== */

/* --- destructive dialogs: 400 wide, pad 20, tile + title on one row, 40-tall controls --- */
.dialog.n-dlg { max-width: 400px !important; padding: 20px !important; gap: 0 !important; border-radius: 16px !important; display: grid !important; grid-template-columns: 36px 1fr; column-gap: 12px !important; row-gap: 0 !important; align-items: center; }
.dialog.n-dlg.n-sm { max-width: 400px !important; grid-template-columns: 1fr; }
.dialog.n-dlg .n-dti { grid-column: 1; grid-row: 1; width: 36px !important; height: 36px !important; border-radius: 10px !important; margin: 0 !important; }
.dialog.n-dlg .n-dti svg { width: 18px; height: 18px; }
.dialog.n-dlg .t-h2 { grid-column: 2; grid-row: 1; margin: 0 !important; font-size: 17px; line-height: 24px; font-weight: 600; letter-spacing: -0.01em; }
.dialog.n-dlg.n-sm .t-h2 { grid-column: 1; }
.dialog.n-dlg p { grid-column: 1 / -1; margin: 10px 0 0 !important; font-size: 14px !important; line-height: 20px !important; color: var(--hd-fg-muted); }
.dialog.n-dlg .field { grid-column: 1 / -1; margin-top: 16px !important; gap: 6px; }
.dialog.n-dlg .field label { font-size: 13.5px; font-weight: 600; line-height: 18px; }
.dialog.n-dlg .field .input { height: 40px !important; min-height: 40px !important; padding: 0 12px; font-size: 14px; }
.dialog.n-dlg .n-dlf { grid-column: 1 / -1; margin-top: 20px !important; gap: 8px; justify-content: flex-end; }
.dialog.n-dlg .n-dlf .btn { height: 40px !important; min-height: 40px; padding: 0 16px; font-size: 14px; border-radius: 10px; }
.dialog.n-dlg .btn.d:not(.dis):not([disabled]) { background: var(--hd-danger-solid, #c93d00) !important; }

/* --- offline banners: slim 44 rows, white surface, hairline, one signal (the glyph) --- */
.n-bwrap { gap: 8px !important; }
.n-banner { min-height: 44px !important; height: 44px; padding: 0 8px 0 14px !important; gap: 8px !important; border-radius: 12px !important; font-size: 14px; background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, var(--hd-border)); color: var(--hd-fg-muted) !important; }
[data-theme="dark"] .n-banner { background: var(--hd-surface-raised) !important; }
.n-banner b { color: var(--hd-fg) !important; font-weight: 600; }
.n-banner span { color: var(--hd-fg-muted) !important; }
.n-banner.warn > .ic { color: var(--hd-warning) !important; } .n-banner.ok > .ic { color: var(--hd-success) !important; }
.n-banner .btn.link { all: unset; box-sizing: border-box; height: 28px; padding: 0 10px; border-radius: 8px; display: inline-flex; align-items: center; font-size: 13px; font-weight: 560; color: var(--hd-fg-muted) !important; text-decoration: none !important; cursor: pointer; }
.n-banner .btn.link:hover { background: var(--n-hover); color: var(--hd-fg) !important; }

/* --- creator card · vertical: compact, one stats line --- */
.card.n-cc { padding: 16px !important; display: grid !important; grid-template-columns: auto auto; justify-content: center; justify-items: center; align-content: start; row-gap: 0 !important; column-gap: 8px; text-align: center; height: 100%; }
.n-cc > * { grid-column: 1 / -1; }
.n-cav { width: 64px !important; height: 64px !important; margin: 0 0 10px !important; }
.n-cc .n-cn { justify-content: center; gap: 4px; } .n-cc .n-cn b { font-size: 15px; font-weight: 600; letter-spacing: -0.01em; line-height: 20px; }
.n-cc > .t-small { font-size: 13px !important; line-height: 18px; margin-top: 2px; }
.n-cc > .n-plat { grid-column: 1; justify-self: end; display: inline-flex; margin: 10px 0 0 !important; gap: 12px !important; font-size: 13px; white-space: nowrap; }
.n-cc > .n-plat span { gap: 4px; } .n-cc .n-plat svg { width: 16px; height: 16px; }
.n-cc > .n-cr { grid-column: 2; justify-self: start; margin: 10px 0 0 !important; font-size: 13px; white-space: nowrap; }
.n-cc > .n-pf { margin-top: 14px !important; padding-top: 0 !important; width: 100%; align-self: end; }
.n-cc > .n-pf .btn.p { height: 36px !important; min-height: 36px; font-size: 14px; border-radius: 10px; }

/* --- product card · horizontal: 104 row, photo flush left --- */
.card.n-ph2 { min-height: 104px !important; height: 104px; }
.card.n-ph2 > img { width: 104px !important; height: 104px !important; min-height: 104px !important; }
.n-ph2 .n-hb { gap: 1px !important; padding: 0 12px 0 16px !important; }
.n-ph2 .n-hbr { font-size: 12.5px; line-height: 16px; }
.n-ph2 .n-hpt { font-size: 15px; line-height: 20px; }
.n-ph2 .n-hee { font-size: 13.5px; line-height: 18px; } .n-ph2 .n-hee b { font-weight: 600; }
.n-ph2 .n-hlf { font-size: 12.5px; line-height: 16px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-ph2 .n-he .btn { height: 34px !important; min-height: 34px; padding: 0 14px; font-size: 13.5px; border-radius: 10px; }

/* --- creator card · horizontal: no overflow, 44 avatar, ellipsis --- */
.card.n-ch { padding: 12px 12px 12px 14px !important; gap: 12px !important; min-width: 0; overflow: hidden; }
.n-ch > img, .n-ch .n-chav { width: 44px !important; height: 44px !important; border-radius: 50%; flex: none; }
.n-ch .n-chav .av { width: 44px !important; height: 44px !important; font-size: 15px !important; }
.n-ch .n-cb2 { display: flex !important; flex-flow: row wrap; align-items: center; column-gap: 4px; row-gap: 2px; min-width: 0; }
.n-ch .n-cn { display: contents !important; }
.n-ch .n-cn b { order: 1; font-size: 15px; font-weight: 600; white-space: nowrap; line-height: 20px; }
.n-ch .n-cn svg { order: 2; }
.n-ch .n-cb2::after { content: ""; order: 3; flex-basis: 100%; height: 0; }
.n-ch .n-cn .t-small { order: 4; margin: 0 !important; flex: 0 1 auto; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 13px; line-height: 18px; }
.n-ch .n-plat { order: 5; margin: 0 0 0 8px !important; gap: 10px !important; font-size: 13px; flex: none; white-space: nowrap; }
.n-ch .n-plat svg { width: 16px; height: 16px; }
.n-ch .n-hc2 .btn { height: 34px !important; padding: 0 14px; font-size: 13.5px; border-radius: 10px; }

/* --- command palette: calm, modern; no keycaps, underline tabs, 40 rows --- */
.dialog.n-cmd { max-width: 560px !important; border-radius: 16px !important; overflow: hidden; }
.n-cmd kbd, .n-cmd .kbd { all: unset; font-family: var(--font-ui); font-size: 12.5px; color: var(--hd-fg-subtle); letter-spacing: 0; }
.n-cmd kbd + kbd { margin-left: 2px; }
.n-cmd .n-cin { height: 52px !important; padding: 0 16px !important; font-size: 15px !important; gap: 10px !important; color: var(--hd-fg) !important; }
.n-cmd .n-cin > .ic { color: var(--hd-fg-muted); width: 18px; height: 18px; }
.n-cmd .n-cin .n-q { flex: 1; }
.n-cmd .n-tabs { gap: 20px !important; padding: 0 16px !important; height: 40px; align-items: stretch; }
.n-cmd .n-tabs span { height: auto !important; padding: 0 !important; border-radius: 0 !important; background: none !important; font-size: 13.5px !important; font-weight: 560; color: var(--hd-fg-muted) !important; box-shadow: none; position: relative; align-items: center; }
.n-cmd .n-tabs span b { color: var(--hd-fg-subtle) !important; font-size: 12.5px !important; font-weight: 500 !important; }
.n-cmd .n-tabs span.on { color: var(--hd-fg) !important; }
.n-cmd .n-tabs span.on::after { content: ""; position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; border-radius: 2px; background: var(--hd-accent); }
.n-cmd .n-cs { padding: 4px 8px 8px !important; gap: 0 !important; }
.n-cmd .n-gh { display: block; padding: 10px 10px 4px; font-size: 12.5px; font-weight: 560; color: var(--hd-fg-subtle); text-transform: none; letter-spacing: 0; }
.n-cmd .n-ci { height: 40px !important; padding: 0 10px !important; border-radius: 8px !important; font-size: 14px !important; gap: 10px !important; }
.n-cmd .n-ci > .ic { width: 16px; height: 16px; margin: 0 6px 0 6px !important; color: var(--hd-fg-muted); }
.n-cmd .n-ci img { width: 28px !important; height: 28px !important; border-radius: 6px !important; }
.n-cmd .n-ci img.n-r { border-radius: 50% !important; }
.n-cmd .n-ci .n-t { flex: none; } .n-cmd .n-ci .n-t b { font-weight: 600; }
.n-cmd .n-ci .n-sub { font-size: 13px !important; color: var(--hd-fg-muted); }
.n-cmd .n-ci .n-sub b { font-weight: 560; color: var(--hd-fg); }
.n-cmd .n-ci.hl { background: var(--n-hover); }
.n-cmd .n-go, .n-cmd .n-k { margin-left: auto !important; display: inline-flex; gap: 2px; font-size: 12.5px; color: var(--hd-fg-subtle); }
.n-cmd .n-cf { padding: 0 16px !important; height: 40px; gap: 16px !important; font-size: 12.5px !important; color: var(--hd-fg-subtle) !important; }
.n-cmd .n-cf > span { gap: 4px; }
.n-cmd .n-cf .sp, .n-cmd .n-cf > span:last-child { display: none; }

/* --- swipe rows: tinted actions, one signal, no slabs --- */
.n-swa .a { width: 72px !important; font-size: 12px; font-weight: 560; gap: 4px; }
.n-swa .a.ok { background: var(--hd-success-subtle) !important; color: var(--hd-success-strong) !important; }
.n-swa .a.mu { background: color-mix(in oklab, var(--hd-fg) 8%, var(--hd-surface)) !important; color: var(--hd-fg) !important; }
.n-swa .a.dg { background: var(--hd-danger-subtle) !important; color: var(--hd-danger-strong) !important; }
.n-swa .a .ic { width: 18px; height: 18px; }

/* --- copy field: small white secondary inside the field --- */
.input.n-copy .btn.s:not(.dis):not([disabled]):not(.n-done) { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, var(--hd-border)) !important; box-shadow: 0 1px 1px rgba(16,20,38,.05) !important; height: 28px !important; margin: 0 !important; align-self: center; padding: 0 10px; font-size: 13px; }
[data-theme="dark"] .input.n-copy .btn.s:not(.dis):not([disabled]):not(.n-done) { background: var(--hd-surface-raised) !important; box-shadow: none !important; }
.input.n-copy .btn.n-done { height: 28px !important; margin: 0 !important; align-self: center; font-size: 13px; }
.input.n-copy .btn.g { height: 28px !important; margin: 0 !important; align-self: center; background: none !important; }
.n-swa .a + .a { box-shadow: inset 1px 0 0 var(--hd-surface); }
.field:has(.n-copy .n-done) .help { display: none; }

/* --- copy field (round 2): 44 tall, 32 white secondary inset 6, no fills --- */
.input.n-copy { height: 44px !important; min-height: 44px !important; padding: 0 6px 0 14px !important; }
.input.n-copy .n-val { font-size: 15px !important; font-variant-numeric: tabular-nums; }
.input.n-copy .btn.s:not(.dis):not([disabled]):not(.n-done), .input.n-copy .btn.s.n-done:not(.dis):not([disabled]) { height: 32px !important; padding: 0 12px !important; font-size: 13.5px !important; background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, var(--hd-border)) !important; box-shadow: 0 1px 1px rgba(16,20,38,.05) !important; margin: 0 !important; }
[data-theme="dark"] .input.n-copy .btn.s:not(.dis):not([disabled]), [data-theme="dark"] .input.n-copy .btn.s.n-done:not(.dis):not([disabled]) { background: var(--hd-surface-raised) !important; box-shadow: none !important; }
.input.n-copy .btn.n-done, .input.n-copy .btn.s.n-done:not(.dis):not([disabled]) { color: var(--hd-success-strong) !important; }
.input.n-copy .btn.n-done .ic { color: var(--hd-success) !important; }
.input.n-copy.dis { background: none !important; }
.input.n-copy.dis .n-val { color: var(--hd-fg-subtle); }
.input.n-copy.dis .btn { height: 32px !important; background: none !important; border: 1px solid var(--hd-hairline, var(--hd-border)) !important; box-shadow: none !important; margin: 0 !important; color: var(--hd-fg-subtle) !important; opacity: .7; }

/* --- avatar upload: 64 everywhere, one left edge --- */
.n-avu { gap: 16px !important; align-items: center; }
.n-av, .n-av.up { width: 64px !important; height: 64px !important; margin: 0 !important; }
.n-av .n-ph { background: none !important; border: 1.5px dashed var(--hd-edge, var(--hd-border)) !important; box-shadow: none !important; }
.n-av.up > img { opacity: .6; }
.n-ringo { left: 0 !important; top: 0 !important; width: 64px !important; height: 64px !important; }
.n-avt { gap: 2px !important; }
.n-avt > b { font-size: 15px; } .n-avt .t-small { font-size: 13px; }
.n-avt .n-act { margin-top: 8px !important; gap: 8px; }
.n-avt .n-act .btn { height: 32px !important; min-height: 32px; padding: 0 12px; font-size: 13.5px; }
.n-avt .n-act .btn.g { margin-left: 0 !important; color: var(--hd-fg-muted) !important; }
.n-avt .n-act .btn.g:only-child { margin-left: -12px !important; }
.n-avt .n-act .btn.g:nth-child(2) { color: var(--hd-danger-strong) !important; margin-left: 0 !important; }
.n-avu:has(.up) { gap: 16px !important; }

/* ===== nw9 chat thread: calm messenger ===== */
.nw9 .t-thr { background: var(--hd-surface) !important; }
[data-theme="dark"] .nw9 .t-thr { background: var(--hd-surface-raised) !important; }
.nw9 .t-head { padding: 12px 16px !important; gap: 12px !important; }
.nw9 .t-head b { font-size: 15px; font-weight: 600; line-height: 20px; } .nw9 .t-head span { font-size: 13px; line-height: 18px; }
.nw9 .t-lg { width: 28px; height: 28px; border-radius: 8px; flex: none; display: inline-grid !important; place-items: center; background: var(--hd-surface); border: 1px solid var(--hd-edge, var(--hd-border)); color: #8a5a00 !important; font-size: 11px !important; font-weight: 700; letter-spacing: 0; box-shadow: 0 1px 2px rgba(16,20,38,.06); }
[data-theme="dark"] .nw9 .t-lg { background: var(--hd-surface); color: #f2b84b !important; box-shadow: none; }
.nw9 .t-head .t-lg { width: 36px; height: 36px; border-radius: 10px; font-size: 13px !important; }
.nw9 .t-thr .t-body { background: none !important; padding: 16px 16px 8px !important; gap: 2px !important; }
.nw9 .t-day { margin: 0 0 14px !important; font-size: 12px; font-weight: 560; color: var(--hd-fg-muted); }
.nw9 .t-m { max-width: 68% !important; gap: 8px !important; }
.nw9 .t-m.last { margin-bottom: 14px !important; }
.nw9 .t-c { gap: 2px !important; }
.nw9 .t-b { padding: 9px 13px !important; font-size: 14.5px !important; line-height: 20px !important; border-radius: 18px !important; border: 0 !important; background: color-mix(in oklab, var(--hd-fg) 6%, var(--hd-surface)) !important; color: var(--hd-fg) !important; }
[data-theme="dark"] .nw9 .t-m.in .t-b, [data-theme="dark"] .nw9 .t-file { background: color-mix(in oklab, #fff 4%, var(--hd-surface-raised)) !important; }
.nw9 .t-m.out .t-b { background: var(--hd-accent) !important; color: #fff !important; }
.nw9 .t-m.in .t-b { border-bottom-left-radius: 6px !important; }
.nw9 .t-m.in:not(.last) + .t-m.in .t-b { border-top-left-radius: 6px !important; }
.nw9 .t-m.out .t-b { border-bottom-right-radius: 6px !important; }
.nw9 .t-m.out:not(.last) + .t-m.out .t-b { border-top-right-radius: 6px !important; }
.nw9 .t-meta { font-size: 11.5px !important; line-height: 16px; color: var(--hd-fg-muted) !important; padding: 2px 4px 0 !important; }
.nw9 .t-m.hm .t-av { margin-bottom: 20px !important; }
.nw9 .t-file { width: 260px !important; padding: 10px 14px 10px 10px !important; gap: 10px !important; border: 0 !important; border-radius: 18px 18px 18px 6px !important; background: color-mix(in oklab, var(--hd-fg) 6%, var(--hd-surface)) !important; }
.nw9 .t-m.in:not(.last) .t-file { border-bottom-left-radius: 6px !important; }
.nw9 .t-ft { width: 36px; height: 36px; border-radius: 10px; display: grid; place-items: center; flex: none; background: var(--hd-surface); border: 1px solid var(--hd-edge, var(--hd-border)); color: var(--hd-fg-muted); }
[data-theme="dark"] .nw9 .t-ft { background: var(--hd-surface-raised); }
.nw9 .t-file b { font-size: 14px; font-weight: 560; line-height: 20px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.nw9 .t-file span { font-size: 12.5px; line-height: 16px; }
.nw9 .t-dl { display: grid; place-items: center; color: var(--hd-fg-subtle); flex: none; }
.nw9 .t-img { width: 240px !important; height: 180px !important; border-radius: 18px !important; border: 1px solid var(--hd-edge, var(--hd-border)); }
.nw9 .t-m.out:not(.last) .t-img { border-bottom-right-radius: 6px !important; }
.nw9 .t-typ { height: 36px !important; padding: 0 12px !important; gap: 4px; }
.nw9 .t-comp { background: none !important; border-top: 1px solid var(--hd-edge, var(--hd-border)); }
.nw9 .t-m.hm .t-meta { white-space: nowrap; }

/* ===== review pass: media, inline edit, combobox clear ===== */
.m-play { width: 44px !important; height: 44px !important; margin: -22px 0 0 -22px !important; }
.m-play svg { width: 18px; height: 18px; }
.m-yt .m-play { width: 52px !important; height: 52px !important; margin: -26px 0 0 -26px !important; }
.m-up.err { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, var(--hd-border)) !important; color: var(--hd-fg) !important; }
.m-up.err > .ic { color: var(--hd-danger) !important; }
.m-up.err b { color: var(--hd-fg); font-weight: 600; }
.m-up.err .btn.link { all: unset; box-sizing: border-box; height: 28px; padding: 0 10px; border-radius: 8px; display: inline-flex; align-items: center; font-size: 12.5px; font-weight: 560; color: var(--hd-danger-strong) !important; text-decoration: none !important; cursor: pointer; }
.m-up.err .btn.link:hover { background: var(--hd-danger-subtle); }
.n-iev2 { background: var(--n-hover) !important; }
.n-clr { width: 18px; height: 18px; background: color-mix(in oklab, var(--hd-fg) 10%, transparent) !important; color: var(--hd-fg-muted) !important; }

/* ===== nw7 round 2: one primary per view, secondary-sm actions, mono glyphs ===== */
.n-trio.n-cgrid { grid-template-columns: repeat(3, minmax(0, 260px)); justify-content: start; }
.n-cc .n-plat svg, .n-ch .n-plat svg { filter: grayscale(1); opacity: .62; }
.n-cc .n-plat .ic:not(.icf), .n-ch .n-plat .ic:not(.icf) { color: var(--hd-fg-muted); }
.n-cc .n-cr svg, .n-ch .n-cr svg { filter: none; opacity: 1; }
.n-cav { width: 56px !important; height: 56px !important; }
.card.n-cc { padding: 16px !important; }
.n-cc > .n-pf { width: 100%; }
.n-cc > .n-pf .btn { width: 100% !important; height: 34px !important; min-height: 34px; font-size: 13.5px; }
.n-ph2 .n-he .btn, .n-ch .n-hc2 .btn { height: 34px !important; min-height: 34px; }
.n-ch > img, .n-ch .n-chav, .n-ch .n-chav .n-ini { width: 40px !important; height: 40px !important; }
.n-ch .n-chav { display: block; }
.n-ini { display: grid; place-items: center; border-radius: 50%; background: var(--hd-success-subtle); color: var(--hd-success-strong); font-size: 14px; font-weight: 600; }

/* ===== nw8 gallery: capped hero, 64 thumbs, quiet selection ===== */
.m-gal { grid-template-columns: 64px 416px !important; gap: 16px !important; justify-content: center; }
.m-rail { gap: 10px; }
.m-th { width: 64px !important; height: 64px !important; border-radius: 10px !important; }
.m-th:not(.on) { opacity: .7 !important; }
.m-th.on { outline: 2px solid var(--hd-fg) !important; outline-offset: 2px; border-color: transparent !important; opacity: 1; }
.m-hero { width: 416px; height: 520px; aspect-ratio: auto !important; border-radius: 16px !important; border: 1px solid var(--hd-edge, var(--hd-border)) !important; }
.m-chip { background: rgba(13,14,18,.62) !important; color: #fff; font-size: 12px; }
.m-hero .m-disc { width: 36px; height: 36px; }

/* ===== nw8 mobile carousel ===== */
.m-top { height: 48px; }
.m-top .btn .ic, .m-top .btn svg { width: 22px !important; height: 22px !important; }
.m-top .btn { background: none !important; border: 0 !important; box-shadow: none !important; }
.m-track { gap: 8px !important; padding-left: 16px !important; }
.m-slide { flex: 0 0 calc(100% - 16px - 20px) !important; border-radius: 16px !important; border-color: var(--hd-edge, var(--hd-border)) !important; }
.m-dots.on-canvas { gap: 6px !important; padding: 12px 0 2px !important; }
.m-dots.on-canvas i { width: 6px !important; height: 6px !important; border-radius: 3px !important; background: var(--hd-fg) !important; opacity: .18 !important; }
.m-dots.on-canvas i.on { width: 16px !important; background: var(--hd-accent) !important; opacity: 1 !important; }
.m-info .t-h2 { font-size: 17px !important; line-height: 24px; font-weight: 600; }
.m-info .n-rw { font-size: 14px; color: var(--hd-fg-muted); gap: 4px; align-items: baseline; }
.m-info .n-rw b { font-family: var(--font-ui); font-size: 14px !important; line-height: 20px !important; font-weight: 600; color: var(--hd-fg); letter-spacing: 0; }
[data-theme="dark"] .n-cc .n-plat svg, [data-theme="dark"] .n-ch .n-plat svg { filter: grayscale(1) brightness(2.4); opacity: .75; }
"""
