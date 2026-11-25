# Layer (xb1). Prefix every class to avoid clashes. Brand desktop shell + pages 1-4.
XB1 = """
/* ---------- brand shell: sidebar + top bar ---------- */
.shell > .sb { background: var(--hd-surface); padding: 14px 12px 12px; gap: 2px; }
.shell > .sb .ws { height: 44px; padding: 0 8px; margin-bottom: 10px; border: 1px solid var(--hd-edge); border-radius: 10px; background: var(--hd-surface); box-shadow: none; }
.shell > .sb .ws b { font-size: 14px; font-weight: 600; }
.shell > .sb .ws .ic { color: var(--hd-fg-muted); flex: none; }
.shell > .sb .sbh { font: 560 12px/16px var(--font-ui); color: var(--hd-fg-subtle); padding: 16px 10px 4px; }
.shell > .sb .nav { height: 36px; border-radius: 8px; font-size: 14px; font-weight: 500; gap: 10px; color: var(--hd-fg-muted); letter-spacing: 0; box-shadow: none; }
.shell > .sb .nav .ic { width: 18px; height: 18px; color: var(--hd-fg-muted); }
.shell > .sb .nav .cnt { font-size: 12.5px; font-weight: 500; color: var(--hd-fg-subtle); }
.shell > .sb .nav.on { background: var(--hd-accent-subtle); color: var(--hd-link); font-weight: 560; box-shadow: none; }
.shell > .sb .nav.on .ic, .shell > .sb .nav.on .cnt { color: var(--hd-link); }
.shell > .sb .me { border-top: 0; padding: 0 8px; height: 52px; margin-top: 0; }
.shell > .sb .me small { font-size: 12.5px; }
.shell > .sb .sbfoot { border-top: 1px solid var(--hd-edge); padding-top: 8px; }
.shell .hdr { height: 56px; background: var(--hd-surface); border-bottom: 1px solid var(--hd-edge); }
.b1-search { display: inline-flex; align-items: center; gap: 8px; width: 260px; height: 36px; padding: 0 12px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); color: var(--hd-fg-subtle); font-size: 14px; }
.b1-search .ic { color: var(--hd-fg-muted); }
.b1-search em { margin-left: auto; font: 400 12.5px var(--font-ui); font-style: normal; color: var(--hd-fg-subtle); }
.shell .hdr .iconbtn { width: 36px; height: 36px; border-radius: 10px; }

/* ---------- page frame ---------- */
.shell .pg:has(> .b1-wrap) { padding: 28px 32px 36px; gap: 0; overflow: visible; }
.shell:has(.b1-wrap.tall) { height: auto; min-height: 900px; }
.shell:has(.b1-wrap.tall) > .mn { overflow: visible; }
.b1-wrap { display: flex; flex-direction: column; min-width: 0; }
.b1-head { display: flex; align-items: flex-start; gap: 12px; }
.b1-head .t { flex: 1; min-width: 0; }
.b1-h1 { margin: 0; font: 700 32px/36px var(--font-brand); letter-spacing: -.035em; color: var(--hd-fg); }
.b1-sub { margin: 6px 0 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); }
.b1-acts { display: flex; align-items: center; gap: 8px; flex: none; }
.b1-wrap .btn { width: auto !important; min-width: 0 !important; height: 44px !important; padding: 0 18px !important; border-radius: 12px !important; font-size: 14px; font-weight: 560; display: inline-flex; align-items: center; justify-content: center; gap: 8px; white-space: nowrap; }
.b1-wrap .btn.sm { height: 36px !important; padding: 0 14px !important; border-radius: 10px !important; }
.b1-wrap .btn.md { height: 40px !important; padding: 0 16px !important; border-radius: 10px !important; }
.b1-wrap .btn.icon { width: 44px !important; padding: 0 !important; }
.b1-wrap .btn.icon.sm { width: 36px !important; }
.b1-wrap .btn .ic { width: 16px !important; height: 16px !important; }
.b1-h2 { margin: 0; font: 600 17px/24px var(--font-ui); letter-spacing: -.01em; color: var(--hd-fg); }
.b1-sechd { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.b1-sechd .b1-h2 { flex: 1; }
.b1-link { font-size: 14px; font-weight: 560; color: var(--hd-link); }
.b1-meta { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.b1-num { font-variant-numeric: tabular-nums; }
.b1-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 20px; min-width: 0; }
.b1-row { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; min-width: 0; }
.b1-tile { width: 40px; height: 40px; flex: none; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); box-shadow: 0 1px 2px rgba(16,20,38,.06); display: grid; place-items: center; }
.b1-tile .ic { width: 20px; height: 20px; }
.b1-tile img { width: 20px; height: 20px; border-radius: 5px; object-fit: cover; }
.b1-thumb { width: 44px; height: 44px; flex: none; border-radius: 10px; object-fit: cover; display: block; }
.b1-st { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: var(--hd-fg-muted); }
.b1-st img { width: 14px; height: 14px; border-radius: 3px; }
.b1-title { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); letter-spacing: -.005em; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

/* ---------- 1 Home ---------- */
.b1-chips { display: flex; gap: 8px; margin-top: 20px; }
.b1-chip { display: inline-flex; align-items: center; gap: 8px; height: 36px; padding: 0 14px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg-muted); }
.b1-chip b { font-weight: 600; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.b1-chip.zero, .b1-chip.zero b { color: var(--hd-fg-subtle); }
.b1-home { display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 32px; margin-top: 28px; align-items: start; }
.b1-todo { display: flex; flex-direction: column; gap: 8px; }
.b1-todo .b1-row { display: flex; align-items: center; gap: 14px; padding: 14px 20px; min-height: 68px; box-sizing: border-box; }
.b1-todo .tx { flex: 1; min-width: 0; }
.b1-todo .b1-title { white-space: normal; }
.b1-act { flex: none; font-size: 14.5px; font-weight: 600; color: var(--hd-link); }
.b1-meta .due, .b1-meta.due { color: var(--hd-warning-strong); }
.b1-last { padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
.b1-last b { display: block; margin-top: 2px; font: 700 40px/46px var(--font-brand); letter-spacing: -.03em; font-variant-numeric: tabular-nums; }
.b1-last p { margin: 0; font-size: 14px; line-height: 22px; color: var(--hd-fg-muted); text-align: right; }
.b1-last p span { display: block; }
.b1-side { display: flex; flex-direction: column; gap: 32px; }
.b1-wal { padding: 20px 24px; display: flex; flex-direction: column; }
.b1-wal .big { display: block; margin-top: 2px; font: 700 40px/46px var(--font-brand); letter-spacing: -.03em; font-variant-numeric: tabular-nums; }
.b1-wal p { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.b1-wal p b { font-weight: 600; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.b1-wal .foot { display: grid; grid-template-columns: 1fr; margin-top: 16px; }
.b1-wal .foot .btn { width: 100% !important; }
.b1-live { display: flex; flex-direction: column; gap: 8px; }
.b1-live .b1-row { display: flex; align-items: center; gap: 12px; padding: 10px 14px; }
.b1-live .tx { flex: 1; min-width: 0; }

/* ---------- 2 Campaigns list ---------- */
.b1-tabs { display: flex; gap: 28px; margin-top: 24px; border-bottom: 1px solid var(--hd-edge); }
.b1-tabs span { display: inline-flex; align-items: center; gap: 8px; height: 44px; font-size: 15px; font-weight: 560; color: var(--hd-fg-muted); border-bottom: 2px solid transparent; margin-bottom: -1px; }
.b1-tabs span i { font-style: normal; font-size: 13.5px; font-weight: 500; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.b1-tabs span.on { color: var(--hd-fg); border-bottom-color: var(--hd-accent); }
.b1-tabs span.on i { color: var(--hd-link); }
.b1-tool { display: flex; align-items: center; gap: 8px; margin-top: 20px; }
.b1-field { display: flex; align-items: center; gap: 10px; height: 44px; padding: 0 14px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 15px; color: var(--hd-fg-subtle); }
.b1-field .ic { color: var(--hd-fg-muted); width: 18px; height: 18px; }
.b1-tool .b1-field { flex: 1; max-width: 420px; }
.b1-sort { display: inline-flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg-muted); }
.b1-sort b { font-weight: 560; color: var(--hd-fg); }
.b1-sort .ic { width: 16px; height: 16px; }
.b1-cols, .b1-crow { display: grid; grid-template-columns: 44px minmax(0, 1.7fr) 128px 118px 154px 104px; column-gap: 16px; align-items: center; }
.b1-cols { margin-top: 20px; padding: 0 16px; font-size: 12.5px; font-weight: 560; color: var(--hd-fg-subtle); }
.b1-cols .r, .b1-crow .r { text-align: right; justify-self: end; }
.b1-list { display: flex; flex-direction: column; gap: 8px; margin-top: 8px; }
.b1-crow { padding: 12px 16px; min-height: 68px; box-sizing: border-box; }
.b1-crow .tx { min-width: 0; }
.b1-crow .b1-st { margin-top: 2px; }
.b1-crow .dt { font-size: 14px; color: var(--hd-fg-muted); }
.b1-crow .cr { font-size: 14px; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.b1-crow .cr small { color: var(--hd-fg-muted); font-size: 14px; }
.b1-crow .sp { font-size: 15px; font-weight: 600; font-variant-numeric: tabular-nums; }
.b1-crow .sp.none { color: var(--hd-fg-subtle); font-weight: 400; }
.b1-sx { font-size: 14px; color: var(--hd-fg-muted); }
.b1-crow .none { color: var(--hd-fg-subtle); }

/* ---------- 3 Campaign detail ---------- */
.b1-dh { display: flex; align-items: center; gap: 16px; }
.b1-dh .b1-thumb { width: 64px; height: 64px; border-radius: 12px; }
.b1-dh .t { flex: 1; min-width: 0; }
.b1-dh .b1-h1 { font-size: 30px; line-height: 34px; }
.b1-dh .line { display: flex; align-items: center; gap: 10px; margin-top: 8px; font-size: 14px; color: var(--hd-fg-muted); }
.b1-line { margin: 16px 0 0; font-size: 14.5px; line-height: 22px; color: var(--hd-fg-muted); }
.b1-line b { font-weight: 600; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.b1-det { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: 32px; margin-top: 28px; align-items: start; }
.b1-col { display: flex; flex-direction: column; gap: 32px; min-width: 0; }
.b1-stack { display: flex; flex-direction: column; gap: 8px; }
.b1-brief { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.b1-brief h4 { margin: 0 0 12px; font: 600 17px/24px var(--font-ui); }
.b1-brief .it { display: flex; gap: 10px; font-size: 14px; line-height: 20px; color: var(--hd-fg); align-items: flex-start; }
.b1-brief .it .ic { width: 16px; height: 16px; margin-top: 2px; flex: none; }
.b1-brief .k { font-size: 12.5px; font-weight: 560; color: var(--hd-fg-subtle); margin-bottom: 6px; }
.b1-brief .it .ic { color: var(--hd-fg-muted); }
.b1-task { display: flex; align-items: center; gap: 14px; padding: 12px 16px; }
.b1-task .tx { flex: 1; min-width: 0; }
.b1-task .n { font-size: 13px; font-weight: 500; color: var(--hd-fg-subtle); width: 16px; font-variant-numeric: tabular-nums; }
.b1-dl { display: grid; grid-template-columns: 1fr 1fr; column-gap: 32px; row-gap: 18px; }
.b1-dl .k { font-size: 13px; color: var(--hd-fg-muted); margin-bottom: 4px; }
.b1-dl .v { font-size: 15px; line-height: 22px; color: var(--hd-fg); display: flex; align-items: center; gap: 8px; min-width: 0; }
.b1-dl .v img { width: 24px; height: 24px; border-radius: 6px; object-fit: cover; }
.b1-dl .v .mono { font: 400 14px var(--font-mono); color: var(--hd-fg-muted); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.b1-dl .v .btn { flex: none; }
.b1-cost { padding: 20px 24px; display: flex; flex-direction: column; }
.b1-cost .h { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.b1-cost .big { display: block; margin-top: 2px; font: 700 40px/46px var(--font-brand); letter-spacing: -.03em; font-variant-numeric: tabular-nums; }
.b1-cost p { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }
.b1-cost .foot { margin-top: 16px; }
.b1-cost .foot .btn { width: 100% !important; }

/* ---------- 4 Composer (focus mode) ---------- */
.shell.b1-focus { display: flex; flex-direction: column; height: auto; min-height: 900px; }
.b1-top { height: 64px; flex: none; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 0 20px; background: var(--hd-surface); border-bottom: 1px solid var(--hd-edge); }
.b1-top .l { display: flex; align-items: center; gap: 12px; }
.b1-top .l b { font: 600 16px var(--font-ui); letter-spacing: -.01em; }
.b1-top .r { display: flex; align-items: center; justify-content: flex-end; gap: 16px; font-size: 13.5px; color: var(--hd-fg-muted); }
.b1-top .r .sv { display: inline-flex; align-items: center; gap: 6px; }
.b1-top .r .sv .ic { width: 16px; height: 16px; color: var(--hd-fg-subtle); }
.b1-top .r .of { font-variant-numeric: tabular-nums; }
.b1-ib { width: 36px; height: 36px; border-radius: 10px; display: inline-grid; place-items: center; color: var(--hd-fg-muted); }
.b1-ib .ic { width: 20px; height: 20px; }
.b1-track { display: flex; align-items: center; gap: 12px; }
.b1-track .s { display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 560; color: var(--hd-fg-subtle); }
.b1-track .s .ic { width: 18px; height: 18px; }
.b1-track .s.done { color: var(--hd-fg-muted); } .b1-track .s.done .ic { color: var(--hd-accent); }
.b1-track .s.on { color: var(--hd-link); } .b1-track .s.on .ic { color: var(--hd-link); }
.b1-track .ln { width: 36px; height: 1px; background: var(--hd-edge); }
.b1-body { flex: 1; display: grid; grid-template-columns: 680px 340px; gap: 32px; justify-content: center; padding: 32px 32px 40px; align-items: start; }
.b1-form { display: flex; flex-direction: column; gap: 16px; min-width: 0; }
.b1-form .b1-h1 { font-size: 34px; line-height: 38px; }
.b1-form .intro { margin-bottom: 8px; }
.b1-fc { padding: 20px 24px; display: flex; flex-direction: column; gap: 14px; }
.b1-fc > .hd { display: flex; align-items: baseline; gap: 12px; }
.b1-fc > .hd .b1-h2 { flex: 1; }
.b1-fc .hint { font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); margin: 0; }
.b1-fc .lab { font-size: 14px; font-weight: 560; color: var(--hd-fg); }
.b1-fc .lab em { font-style: normal; font-weight: 400; color: var(--hd-fg-muted); }
.b1-seg { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
.b1-seg span { height: 40px; border-radius: 10px; display: grid; place-items: center; font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.b1-seg span.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-link); font-weight: 600; }
.b1-opts { display: flex; flex-wrap: wrap; gap: 8px; }
.b1-opt { display: inline-flex; align-items: center; height: 36px; padding: 0 14px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }
.b1-opt.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-link); font-weight: 600; }
.b1-payrow { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.b1-fc .b1-dg { display: flex; flex-direction: column; gap: 14px; }
.b1-inl { display: flex; align-items: center; gap: 16px; }
.b1-pay { display: flex; align-items: baseline; gap: 10px; }
.b1-pay b { font: 700 26px/30px var(--font-brand); letter-spacing: -.03em; font-variant-numeric: tabular-nums; }
.b1-pay span { font-size: 15px; color: var(--hd-fg-muted); }
.b1-in { display: flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-border-input); font-size: 15px; color: var(--hd-fg); }
.b1-in .pre { color: var(--hd-fg-muted); }
.b1-in.ta { height: auto; min-height: 68px; align-items: flex-start; padding: 12px 14px; line-height: 22px; }
.b1-in.ph { color: var(--hd-fg-subtle); }
.b1-stepper { display: inline-flex; align-items: center; height: 44px; border-radius: 12px; border: 1px solid var(--hd-border-input); background: var(--hd-surface); }
.b1-stepper span { width: 44px; display: grid; place-items: center; color: var(--hd-fg-muted); }
.b1-stepper b { min-width: 56px; text-align: center; font: 600 17px var(--font-ui); font-variant-numeric: tabular-nums; }
.b1-two { display: grid; grid-template-columns: 1fr auto; align-items: center; gap: 16px; }
.b1-aside { font-size: 14px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; }
.b1-aside b { color: var(--hd-fg); font-weight: 600; }
.b1-grp { display: flex; flex-direction: column; gap: 10px; }
.b1-trow { display: flex; align-items: center; gap: 14px; padding: 12px 14px; border: 1px solid var(--hd-edge); border-radius: 12px; background: var(--hd-surface); }
.b1-trow .tx { flex: 1; min-width: 0; }
.b1-trow .tx .b1-title { font-size: 15px; }
.b1-trow > .ic { color: var(--hd-fg-subtle); width: 18px; height: 18px; flex: none; }
.b1-drop { height: 44px; border-radius: 12px; border: 1px dashed var(--hd-border-strong); display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 14px; color: var(--hd-fg-muted); }
.b1-drop .ic { width: 18px; height: 18px; }
.b1-cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.b1-sum { position: sticky; top: 24px; padding: 20px; display: flex; flex-direction: column; gap: 16px; }
.b1-sum .pr { display: flex; align-items: center; gap: 12px; }
.b1-sum .pr .tx { min-width: 0; }
.b1-sum dl { margin: 0; display: flex; flex-direction: column; gap: 14px; }
.b1-sum dt { font-size: 13px; color: var(--hd-fg-muted); margin-bottom: 2px; }
.b1-sum dd { margin: 0; font-size: 15px; line-height: 21px; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.b1-sum .rule { border-top: 1px solid var(--hd-edge); padding-top: 16px; font-size: 13px; line-height: 19px; color: var(--hd-fg-muted); }
.b1-foot { height: 72px; flex: none; display: flex; align-items: center; justify-content: space-between; padding: 0 32px; background: var(--hd-surface); border-top: 1px solid var(--hd-edge); }
.b1-foot .btn { height: 44px !important; }
.shell.b1-focus .btn { width: auto !important; min-width: 0 !important; padding: 0 20px !important; border-radius: 12px !important; font-size: 15px; font-weight: 560; display: inline-flex; align-items: center; justify-content: center; gap: 8px; }
.shell.b1-focus .btn .ic { width: 16px !important; height: 16px !important; }
"""
