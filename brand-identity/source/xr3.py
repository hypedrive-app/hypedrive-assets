# design-system-by-logic layer 3
XR3 = r"""
.sec.dm .dm-grp { margin-top: 36px; } .sec.dm .dm-grp:first-of-type { margin-top: 24px; }
.sec.dm .dm-gh { display: flex; align-items: baseline; gap: 14px; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid var(--hd-edge); }
.sec.dm .dm-gh b { font-family: var(--font-brand); font-size: 20px; font-weight: 650; letter-spacing: -0.018em; }
.sec.dm .dm-gh span { font-size: 13px; color: var(--hd-fg-muted); }
.sec.dm .dm-row { display: grid; gap: 22px 18px; align-items: stretch; } .sec.dm .dm-row.n { max-width: 980px; } .sec.dm .dm-cell > [class^="dm-"]:not(.dm-lbl) { flex: 1; }
.sec.dm .dm-row.c2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .sec.dm .dm-row.c3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .sec.dm .dm-row.c6 { grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 14px; } .sec.dm .dm-row.c4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.sec.dm .dm-cell { min-width: 0; display: flex; flex-direction: column; gap: 8px; }
.sec.dm .dm-lbl { font-size: 12px; font-weight: 600; color: var(--hd-fg-subtle); }
.sec.dm .dm-cc, .sec.dm .dm-po, .sec.dm .dm-hold, .sec.dm .dm-rc, .sec.dm .dm-sheet, .sec.dm .dm-task, .sec.dm .dm-sb, .sec.dm .dm-ns, .sec.dm .dm-jr, .sec.dm .dm-ship, .sec.dm .dm-mb, .sec.dm .dm-cta {
  background: var(--hd-surface); border-radius: 16px; box-shadow: inset 0 0 0 1px var(--hd-edge); box-sizing: border-box; }
.sec.dm small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.sec.dm em { font-style: normal; }
/* pills: one quiet signal */
.sec.dm .dm-pill { display: inline-flex; align-items: center; gap: 5px; height: 24px; padding: 0 9px; border-radius: 8px; font-size: 12.5px; font-weight: 600; white-space: nowrap; background: color-mix(in oklab, var(--hd-fg) 7%, var(--hd-surface)); color: var(--hd-fg-muted); width: fit-content; }
.sec.dm .dm-pill.ok { background: var(--hd-success-subtle); color: var(--hd-success); }
.sec.dm .dm-pill.warn { background: var(--hd-warning-subtle); color: var(--hd-warning); }
.sec.dm .dm-pill.info { background: var(--hd-accent-subtle); color: var(--hd-info-strong, var(--hd-info)); }
[data-theme="dark"] .sec.dm .dm-pill.info { color: #dbe6ff; }
.sec.dm .dm-pill.mute { color: var(--hd-fg-muted); }
/* 1 campaign card */
.sec.dm .dm-cc { overflow: hidden; display: flex; flex-direction: column; }
.sec.dm .dm-ph { aspect-ratio: 4/3; overflow: hidden; background: var(--hd-bg-subtle); } .sec.dm .dm-ph img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.sec.dm .dm-cb { padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 6px; flex: 1; }
.sec.dm .dm-sr { display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: var(--hd-fg-muted); }
.sec.dm .dm-store { display: inline-flex; align-items: center; gap: 5px; font-weight: 600; color: var(--hd-fg); } .sec.dm .dm-store img { border-radius: 4px; }
.sec.dm .dm-ti { font-family: var(--font-brand); font-size: 16px; line-height: 21px; font-weight: 650; letter-spacing: -0.018em; }
.sec.dm .dm-pay { display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; margin-top: 2px; }
.sec.dm .dm-bk { font-size: 16px; font-weight: 700; } .sec.dm .dm-w { font-size: 14px; color: var(--hd-fg-muted); } .sec.dm .dm-bn { font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); }
.sec.dm .dm-ft { display: flex; align-items: center; justify-content: space-between; min-height: 24px; margin-top: auto; padding-top: 4px; }
.sec.dm .dm-sp { font-size: 13px; color: var(--hd-fg-muted); } .sec.dm .dm-sp b { font-weight: 600; color: var(--hd-fg); }
.sec.dm .dm-cc.muted .dm-ph img { filter: grayscale(1); opacity: .55; } .sec.dm .dm-cc.muted .dm-ti, .sec.dm .dm-cc.muted .dm-bk { color: var(--hd-fg-muted); }
/* 2 payout */
.sec.dm .dm-po { padding: 4px 18px 14px; }
.sec.dm .dm-po .hd { padding: 14px 0 14px; border-bottom: 1px solid var(--hd-edge); display: flex; flex-direction: column; gap: 2px; }
.sec.dm .dm-po .hd span { font-size: 14px; font-weight: 550; color: var(--hd-fg-muted); } .sec.dm .dm-po .hd b { font-family: var(--font-brand); font-size: 40px; line-height: 46px; font-weight: 700; letter-spacing: -0.025em; }
.sec.dm .dm-po .hd small { font-size: 13px; }
.sec.dm .dm-po .r { display: flex; justify-content: space-between; align-items: center; height: 42px; font-size: 15px; } .sec.dm .dm-po .r span { color: var(--hd-fg-muted); } .sec.dm .dm-po .r b { font-weight: 600; }
.sec.dm .dm-po .r em { font-weight: 400; font-size: 13px; margin-left: 6px; color: var(--hd-fg-subtle); }
.sec.dm .dm-po .ft { display: flex; justify-content: space-between; padding-top: 12px; border-top: 1px solid var(--hd-edge); font-size: 13px; color: var(--hd-fg-muted); } .sec.dm .dm-po .ft b { color: var(--hd-fg); font-weight: 600; }
/* 3 cta */
.sec.dm .dm-cta { padding: 14px; display: flex; flex-direction: column; gap: 10px; } .sec.dm .dm-cta small { text-align: center; }
.sec.dm .dm-cta .btn:disabled { opacity: 1; background: var(--hd-control); color: var(--hd-fg-subtle); box-shadow: none; cursor: not-allowed; }
/* 4 hold */
.sec.dm .dm-hold { padding: 14px 16px; display: flex; flex-direction: column; gap: 12px; }
.sec.dm .dm-hold .t { display: flex; align-items: center; gap: 12px; } .sec.dm .dm-hold .t > .ic { color: var(--hd-fg-muted); flex: none; }
.sec.dm .dm-hold .t > div { flex: 1; min-width: 0; display: flex; flex-direction: column; } .sec.dm .dm-hold .t b { font-size: 15px; font-weight: 600; }
.sec.dm .dm-hold .t small em { font-weight: 700; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.sec.dm .dm-hold .btn { height: 36px; padding: 0 14px; font-size: 14px; flex: none; }
.sec.dm .dm-hold.low .tape i { background: var(--hd-warning); } .sec.dm .dm-hold.low .t small em { color: var(--hd-warning); }
.sec.dm .dm-hold.ended .t > .ic { color: var(--hd-fg-subtle); } .sec.dm .dm-hold.ended .t b { color: var(--hd-fg-muted); }
/* 5 receipt */
.sec.dm .dm-rc { padding: 14px; display: flex; flex-direction: column; gap: 12px; min-height: 196px; justify-content: space-between; }
.sec.dm .dm-rc .dz { border: 1.5px dashed var(--hd-border-strong, var(--hd-edge)); border-radius: 12px; padding: 18px 12px; display: flex; flex-direction: column; align-items: center; gap: 4px; text-align: center; color: var(--hd-fg-muted); }
.sec.dm .dm-rc .dz b { color: var(--hd-fg); font-size: 15px; font-weight: 600; margin-top: 4px; }
.sec.dm .dm-rc .file { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 12px; background: color-mix(in oklab, var(--hd-fg) 6%, var(--hd-surface)); } .sec.dm .dm-rc .file i { width: 34px; height: 42px; border-radius: 6px; background: var(--hd-surface); box-shadow: inset 0 0 0 1px var(--hd-edge); }
.sec.dm .dm-rc .file b { display: block; font-size: 14px; font-weight: 600; }
.sec.dm .dm-rc .wait, .sec.dm .dm-rc .res { display: flex; gap: 12px; align-items: flex-start; } .sec.dm .dm-rc .wait b, .sec.dm .dm-rc .res b { display: block; font-size: 15px; font-weight: 600; margin-bottom: 2px; }
.sec.dm .dm-rc .spin { width: 22px; height: 22px; border-radius: 50%; border: 2.5px solid color-mix(in oklab, var(--hd-fg) 16%, var(--hd-surface)); border-top-color: var(--hd-accent); flex: none; animation: dmspin 900ms linear infinite; margin-top: 1px; }
@keyframes dmspin { to { transform: rotate(360deg); } }
.sec.dm .dm-rc .res.ok > .ic { color: var(--hd-success); } .sec.dm .dm-rc .res.bad > .ic { color: var(--hd-danger); } .sec.dm .dm-rc .res > .ic { flex: none; }
.sec.dm .dm-rc.mid { justify-content: flex-start; gap: 14px; }
/* 6 apply sheet */
.sec.dm .dm-sheet { padding: 8px 18px 18px; display: flex; flex-direction: column; gap: 16px; background: var(--hd-surface-raised, var(--hd-surface)); border-radius: 22px; }
.sec.dm .dm-sheet .grab { width: 36px; height: 5px; border-radius: 3px; background: var(--hd-track-strong, var(--hd-track)); margin: 0 auto; }
.sec.dm .dm-sheet .hd { display: flex; justify-content: space-between; align-items: center; } .sec.dm .dm-sheet .hd b { font-family: var(--font-brand); font-size: 22px; font-weight: 700; letter-spacing: -0.02em; }
.sec.dm .dm-x { width: 32px; height: 32px; border-radius: 50%; background: var(--hd-control); display: grid; place-items: center; color: var(--hd-fg-muted); }
.sec.dm .dm-mini { display: flex; align-items: center; gap: 12px; } .sec.dm .dm-mini img { width: 44px; height: 44px; border-radius: 10px; object-fit: cover; } .sec.dm .dm-mini b { display: block; font-size: 15px; font-weight: 600; }
.sec.dm .f { display: flex; flex-direction: column; gap: 7px; } .sec.dm .f .lr { display: flex; justify-content: space-between; align-items: baseline; } .sec.dm .f label { font-size: 14px; font-weight: 600; } .sec.dm .f .lr span { font-size: 13px; color: var(--hd-fg-muted); }
.sec.dm .f .input { min-height: 46px; } .sec.dm .f .input.textarea { min-height: 84px; height: auto; align-items: flex-start; padding-top: 11px; }
.sec.dm .dm-a { color: var(--hd-link); font-weight: 600; cursor: pointer; }
.sec.dm .dm-ig { display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 12px; box-shadow: inset 0 0 0 1px var(--hd-edge); } .sec.dm .dm-ig > div { flex: 1; } .sec.dm .dm-ig b { display: block; font-size: 15px; font-weight: 600; }
.sec.dm .dm-sheet small.c { text-align: center; margin-top: -6px; }
/* 7 tasks */
.sec.dm .dm-task { padding: 14px; display: flex; flex-direction: column; gap: 12px; min-height: 120px; }
.sec.dm .dm-th { display: flex; align-items: center; gap: 10px; } .sec.dm .dm-th .tx { flex: 1; min-width: 0; } .sec.dm .dm-th b { font-size: 15px; font-weight: 600; }
.sec.dm .dm-chips { display: flex; flex-wrap: wrap; gap: 6px; } .sec.dm .dm-chips span { font-size: 12.5px; font-weight: 550; color: var(--hd-fg-muted); height: 24px; display: inline-flex; align-items: center; padding: 0 9px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--hd-edge); }
.sec.dm .dm-task .f .input { min-height: 42px; gap: 8px; } .sec.dm .dm-task .f .input > .ic { color: var(--hd-fg-subtle); } .sec.dm .dm-task .f label { font-size: 13px; color: var(--hd-fg-muted); font-weight: 600; }
.sec.dm .dm-shots { display: grid; grid-template-columns: repeat(6, 1fr); gap: 6px; } .sec.dm .dm-shots .s { aspect-ratio: 1; border-radius: 10px; overflow: hidden; position: relative; background: var(--hd-bg-subtle); } .sec.dm .dm-shots img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.sec.dm .dm-shots .s i { position: absolute; top: 3px; right: 3px; width: 16px; height: 16px; border-radius: 50%; background: rgba(20,22,30,.72); color: #fff; display: grid; place-items: center; }
.sec.dm .dm-shots .s.add { display: grid; place-items: center; color: var(--hd-fg-muted); background: var(--hd-control); }
.sec.dm .dm-cnt { display: block; margin-top: 6px; }
.sec.dm .dm-done { display: flex; align-items: center; gap: 8px; font-size: 14px; color: var(--hd-fg-muted); padding: 10px 12px; border-radius: 12px; background: color-mix(in oklab, var(--hd-fg) 6%, var(--hd-surface)); } .sec.dm .dm-done span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.sec.dm .dm-note { padding: 11px 12px; border-radius: 12px; background: color-mix(in oklab, var(--hd-fg) 6%, var(--hd-surface)); } .sec.dm .dm-note b { font-size: 13px; font-weight: 650; color: var(--hd-fg); } .sec.dm .dm-note p { margin: 3px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg); }
.sec.dm .dm-task.lock .dm-th b, .sec.dm .dm-task.lock .dm-chips { opacity: .6; } .sec.dm .dm-lk { display: flex; align-items: center; gap: 8px; font-size: 14px; color: var(--hd-fg-muted); }
.sec.dm .dm-task.slim { min-height: 0; max-width: 360px; flex: none !important; }
/* 8 submit bar */
.sec.dm .dm-sb { padding: 14px 14px 12px; display: flex; flex-direction: column; gap: 10px; }
.sec.dm .dm-sb .r { display: flex; align-items: center; gap: 12px; } .sec.dm .dm-sb .r > div { flex: 1; min-width: 0; } .sec.dm .dm-sb .r b { display: block; font-family: var(--font-brand); font-size: 18px; font-weight: 650; letter-spacing: -0.015em; }
.sec.dm .dm-sb .btn { flex: none; } .sec.dm .dm-sb .btn:disabled { opacity: 1; background: var(--hd-control); color: var(--hd-fg-subtle); box-shadow: none; }
.sec.dm .dm-sb .at { margin: 0; display: flex; gap: 7px; align-items: flex-start; font-size: 12.5px; line-height: 17px; color: var(--hd-fg-muted); } .sec.dm .dm-sb .at .ic { flex: none; margin-top: 1px; }
/* 9 next step */
.sec.dm .dm-ns { padding: 14px; display: flex; gap: 14px; align-items: center; } .sec.dm .dm-ns img { width: 64px; height: 64px; border-radius: 12px; object-fit: cover; flex: none; }
.sec.dm .dm-ns .tx { display: flex; flex-direction: column; gap: 5px; min-width: 0; } .sec.dm .dm-ns b { font-family: var(--font-brand); font-size: 20px; line-height: 25px; font-weight: 650; letter-spacing: -0.02em; }
.sec.dm .dm-ns small { display: flex; align-items: center; gap: 6px; } .sec.dm .dm-ns small .ic { color: var(--hd-fg-subtle); }
/* 10 journey */
.sec.dm .dm-jr { padding: 20px 20px 18px; display: grid; grid-template-columns: repeat(var(--n), 1fr); }
.sec.dm .dm-jr .s { position: relative; display: flex; flex-direction: column; align-items: center; gap: 8px; font-size: 13px; font-weight: 550; color: var(--hd-fg-subtle); }
.sec.dm .dm-jr .s::before { content: ""; position: absolute; top: 13px; right: 50%; width: 100%; height: 2px; background: var(--hd-track); } .sec.dm .dm-jr .s:first-child::before { display: none; }
.sec.dm .dm-jr .s.done::before, .sec.dm .dm-jr .s.now::before { background: var(--hd-fg); }
.sec.dm .dm-jr .s i { position: relative; z-index: 1; width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; font-style: normal; font-size: 12.5px; font-weight: 700; background: var(--hd-surface); box-shadow: inset 0 0 0 1.5px var(--hd-track-strong, var(--hd-edge)); }
.sec.dm .dm-jr .s.done i { background: var(--hd-fg); color: var(--hd-bg, #fff); box-shadow: none; } .sec.dm .dm-jr .s.done { color: var(--hd-fg-muted); }
.sec.dm .dm-jr .s.now i { box-shadow: inset 0 0 0 2px var(--hd-accent); color: var(--hd-accent); } .sec.dm .dm-jr .s.now { color: var(--hd-fg); font-weight: 650; }
[data-theme="dark"] .sec.dm .dm-jr .s.now i { color: #9db6ff; }
/* 11 shipment */
.sec.dm .dm-ship { padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 4px; }
.sec.dm .dm-ship .h { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; } .sec.dm .dm-ship .h b { font-family: var(--font-brand); font-size: 18px; font-weight: 650; letter-spacing: -0.015em; }
.sec.dm .dm-trk { display: grid; grid-template-columns: repeat(3, 1fr); margin: 4px 0 10px; }
.sec.dm .dm-trk .s { position: relative; display: flex; flex-direction: column; align-items: center; gap: 7px; font-size: 12px; font-weight: 550; text-align: center; color: var(--hd-fg-subtle); }
.sec.dm .dm-trk .s::before { content: ""; position: absolute; top: 5px; right: 50%; width: 100%; height: 2px; background: var(--hd-track); } .sec.dm .dm-trk .s:first-child::before { display: none; }
.sec.dm .dm-trk .s.done::before, .sec.dm .dm-trk .s.now::before { background: var(--hd-fg); }
.sec.dm .dm-trk .s i { position: relative; z-index: 1; width: 12px; height: 12px; border-radius: 50%; background: var(--hd-surface); box-shadow: inset 0 0 0 2px var(--hd-track-strong, var(--hd-edge)); }
.sec.dm .dm-trk .s.done i { background: var(--hd-fg); box-shadow: none; } .sec.dm .dm-trk .s.now i { background: var(--hd-accent); box-shadow: none; } .sec.dm .dm-trk .s.done, .sec.dm .dm-trk .s.now { color: var(--hd-fg); }
.sec.dm .dm-kv { display: flex; justify-content: space-between; gap: 16px; padding: 9px 0; border-top: 1px solid var(--hd-edge); font-size: 14px; } .sec.dm .dm-kv span { color: var(--hd-fg-muted); flex: none; } .sec.dm .dm-kv b { font-weight: 600; text-align: right; }
.sec.dm .dm-kv.w b { font-weight: 500; font-size: 13.5px; line-height: 19px; } .sec.dm .dm-ship .btn { margin-top: 10px; }
/* 12 money */
.sec.dm .dm-mb { padding: 14px 16px 14px; }
.sec.dm .dm-mb .h { display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-bottom: 6px; } .sec.dm .dm-mb .h b { font-family: var(--font-brand); font-size: 18px; font-weight: 650; letter-spacing: -0.015em; }
.sec.dm .dm-mb .w { font-size: 12.5px; font-weight: 600; color: var(--hd-fg-muted); text-align: right; } .sec.dm .dm-mb .w.ok { color: var(--hd-success); }
.sec.dm .dm-mb .dm-kv em { font-size: 13px; color: var(--hd-fg-subtle); margin-left: 6px; }
.sec.dm .dm-mb .tot { display: flex; justify-content: space-between; align-items: baseline; padding: 12px 0 4px; border-top: 1px solid var(--hd-edge-strong, var(--hd-edge)); } .sec.dm .dm-mb .tot span { font-size: 15px; font-weight: 600; } .sec.dm .dm-mb .tot b { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; }
.sec.dm .dm-mb > small { display: block; margin-top: 4px; }
.sec.dm .input > span, .sec.dm .input > b { background: none !important; box-shadow: none !important; padding: 0 !important; height: auto !important; border-radius: 0 !important; display: inline !important; }
.sec.dm .input { gap: 8px; align-items: center; }
.sec.dm .nil { color: var(--hd-fg-subtle); font-weight: 500; }

/* payout card v6 (calm, matches the Campaign screen) */
.dm-po.dm-po6 { padding: 14px 16px 0 !important; }
.dm-po6 .k { display: block; font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); }
.dm-po6 .big { display: block; margin-top: 2px; font: 700 34px/38px var(--font-brand); letter-spacing: -.025em; color: var(--hd-fg); }
.dm-po6 .mix { margin: 4px 0 0; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); } .dm-po6 .mix b { color: var(--hd-fg); font-weight: 600; }
.dm-po6 .ft { display: flex; justify-content: space-between; margin: 12px -16px 0; padding: 11px 16px; border-top: 1px solid var(--hd-edge); font-size: 13px; color: var(--hd-fg-muted); } .dm-po6 .ft b { color: var(--hd-fg); font-weight: 600; }
"""
