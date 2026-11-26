# c6 layer (rollout of the v5 white language, 2026-11-26)
XC6 = """
.phone .c6-fg { color: var(--hd-fg); font-weight: 600; }
.phone .c6-lk { font-size: 15px; font-weight: 600; color: var(--hd-link) !important; }
.phone .w5-sh span.c6-lk { font-size: 14.5px; }
.phone .c6-amt { font-size: 15px; font-weight: 600; flex: none; color: var(--hd-fg); font-variant-numeric: tabular-nums; }
.phone .c6-amt.in { color: var(--hd-success-strong); }
.phone .c6-dl { margin: 2px 0 0; display: grid; grid-template-columns: 1fr auto; row-gap: 6px; font-size: 14px; line-height: 20px; padding: 0 2px; }
.phone .c6-dl dt { color: var(--hd-fg-muted); } .phone .c6-dl dd { margin: 0; text-align: right; font-variant-numeric: tabular-nums; }
.phone .c6-dl dd.in { color: var(--hd-success-strong); font-weight: 600; }
.phone .w5-sum img.plat, .phone .c6-dl img.plat, .phone .w5-row small img.plat { width: 13px; height: 13px; border-radius: 3px; vertical-align: -2px; margin-right: 4px; }
.phone .w5-row small img.plat { width: 13px !important; height: 13px !important; }
.phone .w5-row small { display: block; }
/* welcome */
.phone .c6-wel { padding-top: 14px; }
.phone .c6-logo { height: 30px; width: auto; align-self: flex-start; margin-top: 8px; }
.phone .c6-mos { position: relative; height: 380px; margin-top: 22px; }
.phone .c6-mos img { position: absolute; object-fit: cover; border-radius: 22px; display: block; }
.phone .c6-mos .a { left: 0; top: 0; width: 214px; height: 380px; }
.phone .c6-mos .b { right: 0; top: 0; width: 130px; height: 184px; }
.phone .c6-mos .c { right: 0; top: 196px; width: 130px; height: 184px; }
.phone .c6-wh { margin-top: 26px; font-size: 38px; line-height: 42px; }
.phone .c6-wb { border-top: 0; display: flex; flex-direction: column; gap: 6px; padding-bottom: 26px; }
/* otp */
.phone .c6-otp { padding-top: 8px; }
.phone .c6-code { margin-top: 28px; display: flex; justify-content: space-between; }
.phone .c6-aux { display: flex; flex-direction: column; align-items: center; gap: 2px; margin-top: 22px; font-size: 14px; color: var(--hd-fg-muted); }
.phone .c6-otp ~ .w5-bb { border-top: 0; }
/* campaign */
.phone .c6-det { padding: 0 16px 14px; }
.phone .c6-hero { position: relative; margin: 0 -16px; height: 250px; flex: none; }
.phone .c6-hero > img { width: 100%; height: 250px; object-fit: cover; display: block; }
.phone .c6-hero .tb { position: absolute; left: 12px; right: 12px; top: 40px; display: flex; justify-content: space-between; }
.phone .c6-tbr { display: flex; gap: 10px; }
.phone .c6-by { display: flex; align-items: center; gap: 6px; margin-top: 16px; font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .c6-by img.plat { width: 14px; height: 14px; border-radius: 3px; }
.phone .c6-det .w5-h1 { margin-top: 4px; font-size: 28px; line-height: 32px; }
.phone .c6-det .w5-sum { margin-top: 18px; padding-top: 14px; }
.phone .c6-det .w5-sum > b { font-size: 32px; line-height: 38px; }
.phone .c6-det .w5-sum dl { margin-top: 8px; row-gap: 5px; }
.phone .c6-det .w5-sh { margin: 20px 0 10px; }
.phone .c6-det .w5-row { padding-top: 10px; padding-bottom: 10px; }
.phone .c6-det .w5-row + .w5-row { margin-top: 8px; }
/* sheets */
.phone .sheet.c6-sh { gap: 12px; padding-bottom: 26px; }
.phone .c6-sh .w5-row > img { width: 48px; height: 48px; }
.phone .c6-hold { display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--hd-fg-muted); padding: 0 2px; }
.phone .c6-hold svg { color: var(--hd-accent); flex: none; } .phone .c6-hold span { flex: 1; } .phone .c6-hold b { color: var(--hd-fg); font-weight: 600; }
.phone .c6-bn { display: inline-flex; align-items: center; gap: 6px; }
.phone .c6-ok { display: flex; align-items: center; gap: 10px; padding: 2px 2px; }
.phone .c6-ok .tx, .phone .c6-ok > div { display: flex; flex-direction: column; }
.phone .c6-ok b { font-size: 14.5px; font-weight: 600; color: var(--hd-success-strong); } .phone .c6-ok small { font-size: 13px; color: var(--hd-fg-muted); }
.phone .c6-ok svg { color: var(--hd-success-strong); flex: none; }
.phone .c6-sh .w5-lk { font-size: 14.5px; }
/* submit */
.phone .c6-saved { font-size: 14px; color: var(--hd-fg-muted); }
.phone .c6-tks { display: flex; flex-direction: column; gap: 14px; margin-top: 18px; }
.phone .c6-tk { border: 1px solid var(--hd-edge); border-radius: 16px; padding: 14px; display: flex; flex-direction: column; gap: 12px; }
.phone .c6-tk > * { flex: none; }
.phone .c6-th { display: flex; align-items: center; gap: 12px; }
.phone .c6-th .tx { display: flex; flex-direction: column; gap: 1px; } .phone .c6-th b { font-size: 15.5px; font-weight: 600; } .phone .c6-th small { font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .c6-f { margin-top: 0 !important; gap: 6px !important; }
.phone .c6-in { height: 44px !important; border-radius: 12px !important; justify-content: flex-start !important; gap: 8px; font-size: 14.5px !important; }
.phone .c6-in svg { color: var(--hd-fg-muted); flex: none; } .phone .c6-in em { font-style: normal; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.phone .c6-fl > span { display: block; font-size: 13.5px; font-weight: 600; margin-bottom: 6px; }
.phone .c6-shots { display: flex; gap: 8px; }
.phone .c6-sh1 { position: relative; width: 56px; height: 56px; border-radius: 12px; flex: none; }
.phone .c6-sh1 img { width: 56px; height: 56px; border-radius: 12px; object-fit: cover; display: block; }
.phone .c6-sh1 i { position: absolute; right: -5px; top: -5px; width: 18px; height: 18px; border-radius: 50%; background: var(--hd-fg); color: var(--hd-surface); display: grid; place-items: center; }
.phone .c6-add { width: 56px; height: 56px; border-radius: 12px; border: 1px dashed var(--hd-border-strong); display: grid; place-items: center; color: var(--hd-fg-muted); flex: none; }
.phone .c6-sub .w5-lead { margin-top: 4px; }
.phone .c6-sub { padding-bottom: 8px; }
/* wallet */
.phone .c6-bal { margin-top: 6px; border-top: 0; padding-top: 0; }
.phone .c6-bal .btn { margin-top: 16px; } .phone .c6-bal p { text-align: center; margin-top: 8px; }
.phone .c6-wal .w5-sh { margin: 24px 0 10px; }
.phone .c6-wal .w5-row > img, .phone .c6-inb .w5-row > img, .phone .c6-wal .w5-row > .x-tile { width: 44px; height: 44px; }
.phone .c6-wal .w5-row > img { border-radius: 10px; }
/* success */
.phone .c6-ok1 { align-items: stretch; }
.phone .c6-ill { width: 196px; height: 196px; align-self: center; margin: 24px 0 6px; display: block; }
.phone .c6-ok1 .w5-h1, .phone .c6-ok1 .w5-lead { text-align: center; }
.phone .c6-ok1 .w5-lead { margin: 8px 8px 22px; }
.phone .c6-bk { margin-top: 4px; }
.phone .c6-wel ~ .w5-bb .btn, .phone .c6-ok1 ~ .w5-bb .btn { flex: none; }
.phone .c6-ok1 ~ .w5-bb { display: flex; flex-direction: column; gap: 6px; border-top: 0; }
/* inbox */
.phone .c6-dot { width: 8px; height: 8px; border-radius: 50%; flex: none; background: transparent; }
.phone .c6-dot.on { background: var(--hd-accent); }
.phone .c6-inb .w5-sh { margin: 22px 0 10px; }
.phone .c6-inb .w5-tabs + .w5-sh { margin-top: 18px; }
/* empty */
.phone .c6-em { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 18px 12px 0; }
.phone .c6-em img { width: 120px; height: 120px; }
.phone .c6-em b { font-family: var(--font-brand); font-size: 22px; line-height: 28px; font-weight: 700; margin-top: 10px; }
.phone .c6-em p { margin: 6px 0 0; font-size: 14.5px; line-height: 21px; color: var(--hd-fg-muted); }
.phone .c6-emp .w5-sh { margin: 28px 0 10px; }
.phone .scr:has(.c6-emp) .searchbar { background: var(--hd-surface); }
/* withdraw */
.phone .c6-ill2 { width: 150px; height: 150px; margin: 14px 0 0; }
.phone .c6-wd .w5-sum { margin-top: 10px; align-items: flex-start; }
.phone .c6-wd .w5-sum dl { width: 100%; }
.phone .c6-wd .w5-sh { margin: 22px 0 10px; }
/* settings */
.phone .c6-set .w5-h1 { margin-bottom: 16px; }
.phone .c6-me > img { width: 52px; height: 52px; border-radius: 50%; }
.phone .c6-gh { margin: 20px 0 8px; } .phone .c6-gh h2 { font-size: 15px; line-height: 20px; color: var(--hd-fg-muted); font-weight: 600; font-family: var(--font-ui); letter-spacing: 0; }
.phone .c6-grp { border: 1px solid var(--hd-edge); border-radius: 16px; background: var(--hd-surface); }
.phone .c6-sr { display: flex; align-items: center; gap: 14px; height: 50px; padding: 0 14px; color: var(--hd-fg); }
.phone .c6-sr + .c6-sr { border-top: 1px solid var(--hd-edge); }
.phone .c6-sr svg { flex: none; } .phone .c6-sr > svg:first-child { color: var(--hd-fg-muted); } .phone .c6-sr > svg:last-child { color: var(--hd-fg-subtle); }
.phone .c6-sr b { flex: 1; font-size: 15.5px; font-weight: 600; }
.phone .c6-sr span { font-size: 14px; color: var(--hd-fg-muted); } .phone .c6-sr span.warn { color: var(--hd-warning-strong); font-weight: 600; }
/* barter */
.phone .c6-bar .w5-prod { margin-top: 4px; }
.phone .c6-bar .w5-h1 { font-size: 28px; line-height: 32px; margin-top: 18px; }
.phone .c6-bar .w5-steps { margin-top: 18px; }
.phone .c6-ill3 { width: 96px; height: 96px; margin: 8px 0 0; }
.phone .c6-bar .w5-sh { margin: 18px 0 8px; }
.phone .c6-dl2 { row-gap: 8px; } .phone .c6-dl2 dd { max-width: 210px; }
.phone .w5-row small img.plat { display: inline-block !important; }
.phone .c6-tabs { gap: 12px; } .phone .c6-tabs > span { font-size: 14px; gap: 5px; }
.phone .c6-hero { height: 236px; margin-top: 0; }
.phone .c6-hero > img { height: 236px; }
.phone .c6-hero .tb { top: 12px; }
.phone .c6-det .w5-sum p { display: none; }
.phone .c6-sub .c6-tk { padding: 12px; gap: 10px; }
.phone .c6-sub .c6-tks { margin-top: 14px; gap: 12px; }
.phone .c6-sh1, .phone .c6-sh1 img, .phone .c6-add { width: 52px; height: 52px; }
.phone .sheet.c6-sh { gap: 10px; padding-bottom: 36px; }
.phone .c6-mos { height: 340px; } .phone .c6-mos .a { height: 340px; } .phone .c6-mos .b, .phone .c6-mos .c { height: 164px; } .phone .c6-mos .c { top: 176px; }
.phone .c6-ill2 { width: 170px; height: 170px; }
.phone .c6-vb { margin-top: 26px; }
.phone .c6-auto { margin: 14px 0 0; text-align: center; font-size: 13.5px; color: var(--hd-fg-muted); }
.phone .c6-otp .c6-auto { text-align: left; margin-top: 12px; }
.phone .c6-aux2 { display: flex; justify-content: space-between; align-items: center; margin-top: 18px; font-size: 14px; color: var(--hd-fg-muted); }
.phone .c6-shc { position: absolute; inset: 0; border-radius: 12px; overflow: hidden; }
.phone .c6-shc > img { width: 100%; height: 100%; object-fit: cover; display: block; }
"""
