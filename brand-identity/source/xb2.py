# Layer (xb2). Prefix every class to avoid clashes.
XB2 = """
.b2-mono { font-family: ui-monospace, 'SF Mono', Menlo, monospace; font-size: 12.5px; letter-spacing: 0; }
.b2-card { background: var(--hd-surface-raised); border: 1px solid var(--hd-edge); border-radius: 14px; box-shadow: none; }
.b2-tt { min-width: 0; flex: 1; display: flex; flex-direction: column; gap: 2px; }
.b2-tt b { font-size: 15px; line-height: 20px; font-weight: 600; letter-spacing: -.005em; color: var(--hd-fg); }
.b2-tt small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.b2-tl { width: 40px; height: 40px; border-radius: 10px; display: grid; place-items: center; flex: none; padding: 0; }
.b2-tl img, .b2-tl svg { flex: none; }
.b2-h { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.b2-sub { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.shell .sp { flex: 1; }

/* ---------- 5 review ---------- */
.shell .pg:has(> .b2-rv) { padding: 0; gap: 0; }
.b2-rv { flex: 1; min-height: 0; display: flex; flex-direction: column; }
.b2-bar { height: 56px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 28px; border-bottom: 1px solid var(--hd-edge); background: var(--hd-surface); }
.b2-bt { font-size: 14px; font-weight: 600; color: var(--hd-fg); }
.b2-bn { font-size: 13px; color: var(--hd-fg-muted); font-weight: 500; }
.b2-prog { width: 96px; height: 3px; border-radius: 3px; background: var(--hd-edge); display: block; overflow: hidden; }
.b2-prog i { display: block; height: 100%; background: var(--hd-accent); border-radius: 3px; }
.b2-hd { flex: none; display: flex; align-items: center; gap: 16px; padding: 18px 28px 6px; }
.b2-av { width: 56px; height: 56px; border-radius: 50%; object-fit: cover; flex: none; }
.b2-who { flex: 1; min-width: 0; }
.b2-name { display: flex; align-items: center; gap: 8px; font-family: var(--font-brand); font-size: 26px; line-height: 32px; }
.b2-who p { margin: 2px 0 0; font-size: 14px; color: var(--hd-fg-muted); }
.b2-camp { display: flex; align-items: center; gap: 10px; padding-right: 8px; }
.b2-camp img { width: 40px; height: 40px; border-radius: 10px; object-fit: cover; }
.b2-camp b { display: block; font-size: 14px; font-weight: 600; } .b2-camp small { font-size: 13px; color: var(--hd-fg-muted); }
.b2-body { flex: 1; min-height: 0; display: grid; grid-template-columns: minmax(0, 1fr) 316px; gap: 16px; padding: 12px 28px 16px; }
.b2-tasks, .b2-side { display: flex; flex-direction: column; gap: 10px; min-height: 0; min-width: 0; }
.b2-task { padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; }
.b2-th { display: flex; align-items: center; gap: 12px; }
.b2-seg { display: flex; gap: 6px; flex: none; }
.b2-seg span { height: 36px; padding: 0 14px; border-radius: 10px; display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 560; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.b2-seg span .ic { color: var(--hd-fg-subtle); }
.b2-seg span.on { border-color: transparent; }
.b2-seg span.good.on { color: var(--hd-fg); border-color: var(--hd-border-strong); } .b2-seg span.good.on .ic { color: var(--hd-fg); }
.b2-seg span.fix.on { background: var(--hd-warning-subtle); color: var(--hd-warning-strong); }
.b2-link { display: flex; align-items: center; gap: 8px; height: 36px; padding: 0 4px 0 12px; border: 1px solid var(--hd-edge); border-radius: 10px; font-size: 14px; color: var(--hd-fg); background: var(--hd-surface); }
.b2-link > .ic { color: var(--hd-fg-subtle); } .b2-link > span { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.b2-link .btn { height: 28px !important; min-height: 0 !important; padding: 0 10px !important; font-size: 13px !important; }
.b2-files { display: flex; align-items: center; gap: 8px; }
.b2-shot { width: 64px; height: 64px; border-radius: 10px; object-fit: cover; flex: none; border: 1px solid var(--hd-edge); }
.b2-full { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 560; color: var(--hd-accent-strong, var(--hd-link)); margin-left: 4px; }
.b2-match { margin-left: auto; display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 560; color: var(--hd-fg-muted); }
.b2-ol { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.b2-ol span { font-size: 13px; color: var(--hd-fg-muted); } .b2-ol b { font-size: 14px; font-weight: 560; display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; }
.b2-why { display: flex; flex-wrap: wrap; gap: 6px; }
.b2-chip { height: 30px; padding: 0 12px; border-radius: 10px; display: inline-flex; align-items: center; font-size: 13px; font-weight: 500; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.b2-chip.on { background: var(--hd-accent-subtle); color: var(--hd-info-strong); border-color: transparent; }
.b2-note { padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; flex: 1; min-height: 0; }
.b2-ta { flex: 1; border: 1px solid var(--hd-border-input, var(--hd-edge)); border-radius: 10px; padding: 12px; font-size: 14px; line-height: 21px; color: var(--hd-fg); background: var(--hd-surface); }
.b2-cost { padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; flex: none; }
.b2-ln { display: flex; justify-content: space-between; font-size: 14px; color: var(--hd-fg-muted); }
.b2-ln .num { color: var(--hd-fg); }
.b2-ln.tot { border-top: 1px solid var(--hd-edge); padding-top: 8px; color: var(--hd-fg); font-weight: 600; } .b2-ln.tot b { font-weight: 600; }
.b2-band { flex: none; height: 72px; display: flex; align-items: center; gap: 10px; padding: 0 28px; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.b2-money { display: flex; align-items: baseline; gap: 8px; font-size: 14px; color: var(--hd-fg-muted); } .b2-money b { font-family: var(--font-brand); font-size: 20px; font-weight: 700; color: var(--hd-fg); }

/* ---------- 6 wallet ---------- */
.shell .pg:has(> .b2-two) { gap: 16px; }
.b2-sq { width: 44px; padding: 0 !important; justify-content: center; }
.b2-tiles { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; flex: none; }
.b2-tile { padding: 14px 20px 16px; display: flex; flex-direction: column; gap: 4px; }
.b2-tile > span { font-size: 14px; font-weight: 560; color: var(--hd-fg-muted); }
.b2-big { font-family: var(--font-brand); font-size: 36px; line-height: 44px; font-weight: 700; letter-spacing: -.02em; color: var(--hd-fg); }
.b2-tile small { font-size: 13px; color: var(--hd-fg-muted); }
.b2-two { flex: 1; min-height: 0; display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 16px; }
.b2-col { display: flex; flex-direction: column; gap: 12px; min-height: 0; min-width: 0; }
.b2-tabs { display: flex; gap: 24px; border-bottom: 1px solid var(--hd-edge); flex: none; }
.b2-tabs span { display: inline-flex; align-items: center; gap: 6px; height: 40px; font-size: 14.5px; font-weight: 560; color: var(--hd-fg-muted); border-bottom: 2px solid transparent; margin-bottom: -1px; }
.b2-tabs span.on { color: var(--hd-fg); border-bottom-color: var(--hd-accent); } .b2-tabs i { font-style: normal; font-size: 13.5px; font-weight: 500; color: var(--hd-fg-subtle); }
.b2-list { display: flex; flex-direction: column; gap: 8px; }
.b2-row { display: flex; align-items: center; gap: 12px; height: 64px; padding: 0 16px; background: var(--hd-surface-raised); border: 1px solid var(--hd-edge); border-radius: 12px; }
.b2-amt { font-size: 15px; font-weight: 600; color: var(--hd-fg); white-space: nowrap; } .b2-amt.in { color: var(--hd-success-strong); }
.b2-inv, .b2-tds { padding: 14px 18px 6px; display: flex; flex-direction: column; gap: 8px; }
.b2-sh { display: flex; flex-direction: column; gap: 2px; } .b2-sh2 b { font-size: 17px; line-height: 24px; font-weight: 600; } .b2-sh2 span { font-size: 13px; color: var(--hd-fg-muted); } .b2-sh2 { display: flex; gap: 10px; flex-direction: row; align-items: baseline; gap: 10px; } .b2-sh b { font-size: 17px; line-height: 24px; font-weight: 600; } .b2-sh span { font-size: 13px; color: var(--hd-fg-muted); line-height: 18px; }
.b2-sums { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; padding: 4px 0 6px; } .b2-sums.two { grid-template-columns: repeat(2, 1fr); }
.b2-sums span { display: block; font-size: 13px; color: var(--hd-fg-muted); } .b2-sums b { font-size: 18px; font-weight: 600; letter-spacing: -.01em; }
.b2-irs { display: flex; flex-direction: column; }
.b2-ir { display: flex; align-items: center; gap: 12px; min-height: 44px; border-top: 1px solid var(--hd-edge); } .b2-irs .b2-ir { min-height: 50px; }
.b2-ir.void .b2-iamt b, .b2-ir.void .b2-tt b { color: var(--hd-fg-subtle); }
.b2-iamt { display: flex; flex-direction: column; align-items: flex-end; gap: 1px; } .b2-iamt b { font-size: 15px; font-weight: 600; } .b2-iamt small { font-size: 12.5px; color: var(--hd-fg-muted); }
.b2-ir .badge { min-width: 52px; justify-content: center; }
.b2-dl { width: 32px; padding: 0 !important; justify-content: center; color: var(--hd-fg-muted) !important; }

/* ---------- 7 team ---------- */
.shell .pg:has(> .b2-split) { padding: 0; gap: 0; }
.b2-split { flex: 1; min-height: 0; display: grid; grid-template-columns: 220px minmax(0, 1fr); }
.b2-rail { padding: 24px 12px; border-right: 1px solid var(--hd-edge); display: flex; flex-direction: column; gap: 2px; background: var(--hd-surface); }
.b2-rg { font-size: 12px; font-weight: 560; color: var(--hd-fg-subtle); padding: 12px 10px 4px; } .b2-rg:first-child { padding-top: 0; }
.b2-ri { display: flex; align-items: center; gap: 10px; height: 34px; padding: 0 10px; border-radius: 8px; font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); }
.b2-ri .ic { color: var(--hd-fg-subtle); } .b2-ri.on { background: color-mix(in oklab, var(--hd-fg) 6%, transparent); color: var(--hd-fg); font-weight: 560; } .b2-ri.on .ic { color: var(--hd-accent); }
.b2-tmain { padding: 24px 28px; display: flex; flex-direction: column; gap: 22px; min-width: 0; min-height: 0; }
.b2-mlist { display: flex; flex-direction: column; gap: 8px; }
.b2-mrow { position: relative; display: flex; align-items: center; gap: 14px; height: 68px; padding: 0 18px; background: var(--hd-surface-raised); border: 1px solid var(--hd-edge); border-radius: 12px; }
.b2-av44 { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; flex: none; }
.b2-tt b em { font-style: normal; font-weight: 500; font-size: 13px; color: var(--hd-fg-subtle); margin-left: 8px; }
.b2-rc { position: relative; width: 200px; flex: none; }
.b2-role { display: flex; align-items: center; justify-content: space-between; height: 36px; padding: 0 10px 0 12px; border-radius: 10px; font-size: 14px; font-weight: 560; color: var(--hd-fg); background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.b2-role .ic { color: var(--hd-fg-muted); } .b2-role.fixed { border-color: transparent; background: none; padding-left: 0; color: var(--hd-fg-muted); } .b2-role.open { background: var(--hd-bg-subtle); }
.b2-seen { width: 130px; flex: none; text-align: right; font-size: 13px; color: var(--hd-fg-muted); }
.b2-menu { position: absolute; z-index: 5; right: 0; top: 42px; width: 500px; padding: 4px; background: var(--hd-surface-raised); border: 1px solid var(--hd-edge); border-radius: 12px; box-shadow: var(--hd-shadow-e3); display: flex; flex-direction: column; gap: 2px; }
.b2-mi { padding: 8px 10px; border-radius: 8px; display: flex; flex-direction: column; gap: 2px; } .b2-mi:first-child { }
.b2-mit { display: flex; align-items: center; justify-content: space-between; } .b2-mit b { font-size: 14px; font-weight: 600; } .b2-mit .ic { color: var(--hd-accent); }
.b2-mi small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.b2-mi:has(.ic) { background: color-mix(in oklab, var(--hd-fg) 6%, transparent); }
.b2-linkc { display: flex; align-items: center; gap: 12px; padding: 14px 18px; }
.b2-linkc .b2-role { width: 160px; flex: none; }
.b2-order { padding: 14px 16px; display: flex; flex-direction: column; gap: 6px; flex: none; }
.b2-order .b2-ol { min-height: 22px; flex-direction: row; justify-content: space-between; align-items: center; gap: 12px; }
.b2-sec { display: flex; flex-direction: column; gap: 10px; }
.b2-sech { display: flex; align-items: baseline; gap: 8px; } .b2-sech b { font-size: 15px; font-weight: 600; } .b2-sech span { font-size: 13px; color: var(--hd-fg-muted); }
.b2-mrow .btn.s.sm { flex: none; }
/* wallet, calm (bw-) */
.bw-bal { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 20px 24px; display: flex; align-items: center; gap: 24px; margin-bottom: 20px; }
.bw-bm { display: flex; flex-direction: column; flex: 1; min-width: 0; }
.bw-act { display: flex; gap: 10px; flex: none; }
.bw-bm small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.bw-bm > b { font-family: var(--font-brand); font-size: 40px; line-height: 46px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; color: var(--hd-fg); margin-top: 2px; }
.bw-bm p { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.bw-bm p .num { color: var(--hd-fg); font-weight: 600; }
.bw-grid { display: grid; grid-template-columns: 1.25fr 1fr; gap: 20px; align-items: start; }
.bw-side { display: flex; flex-direction: column; gap: 20px; }
.bw-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 4px 20px; }
.bw-h { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; padding: 14px 0 10px; }
.bw-h > b { font-family: var(--font-brand); font-size: 17px; line-height: 22px; font-weight: 650; }
.bw-h > span { font-size: 13px; color: var(--hd-fg-muted); } .bw-h > span .num { color: var(--hd-fg); font-weight: 600; }
.bw-lk { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); }
.bw-lr { display: flex; align-items: center; gap: 16px; min-height: 56px; border-top: 1px solid var(--hd-edge); }
.bw-tx { display: flex; flex-direction: column; gap: 1px; flex: 1; min-width: 0; }
.bw-tx b { font-size: 14.5px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.bw-tx small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.bw-d { font-size: 13px; color: var(--hd-fg-subtle); width: 52px; text-align: right; flex: none; }
.bw-a { font-size: 14.5px; font-weight: 600; color: var(--hd-fg); min-width: 96px; text-align: right; flex: none; }
.bw-a.cr { color: var(--hd-success-strong); }
.bw-ic { color: var(--hd-fg-subtle); flex: none; display: inline-flex; }
.bw-lr.void .bw-tx b, .bw-lr.void .bw-a { color: var(--hd-fg-subtle); }
.bw-lr.void .bw-a { text-decoration: line-through; }
/* team, calm */
.shell:has(.b2-split) { height: auto; min-height: 900px; }
.shell:has(.b2-split) > .mn { overflow: visible; }
.shell .pg:has(> .b2-split) { overflow: visible; }
.b2-role.q { border-color: transparent; background: none; padding-left: 0; gap: 6px; justify-content: flex-start; color: var(--hd-fg); }
.b2-lk { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); white-space: nowrap; }
.b2-acts { display: flex; gap: 20px; flex: none; }
.b2-linkc { padding: 16px 20px; }
.b2-linkc .b2-role { width: 150px; flex: none; }
.b2-sec .bw-card .bw-lr:first-child { border-top: 0; }
"""
