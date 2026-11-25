# Screen layer (xh2). Prefix every class to avoid clashes.
XH2 = """
.phone .scr:has(.e1-pg) { background: var(--hd-canvas); }
.phone .scr:has(.e1-pg) .sbar { background: var(--hd-canvas); }
.phone .e1-bar { background: var(--hd-canvas); gap: 14px; }
.phone .e1-bar .e1-r { margin-left: auto; display: flex; align-items: center; gap: 16px; }
.phone .e1-bar .e1-ib { display: flex; color: var(--hd-fg); }
.phone .e1-bar .e1-bt { font-size: 16px; font-weight: 600; font-family: var(--font-ui); }
.phone .e1-bar .e1-bt0 { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; }
.phone .e1-bar .e1-note { font-size: 13px; color: var(--hd-fg-subtle); }
.phone .e1-bar .e1-mk { font-size: 14px; text-decoration: none; }
.phone .e1-pg { gap: 10px; }
.phone .e1-pg .hm-h { margin-top: 0; }
.phone .e1-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; }
.phone .e1-row .ic { color: inherit; }
.phone .e1-row small { display: flex; align-items: center; gap: 6px; }
.phone .e1-row small img.plat { flex: none; border-radius: 4px; width: 14px; height: 14px; }
.phone .e1-row .bankl { width: 22px; height: 22px; border-radius: 0; }
.phone .e1-row > .x-tile, .phone .e1-row > .bankt { width: 40px !important; height: 40px !important; flex: none; border-radius: 10px !important; display: grid; place-items: center; }
.phone .e1-row > .x-tile .ic { width: 20px; height: 20px; }
.phone .e1-row > .bankt .bankl { width: 22px; height: 22px; }
.phone .e1-amt { font-size: 15px; font-weight: 600; color: var(--hd-fg); flex: none; }
.phone .e1-amt.pos { color: var(--hd-success-strong); }
.phone .e1-amt.mut { color: var(--hd-fg-muted); }
.phone .e1-lk { font-size: 14px; text-decoration: none; flex: none; }

.phone .e1-wf { padding: 0 0 16px; }
.phone .e1-wf .btn { height: 44px; }
/* tracking */
.phone .e1-hd { min-height: 64px; }
.phone .e1-tl { padding: 16px 16px 4px; display: flex; flex-direction: column; }
.phone .e1-st { position: relative; display: flex; gap: 14px; padding-bottom: 18px; }
.phone .e1-st > i { position: relative; z-index: 1; flex: none; width: 20px; height: 20px; border-radius: 50%; box-sizing: border-box; display: grid; place-items: center; margin-top: 0; background: var(--hd-surface); border: 2px solid var(--hd-border-strong); }
.phone .e1-st:not(:last-child)::before { content: ""; position: absolute; left: 9px; top: 20px; bottom: 0; width: 2px; background: var(--hd-edge); }
.phone .e1-st.done > i { background: var(--hd-accent); border-color: var(--hd-accent); }
.phone .e1-st.done:not(:last-child)::before { background: var(--hd-accent); }
.phone .e1-st.now > i { border-color: var(--hd-accent); background: var(--hd-surface); }
.phone .e1-st.now > i::after { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-accent); }
.phone .e1-st b { display: block; font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg-muted); }
.phone .e1-st.done b, .phone .e1-st.now b { color: var(--hd-fg); }
.phone .e1-st small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .e1-mn { padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; }
.phone .e1-mn .e1-big { display: flex; align-items: baseline; justify-content: space-between; padding-bottom: 10px; border-bottom: 1px solid var(--hd-edge); }
.phone .e1-mn .e1-big span { font-size: 14px; color: var(--hd-fg-muted); }
.phone .e1-mn .e1-big b { font-family: var(--font-brand); font-size: 30px; line-height: 34px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; }
.phone .e1-mn > div:not(.e1-big) { display: flex; justify-content: space-between; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .e1-mn > div:not(.e1-big) b { font-weight: 600; color: var(--hd-fg); }
.phone .e1-cta { background: var(--hd-surface); }
.phone .e1-cta .btn.lg { height: 48px; }

/* submit tasks */
.phone .e1-hb p { margin: 4px 4px 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .e1-tk { padding: 14px 14px 14px; display: flex; flex-direction: column; }
.phone .e1-th { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.phone .e1-th b { font-size: 15px; font-weight: 600; flex: 1; }
.phone .e1-th small { font-size: 13px; color: var(--hd-fg-muted); }
.phone .e1-tk label { font-size: 13px; line-height: 18px; font-weight: 600; color: var(--hd-fg-muted); margin: 0 0 6px; display: block; }
.phone .e1-tk label .num { font-weight: 400; color: var(--hd-fg-subtle); margin-left: 4px; }
.phone .e1-in { height: 44px; border-radius: 12px; border: 1px solid var(--hd-edge); background: var(--hd-surface); display: flex; align-items: center; padding: 0 12px; font-size: 14px; color: var(--hd-fg); margin-bottom: 12px; }
.phone .e1-in span { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .e1-shs { display: flex; gap: 8px; }
.phone .e1-sh { position: relative; width: 56px; height: 56px; border-radius: 10px; flex: none; }
.phone .e1-sh img { width: 100%; height: 100%; border-radius: 10px; object-fit: cover; display: block; }
.phone .e1-sh span { position: absolute; top: -5px; right: -5px; width: 18px; height: 18px; border-radius: 50%; background: var(--hd-fg); color: var(--hd-surface); display: grid; place-items: center; }
.phone .e1-add { border: 1px solid var(--hd-edge); background: var(--hd-surface); display: grid; place-items: center; color: var(--hd-fg-muted); }
.phone .e1-att { margin: 2px 4px 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }

/* success */
.phone .e1-ok { justify-content: center; gap: 12px; padding-bottom: 24px; }
.phone .e1-ill { display: flex; justify-content: center; margin-bottom: 4px; }
.phone .e1-ill img { width: 168px; height: 168px; object-fit: contain; }
.phone .e1-okt { text-align: center; margin-bottom: 8px; }
.phone .e1-okt p { margin: 6px 8px 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); }
.phone .e1-cta2 { flex-direction: column; gap: 8px; }

/* inbox */
.phone .e1-tabs { display: flex; gap: 22px; border-bottom: 1px solid var(--hd-edge); margin: 0 4px 2px; }
.phone .e1-tabs span { padding: 8px 0 10px; font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); position: relative; }
.phone .e1-tabs span.on { color: var(--hd-fg); }
.phone .e1-tabs span.on::after { content: ""; position: absolute; left: 0; right: 0; bottom: -1px; height: 2px; background: var(--hd-accent); }
.phone .e1-nr { min-height: 64px; padding-left: 12px; }
.phone .e1-nr .tx b { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .e1-ne { display: flex; align-items: center; flex: none; width: 8px; }
.phone .e1-ne i { width: 8px; height: 8px; border-radius: 50%; background: transparent; }
.phone .e1-ne i.on { background: var(--hd-accent); }

/* settings */
.phone .e1-id { min-height: 72px; padding: 12px 14px 12px 12px; }
.phone .e1-id img { width: 48px; height: 48px; border-radius: 50%; }
.phone .e1-gr { padding: 4px 0; overflow: hidden; }
.phone .e1-gi { display: flex; align-items: center; gap: 12px; min-height: 48px; padding: 0 14px; font-size: 15px; color: var(--hd-fg); }
.phone .e1-gi { position: relative; }
.phone .e1-gi + .e1-gi::before { content: ""; position: absolute; top: 0; left: 46px; right: 0; height: 1px; background: var(--hd-edge); }
.phone .e1-gi > .ic:first-child { color: var(--hd-fg-muted); flex: none; }
.phone .e1-gi b { font-weight: 500; flex: 1; }
.phone .e1-gi > span:not(.e1-c) { font-size: 13.5px; color: var(--hd-fg-muted); display: flex; align-items: center; gap: 6px; }
.phone .e1-gi .e1-vr { font-style: normal; font-weight: 600; color: var(--hd-link); }
.phone .e1-gi .e1-c { color: var(--hd-fg-subtle); display: flex; }
.phone .e1-gi .e1-bk img { border-radius: 4px; }
.phone .e1-lo .e1-gi { color: var(--hd-fg); }

/* empty search */
.phone .e1-nil { padding: 8px 4px 6px; }
.phone .e1-nil b { display: block; font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 650; }
.phone .e1-nil p { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .e1-lr .tx small { white-space: nowrap; }
.phone .scr[data-theme="light"] .xm1-bar.e1-bar.e1-bar.e1-bar { background: var(--hd-canvas) !important; border-top: 0 !important; }
"""
