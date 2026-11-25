# Screen layer (xn1). Prefix every class to avoid clashes.
XN1 = """
.phone .scr:has(.n1-ob) { background: var(--hd-surface); }
.phone .scr:has(.n1-br), .phone .scr:has(.n1-br), .phone .scr:has(.n1-en) { background: var(--hd-canvas); }
.phone .n1-ob, .phone .n1-br, .phone .n1-en { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; background: var(--hd-canvas); }
.phone .n1-ob { background: var(--hd-surface) !important; }
.phone .n1-top { height: 44px; flex: none; display: flex; align-items: center; padding: 0 20px; color: var(--hd-fg); }
.phone .n1-top .ic { width: 22px; height: 22px; }
.phone .n1-top2 { justify-content: space-between; height: 48px; padding-top: 2px; }
.phone .n1-h2, .phone .n1-h { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; color: var(--hd-fg); }
/* onboarding */
.phone .n1-prog { display: flex; gap: 6px; margin: 4px 20px 0; }
.phone .n1-prog i { flex: 1; height: 3px; border-radius: 2px; background: var(--hd-edge); }
.phone .n1-prog i.on { background: var(--hd-accent); }
.phone .n1-step { margin: 10px 20px 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n1-ob .n1-h { margin: 4px 20px 0; }
.phone .n1-form { display: flex; flex-direction: column; gap: 20px; padding: 28px 20px 0; flex: 1; }
.phone .n1-f { display: flex; flex-direction: column; gap: 8px; }
.phone .n1-f label { font-size: 13.5px; line-height: 18px; font-weight: 600; color: var(--hd-fg); }
.phone .n1-in { height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 15px; color: var(--hd-fg); }
.phone .n1-in .ic { color: var(--hd-fg-subtle); }
.phone .n1-opts { display: flex; gap: 8px; }
.phone .n1-opt { flex: 1; height: 44px; display: flex; align-items: center; justify-content: center; border-radius: 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 15px; color: var(--hd-fg-muted); }
.phone .n1-opt.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-accent-strong, var(--hd-link)); font-weight: 600; }
.phone .n1-bar { flex: none; padding: 12px 20px 34px; background: var(--hd-surface); }
.phone .n1-bar .btn { height: 48px; }
/* browse */
.phone .n1-chips, .phone .n1-flts { display: flex; gap: 8px; padding: 0 16px; flex: none; }
.phone .n1-chip { height: 36px; padding: 0 14px; display: inline-flex; align-items: center; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); }
.phone .n1-chip.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-accent-strong, var(--hd-link)); font-weight: 600; }
.phone .n1-flts { margin-top: 8px; }
.phone .n1-flt { height: 36px; padding: 0 8px 0 12px; display: inline-flex; align-items: center; gap: 2px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg); }
.phone .n1-flt .ic { color: var(--hd-fg-subtle); }
.phone .n1-sort { display: flex; align-items: center; justify-content: space-between; padding: 14px 20px 8px; font-size: 13px; color: var(--hd-fg-muted); flex: none; }
.phone .n1-sb { display: inline-flex; align-items: center; gap: 4px; color: var(--hd-fg); font-weight: 600; }
.phone .n1-sb .ic { color: var(--hd-fg-subtle); }
.phone .n1-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 0 16px 12px; flex: 1; min-height: 0; overflow: hidden; align-content: start; }
.phone .n1-cc { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; }
.phone .n1-ph img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; display: block; }
.phone .n1-bd { padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.phone .n1-sr { display: flex; align-items: center; gap: 5px; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); }
.phone .n1-t { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .n1-pay { margin: 0; font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .n1-bn { font-size: 13px; line-height: 18px; font-weight: 600; color: var(--hd-success-strong); }
.phone .n1-ft { font-size: 13px; line-height: 18px; color: var(--hd-fg-subtle); }
.phone .n1-jn { display: inline-flex; align-items: center; gap: 4px; font-size: 13px; line-height: 18px; font-weight: 600; color: var(--hd-success-strong); }
/* enrollments */
.phone .n1-list { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 8px; padding: 0 16px; }
.phone .n1-sh { display: flex; align-items: baseline; justify-content: space-between; margin: 4px 4px 0; }
.phone .n1-sh h2 { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 0; }
.phone .n1-sh span { font-size: 13px; color: var(--hd-fg-subtle); }
.phone .n1-row { display: flex; align-items: center; gap: 12px; min-height: 52px; padding: 5px 14px 5px 6px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; flex: none; }
.phone .n1-row img { width: 40px; height: 40px; border-radius: 10px; object-fit: cover; flex: none; }
.phone .n1-row .tx { display: flex; flex-direction: column; gap: 1px; min-width: 0; }
.phone .n1-row b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .n1-row small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .n1-row small em { font-style: normal; font-weight: 600; color: var(--hd-fg); }
.phone .n1-row small.warn em { color: var(--hd-warning-strong); }
"""
