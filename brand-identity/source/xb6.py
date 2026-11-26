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
/* b8: campaign detail on the Home structure */
.b8 { display: flex; flex-direction: column; gap: 16px; }
.b8 > * { flex: none; }
.b8-head { display: flex; align-items: center; gap: 18px; margin-bottom: 4px; }
.b8-head > img { width: 72px; height: 72px; border-radius: 16px; object-fit: cover; flex: none; }
.b8-head .t { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.b8-head .b1-h1 { margin: 0; }
.b8-head .b1-sub { margin: 0; }
.b8-meta { display: flex; align-items: center; gap: 6px; font-size: 13px; color: var(--hd-fg-muted); }
.b8-meta img { width: 14px; height: 14px; border-radius: 4px; }
.b8-k { gap: 16px !important; }
.b8-r2 { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; align-items: stretch; }
.b8-r3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; align-items: stretch; }
.b8 .panel { margin: 0; }
.b8 .phd { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px; }
.b8 .phd b { font-size: 15px; font-weight: 600; }
.b8-posts .v3-posts { grid-template-columns: repeat(4, 1fr); }
.b8-posts .v3-post .th { height: 172px; }
.b8-r2 > .mn-card { margin: 0; height: 100%; box-sizing: border-box; }
.b8-task { display: flex; align-items: center; gap: 12px; padding: 10px 0; border-top: 1px solid var(--hd-edge); }
.b8-task:first-of-type { border-top: 0; padding-top: 0; }
.b8-task .x-tile { width: 36px; height: 36px; flex: none; }
.b8-task b { display: block; font-size: 14px; font-weight: 600; } .b8-task small { font-size: 12.5px; color: var(--hd-fg-muted); }
.b8 .b8-in { border: 0 !important; padding: 0 !important; background: none !important; box-shadow: none !important; margin: 0 !important; }
.b8 .v3-facts.b8-in > div { padding: 7px 0; font-size: 13.5px; }
.b8 .panel { padding: 20px 22px; }
.b8 .b8-k .panel { padding: 16px 18px; }
.b8-cost { display: flex; }
.b8-cost > .mn-card { flex: 1; margin: 0; padding: 20px 22px; border-radius: 16px; display: flex; flex-direction: column; }
.b8-cost .mn-lns { margin-top: 14px; }
.b8 .phd { padding: 0 !important; border: 0 !important; min-height: 0 !important; }
.b8-cn { margin: auto 0 0; padding-top: 14px; font-size: 13px; line-height: 19px; color: var(--hd-fg-muted); }
.b8 .stat .vz:empty { display: none; }
.b8 .phd + .b8-task { border-top: 1px solid var(--hd-edge); padding-top: 10px; }
.b8 .b8-task:first-of-type { border-top: 1px solid var(--hd-edge); padding-top: 10px; }
.b8-wait .vz { display: flex; align-items: center; gap: 10px; margin-top: 10px; }
.b8-avs { display: flex; } .b8-avs img, .b8-avs i { width: 26px; height: 26px; border-radius: 50%; object-fit: cover; border: 2px solid var(--hd-surface-raised); margin-left: -6px; flex: none; }
.b8-avs img:first-child { margin-left: 0; }
.b8-avs i { font-style: normal; display: grid; place-items: center; background: var(--hd-bg-subtle); font-size: 11px; font-weight: 600; color: var(--hd-fg-muted); }
.b8-wait small { font-size: 12.5px; color: var(--hd-fg-muted); }
.b8 .b8-wait .vz { flex-direction: row !important; justify-content: flex-start !important; align-items: center !important; text-align: left; margin-top: auto; padding-top: 12px; }
.b8 .b8-wait { display: flex; flex-direction: column; }
.v3-shot { overflow: hidden; }
.v3-shots:has(.v3-quote) { align-items: flex-start; }
.v3-shots .v3-quote { align-self: flex-start; padding-top: 8px; }
.b7-c .b7-ph { overflow: hidden; }
"""
