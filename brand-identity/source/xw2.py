# direction A screens layer 2 (screens 7-12): type + colour only
XW2 = r"""
.w2m { display: none; }
/* ink = #16181d; display = Geist 700 tight */
.phone .scr:has(.w2m) { --ink: #16181d; }
.phone .scr:has(.w2m) .xm2-h, .phone .scr:has(.w2m) .xm3-h, .phone .scr:has(.w2m) .xm3-nil h2, .phone .scr:has(.w2m) .x-page, .phone .scr:has(.w2m) .xm2-earn b {
  font-family: var(--font-brand) !important; font-weight: 700 !important; letter-spacing: -0.02em !important; font-variation-settings: normal !important; }
.phone .scr:has(.w2m) .xm2-h { font-size: 28px; }
.phone .scr:has(.w2m) .xm3-h { font-size: 34px; line-height: 38px; letter-spacing: -0.02em !important; }
.phone .scr:has(.w2m) .x-page { font-size: 30px; }
/* white cards on warm, warm hairline */
.phone .scr:has(.w2m) .input, .phone .scr:has(.w2m) .xm2-add, .phone .scr:has(.w2m) .xm2-c, .phone .scr:has(.w2m) .xy-pay, .phone .scr:has(.w2m) .xm3-lr, .phone .scr:has(.w2m) .xm3-chips span, .phone .scr:has(.w2m) .search { background: #fff; border-color: var(--warm-edge); }
.phone .scr:has(.w2m) .xm3-nr { background: #fff; border: 1px solid var(--warm-edge); border-radius: 16px; height: 68px; padding: 0 14px 0 12px; margin-bottom: 8px; box-sizing: border-box; }
.phone .scr:has(.w2m) .xm3-ne { align-self: center; padding-top: 0; }
.phone .scr:has(.w2m) .xm3-nt p b { font-weight: 700; }
.phone .scr:has(.w2m) .xm3-nl { gap: 0; }
.phone .scr:has(.w2m) .searchbar .search.foc, .phone .scr:has(.w2m) .search.foc, .phone .scr:has(.w2m) .search { border: 1px solid rgba(40,30,20,.30) !important; box-shadow: none !important; outline: 0; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-nt p { font-size: 14px; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-ne i { margin-left: -2px; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-ne { font-size: 12px; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-nr { gap: 10px; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-ne { gap: 6px; }
/* the one ink block */
.phone .scr:has(.w2m[data-w=wallet]) .xm2-wh { background: #16181d; border-radius: 20px; }
.phone .scr:has(.w2m[data-w=wallet]) .xm2-wb { font-family: var(--font-brand); font-weight: 700; letter-spacing: -0.02em; font-size: 48px; }
.phone .scr:has(.w2m[data-w=wallet]) .xm2-ah b { font-weight: 700; letter-spacing: -0.02em; }
.phone .scr:has(.w2m[data-w=review]) .stars { gap: 8px; }
.phone .scr:has(.w2m[data-w=success]) .xy-pay b .num { font-weight: 700; }
.phone .scr:has(.w2m[data-w=success]) .xm3-succ img { width: 176px; }
/* profile: dark surface everywhere, white display type */
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) { background: #0f1014 !important; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .tabbar { background: #0f1014 !important; border-top: 1px solid rgba(255,255,255,.10) !important; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xz-ptop .ttl { color: #fff !important; font-size: 30px !important; letter-spacing: -0.02em !important; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xz-ptop { color: #fff; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xm3-nm { letter-spacing: -0.02em !important; font-size: 18px !important; color: #fff; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xm3-stats b { font-family: var(--font-brand); font-weight: 700 !important; letter-spacing: -0.02em; font-size: 20px !important; }
.phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xm3-grp, .phone .scr[data-theme="dark"]:has(.w2m[data-w=profile]) .xz-idc { border-color: rgba(255,255,255,.12) !important; }
:root:root:root:root .phone .scr:has(.w2m) .searchbar .search.foc { border: 1px solid rgba(40,30,20,.30) !important; }
.phone .scr:has(.w2m[data-w=notifs]) .xm3-nt p { font-size: 13.5px; }

.phone .scr:has(.w2m[data-w=empty]) .xm3-lr { height: 64px; padding: 0 16px; gap: 12px; box-sizing: border-box; }
.phone .scr:has(.w2m[data-w=empty]) .xm3-lr img { width: 48px; height: 48px; border-radius: 10px; border: 1px solid rgba(40,30,20,.14); box-sizing: border-box; object-fit: cover; }
.phone .scr:has(.w2m[data-w=empty]) .xm3-ll { gap: 8px; }
.phone .scr:has(.w2m[data-w=empty]) .xm3-lt b { font-size: 15px; font-weight: 600; }
.phone .scr:has(.w2m[data-w=empty]) .xm3-lt small { font-size: 13px; color: var(--hd-fg-muted); }
.phone .scr:has(.w2m[data-w=empty]) .w2-ea { text-align: right; flex: none; }
.phone .scr:has(.w2m[data-w=empty]) .w2-ea small { display: block; font-size: 11.5px; line-height: 14px; color: var(--hd-fg-muted); }
.phone .scr:has(.w2m[data-w=empty]) .w2-ea b { display: block; font-size: 15px; line-height: 20px; font-weight: 650; color: var(--hd-fg); }
.phone .scr:has(.w2m[data-w=empty]) .xm3-chips { padding-left: 0; }
.phone .scr:has(.w2m[data-w=empty]) .xm3-nil .btn { height: 44px; min-height: 0; padding: 0 18px; border-radius: 12px; font-size: 15px; }
.phone .scr:has(.w2m[data-w=empty]) .search .clr { background: transparent !important; color: var(--hd-fg-subtle) !important; box-shadow: none !important; width: 20px; height: 20px; }
"""
