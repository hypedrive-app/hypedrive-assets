XY = r"""
/* ===== xy: mobile screens review pass (loads before xz). :root:root:root beats the xs snap layer ===== */
/* 16px screen padding, everywhere */
:root:root:root .phone .xm1-bar { padding: 0 16px !important; }
:root:root:root .phone .xm1-wel { padding-left: 16px; padding-right: 16px; }
:root:root:root .phone .xm1-otp { padding: 8px 16px 12px; gap: 24px; }
:root:root:root .phone .xm1-head { padding-left: 16px; padding-right: 16px; }
:root:root:root .phone .xm1-home .tabs { margin: 12px 16px 0; }
:root:root:root .phone .xm1-card { margin: 16px 16px 0; }
:root:root:root .phone .xm1-sech { padding: 24px 16px 12px; }
:root:root:root .phone .xm1-two { padding: 0 16px; }
:root:root:root .phone .xm1-det .sh { padding: 20px 16px 0; gap: 16px; }
:root:root:root .phone .xm1-bar2 { padding: 12px 16px 10px; }
.scr:has(.xm2m) .body { padding-left: 16px !important; padding-right: 16px !important; }
.scr:has(.xm2m) .cta { padding: 12px 16px 8px !important; }
.scr:has(.xm2m[data-s=apply]) .sheet { padding-left: 16px; padding-right: 16px; }
.scr:has(.xm3-s) .body { padding-left: 16px; padding-right: 16px; }
:root:root:root .xm3-cta { padding: 12px 16px 8px !important; }

/* 1 welcome: stronger top scrim so the wordmark reads */
:root:root:root .phone .xm1-wel .xm1-fade { background: linear-gradient(180deg, rgba(13,14,18,.96) 0px, rgba(13,14,18,.78) 56px, rgba(13,14,18,.30) 104px, rgba(13,14,18,0) 150px, rgba(13,14,18,0) 250px, rgba(13,14,18,.86) 400px, #0d0e12 480px) !important; }
:root:root:root .phone .xm1-wel .xm1-p { font-size: 15px !important; line-height: 22px !important; }

/* 2 verify: Verify sits 24 under the resend line, keypad docked */
:root:root:root .phone .xm1-otp .xy-verify { height: 48px !important; margin: 0; flex: none; }
:root:root:root .phone .xm1-code { gap: 8px; }
:root:root:root .phone .xm1-code span { width: 48px; height: 48px; }

/* 4 drop details */
:root:root:root .phone .xm1-facts b { font-size: 17px !important; font-weight: 650 !important; }
:root:root:root .phone .xm1-facts b i { font-size: 13px; }
:root:root:root .phone .xm1-facts div > small { font-size: 12.5px !important; line-height: 18px; color: var(--hd-fg-muted); }
:root:root:root .phone .xm1-det .also { font-size: 13.5px; }
:root:root:root .phone .xm1-det .crt { font-size: 13.5px; }
:root:root:root .phone .xm1-det .desc { font-size: 15px; line-height: 22px; }

/* 5 apply: clean scrim over the photo */
:root:root:root .phone .scr:has(.xm2m[data-s=apply]) .scrim { background: rgba(10,12,18,.40) !important; }

/* 6 tracking: bare 56 thumb in the title row, 52 per step, review-due row */
:root:root:root .scr:has(.xm2m[data-s=track]) .body { gap: 24px; padding-top: 8px; }
:root:root:root .scr:has(.xm2m[data-s=track]) .xm2-hero { justify-content: flex-start; gap: 14px; }
:root:root:root .scr:has(.xm2m[data-s=track]) .xm2-hero img { width: 56px; height: 56px; margin: 0; border-radius: 0; }
:root:root:root .scr:has(.xm2m[data-s=track]) .xm2-big { font-size: 28px; line-height: 32px; font-weight: 700 !important; }
:root:root:root .scr:has(.xm2m[data-s=track]) .xm2-sub { margin-top: 2px; font-size: 13.5px !important; }
:root:root:root .scr:has(.xm2m[data-s=track]) .x-tl .s { min-height: 52px; }
:root:root:root .scr:has(.xm2m[data-s=track]) .x-tl .tx { padding-bottom: 14px; }
:root:root:root .scr:has(.xm2m[data-s=track]) .x-tl .s:last-child { min-height: 0; }
.xy-due { display: flex; align-items: center; gap: 10px; font-size: 13.5px; line-height: 20px; color: var(--hd-fg-muted); }
.xy-due .ic { color: var(--hd-fg-subtle); flex: none; }
:root:root:root .scr:has(.xm2m[data-s=track]) .xm2-tip { margin: -8px 0 0; }

/* 7 submit review: bigger text */
:root:root:root .scr:has(.xm2m[data-s=review]) .field > label { font-size: 14px !important; font-weight: 600 !important; }
:root:root:root .scr:has(.xm2m[data-s=review]) .input, :root:root:root .scr:has(.xm2m[data-s=review]) .input .t-body { font-size: 15px !important; }
:root:root:root .scr:has(.xm2m[data-s=review]) .input.textarea { min-height: 120px; line-height: 22px; }
:root:root:root .scr:has(.xm2m[data-s=review]) .body { gap: 24px; }
:root:root:root .scr:has(.xm2m[data-s=review]) .xm2-h { font-weight: 700 !important; }

/* 8 wallet: calmer ink hero */
:root:root:root .scr:has(.xm2m[data-s=wallet]) .xm2-wh { padding: 20px; }
:root:root:root .scr:has(.xm2m[data-s=wallet]) .xm2-wb { font-size: 36px; line-height: 40px; }
:root:root:root .scr:has(.xm2m[data-s=wallet]) .xm2-wr .btn { height: 40px !important; }
:root:root:root .scr:has(.xm2m[data-s=wallet]) .xm2-wr { margin: 0 0 4px; }
:root:root:root .scr:has(.xm2m[data-s=wallet]) .body { gap: 24px; }
:root:root:root .scr:has(.xm2m[data-s=wallet]) .xm2-ah { margin: 0 0 -12px; }

/* 9 success: illustration, headline, compact payout card, actions at the bottom */
:root:root:root .xm3-succ { justify-content: center; padding-top: 0; padding-bottom: 96px; gap: 0; }
:root:root:root .xm3-succ img { width: 160px; margin-bottom: 24px; }
:root:root:root h1.xm3-h { font-size: 30px; line-height: 36px; font-weight: 700 !important; }
.xy-pay { margin-top: 28px; align-self: stretch; display: flex; align-items: center; gap: 12px; text-align: left; min-height: 64px; padding: 10px 14px 10px 10px; box-sizing: border-box; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; }
[data-theme="dark"] .xy-pay { background: var(--hd-surface-raised); }
.xy-pay .x-tile { width: 40px; height: 40px; flex: none; display: inline-grid; place-items: center; }
.xy-pay .tx { flex: 1; min-width: 0; }
.xy-pay .tx b { display: block; font-size: 15px; line-height: 20px; font-weight: 600; color: var(--hd-fg); }
:root:root:root .xy-pay .tx b .num { font-weight: 650; }
.xy-pay .tx small { display: block; margin-top: 1px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
:root:root:root .xm3-cta { margin-top: auto; border-top: 1px solid var(--hd-edge) !important; }

/* 12 empty search: one accent edge, no ring */
:root:root:root .phone .searchbar .search.foc { border: 1px solid var(--hd-accent) !important; box-shadow: none !important; outline: 0 !important; }
:root:root:root .xm3-chips span { height: 36px; }
.scr:has(.xm2m) .btn.link { text-decoration: none; font-weight: 560; }
"""
