# Layer for scr_home.py (evolved direction, 2026-11-26).
XCV = """
.phone .cv { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 22px; padding: 2px 0 20px; background: var(--hd-canvas); }
.phone .scr:has(.cv) { background: var(--hd-canvas); }
.phone .scr:has(.cv) .xm1-bar { padding-bottom: 6px; }
.cv-pad { padding: 0 16px; }
.phone .cv > * { flex: none; }
.cv-act .tag img, .cv-pick .st img { width: 14px !important; height: 14px !important; border-radius: 4px; flex: none; }
.cv-hi { display: flex; align-items: flex-end; justify-content: space-between; padding: 6px 20px 0; }
.cv-hi small { display: block; font-size: 13px; color: var(--hd-fg-muted); margin-bottom: 2px; }
.cv-hi h1 { font-family: var(--font-brand); font-size: 30px; line-height: 34px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
/* the wallet: ink, the parcel pattern fading in at the corner */
.cv-wal { position: relative; overflow: hidden; margin: 0 16px; border-radius: 22px; background: #121417; color: #fff; padding: 20px 20px 0; }
.cv-wal > * { position: relative; }
.cv-wal small { font-size: 13px; color: rgba(255,255,255,.66); }
.cv-wal .big { display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; margin-top: 2px; }
.cv-wal b.num { font-family: var(--font-brand); font-size: 42px; line-height: 46px; font-weight: 700; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; }
.cv-wal .wd { height: 36px; padding: 0 14px; border-radius: 10px; background: #fff; color: #121417; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; border: 0; }
.cv-wal p { margin: 6px 0 18px; font-size: 13.5px; color: rgba(255,255,255,.72); } .cv-wal p .num { color: #fff; font-weight: 600; }
.cv-wal .ft { display: flex; align-items: center; gap: 10px; margin: 0 -20px; padding: 13px 20px; border-top: 1px solid rgba(255,255,255,.12); font-size: 14px; }
.cv-wal .ft span { flex: 1; } .cv-wal .ft em { font-style: normal; font-weight: 600; color: #a0c6ff; }
.cv-sh { display: flex; align-items: baseline; justify-content: space-between; padding: 0 20px; margin-bottom: -10px; }
.cv-sh h2 { font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 650; margin: 0; letter-spacing: -0.01em; }
.cv-sh span { font-size: 13px; color: var(--hd-fg-muted); } .cv-sh em { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); }
/* your turn: big action cards in a row */
.cv-rail { display: flex; gap: 12px; padding: 0 16px; overflow: hidden; }
.cv-act { flex: none; width: 268px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; }
.cv-act .ph { position: relative; height: 132px; } .cv-act .ph img { width: 100%; height: 100%; object-fit: cover; display: block; }
.cv-act .ph .tag { position: absolute; left: 12px; bottom: 12px; height: 26px; padding: 0 10px; border-radius: 8px; background: rgba(255,255,255,.94); color: #121417; font-size: 12.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
.cv-act .bd { padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 2px; }
.cv-act .bd small { font-size: 13px; color: var(--hd-fg-muted); }
.cv-act .bd b { font-family: var(--font-brand); font-size: 21px; line-height: 26px; font-weight: 700; letter-spacing: -0.015em; }
.cv-act .bd b.warn { color: var(--hd-warning-strong); }
.cv-act .pr { display: flex; align-items: center; gap: 10px; margin-top: 12px; }
.cv-act .pr i { flex: 1; height: 4px; border-radius: 4px; background: var(--hd-control); position: relative; overflow: hidden; }
.cv-act .pr i u { position: absolute; inset: 0 auto 0 0; background: var(--hd-accent); border-radius: 4px; }
.cv-act .pr span { font-size: 12.5px; color: var(--hd-fg-muted); white-space: nowrap; }
.cv-act .go { margin-top: 14px; height: 40px; border-radius: 12px; border: 0; background: var(--hd-accent); color: #fff; font-weight: 600; font-size: 14.5px; }
.cv-act .go.s { background: var(--hd-surface); color: var(--hd-fg); box-shadow: inset 0 0 0 1px var(--hd-border-strong); }
/* on the way: the shipment, with the tracking illustration */
.cv-ship { margin: 0 16px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 20px; padding: 16px; display: flex; gap: 14px; align-items: center; }
.cv-ship img.il { width: 76px; height: 76px; flex: none; }
.cv-ship .tx { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; }
.cv-ship b { font-size: 15px; line-height: 20px; font-weight: 600; } .cv-ship small { font-size: 13px; color: var(--hd-fg-muted); }
.cv-steps { display: flex; gap: 4px; margin-top: 8px; } .cv-steps i { flex: 1; height: 4px; border-radius: 4px; background: var(--hd-control); } .cv-steps i.on { background: var(--hd-accent); }
/* in review: one quiet row */
.cv-row { margin: 0 16px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 10px 14px 10px 10px; display: flex; gap: 12px; align-items: center; }
.cv-row img { width: 48px; height: 48px; border-radius: 10px; object-fit: cover; } .cv-row .tx { flex: 1; display: flex; flex-direction: column; gap: 2px; }
.cv-row b { font-size: 15px; font-weight: 600; } .cv-row small { font-size: 13px; color: var(--hd-fg-muted); } .cv-row .amt { font-weight: 600; font-size: 15px; }
/* picked for you: one editorial photo card */
.cv-pick { position: relative; margin: 0 16px; height: 236px; border-radius: 22px; overflow: hidden; }
.cv-pick img { width: 100%; height: 100%; object-fit: cover; display: block; }
.cv-pick::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10,12,16,0) 38%, rgba(10,12,16,.78) 100%); }
.cv-pick .st { position: absolute; z-index: 1; left: 14px; top: 14px; height: 26px; padding: 0 10px; border-radius: 8px; background: rgba(255,255,255,.94); color: #121417; font-size: 12.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
.cv-pick .bt { position: absolute; z-index: 1; left: 18px; right: 18px; bottom: 16px; color: #fff; display: flex; align-items: flex-end; justify-content: space-between; gap: 12px; }
.cv-pick .bt small { display: block; font-size: 13px; color: rgba(255,255,255,.8); }
.cv-pick .bt b { display: block; font-family: var(--font-brand); font-size: 24px; line-height: 28px; font-weight: 700; letter-spacing: -0.02em; }
.cv-pick .bt em { font-style: normal; font-size: 13px; color: rgba(255,255,255,.86); }
.cv-pick .bt .j { height: 36px; padding: 0 14px; border-radius: 10px; background: #fff; color: #121417; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; flex: none; }
.cv-long .phone, .cv-long .scr { height: auto !important; } .cv-long .cv { overflow: visible; }
"""
