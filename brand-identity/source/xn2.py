# Screen layer (xn2). Prefix every class to avoid clashes.
XN2 = """
.phone .n2 { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 10px; padding: 12px 16px 12px; background: var(--hd-canvas); font-family: var(--font-ui); }
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
.phone .n2-st { font-size: 13px; color: var(--hd-fg-muted); flex: none; }
.phone .n2-h { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 8px 4px -2px; }
.phone .n2-title { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 4px 4px 0; }
.phone .n2-prod { display: flex; align-items: center; gap: 12px; padding: 0 4px; }
.phone .n2-th { border-radius: 10px; object-fit: cover; flex: none; display: block; }
/* next step */
.phone .n2-next { padding: 16px; }
.phone .n2-next small { display: block; }
.phone .n2-next h1 { font-family: var(--font-brand); font-size: 26px; line-height: 30px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 2px 0 0; }
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
/* money */
.phone .n2-money, .phone .n2-sum { padding: 4px 16px 0; }
.phone .n2-kv { display: flex; justify-content: space-between; align-items: baseline; padding: 8px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .n2-kv b { font-family: var(--font-ui); font-size: 14px; font-weight: 500; color: var(--hd-fg); }
.phone .n2-kv em { font-style: normal; color: var(--hd-fg-subtle); margin-left: 4px; }
.phone .n2-tot { display: flex; justify-content: space-between; align-items: baseline; margin: 10px -16px 0; padding: 12px 16px; border-top: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg); }
.phone .n2-tot b { font-family: var(--font-brand); font-size: 22px; line-height: 26px; font-weight: 700; letter-spacing: -0.02em; }
/* bottom bar */
.phone .n2-bb { flex: none; display: flex; align-items: center; gap: 16px; padding: 12px 16px 10px; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .n2-bb .e { flex: 1; min-width: 0; }
.phone .n2-bb .e b { display: block; font-size: 15px; line-height: 20px; }
.phone .n2-bb .e small { display: block; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); white-space: nowrap; }
.phone .n2-bb .btn { height: 48px !important; flex: 1; }
.phone .n2-bb .e + .btn { flex: none; padding: 0 20px; }
/* withdraw */
.phone .n2-amt { display: flex; flex-direction: column; align-items: center; padding: 20px 0 14px; }
.phone .n2-amt small { color: var(--hd-fg-muted); }
.phone .n2-amt b { font-family: var(--font-brand); font-size: 56px; line-height: 64px; font-weight: 700; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; margin-top: 2px; }
.phone .n2-amt p { margin: 4px 0 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n2-amt p .num { color: var(--hd-fg); font-weight: 600; }
.phone .n2-keys { margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); }
.phone .n2-keys span { height: 52px; display: flex; align-items: center; justify-content: center; font-family: var(--font-ui); font-size: 26px; font-weight: 500; color: var(--hd-fg); }
.phone .n2-keys span .ic { width: 22px; height: 22px; color: var(--hd-fg-muted); }
/* barter */
.phone .n2-offer { display: grid; grid-template-columns: auto 1fr 1fr; padding: 14px 16px; gap: 12px; }
.phone .n2-offer > div { display: flex; flex-direction: column; gap: 2px; }
.phone .n2-offer b { white-space: nowrap; font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 700; letter-spacing: -0.02em; }
.phone .n2-vj { padding: 14px 16px; display: flex; flex-direction: column; }
.phone .n2-vs { position: relative; display: flex; gap: 14px; padding-bottom: 14px; }
.phone .n2-vs:last-child { padding-bottom: 0; }
.phone .n2-vs i { width: 20px; height: 20px; flex: none; border-radius: 50%; border: 1.5px solid var(--hd-edge-strong, var(--hd-edge)); background: var(--hd-surface); display: flex; align-items: center; justify-content: center; color: #fff; position: relative; z-index: 1; margin-top: 0; }
.phone .n2-vs:not(:last-child)::before { content: ""; position: absolute; left: 9px; top: 20px; bottom: 0; width: 2px; background: var(--hd-edge); }
.phone .n2-vs.done:not(:last-child)::before { background: var(--hd-accent); }
.phone .n2-vs.done i { background: var(--hd-accent); border-color: var(--hd-accent); }
.phone .n2-vs.now i { border-color: var(--hd-accent); border-width: 5px; }
.phone .n2-vs .tx { display: flex; flex-direction: column; min-width: 0; }
.phone .n2-vs:not(.done):not(.now) b { color: var(--hd-fg-muted); font-weight: 560; }
"""
