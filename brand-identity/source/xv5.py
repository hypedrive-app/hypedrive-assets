# Layer for scr_v5.py: white pages, inline headers, imagery first, cards only for list items.
XV5 = """
.phone .scr:has(.w5), .phone .scr:has(.w5) .xm1-bar { background: var(--hd-surface) !important; }
.phone .w5 { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; padding: 4px 16px 20px; }
.phone .w5 > * { flex: none; }
.phone .w5-bar { display: flex; align-items: center; justify-content: space-between; padding: 10px 16px 6px; }
.phone .w5-bar .l, .phone .w5-bar .r { display: flex; align-items: center; gap: 16px; color: var(--hd-fg); }
.phone .w5-step { font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); }
.phone .w5-h1 { font-family: var(--font-brand); font-size: 30px; line-height: 36px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 8px 0 0; color: var(--hd-fg); }
.phone .w5-h1.w5-inbar { margin: 0; }
.phone .w5-lead { margin: 6px 0 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); }
.phone .w5-sh { display: flex; align-items: baseline; justify-content: space-between; margin: 26px 0 12px; }
.phone .w5-sh h2 { font-family: var(--font-brand); font-size: 19px; line-height: 24px; font-weight: 650; margin: 0; letter-spacing: -0.01em; }
.phone .w5-sh span { font-size: 13px; color: var(--hd-fg-muted); }
/* rows: separate cards on white */
.phone .w5-row { display: flex; align-items: center; gap: 14px; padding: 12px 14px 12px 12px; border: 1px solid var(--hd-edge); border-radius: 16px; background: var(--hd-surface); }
.phone .w5-row + .w5-row { margin-top: 10px; }
.phone .w5-row > img { width: 52px; height: 52px; border-radius: 12px; object-fit: cover; flex: none; }
.phone .w5-row .tx { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; }
.phone .w5-row b { font-size: 15.5px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .w5-row small { font-size: 13.5px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .w5-row small.warn { color: var(--hd-warning-strong); font-weight: 600; }
.phone .w5-row > .ic { color: var(--hd-fg-subtle); flex: none; }
.phone .w5-ti { width: 44px; height: 44px; flex: none; }
.phone .w5-ti img { width: 22px !important; height: 22px !important; }
.phone .w5-lk { font-style: normal; font-weight: 600; font-size: 15px; color: var(--hd-link); flex: none; }
/* bottom bar */
.phone .w5-bb { flex: none; padding: 12px 16px 10px; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .w5-bb p { margin: 0 0 10px; text-align: center; font-size: 13.5px; color: var(--hd-fg-muted); }
/* onboarding */
.phone .w5-ob .w5-two { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 28px; }
.phone .w5-f { display: flex; flex-direction: column; gap: 8px; margin-top: 18px; }
.phone .w5-two .w5-f { margin-top: 0; }
.phone .w5-f > span { font-size: 13.5px; font-weight: 600; color: var(--hd-fg); }
.phone .w5-in { height: 50px; border-radius: 14px; border: 1px solid var(--hd-border-strong); padding: 0 14px; display: flex; align-items: center; justify-content: space-between; font-size: 16px; color: var(--hd-fg); }
.phone .w5-ic { font-style: normal; color: var(--hd-fg-muted); display: inline-flex; }
.phone .w5-seg { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.phone .w5-seg span { height: 46px; border-radius: 14px; border: 1px solid var(--hd-border-strong); display: grid; place-items: center; font-size: 15px; font-weight: 600; color: var(--hd-fg); }
.phone .w5-seg span.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-info-strong); }
/* browse */
.phone .w5-chips { display: flex; gap: 8px; margin: 6px -16px 0; padding: 0 16px; overflow: hidden; }
.phone .w5-chips .chip { height: 36px; padding: 0 14px; border-radius: 18px; font-size: 14px; flex: none; display: inline-flex; align-items: center; gap: 6px; }
.phone .w5-feat { position: relative; height: 220px; border-radius: 22px; overflow: hidden; margin-top: 16px; }
.phone .w5-feat > img { width: 100%; height: 100%; object-fit: cover; display: block; }
.phone .w5-feat::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10,12,16,0) 30%, rgba(10,12,16,.35) 55%, rgba(10,12,16,.82) 100%); }
.phone .w5-tag { position: absolute; z-index: 1; left: 14px; top: 14px; height: 28px; padding: 0 10px; border-radius: 14px; background: rgba(255,255,255,.95); color: #121417; font-size: 13px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
.phone .w5-tag img, .phone .w5-sr img { width: 13px !important; height: 13px !important; border-radius: 3px; }
.phone .w5-ft { position: absolute; z-index: 1; left: 18px; right: 18px; bottom: 16px; color: #fff; display: flex; flex-direction: column; }
.phone .w5-ft small { font-size: 13px; font-weight: 600; color: rgba(255,255,255,.92); }
.phone .w5-ft b { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.02em; }
.phone .w5-ft span { font-size: 13.5px; color: rgba(255,255,255,.9); }
.phone .w5-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.phone .w5-tile { display: flex; flex-direction: column; gap: 3px; }
.phone .w5-tp { height: 186px; border-radius: 18px; overflow: hidden; background: var(--hd-bg-subtle); margin-bottom: 8px; }
.phone .w5-tp img { width: 100%; height: 100%; object-fit: cover; display: block; }
.phone .w5-sr { display: flex; align-items: center; gap: 5px; font-size: 12.5px; color: var(--hd-fg-muted); }
.phone .w5-tn { font-size: 15.5px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .w5-back { font-size: 15px; font-weight: 700; color: var(--hd-fg); display: flex; gap: 6px; align-items: baseline; }
.phone .w5-back em { font-style: normal; font-size: 13px; font-weight: 600; color: var(--hd-success-strong); }
.phone .w5-state { font-size: 13px; color: var(--hd-fg-muted); margin-top: 2px; }
.phone .w5-state.ok { color: var(--hd-link); font-weight: 600; }
/* enrollment detail */
.phone .w5-prod { display: flex; align-items: center; gap: 12px; margin-top: 4px; }
.phone .w5-prod img { width: 48px; height: 48px; border-radius: 12px; object-fit: cover; }
.phone .w5-prod b { display: block; font-size: 15px; font-weight: 600; } .phone .w5-prod small { display: flex; align-items: center; gap: 5px; font-size: 13px; color: var(--hd-fg-muted); }
.phone .w5-prod small img { width: 13px !important; height: 13px !important; border-radius: 3px; }
.phone .w5-dt .w5-h1 { margin-top: 22px; }
.phone .w5-steps { display: flex; margin-top: 22px; }
.phone .w5-st { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 8px; position: relative; font-size: 12.5px; color: var(--hd-fg-subtle); }
.phone .w5-st::before { content: ""; position: absolute; top: 11.5px; left: -50%; width: 100%; height: 1.5px; background: var(--hd-control); z-index: 0; }
.phone .w5-st:first-child::before { display: none; }
.phone .w5-st.done::before, .phone .w5-st.now::before { background: var(--hd-accent); }
.phone .w5-st i { position: relative; z-index: 1; width: 24px; height: 24px; border-radius: 50%; background: var(--hd-surface); box-shadow: inset 0 0 0 2px var(--hd-control); display: grid; place-items: center; }
.phone .w5-st.done i { background: var(--hd-accent); box-shadow: none; }
.phone .w5-st.now i { box-shadow: inset 0 0 0 2px var(--hd-accent); }
.phone .w5-st.now i::after { content: ""; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-accent); }
.phone .w5-st.done span, .phone .w5-st.now span { color: var(--hd-fg); } .phone .w5-st.now span { font-weight: 600; }
.phone .w5-money { margin-top: 26px; padding-top: 20px; border-top: 1px solid var(--hd-edge); display: flex; flex-direction: column; }
.phone .w5-money small { font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .w5-money b { font-family: var(--font-brand); font-size: 36px; line-height: 42px; font-weight: 700; letter-spacing: -0.025em; }
.phone .w5-money p { margin: 2px 0 0; font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .w5-prog { display: flex; gap: 6px; } .phone .w5-prog i { width: 28px; height: 4px; border-radius: 4px; background: var(--hd-control); } .phone .w5-prog i.on { background: var(--hd-accent); }
.phone .w5-ob .w5-h1 { margin-top: 14px; }
.phone .w5-task > .ic { color: var(--hd-fg-subtle); flex: none; }
/* refine 3 */
.phone .w5-en .w5-sh:first-child { margin-top: 10px; }
.phone .w5-sh span { font-variant-numeric: tabular-nums; }
.phone .w5-hint { margin: 8px 0 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .w5-sum { margin-top: 24px; padding-top: 18px; border-top: 1px solid var(--hd-edge); display: flex; flex-direction: column; }
.phone .w5-sum small { font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .w5-sum > b { font-family: var(--font-brand); font-size: 36px; line-height: 42px; font-weight: 700; letter-spacing: -0.025em; font-variant-numeric: tabular-nums; }
.phone .w5-sum dl { margin: 12px 0 0; display: grid; grid-template-columns: 1fr auto; row-gap: 8px; font-size: 14px; line-height: 20px; }
.phone .w5-sum dt { color: var(--hd-fg-muted); } .phone .w5-sum dd { margin: 0; color: var(--hd-fg); font-variant-numeric: tabular-nums; text-align: right; }
.phone .w5-sum dd.in { color: var(--hd-success-strong); font-weight: 600; }
.phone .w5-sum p { margin: 12px 0 0; font-size: 13px; color: var(--hd-fg-muted); }
.phone .w5-tabs { margin: 2px -16px 0; padding: 0 16px; gap: 20px; overflow: hidden; flex-wrap: nowrap; }
.phone .w5-tabs > span { flex: none; white-space: nowrap; font-size: 14.5px; font-weight: 500; gap: 6px; }
.phone .w5-tabs > span.on { font-weight: 600; }
.phone .w5-tabs .tc { font-size: 13px; font-weight: 500; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }
.phone .w5-dt .w5-h1 { margin-top: 16px; }
.phone .w5-dt .w5-steps { margin-top: 16px; }
.phone .w5-dt .w5-sh { margin: 20px 0 10px; }
.phone .w5-dt .w5-row { padding-top: 10px; padding-bottom: 10px; }
.phone .w5-dt .w5-row + .w5-row { margin-top: 8px; }
.phone .w5-dt .w5-sum { margin-top: 18px; padding-top: 14px; }
.phone .w5-dt .w5-sum > b { font-size: 32px; line-height: 38px; }
.phone .w5-dt .w5-sum dl { margin-top: 8px; row-gap: 5px; }
.phone .w5-dt .w5-sum p { margin-top: 8px; }
/* tab roots and detail pages share the Home canvas; full-screen flows (onboarding) stay white */
.phone .scr:has(.w5-br), .phone .scr:has(.w5-br) .xm1-bar, .phone .scr:has(.w5-en), .phone .scr:has(.w5-en) .xm1-bar,
.phone .scr:has(.w5-dt), .phone .scr:has(.w5-dt) .xm1-bar { background: var(--hd-canvas) !important; }
.phone .w5-dt .w5-bb, .phone .w5-bb { background: var(--hd-surface); }
.phone .w5-br .w5-tabs { border-bottom-color: var(--hd-edge); }
.phone .w5-dt .w5-sum { border-top: 0; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 20px; padding: 16px 18px; margin-top: 16px; }
.phone .w5-dt .w5-sum > b { font-size: 32px; line-height: 38px; }
.phone .scr:has(.w5-dt):not(:has(.w5-bb)) .home-ind, .phone .scr:has(.m7):not(:has(.w5-bb)):not(:has(.tabbar)):not(:has(.m6-dock)) .home-ind { background: var(--hd-canvas) !important; }
:root:root:root:root .phone .scr:is(:has(.w5), :has(.m7)):not(:has(.w5-bb)):not(:has(.tabbar)):not(:has(.m6-dock)):not(:has(.xm1-pad)) .home-ind { background: transparent !important; }
.phone .scr:has(.c6-det), .phone .scr:has(.c6-det) .xm1-bar { background: var(--hd-canvas) !important; }
.phone .c6-det .w5-sum.c6-offer { border-top: 0 !important; background: var(--hd-surface); border: 1px solid var(--hd-edge) !important; border-radius: 20px; padding: 16px 18px !important; margin-top: 14px; }
.phone .c6-det .w5-sum.c6-offer > b { font-size: 32px; line-height: 38px; }
.phone .c6-det .w5-row { background: var(--hd-surface); }
:root:root:root .phone .scr:has(.c6-det) { position: relative; }
:root:root:root .phone .scr:has(.c6-det) .sbar { position: absolute; top: 0; left: 0; right: 0; z-index: 6; background: transparent !important; color: #fff !important; }
.phone .c6-det .c6-hero { margin-top: 0; }
.phone .c6-det .c6-hero .tb { top: 54px !important; }
.phone .c6-det .c6-hero::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 96px; z-index: 1; background: linear-gradient(180deg, rgba(10,12,16,.42), rgba(10,12,16,0)); pointer-events: none; }
.phone .c6-det .c6-hero .tb { z-index: 2; }
.phone .scr:is(:has(.c6-inb), :has(.c6-emp), :has(.c6-bar)), .phone .scr:is(:has(.c6-inb), :has(.c6-emp), :has(.c6-bar)) .xm1-bar { background: var(--hd-canvas) !important; }
.phone :is(.c6-inb, .c6-emp, .c6-bar) .w5-row { background: var(--hd-surface); }
.phone .c6-dl.c6-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 12px 16px; margin: 0; }
:root:root:root .phone .scr:has(.c6-emp) .searchbar { background: var(--hd-canvas) !important; }
:root:root:root .phone .scr:has(.c6-emp) .searchbar .search { background: var(--hd-surface) !important; }
"""
