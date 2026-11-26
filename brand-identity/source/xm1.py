# mobile screens redesign layer 1: welcome, verify phone, home, drop details. Every selector is scoped under .phone .scr:has(.xm1-*) or .phone .xm1-*
XM1 = r"""
/* shared: plain surface, not the grey canvas */
.phone .scr:has(.xm1-s) { background: var(--hd-surface); }
.phone .xm1-s { font-family: var(--font-ui); }

/* ---------- welcome (dark) ---------- */
.phone .scr:has(.xm1-wel) { background: #0d0e12; }
.phone .xm1-wel { flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 0 20px 8px; position: relative; overflow: hidden; }
.phone .xm1-wel .xm1-logo { height: 26px; align-self: flex-start; margin: 6px 0 0; display: block; }
.phone .xm1-wel .xm1-mos { position: absolute; left: 0; right: 0; top: 54px; height: 372px; display: flex; gap: 10px; padding: 0 20px; }
.phone .xm1-wel .xm1-mos div { flex: 1; display: flex; flex-direction: column; gap: 10px; }
.phone .xm1-wel .xm1-mos div:nth-child(2) { margin-top: 34px; }
.phone .xm1-wel .xm1-mos img { width: 100%; object-fit: cover; border-radius: 16px; display: block; }
.phone .xm1-wel .xm1-fade { position: absolute; left: 0; right: 0; top: 270px; height: 170px; background: linear-gradient(180deg, rgba(13,14,18,0), #0d0e12 92%); pointer-events: none; }
.phone .xm1-wel .xm1-copy { margin-top: auto; position: relative; display: flex; flex-direction: column; gap: 12px; }
.phone .xm1-wel .xm1-h { font-family: var(--font-brand); font-size: 46px; line-height: 48px; font-weight: 650; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; color: #fff; margin: 0; }
.phone .xm1-wel .xm1-h span { color: #a0c6ff; }
.phone .xm1-wel .xm1-p { margin: 0; font-size: 16px; line-height: 24px; color: rgba(255,255,255,.66); max-width: 320px; }
.phone .xm1-wel .xm1-act { display: flex; flex-direction: column; gap: 4px; margin-top: 12px; }
.phone .xm1-wel .xm1-act .btn.g { height: 44px !important; color: rgba(255,255,255,.78); font-weight: 560; }

/* ---------- verify phone ---------- */
.phone .xm1-otp { flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 8px 20px 12px; gap: 24px; }
.phone .xm1-otp .xm1-h { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .xm1-otp .xm1-sub { margin: 6px 0 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); }
.phone .xm1-otp .xm1-sub b { color: var(--hd-fg); font-weight: 560; }
.phone .xm1-code { display: flex; justify-content: center; gap: 8px; }
.phone .xm1-code span { width: 48px; height: 48px; flex: none; box-sizing: border-box; border: 1px solid var(--hd-border-input); border-radius: 10px; background: var(--hd-surface); display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 560; font-variant-numeric: tabular-nums; color: var(--hd-fg); box-shadow: none !important; }
.phone .xm1-code span.on { border: 2px solid var(--hd-accent); }
.phone .xm1-code span.on::after { content: ''; width: 2px; height: 22px; border-radius: 1px; background: var(--hd-accent); }
.phone .xm1-aux { display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 14px; color: var(--hd-fg-muted); }
.phone .xm1-aux .num { font-variant-numeric: tabular-nums; }
.phone .xm1-aux .btn.link { font-size: 14px; font-weight: 560; color: var(--hd-link); text-decoration: none; }
.phone .xm1-otp .btn.lg { height: 48px !important; }
.phone .xm1-pad { flex: none; display: grid; grid-template-columns: repeat(3, 1fr); padding: 4px 8px 8px; border-top: 1px solid var(--hd-border); background: var(--hd-surface); }
.phone .xm1-pad span { height: 52px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-radius: 10px; }
.phone .xm1-pad b { font-size: 24px; line-height: 26px; font-weight: 450; font-variant-numeric: tabular-nums; color: var(--hd-fg); }
.phone .xm1-pad small { font-size: 10px; line-height: 11px; font-weight: 600; letter-spacing: .08em; color: var(--hd-fg-subtle); height: 11px; }
.phone .xm1-pad span:last-child .ic { color: var(--hd-fg); }
.phone .scr:has(.xm1-pad) .home-ind { background: var(--hd-surface); }

/* ---------- home ---------- */
.phone .xm1-bar { height: 44px; display: flex; align-items: center; gap: 18px; padding: 0 20px; flex: none; }
.phone .xm1-bar img.av { width: 32px; height: 32px; border-radius: 50%; object-fit: cover; display: block; margin-right: auto; }
.phone .xm1-bar .ic { width: 22px; height: 22px; color: var(--hd-fg); }
.phone .xm1-bar .bell { position: relative; display: flex; } .phone .xm1-bar .bell i { position: absolute; top: -1px; right: 0; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-tone-vermilion); box-shadow: 0 0 0 2px var(--hd-surface); }
.phone .xm1-home { flex: 1; min-height: 0; display: flex; flex-direction: column; overflow: hidden; }
.phone .xm1-head { padding: 6px 20px 0; }
.phone .xm1-head .xm1-h { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .xm1-earn { margin: 4px 0 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); display: flex; gap: 6px; align-items: baseline; }
.phone .xm1-earn b { color: var(--hd-fg); font-weight: 650; font-variant-numeric: tabular-nums; } .phone .xm1-earn em { font-style: normal; font-size: 13.5px; font-weight: 560; color: var(--hd-success-strong); font-variant-numeric: tabular-nums; }
.phone .xm1-home .tabs { margin: 14px 20px 0; }
.phone .xm1-card { position: relative; margin: 16px 20px 0; height: 270px; border-radius: 20px; overflow: hidden; flex: none; background: var(--hd-bg-subtle); }
.phone .xm1-card > img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.phone .xm1-card::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(8,10,16,0) 0%, rgba(8,10,16,0) 38%, rgba(8,10,16,.38) 54%, rgba(8,10,16,.74) 72%, rgba(8,10,16,.90) 100%); }
.phone .xm1-card .top { position: absolute; z-index: 2; top: 12px; left: 12px; right: 12px; display: flex; justify-content: space-between; align-items: center; }
.phone .xm1-card .top .chip { height: 28px; padding: 0 10px; border-radius: 8px; display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; background: #121417 !important; color: #fff !important; border: 0 !important; box-shadow: none !important; }
.phone .xm1-card .top .chip .ic { width: 14px; height: 14px; color: #fff !important; }
.phone .xm1-card .x-disc { width: 36px; height: 36px; }
.phone .xm1-card .bt { position: absolute; z-index: 2; left: 16px; right: 16px; bottom: 16px; color: #fff; }
.phone .xm1-card .bt small { display: block; font-size: 13px; line-height: 18px; color: rgba(255,255,255,.80); }
.phone .xm1-card .bt b { display: block; margin-top: 2px; font-family: var(--font-brand); font-size: 22px; line-height: 26px; font-weight: 650; letter-spacing: -0.025em; }
.phone .xm1-card .bt .mt { display: flex; justify-content: space-between; margin-top: 6px; font-size: 14px; color: rgba(255,255,255,.88); font-variant-numeric: tabular-nums; }
.phone .xm1-card .bt .mt em { font-style: normal; font-weight: 650; color: #fff; }
.phone .xm1-card .bt .sl { display: block; height: 3px; margin-top: 10px; border-radius: 2px; background: rgba(255,255,255,.28); overflow: hidden; }
.phone .xm1-card .bt .sl u { display: block; height: 100%; background: #fff; text-decoration: none; }
.phone .xm1-sech { display: flex; justify-content: space-between; align-items: baseline; padding: 20px 20px 10px; }
.phone .xm1-sech b { font-size: 17px; font-weight: 650; letter-spacing: -0.01em; } .phone .xm1-sech .btn.link { font-size: 14px; text-decoration: none; }
.phone .xm1-two { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; padding: 0 20px; }
.phone .xm1-mini img { width: 100%; height: 104px; object-fit: cover; border-radius: 14px !important; display: block; }
.phone .xm1-mini b { display: block; margin-top: 8px; font-size: 15px; line-height: 20px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .xm1-mini small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); font-variant-numeric: tabular-nums; } .phone .xm1-mini small em { font-style: normal; font-weight: 600; color: var(--hd-success-strong); }
.phone .scr:has(.xm1-home) .tabbar { background: var(--hd-surface); }

/* ---------- drop details ---------- */
.phone .scr:has(.xm1-det) > .sbar { position: absolute; left: 0; right: 0; top: 0; z-index: 25; color: #111; }
.phone .xm1-det { flex: 1; min-height: 0; display: flex; flex-direction: column; overflow: hidden; }
.phone .xm1-det .ph { position: relative; height: 404px; flex: none; }
.phone .xm1-det .ph > img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.phone .xm1-det .ph .tb { position: absolute; top: 58px; left: 16px; right: 16px; display: flex; justify-content: space-between; z-index: 3; }
.phone .xm1-det .ph .x-disc { width: 40px; height: 40px; }
.phone .xm1-det .ph .x-dots { bottom: 40px; }
.phone .xm1-det .sh { position: relative; margin-top: -24px; border-radius: 24px 24px 0 0; background: var(--hd-surface); padding: 20px 20px 0; flex: 1; min-height: 0; display: flex; flex-direction: column; gap: 14px; }
.phone .xm1-det .xm1-t { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; }
.phone .xm1-det .by { margin: 4px 0 0; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.phone .xm1-facts { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--hd-border); border-bottom: 1px solid var(--hd-border); }
.phone .xm1-facts div { padding: 12px 0 12px 16px; border-left: 1px solid var(--hd-border); } .phone .xm1-facts div:first-child { padding-left: 0; border-left: 0; }
.phone .xm1-facts b { display: block; font-size: 17px; line-height: 22px; font-weight: 650; font-variant-numeric: tabular-nums; } .phone .xm1-facts b i { font-style: normal; font-size: 13px; font-weight: 450; color: var(--hd-fg-muted); }
.phone .xm1-facts small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .xm1-det .also { display: flex; align-items: center; gap: 14px; font-size: 14px; color: var(--hd-fg-muted); }
.phone .xm1-det .also span.p { display: inline-flex; align-items: center; gap: 6px; color: var(--hd-fg); font-weight: 520; } .phone .xm1-det .also .plat { border-radius: 4px; }
.phone .xm1-det .desc { margin: 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); } .phone .xm1-det .desc b { color: var(--hd-link); font-weight: 560; }
.phone .xm1-det .crt { display: flex; align-items: center; gap: 10px; font-size: 14px; color: var(--hd-fg-muted); } .phone .xm1-det .crt b { color: var(--hd-fg); font-weight: 600; font-variant-numeric: tabular-nums; }
.phone .xm1-bar2 { flex: none; display: flex; align-items: center; gap: 16px; padding: 12px 20px 10px; border-top: 1px solid var(--hd-border); background: var(--hd-surface); }
.phone .xm1-bar2 .e small { display: block; font-size: 13px; line-height: 16px; color: var(--hd-fg-muted); }
.phone .xm1-bar2 .e b { display: block; font-family: var(--font-brand); font-size: 22px; line-height: 26px; font-weight: 650; letter-spacing: -0.025em; font-variant-numeric: tabular-nums; }
.phone .xm1-bar2 .btn { flex: 1; height: 48px !important; }
.phone .scr:has(.xm1-det) .home-ind { background: var(--hd-surface); }
"""
