"""A/B: current mobile standard (before) vs a bolder 'after' standard, same tokens and rules."""
import sys; sys.path.insert(0, "/tmp/hdwm")
from kit_build import *          # phone, ic, ics, PH, LOGO, CSS, CSS2, PAGE_CSS, s_home, s_detail, plat, av, vhex, tabbar, STOCK
PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-21", "women-44", "women-65", "men-12", "men-32")}
XCSS = """
.x-head { font-family: var(--font-brand); font-size: 34px; line-height: 38px; font-weight: 650; letter-spacing: -0.035em; font-variation-settings: 'opsz' 96; text-wrap: balance; }
.x-head span { color: var(--hd-fg-subtle); }
.x-title { font-family: var(--font-brand); font-size: 32px; line-height: 35px; font-weight: 650; letter-spacing: -0.035em; font-variation-settings: 'opsz' 96; }
.x-who { display: flex; align-items: center; gap: 10px; } .x-who img { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; display: block; }
.x-who b { display: flex; align-items: center; gap: 4px; font-size: 15px; font-weight: 600; } .x-who small { display: block; font-size: 13px; color: var(--hd-fg-muted); }
.x-hero { position: relative; z-index: 1; border-radius: 24px; overflow: hidden; height: 300px; flex: none; margin-top: 10px; }
.x-stack { position: relative; padding-top: 14px; }
.x-stack::before, .x-stack::after { content: ''; position: absolute; left: 22px; right: 22px; top: 0; height: 30px; border-radius: 20px; background: var(--hd-accent); opacity: .35; z-index: 0; }
.x-stack::after { left: 11px; right: 11px; top: 7px; opacity: .6; }
.x-hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; border-radius: 0 !important; }
.x-hero .sh { position: absolute; inset: auto 0 0 0; height: 62%; background: linear-gradient(to top, rgba(9,11,18,.86), rgba(9,11,18,0)); }
.x-hero .top { position: absolute; top: 14px; left: 14px; right: 14px; display: flex; justify-content: space-between; align-items: center; }
.x-pill { height: 30px; padding: 0 12px; border-radius: 999px; display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; background: rgba(255,255,255,.92); color: #121417; }
.x-hero .bt { position: absolute; left: 18px; right: 18px; bottom: 18px; color: #fff; display: flex; align-items: flex-end; gap: 12px; }
.x-hero .bt .t { flex: 1; } .x-hero .bt b { display: block; font-family: var(--font-brand); font-size: 26px; line-height: 29px; font-weight: 650; letter-spacing: -0.03em; white-space: nowrap; }
.x-hero .bt small { display: block; font-size: 14px; color: rgba(255,255,255,.78); margin-top: 4px; }
.x-go { width: 56px; height: 56px; border-radius: 50%; background: #fff; color: #121417; display: flex; align-items: center; justify-content: center; flex: none; }
.x-meta { display: flex; justify-content: space-between; padding: 14px 2px; border-top: 1px solid var(--hd-border); border-bottom: 1px solid var(--hd-border); }
.x-meta div { display: flex; align-items: center; gap: 6px; font-size: 14px; color: var(--hd-fg-muted); } .x-meta b { color: var(--hd-fg); font-weight: 650; }
.x-meta .ic { color: var(--hd-fg-muted); }
.x-bar { position: absolute; left: 18px; right: 18px; bottom: 30px; height: 64px; border-radius: 999px; background: var(--hd-surface); box-shadow: var(--hd-shadow-e3), 0 0 0 1px var(--hd-border); display: flex; align-items: center; justify-content: space-between; padding: 0 8px; z-index: 3; }
.x-bar .on { height: 48px; padding: 0 18px 0 14px; border-radius: 999px; background: var(--hd-accent); color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 600; font-size: 15px; }
.x-bar .d { width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--hd-fg-muted); }
.x-photo { position: relative; height: 410px; flex: none; margin: -50px 0 0; }
.x-photo img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 0 !important; }
.x-photo .tb { position: absolute; top: 58px; left: 16px; right: 16px; display: flex; justify-content: space-between; }
.x-disc { width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,.92); color: #121417; display: flex; align-items: center; justify-content: center; }
.x-sheet { position: relative; margin-top: -28px; border-radius: 28px 28px 0 0; background: var(--hd-canvas); padding: 22px 20px 0; display: flex; flex-direction: column; gap: 16px; flex: 1; }
.x-chips { display: flex; gap: 8px; } .x-chip { height: 36px; padding: 0 14px; border-radius: 10px; background: var(--hd-control); display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 560; }
.x-avs { display: flex; } .x-avs img { width: 30px; height: 30px; border-radius: 50%; object-fit: cover; box-shadow: 0 0 0 2px var(--hd-canvas); margin-left: -8px; } .x-avs img:first-child { margin-left: 0; }
.x-cta { display: flex; gap: 10px; padding: 12px 20px 30px; margin-top: auto; } .x-cta .btn { flex: 1; } .x-cta .sq { width: 52px !important; height: 52px; flex: none !important; padding: 0; border-radius: 14px; }
.x-row { display: flex; align-items: center; gap: 12px; }
.ab { display: flex; gap: 40px; align-items: flex-start; } .ab h3 { font: 600 15px var(--font-ui); margin: 0 0 12px; color: #555; }
"""
def home_after():
    return phone(f'<div class="topbar" style="height:60px"><div class="x-who"><img src="{PEOPLE["women-21"]}" alt=""><div><b>Riya Sharma {vhex(15)}</b><small>Creator · Kolkata</small></div></div><span class="ttl"></span>{ic("search")}<span style="position:relative">{ic("bell")}<span class="dot" style="position:absolute;top:0;right:1px;background:var(--hd-tone-vermilion)"></span></span></div>'
                 f'<div class="body" style="gap:14px;padding-top:8px"><div class="x-head">Hi Riya, <span>3 drops picked for you.</span></div>'
                 f'<div class="tabs"><span class="on">{ics("foryou", 16, "var(--hd-accent)")}For you <span class="cnt-b">3</span></span><span>{ic("trend", 16, "var(--hd-tone-vermilion)")}Trending</span><span>{ic("heart", 16, "var(--hd-tone-mint)")}Saved</span></div>'
                 f'<div class="x-stack"><div class="x-hero" style="margin-top:0"><img src="{PH["serum_hero"]}" alt=""><div class="sh"></div>'
                 f'<div class="top"><span class="x-pill">{ic("clock", 14)}Ends Fri</span><span class="x-pill"><span class="x-avs">' + "".join(f'<img src="{PEOPLE[p]}" style="width:20px;height:20px;box-shadow:0 0 0 1.5px #fff;margin-left:-6px">' for p in ("women-44", "men-12", "women-65")) + '</span>36 left</span></div>'
                 f'<div class="bt"><div class="t"><b>Glow serum, 30 ml</b><small>Lumen Labs · you earn ₹ 1,240</small></div><span class="x-go">{ic("arrow", 22)}</span></div></div></div>'
                 f'<div class="x-meta"><div>{ic("rupee", 18)}<b class="num">8,460</b> this month</div><div>{ic("star", 18)}<b class="num">4.9</b> rating</div></div>'
                 f'<div class="row"><img class="lead" src="{PH["scooter"]}"><div class="tx"><b>Kick scooter</b><small>Out for delivery · today</small></div><span class="badge info">On the way</span></div>'
                 f'</div><div class="x-bar"><span class="on">{ics("home", 20)}Home</span><span class="d">{ic("box", 22)}</span><span class="d">{ic("wallet", 22)}</span><span class="d">{ic("user", 22)}</span></div>', label="Home · after")

def detail_after():
    return phone(f'<div class="x-photo"><img src="{PH["serum_hero"]}" alt=""><div class="tb"><span class="x-disc">{ic("back", 22)}</span><span class="x-disc">{ic("share", 20)}</span></div></div>'
                 f'<div class="x-sheet"><div><div class="x-title">Glow serum, 30 ml</div><div class="flexw" style="margin-top:6px;font-size:15px;color:var(--hd-fg-muted)">by Lumen Labs · also on {plat("nykaa", 18)}{plat("amazon", 18)}</div></div>'
                 f'<div class="x-chips"><span class="x-chip">Skincare</span><span class="x-chip">Vitamin C</span><span class="x-chip">Vegan</span></div>'
                 f'<div class="x-meta"><div>{ic("rupee", 18)}<b class="num">1,240</b> you earn</div><div>{ic("gift", 18)}<b class="num">1,899</b> worth</div><div>{ic("clock", 18)}<b class="num">7</b> days</div></div>'
                 f'<p class="t-body muted" style="margin:0;font-size:16px;line-height:24px">A light vitamin C serum. Use it for two weeks, then tell your people how it went. <b style="color:var(--hd-link);font-weight:600">More</b></p>'
                 f'<div class="x-row"><div class="x-avs">' + "".join(f'<img src="{PEOPLE[p]}">' for p in ("women-44", "men-12", "women-65", "men-32")) + f'</div><span style="font-size:14px;color:var(--hd-fg-muted)"><b class="num" style="color:var(--hd-fg)">84</b> creators trying it · 36 slots left</span></div></div>'
                 f'<div class="x-cta" style="background:var(--hd-canvas)"><button class="btn s sq" aria-label="Save">{ic("heart", 22)}</button><button class="btn p lg">Apply for this drop</button></div>', label="Drop details · after")

body = (f'<div class="sheet-w" style="padding:40px"><div class="ab">'
        f'<div><h3>Before</h3>{s_home()}</div><div><h3>After</h3>{home_after()}</div>'
        f'<div><h3>Before</h3>{s_detail()}</div><div><h3>After</h3>{detail_after()}</div></div></div>')
U = os.path.expanduser("~/Downloads/hypedrive-wordmark/BRAND/ui")
open(os.path.join(U, "hypedrive-before-after.html"), "w").write(html(body, "Before / after").replace("</style>", XCSS + "</style>", 1))
print("ok")
