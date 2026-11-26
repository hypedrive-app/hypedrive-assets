# Enroll sheet mockup: the real creator online_purchase flow (packages/ui/src/enroll-flow + apps/creator enroll-dialog),
# drawn in the current kit (white canvas, Bricolage headings, Geist UI, cobalt primary, no tints).
import os
import kit_build as K
from kit_build import phone, ic, ics, icf, PH, plat, html

OUT = K.OUT

EN = r"""
.en-wrap { display:flex; flex-wrap:wrap; gap:36px; padding:40px; align-items:flex-start; }
.phone .scr .en-under { position:absolute; inset:0; }
.phone .scr .en-under img { width:100%; height:100%; object-fit:cover; display:block; }
.phone .scr .en-scrim { position:absolute; inset:0; background:rgba(10,12,18,.5); }
.phone .scr .home-ind { position:relative; z-index:5; }
.phone .scr .en-sheet { position:absolute; left:0; right:0; bottom:0; background:var(--hd-surface); border-radius:24px 24px 0 0;
  padding:8px 20px 34px; display:flex; flex-direction:column; gap:20px; box-shadow:0 -1px 0 var(--hd-edge); }
.en-grab { width:36px; height:5px; border-radius:3px; background:var(--hd-track-strong, #d4d6dc); margin:0 auto 2px; }
.en-head { display:flex; align-items:center; gap:10px; min-height:28px; }
.en-head .t { flex:1; font:600 13px/1.2 var(--font-ui); color:var(--hd-fg-muted); }
.en-head .x { width:28px; height:28px; display:grid; place-items:center; color:var(--hd-fg-muted); }
.en-prog { display:flex; gap:4px; }
.en-prog i { width:22px; height:4px; border-radius:2px; background:var(--hd-track, #e6e7eb); }
.en-prog i.on { background:var(--hd-accent); }
.en-h { font:700 24px/1.15 var(--font-brand); letter-spacing:-.01em; color:var(--hd-fg); margin:0; text-wrap:balance; }
.en-d { font:400 14px/1.45 var(--font-ui); color:var(--hd-fg-muted); margin:6px 0 0; }
.en-list { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:16px; }
.en-list li { display:flex; gap:14px; align-items:flex-start; }
.en-n { width:30px; height:30px; flex:none; border-radius:50%; display:grid; place-items:center; font:600 13px var(--font-ui);
  color:var(--hd-fg); background:var(--hd-surface-sunken); }
.en-list b { display:block; font:600 15px/1.3 var(--font-ui); color:var(--hd-fg); }
.en-list small { display:block; font:400 13px/1.4 var(--font-ui); color:var(--hd-fg-muted); margin-top:2px; }
.en-foot { display:flex; flex-direction:column; gap:10px; }
.en-foot .btn { width:100%; height:48px; justify-content:center; }
.en-note { text-align:center; font:400 13px/1.4 var(--font-ui); color:var(--hd-fg-muted); }
.en-hold { display:flex; align-items:center; gap:10px; font:500 13px var(--font-ui); color:var(--hd-fg); padding:10px 0; border-bottom:1px solid var(--hd-edge); }
.en-hold .num { font-weight:600; }
.en-hold span.sp { flex:1; color:var(--hd-fg-muted); }
.en-hold a { color:var(--hd-accent); font-weight:600; text-decoration:none; }
.en-prod { display:flex; gap:12px; align-items:center; }
.en-prod img { width:56px; height:56px; border-radius:12px; object-fit:cover; flex:none; }
.en-prod b { display:block; font:600 15px/1.3 var(--font-ui); color:var(--hd-fg); }
.en-prod small { display:flex; align-items:center; gap:6px; font:400 13px var(--font-ui); color:var(--hd-fg-muted); margin-top:3px; }
.en-prod small img { width:16px; height:16px; border-radius:4px; }
.en-big { font:700 28px/1.1 var(--font-brand); color:var(--hd-fg); }
.en-big small { display:block; font:400 13px var(--font-ui); color:var(--hd-fg-muted); margin-top:4px; }
.en-drop { border:1.5px dashed var(--hd-control-edge); border-radius:16px; padding:22px 16px; display:flex; flex-direction:column; align-items:center; gap:8px; text-align:center; }
.en-drop .g { width:44px; height:44px; border-radius:12px; display:grid; place-items:center; background:var(--hd-surface-sunken); color:var(--hd-fg); }
.en-drop b { font:600 15px var(--font-ui); color:var(--hd-fg); }
.en-drop small { font:400 13px var(--font-ui); color:var(--hd-fg-muted); }
.en-must { font:600 13px var(--font-ui); color:var(--hd-fg); margin:0 0 8px; }
.en-checks { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:8px; }
.en-checks li { display:flex; gap:10px; align-items:center; font:400 14px var(--font-ui); color:var(--hd-fg); }
.en-checks li svg { color:var(--hd-success); flex:none; }
.en-center { display:flex; flex-direction:column; align-items:center; text-align:center; gap:14px; padding:28px 0 8px; }
.en-center .n-spin { width:40px; height:40px; }
.en-shot { display:flex; gap:12px; align-items:center; padding:12px; border:1px solid var(--hd-edge); border-radius:14px; }
.en-shot img { width:40px; height:52px; border-radius:6px; object-fit:cover; }
.en-shot b { display:block; font:600 14px var(--font-ui); color:var(--hd-fg); }
.en-shot small { font:400 13px var(--font-ui); color:var(--hd-fg-muted); }
.en-ledger { border:1px solid var(--hd-edge); border-radius:14px; padding:4px 14px; }
.en-ledger div { display:flex; justify-content:space-between; padding:11px 0; font:400 14px var(--font-ui); color:var(--hd-fg-muted); }
.en-ledger div + div { border-top:1px solid var(--hd-edge); }
.en-ledger div b { font-weight:600; color:var(--hd-fg); font-variant-numeric:tabular-nums; }
.en-ledger .src { display:flex; align-items:center; gap:6px; font-size:12px; }
.en-coupon { display:flex; justify-content:space-between; align-items:center; font:500 14px var(--font-ui); color:var(--hd-fg); }
.en-coupon a { color:var(--hd-accent); font-weight:600; text-decoration:none; }
.en-ok { width:56px; height:56px; border-radius:50%; display:grid; place-items:center; background:var(--hd-success); color:#fff; }
"""

def sheet(body, theme="light", label="", head=None):
    under = f'<div class="en-under"><img src="{PH["serum_hero"]}" alt=""></div><div class="en-scrim"></div>'
    hd = head if head is not None else ''
    return phone(f'{under}<div class="en-sheet"><div class="en-grab"></div>{hd}{body}</div><div style="flex:1"></div>', theme, label)

def head(step):
    # step = 1..3 of Buy it / Send the receipt / Confirm & enroll
    bars = "".join(f'<i class="{"on" if i <= step else ""}"></i>' for i in (1, 2, 3))
    return f'<div class="en-head"><div class="en-prog">{bars}</div><span class="t">Step {step} of 3</span><span class="x">{ic("x", 20)}</span></div>'

def title(h, d=""):
    return f'<div><h2 class="en-h">{h}</h2>{f"<p class=en-d>{d}</p>" if d else ""}</div>'

def hold(mins="14:52"):
    return f'<div class="en-hold">{ic("clock", 18)}<b>Spot held for you</b><span class="sp num">{mins}</span><a>Add 10 min</a></div>'

AMZ = f'<img src="{K.STOCK}/platforms/amazon.png" alt="">'

def s_brief(t="light"):
    items = [("Buy it", "Buy the product through the store link, then come back here."),
             ("Send the receipt", "A screenshot of your order page. We read it in about 20 seconds."),
             ("Confirm & enroll", "Check what we read, then confirm to join.")]
    li = "".join(f'<li><span class="en-n">{i}</span><div><b>{a}</b><small>{b}</small></div></li>' for i, (a, b) in enumerate(items, 1))
    hd = f'<div class="en-head"><span class="t">Join Glow serum</span><span class="x">{ic("x", 20)}</span></div>'
    return sheet(title("Before you join", "Glow serum, 30 ml · Amazon") + f'<ol class="en-list">{li}</ol>'
                 f'<div class="en-foot"><button class="btn p lg">Join campaign</button><span class="en-note">You can leave before you buy.</span></div>', t, "1 · Before you join", hd)

def s_buy(t="light"):
    body = (hold() + title("Buy it") +
            f'<div class="en-prod"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><small>{AMZ}Amazon · ₹1,899</small></div></div>'
            f'<div class="en-big">₹1,240 back<small>on your purchase, once the brand approves your work</small></div>'
            f'<ol class="en-list"><li><span class="en-n">{ic("bag", 16)}</span><div><b>You pay on the store</b><small>With your own money, at their checkout, never inside the app.</small></div></li>'
            f'<li><span class="en-n">{ic("wallet", 16)}</span><div><b>The money comes back</b><small>Your cashback lands in your wallet once the brand approves your work.</small></div></li></ol>'
            f'<div class="en-foot"><button class="btn p lg">Order on Amazon {ic("arrow", 18)}</button><button class="btn s lg">I\'ve ordered</button></div>')
    return sheet(body, t, "2 · Buy it", head(1))

def s_receipt(t="light"):
    checks = "".join(f'<li>{ic("check", 16, "currentColor", 2.5)}{x}</li>' for x in ("The order number", "The product name and the price", "The store and the order date"))
    body = (hold("11:08") + title("Send the receipt", "A screenshot of your order page. We read it in about 20 seconds.") +
            f'<div class="en-drop"><span class="g">{ic("upload", 22)}</span><b>Add a screenshot</b><small>From your Amazon order page</small></div>'
            f'<div><p class="en-must">Your receipt must show</p><ul class="en-checks">{checks}</ul></div>'
            f'<div class="en-foot"><button class="btn p lg">Choose screenshot</button></div>')
    return sheet(body, t, "3 · Send the receipt", head(2))

def s_checking(t="light"):
    body = (f'<div class="en-center"><span class="n-spin"></span>{title("Checking your receipt", "This takes about 20 seconds. Keep this open.")}</div>'
            f'<div class="en-shot"><img src="{PH["flatlay"]}" alt=""><div><b>Order screenshot</b><small>Sent just now</small></div></div>')
    return sheet(body, t, "4 · Checking", head(2))

def s_confirm(t="light"):
    body = (hold("08:30") + title("Confirm & enroll", "Check what we read, then confirm to join.") +
            f'<div class="en-ledger"><div><span class="src">{icf("success", 14)}Read from your receipt</span><span></span></div>'
            f'<div><span>Order value</span><b>₹1,899</b></div><div><span>Cashback</span><b>₹1,240</b></div></div>'
            f'<div class="en-coupon"><span>Have a coupon?</span><a>Enter</a></div>'
            f'<div class="en-foot"><button class="btn p lg">Join and earn ₹1,240</button><span class="en-note">You\'ll have 7 days to post after you join.</span></div>')
    return sheet(body, t, "5 · Confirm & enroll", head(3))

def s_done(t="light"):
    body = (f'<div class="en-center"><span class="en-ok">{ic("check", 28, "currentColor", 3)}</span>{title("You\'re in", "Your tasks are ready. Open your enrollment to see what\'s next.")}</div>'
            f'<div class="en-foot"><button class="btn p lg">See what\'s next</button><button class="btn s lg">Done</button></div>')
    hd = f'<div class="en-head"><span class="t"></span><span class="x">{ic("x", 20)}</span></div>'
    return sheet(body, t, "6 · You're in", hd)

SCREENS = [s_brief, s_buy, s_receipt, s_checking, s_confirm, s_done]

if __name__ == "__main__":
    for t in ("light", "dark"):
        body = "".join(f(t) for f in SCREENS)
        page = f'<div class="en-wrap" style="width:2900px;background:{"#000" if t == "dark" else "#f2f3f6"}">{body}</div>'
        doc = html(page, f"Enroll sheet · {t}").replace("</style>", EN + "</style>", 1)
        open(os.path.join(OUT, f"enroll-sheet-{t}.html"), "w").write(doc)
    print("ok")
