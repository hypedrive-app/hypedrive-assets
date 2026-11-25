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
        f'<div class="grid g2" style="margin-top:22px"><div class="box tstack">{lbl("type")}<div class="t-display">Display 34 · Bricolage</div><div class="t-h1">Title 1 · 24 · Bricolage</div><div class="t-h2">Title 2 · 20 · Bricolage</div><div class="t-h3">Title 3 · 15 · Geist</div>'
        f'<div class="kt-body">Body 15 · Geist. Creators get the product, try it for real, and tell their people.</div><div class="t-small muted">Small 13.5. Payouts land fast and fair.</div><div class="t-cap subtle">Caption 12.5 · 9:41 · ₹1,240</div>'
        f'<div style="margin-top:22px">{lbl("weights · roles")}</div><div class="typewt"><span style="font-weight:400">Regular 400<small>body, help</small></span><span style="font-weight:500">Medium 500<small>labels, buttons</small></span><span style="font-weight:600">Semibold 600<small>titles</small></span></div></div>'
        f'<div class="box">{lbl("spacing · 4px base")}<div class="flexw" style="align-items:flex-end">' + "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><span style="width:{v}px;height:{v}px;background:var(--hd-accent);border-radius:4px"></span><span class="t-cap subtle num">{v}</span></div>' for v in (4, 8, 12, 16, 24, 32, 48, 64)) + '</div>'
        f'<div style="margin-top:22px">{lbl("radius")}</div><div class="flexw" style="gap:14px">' + "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:56px;height:52px;border-radius:{v}px;background:var(--hd-surface-raised);border:1px solid var(--hd-edge)"></div><span class="t-cap num muted">{n}</span></div>' for n, v in (("4", 4), ("6", 6), ("8", 8), ("10", 10), ("12", 12), ("14", 14), ("16", 16), ("24", 24), ("full", 999))) + '</div>'
        f'<div style="margin-top:22px">{lbl("elevation")}</div><div class="flexw" style="padding-bottom:12px">' + "".join(f'<div style="width:120px;height:64px;border-radius:12px;background:var(--hd-surface-raised);border:1px solid var(--hd-edge);box-shadow:var(--hd-shadow-{e});display:flex;align-items:flex-end;padding:8px;font-size:12px;font-weight:700">{e}</div>' for e in ("e1", "e2", "e3")) + '</div></div></div>'
        f'<div class="box" style="margin-top:22px">{lbl(f"icons · 18 grid · 1.5 stroke · {ICON_SET}")}<div class="grid" style="grid-template-columns:repeat(12,1fr);gap:10px">' +
        "".join(f'<div class="iconcell">{ic(n, 24)}<span>{n}</span></div>' for n in P) + '</div></div>'))
    # buttons
    states = ["", "hov", "prs", "foc", "dis"]
    rows = "".join(f'<div class="t-small" style="font-weight:700;align-self:center">{lab}</div>' + "".join(f'<button class="btn {c} {st}">{t}</button>' for st in states) for lab, c, t in
                   [("Primary", "p", "Send"), ("Secondary", "s", "Later"), ("Ghost", "g", "See all"), ("Danger", "d", "Remove")])
    o.append(sec("Buttons", "Deep cobalt for the one main action, with a quiet tactile edge and a pressed state that sinks. White secondary with a hairline and lip. Icons only where they help you recognise the action.",
        f'<div class="grid g2"><div class="box"><div class="grid" style="grid-template-columns:90px repeat(5,1fr);gap:14px;justify-items:start">'
        f'<span></span>' + "".join(f'<span class="t-cap muted">{x}</span>' for x in ("Default", "Hover", "Pressed", "Focus", "Disabled")) + rows + '</div>' + f'<div style="margin-top:28px">{lbl("group · link")}</div><div class="flexw"><span class="btngroup split"><button class="btn p">Publish</button><button class="btn p icon" aria-label="More publish options">{ic("down", 16)}</button></span><span class="seg" role="tablist"><span>Week</span><span class="on">Month</span><span>Year</span></span><button class="btn link">How payouts work</button></div></div>'
        f'<div class="box">{lbl("sizes")}<div class="flexw"><button class="btn p sm">Small 36</button><button class="btn p">Medium 44</button><button class="btn p lg">Large 52</button></div>'
        f'<div style="margin-top:22px">{lbl("with icon · icon only")}</div><div class="flexw"><button class="btn p">{ic("upload", 20)}Upload review</button><button class="btn s">{ic("share", 20)}Share</button>'
        f'<button class="btn s icon" aria-label="More">{ic("more", 22)}</button><button class="btn s icon" aria-label="Close">{ic("x", 20)}</button><button class="btn g">See all {ic("arrow", 18)}</button></div>'
        f'<div style="margin-top:22px">{lbl("full width · loading")}</div><div class="stack"><button class="btn p lg block">Apply for this drop</button><button class="btn p lg block" aria-busy="true"><span class="spin"></span>Sending…</button></div>'
        f'</div></div>'))
    # inputs & selection
    o.append(sec("Inputs & selection", "44px fields and search. Labels sit above, help below. Errors say what to do.",
        f'<div class="grid g3"><div class="box stack">'
        f'<div class="field"><div class="labrow"><label>Full name</label><span>Required</span></div><div class="input"><span class="ph">e.g. Riya Sharma</span></div></div>'
        f'<div class="field"><label>Email · hover</label><div class="input hov">{ic("mail", 18)}<span>riya@studio.in</span><span class="trail">{ic("x", 16)}</span></div></div>'
        f'<div class="field"><label>Payout amount · focus</label><div class="input foc"><span class="addon">₹</span><span class="num">1,240</span><span class="trail t-small">INR</span></div><span class="help">Minimum ₹100 per payout</span></div>'
        f'<div class="field"><label>Instagram handle · error</label><div class="input err"><span class="addon">{soc("Instagram", 16)}</span><span class="ph">yourhandle</span></div><span class="help err">{ic("alert", 14)}Add your handle so brands can see your work.</span></div>'
        f'<div class="field"><label>UPI ID · valid</label><div class="input ok">{bank("hdfc", 18)}<span>riya@okhdfcbank</span><span class="trail" style="color:var(--hd-success)">{ic("check", 18)}</span></div><span class="help ok">{ic("check", 14)}Verified · Riya Sharma</span></div>'
        f'<div class="field"><label>PAN · disabled</label><div class="input dis">{ic("lock", 18)}<span class="mono">ABCDE1234F</span></div></div>'
        f'<div class="field"><label>Category</label><div class="input"><span style="flex:1">Skincare</span><span class="trail">{ic("down", 18)}</span></div></div>'
        f'<div class="field"><label>Password</label><div class="input"><span class="num" style="letter-spacing:.2em">••••••••</span><span class="trail">{ic("eye", 18)}</span></div></div>'
        f'</div>'
        f'<div class="box stack"><div class="search">{ic("search", 18)}Search drops, brands<span class="kbd">⌘K</span></div><div class="search foc">{ic("search", 18)}<span class="q">glo</span><span class="clr">{ic("x", 11, sw=3)}</span></div>'
        f'<div class="suggest" style="margin-top:-6px"><div class="sg hl">{ic("search", 18)}<span><b>glo</b>w serum</span><span class="sub">23 drops {kbd("↵")}</span></div><div class="sg">{ic("search", 18)}<span><b>glo</b>ss lip oil</span><span class="sub">4 drops</span></div>'
        f'<div class="sg-h">Drops</div><div class="sg"><img src="{PH["serum"]}" alt=""><span><b>Glo</b>w serum, 30 ml<span class="m"> · you earn ₹1,240</span></span><span class="sub">Lumen Labs</span></div>'
        f'<div class="sg-h">Brands</div><div class="sg"><span class="sg-logo">{av("GL", 1, 28)}</span><span><b>Glo</b>Theory</span><span class="sub">6 live drops</span></div>'
        f'<div class="sg-h">Recent</div><div class="sg">{ic("clock", 18)}<span class="m">night cream</span><span class="sub sg-x">{ic("x", 14)}</span></div><div class="sg-f"><span>{kbd("↑")}{kbd("↓")} move</span><span>{kbd("↵")} open</span><span>{kbd("esc")} close</span></div></div>'
        f'<div class="field"><div class="labrow"><label>Your review</label><span>Optional</span></div><div class="input textarea">Used it every night for two weeks. Skin feels…</div><span class="help">Be specific about what changed<span class="cnt">120 / 600</span></span></div>'
        f'<div class="field"><label>Verification code</label><div class="otp2 num" role="group" aria-label="6-digit code"><span class="f">4</span><span class="f">8</span><span class="f">2</span><i></i><span class="on"></span><span></span><span></span></div></div>'
        f'</div>'
        f'<div class="box stack"><div class="flexw"><span class="check on">{ic("check", 16, "#fff", 3)}</span><span class="kt-body">Checkbox on</span><span class="check"></span><span class="kt-body">off</span></div>'
        f'<div class="flexw"><span class="radio on"></span><span class="kt-body">Radio on</span><span class="radio"></span><span class="kt-body">off</span></div>'
        f'<div class="flexw"><span class="switch on"></span><span class="kt-body">Notifications</span><span class="switch"></span><span class="kt-body">off</span></div>'
        f'<div>{lbl("filter chips")}<div class="flexw"><span class="chip on">{ics("drop", 16)}Skincare</span><span class="chip">{ic("lipstick", 16)}Makeup</span><span class="chip">{ic("shirt", 16)}Fashion</span><span class="chip">{ic("lamp", 16)}Home</span><span class="chip">{ic("sliders", 16)}Filters</span></div></div>'
        f'<div>{lbl("slider")}<div class="slider"><i></i><b></b></div><div class="flexw t-small muted" style="justify-content:space-between;margin-top:10px"><span>₹0</span><span class="num">₹5,000</span></div></div>'
        f'<div>{lbl("focus · keyboard")}<div class="flexw"><span class="chip foc">{ic("drop", 16)}Skincare</span><span class="check on foc">{ic("check", 16, "#fff", 3)}</span><span class="radio foc"></span><span class="switch on foc"></span><button class="btn s sm foc">Later</button></div></div>'
        f'<div>{lbl("radio cards")}<div class="grid g2" style="gap:8px"><div class="row sel" style="flex-direction:column;align-items:flex-start;gap:4px"><span class="radio on"></span><b class="t-small" style="margin-top:4px">Per review</b><small class="t-cap muted">Pay ₹1,240 each</small></div>'
        f'<div class="row" style="flex-direction:column;align-items:flex-start;gap:4px"><span class="radio"></span><b class="t-small" style="margin-top:4px">Flat fee</b><small class="t-cap muted">One price, any reach</small></div></div></div>'
        f'<div>{lbl("checkbox list")}<div class="stack" style="gap:8px">' + "".join(f'<div class="row"><span class="check {"on" if on else ""}">{ic("check", 14, "#fff", 3) if on else ""}</span>{soc(k, 18)}<div class="tx"><b>{t}</b></div><span class="t-small muted num">{m}</span></div>' for t, k, m, on in (("Instagram", "Instagram", "18.4k", True), ("YouTube", "Youtube", "6.1k", True), ("Threads", "Threads", "2.3k", False))) + '</div></div></div></div>'))
    # navigation
    o.append(sec("Navigation", "Bars are strips, not cards: a hairline edge and nothing else. Underline tabs sit straight under the bar. One tab bar on phone, one bare header on desktop.",
        f'<div class="grid g2 xa-nav"><div class="box"><div class="lbl">Phone</div><div class="xa-phone">'
        f'<div class="xa-bar">{ic("back", 20)}<span class="ttl">Drop details</span>{ic("share", 20)}{ic("more", 20)}</div>'
        f'<div class="xa-bar"><img src="{LOGO[theme]}" style="height:20px"><span class="ttl"></span>{ic("search", 20)}<span class="xa-bell">{ic("bell", 20)}<i></i></span></div>'
        f'<div class="tabs xa-tabs"><span class="on">{ics("foryou", 16, "var(--hd-accent)")}For you</span><span>{ics("trending", 16, "var(--hd-tone-vermilion)")}Trending</span><span>{ics("heart", 16, "var(--hd-tone-mint)")}Saved</span></div>'
        f'<div class="xa-fill"></div>{tabbar("Wallet")}</div></div>'
        f'<div class="box"><div class="lbl">Desktop</div><div class="xa-desk"><div class="xa-crumb"><span class="crumb">Lumen Labs{ic("chev", 14)}<b>Campaigns</b></span><span class="xa-bell">{ic("bell", 20)}<i></i></span></div>'
        f'<div class="xa-ph"><div><div class="xa-h">Campaigns</div><p>Every drop you run, and who is reviewing it.</p></div><button class="btn p sm">{ic("plus", 16)}New</button></div></div></div></div>'))
    # data display
    o.append(sec("Data display", "Every list item is its own rounded card. Product images sit bare, no plate behind them.",
        f'<div class="grid g3"><div class="box stack">'
        f'<div class="row"><img class="lead" src="{PH["serum"]}"><div class="tx"><b>Glow serum, 30 ml</b><small>Lumen Labs · 120 creators</small></div><span class="badge success">Live</span></div>'
        f'<div class="row"><img class="lead" src="{PH["cream"]}"><div class="tx"><b>Night cream, 50 g</b><small>Lumen Labs · 42 creators</small></div><span class="badge warning">To check</span></div>'
        f'<div class="row">{av("RS", 0)}<div class="tx"><b>Riya Sharma</b><small>@riya.glows · 18.4k</small></div><div class="end"><b class="num">₹1,240</b><small class="muted t-cap">paid</small></div></div>'
        f'<div class="row"><div class="tx"><b>Notifications</b><small>Drops, payouts, reviews</small></div><span class="switch on"></span></div>'
        f'<div class="row"><span class="skel" style="width:48px;height:48px"></span><div class="tx"><span class="skel" style="display:block;height:12px;width:60%"></span><span class="skel" style="display:block;height:10px;width:40%;margin-top:8px"></span></div></div></div>'
        f'<div class="box stack xa-d2"><div class="flexw"><span class="badge success">Live</span><span class="badge warning">To check</span><span class="badge danger">Rejected</span><span class="badge info">New</span><span class="badge neutral">Paid</span></div>'
        f'<div class="flexw xa-avrow">{av("RS",0,24)}{av("RS",0,32)}{av("RS",0,40)}<img class="xa-photo" src="{PEOPLE["women-68"]}" alt=""><div class="avs xa-stack">{av("RS",0)}{av("AK",1)}{av("MJ",2)}<span class="xa-more">+9</span></div></div>'
        f'<div class="xa-stats">' + stat("Earned this month", "₹8,460", "+24%", True, spark=EARN, uid="kd") +
        f'<div class="panel stat k-rate2"><div class="sh"><span class="sl">Avg. rating</span></div><div class="sv"><b class="num">4.7</b><span class="xa-st">' + "".join(ics("star", 14, "var(--hd-star)") for _ in range(5)) + '</span></div>'
        f'<div class="vz"><div class="xa-rcap"><span class="xa-rbar"><b style="width:78%"></b></span><span>78% five-star · from 62 reviews</span></div></div></div></div></div>'
        f'<div class="box">' + vtl([("done", "Applied", "Nov 12 · approved in 2 h"), ("done", "Shipped", "Nov 13 · Delhivery 4471 2280"), ("now", "Out for delivery", "Today, by 7 pm"), ("", "Review due", "7 days after delivery")]) +
        f'<div style="margin-top:20px">' + goal("Slots filled", 84, 120).replace('<span class="su">/ 120</span>', '<span class="su">of 120</span>') + f'</div><div style="margin-top:20px"><div class="lblgap">{lbl("star input")}<div class="stars">' + "".join(ic("star", 22, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(4)) + ic("star", 22, "var(--hd-track-strong)", 1.5) + '</div></div></div></div></div>'))
    # feedback & overlays
    o.append(sec("Feedback & overlays", "Notices explain, toasts confirm, dialogs ask. One action each.",
        f'<div class="grid g3"><div class="box stack"><div class="notice info">{icf("info")}<span>Reviews go live after the brand approves them, usually within a day.</span></div>'
        f'<div class="notice warning">{icf("warning")}<span>₹640 is held until your review is approved.</span></div>'
        f'<div class="notice success">{icf("success")}<span>Payout sent to HDFC ••6093.</span></div><div class="notice danger">{icf("danger")}<span>Link not public. Make the post public and try again.</span></div>'
        f'<div class="lblgap">{lbl("toast")}<div class="flexw"><div class="toast"><span class="ok">{ics("success", 18)}</span>Review submitted<b>Undo</b></div></div></div><div class="lblgap">{lbl("tooltip")}<div class="flexw" style="padding-bottom:6px"><span class="tooltip">Paid within 48 h of approval</span></div></div></div>'
        f'<div class="box" style="display:flex;flex-direction:column;gap:18px;align-items:center"><div class="dialog n-dlg2 sm"><div class="d2b"><b class="d2t">Remove this review?</b><p class="d2p">The brand will no longer see it, and the slot opens for someone else.</p></div>'
        f'<div class="d2f"><button class="btn s sm">Keep review</button><button class="btn d sm">Remove</button></div></div>'
        f'<div class="menu n-ctx"><div class="hl">{ic("share", 16)}Share drop</div><div>{ic("heart", 16)}Save</div><div>{ic("link", 16)}Copy link</div><i class="n-sep"></i><div class="dg">{ic("x", 16)}Not interested</div></div></div>'
        f'<div class="box" style="padding:18px;display:flex;justify-content:center"><div class="sheetdemo"><div class="sd-ghost sd-photo"><img src="{PH["serum"]}" alt=""><div class="sd-pt"><b>Glow serum, 30 ml</b><span>Lumen Labs · You earn ₹1,240</span></div></div><div class="scrim"></div>'
        f'<div class="sheet sd-sheet"><div class="grab"></div><div class="t-h2">Where should we ship it?</div><p class="t-small muted" style="margin:4px 0 14px">We’ll send Glow serum here.</p>'
        f'<div class="stack" style="gap:8px"><div class="row sel"><span class="radio on"></span><div class="tx"><b>Home</b><small>14 Park Street, Kolkata 700016</small></div></div><div class="row"><span class="radio"></span><div class="tx"><b>Work</b><small>Salt Lake Sector V, Kolkata</small></div></div>'
        f'<button class="btn p block sd-cta">Confirm address</button></div><div class="home-ind" style="margin-top:6px;height:18px"><i></i></div></div></div></div></div>'))
    # empty & tables
    o.append(sec("Empty states & tables", "Empty states use one illustration and one next step. Tables are for desktop only.",
        f'<div class="grid g2 eb-wrap"><div class="stack" style="gap:12px"><div class="lbl">Empty state</div><div class="card eb-empty2"><img src="{ILL[("search",theme)]}" alt=""><b class="e2t">No drops near you yet</b><p class="e2p">New brands join every week. We’ll tell you the moment one ships to Kolkata.</p>'
        f'<button class="btn p e2b">{ic("bell", 18)}Turn on alerts</button><a class="e2l">Browse all drops</a></div>'
        f'<div class="lbl" style="margin-top:8px">Meanwhile, popular nearby</div><div class="grid g3" style="gap:12px">' + "".join(f'<div class="card eb-near2"><img src="{PH[i]}" alt=""><div class="en-b"><b>{t}</b><span>You earn <b class="num">{e}</b></span><small class="num">{l}</small></div></div>' for i, t, e, l in (("serum", "Glow serum, 30 ml", "₹1,240", "36 of 120 left"), ("cream", "Night cream, 50 g", "₹990", "58 of 100 left"), ("bottles", "Daily cleanser trio", "₹640", "72 of 90 left"))) + '</div></div>'
        f'<div class="stack" style="gap:12px"><div class="lbl">Table</div><div class="card" style="overflow:hidden"><table class="tbl eb-tbl"><tr><th>Creator</th><th>Campaign</th><th>Status</th><th style="text-align:right">Payout</th></tr>' +
        "".join(f'<tr><td><div class="tcell"><img class="tav" src="{STOCK}/people/{a}.jpg" alt=""><b>{n}</b></div></td><td class="muted">{c}</td><td><span class="tst {b}">{ics({"success":"success","warning":"clock","neutral":"check","danger":"danger"}[b], 14)}{bl}</span></td><td class="num tpay{" nil" if p == "−" else ""}">{p}</td></tr>'
                for a, k, n, c, b, bl, p in [("women-68", 0, "Riya Sharma", "Glow serum", "success", "Approved", "₹1,240"), ("men-12", 1, "Arjun Kapoor", "Night cream", "warning", "In review", "₹990"),
                                             ("women-44", 2, "Meera Joshi", "Daily cleanser trio", "neutral", "Paid", "₹640"), ("women-21", 3, "Tanvi Nair", "Glow serum", "danger", "Rejected", "−")]) + '</table></div></div></div>'))
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
    return phone(f'<div class="xm1-bar xm1-s"><img class="av" src="{PEOPLE["women-68"]}" alt="Riya Sharma">{ic("search")}<span class="bell">{ic("bell")}<i></i></span></div>'
                 f'<div class="xm1-s xm1-home"><div class="xm1-head"><h1 class="xm1-h">Hi, Riya</h1><p class="xm1-earn"><b>₹8,460</b> earned this month <em>+24%</em></p></div>'
                 f'<div class="tabs"><span class="on">{ics("foryou", 16, "var(--hd-accent)")}For you</span><span>{ics("trending", 16, "var(--hd-tone-vermilion)")}Trending</span><span>{ics("heart", 16, "var(--hd-tone-mint)")}Saved</span></div>'
                 f'<div class="xm1-card"><img src="{PH["serum_hero"]}" alt=""><div class="top"><span class="chip">{ic("clock", 14)}Ends Thu</span><span class="x-disc" aria-label="Save">{ic("heart", 18)}</span></div>'
                 f'<div class="bt"><small>Lumen Labs</small><b>Glow serum, 30 ml</b><div class="mt"><span>You earn <em>₹1,240</em></span><span><em>36</em> of 120 left</span></div><i class="sl"><u style="width:70%"></u></i></div></div>'
                 f'<div class="xm1-sech"><b>More drops</b><button class="btn link">See all</button></div>'
                 f'<div class="xm1-two"><div class="xm1-mini"><img src="{PH["cream"]}" alt=""><b>Night cream, 50 g</b><small>Earn <em>₹990</em> · 58 left</small></div>'
                 f'<div class="xm1-mini"><img src="{PH["bottles"]}" alt=""><b>Daily cleanser trio</b><small>Earn <em>₹640</em> · 72 left</small></div></div></div>'
                 f'{tabbar("Home")}', label="Home")

def s_detail():
    st = lambda n, t: f'<div class="cp-st"><i class="num">{n}</i><span>{t}</span></div>'
    task = lambda ic_, t, d: f'<div class="cp-task">{ic_}<div class="tx"><b>{t}</b><small>{d}</small></div></div>'
    return phone(f'<div class="xm1-s xm1-det xq-cp"><div class="ph"><img src="{PH["serum_hero"]}" alt=""><div class="tb"><span class="x-disc">{ic("back", 22)}</span><span style="display:flex;gap:10px"><span class="x-disc">{ic("heart", 20)}</span><span class="x-disc">{ic("share", 20)}</span></span></div></div>'
                 f'<div class="sh"><div class="cp-head"><span class="cp-store">{plat("nykaa", 16)}Nykaa</span><p class="by">Lumen Labs</p>'
                 f'<h1 class="xm1-t">Glow serum, 30 ml</h1><p class="cp-close">Closes 26 Nov 2026 · <b>8 spots left</b></p></div>'
                 f'<div class="cp-calc cp2"><div class="hd"><span>You get back</span><b class="num">₹1,339</b><small>After the brand approves</small></div>'
                 f'<div class="r"><span>Cashback <em>60% of ₹1,899</em></span><b class="num">₹1,139</b></div>'
                 f'<div class="r"><span>Bonus</span><b class="num">₹200</b></div>'
                 f'<div class="ft"><span>You pay <b class="num">₹1,899</b> on Nykaa</span><span>It costs you <b class="num">₹560</b></span></div></div>'
                 f'<div class="cp-sec"><h2>How it works</h2><div class="cp-steps">{st(1, "Buy it on Nykaa")}{st(2, "Post 2 tasks")}{st(3, "Get ₹1,339 back")}</div></div>'
                 f'<div class="cp-sec"><h2>What you\'ll create</h2>'
                 f'{task(soc("Instagram", 24), "Instagram reel", "Link, screenshots, #ad and the Paid partnership label")}'
                 f'{task(plat("nykaa", 24), "Nykaa review", "Link, a screenshot and 40+ words")}</div>'
                 f'<div class="cp-sec"><h2>Brief</h2><div class="cp-dd"><div><b>Do</b><p>Show it on bare skin in daylight.</p><p>Say how it felt after a week.</p></div>'
                 f'<div><b>Don\'t</b><p>Compare it with other brands.</p><p>Use filters on the product.</p></div></div></div></div>'
                 f'<div class="cp-bar cp-bar2"><div class="l"><b class="num">₹1,339 back</b><small>45 days to post after you join</small></div><button class="btn p lg">Join campaign</button></div></div>', label="Campaign")

def s_apply():
    under = f'<div class="x-photo"><img src="{PH["serum_hero"]}" alt=""></div><div class="x-sheet"><div class="x-title">Glow serum, 30 ml</div></div>'
    return phone(f'<i class="xm2m" data-s="apply"></i>' + under + f'<div class="scrim"></div><div class="overlay"><div class="sheet"><div class="grab"></div><div class="xm2-h">Where will you post?</div>'
                 f'<div class="xm2-ch"><div class="xm2-c on"><span class="radio on"></span>{soc("Instagram", 24)}<div class="tx"><b>Instagram</b><small>@riya.glows · 18.4k followers</small></div></div>'
                 f'<div class="xm2-c"><span class="radio"></span>{soc("Youtube", 24)}<div class="tx"><b>YouTube</b><small>Riya Sharma · 6.1k subscribers</small></div></div></div>'
                 f'<div class="xm2-c xm2-ship">{ic("home", 20)}<div class="tx"><b>Ship to Home</b><small>14 Park Street, Kolkata 700016</small></div>{ic("chev", 18)}</div>'
                 f'<button class="btn p block">Send application</button><span class="xm2-hint">Brands usually reply within a day</span></div></div>', label="Apply (sheet)")

def s_track():
    tl = vtl([("done", "Approved", "Nov 12, 4:10 pm"), ("done", "Shipped", "Nov 13 · Delhivery 4471 2280"), ("now", "Out for delivery", "6 stops away in Kolkata"), ("", "Delivered", "Expected today")])
    return phone(f'<i class="xm2m" data-s="track"></i><div class="topbar">{ic("back")}<span class="ttl"></span>{ic("more")}</div><div class="body">'
                 f'<div class="xm2-hero"><img src="{PH["scooter"]}" alt=""><div><div class="xm2-big">Arrives by 7 pm</div><span class="xm2-sub">Kick scooter · out for delivery today</span></div></div>'
                 f'{tl}'
                 f'<div class="xm2-c xm2-cour"><span class="x-tile bankt"><img class="bankl" src="assets/banks/delhivery.png" alt="Delhivery" width="22" height="22"></span><div class="tx"><b>Ravi, Delhivery</b><small>4471 2280</small></div><button class="btn s icon" aria-label="Call Ravi">{ic("phone", 18)}</button></div>'
                 f'<div class="xy-due">{ic("clock", 18)}<span>Review due Fri, Nov 27 · 7 days after delivery</span></div></div>{tabbar("Drops")}', label="Parcel tracking")

def s_review():
    th = "".join(f'<div class="xm2-ph"><img src="{PH[i]}" alt=""><span aria-label="Remove">{ic("x", 10, "currentColor", 3)}</span></div>' for i in ("serum", "bottles"))
    return phone(f'<i class="xm2m" data-s="review"></i><div class="topbar">{ic("x")}<span class="ttl"></span><span class="t-small" style="color:var(--hd-fg-subtle);font-weight:600">Draft saved</span></div><div class="body">'
                 f'<div><div class="xm2-h">Your review</div><span class="xm2-sub">Night cream · due Mon, Nov 23</span></div>'
                 f'<div class="field"><label>How was it?</label><div class="stars">' + "".join(ic("star", 32, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(4)) + ic("star", 32, "var(--hd-track-strong)", 1.5) + '</div></div>'
                 f'<div class="field"><label>Photos and video</label><div class="xm2-phs">{th}<div class="xm2-add">{ic("plus", 22)}</div></div></div>'
                 f'<div class="field"><label>Post link</label><div class="input">{soc("Instagram", 18)}<span class="t-body">instagram.com/p/C9x…</span></div></div>'
                 f'<div class="field"><label>A few words</label><div class="input textarea t-body">Used it every night for a week. Rich but not greasy, and my skin feels softer by morning.</div><span class="help xm2-cnt">86 of 600</span></div></div>'
                 f'<div class="cta"><button class="btn s">Preview</button><button class="btn p" style="flex:1">Submit review</button></div>', label="Submit review")

def s_wallet():
    tx = [("trolley", "Kitchen trolley", "Review approved · Wed, Nov 18", "+₹640", "in"), ("bank", "Payout to HDFC ••6093", "Sent · Mon, Nov 16", "−₹2,000", "out"), ("chair", "Ergo office chair", "Review approved · Wed, Nov 11", "+₹480", "in")]
    from uikit2 import spark_area
    def lead(i): return bank("hdfc", 24, tile=True) if i == "bank" else f'<img class="lead" src="{PH[i]}" alt="">'
    rows = "".join(f'<div class="xm2-c xm2-tx">{lead(i)}<div class="tx"><b>{t}</b><small>{d}</small></div><b class="num w-amt {k}">{a}</b></div>' for i, t, d, a, k in tx)
    return phone(f'<i class="xm2m" data-s="wallet"></i><div class="topbar x-large"><span class="ttl x-page">Wallet</span>{ic("clock")}{ic("settings")}</div><div class="body">'
                 f'<div class="xm2-wh"><small>Available</small><div class="xm2-wr"><div class="xm2-wb num"><span>₹</span>6,820</div><button class="btn p">Withdraw</button></div><small>₹990 held · next payout Tue, Nov 24</small></div>'
                 f'<div class="xm2-c xm2-earn"><div><small>Earned this month</small><b class="num">₹8,460</b></div><div class="xm2-sp">{spark_area(EARN, uid="wm")}</div><em>+24%</em></div>'
                 f'<div class="xm2-ah"><b>Activity</b><button class="btn link">See all</button></div>'
                 f'<div class="xm2-list">{rows}</div></div>{tabbar("Wallet")}', label="Wallet")

def s_success():
    return phone(f'<div class="topbar"><span class="ttl"></span>{ic("x")}</div><div class="body xm3-s xm3-succ">'
                 f'<img src="{ILL[("approved","light")]}" alt="">'
                 f'<h1 class="xm3-h">Review approved</h1>'
                 f'<div class="xy-pay">{bank("hdfc", 24, tile=True)}<div class="tx"><b><span class="num">₹990</span> to HDFC ••6093</b><small>Lands by Tue, Nov 24</small></div></div></div>'
                 f'<div class="cta xm3-cta"><button class="btn p lg block">Find your next drop</button><button class="btn s block">Share your review</button></div>', label="Success")

def s_notifs():
    def item(tile, text, sub, time, unread=False):
        return (f'<div class="xm3-nr">{tile}<div class="xm3-nt"><p>{text}</p><small>{sub}</small></div>'
                f'<div class="xm3-ne"><span class="num">{time}</span><i class="{"on" if unread else ""}"></i></div></div>')
    t = lambda c, i: f'<span class="x-tile {c}">{ics(i, 20)}</span>'
    today = (item(t("cobalt", "box"), "<b>Glow serum</b> is open for you", "Lumen Labs · 36 slots left", "2m", True)
             + item(t("mint", "fast"), "<b>Kick scooter</b> is out for delivery", "Arrives by 7 pm", "1h", True)
             + item(t("marigold", "clock"), "<b>Night cream</b> review due Monday", "Nov 23 · 3 days left", "4h"))
    week = (item(bank("hdfc", 22, tile=True), "<b>₹2,000</b> sent to HDFC ••6093", "Lands by Tue, Nov 24", "Mon")
            + item(t("vermilion", "linkbroken"), "Your post link is private", "Make it public so we can verify it", "Wed"))
    return phone(f'<div class="topbar x-large"><span class="ttl x-page">Notifications</span><button class="btn link">Mark all read</button></div><div class="body xm3-s xm3-notifs">'
                 f'<span class="xm3-day">Today</span><div class="xm3-nl">{today}</div><span class="xm3-day">This week</span><div class="xm3-nl">{week}</div></div>', label="Notifications")

def s_profile():
    chev = f'<span class="chevr">{ic("chev", 18)}</span>'
    def gi(icon, label, tail=chev): return f'<div class="xm3-gi">{ic(icon, 20)}<b>{label}</b>{tail}</div>'
    account = (gi("user", "Personal details") + gi("link", "Linked accounts", soc("Instagram", 18) + soc("Youtube", 18) + chev) +
               gi("bank", "Payout method", f'<span class="meta xz-bk">{bank("hdfc", 16)}••6093</span>{chev}'))
    prefs = gi("bell", "Notifications", '<span class="switch on"></span>') + gi("privacy", "Privacy") + gi("help", "Help and support")
    stats = "".join(f'<div><b class="num">{v}</b><small>{kk}</small></div>' for v, kk in (("52", "Reviews"), ("4.9", "Rating"), ("18.4k", "Reach")))
    return phone(f'<div class="topbar xm3-top xz-ptop"><span class="ttl">You</span>{ic("settings")}</div><div class="body xm3-s xm3-prof xz-prof">'
                 f'<div class="xz-idc"><div class="xm3-id"><img src="{PEOPLE["women-68"]}" alt=""><div><div class="xm3-nm">Riya Sharma {vhex(16)}</div><span>@riya.glows · Kolkata</span></div><button class="btn s sm">Edit</button></div>'
                 f'<div class="xm3-stats">{stats}</div></div>'
                 f'<div class="xm3-grp">{account}</div><div class="xm3-grp">{prefs}</div>'
                 f'<div class="xm3-grp xz-outg"><div class="xm3-out">{ic("logout", 20)}<b>Log out</b></div></div></div>{tabbar("You")}', "dark", "Profile · dark", "#fff")

def s_empty():
    pop = [("lipstick", "Lip balm"), ("drop", "Face mist"), ("headphones", "Earbuds"), ("lamp", "Desk lamp"), ("shirt", "Linen shirt")]
    sim = [("serum", "Glow serum, 30 ml", "Lumen Labs", "+₹1,240"), ("cream", "Night cream", "Lumen Labs", "+₹990"), ("bottles", "Daily cleanser trio", "Lumen Labs", "+₹640")]
    rows = "".join(f'<div class="xm3-lr"><img src="{PH[i]}" alt=""><div class="xm3-lt"><b>{t}</b><small>{b}</small></div><b class="num xm3-amt">{r}</b></div>' for i, t, b, r in sim)
    return phone(f'<div class="searchbar"><div class="search foc">{ic("search", 18)}<span class="q">matcha whisk</span><span class="clr">{ic("x", 11, sw=3)}</span></div><button class="btn link" style="text-decoration:none">Cancel</button></div>'
                 f'<div class="body xm3-s xm3-emp"><div class="xm3-nil xz-nil2"><b>No results for “matcha whisk”</b><p>We’ll tell you when a brand lists one. <a class="xz-al">{ic("bell", 15)}Turn on alert</a></p></div>'
                 f'<div class="xm3-sec"><b>Popular right now</b><div class="xm3-chips">' + "".join(f'<span>{ic(i, 16)}{p}</span>' for i, p in pop) + '</div></div>'
                 f'<div class="xm3-sec"><div class="xm3-sh"><b>Live now</b><button class="btn link">See all</button></div><div class="xm3-ll">{rows}</div></div></div>{tabbar("Drops")}', label="Empty search")

MOBILE = [s_welcome, s_otp, s_home, s_detail, s_apply, s_track, s_review, s_wallet, s_success, s_notifs, s_profile, s_empty]

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
    import importlib, xlead, xa, xb, xc, xd, xe, xf, xg, xm1, xm2, xm3, xs, xy, xq1, xq2, xr1, xr2, xr3, xr4, xz
    return xlead.XLEAD + xa.XA + xb.XB + xc.XC + xd.XD + xe.XE + xf.XF + xg.XG + xm1.XM1 + xm2.XM2 + xm3.XM3 + xs.XS + xy.XY + xq1.XQ1 + xq2.XQ2 + xr1.XR1 + xr2.XR2 + xr3.XR3 + xr4.XR4 + xz.XZ
def html(body, title, base=""): return f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{title}</title><link rel=icon type='image/svg+xml' href='assets/favicon.svg'>{f'<base href={chr(34)}{base}{chr(34)}>' if base else ''}<style>{_snap(CSS)}{_snap(CSS2)}{PAGE_CSS}{XPASS}{XSTEPS}{_late()}</style></head><body>{_snap(badgeize(body))}<script>{SQJS}</script></body></html>"

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
