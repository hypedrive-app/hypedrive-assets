# Section polish layer (xc): nw1-nw5. Appended after XLEAD.
XC = r"""
/* ---- nw1 fields ---- */
.n-opt .check.on .ic, .n-opt .check.on svg { color: #fff; }
.n-list { padding: 4px; gap: 0; }
.n-opt { min-height: 40px; height: 40px; padding: 0 10px; border-radius: 8px; gap: 12px; }
.n-opt.hv { background: color-mix(in oklab, var(--hd-fg) 5%, transparent); }
.n-opt .check { margin: 0 2px 0 0; }
.n-opt .check.on svg { stroke: #fff; color: #fff; stroke-width: 2; }
.input.n-multi { min-height: 44px; padding: 7px 10px 7px 8px; gap: 6px; align-items: center; }
.input.n-multi .n-q { min-width: 40px; height: 28px; }
.n-tok { height: 28px; padding: 0 3px 0 10px; gap: 2px; border-radius: 8px; border: 0; background: var(--hd-accent-subtle); color: var(--hd-info-strong); font-size: 13px; font-weight: 500; }
.n-tok .n-x { width: 22px; height: 22px; border-radius: 6px; color: var(--hd-info-strong); opacity: .7; }
.n-tok .n-x:hover { opacity: 1; background: color-mix(in oklab, var(--hd-accent) 14%, transparent); color: var(--hd-info-strong); }
[data-theme="dark"] .n-tok { color: #dbe6ff; } [data-theme="dark"] .n-tok .n-x { color: #dbe6ff; }
/* date picker: compact 300, 36 circles, flat selected, today = accent text + dot */
.suggest.n-cal { width: 300px; max-width: 100%; padding: 12px 12px 10px; }
.n-calh { margin: 0 0 8px; padding-left: 4px; } .n-calh b { font-size: 15px; font-weight: 600; }
.n-calnav { display: inline-flex; gap: 2px; } .n-calnav .btn { width: 32px !important; height: 32px !important; min-height: 0 !important; border-radius: 8px !important; }
.n-cg { gap: 2px 0; }
.n-cg span { width: 36px; height: 36px; justify-self: center; border-radius: 50%; font-size: 13.5px; font-weight: 450; position: relative; }
.n-cg .dw { width: auto; height: 28px; border-radius: 0; }
.n-cg .mu { color: var(--hd-fg-subtle); opacity: .45; }
.n-cg .off { color: var(--hd-fg-subtle); opacity: .6; text-decoration: none; cursor: not-allowed; }
.n-cg .td { border: 0; color: var(--hd-accent); font-weight: 600; }
.n-cg .td::after { content: ''; position: absolute; left: 50%; bottom: 5px; width: 4px; height: 4px; margin-left: -2px; border-radius: 50%; background: var(--hd-accent); }
.n-cg .hv { background: color-mix(in oklab, var(--hd-fg) 7%, transparent); }
.n-cg .sl { background: var(--hd-accent); color: #fff; box-shadow: none; font-weight: 600; }
[data-theme="dark"] .n-cg .td { color: #8fb0ff; } [data-theme="dark"] .n-cg .td::after { background: #8fb0ff; }
.n-opt { font-size: 15px; font-variant-numeric: tabular-nums; }
.input .n-val, .input.n-sel { font-size: 15px; }
.n-opt.n-slot.on { background: var(--hd-accent-subtle); color: var(--hd-info-strong); font-weight: 560; }
.n-opt.n-slot.on .n-tick { color: var(--hd-info-strong); }
[data-theme="dark"] .n-opt.n-slot.on { color: #dbe6ff; } [data-theme="dark"] .n-opt.n-slot.on .n-tick { color: #dbe6ff; }
.n-opt.dis { color: var(--hd-fg-subtle); cursor: not-allowed; }
.n-cg .mu { visibility: hidden; opacity: 1; }
.suggest.n-cal { width: 100%; }
.input.n-time { gap: 10px; font-variant-numeric: tabular-nums; font-size: 15px; }
.input.n-time > .ic { margin-right: 0; }
.n-tv { display: inline-flex; align-items: center; gap: 2px; }
.n-tv .n-seg { padding: 2px 5px; border-radius: 6px; margin: 0; color: var(--hd-fg); font-weight: 500; }
.n-tv .n-seg:last-child { margin-left: 0; }
.n-tv .n-colon { margin: 0; } .n-tv .n-ap { margin-left: 6px; color: var(--hd-fg-muted); font-weight: 500; }
.n-tv .n-seg.on { background: var(--hd-accent-subtle); color: var(--hd-info-strong); }
[data-theme="dark"] .n-tv .n-seg.on { color: #dbe6ff; }
/* ---- toggle groups ---- */
.sec .seg { display: inline-flex; align-items: center; height: 36px; padding: 3px; gap: 0; border-radius: 10px; background: var(--hd-control); border: 0; box-shadow: none; }
.sec .seg > span { height: 30px; min-width: 0; padding: 0 12px; border-radius: 8px; display: inline-flex; align-items: center; justify-content: center; gap: 6px; font-size: 14px; font-weight: 560; color: var(--hd-fg-muted); background: none; border: 0; box-shadow: none; }
.sec .seg > span.on { background: var(--hd-surface); color: var(--hd-fg); box-shadow: 0 0 0 1px var(--hd-edge, rgba(16,20,38,.12)), 0 1px 2px rgba(16,20,38,.08); }
[data-theme="dark"] .sec .seg > span.on { background: var(--hd-surface-raised); box-shadow: 0 0 0 1px rgba(255,255,255,.08), 0 1px 2px rgba(0,0,0,.5); }
.sec .seg .ic { width: 18px; height: 18px; }
.sec .n-tgm span { height: 36px !important; padding: 0 12px !important; border-radius: 10px !important; font-size: 14px; font-weight: 560; gap: 6px; background: var(--hd-surface); color: var(--hd-fg) !important; }
.sec .n-tgm span:not(.on) { color: var(--hd-fg-muted) !important; }
.sec .n-tgm span.on { background: var(--hd-accent-subtle) !important; border-color: transparent !important; color: var(--hd-fg) !important; }
.sec .n-tgm span.on > .ic:first-child { color: var(--hd-accent); margin-right: -2px; }
.n-fil .chip { height: 36px; border-radius: 10px; font-size: 14px; font-weight: 560; }
.n-fil .chip.on, .n-sortw .chip.on { border: 0 !important; box-shadow: none !important; color: var(--hd-fg) !important; background: var(--hd-accent-subtle) !important; }
[data-theme="dark"] .n-fil .chip.on { color: #fff !important; }
/* ---- range slider ---- */
.n-rng { height: 20px; } .n-rng .tr { top: 8px; height: 4px; border-radius: 4px; } .n-rng .fill { top: 8px; height: 4px; }
.n-rng .th, .n-rng .th.foc { top: 0; width: 20px; height: 20px; margin-left: -10px; border: 0; background: #fff; box-shadow: 0 0 0 1px var(--hd-edge-strong, rgba(16,20,38,.22)), 0 1px 3px rgba(16,20,38,.22); }
[data-theme="dark"] .n-rng .th { box-shadow: 0 0 0 1px rgba(255,255,255,.2), 0 1px 3px rgba(0,0,0,.6); }
.n-rsc { display: flex; justify-content: space-between; font-size: 12.5px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; margin-top: -6px; }
.n-rngw { gap: 12px; } .n-fsec .n-rsc { margin-top: 6px; }
.n-rin { align-items: flex-end; gap: 10px; } .n-rf { flex: 1; display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.n-rl { font-size: 12px; color: var(--hd-fg-muted); } .n-rin .input { height: 40px; min-height: 40px; flex: none; box-sizing: border-box; padding: 0 12px; display: flex; align-items: center; font-size: 15px; width: 100%; }
.input.n-ta.foc { box-shadow: 0 0 0 3px var(--hd-accent-subtle); } .n-rin .input .pre { font-weight: 450; }
.n-rin .n-dash { margin-bottom: 19px; width: 8px; }
/* ---- counted textarea ---- */
.input.n-ta { height: auto; min-height: 0; padding: 12px 14px; font-size: 15px; line-height: 22px; border-radius: 12px; }
.input.n-ta > span { min-height: 66px; display: block; }
.n-warn { font-weight: 600; } .help .cnt.n-warn { color: var(--hd-warning-strong) !important; }
.help.err .cnt { color: var(--hd-danger); }
.field .help { font-size: 12.5px; }
/* ---- dropzone ---- */
.u-dz { border: 1.5px dashed color-mix(in oklab, var(--hd-fg) 24%, transparent); background: var(--hd-surface); border-radius: 14px; min-height: 76px; padding: 0 16px; }
.u-dz b { font-size: 15px; } .u-dz span:not(.u-ic) { font-size: 13.5px; }
.u-dz.drag { border-color: var(--hd-accent); background: color-mix(in oklab, var(--hd-accent) 6%, var(--hd-surface)); }
.u-dz.drag .u-ic { color: var(--hd-accent); } .u-dz.drag b { color: var(--hd-fg); }
/* ---- nw2 input, upload, layout ---- */
.u-row .btn.g.icon, .u-row .btn.g.icon .ic { color: var(--hd-fg-subtle); }
.u-row .btn.g.icon:hover .ic { color: var(--hd-fg); }
.n-togl { display: flex; align-items: center; gap: 12px; min-height: 44px; }
.n-togl > span:not(.switch) { background: none !important; padding: 0 !important; border: 0 !important; box-shadow: none !important; }
/* ---- nw4 filters, load more ---- */
.n-fil .chip:not(.on), .n-sortw .chip:not(.on) { background: var(--hd-surface); border: 1px solid var(--hd-edge, rgba(16,20,38,.16)); box-shadow: none; }
[data-theme="dark"] .n-fil .chip:not(.on) { background: var(--hd-surface-raised); }
/* ---- nw5 dialogs, states ---- */
.dialog.n-dlg p, .n-state p { background: none !important; padding: 0 !important; border-radius: 0 !important; }
.dialog.n-dlg .field { margin-top: 8px; }
.n-dti, .n-ti.dg { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); color: var(--hd-danger) !important;
  box-shadow: 0 1px 1px rgba(16,20,38,.05), 0 3px 8px -2px rgba(16,20,38,.08); }
[data-theme="dark"] .n-dti, [data-theme="dark"] .n-ti.dg { background: var(--hd-surface-raised) !important; box-shadow: 0 1px 2px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.06); }
.n-serr span:not(.x-tile) { display: block; line-height: 18px; }
/* ---- nw3 ---- */
.n-mention u { background: none !important; padding: 0 !important; color: var(--hd-link); text-decoration: none; font-weight: 560; }
/* ---- iOS action sheet ---- */
.n-asd { height: 500px; }
.n-ghost .t-cap, .n-ghost .num { font-family: var(--font-ui); font-variant-numeric: tabular-nums; }
.n-scrim { background: rgba(10,12,18,.40); }
[data-theme="dark"] .n-scrim { background: rgba(0,0,0,.5); }
.n-as { gap: 8px; bottom: 8px; }
.n-asg { border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); border-radius: 14px; }
.n-ash { display: flex; align-items: center; gap: 12px; padding: 12px 16px; text-align: left; }
.n-ast { position: relative; width: 36px; height: 36px; flex: none; }
.n-ast > img:first-child { width: 36px; height: 36px; border-radius: 8px; object-fit: cover; display: block; }
.n-asv { position: absolute; right: -5px; bottom: -5px; width: 18px; height: 18px; border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 2px var(--hd-surface); }
.n-asx { min-width: 0; } .n-asx b { font-size: 15px; font-weight: 600; line-height: 20px; }
.n-asx small { display: flex; align-items: center; gap: 5px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.n-asx small .plat, .n-asx small svg { border-radius: 3px; flex: none; }
.n-asa { height: 52px; justify-content: flex-start; gap: 12px; padding: 0 16px; font-size: 15px; font-weight: 500; color: var(--hd-fg); letter-spacing: 0; position: relative; box-shadow: none; }
.n-asa > .ic { color: var(--hd-fg-muted); flex: none; }
.n-asa::before { content: ''; position: absolute; top: 0; left: 46px; right: 0; height: 1px; background: var(--hd-edge, rgba(16,20,38,.12)); }
.n-ash + .n-asa::before { left: 0; } .n-asg > .n-asa:first-child::before { display: none; }
.n-asa.dg { color: var(--hd-danger); } .n-asa.cn { justify-content: center; font-weight: 600; color: var(--hd-fg); }
/* ---- hover card ---- */
.dialog.n-hc { width: 340px; padding: 16px; gap: 12px; }
.n-hc p { font-size: 14px; line-height: 20px; text-wrap: pretty; color: var(--hd-fg-muted); }
.n-hch b { font-size: 15px; line-height: 20px; } .n-hch span:not(.n-vb) { font-size: 13px; line-height: 18px; }
.n-hcs { border: 0; border-top: 1px solid var(--hairline); margin: 0; padding: 12px 0 0; gap: 0; }
.n-hcs b { font-size: 15px; font-weight: 600; letter-spacing: 0; font-variant-numeric: tabular-nums; line-height: 20px; }
.n-hcs span { font-size: 12.5px; gap: 5px; margin-top: 2px; }
.n-hca { margin-top: 4px !important; display: grid !important; grid-template-columns: 1fr 1fr; gap: 8px; }
.n-hca .btn { width: 100%; height: 40px; min-height: 40px; justify-content: center; }
.n-mention u { text-decoration: none; } .n-mention u:hover { text-decoration: underline dotted; text-underline-offset: 3px; }
/* ---- wizard stepper: 4 equal columns, circle + line on one row, text below ---- */
.sec .n-wzcard { padding: 18px 20px; min-width: 0; overflow: hidden; }
.sec .n-wz { display: flex; align-items: flex-start; gap: 0; }
.sec .n-wz .s { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; align-items: stretch; gap: 10px; white-space: normal; }
.sec .n-sr1 { display: flex; align-items: center; }
.sec .n-wz .s .k { box-sizing: border-box; width: 28px; height: 28px; border: 0; box-shadow: inset 0 0 0 1.5px var(--hd-border-strong); background: transparent; color: var(--hd-fg-muted); font-size: 13px; font-weight: 600; font-variant-numeric: tabular-nums; }
.sec .n-wz .s.done .k { background: var(--hd-accent); box-shadow: none; color: #fff; }
.sec .n-wz .s.now .k { background: var(--hd-accent); box-shadow: 0 0 0 4px var(--hd-accent-subtle); color: #fff; }
.sec .n-wz .ln { flex: 1; min-width: 0; margin: 0 12px; height: 2px; background: var(--hd-border-strong); }
.sec .n-wz .s.now .ln { margin-left: 16px; } .sec .n-wz .ln.done { background: var(--hd-accent); }
.sec .n-st { min-width: 0; padding-right: 12px; } .sec .n-st b { font-size: 14px; font-weight: 600; line-height: 20px; color: var(--hd-fg-muted); }
.sec .n-st small { font-size: 12.5px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.sec .n-wz .s.now .n-st b, .sec .n-wz .s.done .n-st b { color: var(--hd-fg); }
.sec .n-wz .s.now .k::after { display: none; }
.sec .n-fil .chip:not(.on), .sec .n-sortw .chip:not(.on) { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.16)) !important; box-shadow: none !important; color: var(--hd-fg-muted) !important; }
[data-theme="dark"] .sec .n-fil .chip:not(.on) { background: var(--hd-surface-raised) !important; }
.sec .n-fil .chip.on { border: 0 !important; }
[data-theme="dark"] .sec .seg > span.on { background: color-mix(in oklab, var(--hd-fg) 14%, var(--hd-control)); }
[data-theme="dark"] .sec .n-tgm span.on > .ic:first-child { color: #8fb0ff; }
"""
