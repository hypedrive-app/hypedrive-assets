"""Build the UI kit sheet and high-fidelity screens from uikit.py's components."""
import sys, os, subprocess
sys.path.insert(0, "/tmp/hdwm")
from uikit import *
from xpass import XPASS
from kit2 import kit_more, DESKTOP2, CSS2, header
from uikit2 import stat, goal, kbd
from xsteps import XSTEPS

def vtl(items):
    """Vertical stepper / timeline: one marker system (done check, current ring + dot, upcoming outline), a continuous line, optional meta on any step."""
    n = len(items); out = []
    for i, it in enumerate(items):
        k, t, d = it[:3]; m = it[3] if len(it) > 3 else ""
        mk = ic("check", 14, "#fff", 3) if k == "done" else ""
        out.append(f'<div class="s {k}"{" aria-current=\"step\"" if k == "now" else ""}><div class="k"><i>{mk}</i>{"<em></em>" if i < n - 1 else ""}</div>'
                   f'<div class="tx"><div class="hd"><b>{t}</b>{f"<span class=tm>{m}</span>" if m else ""}</div><small>{d}</small></div></div>')
    return '<div class="x-tl" role="list">' + "".join(out) + '</div>'
EARN_REV = [42, 58, 64, 61, 77, 84, 91]
EARN = [5200, 5600, 6100, 6400, 7100, 7800, 8460]

PAGE_CSS = """
.sheet-w { width: 1600px; margin: 0 auto; background: var(--hd-bg); color: var(--hd-fg); padding: 64px 72px 80px; }
.sec { margin-top: 56px; } .sec > h2 { font-size: 30px; font-weight: 700; font-variation-settings: 'opsz' 48; margin: 0 0 4px; letter-spacing: -.015em; }
.sec > p { margin: 0 0 22px; color: var(--hd-fg-muted); font-size: 16px; }
.lbl { font-size: 13px; font-weight: 650; color: var(--hd-fg-muted); margin: 0 0 10px; }
.grid { display: grid; gap: 22px; } .g2 { grid-template-columns: repeat(2, 1fr); } .g3 { grid-template-columns: repeat(3, 1fr); } .g4 { grid-template-columns: repeat(4, 1fr); } .g6 { grid-template-columns: repeat(6, 1fr); }
.box { background: var(--hd-canvas); border-radius: 16px; padding: 22px; box-shadow: inset 0 0 0 1px var(--hairline); } .flexw { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
.iconcell { display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 14px 4px; border-radius: 12px; background: var(--hd-surface-raised); border: 1px solid var(--hd-border); font-size: 11px; color: var(--hd-fg-muted); }
.hero { display: flex; align-items: center; justify-content: space-between; }
.pf { margin: 0; display: flex; flex-direction: column; align-items: center; gap: 14px; } .pf figcaption { font-size: 14px; font-weight: 600; color: var(--hd-fg-muted); }
.screens { display: grid; grid-template-columns: repeat(4, 390px); gap: 40px 36px; justify-content: center; }
.desk { width: 1440px; height: 900px; border-radius: 14px; overflow: hidden; box-shadow: 0 8px 28px rgba(16,20,38,.05); display: grid; grid-template-columns: 248px 1fr; background: var(--hd-bg-subtle); border: 1px solid var(--hd-border); }
.side { background: var(--hd-surface); border-right: 1px solid var(--hd-border); padding: 22px 16px; display: flex; flex-direction: column; gap: 4px; }
.side .it { display: flex; gap: 12px; align-items: center; padding: 10px 12px; border-radius: 10px; font-size: 15px; font-weight: 600; color: var(--hd-fg-muted); }
.side .it.on { background: var(--hd-accent-subtle); color: var(--hd-accent); }
.main { padding: 26px 34px; display: flex; flex-direction: column; gap: 20px; overflow: hidden; }
.dtop { display: flex; align-items: center; gap: 16px; } .dtop .t-h1 { flex: 1; }
.keypad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; padding: 8px 6px 4px; background: var(--hd-border); flex: none; }
.keypad span { height: 46px; border-radius: 8px; background: var(--hd-surface); box-shadow: 0 1px 0 var(--hd-border-strong); display: flex; flex-direction: column; align-items: center; justify-content: center; }
.keypad span.blank { background: transparent; box-shadow: none; } .keypad b { font-size: 22px; font-weight: 450; line-height: 1; } .keypad small { font-size: 10.5px; letter-spacing: .12em; color: var(--hd-fg-muted); font-weight: 600; }
.sheetdemo { position: relative; width: 340px; height: 420px; border-radius: 34px; overflow: hidden; background: var(--hd-canvas); box-shadow: 0 0 0 6px #000; }
.sd-ghost { padding: 54px 18px 0; } .sheetdemo .scrim { position: absolute; inset: 0; background: rgba(13,14,18,.44); }
.sd-sheet { position: absolute; left: 0; right: 0; bottom: 0; padding-bottom: 8px; }

.tbl .flexw { flex-wrap: nowrap; } .tbl b { white-space: nowrap; }
.stepn { width: 22px; height: 22px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; background: var(--hd-bg-subtle); color: var(--hd-fg-muted); box-shadow: inset 0 0 0 1px var(--hd-border); }
.tabs .stepn:has(svg) { background: var(--hd-success); color: #fff; box-shadow: none; } .tabs .on .stepn { background: var(--hd-accent); color: #fff; box-shadow: none; }
"""

def sec(title, desc, body): return f'<section class="sec"><h2>{title}</h2><p>{desc}</p>{body}</section>'
def lbl(t): return f'<div class="lbl">{t[0].upper() + t[1:]}</div>'

# ================================================================== UI KIT
ICLBL = {"drop": "skincare", "foryou": "picked for you", "payouts": "withdraw", "live": "open", "ok": "approved", "fast": "instant", "linkbroken": "broken link",
         "reports": "statements", "overview": "overview", "campaign": "campaigns", "bag": "store", "bank": "payout account", "box": "product", "checkdouble": "all read",
         "clip": "attach", "filecheck": "receipt checked", "film": "reel", "gift": "bonus", "headphones": "support", "privacy": "verify PAN", "receipt": "receipt",
         "send": "send application", "tag": "category", "truck": "shipment", "upload": "upload screenshot", "users": "creators", "wifioff": "offline",
         "lamp": "home & living", "lipstick": "makeup", "shirt": "fashion", "trending": "ending soon", "heart": "saved", "pin": "address", "login": "sign in", "logout": "sign out",
         "alert": "fix tasks", "pause": "paused", "spark": "new", "trend": "earnings", "sort": "sort", "sliders": "filters", "filter": "filter", "list": "enrolled", "grid": "browse"}
def kit(theme="light"):
    o = []
    o.append(f'<div class="hero"><div><img src="{LOGO[theme]}" style="height:40px"><div class="t-display" style="margin-top:28px">UI kit</div>'
             f'<p class="muted t-body" style="max-width:620px">Primitives and components for every Hypedrive surface. Everything here reads from the brand tokens, so light and dark come for free.</p></div>'
             f'<img src="{ILL[("growth",theme)]}" style="height:220px"></div>')
    # primitives: colour roles
    roles = ["bg", "bg-subtle", "surface-raised", "fg", "fg-muted", "border", "accent", "accent-subtle", "success", "warning", "danger", "info"]
    sw = "".join(f'<div style="display:flex;gap:10px;align-items:center"><span style="width:38px;height:38px;border-radius:10px;background:var(--hd-{r});border:1px solid var(--hd-edge)"></span><span class="t-small"><b>{r}</b></span></div>' for r in roles)
    o.append(sec("Primitives", "Colour roles, type, spacing, radius, elevation and icons. Use roles, never raw hex.",
        f'<div class="grid g2"><div class="box" data-theme="light" style="background:var(--hd-bg-subtle);color:var(--hd-fg)"><div class="lbl">Colour roles · light</div><div class="grid g3" style="gap:12px">{sw}</div></div>'
        f'<div class="box" data-theme="dark" style="background:var(--hd-bg)"><div class="lbl">Colour roles · dark</div><div class="grid g3" style="gap:12px;color:var(--hd-fg)">{sw}</div></div></div>'
        f'<div class="grid g2" style="margin-top:22px"><div class="box tstack">{lbl("type")}<div class="t-display">Get ₹1,139 back</div><div class="t-h1">Glow serum, 30 ml</div><div class="t-h2">Your wallet</div><div class="t-h3">Submit 2 tasks</div>'
        f'<div class="kt-body">Body 15 · Allo. Buy it on Nykaa, send 2 tasks, and get ₹1,339 back after the brand approves.</div><div class="t-small muted">Small 13.5. Closes 26 Nov 2026 · 8 spots left</div><div class="t-cap subtle">Caption 12.5. Due in 41 days · Available ₹6,820</div><div class="flexw t-cap subtle" style="gap:18px;margin-top:2px"><span>Display 34 · Bricolage</span><span>Title 1 · 24</span><span>Title 2 · 20</span><span>Title 3 · 15 · Allo</span></div>'
        f'<div style="margin-top:22px">{lbl("weights · roles")}</div><div class="typewt"><span style="font-weight:400">Regular 400<small>body, help text</small></span><span style="font-weight:500">Medium 500<small>labels, buttons</small></span><span style="font-weight:600">Semibold 600<small>titles, amounts</small></span></div></div>'
        f'<div class="box">{lbl("spacing · 4px base")}<div class="flexw" style="align-items:flex-end">' + "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><span style="width:{v}px;height:{v}px;background:var(--hd-accent);border-radius:4px"></span><span class="t-cap subtle num">{v}</span></div>' for v in (4, 8, 12, 16, 24, 32, 48, 64)) + '</div>'
        f'<div style="margin-top:22px">{lbl("radius")}</div><div class="flexw" style="gap:14px">' + "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:56px;height:52px;border-radius:{v}px;background:var(--hd-surface-raised);border:1px solid var(--hd-edge)"></div><span class="t-cap num muted">{n}</span></div>' for n, v in (("4", 4), ("6", 6), ("8", 8), ("10", 10), ("12", 12), ("14", 14), ("16", 16), ("24", 24), ("full", 999))) + '</div>'
        f'<div style="margin-top:22px">{lbl("elevation")}</div><div class="flexw" style="padding-bottom:12px">' + "".join(f'<div style="width:120px;height:64px;border-radius:12px;background:var(--hd-surface-raised);border:1px solid var(--hd-edge);box-shadow:var(--hd-shadow-{e});display:flex;align-items:flex-end;padding:8px;font-size:12px;font-weight:700">{e}</div>' for e in ("e1", "e2", "e3")) + '</div></div></div>'
        f'<div class="box" style="margin-top:22px">{lbl(f"icons · 18 grid · 1.5 stroke · {ICON_SET}")}<div class="grid" style="grid-template-columns:repeat(12,1fr);gap:10px">' +
        "".join(f'<div class="iconcell">{ic(n, 24)}<span>{ICLBL.get(n, n)}</span></div>' for n in P) + '</div></div>'))
    # buttons
    states = ["", "hov", "prs", "foc", "dis"]
    rows = "".join(f'<div class="t-small" style="font-weight:700;align-self:center">{lab}</div>' + "".join(f'<button class="btn {c} {st}">{t}</button>' for st in states) for lab, c, t in
                   [("Primary", "p", "Verify PAN"), ("Secondary", "s", "Withdraw"), ("Ghost", "g", "See all"), ("Danger", "d", "Leave")])
    o.append(sec("Buttons", "Deep cobalt for the one main action, with a quiet tactile edge and a pressed state that sinks. White secondary with a hairline and lip. Icons only where they help you recognise the action.",
        f'<div class="grid g2"><div class="box"><div class="grid" style="grid-template-columns:90px repeat(5,1fr);gap:14px;justify-items:start">'
        f'<span></span>' + "".join(f'<span class="t-cap muted">{x}</span>' for x in ("Default", "Hover", "Pressed", "Focus", "Disabled")) + rows + '</div>' + f'<div style="margin-top:28px">{lbl("group · link")}</div><div class="flexw"><span class="btngroup split"><button class="btn p">Withdraw ₹6,820</button><button class="btn p icon" aria-label="Choose payout account">{ic("down", 16)}</button></span><span class="seg" role="tablist"><span>7 days</span><span class="on">30 days</span><span>All time</span></span><button class="btn link">How cashback works</button></div>'
        f'<div style="margin-top:28px">{lbl("row actions · one style")}</div><div class="flexw"><button class="btn s sm">Fix tasks</button><button class="btn s sm">View campaign</button><button class="btn g sm">Withdraw application</button></div></div>'
        f'<div class="box">{lbl("sizes · 36 · 44 · 48 on a phone bottom bar")}<div class="flexw"><button class="btn p sm">Apply to join</button><button class="btn p">Join campaign</button><button class="btn p lg xt1-bar">Join and earn ₹1,139</button></div>'
        f'<div style="margin-top:22px">{lbl("with icon · icon only")}</div><div class="flexw"><button class="btn p">{ic("privacy", 20)}Verify PAN</button><button class="btn s">{ic("upload", 20)}Add screenshot</button>'
        f'<button class="btn s icon" aria-label="Share campaign">{ic("share", 20)}</button><button class="btn s icon" aria-label="Save campaign">{ic("heart", 20)}</button><button class="btn g">See all campaigns {ic("arrow", 18)}</button></div>'
        f'<div style="margin-top:22px">{lbl("full width · loading")}</div><div class="stack"><button class="btn p lg block">Submit 2 tasks</button><button class="btn p lg block" aria-busy="true"><span class="spin"></span>Sending application…</button><button class="btn p lg block" disabled>Send application</button><button class="btn d lg block">Leave this enrollment</button></div>'
        f'</div></div>'))
    # inputs & selection
    o.append(sec("Inputs & selection", "44px fields and search. Labels sit above, help below. Errors say what to do.",
        f'<div class="grid g3"><div class="box stack">'
        f'<div class="field"><div class="labrow"><label>Link to your reel</label><span>Required</span></div><div class="input">{ic("link", 18)}<span class="ph">https://instagram.com/reel/…</span></div></div>'
        f'<div class="field"><label>Link to your reel · error</label><div class="input err">{ic("link", 18)}<span>instagram.com/reel/C4xQ2</span></div><span class="help err">{ic("alert", 14)}Enter the full link, starting with https://</span></div>'
        f'<div class="field"><label>Instagram handle · hover</label><div class="input hov"><span class="addon">{soc("Instagram", 16)}</span><span>@riya.glows</span></div></div>'
        f'<div class="field"><label>Amount · focus</label><div class="input foc"><span class="addon">₹</span><span class="num">1,240</span></div><span class="help">Minimum ₹100 · Available ₹6,820</span></div>'
        f'<div class="field"><label>UPI ID · valid</label><div class="input ok">{bank("hdfc", 18)}<span>riya@okhdfcbank</span><span class="trail" style="color:var(--hd-success)">{ic("check", 18)}</span></div><span class="help ok">{ic("check", 14)}Verified · Riya Sharma</span></div>'
        f'<div class="grid g2" style="gap:12px"><div class="field"><label>Account number</label><div class="input"><span class="num mono">50100281946093</span></div></div><div class="field"><label>IFSC</label><div class="input"><span class="mono">HDFC0001234</span></div></div></div>'
        f'<div class="grid g2" style="gap:12px"><div class="field"><label>PAN · verified</label><div class="input dis">{ic("lock", 18)}<span class="mono">ABCDE1234F</span></div></div><div class="field"><label>Date of birth</label><div class="input"><span class="num">14 / 03 / 1998</span><span class="trail">{ic("calendar", 18)}</span></div></div></div>'
        f'<div class="field"><label>Category</label><div class="input"><span style="flex:1">Skincare</span><span class="trail">{ic("down", 18)}</span></div></div>'
        f'</div>'
        f'<div class="box stack"><div class="search">{ic("search", 18)}Search campaigns<span class="kbd">⌘K</span></div><div class="search foc">{ic("search", 18)}<span class="q">glo</span><span class="clr">{ic("x", 11, sw=3)}</span></div>'
        f'<div class="suggest" style="margin-top:-6px"><div class="sg hl">{ic("search", 18)}<span><b>glo</b>w serum</span><span class="sub">3 campaigns {kbd("↵")}</span></div><div class="sg">{ic("search", 18)}<span><b>glo</b>ss lip oil</span><span class="sub">1 campaign</span></div>'
        f'<div class="sg-h">Campaigns</div><div class="sg"><img src="{PH["serum"]}" alt=""><span><b>Glo</b>w serum, 30 ml<span class="m"> · 60% back</span></span><span class="sub">Lumen Labs</span></div>'
        f'<div class="sg-h">Brands</div><div class="sg"><span class="sg-logo">{av("GL", 1, 28)}</span><span><b>Glo</b>Theory</span><span class="sub">6 open campaigns</span></div>'
        f'<div class="sg-h">Recent</div><div class="sg">{ic("clock", 18)}<span class="m">night cream</span><span class="sub sg-x">{ic("x", 14)}</span></div><div class="sg-f"><span>{kbd("↑")}{kbd("↓")} move</span><span>{kbd("↵")} open</span><span>{kbd("esc")} close</span></div></div>'
        f'<div class="field"><div class="labrow"><label>Why you are a good fit</label><span>Optional</span></div><div class="input textarea">I post skincare reels every week and have used Lumen Labs products for a year.</div><span class="help">The brand reads this before approving you.<span class="cnt">78 / 300</span></span></div>'
        f'<div class="field"><label>Verification code</label><div class="otp2 num" role="group" aria-label="6-digit code"><span class="f">4</span><span class="f">8</span><span class="f">2</span><i></i><span class="on"></span><span></span><span></span></div></div>'
        f'<div style="margin-top:4px">{lbl("radio cards · withdraw to")}<div class="grid g2" style="gap:8px"><div class="row sel" style="flex-direction:column;align-items:flex-start;gap:4px"><span class="radio on"></span><b class="t-small" style="margin-top:4px">HDFC ••6093</b><small class="t-cap muted">Usually within minutes</small></div>'
        f'<div class="row" style="flex-direction:column;align-items:flex-start;gap:4px"><span class="radio"></span><b class="t-small" style="margin-top:4px">UPI riya@okhdfcbank</b><small class="t-cap muted">Usually within minutes</small></div></div></div>'
        f'</div>'
        f'<div class="box stack"><div class="flexw"><span class="check on">{ic("check", 16, "#fff", 3)}</span><span class="kt-body">#ad label added</span><span class="check"></span><span class="kt-body">Paid partnership</span></div>'
        f'<div class="flexw"><span class="radio on"></span><span class="kt-body">Pay by UPI</span><span class="radio"></span><span class="kt-body">Bank account</span></div>'
        f'<div class="flexw"><span class="switch on"></span><span class="kt-body">Campaign updates</span><span class="switch"></span><span class="kt-body">Marketing</span></div>'
        f'<div>{lbl("filter chips")}<div class="flexw"><span class="chip on">All</span><span class="chip">Ending soon</span><span class="chip">New</span><span class="chip">Saved</span></div><div class="flexw" style="margin-top:10px"><span class="chip">Platform{ic("down", 14)}</span><span class="chip on">Store · Nykaa{ic("down", 14)}</span><span class="chip">Category{ic("down", 14)}</span><span class="chip">{ic("sort", 16)}Cashback high to low</span></div></div>'
        f'<div>{lbl("slider · withdraw amount")}<div class="slider"><i></i><b></b></div><div class="flexw t-small muted" style="justify-content:space-between;margin-top:10px"><span>Minimum ₹100</span><span class="num">₹6,820</span></div></div>'
        f'<div>{lbl("focus · keyboard")}<div class="flexw"><span class="chip foc">Ending soon</span><span class="check on foc">{ic("check", 16, "#fff", 3)}</span><span class="radio foc"></span><span class="switch on foc"></span><button class="btn s sm foc">Later</button></div></div>'
        f'<div>{lbl("checkbox list · store")}<div class="stack" style="gap:8px">' + "".join(f'<div class="row"><span class="check {"on" if on else ""}">{ic("check", 14, "#fff", 3) if on else ""}</span>{plat(t.lower(), 20)}<div class="tx"><b>{t}</b></div><span class="t-small muted num">{m}</span></div>' for t, k, m, on in (("Nykaa", "", "14 campaigns", True), ("Amazon", "", "9 campaigns", True), ("Myntra", "", "4 campaigns", False))) + '</div></div></div></div>'))
    # navigation
    o.append(sec("Navigation", "Bars are strips, not cards: a hairline edge and nothing else. Underline tabs sit straight under the bar. One tab bar on phone, one bare header on desktop.",
        f'<div class="grid g2 xa-nav"><div class="box"><div class="lbl">Phone</div><div class="xa-phone">'
        f'<div class="xa-bar">{ic("back", 20)}<span class="ttl">Glow serum</span>{ic("share", 20)}{ic("more", 20)}</div>'
        f'<div class="xa-bar"><img src="{LOGO[theme]}" style="height:20px"><span class="ttl"></span>{ic("search", 20)}<span class="xa-bell">{ic("bell", 20)}<i></i></span></div>'
        f'<div class="tabs xa-tabs"><span class="on">Ordered</span><span>Tasks sent</span><span>Fixes needed</span><span>Paid</span></div>'
        f'<div class="xa-fill"></div><div class="tabbar">' + "".join(f'<div class="{"on" if n == "Enrolled" else ""}">{ics(i, 24) if n == "Enrolled" else ic(i, 24)}<span>{n}</span></div>' for i, n in (("home", "Home"), ("campaign", "Campaigns"), ("list", "Enrolled"), ("wallet", "Wallet"))) + '</div></div></div>'
        f'<div class="box"><div class="lbl">Desktop</div><div class="xa-desk"><div class="xa-crumb"><span class="crumb">Campaigns{ic("chev", 14)}<b>Glow serum</b></span><span class="xa-bell">{ic("bell", 20)}<i></i></span></div>'
        f'<div class="xa-ph"><div><div class="xa-h">Glow serum, 30 ml</div><p>Lumen Labs · Buy on Nykaa · Closes 26 Nov 2026</p></div><button class="btn p sm">Join campaign</button></div>'
        f'</div><div class="xa-desk" style="margin-top:14px"><div class="xa-ph" style="padding-top:14px"><div><div class="xa-h">Wallet</div><p>Available ₹6,820 · ₹1,339 on hold</p></div><button class="btn p sm">Withdraw</button></div>'
        f'<div class="tabs" style="padding:0 24px"><span class="on">Activity</span><span>Statements</span></div></div></div></div>'))
    # data display
    o.append(sec("Data display", "Every list item is its own rounded card. Product images sit bare, no plate behind them.",
        f'<div class="grid g3"><div class="box stack">'
        f'<div class="row"><img class="lead" src="{PH["serum"]}"><div class="tx"><b>Glow serum, 30 ml</b><small>Nykaa · 8 spots left</small></div><div class="end"><b class="num">60% back</b><small class="muted t-cap">+₹200 bonus</small></div></div>'
        f'<div class="row"><img class="lead" src="{PH["cream"]}"><div class="tx"><b>Night cream, 50 g</b><small>Amazon · Closes 26 Nov 2026</small></div><div class="end"><b class="num">50% back</b><small class="muted t-cap">Closing soon</small></div></div>'
        f'<div class="row"><img class="lead" src="{PH["bottles"]}"><div class="tx"><b>Daily cleanser trio</b><small>Nykaa · Due in 41 days</small></div><span class="badge info">Submit tasks</span></div>'
        f'<div class="row"><img class="lead xt1-ava" src="{PEOPLE["women-68"]}" alt=""><div class="tx"><b>Riya Sharma</b><small>@riya.glows · Kolkata</small></div><div class="end"><b class="num">₹24,610</b><small class="muted t-cap">earned so far</small></div></div>'
        f'<div class="row"><span class="x-tile">{ic("rupee", 20)}</span><div class="tx"><b>Cashback · Night cream</b><small>26 Nov 2026 · HDFC ••6093</small></div><div class="end"><b class="num" style="color:var(--hd-success-strong)">+₹950</b><small class="muted t-cap">Paid</small></div></div>'
        f'<div class="row"><span class="skel" style="width:48px;height:48px"></span><div class="tx"><span class="skel" style="display:block;height:12px;width:60%"></span><span class="skel" style="display:block;height:10px;width:40%;margin-top:8px"></span></div></div></div>'
        f'<div class="box stack xa-d2"><div>{lbl("enrollment status")}<div class="flexw" style="gap:8px"><span class="badge neutral">{ics("send", 13)}Applied</span><span class="badge info">Ready to join</span><span class="badge info">Submit tasks</span><span class="badge neutral">In review</span><span class="badge warning">Fix tasks</span><span class="badge success">Paid</span><span class="badge danger">Not approved</span></div></div>'
        f'<div>{lbl("campaign availability")}<div class="flexw" style="gap:8px"><span class="badge success">Open</span><span class="badge warning">Closing soon</span><span class="badge neutral">Full</span><span class="badge neutral">Paused</span><span class="badge neutral">{ics("lock", 13)}Closed</span></div></div>'
        f'<div class="flexw xa-avrow">{av("RS",0,24)}{av("RS",0,32)}{av("RS",0,40)}<img class="xa-photo" src="{PEOPLE["women-68"]}" alt=""><div class="avs xa-stack">{av("RS",0)}{av("AK",1)}{av("MJ",2)}<span class="xa-more">+9</span></div></div>'
        f'<div class="xa-stats"><div class="panel stat"><div class="sh"><span class="sl">Available</span></div><div class="sv"><b class="num">₹6,820</b></div><div class="vz"><span class="t-small muted">+₹1,139 this week</span></div></div>'
        f'<div class="panel stat"><div class="sh"><span class="sl">On hold</span></div><div class="sv"><b class="num">₹1,339</b></div><div class="vz"><span class="t-small muted">Until the brand approves</span></div></div>'
        f'</div></div>'
        f'<div class="box">' + vtl([("done", "Proof", "Order receipt checked · 20 Nov 2026"), ("now", "Tasks", "Submit 2 tasks · Due in 41 days"), ("", "Review", "The brand checks your tasks"), ("", "Paid", "₹1,339 lands in your wallet")]) +
        f'<div style="margin-top:20px">' + f'<div class="panel stat xt1-spots"><div class="sh"><span class="sl">Spots</span></div><div class="sv"><b class="num">112</b><span class="su">of 120</span></div><div class="xt1-bar3"><i style="width:93.3%"></i></div></div>' + f'</div>'
        '</div></div>'))
    # feedback & overlays
    dlg_ = lambda t, b, cancel, act, cls="d": f'<div class="dialog n-dlg2 sm"><div class="d2b"><b class="d2t">{t}</b><p class="d2p">{b}</p></div><div class="d2f"><button class="btn s sm">{cancel}</button><button class="btn {cls} sm">{act}</button></div></div>'
    o.append(sec("Feedback & overlays", "Notices explain, toasts confirm, dialogs ask. One action each.",
        f'<div class="grid g3"><div class="box stack"><div class="notice success">{icf("success")}<span><b style="display:block">Your receipt is verified</b>It passed and is ready to join.</span></div>'
        f'<div class="notice warning">{icf("warning")}<span><b style="display:block">Verify your PAN to withdraw</b>Your ₹6,820 stays safe until you do.</span></div>'
        f'<div class="notice info">{icf("info")}<span>A new account can take withdrawals 24 hours after it’s added.</span></div>'
        f'<div class="notice warning">{icf("warning")}<span><b style="display:block">You’re offline</b>Check your connection and try again.</span></div>'
        f'<div class="lblgap">{lbl("toast")}<div class="flexw"><div class="toast"><span class="ok">{ics("success", 18)}</span>Spot held for you<b>Add 10 min</b></div><div class="toast"><span class="ok">{ics("success", 18)}</span>Your receipt is verified</div></div></div><div class="lblgap">{lbl("tooltip")}<div class="flexw" style="padding-bottom:6px"><span class="tooltip">Usually within minutes</span></div></div></div>'
        f'<div class="box" style="display:flex;flex-direction:column;gap:18px;align-items:center">'
        + dlg_("Leave this enrollment?", "<b>You’ll lose your spot.</b> You can join again while spots remain.", "Stay enrolled", "Leave")
        + dlg_("Withdraw application?", "<b>The brand won’t see it.</b> You can apply again before the campaign closes.", "Keep it", "Withdraw")
        + f'<div class="dialog n-dlg2 sm"><div class="d2b"><b class="d2t">Review and send</b><p class="d2p"><b>2 tasks go to Lumen Labs for review.</b> By submitting you confirm the posts follow the brief and stay public.</p></div><div class="d2f"><button class="btn s sm">Back</button><button class="btn p sm">Submit 2 tasks</button></div></div>'
        + dlg_("Raise a dispute", "<b>Hypedrive support steps in.</b> Tell us what went wrong with this enrollment.", "Cancel", "Raise a dispute", "p")
        + f'</div>'
        f'<div class="box stack" style="align-items:center"><div class="sheetdemo"><div class="sd-ghost sd-photo"><img src="{PH["bottles"]}" alt=""><div class="sd-pt"><b>Clear skin set</b><span>Free product · Worth ₹2,400</span></div></div><div class="scrim"></div>'
        f'<div class="sheet sd-sheet"><div class="grab"></div><div class="t-h2">Where should we send it?</div><p class="t-small muted" style="margin:4px 0 14px">Lumen Labs ships Clear skin set here.</p>'
        f'<div class="stack" style="gap:8px"><div class="row sel"><span class="radio on"></span><div class="tx"><b>Home</b><small>14 Park Street, Kolkata 700016</small></div></div><div class="row"><span class="radio"></span><div class="tx"><b>Work</b><small>Salt Lake Sector V, Kolkata</small></div></div>'
        f'<button class="btn p block sd-cta">Confirm address</button></div><div class="home-ind" style="margin-top:6px;height:18px"><i></i></div></div></div>'
        f'<div class="menu n-ctx"><div class="hl">{ic("share", 16)}Share campaign</div><div>{ic("heart", 16)}Save</div><div>{ic("link", 16)}Copy link</div><i class="n-sep"></i><div class="dg">{ic("x", 16)}Leave this enrollment</div></div></div></div>'))
    # empty & tables
    btn = lambda c, x: f'<button class="btn {c}">{x}</button>'
    em = lambda i, t, d, act: f'<div class="n-ea2"><span class="n-eai">{ic(i, 22)}</span><div><b>{t}</b><span class="t-small muted">{d}</span></div>{act}</div>'
    o.append(sec("Empty states & tables", "Empty states use one illustration and one next step. Tables are for desktop only.",
        f'<div class="grid g2 eb-wrap"><div class="stack" style="gap:12px"><div class="lbl">Empty state</div><div class="card eb-empty2"><img src="{ILL[("search",theme)]}" alt=""><b class="e2t">No campaigns found</b><p class="e2p">Nothing matches these filters. Clear them to see every open campaign.</p>'
        f'<button class="btn p e2b">Clear filters</button></div>'
        f'<div class="lbl" style="margin-top:8px">Compact</div><div class="stack" style="gap:10px">'
        + em("check", "Nothing to do right now", "We’ll tell you when there is.", "")
        + em("payouts", "No activity yet", "Money in and out shows here.", btn("s sm", "Browse campaigns"))
        + em("receipt", "No commissions yet", "Orders through your links show here once they are approved.", "")
        + em("bank", "No payout account yet", "Add one to withdraw.", btn("s sm", "Add account")) + '</div></div>'
        f'<div class="stack" style="gap:12px"><div class="lbl">Table · review queue</div><div class="card" style="overflow:hidden"><table class="tbl eb-tbl"><tr><th>Creator</th><th>Campaign</th><th style="text-align:right">Tasks sent</th><th>Status</th></tr>' +
        "".join(f'<tr><td><div class="tcell"><img class="tav" src="{STOCK}/people/{a}.jpg" alt=""><b>{n}</b></div></td><td class="muted">{c}</td><td class="num tpay">{p}</td><td><span class="tst {b}">{ics({"success":"success","warning":"clock","neutral":"check","danger":"danger"}[b], 14)}{bl}</span></td></tr>'
                for a, k, n, c, b, bl, p in [("women-68", 0, "Riya Sharma", "Glow serum, 30 ml", "warning", "In review", "2 of 2"), ("men-12", 1, "Arjun Kapoor", "Night cream, 50 g", "warning", "In review", "2 of 2"),
                                             ("women-44", 2, "Meera Joshi", "Daily cleanser trio", "danger", "Fix tasks", "2 of 2"), ("women-65", 3, "Tanvi Nair", "Glow serum, 30 ml", "neutral", "Paid", "2 of 2"), ("women-21", 4, "Kabir Nanda", "Night cream, 50 g", "danger", "Not approved", "1 of 2")]) + '</table></div>'
        f'<div class="lbl" style="margin-top:8px">Blocked and error</div><div class="stack" style="gap:10px">'
        + em("privacy", "Verify your PAN to withdraw", "Your ₹6,820 stays safe until you do.", btn("s sm", "Verify PAN"))
        + em("lock", "Your account is on hold", "Support is reviewing it. We’ll email you.", btn("s sm", "Contact support"))
        + em("search", "Campaign not found", "It may have closed or the link is wrong.", btn("s sm", "Browse campaigns")) + '</div></div></div>'))
    o.append(kit_more(theme))
    from kit3 import kit_new
    o.append(kit_new(theme))
    from kit4 import kit_domain
    o.append(kit_domain(theme))
    from kit5 import kit_money
    o.append(kit_money(theme))
    return f'<div class="sheet-w">{"".join(o)}</div>'

# ================================================================== MOBILE SCREENS
PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-68", "women-44", "women-65", "men-12", "men-32")}
def avs(ps, size=30): return '<span class="x-avs">' + "".join(f'<img src="{PEOPLE[p]}" alt="" style="width:{size}px;height:{size}px">' for p in ps) + '</span>'
def meta(*items): return '<div class="x-meta">' + "".join(f'<div>{ic(i, 18)}<b class="num">{v}</b> {k}</div>' for i, v, k in items) + '</div>'

def s_welcome():
    col = lambda *ks: '<div>' + "".join(f'<img src="{PH[k]}" alt="" style="height:{h}px">' for k, h in ks) + '</div>'
    return phone(f'<div class="xm1-wel"><img class="xm1-logo" src="{LOGO["dark"]}" alt="Hypedrive"><div class="xm1-mos" aria-hidden="true">'
                 + col(("sand", 168), ("serum", 168), ("set", 168)) + col(("cream", 168), ("flatlay", 168), ("bottles", 168)) + col(("mask", 168), ("bottles", 168), ("serum", 168)) + '</div><div class="xm1-fade"></div>'
                 f'<div class="xm1-copy"><h1 class="xm1-h">Products in.<br><span>Hype out.</span></h1>'
                 f'<p class="xm1-p">Try new products free, tell your people, and get paid for honest reviews.</p>'
                 f'<div class="xm1-act"><button class="btn p lg block">Get started</button><button class="btn g block">I already have an account</button></div></div></div>', "dark", "Welcome", "#fff")

def s_otp():
    cells = "".join(f'<span>{d}</span>' for d in "482") + '<span class="on"></span><span></span><span></span>'
    keys = [('1', ''), ('2', 'ABC'), ('3', 'DEF'), ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'), ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ'), ('', ''), ('0', ''), ('⌫', '')]
    return phone(f'<div class="xm1-bar" style="padding:0 16px">{ic("back")}</div><div class="xm1-s xm1-otp"><div><h1 class="xm1-h">Verify your phone</h1><p class="xm1-sub">Enter the 6-digit code sent to <b class="num">+91 98•••• 4821</b></p></div>'
                 f'<div class="xm1-code num" role="group" aria-label="6-digit code">{cells}</div>'
                 f'<div class="xm1-aux"><span>Resend code in <span class="num">0:24</span></span><button class="btn link">Change number</button></div>'
                 f'<button class="btn p lg block dis xy-verify">Verify</button><div style="flex:1"></div></div>'
                 f'<div class="xm1-pad">' + "".join(f'<span><b>{ic("back", 22) if a == "⌫" else a}</b><small>{b}</small></span>' for a, b in keys) + '</div>', label="Verify phone")

def s_home():
    """Home, by the spec: greeting, the last setup step, money at a glance, what needs Riya, what waits on brands, picks."""
    def row(photo, title, meta, cls=""):
        return (f'<div class="hm-row"><img src="{PH[photo]}" alt=""><div class="tx"><b>{title}</b>'
                f'<small class="{cls}">{meta}</small></div>{ic("chev", 16)}</div>')
    def pick(photo, store, title, lead, bonus, foot):
        return (f'<div class="hm-pick"><img src="{PH[photo]}" alt=""><div class="bd"><span class="sr">{plat(store, 14)}{store.title()}</span>'
                f'<b>{title}</b><p>{lead}{f"<em>+{bonus} bonus</em>" if bonus else ""}</p><small>{foot}</small></div></div>')
    return phone(
        f'<div class="xm1-bar xm1-s"><img class="av" src="{PEOPLE["women-68"]}" alt="Riya Sharma">{ic("search")}<span class="bell">{ic("bell")}<i></i></span></div>'
        f'<div class="xm1-s hm">'
        f'<h1 class="hm-h">Hi, Riya</h1>'
        f'<div class="hm-wal"><small>Available</small><b class="num">₹6,820</b>'
        f'<p><span class="num">₹1,339</span> on hold · <span class="num">₹990</span> pending approval</p>'
        f'<a class="ft">{ics("privacy", 16, "var(--hd-accent)")}<span>Verify your PAN to withdraw</span><em>Verify</em></a></div>'
        f'<div class="hm-sh"><h2>Your turn</h2><span class="num">2</span></div>'
        + row("serum", "Glow serum, 30 ml", "Submit 2 tasks · due in 41 days")
        + row("bottles", "Daily cleanser trio", "Fix 1 task · due in 6 days", "warn")
        + f'<div class="hm-sh"><h2>In review</h2><span class="num">1</span></div>'
        + row("cream", "Night cream, 50 g", "₹990 back after approval")
        + f'<div class="hm-sh"><h2>Picked for you</h2><button class="btn link">See all</button></div>'
        f'<div class="hm-picks">{pick("set", "nykaa", "Clear skin set", "<span>Free product</span>", "₹500", "Worth ₹2,400")}'
        f'{pick("mask", "nykaa", "Clay mask, 100 g", "<span class=num>45% back</span>", "", "3 spots left")}</div>'
        f'</div>{tabbar("Home")}', label="Home")

def s_detail():
    step = lambda i, t, d: f'<div class="c5-st"><span class="x-tile c5-ti">{ics(i, 20)}</span><b>{t}</b><small>{d}</small></div>'
    req = lambda *xs: '<div class="c4-req">' + "".join(f'<span>{x}</span>' for x in xs) + '</div>'
    task = lambda tile, t, d, r: f'<div class="c4-task"><span class="x-tile c4-ti">{tile}</span><div class="tx"><b>{t}</b><small>{d}</small>{r}</div></div>'
    return phone(f'<div class="xm1-s xm1-det xq-cp c4 c5"><div class="c4-hero"><img src="{PH["serum_hero"]}" alt=""><div class="tb"><span class="x-disc">{ic("back", 22)}</span><span style="display:flex;gap:10px"><span class="x-disc">{ic("heart", 20)}</span><span class="x-disc">{ic("share", 20)}</span></span></div>'
                 f'<div class="c4-hb"><span class="c4-store">{plat("nykaa", 16)}Buy on Nykaa</span><h1>Glow serum, 30 ml</h1><p class="c5-by"><b>Lumen Labs</b>{vhex(14)}<span>·</span>Closes 26 Nov · 8 spots left</p></div></div>'
                 f'<div class="c4-body"><div class="c6-offer"><span class="k">You get back</span><b class="num big">₹1,339</b>'
                 f'<p class="mix"><b class="num">₹1,139</b> cashback (60%) + <b class="num">₹200</b> bonus · after the brand approves</p>'
                 f'<div class="ft"><span>You pay <b class="num">₹1,899</b> on Nykaa</span><span>It costs you <b class="num">₹560</b></span></div></div>'
                 f'<h2 class="c4-h">How it works</h2><div class="c5-steps">{step("bag", "Buy it", "on Nykaa")}{step("camera", "Post", "2 tasks")}{step("wallet", "Get paid back", "to your wallet")}</div>'
                 f'<h2 class="c4-h">What you\'ll create</h2>'
                 f'{task(soc("Instagram", 22), "Instagram reel", "Show it on bare skin in daylight", req("Link", "Screenshots", "#ad", "Paid partnership"))}'
                 f'{task(plat("nykaa", 22), "Nykaa review", "Say how it felt after a week", req("Link", "Screenshot", "40+ words"))}</div>'
                 f'<div class="cp-bar cp-bar2"><div class="l"><b class="num">₹1,339 back</b><small>45 days to post after you join</small></div><button class="btn p lg">Join campaign</button></div></div>', label="Campaign", sbar_color="#fff")

def _join_under():
    return f'<div class="jf-under"><img src="{PH["serum_hero"]}" alt=""></div><div class="scrim"></div>'

def _hold(left, pct):
    return (f'<div class="jf-hold2">{ics("clock", 16)}<span>Spot held · <b class="num">{left}</b> left</span><button class="jf-add">Add 10 min</button></div>')

def s_apply():
    row = lambda i, t, d: f'<div class="jf-row"><span class="x-tile jf-ti">{ics(i, 18)}</span><div class="tx"><b>{t}</b><small>{d}</small></div></div>'
    return phone(_join_under() + f'<div class="overlay"><div class="sheet jf"><div class="grab"></div>'
                 f'<div class="jf-hd"><div><small>Step 1 of 2</small><h2>Buy it first</h2></div><span class="x-disc jf-x">{ic("x", 18)}</span></div>'
                 + _hold("9:41", 97) +
                 f'<div class="jf-list">{row("bag", "Buy it on Nykaa", "₹1,899 · use the button below")}{row("camera", "Send 2 tasks", "Within 45 days of joining")}{row("wallet", "Get ₹1,339 back", "After the brand approves")}</div>'
                 f'<div class="jf-act"><button class="btn p lg block">{ic("external", 18)}Buy on Nykaa</button><button class="btn s lg block">I\'ve ordered — add receipt</button></div>'
                 f'<p class="jf-note">You can leave before you buy.</p></div></div>', label="Join · buy", sbar_color="#fff")

def s_join_receipt():
    return phone(_join_under() + f'<div class="overlay"><div class="sheet jf"><div class="grab"></div>'
                 f'<div class="jf-hd"><div><small>Step 2 of 2</small><h2>Add your receipt</h2></div><span class="x-disc jf-x">{ic("x", 18)}</span></div>'
                 + _hold("6:12", 62) +
                 f'<div class="jf-file"><span class="x-tile jf-fi">{ic("file", 20)}</span><div class="tx"><b>nykaa-order-4471.pdf</b><small>284 KB · Replace</small></div></div>'
                 f'<div class="jf-ok"><span class="ic-ok">{ics("success", 20)}</span><div class="tx"><b>Your receipt is verified</b><small>Nykaa · <b class="num">₹1,899</b> · 20 Nov 2026</small></div></div>'
                 f'<div class="jf-sum"><span>You get back after the brand approves</span><b class="num">₹1,339</b></div>'
                 f'<div class="jf-act"><button class="btn p lg block">Join and earn ₹1,339</button></div>'
                 f'<p class="jf-note">You\'ll have 45 days to post after you join.</p></div></div>', label="Join · receipt", sbar_color="#fff")

def _e1_bar(left="", right="", title=""):
    return f'<div class="xm1-bar xm1-s e1-bar">{left}{f"<b class=e1-bt>{title}</b>" if title else ""}<span class="e1-r">{right}</span></div>'

def _e1_row(lead, title, meta, tail="", cls=""):
    return f'<div class="hm-row e1-row {cls}">{lead}<div class="tx"><b>{title}</b><small>{meta}</small></div>{tail}</div>'

def s_track():
    """The enrollment page in its other state: their turn, in review (Night cream)."""
    from scr_n2 import s_enrollment_detail
    return s_enrollment_detail("review")

def s_review():
    """Submit tasks: link + 1-6 screenshots per task, one button, attestation."""
    def shot(i): return f'<div class="e1-sh"><img src="{PH[i]}" alt=""><span aria-label="Remove">{ic("x", 10, "currentColor", 3)}</span></div>'
    add = f'<div class="e1-sh e1-add">{ic("plus", 20)}</div>'
    def task(logo, t, lab, ph, shots, n, hint):
        return (f'<div class="e1-card e1-tk"><div class="e1-th">{logo}<b>{t}</b><small>{hint}</small></div>'
                f'<label>{lab}</label><div class="e1-in">{ph}</div>'
                f'<label>Screenshots <span class="num">{n}</span></label><div class="e1-shs">{"".join(shot(s) for s in shots)}{add}</div></div>')
    return phone(_e1_bar(f'<span class="e1-ib">{ic("x", 22)}</span>', '<span class="e1-note">Draft saved</span>')
                 + f'<div class="xm1-s hm e1-pg"><div class="e1-hb"><h1 class="hm-h">Submit tasks</h1><p>Glow serum, 30 ml · due in 41 days</p></div>'
                 + task(soc("Instagram", 22), "Instagram reel", "Link to your reel", '<span>instagram.com/reel/C9xQ2…</span>', ("serum", "flatlay", "sand"), "3 of 6", "#ad · Paid partnership")
                 + task(plat("nykaa", 22), "Nykaa review", "Link to your review", '<span>nykaa.com/reviews/glow-serum…</span>', ("bottles",), "1 of 6", "40+ words")
                 + '<p class="e1-att">By submitting you confirm these are your own posts and they are live.</p></div>'
                 f'<div class="cta e1-cta"><button class="btn p lg block">Submit 2 tasks</button></div>', label="Submit tasks")

def s_wallet():
    """Wallet: Available is the one number; on hold and earned so far sit under it; real money movements below."""
    def mv(lead, t, d, a, cls=""):
        return _e1_row(lead, t, d, f'<b class="num e1-amt {cls}">{a}</b>')
    tile = lambda i, c="": f'<span class="x-tile e1-tile {c}">{ic(i, 20)}</span>'
    rows = (mv(tile("clock"), "On hold", "Glow serum · after approval", "₹1,339", "mut")
            + mv(bank("hdfc", 22, tile=True), "Withdrawal", "HDFC ••6093 · 16 Nov 2026", "−₹2,000")
            + mv(f'<img src="{PH["bottles"]}" alt="">', "Cashback", "Face wash, 100 ml · 12 Nov 2026", "+₹540", "pos"))
    return phone(_e1_bar(f'<b class="e1-bt e1-bt0">Wallet</b>', f'<span class="e1-ib">{ic("settings", 22)}</span>')
                 + f'<div class="xm1-s hm e1-pg">'
                 f'<div class="hm-wal e1-w"><small>Available</small><b class="num">₹6,820</b>'
                 f'<p><span class="num">₹1,339</span> on hold · <span class="num">₹24,610</span> earned so far</p>'
                 f'<div class="e1-wf"><button class="btn p block">Withdraw</button></div></div>'
                 + _e1_row(bank("hdfc", 22, tile=True), "Payout to HDFC ••6093", "Usually within minutes · fee ₹0", f'<button class="btn link e1-lk">Change</button>')
                 + f'<div class="hm-sh"><h2>Activity</h2><button class="btn link">Statements</button></div>'
                 + rows + '</div>' + tabbar("Wallet"), label="Wallet")

def s_success():
    """Tasks submitted: the moment after Submit 2 tasks."""
    return phone(_e1_bar("", f'<span class="e1-ib">{ic("x", 22)}</span>')
                 + f'<div class="xm1-s hm e1-pg e1-ok"><div class="e1-ill"><img src="{ILL[("approved","light")]}" alt=""></div>'
                 f'<div class="e1-okt"><h1 class="hm-h">Tasks submitted</h1><p>Lumen Labs will review your 2 tasks. We\'ll tell you the moment they\'re approved.</p></div>'
                 + _e1_row(f'<img src="{PH["serum"]}" alt="">', "Glow serum, 30 ml", "₹1,339 back after approval") +
                 '</div>'
                 f'<div class="cta e1-cta e1-cta2"><button class="btn p lg block">View enrollment</button><button class="btn g block">Back to Home</button></div>', label="Tasks submitted")

def s_notifs():
    """Inbox: real events only. One unread signal (the dot); tabs by meaning."""
    def item(tile, title, sub, time, unread=False):
        return (f'<div class="hm-row e1-row e1-nr">{tile}<div class="tx"><b>{title}</b><small>{sub} · {time}</small></div>'
                f'<div class="e1-ne"><i class="{"on" if unread else ""}"></i></div></div>')
    t = lambda c, i: f'<span class="x-tile e1-tile {c}">{ics(i, 20)}</span>'
    today = (item(t("cobalt", "campaign"), "Glow serum is open", "Lumen Labs · 8 spots left", "2m", True)
             + item(t("mint", "filecheck"), "Receipt checked", "Glow serum, 30 ml · submit 2 tasks next", "4h", True)
             + item(t("vermilion", "alert"), "Your enrollment needs a change", "Daily cleanser trio · Fix 1 task", "6h", True))
    earlier = (item(t("mint", "wallet"), "Your earnings have landed", "₹540 from Face wash, 100 ml", "Wed")
               + item(bank("hdfc", 22, tile=True), "Withdrawal sent", "₹2,000 to HDFC ••6093", "Mon"))
    tabs = "".join(f'<span class="{"on" if i == 0 else ""}">{n}</span>' for i, n in enumerate(("All", "To do", "Money", "Campaigns")))
    return phone(_e1_bar(f'<span class="e1-ib">{ic("back", 22)}</span>', '<button class="btn link e1-mk">Mark all read</button>')
                 + f'<div class="xm1-s hm e1-pg"><h1 class="hm-h">Inbox</h1><div class="e1-tabs">{tabs}</div>'
                 f'<div class="hm-sh"><h2>Today</h2></div>{today}<div class="hm-sh"><h2>Earlier</h2></div>{earlier}</div>', label="Inbox")

def s_profile():
    """Settings in dark mode: the same page as the light Settings screen."""
    from scr_n2 import s_settings
    return s_settings("dark")

def s_empty():
    sim = [("serum", "nykaa", "Glow serum, 30 ml", "Nykaa", "60% back"), ("cream", "amazon", "Night cream, 50 g", "Amazon", "50% back"), ("bottles", "nykaa", "Daily cleanser trio", "Nykaa", "55% back")]
    rows = "".join(_e1_row(f'<img src="{PH[i]}" alt="">', t, f'{plat(p, 14)}{s} · Lumen Labs', f'<b class="num e1-amt">{r}</b>', "e1-lr") for i, p, t, s, r in sim)
    return phone(f'<div class="searchbar"><div class="search foc">{ic("search", 18)}<span class="q">matcha whisk</span><span class="clr">{ic("x", 11, sw=3)}</span></div><button class="btn link" style="text-decoration:none">Cancel</button></div>'
                 f'<div class="xm1-s hm e1-pg"><div class="e1-nil"><b>No campaigns found</b><p>Nothing matches “matcha whisk”. Check the spelling or try a shorter word.</p></div>'
                 f'<div class="hm-sh"><h2>Open now</h2><button class="btn link">See all</button></div>{rows}</div>{tabbar("Campaigns")}', label="Empty search")

from scr_n1 import s_onboarding, s_browse, s_enrollments
from scr_n2 import s_enrollment_detail, s_withdraw, s_settings, s_barter
MOBILE = [s_welcome, s_otp, s_home, s_detail, s_apply, s_join_receipt, s_track, s_review, s_wallet, s_success, s_notifs, s_profile, s_empty,
          s_onboarding, s_browse, s_enrollments, s_enrollment_detail, s_withdraw, s_settings, s_barter]

# ================================================================== DESKTOP
def sidebar(active):
    items = [("overview", "Overview"), ("campaign", "Campaigns"), ("star", "Reviews"), ("users", "Creators"), ("wallet", "Wallet"), ("reports", "Reports")]
    return (f'<aside class="side"><img src="{LOGO["light"]}" style="height:26px;margin:0 8px 22px;align-self:flex-start">' +
            "".join(f'<div class="it {"on" if n == active else ""}">{ic(i)}{n}</div>' for i, n in items) +
            f'<div style="flex:1"></div><div class="card" style="padding:14px;background:var(--hd-bg-subtle)"><b class="t-small">Wallet balance</b><div class="num t-h2">₹2,40,000</div><button class="btn p sm block" style="margin-top:8px">Add funds</button></div>'
            f'<div class="it">{av("LL", 2, 30)}Lumen Labs</div></aside>')

def d_dashboard():
    kpis = [("Active creators", "312", "▲ 18%", "up"), ("Reviews this week", "91", "▲ 42%", "up"), ("Avg. rating", "4.7", "▲ 0.2", "up"), ("Cost per review", "₹1,180", "▼ 6%", "up")]
    bars = EARN_REV
    rev = [("RS", 0, "Riya Sharma", "Glow serum", 5, "success", "Approved"), ("AK", 1, "Arjun Kapoor", "Glow serum", 4, "warning", "In review"), ("MJ", 2, "Meera Joshi", "Night cream", 5, "success", "Approved"), ("TN", 3, "Tanvi Nair", "Glow serum", 3, "warning", "In review")]
    return (f'<div class="desk">{sidebar("Overview")}<div class="main"><div class="dtop"><div class="t-h1">Good morning, Lumen Labs</div><div class="search" style="width:320px;background:var(--hd-surface)">{ic("search", 20)}Search creators, reviews</div>{ic("bell")}<button class="btn p">{ic("plus", 20)}New campaign</button></div>'
            f'<div class="grid g4">' + "".join(f'<div class="card kpi"><small>{k}</small><b class="num">{v}</b><span class="delta {c}">{d}</span><span class="t-small muted"> vs last week</span></div>' for k, v, d, c in kpis) + '</div>'
            f'<div class="grid" style="grid-template-columns:1.6fr 1fr"><div class="card" style="padding:20px"><div class="flexw" style="justify-content:space-between"><b class="t-h3">Reviews per week</b><div class="tabs" style="border:0"><span class="on">7 weeks</span><span>Quarter</span></div></div>'
            f'<div class="bars">' + "".join(f'<div><span class="num" style="font-weight:700;color:var(--hd-fg)">{v}</span><i style="height:{v*1.3}px;{"background:" + V["500"] if v == 91 else ""}"></i><span>W{n+1}</span></div>' for n, v in enumerate(bars)) + '</div></div>'
            f'<div class="card" style="padding:20px"><b class="t-h3">Live campaigns</b><div class="stack" style="margin-top:12px">' +
            "".join(f'<div class="row" style="background:var(--hd-bg-subtle)"><img class="lead" src="{PH[i]}" style="width:40px;height:40px"><div class="tx"><b>{t}</b><div class="tape" style="margin-top:6px;height:6px"><i style="width:{p}%"></i></div></div><span class="t-small muted num">{p}%</span></div>' for i, t, p in (("serum", "Glow serum", 70), ("cream", "Night cream", 42), ("mask", "Repair hair mask", 18))) + '</div></div></div>'
            f'<div class="card" style="overflow:hidden"><div class="flexw" style="justify-content:space-between;padding:16px 18px 6px"><b class="t-h3">Latest reviews</b><span class="t-small" style="color:var(--hd-link);font-weight:700">See all</span></div>'
            f'<table class="tbl"><tr><th>Creator</th><th>Product</th><th>Rating</th><th>Status</th><th></th></tr>' +
            "".join(f'<tr><td><div class="flexw">{av(a, k, 34)}<b>{n}</b></div></td><td class="muted">{p}</td><td><div class="stars">{"".join(ic("star", 16, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(r))}</div></td><td><span class="badge {b}">{bl}</span></td><td style="text-align:right">{ic("more", 20)}</td></tr>' for a, k, n, p, r, b, bl in rev) +
            '</table></div></div></div>')

def d_builder():
    steps = ["Product", "Creators", "Budget", "Review"]
    return (f'<div class="desk">{sidebar("Campaigns")}<div class="main"><div class="dtop"><div><span class="t-small muted">Campaigns / New</span><div class="t-h1">Create a campaign</div></div><div style="flex:1"></div><button class="btn s">Save draft</button><button class="btn p">Continue</button></div>'
            f'<div class="card n-wzcard"><div class="n-wz" role="list">' + "".join(f'<div class="s {"done" if n < 2 else "now" if n == 2 else ""}" role="listitem"><span class="k">{ic("check", 14, sw=3) if n < 2 else ""}</span><span class="n-st"><b>{s}</b></span></div>' + ('<i class="ln' + (' done' if n < 2 else '') + '"></i>' if n < len(steps) - 1 else '') for n, s in enumerate(steps)) + '</div></div>'
            f'<div class="grid" style="grid-template-columns:1.3fr 1fr;gap:28px"><div class="card stack" style="padding:24px;gap:18px"><b class="t-h2">Budget and payout</b>'
            f'<div class="grid g2"><div class="field"><label>Payout per review</label><div class="input"><span class="pre">₹</span><span class="num">1,240</span></div><span class="help">Creators in your category earn ₹900–1,500</span></div>'
            f'<div class="field"><label>Number of creators</label><div class="input foc"><span class="num">120</span></div></div></div>'
            f'<div class="field"><label>Minimum followers</label><div class="slider" style="margin:12px 0 6px"><i></i><b></b></div><div class="flexw t-small muted" style="justify-content:space-between"><span>1k</span><b class="num" style="color:var(--hd-fg)">10k+</b><span>100k</span></div></div>'
            f'<div class="field"><label>Platforms</label><div class="flexw"><span class="chip on">{soc("Instagram", 16)}Instagram</span><span class="chip on">{soc("Youtube", 16)}YouTube</span><span class="chip">{soc("Threads", 16)}Threads</span><span class="chip">{ic("edit", 16)}Blogs</span></div></div>'
            f'<div class="row"><div class="tx"><b>Auto-approve 4★ and up</b><small>We still check every link is public</small></div><span class="switch on"></span></div>'
            f'<div class="notice warning">{icf("warning")}<span>Your wallet covers 120 creators. <b>₹1,48,800</b> will be reserved when you publish.</span></div></div>'
            f'<div class="stack"><span class="t-small muted" style="font-weight:600">Preview: what creators see</span><div class="card" style="padding:18px"><img src="{PH["serum_hero"]}" style="width:100%;height:180px;display:block;margin-bottom:12px">'
            f'<div class="flexw"><span class="badge success">Live</span><span class="badge neutral">Skincare</span></div><div class="t-h2" style="margin-top:8px">Glow serum, 30 ml</div><span class="t-small muted">by Lumen Labs</span>'
            f'<div class="grid g3" style="gap:8px;margin-top:12px"><div class="card kpi" style="padding:10px"><small>Earn</small><b class="num" style="font-size:18px">₹1,240</b></div><div class="card kpi" style="padding:10px"><small>Slots</small><b class="num" style="font-size:18px">120</b></div><div class="card kpi" style="padding:10px"><small>Review in</small><b style="font-size:18px">7 days</b></div></div>'
            f'<button class="btn p block" style="margin-top:14px">Apply for this drop</button></div></div></div></div></div>')

def d_moderation():
    rows = [("RS", 0, "Riya Sharma", "18.4k", 5, "Light, no smell, skin feels calmer after two weeks.", "warning", "New"), ("AK", 1, "Arjun Kapoor", "9.2k", 4, "Good but the dropper leaks a little.", "warning", "New"),
            ("MJ", 2, "Meera Joshi", "41k", 5, "My new nightly step. Showed results in a week.", "success", "Approved"), ("TN", 3, "Tanvi Nair", "6.0k", 2, "Link is private.", "danger", "Rejected")]
    tr = "".join(f'<tr style="{"background:var(--hd-accent-subtle)" if i == 0 else ""}"><td><span class="check {"on" if i == 0 else ""}">{ic("check", 14, "#fff", 3) if i == 0 else ""}</span></td><td><div class="flexw">{av(a, k, 34)}<div><b>{n}</b><div class="t-cap subtle">{f} followers</div></div></div></td>'
                 f'<td><div class="stars">{"".join(ic("star", 15, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(r))}</div></td><td class="muted" style="max-width:300px">{q}</td><td><span class="badge {b}">{bl}</span></td></tr>' for i, (a, k, n, f, r, q, b, bl) in enumerate(rows))
    return (f'<div class="desk">{sidebar("Reviews")}<div class="main" style="flex-direction:row;gap:22px;padding-right:0"><div style="flex:1;display:flex;flex-direction:column;gap:18px">'
            f'<div class="dtop"><div class="t-h1">Reviews</div><span class="badge warning num">23 to check</span><div style="flex:1"></div><div class="search" style="width:260px;background:var(--hd-surface)">{ic("search", 20)}Search</div></div>'
            f'<div class="flexw"><span class="chip on"><img src="{PH["serum"]}" style="width:18px;height:18px;border-radius:6px">Glow serum</span><span class="chip">{ic("star", 16)}All ratings</span><span class="chip">{ic("sliders", 16)}More filters</span><div style="flex:1"></div><button class="btn s sm">Reject</button><button class="btn p sm">{ic("check", 16)}Approve 1</button></div>'
            f'<div class="card" style="overflow:hidden"><table class="tbl"><tr><th></th><th>Creator</th><th>Rating</th><th>Review</th><th>Status</th></tr>{tr}</table></div></div>'
            f'<div style="width:400px;background:var(--hd-surface);border-left:1px solid var(--hd-border);margin:-26px 0;padding:26px 24px;display:flex;flex-direction:column;gap:16px">'
            f'<div class="flexw" style="justify-content:space-between"><b class="t-h2">Review</b>{ic("x")}</div><div class="flexw">{av("RS", 0, 48)}<div><b>Riya Sharma</b><div class="t-small muted">@riya.glows · 18.4k · Kolkata</div></div></div>'
            f'<div style="height:240px;border-radius:14px;overflow:hidden;position:relative"><img src="{PH["flatlay"]}" style="width:100%;height:100%;border-radius:0"><span class="badge neutral" style="position:absolute;bottom:12px;left:12px">{ic("play", 14)}Reel · 0:24</span></div>'
            f'<div class="stars">' + "".join(ic("star", 22, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(5)) + '</div><p class="t-body" style="margin:0">Used it every night for two weeks. Light, no smell, and my skin feels calmer. Would buy again.</p>'
            f'<div class="notice success">{icf("success")}<span>Link is public and the brand tag is present.</span></div><div style="flex:1"></div><div class="flexw"><button class="btn s" style="flex:1">Reject</button><button class="btn p" style="flex:2">Approve and pay ₹1,240</button></div></div></div></div>')

DESKTOP = [("Brand dashboard", d_dashboard), ("Campaign builder", d_builder), ("Review moderation", d_moderation)]

SQJS = open("/tmp/hdwm/squircle.js").read()
import re as _re
BADGE_ICON = {"Live": "live", "To check": "clock", "In review": "clock", "Review": "clock", "Approved": "success", "Found": "success", "Verified": "success",
              "Rejected": "danger", "Failed": "danger", "New": "info", "Paid": "check", "Draft": "edit", "Full": "lock", "Paused": "pause", "On the way": "fast"}
BADGE_CLASS = {"success": "success", "warning": "clock", "danger": "danger", "info": "info"}
def _badge(m):
    cls, inner = m.group(1), m.group(2)
    inner = inner.replace('<span class="bdot"></span>', '')
    text = _re.sub(r"<[^>]+>", "", inner).strip()
    if "<svg" in inner or not text or text.replace(",", "").isdigit(): return m.group(0).replace('<span class="bdot"></span>', '')
    key = BADGE_ICON.get(text) or BADGE_CLASS.get(cls.split()[0])
    return f'<span class="badge {cls}">{ics(key, 13) if key else ""}{inner}</span>' if key else f'<span class="badge {cls}">{inner}</span>'
def badgeize(s):
    s = s.replace('<span class="bdot"></span>', '')
    return _re.sub(r'<span class="badge ((?:success|warning|danger|info|neutral)[^"]*)">(.*?)</span>(?!</span>)', _badge, s)
_FS = {"11.5": "12", "12.5": "13", "13.5": "14", "14.5": "15", "13.8": "14", "15.5": "16"}
def _snap(css):
    """Half-pixel font sizes sit off the type scale (11/12/13/14/15/16); snap them to it."""
    css = _re.sub(r"font-size:\s*(\d+\.\d)px", lambda m: "font-size:" + _FS.get(m.group(1), m.group(1)) + "px", css)
    return _re.sub(r"(font:[^;}\"]*?)(\d+\.\d)px", lambda m: m.group(1) + _FS.get(m.group(2), m.group(2)) + "px", css)
def _late():
    import importlib, xlead, xa, xb, xc, xd, xe, xf, xg, xm1, xm2, xm3, xs, xy, xq1, xq2, xr1, xr2, xr3, xr4, xt1, xt2, xt3, xz, xh, xh2, xn1, xn2
    return xlead.XLEAD + xa.XA + xb.XB + xc.XC + xd.XD + xe.XE + xf.XF + xg.XG + xm1.XM1 + xm2.XM2 + xm3.XM3 + xs.XS + xy.XY + xq1.XQ1 + xq2.XQ2 + xr1.XR1 + xr2.XR2 + xr3.XR3 + xr4.XR4 + xt1.XT1 + xt2.XT2 + xt3.XT3 + xz.XZ + xh.XH + xh2.XH2 + xn1.XN1 + xn2.XN2

import re as _re
_STORES = {"Nykaa": "nykaa", "Amazon": "amazon", "Myntra": "myntra", "Flipkart": "flipkart", "Meesho": "meesho"}
def favify(h):
    """Store favicons where a store is named as the store — skipped when that store's logo is already right before it."""
    def ico(n): return f'<img class="plat sfav" src="{STOCK}/platforms/{_STORES[n]}.png" width="14" height="14" alt="">'
    def has_logo(src, i, name): return f'platforms/{_STORES[name]}.png' in src[max(0, i - 260):i]
    def sub(pat, mk, src):
        return _re.sub(pat, lambda m: m.group(0) if has_logo(src, m.start(), m.group("n")) else mk(m), src)
    h = sub(r'· (?P<n>Nykaa|Amazon|Myntra|Flipkart|Meesho)(?=\s*(?:<|·))', lambda m: f'· {ico(m.group("n"))}{m.group("n")}', h)
    h = sub(r'>(?P<n>Nykaa|Amazon|Myntra|Flipkart|Meesho)<', lambda m: f'>{ico(m.group("n"))}{m.group("n")}<', h)
    h = sub(r'(?P<o>on|On) (?P<n>Nykaa|Amazon|Myntra)(?=\s*<)', lambda m: f'{m.group("o")} {ico(m.group("n"))}{m.group("n")}', h)
    return h

def html(body, title, base=""): return f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{title}</title><link rel=icon type='image/svg+xml' href='assets/favicon.svg'>{f'<base href={chr(34)}{base}{chr(34)}>' if base else ''}<style>{_snap(CSS)}{_snap(CSS2)}{PAGE_CSS}{XPASS}{XSTEPS}{_late()}</style></head><body>{_snap(favify(badgeize(body)))}<script>{SQJS}</script></body></html>"

if __name__ == "__main__":
    open(os.path.join(OUT, "hypedrive-ui-kit.html"), "w").write(html(kit(), "Hypedrive UI kit"))
    open(os.path.join(OUT, "hypedrive-ui-kit-dark.html"), "w").write(html(kit("dark"), "Hypedrive UI kit · dark").replace("<body>", '<body data-theme="dark" style="background:#000">'))
    mob = f'<div class="sheet-w" style="width:1860px"><img src="{LOGO["light"]}" style="height:32px"><div class="t-display" style="margin:20px 0 6px">App screens · mobile</div><p class="muted t-body" style="margin:0 0 40px">High-fidelity concept, 390 × 844.</p><div class="screens">{"".join(f() for f in MOBILE)}</div></div>'
    open(os.path.join(OUT, "hypedrive-screens-mobile.html"), "w").write(html(mob, "Hypedrive mobile screens"))
    for n, (t, f) in enumerate(DESKTOP2, 1):
        open(os.path.join(OUT, f"hypedrive-desktop-{n}.html"), "w").write(html(f'<div style="padding:40px;display:flex;justify-content:center;background:#e9eaee">{f()}</div>', t))
    # each mobile screen alone, for PNG export
    for n, f in enumerate(MOBILE, 1):
        open(os.path.join(OUT, f"_m{n:02d}.html"), "w").write(html(f'<div style="padding:30px;display:inline-block">{f()}</div>', "screen", "../"))
    print("built", len(MOBILE), "mobile,", len(DESKTOP), "desktop")
