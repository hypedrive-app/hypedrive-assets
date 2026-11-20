# direction A screens layer 1
XW1 = r"""
/* shared tokens: Geist 700 tight, warm canvas, ink type */
.phone .scr:has(.xw1-home), .phone .scr:has(.xw1-det), .phone .scr:has(.xw1-otp), .phone .scr:has(.xw1-ap), .phone .scr:has(.xw1-tr) { --ink: #16181d; --mut: #7a766e; --we: rgba(16,20,38,.09); font-family: var(--font-brand); }
/* ---------- welcome ---------- */
.phone .xw1-wel .xm1-h { font-size: 50px; line-height: 50px; font-weight: 700 !important; letter-spacing: -0.02em !important; color: #fff; }

.phone .xw1-wel .xm1-p { font-size: 16px; color: rgba(255,255,255,.7); }
.phone .xw1-wel .xm1-mos img { border-radius: 18px; }
/* ---------- verify ---------- */
.phone .scr:has(.xw1-otp) { background: #f7f7f8 !important; }
.phone .xw1-otp { padding: 8px 16px 12px; gap: 20px; }
.phone .xw1-otp .xm1-h { font-size: 36px; line-height: 38px; letter-spacing: -0.02em !important; color: var(--ink); }
.phone .xw1-otp .xm1-sub { font-size: 15px; color: var(--mut); }
.phone .xw1-otp .xm1-sub b { color: var(--ink); font-weight: 600; }
.phone .xw1-otp .xm1-code { justify-content: space-between; gap: 8px; }
.phone .xw1-otp .xm1-code span { flex: 1; width: auto; max-width: 54px; height: 60px; border: 0; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px var(--we); font-size: 28px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .xw1-otp .xm1-code span.on { box-shadow: 0 0 0 2px var(--ink); }
.phone .xw1-otp .xm1-code span.on::after { background: var(--ink); }
.phone .xw1-otp .xm1-aux { flex-direction: row; justify-content: space-between; color: var(--mut); }
.phone .xw1-otp .xm1-aux .btn.link { color: var(--ink); font-weight: 600; }
.phone .scr:has(.xw1-otp) .xm1-pad { background: #efebe4; border-top: 1px solid var(--we); }
.phone .scr:has(.xw1-otp) .xm1-pad b { font-weight: 500; }
.phone .scr:has(.xw1-otp) .home-ind { background: #efebe4; }
/* ---------- home ---------- */
.phone .xw1-home { flex: 1; min-height: 0; display: flex; flex-direction: column; padding: 4px 16px 0; overflow: hidden; }
.phone .xw1-home .hd { display: flex; justify-content: space-between; align-items: flex-start; }
.phone .xw1-home .hd small { display: block; font-size: 13px; color: var(--mut); font-weight: 500; margin-bottom: 2px; }
.phone .xw1-home .hd h1 { font-size: 32px; line-height: 34px; margin: 0; color: var(--ink); letter-spacing: -0.02em !important; }
.phone .xw1-home .ico { display: flex; margin: 6px -8px 0 0; }
.phone .xw1-home .ico span { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; position: relative; color: var(--ink); }
.phone .xw1-home .bell i { position: absolute; top: 9px; right: 10px; width: 8px; height: 8px; border-radius: 50%; background: var(--hd-tone-vermilion); box-shadow: 0 0 0 2px #f7f7f8; }
.phone .xw1-home .earn { margin-top: 14px; height: 84px; border-radius: 18px; background: #16181d; color: #fff; padding: 14px 18px; display: flex; justify-content: space-between; flex: none; }
.phone .xw1-home .earn small { font-size: 13px; font-weight: 500; color: rgba(255,255,255,.62); }
.phone .xw1-home .earn b { display: block; font-size: 38px; line-height: 40px; font-weight: 700; letter-spacing: -0.02em; margin-top: 2px; }
.phone .xw1-home .earn em { font-style: normal; font-size: 14px; font-weight: 600; color: #7fe0a8; }
.phone .xw1-home .hero { position: relative; margin-top: 12px; height: 288px; border-radius: 24px; overflow: hidden; color: #fff; flex: none; }
.phone .xw1-home .hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.phone .xw1-home .hero::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(10,10,10,0) 30%, rgba(10,10,10,.82) 100%); }
.phone .xw1-home .hero .chip { position: absolute; top: 12px; left: 12px; z-index: 2; background: #fff !important; color: var(--ink) !important; font-size: 12.5px; font-weight: 600; padding: 5px 10px; border-radius: 999px; height: auto; border: 0 !important; box-shadow: none !important; line-height: 16px; }
.phone .xw1-home .hero .tx { position: absolute; z-index: 2; left: 16px; right: 16px; bottom: 14px; }
.phone .xw1-home .hero small { font-size: 13px; opacity: .85; font-weight: 500; }
.phone .xw1-home .hero h3 { font-size: 28px; line-height: 30px; font-weight: 700; letter-spacing: -0.02em; margin: 2px 0 10px; }
.phone .xw1-home .hero .mt { display: flex; justify-content: space-between; font-size: 13.5px; align-items: baseline; }
.phone .xw1-home .hero .mt b { font-size: 19px; font-weight: 700; letter-spacing: -0.02em; }
.phone .xw1-home .hero .bar { height: 3px; background: rgba(255,255,255,.3); border-radius: 2px; margin-top: 9px; }
.phone .xw1-home .hero .bar i { display: block; height: 100%; width: 70%; background: #fff; border-radius: 2px; }
.phone .xw1-home .sh { display: flex; justify-content: space-between; align-items: baseline; margin-top: 16px; }
.phone .xw1-home .sh b { font-size: 20px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .xw1-home .sh span { font-size: 13.5px; color: var(--mut); font-weight: 500; }
.phone .xw1-home .rail { display: flex; gap: 12px; margin-top: 10px; }
.phone .xw1-home .rc { flex: 1; min-width: 0; }
.phone .xw1-home .rc img { width: 100%; height: 118px; border-radius: 16px; object-fit: cover; display: block; }
.phone .xw1-home .rc b { display: block; font-size: 14.5px; font-weight: 600; letter-spacing: -0.02em; margin-top: 7px; color: var(--ink); }
.phone .xw1-home .rc small { font-size: 12.5px; color: var(--mut); }
.phone .xw1-home .rc small em { font-style: normal; color: var(--ink); font-weight: 600; }


/* ---------- detail ---------- */
.phone .scr:has(.xw1-det) > .sbar { position: absolute; left: 0; right: 0; top: 0; z-index: 25; color: #fff; }
.phone .xw1-det { flex: 1; min-height: 0; display: flex; flex-direction: column; position: relative; }
.phone .xw1-det .ph { position: absolute; top: 0; left: 0; right: 0; height: 400px; }
.phone .xw1-det .ph img { width: 100%; height: 100%; object-fit: cover; display: block; }
.phone .xw1-det .ph::after { content: ''; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,.3), rgba(0,0,0,0) 24%); }
.phone .xw1-det .disc { position: absolute; top: 52px; width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,.95); color: var(--ink); display: flex; align-items: center; justify-content: center; z-index: 5; }
.phone .xw1-det .sheet { position: relative; margin-top: 366px; flex: 1; min-height: 0; background: #f7f7f8; border-radius: 28px 28px 0 0; padding: 20px 16px 0; z-index: 2; }
.phone .xw1-det .eyebrow { font-size: 13.5px; color: var(--mut); font-weight: 500; }
.phone .xw1-det h1 { font-size: 36px; line-height: 38px; margin: 4px 0 6px; color: var(--ink); letter-spacing: -0.02em !important; }
.phone .xw1-det .sub { margin: 0; font-size: 14.5px; color: #525459; }
.phone .xw1-det .facts { display: flex; margin-top: 16px; background: #fff; border-radius: 16px; box-shadow: 0 0 0 1px var(--we); }
.phone .xw1-det .facts div { flex: 1; padding: 12px 14px; }
.phone .xw1-det .facts div + div { border-left: 1px solid var(--we); }
.phone .xw1-det .facts b { display: block; font-size: 24px; line-height: 27px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .xw1-det .facts b i { font-style: normal; font-size: 14px; color: var(--mut); font-weight: 500; letter-spacing: -0.01em; }
.phone .xw1-det .facts small { font-size: 12.5px; color: var(--mut); }
.phone .xw1-det .desc { margin: 18px 0 0; font-size: 15px; line-height: 22px; color: #3b3d42; }
.phone .xw1-det .crt { display: flex; align-items: center; gap: 10px; margin-top: 14px; font-size: 14px; color: #3b3d42; }
.phone .xw1-det .crt b { color: var(--ink); font-weight: 600; }
.phone .xw1-det .crt .x-avs { display: flex; } .phone .xw1-det .crt .x-avs img { border-radius: 50%; border: 2px solid #f7f7f8; margin-left: -8px; box-sizing: content-box; } .phone .xw1-det .crt .x-avs img:first-child { margin-left: 0; }
.phone .xw1-det .cta { position: relative; z-index: 3; flex: none; display: flex; align-items: center; gap: 16px; padding: 12px 16px 6px !important; background: #f7f7f8; border-top: 1px solid var(--we); }
.phone .xw1-det .cta small { display: block; font-size: 12.5px; color: var(--mut); }
.phone .xw1-det .cta b { font-size: 28px; line-height: 30px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .xw1-det .cta .btn { flex: 1; height: 52px; }
.phone .scr:has(.xw1-det) .home-ind { background: #f7f7f8; }
/* ---------- apply ---------- */
.phone .scr:has(.xw1-ap) .sheet { background: #f7f7f8 !important; }
.phone .scr:has(.xw1-ap) .xm2-h { font-family: var(--font-brand); font-size: 30px; line-height: 32px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .scr:has(.xw1-ap) .xm2-c { background: #fff !important; border: 0 !important; box-shadow: 0 0 0 1px var(--we); border-radius: 16px; }
.phone .scr:has(.xw1-ap) .sheet { padding: 8px 20px 36px !important; box-sizing: border-box; width: 100%; }
.phone .scr:has(.xw1-ap) .sheet > *, .phone .scr:has(.xw1-ap) .xm2-ch > * { box-sizing: border-box; width: 100%; max-width: 100%; margin-left: 0; margin-right: 0; }
.phone .scr:has(.xw1-ap) .sheet > .grab { width: 40px; max-width: 40px; margin: 0 auto 18px; }
.phone .scr:has(.xw1-ap) .xm2-c.on { box-shadow: 0 0 0 1px var(--we); }
.phone .scr:has(.xw1-ap) .xm2-c .tx b { font-weight: 600; letter-spacing: -0.02em; }
.phone .scr:has(.xw1-ap) .radio { width: 20px; height: 20px; box-sizing: border-box; border: 1.5px solid color-mix(in srgb, var(--ink) 28%, transparent) !important; background: #fff !important; box-shadow: none !important; }
.phone .scr:has(.xw1-ap) .radio.on { background: var(--hd-accent) !important; border-color: var(--hd-accent) !important; box-shadow: none !important; }
.phone .scr:has(.xw1-ap) .radio.on::after { content: ''; width: 8px; height: 8px; border-radius: 50%; background: #fff; }
.phone .scr:has(.xw1-ap) .btn.p { height: 48px !important; }
.phone .scr:has(.xw1-ap) .xm2-hint { color: var(--mut); }
/* ---------- track ---------- */
.phone .scr:has(.xw1-tr) .xm2-big { font-family: var(--font-brand); font-size: 34px; line-height: 36px; font-weight: 700; letter-spacing: -0.02em; color: var(--ink); }
.phone .scr:has(.xw1-tr) .xm2-sub { color: var(--mut); }
.phone .scr:has(.xw1-tr) .xm2-hero img { background: #fff; border-radius: 18px; box-shadow: 0 0 0 1px var(--we); padding: 6px; box-sizing: border-box; width: 76px; height: 76px; object-fit: contain; }
.phone .scr:has(.xw1-tr) .xm2-c, .phone .scr:has(.xw1-tr) .xy-due { background: #fff; border: 0 !important; box-shadow: 0 0 0 1px var(--we); border-radius: 16px; }
.phone .scr:has(.xw1-tr) .xy-due { padding: 12px 14px; color: var(--ink); }
.phone .scr:has(.xw1-tr) .x-tl .s.done .k i { background: var(--ink); border-color: var(--ink); }
.phone .scr:has(.xw1-tr) .x-tl .s.done .k em { background: var(--ink); }
.phone .scr:has(.xw1-tr) .x-tl .s.now .k i { border-color: var(--ink); }
.phone .scr:has(.xw1-tr) .x-tl .s.now .k i::after { background: var(--ink); }

"""
