# Layer for scr_n2.py: page layout only. Components come from the kit (dm-*, cv-wal, eb-empty2, row, badge), re-scoped in xn1.
XN2 = """
.phone .n2 { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 4px 16px 12px; background: var(--hd-canvas); }
.phone .n2 > * { flex: none; }
.phone .scr:has(.n2) { background: var(--hd-canvas); }
.phone .n2-bar .n2-bt { flex: 1; text-align: center; font-size: 16px; font-weight: 600; margin-right: 22px; }
.phone .n2-bar { gap: 8px; }
.phone .n2-sh { padding: 0 4px; margin: 6px 0 -4px; }
.phone .n2-sh h2 { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 0; }
.phone .n2-title { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 4px 4px 0; }
.phone .n2-ink { margin: 0; }
.phone .n2 .dm-jr { padding: 16px 12px 14px; }
.phone .n2-sbw { flex: none; padding: 10px 16px 6px; background: var(--hd-surface); border-top: 1px solid var(--hd-edge); }
.phone .n2-sbw .dm-sb { box-shadow: none !important; border: 0 !important; background: transparent !important; padding: 0 !important; }
.phone .n2-lk { font-size: 15px; font-weight: 600; color: var(--hd-link); flex: none; }
.phone .n2-v { font-size: 17px; font-weight: 600; }
.phone .n2-wd .card.eb-empty2 { margin: 0; }
.phone .n2-list { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; }
.phone .n2-list .row { border: 0 !important; border-radius: 0 !important; box-shadow: none !important; background: transparent !important; min-height: 52px; }
.phone .n2-list .row + .row { border-top: 1px solid var(--hd-edge) !important; }
.phone .n2-sr > .ic:first-child { color: var(--hd-fg-muted); flex: none; }
.phone .n2-sr > .ic:last-child { color: var(--hd-fg-subtle); flex: none; }
.phone .n2 small.warn { color: var(--hd-warning-strong); }
.phone .n2-me .lead { width: 48px; height: 48px; }
.phone .n2-moment { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0 16px; }
.phone .n2-moment img { width: 116px; height: 116px; object-fit: contain; display: block; }
.phone .n2-moment h1 { font-family: var(--font-brand); font-size: 22px; line-height: 26px; font-weight: 700; letter-spacing: -0.02em; margin: 2px 0 0; }
.phone .n2-moment p { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
"""

XN2 += """
.phone .n2-money { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 18px; padding: 18px 20px 20px; display: flex; flex-direction: column; gap: 4px; margin-top: 4px; }
.phone .n2-money small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n2-money b { font-family: var(--font-brand); font-size: 38px; line-height: 44px; font-weight: 700; letter-spacing: -0.025em; color: var(--hd-fg); }
.phone .n2-money p { margin: 2px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .dm-ns .n2-pn { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
"""
