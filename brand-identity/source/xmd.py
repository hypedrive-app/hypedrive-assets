# Layer (xmd). Prefix every class to avoid clashes.
XMD = """
.phone .scr:has(.md-pg) { background: var(--hd-canvas); }
.phone .md-pg { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 0 16px 12px; background: var(--hd-canvas); font-family: var(--font-ui); color: var(--hd-fg); }
.phone .md-pg > * { flex: none; }
.phone .md-bar { height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 4px; margin: 0 -4px; }
.phone .md-bar .l, .phone .md-bar .r { display: flex; align-items: center; gap: 18px; }
.phone .md-bar .ic { width: 22px; height: 22px; color: var(--hd-fg); }
.phone .md-bar .bell { position: relative; display: flex; } .phone .md-bar .bell i { position: absolute; top: -1px; right: 0; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-tone-vermilion); box-shadow: 0 0 0 2px var(--hd-canvas); }
.phone .md-av { border-radius: 50%; object-fit: cover; flex: none; display: block; } .phone .md-av.s40 { width: 40px; height: 40px; } .phone .md-av.s32 { width: 32px; height: 32px; }
.phone .md-th { border-radius: 10px; object-fit: cover; flex: none; display: block; } .phone .md-th.s48 { width: 48px; height: 48px; } .phone .md-th.s40 { width: 40px; height: 40px; } .phone .md-th.s56 { width: 56px; height: 56px; } .phone .md-th.s64 { width: 64px; height: 64px; } .phone .md-th.s32 { width: 32px; height: 32px; border-radius: 8px; }
.phone .md-hd h1, .phone .md-top h1 { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .md-hd { margin: 0 4px; } .phone .md-hd p { display: flex; align-items: center; gap: 5px; margin: 2px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .md-top { height: 48px; display: flex; align-items: center; justify-content: space-between; margin: 0 4px; padding-top: 2px; } .phone .md-top .ic { width: 22px; height: 22px; }
.phone .md-hd2 { display: flex; align-items: center; gap: 12px; } .phone .md-hd2 h1 { font-size: 24px; line-height: 28px; }
.phone .md-sh { display: flex; align-items: baseline; justify-content: space-between; margin: 4px 4px -2px; }
.phone .md-sh h2 { font-family: var(--font-brand); font-size: 18px; line-height: 24px; font-weight: 650; margin: 0; }
.phone .md-sh span { font-size: 13px; color: var(--hd-fg-subtle); } .phone .md-sh span:not(:empty) { font-weight: 560; }
.phone .md-sh span.k { color: var(--hd-link); }
.phone .md-tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.phone .md-tile { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; padding: 12px; display: flex; flex-direction: column; gap: 4px; min-width: 0; }
.phone .md-tile small { font-size: 12.5px; line-height: 16px; min-height: 32px; color: var(--hd-fg-muted); }
.phone .md-tile b { font-family: var(--font-brand); font-size: 22px; line-height: 26px; font-weight: 700; letter-spacing: -0.02em; white-space: nowrap; }
.phone .md-row, .phone .md-act, .phone .md-cc, .phone .md-store, .phone .md-bal, .phone .md-pay, .phone .md-earn, .phone .md-stats, .phone .md-stats2, .phone .md-jr { background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 16px; }
.phone .md-row { display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 10px 14px 10px 10px; }
.phone .md-row .tx, .phone .md-act .tx, .phone .md-cc .tx, .phone .md-store .tx, .phone .md-opt .tx, .phone .md-pickd .tx { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1; }
.phone .md-row b, .phone .md-act b, .phone .md-cc b, .phone .md-store b, .phone .md-opt b, .phone .md-pickd b { font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
.phone .md-row small, .phone .md-act small, .phone .md-cc small, .phone .md-store small, .phone .md-opt small, .phone .md-pickd small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: flex; align-items: center; gap: 4px; }
.phone .md-row small em { font-style: normal; font-weight: 600; color: var(--hd-fg); }
.phone .md-pg em.warn, .phone .md-pg .warn { color: var(--hd-warning-strong); font-style: normal; font-weight: 600; }
.phone .md-act { padding: 10px 10px 10px 10px; display: flex; flex-direction: column; gap: 10px; }
.phone .md-act .top { display: flex; align-items: center; gap: 12px; } .phone .md-act .amt { font-size: 15px; padding-right: 4px; }
.phone .md-act .ft { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--hd-edge); margin: 0 -10px -10px; padding: 8px 10px 8px 14px; font-size: 14px; }
.phone .md-act .ft .btn { flex: none; }
/* deals */
.phone .md-tabs { display: flex; gap: 24px; border-bottom: 1px solid var(--hd-edge); margin: 0 -16px; padding: 0 20px; }
.phone .md-tabs span { height: 42px; display: inline-flex; align-items: center; font-size: 15px; font-weight: 560; color: var(--hd-fg-muted); border-bottom: 2px solid transparent; margin-bottom: -1px; }
.phone .md-tabs span.on { color: var(--hd-fg); border-bottom-color: var(--hd-accent); }
.phone .md-search { height: 44px; display: flex; align-items: center; gap: 10px; padding: 0 14px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 12px; color: var(--hd-fg-subtle); font-size: 15px; }
.phone .md-search span { flex: 1; } .phone .md-search .ic { color: var(--hd-fg-muted); flex: none; }
.phone .md-chips { display: flex; gap: 6px; }
.phone .md-chip { height: 36px; padding: 0 10px; display: inline-flex; align-items: center; gap: 6px; border-radius: 10px; background: var(--hd-surface); border: 1px solid var(--hd-edge); font-size: 14px; font-weight: 500; color: var(--hd-fg-muted); white-space: nowrap; }
.phone .md-chip i { font-style: normal; font-size: 13px; color: var(--hd-fg-subtle); }
.phone .md-chip.on { background: var(--hd-accent-subtle); border-color: transparent; color: var(--hd-accent-strong, var(--hd-link)); font-weight: 600; } .phone .md-chip.on i { color: inherit; }
.phone .md-cc { padding: 12px 12px 10px; display: flex; flex-direction: column; gap: 10px; }
.phone .md-cc .top { display: flex; gap: 12px; } .phone .md-cc .sr { display: flex; align-items: center; gap: 5px; font-size: 12.5px; line-height: 16px; color: var(--hd-fg-muted); }
.phone .md-cc .ft { display: flex; align-items: center; justify-content: space-between; font-size: 13.5px; }
.phone .md-store { padding: 4px 14px; display: flex; flex-direction: column; }
.phone .md-store .lkr, .phone .md-store .swr { display: flex; align-items: center; gap: 12px; padding: 10px 0; } .phone .md-store .swr { border-top: 1px solid var(--hd-edge); align-items: flex-start; }
.phone .md-store .swr small { white-space: normal; display: block; }
.phone .md-switch { width: 44px; height: 26px; border-radius: 13px; background: var(--hd-track, #e3e5ea); position: relative; flex: none; margin-top: 2px; } .phone .md-switch i { position: absolute; top: 2px; left: 2px; width: 22px; height: 22px; border-radius: 50%; background: #fff; box-shadow: 0 1px 2px rgba(16,20,38,.3); }
.phone .md-switch.on { background: var(--hd-accent); } .phone .md-switch.on i { left: 20px; }
.phone .md-deal small:nth-of-type(1):empty { display: none; }
/* sheet */
.phone .md-sheet { background: var(--hd-surface); border-radius: 24px 24px 0 0; padding: 8px 16px 30px; display: flex; flex-direction: column; gap: 12px; }
.phone .md-sheet .grab { width: 40px; height: 5px; border-radius: 3px; background: var(--hd-track-strong, #d5d7de); margin: 0 auto -2px; }
.phone .md-sh2 { display: flex; justify-content: space-between; align-items: flex-start; }
.phone .md-sh2 small { font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); }
.phone .md-sh2 h2 { margin: 2px 0 0; font: 700 24px/28px var(--font-brand); letter-spacing: -.02em; }
.phone .md-x { color: var(--hd-fg-muted); display: flex; padding-top: 4px; }
.phone .md-pickd { display: flex; align-items: center; gap: 12px; } .phone .md-pickd small img { vertical-align: middle; }
.phone .md-sl { display: flex; flex-direction: column; gap: 6px; }
.phone .md-sl .t { display: flex; justify-content: space-between; align-items: baseline; } .phone .md-sl .t b { font-size: 15px; font-weight: 600; } .phone .md-sl .t span { font-size: 14px; font-weight: 600; }
.phone .md-sl .rail { position: relative; height: 4px; border-radius: 2px; background: var(--hd-track, #e3e5ea); margin: 10px 0 8px; }
.phone .md-sl .rail i { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 2px; background: var(--hd-accent); }
.phone .md-sl .rail s { position: absolute; top: 50%; width: 28px; height: 28px; margin: -14px 0 0 -14px; border-radius: 50%; background: #fff; border: 1px solid var(--hd-edge); box-shadow: 0 1px 3px rgba(16,20,38,.22), 0 2px 6px rgba(16,20,38,.08); text-decoration: none; }
.phone .md-sl small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); } .phone .md-sl small.sp { color: var(--hd-fg); font-weight: 600; }
.phone .md-drag { margin: -4px 0 0; text-align: center; font-size: 12.5px; color: var(--hd-fg-subtle); }
.phone .md-fig { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--hd-edge); border-radius: 14px; padding: 12px 14px; gap: 8px; }
.phone .md-fig small { display: block; font-size: 12.5px; color: var(--hd-fg-muted); } .phone .md-fig b { display: block; font-family: var(--font-brand); font-size: 20px; line-height: 26px; font-weight: 700; letter-spacing: -.02em; white-space: nowrap; }
.phone .md-note { margin: 0; text-align: center; font-size: 13px; color: var(--hd-fg-muted); }
.phone .md-sheet .btn.lg { height: 48px !important; }
/* enroll */
.phone .md-for { margin: 0; font-size: 14px; color: var(--hd-fg-muted); } .phone .md-cant { margin: 4px 0 -4px; font-size: 13px; font-weight: 600; color: var(--hd-fg-muted); }
.phone .md-opt { display: flex; align-items: center; gap: 12px; padding: 10px; border: 1px solid var(--hd-edge); border-radius: 16px; }
.phone .md-opt.on { background: var(--hd-accent-subtle); border-color: transparent; } .phone .md-opt .md-tick { color: var(--hd-accent); display: flex; padding-right: 4px; }
.phone .md-opt.no .tx small { white-space: normal; display: block; } .phone .md-opt.no { opacity: .72; }
/* enrollment */
.phone .md-pay { padding: 16px; display: flex; flex-direction: column; gap: 8px; }
.phone .md-pay h2 { margin: 0; font-family: var(--font-brand); font-size: 24px; line-height: 30px; font-weight: 700; letter-spacing: -.02em; }
.phone .md-pay p { margin: 0 0 6px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .md-who .md-ib { width: 36px; height: 36px; border-radius: 10px; border: 1px solid var(--hd-edge); background: var(--hd-surface); display: grid; place-items: center; color: var(--hd-fg); flex: none; }
.phone .md-jr { list-style: none; margin: 0; padding: 6px 14px; display: flex; flex-direction: column; }
.phone .md-jr li { display: flex; align-items: center; gap: 12px; min-height: 34px; font-size: 14px; }
.phone .md-jr li div { flex: 1; } .phone .md-jr li b { font-weight: 560; color: var(--hd-fg); } .phone .md-jr li span { color: var(--hd-fg-muted); font-size: 13px; }
.phone .md-jr li .ic { color: var(--hd-success-strong); flex: none; }
.phone .md-jr li.now { align-items: flex-start; padding: 8px 0 6px; } .phone .md-jr li.now small { display: block; font-size: 13px; color: var(--hd-fg-muted); margin-top: 2px; }
.phone .md-jr .ring { width: 18px; height: 18px; border-radius: 50%; border: 2px solid var(--hd-accent); flex: none; box-sizing: border-box; margin-top: 1px; }
/* wallet */
.phone .md-bal { padding: 16px 16px 0; display: flex; flex-direction: column; }
.phone .md-bal > small { font-size: 13px; color: var(--hd-fg-muted); } .phone .md-bal > b { font-family: var(--font-brand); font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -.025em; margin-top: 2px; }
.phone .md-bal { padding-bottom: 16px; } .phone .md-bal p { display: flex; justify-content: space-between; margin: 2px 0 14px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); } .phone .md-bal p .num { color: var(--hd-fg); font-weight: 600; }
.phone .md-bal .ft { display: flex; align-items: center; gap: 8px; margin: 14px -16px 0; padding: 12px 16px; border-top: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-link); font-weight: 600; } .phone .md-bal .ft .ic { color: var(--hd-fg-muted); }
.phone .md-pa { min-height: 60px; } .phone .md-pa .bankt { width: 40px !important; height: 40px !important; }
.phone .md-earn { padding: 14px 16px; display: flex; flex-direction: column; }
.phone .md-earn > small { font-size: 13px; color: var(--hd-fg-muted); } .phone .md-earn .big { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 10px; } .phone .md-earn .big b { font-family: var(--font-brand); font-size: 28px; line-height: 34px; font-weight: 700; letter-spacing: -.02em; } .phone .md-earn .big span { font-size: 13px; color: var(--hd-fg-muted); }
.phone .md-earn .mo { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.phone .md-earn .mo div { display: flex; flex-direction: column; gap: 2px; } .phone .md-earn .mo small { font-size: 13px; color: var(--hd-fg-muted); } .phone .md-earn .mo b { font-size: 15px; font-weight: 600; color: var(--hd-fg-muted); } .phone .md-earn .mo .on b { color: var(--hd-fg); }
.phone .md-erow { display: flex; align-items: center; gap: 12px; height: 44px; padding: 0 14px 0 6px; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; }
.phone .md-erow b { flex: 1; font-size: 15px; font-weight: 600; } .phone .md-erow span { font-size: 15px; font-weight: 600; }
/* trust */
.phone .md-tl { width: 40px !important; height: 40px !important; }
.phone .md-rv b { display: flex; align-items: center; gap: 5px; } .phone .md-rv small .st { display: inline-flex; color: var(--hd-tone-marigold); margin-right: 4px; } .phone .md-rv .st .ic { width: 12px; height: 12px; }
.phone .md-stats { display: grid; grid-template-columns: 1fr 1fr; padding: 14px 16px; gap: 12px; }
.phone .md-stats .hero { display: flex; flex-direction: column; } .phone .md-stats .hero b { font-family: var(--font-brand); font-size: 34px; line-height: 38px; font-weight: 700; letter-spacing: -.025em; }
.phone .md-stats .hero small { font-size: 13px; color: var(--hd-fg-muted); } .phone .md-stats .hero span { font-size: 13px; color: var(--hd-fg-subtle); }
.phone .md-stats2 { display: grid; grid-template-columns: repeat(5, 1fr); padding: 12px 10px; gap: 4px; text-align: center; }
.phone .md-stats2 div { display: flex; flex-direction: column; gap: 2px; min-width: 0; } .phone .md-stats2 b { font-family: var(--font-brand); font-size: 20px; line-height: 24px; font-weight: 700; } .phone .md-stats2 small { font-size: 11.5px; color: var(--hd-fg-muted); white-space: nowrap; }
/* dock */
.phone .md-dock { height: 64px; flex: none; display: flex; border-top: 1px solid var(--hd-edge); background: var(--hd-surface); }
.phone .md-di { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 8px; gap: 3px; font-size: 11px; font-weight: 560; color: var(--hd-fg-subtle); }
.phone .md-di.on { color: var(--hd-link); }
.phone .md-disc { width: 36px; height: 36px; border-radius: 50%; background: var(--hd-accent); color: #fff; display: grid; place-items: center; box-shadow: inset 0 1px 0 rgba(255,255,255,.16), 0 1px 2px rgba(16,20,38,.2); margin-bottom: 0; } .phone .md-disc .ic { width: 20px; height: 20px; }
.phone .md-bal p em { font-style: normal; font-weight: 600; color: var(--hd-link); }
.phone .md-pg .hm-wal { margin-bottom: 2px; }
.phone .md-pg .hm-wal p { margin-bottom: 16px; }
.phone .md-row .md-lk { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); flex: none; }
.phone .md-row small .warn { font-style: normal; color: var(--hd-warning-strong); font-weight: 600; }
.phone .md-trust { padding-bottom: 4px; }
.phone .md-trust p { margin-bottom: 8px !important; }
.phone .md-kv { display: flex; justify-content: space-between; align-items: center; height: 40px; border-top: 1px solid var(--hd-edge); font-size: 14px; color: var(--hd-fg); }
.phone .md-kv b { font-weight: 600; }
.phone .md-kv.mute { color: var(--hd-fg-subtle); }
/* p4 maturity pass */
.phone .md-pg .md-lk { font-style: normal; font-weight: 600; font-size: 14px; color: var(--hd-link); flex: none; }
.phone .md-row .md-val { font-size: 15px; font-weight: 600; color: var(--hd-fg); flex: none; }
.phone .md-store .swr { align-items: center; } .phone .md-store .lkr { padding: 12px 0; } .phone .md-store .swr { padding: 12px 0; } .phone .md-switch { margin-top: 0; }
.phone .md-chip.on { background: var(--hd-accent-subtle); }
.phone .md-fig { display: flex; flex-direction: column; border: 0; border-radius: 0; padding: 4px 0 0; gap: 0; }
.phone .md-fig small { font-size: 13px; line-height: 18px; }
.phone .md-fig b { font-size: 34px; line-height: 40px; }
.phone .md-fig p { margin: 2px 0 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); } .phone .md-fig p .num { color: var(--hd-fg); font-weight: 600; }
.phone .md-note { margin: 4px 0 -4px; }
.phone .md-opt.on { background: var(--hd-surface); border-color: var(--hd-edge); }
.phone .md-opt .md-tick { color: var(--hd-accent); display: flex; flex: none; padding-right: 2px; }
.phone .md-opt.no { border: 0; padding: 0 0 0 4px; opacity: 1; }
.phone .md-opt.no .md-th { opacity: .55; } .phone .md-opt.no b { color: var(--hd-fg-muted); font-weight: 600; }
.phone .md-opt.no .tx small { color: var(--hd-fg-subtle); }
.phone .md-hd2 h1 { font-size: 28px; line-height: 32px; }
.phone .md-pay { padding: 16px; gap: 0; }
.phone .md-pay > small { font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .md-pay > b { font-family: var(--font-brand); font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -.025em; font-variation-settings: 'opsz' 96; margin-top: 2px; }
.phone .md-pay p { margin: 2px 0 14px; font-size: 13px; line-height: 18px; } .phone .md-pay p .num { color: var(--hd-fg); font-weight: 600; }
.phone .md-jr { background: none; border: 0; border-radius: 0; padding: 0 4px; margin-top: -4px; }
.phone .md-jr li { position: relative; min-height: 36px; } .phone .md-jr li b { font-weight: 500; color: var(--hd-fg-muted); }
.phone .md-jr .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--hd-fg-subtle); flex: none; margin: 0 5px; position: relative; z-index: 1; }
.phone .md-jr li:not(:last-child)::before { content: ""; position: absolute; left: 8.5px; top: 50%; height: 100%; width: 1px; background: var(--hd-edge); }
.phone .md-jr li.now { align-items: flex-start; padding: 8px 0 0; min-height: 0; } .phone .md-jr li.now .dot { margin-top: 6px; width: 8px; height: 8px; background: var(--hd-accent); box-shadow: 0 0 0 4px var(--hd-accent-subtle); }
.phone .md-jr li.now b { font-weight: 600; color: var(--hd-fg); }
"""
