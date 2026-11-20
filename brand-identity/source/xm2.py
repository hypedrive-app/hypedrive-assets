# mobile screens redesign layer 2: apply / track / review / wallet. Every selector is scoped to .scr:has(.xm2m[data-s=...]).
XM2 = r"""
.xm2m { display: none; }
.scr:has(.xm2m) { background: var(--hd-surface); }
.scr:has(.xm2m) .body { background: var(--hd-surface); padding: 4px 20px 20px; gap: 20px; }
.scr:has(.xm2m) .topbar { background: var(--hd-surface); }
.scr:has(.xm2m) .cta { background: var(--hd-surface); border-top: 1px solid var(--hd-edge); padding: 12px 20px 8px !important; }
.scr:has(.xm2m) .cta .btn, .scr:has(.xm2m[data-s=apply]) .sheet .btn.p { height: 48px !important; min-height: 0; border-radius: 12px; font-size: 15px; }
.scr:has(.xm2m) .tabbar { background: var(--hd-surface); border-top: 1px solid var(--hd-edge); }

/* shared bits */
.scr:has(.xm2m) .xm2-h { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 650; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; color: var(--hd-fg); }
.scr:has(.xm2m) .xm2-sub { display: block; margin-top: 4px; font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); }
.scr:has(.xm2m) .xm2-c { display: flex; align-items: center; gap: 12px; min-height: 56px; padding: 10px 14px; box-sizing: border-box; background: var(--hd-surface); border: 1px solid var(--hd-edge); border-radius: 14px; box-shadow: none; }
.scr:has(.xm2m) .xm2-c .tx { flex: 1; min-width: 0; }
.scr:has(.xm2m) .xm2-c .tx b { display: block; font-size: 15px; line-height: 20px; font-weight: 600; letter-spacing: 0; color: var(--hd-fg); }
.scr:has(.xm2m) .xm2-c .tx small { display: block; margin-top: 1px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }

/* apply */
.scr:has(.xm2m[data-s=apply]) .sheet { padding: 8px 20px 36px; display: flex; flex-direction: column; gap: 0; }
.scr:has(.xm2m[data-s=apply]) .sheet .grab { margin: 0 auto 18px; }
.scr:has(.xm2m[data-s=apply]) .xm2-h { font-size: 26px; line-height: 30px; margin-bottom: 16px; }
.scr:has(.xm2m[data-s=apply]) .xm2-ch { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }
.scr:has(.xm2m[data-s=apply]) .xm2-c.on { background: var(--hd-accent-subtle); border-color: transparent; }
.scr:has(.xm2m[data-s=apply]) .xm2-c.on .tx small { color: var(--hd-fg-muted); }
.scr:has(.xm2m[data-s=apply]) .xm2-ship { margin-bottom: 20px; }
.scr:has(.xm2m[data-s=apply]) .xm2-ship > .ic { color: var(--hd-fg-muted); flex: none; }
.scr:has(.xm2m[data-s=apply]) .xm2-ship > .ic:last-child { color: var(--hd-fg-subtle); }
.scr:has(.xm2m[data-s=apply]) .xm2-hint { display: block; margin-top: 12px; text-align: center; font-size: 13px; line-height: 18px; color: var(--hd-fg-subtle); }

/* track */
.scr:has(.xm2m[data-s=track]) .body { gap: 32px; padding-top: 12px; }
.scr:has(.xm2m[data-s=track]) .xm2-hero { display: flex; align-items: center; justify-content: space-between; gap: 16px; }
.scr:has(.xm2m[data-s=track]) .xm2-big { font-family: var(--font-brand); font-size: 32px; line-height: 36px; font-weight: 650; letter-spacing: -0.03em; font-variation-settings: 'opsz' 96; }
.scr:has(.xm2m[data-s=track]) .xm2-sub { margin-top: 6px; }
.scr:has(.xm2m[data-s=track]) .xm2-hero img { width: 88px; height: 88px; object-fit: contain; flex: none; margin: -8px -4px -8px 0; }
.scr:has(.xm2m[data-s=track]) .x-tl .tx { padding-bottom: 28px; }
.scr:has(.xm2m[data-s=track]) .x-tl .s:last-child .tx { padding-bottom: 0; }
.scr:has(.xm2m[data-s=track]) .xm2-cour .btn { width: 40px; height: 40px; min-height: 0; padding: 0; border-radius: 10px; flex: none; }
.scr:has(.xm2m[data-s=track]) .xm2-cour .av { flex: none; }
.scr:has(.xm2m[data-s=track]) .xm2-tip { display: flex; gap: 8px; align-items: flex-start; margin: -4px 0 0; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.scr:has(.xm2m[data-s=track]) .xm2-tip .icf { flex: none; color: var(--hd-fg-subtle); width: 16px; height: 16px; margin-top: 1px; }

/* review */
.scr:has(.xm2m[data-s=review]) .body { gap: 24px; }
.scr:has(.xm2m[data-s=review]) .field { gap: 8px; }
.scr:has(.xm2m[data-s=review]) .field > label { font-size: 13.5px; font-weight: 600; color: var(--hd-fg); }
.scr:has(.xm2m[data-s=review]) .stars { gap: 8px; }
.scr:has(.xm2m[data-s=review]) .xm2-phs { display: flex; gap: 10px; }
.scr:has(.xm2m[data-s=review]) .xm2-ph { position: relative; width: 72px; height: 72px; flex: none; }
.scr:has(.xm2m[data-s=review]) .xm2-ph img { width: 72px; height: 72px; object-fit: cover; border-radius: 12px; display: block; }
.scr:has(.xm2m[data-s=review]) .xm2-ph span { position: absolute; top: 4px; right: 4px; width: 20px; height: 20px; border-radius: 50%; background: var(--hd-surface); color: var(--hd-fg); display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 2px rgba(16,20,38,.28); }
.scr:has(.xm2m[data-s=review]) .xm2-add { width: 72px; height: 72px; border-radius: 12px; border: 1px solid var(--hd-edge); background: var(--hd-surface); color: var(--hd-fg-muted); display: flex; align-items: center; justify-content: center; box-sizing: border-box; flex: none; }
.scr:has(.xm2m[data-s=review]) .input { height: 44px; box-sizing: border-box; border: 1px solid var(--hd-edge); background: var(--hd-surface); box-shadow: none; border-radius: 12px; }
.scr:has(.xm2m[data-s=review]) .input.textarea { height: auto; min-height: 104px; padding: 12px 14px; font-size: 15px; line-height: 22px; align-items: flex-start; }
.scr:has(.xm2m[data-s=review]) .xm2-cnt { display: block; text-align: right; font-size: 13px; color: var(--hd-fg-subtle); font-variant-numeric: tabular-nums; }

/* wallet */
.scr:has(.xm2m[data-s=wallet]) .body { gap: 16px; padding-top: 4px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-wh { border-radius: 20px; background: var(--hd-inverse); color: var(--hd-inverse-fg); padding: 20px; display: flex; flex-direction: column; gap: 4px; }
.scr[data-theme="dark"]:has(.xm2m[data-s=wallet]) .xm2-wh { background: var(--hd-surface-raised); color: var(--hd-fg); border: 1px solid var(--hd-edge); padding: 19px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-wh small { font-size: 13px; line-height: 18px; color: color-mix(in oklab, currentColor 66%, transparent); }
.scr:has(.xm2m[data-s=wallet]) .xm2-wr { display: flex; align-items: center; justify-content: space-between; gap: 12px; margin: 2px 0 6px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-wb { font-family: var(--font-brand); font-size: 44px; line-height: 48px; font-weight: 650; letter-spacing: -0.04em; } .scr:has(.xm2m[data-s=wallet]) .xm2-wb span { font-weight: 500; margin-right: 1px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-wr .btn { height: 44px; min-height: 0; padding: 0 20px; flex: none; }
.scr:has(.xm2m[data-s=wallet]) .xm2-earn { padding: 12px 16px; gap: 16px; min-height: 68px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-earn > div:first-child { flex: none; }
.scr:has(.xm2m[data-s=wallet]) .xm2-earn small { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.scr:has(.xm2m[data-s=wallet]) .xm2-earn b { display: block; font-family: var(--font-brand); font-size: 24px; line-height: 30px; font-weight: 650; letter-spacing: -0.02em; }
.scr:has(.xm2m[data-s=wallet]) .xm2-sp { position: relative; flex: 1; min-width: 0; height: 36px; margin-right: 6px; } .scr:has(.xm2m[data-s=wallet]) .xm2-sp svg { display: block; height: 36px; width: 100%; }
.scr:has(.xm2m[data-s=wallet]) .xm2-earn em { font-style: normal; font-size: 13px; font-weight: 600; color: var(--hd-success-strong); flex: none; align-self: flex-start; margin-top: 6px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-ah { display: flex; align-items: center; justify-content: space-between; margin-top: 4px; margin-bottom: -6px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-ah b { font-size: 17px; font-weight: 650; }
.scr:has(.xm2m[data-s=wallet]) .xm2-list { display: flex; flex-direction: column; gap: 8px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-tx { min-height: 60px; padding: 10px 14px 10px 10px; }
.scr:has(.xm2m[data-s=wallet]) .xm2-tx img.lead { width: 40px; height: 40px; object-fit: contain; flex: none; border-radius: 0; }
.scr:has(.xm2m[data-s=wallet]) .xm2-tx .x-tile { width: 40px; height: 40px; flex: none; }
.scr:has(.xm2m[data-s=wallet]) .xm2-tx .w-amt { font-size: 15px; font-weight: 600; flex: none; }
"""
