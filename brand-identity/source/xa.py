# Section polish layer (xa). Appended after XLEAD.
XA = r"""
/* kit sections 1-6: the thread-body class collides with the type sample, so the kit uses its own */
.sec .kt-body { font-size: 15px; line-height: 22px; }
.sec .box { box-shadow: none; border: 1px solid var(--hd-edge); }
.sec .box .lbl { letter-spacing: 0; }
.sec .tstack { display: flex; flex-direction: column; gap: 6px; }
.sec .tstack .lbl { margin-top: 16px; margin-bottom: 4px; }
.sec .stat .rhist { display: none; }
.sec .sheetdemo { box-shadow: none; border: 1px solid var(--hd-edge); }
.sec .kt-body + :is(.check, .radio, .switch) { margin-left: 20px; }
.sec .box.stack:has(> .flexw > .switch) { gap: 14px; }
"""
XA += r"""
/* ===== round 1 ===== */
/* keyboard hints: plain text, never a keycap */
.sec .kbd { background: none !important; box-shadow: none !important; border: 0 !important; min-width: 0 !important; height: auto !important; padding: 0 !important; font: 450 12.5px var(--font-ui) !important; color: var(--hd-fg-subtle) !important; }
.sec .suggest .sg-f { gap: 16px; }
.sec .suggest .sg-f > span { display: inline-flex; gap: 4px; align-items: center; }
.sec .suggest .sg .sub .kbd { margin-left: 8px; }
/* filter chips: one signal. off = white + hairline + muted; on = accent-subtle, no border */
.sec .chip { height: 36px; border-radius: 10px; background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; color: var(--hd-fg-muted); box-shadow: none; }
.sec .chip .ic { color: var(--hd-fg-subtle); }
.sec .chip.on { background: var(--hd-accent-subtle) !important; border-color: transparent !important; color: var(--hd-info-strong) !important; }
.sec .chip.on .ic { color: currentColor; }
[data-theme="dark"] .sec .chip.on { background: color-mix(in oklab, var(--hd-accent) 30%, var(--hd-surface)) !important; color: #dbe6ff !important; }
/* inputs: no grey addon slab, one signal for state */
.sec .input .addon { background: none; border-right: 0; margin-left: 0; padding: 0; color: var(--hd-fg-muted); }
.sec .input.ok { border-color: var(--hd-border-input); }
.sec .help.err, .sec .help.ok { display: flex; align-items: center; gap: 0; }
.sec .help.err > svg, .sec .help.ok > svg, .sec .help.err > .ic, .sec .help.ok > .ic { display: none; }
.sec .help.ok { color: var(--hd-success-strong); font-weight: 500; }
.sec .help.err { color: var(--hd-danger-strong); }
.sec .input.dis { background: transparent; }
/* selected radio card: one signal (tint), the radio is the control itself */
.sec .row.sel { background: var(--hd-accent-subtle); border-color: transparent; box-shadow: none; }
[data-theme="dark"] .sec .row.sel { background: color-mix(in oklab, var(--hd-accent) 22%, var(--hd-surface)); }
/* suggestion list: menu-row rhythm */
.sec .suggest .sg { height: 36px; font-size: 14px; }
.sec .suggest .sg.hl { background: color-mix(in oklab, var(--hd-fg) 6%, transparent); }
.sec .suggest .sg .ic { width: 16px; height: 16px; }
/* otp cells: 44 tall controls */
.sec .otp2 span { width: 44px; height: 44px; }
/* primitives */
.sec .tstack > .lbl:first-child { margin-top: 0; }
.sec .iconcell { background: transparent; border: 0; padding: 12px 4px 8px; }
.sec .iconcell span { font-size: 11.5px; }
/* data display */
.sec .x-tl .tm { display: none; }
.sec .bar.seg { -webkit-mask: none; mask: none; height: 3px; border-radius: 999px; background: var(--hd-track); }
.sec .bar.seg i { border-radius: 999px; }
/* grids: cards keep their own height, no stretched dead space */
.sec .grid.g3:has(> .box) { align-items: start; }
/* menu in feedback: approved menu anatomy */
.sec .menu.n-ctx { margin: 0; }
"""
XA += r"""
/* ===== round 2 ===== */
/* progress: one hairline 3px bar, "N of M" says the number once */
.sec .segs { gap: 0; height: 3px; border-radius: 999px; overflow: hidden; background: var(--hd-track); }
.sec .segs i { height: 3px; border-radius: 0 !important; background: transparent; }
.sec .segs i.on { background: var(--hd-accent); }
[data-theme="dark"] .sec .segs i.on { background: var(--hd-chart) !important; }
/* timeline markers: smaller, calmer */
.sec .x-tl .k { width: 20px; }
.sec .x-tl .s .k i { width: 20px; height: 20px; border-width: 1.5px; }
.sec .x-tl .s .k i svg { width: 12px; height: 12px; }
.sec .x-tl .s.now .k i::after { width: 6px; height: 6px; }
.sec .x-tl .hd { min-height: 20px; } .sec .x-tl b { line-height: 20px; }
.sec .x-tl .tx { padding-bottom: 18px; }
/* navigation demos: one surface, one hairline, one radius */
.sec .box > .topbar, .sec .box > .tabs { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge); border-radius: 12px !important; box-shadow: none; }
.sec .box > .tabs { padding: 0 16px !important; }
.sec .box > .tabs > span { padding: 11px 0; }
.sec .box > div[style*="overflow:hidden"] { border: 1px solid var(--hd-edge); border-radius: 12px !important; background: var(--hd-surface); }
.sec .box > div[style*="overflow:hidden"] .tabbar { border-top: 0; background: transparent; }
.sec .box > .panel { border: 1px solid var(--hd-edge); }
/* primitives */
.sec .tstack > div:has(> .lbl) { margin-top: 12px !important; }
.sec .tstack .typewt { margin-top: 0; }
.sec .tstack .t-cap { margin-bottom: 0; }
.sec .box span[style*="background:var(--hd-accent);border-radius:4px"] { background: color-mix(in oklab, var(--hd-accent) 22%, var(--hd-surface)) !important; }
.sec .input.textarea { height: 120px; }
.sec .kbd + .kbd { margin-left: 2px; }
.sec .menu.n-ctx { box-shadow: var(--hd-shadow-e3); }
"""
XA += r"""
/* ===== round 3 ===== */
.sec .k-goal .vz, .sec .stat.k-goal:not(.compact) .vz { height: auto; padding-top: 14px; margin-top: 0; }
.sec .k-goal .sv { margin-top: 4px; }
"""
XA += r"""
.sec .box span[style*="background:var(--hd-accent);border-radius:4px"] { background: color-mix(in oklab, var(--hd-accent) 38%, var(--hd-surface)) !important; }
"""
XA += r"""
/* ===== round 4: navigation as real bars, calm sheet demo ===== */
.sec .xa-nav { align-items: start; }
.sec .xa-phone { width: 390px; max-width: 100%; margin: 0 auto; background: var(--hd-surface); border: 1px solid var(--hd-edge); display: flex; flex-direction: column; min-height: 420px; overflow: hidden; border-radius: 0; }
.sec .xa-bar { height: 52px; display: flex; align-items: center; gap: 16px; padding: 0 16px; border-bottom: 1px solid var(--hd-edge); background: var(--hd-surface); color: var(--hd-fg); }
.sec .xa-bar .ttl { flex: 1; font-size: 17px; font-weight: 600; letter-spacing: -.012em; }
.sec .xa-bar .ic { color: var(--hd-fg); }
.sec .xa-bell { position: relative; display: inline-flex; } .sec .xa-bell .ic { color: var(--hd-fg-muted); }
.sec .xa-bell i { position: absolute; top: -1px; right: 0; width: 6px; height: 6px; border-radius: 50%; background: var(--hd-accent); }
.sec .xa-phone .xa-tabs { background: var(--hd-surface) !important; border: 0; border-bottom: 1px solid var(--hd-edge); border-radius: 0 !important; padding: 0 16px !important; box-shadow: none; gap: 22px; }
.sec .xa-phone .xa-fill { flex: 1; }
.sec .xa-phone .tabbar { height: 60px; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); border-radius: 0; }
.sec .xa-phone .tabbar div { font-size: 11px; font-weight: 560; }
.sec .xa-phone .tabbar .ic { width: 24px; height: 24px; }
.sec .xa-desk { background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.sec .xa-crumb { height: 52px; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; font-size: 13.5px; color: var(--hd-fg-muted); }
.sec .xa-crumb .crumb { display: inline-flex; align-items: center; gap: 6px; } .sec .xa-crumb b { color: var(--hd-fg); font-weight: 560; }
.sec .xa-ph { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 8px 24px 24px; }
.sec .xa-h { font: 650 22px/28px var(--font-display, inherit); letter-spacing: -.02em; }
.sec .xa-ph p { margin: 2px 0 0; font-size: 14px; color: var(--hd-fg-muted); }
/* sheet demo: faint page under a light scrim */
.sec .sheetdemo { background: var(--hd-bg-subtle); box-shadow: none; border: 1px solid var(--hd-edge); }
.sec .sd-ghost { padding: 28px 16px 0; display: flex; flex-direction: column; gap: 10px; }
.sec .sd-ghost i { display: block; height: 52px; border-radius: 12px; background: color-mix(in oklab, var(--hd-fg) 6%, transparent); }
.sec .sheetdemo .scrim { background: rgba(10,12,18,.32); }
.sec .sheet.sd-sheet .row.sel { background: var(--hd-accent-subtle); border-color: transparent; box-shadow: none; }
.sec .sheet.sd-sheet .btn.p { height: 44px; }
"""
XA += r"""
.sec .xa-h { font-family: var(--font-display, 'Bricolage Grotesque', var(--font-ui)); font-weight: 650; font-size: 22px; line-height: 28px; letter-spacing: -.02em; }
.sec .xa-phone { min-height: 0; } .sec .xa-phone .xa-fill { display: none; }
.sec .xa-phone .tabbar { border-top: 0; } .sec .xa-phone .xa-tabs { border-bottom: 1px solid var(--hd-edge); margin-bottom: 0; }
.sec .xa-phone .xa-tabs + .tabbar { margin-top: 24px; border-top: 1px solid var(--hd-edge); }
.sec .sd-ghost i { background: color-mix(in oklab, var(--hd-fg) 7%, transparent); }
"""
XA += r"""
/* ===== round 5: data display box 2 ===== */
.sec .xa-d2 .badge { height: 24px; padding: 0 8px; border-radius: 6px; font-size: 12.5px; font-weight: 560; gap: 4px; }
.sec .xa-d2 .badge.success { color: var(--hd-success-strong) !important; } .sec .xa-d2 .badge.warning { color: var(--hd-warning-strong) !important; }
.sec .xa-d2 .badge.danger { color: var(--hd-danger-strong) !important; } .sec .xa-d2 .badge.info { color: var(--hd-info-strong) !important; }
.sec .xa-d2 .badge.neutral { background: var(--hd-control) !important; color: var(--hd-fg-muted) !important; box-shadow: none; }
.sec .xa-d2 .av { font-weight: 600; letter-spacing: 0; }
.sec .xa-d2 .av-0 { background: var(--hd-accent-subtle); color: var(--hd-info-strong); }
.sec .xa-d2 .av-1 { background: var(--hd-danger-subtle); color: var(--hd-danger-strong); }
.sec .xa-d2 .av-2 { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); }
.sec .xa-d2 .av-3 { background: var(--hd-success-subtle); color: var(--hd-success-strong); }
.sec .xa-avrow { gap: 12px; }
.sec .xa-d2 img.xa-ph { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; }
.sec .xa-stack { margin-left: 8px; align-items: center; }
.sec .xa-stack .av, .sec .xa-stack .xa-more { width: 28px; height: 28px; font-size: 11px; margin-left: -8px; -webkit-mask: none; mask: none; box-shadow: 0 0 0 2px var(--hd-surface) !important; }
.sec .xa-stack .av:first-child { margin-left: 0; }
.sec .xa-more { border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; background: var(--hd-control); color: var(--hd-fg-muted); font-weight: 560; }
/* stat anatomy */
.sec .xa-stats { display: flex; flex-direction: column; gap: 12px; }
.sec .xa-d2 .stat { padding: 16px; gap: 0; }
.sec .xa-d2 .stat .sh { align-items: baseline; }
.sec .xa-d2 .stat .sl { font-size: 13.5px; font-weight: 450; color: var(--hd-fg-muted); }
.sec .xa-d2 .stat .dtext { font-size: 12.5px; font-weight: 560; color: var(--hd-success-strong); }
.sec .xa-d2 .stat .sv { margin-top: 6px; align-items: center; gap: 8px; }
.sec .xa-d2 .stat .sv b { font: 650 28px/32px var(--font-ui); letter-spacing: -.03em; font-variant-numeric: tabular-nums; }
.sec .xa-d2 .stat .vz { height: 40px; margin-top: 12px; padding-top: 0; display: flex; flex-direction: column; justify-content: flex-end; position: relative; }
.sec .xa-d2 .stat .spk { margin: 0 !important; height: 40px; } .sec .xa-d2 .stat .spk svg { height: 40px; }
.sec .xa-d2 .stat .spk path[stroke] { stroke-width: 1.5; }
.sec .xa-d2 .stat .spk-dot { width: 4px !important; height: 4px !important; box-shadow: none !important; }
.sec .xa-st { display: inline-flex; gap: 2px; } .sec .xa-st svg { width: 14px; height: 14px; }
.sec .xa-dist { display: flex; flex-direction: column; justify-content: space-between; height: 40px; }
.sec .xa-dist > div { display: flex; align-items: center; gap: 8px; height: 6px; font-size: 10.5px; line-height: 6px; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.sec .xa-dist span { width: 8px; } .sec .xa-dist i { flex: 1; height: 3px; border-radius: 3px; background: var(--hd-track); overflow: hidden; display: block; } .sec .xa-dist b { display: block; height: 100%; background: var(--hd-accent); border-radius: 3px; }
"""
XA += r"""
.sec .xa-d2 img.xa-photo { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; display: block; }
.sec .xa-dist > div { height: 8px; font-size: 10px; line-height: 8px; }
.sec .xa-dist span { width: 8px; text-align: left; }
"""
XA += r"""
.sec .xa-dist span { display: none; }
"""
