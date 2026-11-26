# Home (creator), by the business-logic spec. Calm language: separate row cards, one signal per state, 15/600 titles.
XH = """
.phone .hm { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 4px 16px 16px; background: var(--hd-canvas); }
.phone .scr:has(.hm) { background: var(--hd-canvas); }
.phone .hm-h { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 4px 4px 0; }
.phone .hm-wal, .phone .hm-row, .phone .hm-pick { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; }
.phone .hm-wal { padding: 16px 16px 0; display: flex; flex-direction: column; }
.phone .hm-wal small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .hm-wal > b { font-family: var(--font-brand); font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; color: var(--hd-fg); margin-top: 2px; }
.phone .hm-wal p { margin: 2px 0 14px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .hm-wal p .num { color: var(--hd-fg); font-weight: 600; }
.phone .hm-wal .ft { display: flex; align-items: center; gap: 8px; margin: 0 -16px; padding: 12px 16px; border-top: 1px solid var(--hd-edge); color: inherit; text-decoration: none; font-size: 14px; line-height: 20px; }
.phone .hm-wal .ft span { flex: 1; color: var(--hd-fg); }
.phone .hm-wal .ft em { font-style: normal; font-weight: 600; color: var(--hd-link); }
.phone .hm-sh { display: flex; align-items: baseline; justify-content: space-between; margin: 8px 4px -2px; }
.phone .hm-sh h2 { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 0; }
.phone .hm-sh > span { font-size: 13px; color: var(--hd-fg-subtle); }
.phone .hm-row { display: flex; align-items: center; gap: 12px; min-height: 68px; padding: 10px 14px 10px 10px; }
.phone .hm-row img { width: 48px; height: 48px; border-radius: 10px; object-fit: cover; flex: none; }
.phone .hm-row .tx { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1; }
.phone .hm-row b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .hm-row small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .hm-row small.warn { color: var(--hd-warning-strong); }
.phone .hm-row > .ic { color: var(--hd-fg-subtle); flex: none; }
.phone .hm-picks { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.phone .hm-pick { overflow: hidden; display: flex; flex-direction: column; }
.phone .hm-pick img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; display: block; }
.phone .hm-pick .bd { padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 2px; }
.phone .hm-pick .sr { display: flex; align-items: center; gap: 5px; font-size: 12.5px; color: var(--hd-fg-muted); }
.phone .hm-pick b { font-size: 15px; line-height: 20px; font-weight: 600; }
.phone .hm-pick p { margin: 0; display: flex; gap: 6px; align-items: baseline; font-size: 14px; font-weight: 600; color: var(--hd-fg); }
.phone .hm-pick p em { font-style: normal; font-size: 12.5px; font-weight: 600; color: var(--hd-success-strong); }
.phone .hm-pick small { font-size: 12.5px; color: var(--hd-fg-subtle); }
"""
