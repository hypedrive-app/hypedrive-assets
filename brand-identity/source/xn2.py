# Screen layer (xn2). Prefix every class to avoid clashes.
XN2 = """
.phone .n2 { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 12px 16px 12px; background: var(--hd-canvas); font-family: var(--font-ui); }
.phone .n2-bar { gap: 8px; }
.phone .n2-bar .n2-bt { flex: 1; text-align: center; font-size: 16px; font-weight: 600; margin-right: 22px; }
.phone .n2 b, .phone .n2 small, .phone .n2 span { font-family: var(--font-ui); }
.phone .n2-card, .phone .n2-row { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; }
.phone .n2-row { display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 10px 14px 10px 12px; }
.phone .n2-row .tx, .phone .n2-prod .tx { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1; }
.phone .n2 b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .n2 small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n2 small.ok { color: var(--hd-success-strong); font-weight: 560; }
.phone .n2 small .plat { display: inline-block; vertical-align: -2px; margin-right: 4px; border-radius: 3px; }
.phone .n2-ti { width: 40px; height: 40px; border-radius: 10px; flex: none; display: flex; align-items: center; justify-content: center; }
.phone .n2-ti .ic, .phone .n2-ti img { width: 22px; height: 22px; }
.phone .n2-row .bankt { width: 40px; height: 40px; flex: none; }
.phone .n2-row .bankt img { width: 24px; height: 24px; }
.phone .n2-row > .ic, .phone .n2-sr > .ic:last-child { color: var(--hd-fg-subtle); flex: none; }
.phone .n2-lk { font-size: 15px; font-weight: 600; color: var(--hd-link); flex: none; }
.phone .n2-list { display: flex; flex-direction: column; }
.phone .n2-sr { display: flex; align-items: center; gap: 12px; min-height: 60px; padding: 8px 14px 8px 16px; }
.phone .n2-sr + .n2-sr { border-top: 1px solid var(--hd-edge); }
.phone .n2-sr > .ic:first-child { width: 20px; height: 20px; color: var(--hd-fg-muted); flex: none; }
.phone .n2-sr .tx { display: flex; flex-direction: column; gap: 1px; min-width: 0; flex: 1; }
.phone .n2 small.warn { color: var(--hd-warning-strong); }
.phone .n2-h { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 8px 4px -2px; }
.phone .n2-title { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 4px 4px 0; }
.phone .n2-prod { display: flex; align-items: center; gap: 12px; padding: 0 4px; }
.phone .n2-th { border-radius: 10px; object-fit: cover; flex: none; display: block; }
/* next step */
.phone .n2-next { padding: 16px; }
.phone .n2-next h1 { font-family: var(--font-brand); font-size: 26px; line-height: 30px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .n2-next p { margin: 2px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .n2-jr { display: flex; margin: 16px -4px 0; }
.phone .n2-js { flex: 1; position: relative; display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-subtle); }
.phone .n2-js i { width: 20px; height: 20px; border-radius: 50%; border: 1.5px solid var(--hd-edge-strong, var(--hd-edge)); background: var(--hd-surface); display: flex; align-items: center; justify-content: center; position: relative; z-index: 1; color: #fff; }
.phone .n2-js:not(:first-child)::before { content: ""; position: absolute; top: 9px; right: 50%; width: 100%; height: 2px; background: var(--hd-edge); }
.phone .n2-js.done::before, .phone .n2-js.now::before { background: var(--hd-accent); }
.phone .n2-js.done i { background: var(--hd-accent); border-color: var(--hd-accent); }
.phone .n2-js.now i { border-color: var(--hd-accent); border-width: 5px; }
.phone .n2-js.done, .phone .n2-js.now { color: var(--hd-fg); }
.phone .n2-js.now span { font-weight: 600; }
.phone .n2-money { padding: 16px; display: flex; flex-direction: column; }
.phone .n2-money > b { font-family: var(--font-brand); font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin-top: 2px; }
.phone .n2-money p, .phone .n2-amt p { margin: 2px 0 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n2-money p .num, .phone .n2-amt p .num { color: var(--hd-fg); font-weight: 600; }
/* bottom bar */
.phone .n2-bb { flex: none; display: flex; align-items: center; gap: 16px; padding: 12px 16px 10px; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .n2-bb .e { flex: 1; min-width: 0; }
.phone .n2-bb .e b { display: block; font-size: 15px; line-height: 20px; }
.phone .n2-bb .e small { display: block; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); white-space: nowrap; }
.phone .n2-bb .btn { height: 48px !important; flex: 1; }
.phone .n2-bb1 .btn { flex: none; width: 100%; }
.phone .n2-bb1 { flex-direction: column; align-items: stretch; gap: 8px; }
.phone .n2-bb1 p { margin: 0; text-align: center; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); }
/* withdraw */
.phone .n2-amt { display: flex; flex-direction: column; align-items: center; padding: 28px 0 14px; }
.phone .n2-amt b { font-family: var(--font-brand); font-size: 48px; line-height: 56px; font-weight: 700; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; }
.phone .n2-amt p { margin-top: 4px; }
.phone .n2-keys { margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); }
.phone .n2-keys span { height: 60px; display: flex; align-items: center; justify-content: center; font-family: var(--font-ui); font-size: 26px; font-weight: 500; color: var(--hd-fg); }
.phone .n2-keys span .ic { width: 22px; height: 22px; color: var(--hd-fg-muted); }
/* barter */
.phone .n2-vj { padding: 16px; display: flex; flex-direction: column; }
.phone .n2-vs { position: relative; display: flex; gap: 14px; padding-bottom: 20px; }
.phone .n2-vs:last-child { padding-bottom: 0; }
.phone .n2-vs i { width: 20px; height: 20px; flex: none; border-radius: 50%; border: 1.5px solid var(--hd-edge-strong, var(--hd-edge)); background: var(--hd-surface); display: flex; align-items: center; justify-content: center; color: #fff; position: relative; z-index: 1; margin-top: 0; }
.phone .n2-vs:not(:last-child)::before { content: ""; position: absolute; left: 9px; top: 20px; bottom: 0; width: 2px; background: var(--hd-edge); }
.phone .n2-vs.done:not(:last-child)::before { background: var(--hd-accent); }
.phone .n2-vs.done i { background: var(--hd-accent); border-color: var(--hd-accent); }
.phone .n2-vs.now i { border-color: var(--hd-accent); border-width: 5px; }
.phone .n2-vs .tx { display: flex; flex-direction: column; min-width: 0; }
.phone .n2-vs:not(.done):not(.now) b { color: var(--hd-fg-muted); font-weight: 560; }
"""
