# m6 layer (rollout of the v5 white language, 2026-11-26): mediator pages on the w5-* classes
XM6 = """
.phone .m6-pg { padding-top: 0; }
.phone .m6-pg .w5-h1 { margin-top: 6px; }
.phone .m6-pg .w5-sh { margin: 22px 0 10px; }
.phone .m6-pg .warn { color: var(--hd-warning-strong); font-weight: 600; font-style: normal; }
.phone .w5-row > img.m6-pa { border-radius: 50%; }
.phone .w5-row .w5-lk { margin-left: auto; }
.phone .m6-pg .w5-tabs { margin-bottom: 14px; }
.phone .m6-pg .w5-feat { margin-top: 4px; }
/* money block: white, quiet breakdown */
.phone .m6-pg .m6-money, .phone .m6-pg .m6-score { margin-top: 14px; padding-top: 0; border-top: 0; }
.phone .m6-mh { display: flex; align-items: baseline; justify-content: space-between; }
.phone .m6-money > b { margin-top: 0; }
.phone .m6-cta { margin-top: 16px; }
.phone .m6-pg .w5-sum p { line-height: 18px; }
.phone .m6-to { display: flex; align-items: center; gap: 8px; margin-top: 14px; font-size: 14px; }
.phone .m6-to span { flex: 1; color: var(--hd-fg-muted); }
.phone .m6-to .bankl { width: 18px; height: 18px; border-radius: 4px; }
.phone .m6-amt { font-size: 16px; font-weight: 650; color: var(--hd-fg); flex: none; }
/* today: the one action card */
.phone .m6-act { border: 1px solid var(--hd-edge); border-radius: 16px; background: var(--hd-surface); padding: 12px 12px 12px; display: flex; flex-direction: column; gap: 12px; margin-bottom: 10px; }
.phone .m6-act > * { flex: none; }
.phone .m6-act .w5-row.m6-nb { border: 0; padding: 0; margin: 0; }
.phone .m6-act .w5-row > img { width: 52px; height: 52px; }
.phone .m6-pg .w5-row + .w5-row { margin-top: 10px; }
/* store */
.phone .m6-store { border: 1px solid var(--hd-edge); border-radius: 16px; background: var(--hd-surface); padding: 14px; display: flex; flex-direction: column; gap: 12px; margin-bottom: 18px; }
.phone .m6-store > * { flex: none; }
.phone .m6-sl { display: flex; align-items: center; gap: 12px; }
.phone .m6-sl .tx { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 1px; }
.phone .m6-sl b { font-size: 15.5px; font-weight: 600; line-height: 20px; } .phone .m6-sl small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .m6-lnk { color: var(--hd-fg-muted); display: flex; }
.phone .m6-sw { display: flex; align-items: center; justify-content: space-between; font-size: 15px; font-weight: 500; padding-top: 12px; border-top: 1px solid var(--hd-edge); }
/* enrollment */
.phone .m6-ct { display: flex; gap: 16px; margin-left: auto; color: var(--hd-fg); }
.phone .m6-pg .w5-prod { margin-top: 2px; }
.phone .m6-pg .w5-prod > img { width: 48px; height: 48px; }
.phone .m6-pg .w5-prod > div { flex: none; }
.phone .m6-pg .w5-steps { margin-top: 18px; }
.phone .m6-pg .w5-sum { margin-top: 20px; }
.phone .m6-score > b { margin-top: 0; }
.phone .m6-score p { margin: 2px 0 0; }
.phone .m6-score p .num { color: var(--hd-fg); font-weight: 600; }
.phone .m6-score dl { margin-top: 14px; }
/* sheets */
.phone .m6-sumsheet { margin-top: 8px; padding-top: 14px; }
.phone .m6-sumsheet > b { font-size: 34px; line-height: 40px; }
.phone .m6-for { margin: 4px 0 0; font-size: 14px; color: var(--hd-fg-muted); }
.phone .md-sheet .w5-row { padding: 10px 14px 10px 10px; }
.phone .md-sheet .w5-row + .w5-row { margin-top: 0; }
.phone .md-sheet .w5-row small { white-space: normal; }
.phone .md-sheet .w5-row > img { width: 48px; height: 48px; }
.phone .m6-sel { border-color: var(--hd-accent); box-shadow: inset 0 0 0 1px var(--hd-accent); }
.phone .m6-sel > .ic { color: var(--hd-accent); }
.phone .m6-no { opacity: .6; }
/* dock: calm, one cobalt disc for New */
.phone .m6-dock { height: 64px; flex: none; display: flex; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .m6-di { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 8px; gap: 3px; font-size: 11px; font-weight: 560; color: var(--hd-fg-subtle); }
.phone .m6-di.on { color: var(--hd-link); }
.phone .m6-new i { width: 44px; height: 32px; border-radius: 16px; background: var(--hd-accent); display: grid; place-items: center; margin-bottom: 1px; }
.phone .m6-new i .ic { color: #fff; }
.phone .m6-new { padding-bottom: 8px; }
.phone .m6-new { color: var(--hd-fg-subtle); }
.phone .m6-new i { height: 30px; width: 46px; border-radius: 15px; margin-bottom: 0; }
/* m7: mediator on the approved Home structure — canvas page, white cards, quiet inline actions */
.phone .scr:has(.m7), .phone .scr:has(.m7) .xm1-bar { background: var(--hd-canvas) !important; }
.phone .m7-date { margin: 2px 0 0; font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .m7 .m7-date + .w5-h1 { margin-top: 0; }
.phone .m7-money { margin-top: 16px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 20px; padding: 18px 18px 0; display: flex; flex-direction: column; }
.phone .m7-money > * { flex: none; }
.phone .m7-money > small { font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .m7-money > b { font-family: var(--font-brand); font-size: 40px; line-height: 46px; font-weight: 700; letter-spacing: -0.03em; margin-top: 2px; }
.phone .m7-money > p { margin: 4px 0 16px; font-size: 13.5px; line-height: 19px; color: var(--hd-fg-muted); display: flex; align-items: center; flex-wrap: wrap; gap: 0 4px; }
.phone .m7-money > p b { color: var(--hd-fg); font-weight: 600; }
.phone .m7-ft { margin: 0 -18px; padding: 12px 18px; border-top: 1px solid var(--hd-edge); display: flex; align-items: center; gap: 10px; font-size: 14px; min-height: 52px; box-sizing: border-box; }
.phone .m7-ft > span { flex: 1; color: var(--hd-fg); font-weight: 500; }
.phone .m7-ft .bankl { width: 20px; height: 20px; border-radius: 5px; }
.phone .m7-ft .btn.sm, .phone .m7-due .btn.sm { height: 34px !important; padding: 0 14px; font-size: 14px; flex: none; }
.phone .m7 .w5-row { background: var(--hd-surface); }
.phone .m7 .w5-sh { margin: 24px 0 10px; }
.phone .m7-store { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 12px 14px; display: flex; flex-direction: column; gap: 12px; margin-top: 14px; }
.phone .m7-store > * { flex: none; }
.phone .m7-store .m6-sl small { font-size: 12.5px; }
.phone .m7-store .btn.sm { height: 34px !important; padding: 0 14px; flex: none; }
.phone .m7-mute b, .phone .m7-mute > img { opacity: .55; }
.phone .m7 .w5-tabs { margin-bottom: 0; }
/* trust score */
.phone .m7-score { padding-bottom: 16px; }
.phone .m7-score > p .ic { margin-left: 2px; }
.phone .m7-bar { display: flex; gap: 3px; height: 8px; border-radius: 4px; overflow: hidden; margin-top: 2px; }
.phone .m7-bar i { display: block; height: 100%; }
.phone .m7-leg { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 12px; margin-top: 12px; font-size: 13px; color: var(--hd-fg-muted); }
.phone .m7-leg span { display: flex; align-items: center; gap: 6px; }
.phone .m7-leg i { width: 8px; height: 8px; border-radius: 2px; flex: none; }
.phone .m7-leg b { margin-left: auto; color: var(--hd-fg); font-weight: 600; }
.phone .m7-money:not(.m7-score) > p { display: block; }
.phone .m7-date { margin-top: 8px; }
.phone .m7-ft > span.m7-hint { font-weight: 400; color: var(--hd-fg-muted); font-size: 13px; line-height: 17px; }
.phone .m7 .w5-steps { margin-top: 20px; }
.phone .m7 .w5-prod + .w5-h1 { margin-top: 18px; }
.phone .m7 .w5-row small img { width: 13px !important; height: 13px !important; border-radius: 3px; vertical-align: -2px; }
.phone .m7 .warn { color: var(--hd-warning-strong); font-weight: 600; font-style: normal; }
"""
