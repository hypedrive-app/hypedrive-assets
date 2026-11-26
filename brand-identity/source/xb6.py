# b6 layer (rollout of the v5 white language, 2026-11-26): brand desktop pages 2-7
XB6 = """
/* kit underline tabs on desktop pages: coloured solid icons + grey count */
.b6-tabs { margin: 4px 0 0; gap: 28px; }
.b6-tabs > span { gap: 8px; font-size: 15px; font-weight: 500; padding: 12px 0; }
.b6-tabs > span.on { font-weight: 600; }
.b6-tabs .tc { font-size: 13.5px; font-weight: 500; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.b6-tabs .ic { flex: none; }
.b6-wt { margin: 0 0 14px; gap: 22px; }

/* 2 campaigns: separate calm row cards */
.v3k .v3-tool { margin: 16px 0 0; } .v3k .v3-tool .input { height: 40px !important; min-height: 0 !important; border-radius: 10px !important; width: 360px; } .v3k .v3-tool .chip { height: 40px; }
.b6-list { display: flex; flex-direction: column; gap: 10px; margin-top: 14px; }
.b6-list > * { flex: none; }
.b6-crow { display: grid; grid-template-columns: 64px minmax(0, 1fr) 230px 120px 132px; column-gap: 20px; align-items: center; height: 88px; box-sizing: border-box; padding: 0 20px 0 12px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; }
.b6-th { width: 64px; height: 64px; border-radius: 12px; object-fit: cover; display: block; }
.b6-tx { display: flex; flex-direction: column; gap: 3px; min-width: 0; }
.b6-tx b { font-size: 15.5px; line-height: 22px; font-weight: 600; letter-spacing: -.005em; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.b6-tx small { display: flex; align-items: center; gap: 10px; font-size: 13.5px; line-height: 18px; color: var(--hd-fg-muted); }
.b6-st { display: inline-flex; align-items: center; gap: 6px; color: var(--hd-fg); font-weight: 500; }
.b6-st img { width: 14px; height: 14px; border-radius: 3px; }
.b6-cr { display: flex; flex-direction: column; gap: 7px; font-size: 13.5px; color: var(--hd-fg-muted); min-width: 0; }
.b6-cr b { color: var(--hd-fg); font-weight: 600; }
.b6-cr .bar2 { height: 4px; border-radius: 4px; background: var(--hd-track); overflow: hidden; }
.b6-cr .bar2 i { display: block; height: 100%; background: var(--hd-chart); border-radius: 4px; }
.b6-sp { display: flex; flex-direction: column; align-items: flex-end; gap: 1px; } .b6-sp b { font-size: 15.5px; line-height: 22px; font-weight: 600; font-variant-numeric: tabular-nums; color: var(--hd-fg); } .b6-sp small { font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); }
.b6-state { display: flex; justify-content: flex-end; font-size: 13.5px; color: var(--hd-fg-muted); }

/* 3 detail: rail starts level with the first section, money card has a quiet text action */
.v3k .v3-side { margin-top: 0; }
.b6-lk { margin-top: 14px; font-size: 14px; font-weight: 600; color: var(--hd-link); }

/* 7 team: one column grid for roles and status/actions */
.v3-rc { flex: none; }
.v3-seen, .v3-acts { width: 170px; flex: none; justify-content: flex-end; }
.sb .sb-lg-d { display: none; }
[data-theme="dark"] .sb .sb-lg-l { display: none; } [data-theme="dark"] .sb .sb-lg-d { display: block; }
/* b7: campaigns as the approved Home photo cards */
.b7 .b7-bar { display: flex; align-items: flex-end; gap: 16px; border-bottom: 1px solid var(--hd-border); }
.b7 .b7-bar .tabs { border-bottom: 0; flex: 1; }
.b7 .b7-tools { display: flex; align-items: center; gap: 8px; padding-bottom: 8px; }
.b7 .b7-sh { margin-top: 26px; margin-bottom: 12px; display: flex; align-items: baseline; gap: 8px; }
.b7 .b7-sh h2 { margin: 0; }
.b7 em.b7-n { font-style: normal; font-size: 14px; color: var(--hd-fg-subtle); font-weight: 500; }
.b7-c .b7-ph { position: relative; height: 168px; background: var(--hd-bg-subtle); }
.b7-c .b7-ph > img { width: 100%; height: 168px; object-fit: cover; display: block; }
.b7-c .b7-tag { position: absolute; left: 12px; top: 12px; height: 28px; padding: 0 10px; border-radius: 14px; background: rgba(255,255,255,.96); color: #121417; font-size: 13px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 1px 2px rgba(0,0,0,.08); }
.b7-c .b7-noph { height: 168px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; color: var(--hd-fg-subtle); font-size: 13px; }
.b7-c .b7-nobar { visibility: hidden; }
.b7-c.b7-end .b7-ph > img { filter: grayscale(1); opacity: .75; }
.b7-c .b small:not(.m) span:first-child { color: var(--hd-fg); font-weight: 500; }
.b7-c .b small.m:empty { display: none; }
.b7-c .b7-lk { font-style: normal; color: var(--hd-link); font-weight: 600; }
.b7-c .b7-nobar { display: none; }
.b7-c .b7-nobar + small { margin-top: 12px; }
.b7 .bd2-sh.b7-sh { justify-content: flex-start; }
.b7-c.b7-end .bar i { background: var(--hd-fg-subtle); }
"""
