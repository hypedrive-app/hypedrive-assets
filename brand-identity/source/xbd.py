# Layer for desk_home.py (evolved direction, 2026-11-26).
XBD = """
.bd2 { display: flex; flex-direction: column; gap: 28px; }
.bd2 > * { flex: none; }
.bd2-hd { display: flex; align-items: flex-end; justify-content: space-between; }
.bd2-hd small { font-size: 14px; color: var(--hd-fg-muted); }
.bd2-hd h1 { font-family: var(--font-brand); font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 2px 0 0; }
.bd2-row { display: grid; grid-template-columns: 1fr 360px; gap: 20px; align-items: stretch; }
.bd2-card { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 20px; padding: 20px; }
.bd2-sh { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px; }
.bd2-sh h2 { font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 650; margin: 0; letter-spacing: -0.01em; }
.bd2-sh span { font-size: 13.5px; color: var(--hd-fg-muted); } .bd2-sh em { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); }
/* needs you: submissions as content */
.bd2-subs { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.bd2-sub { display: flex; flex-direction: column; gap: 8px; }
.bd2-sub .bd2-th { position: relative; height: 208px; border-radius: 14px; overflow: hidden; }
.bd2-sub .bd2-th > img { width: 100%; height: 100%; object-fit: cover; display: block; }
.bd2-sub .bd2-th .k img { width: 14px; height: 14px; border-radius: 4px; }
.bd2-sub .bd2-th .k { position: absolute; left: 8px; top: 8px; height: 24px; padding: 0 8px; border-radius: 7px; background: rgba(255,255,255,.94); font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; gap: 5px; color: #121417; }
.bd2-sub .who { display: flex; align-items: center; gap: 8px; } .bd2-sub .who img { width: 24px; height: 24px; border-radius: 50%; }
.bd2-sub .who b { font-size: 13.5px; font-weight: 600; } .bd2-sub small { font-size: 12.5px; color: var(--hd-fg-muted); }
.bd2-more { display: flex; align-items: center; justify-content: space-between; margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg-muted); }
.bd2-more .btn { height: 40px; }
/* wallet: ink, like the creator wallet */
.bd2-side { display: flex; flex-direction: column; gap: 20px; }
/* live campaigns as visual cards */
.bd2-camps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.bd2-camp { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 18px; overflow: hidden; }
.bd2-camp > img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; display: block; }
.bd2-camp .b { padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 4px; }
.bd2-camp .b span.s { display: flex; align-items: center; gap: 5px; font-size: 12.5px; color: var(--hd-fg-muted); } .bd2-camp .b span.s img { width: 14px; height: 14px; aspect-ratio: auto; border-radius: 4px; }
.bd2-camp b { font-size: 15.5px; font-weight: 600; }
.bd2-camp .bar { height: 4px; border-radius: 4px; background: var(--hd-control); margin-top: 8px; overflow: hidden; } .bd2-camp .bar i { display: block; height: 100%; background: var(--hd-accent); }
.bd2-camp small { display: flex; justify-content: space-between; font-size: 12.5px; color: var(--hd-fg-muted); margin-top: 4px; } .bd2-camp small .warn { color: var(--hd-warning-strong); font-weight: 600; }
/* trend + posts */
.bd2-two { display: grid; grid-template-columns: 1fr 1.4fr; gap: 20px; }
.bd2-trend b.num { font-family: var(--font-brand); font-size: 40px; line-height: 46px; font-weight: 700; letter-spacing: -0.03em; }
.bd2-trend p { margin: 2px 0 18px; font-size: 14px; color: var(--hd-fg-muted); }
.bd2-bars { display: flex; align-items: flex-end; gap: 14px; height: 150px; }
.bd2-bars div { flex: 1; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 6px; height: 100%; } .bd2-bars i { display: block; flex: none; width: 100%; border-radius: 8px 8px 4px 4px; background: color-mix(in oklab, var(--hd-accent) 26%, var(--hd-surface)); }
.bd2-bars div.on i { background: var(--hd-accent); } .bd2-bars small { font-size: 12px; color: var(--hd-fg-muted); }
.bd2-posts { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.bd2-post { position: relative; aspect-ratio: 1; border-radius: 12px; overflow: hidden; } .bd2-post > img { width: 100%; height: 100%; object-fit: cover; display: block; }
.bd2-post span { position: absolute; left: 6px; bottom: 6px; width: 24px; height: 24px; border-radius: 7px; background: rgba(255,255,255,.94); display: grid; place-items: center; }
.bd2-post span img { width: 14px; height: 14px; }
.bd2-inb { padding: 6px 20px; flex: 1; }
.bd2-inb .bd2-sh { margin: 12px 0 4px; }
.bd2-ir { display: flex; flex-direction: column; gap: 2px; padding: 12px 0; border-top: 1px solid var(--hd-edge); }
.bd2-ir b { font-size: 14.5px; font-weight: 600; } .bd2-ir small { font-size: 13px; color: var(--hd-fg-muted); } .bd2-ir small.warn { color: var(--hd-warning-strong); }
.bd2-trend { display: flex; flex-direction: column; } .bd2-trend .bd2-bars { margin-top: auto; height: 190px; }
.bd2-sub .who div { display: flex; flex-direction: column; } .bd2-sub .who small { font-size: 12px; color: var(--hd-fg-muted); } .bd2-sub small.sent { font-size: 12.5px; color: var(--hd-fg-muted); }
.bd2-camp small.m { margin-top: 2px; color: var(--hd-fg); font-weight: 500; }
.bd2-low { display: grid; grid-template-columns: 1fr 360px; gap: 20px; align-items: start; }
.bd2-camps.g2 { grid-template-columns: repeat(2, 1fr); } .bd2-camps.g2 .bd2-camp > img { aspect-ratio: 16 / 8; }
.bd2-top { padding: 4px 20px; }
.bd2-tr { display: flex; align-items: center; gap: 12px; min-height: 62px; } .bd2-tr + .bd2-tr { border-top: 1px solid var(--hd-edge); }
.bd2-tr .n { width: 16px; font-size: 13px; color: var(--hd-fg-subtle); } .bd2-tr img { width: 36px; height: 36px; border-radius: 50%; object-fit: cover; }
.bd2-tr .tx { flex: 1; display: flex; flex-direction: column; } .bd2-tr .tx b { font-size: 14.5px; font-weight: 600; } .bd2-tr .tx small { font-size: 12.5px; color: var(--hd-fg-muted); }
.bd2-tr .v { display: flex; flex-direction: column; align-items: flex-end; } .bd2-tr .v b { font-family: var(--font-brand); font-size: 19px; font-weight: 700; } .bd2-tr .v small { font-size: 12px; color: var(--hd-fg-muted); }
.pg .ph .t p b { color: var(--hd-fg); font-weight: 600; }
.bd2-need { display: flex; flex-direction: column; }
.bd2-nh { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 16px; }
.bd2-nh h2 { font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 650; margin: 0; letter-spacing: -0.01em; }
.bd2-nh small { font-size: 13.5px; color: var(--hd-fg-muted); }
.bd2-need .bd2-subs { flex: 1; } .bd2-need .bd2-sub { height: 100%; } .bd2-need .bd2-sub .bd2-th { flex: 1; height: auto; min-height: 200px; }
.bd2-sub .who { align-items: flex-start; } .bd2-sub .who img { margin-top: 2px; } .bd2-sub .who div { display: flex; flex-direction: column; gap: 1px; min-width: 0; }
.bd2-sub .who small { font-size: 12.5px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
"""
