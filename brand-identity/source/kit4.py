"""Domain components: campaign + enrollment (built from the real business logic, see CREATOR-SPEC.md)."""
from uikit2 import *

def sec(title, desc, body, cls=""):
    return f'<section class="sec nw {cls}"><h2>{title}</h2><p>{desc}</p>{body}</section>'

def _g(title, note, body, cols=3):
    return (f'<div class="dm-grp"><div class="dm-gh"><b>{title}</b><span>{note}</span></div>'
            f'<div class="dm-row c{cols}">{body}</div></div>')
def _lbl(t): return f'<div class="dm-lbl">{t}</div>'
def _cell(label, inner): return f'<div class="dm-cell">{_lbl(label)}{inner}</div>'
def _kv(k, v, cls=""): return f'<div class="dm-kv {cls}"><span>{k}</span><b class="num">{v}</b></div>'

# 1 ---------------------------------------------------------------- campaign card
def _cc(photo, store, title, by, back, bonus, spots="", state="", barter=False, cls="", worth=""):
    lead = (f'<b class="dm-bk">Free product</b><span class="dm-w">Worth {worth}</span>' if barter
            else f'<b class="dm-bk num">{back}</b>')
    bn = f'<span class="dm-bn num">+{bonus} bonus</span>' if bonus else ""
    sp = f'<span class="dm-sp"><b class="num">{spots}</b></span>' if spots else ""
    stt = f'<div class="dm-state">{state}</div>' if state else ""
    return (f'<div class="dm-cc {cls}"><div class="dm-ph"><img src="{PH[photo]}" alt=""></div>'
            f'<div class="dm-cb"><div class="dm-sr"><span class="dm-store">{plat(store, 14)}{store.title()}</span><span class="dm-by">{by}</span></div>'
            f'<div class="dm-ti">{title}</div><div class="dm-pay">{lead}{bn}</div>'
            f'<div class="dm-ft">{sp}{stt}</div></div></div>')

def _st(kind, icon, text):
    return f'<span class="dm-pill {kind}">{ics(icon, 13) if icon else ""}{text}</span>'

def cards():
    c = [
        _cell("Open · 8 spots left", _cc("serum", "nykaa", "Glow serum, 30 ml", "Lumen Labs", "60% back", "₹200", "8 spots left")),
        _cell("Joined", _cc("cream", "amazon", "Night cream, 50 g", "Lumen Labs", "50% back", "", "", _st("ok", "check", "Joined"))),
        _cell("Closing soon", _cc("bottles", "nykaa", "Daily cleanser trio", "Lumen Labs", "55% back", "₹100", "3 spots left", _st("warn", "clock", "Closing soon"))),
        _cell("Full", _cc("mask", "nykaa", "Clay mask, 100 g", "Lumen Labs", "45% back", "", "", _st("mute", "", "Full"), cls="muted")),
        _cell("Opens {date}", _cc("flatlay", "myntra", "Cotton co-ord set", "Weave & Co", "40% back", "₹150", "", _st("mute", "calendar", "Opens 28 Nov 2026"))),
        _cell("Barter", _cc("set", "nykaa", "Clear skin set", "Lumen Labs", "", "₹500", "", "", barter=True, worth="₹2,400")),
    ]
    return _g("Campaign card", "Spots show only at 10 or fewer. A state sits at the foot, one at a time.", "".join(c), 6)

# 2 ---------------------------------------------------------------- payout card
def payout():
    online = (f'<div class="dm-po dm-po6"><span class="k">You get back</span><b class="num big">₹1,339</b>'
              f'<p class="mix"><b class="num">₹1,139</b> cashback (60%) + <b class="num">₹200</b> bonus · after the brand approves</p>'
              f'<div class="ft"><span>You pay <b class="num">₹1,899</b> on Nykaa</span><span>It costs you <b class="num">₹560</b></span></div></div>')
    barter = (f'<div class="dm-po dm-po6"><span class="k">You get</span><b class="big">Free product</b>'
              f'<p class="mix">Clear skin set, worth <b class="num">₹2,400</b> + <b class="num">₹500</b> bonus · after the brand approves</p>'
              f'<div class="ft"><span>You pay <b class="num">₹0</b></span><span>Shipped to you</span></div></div>')
    return _g("Payout card", "The number that matters leads; the sum sits underneath.", _cell("Online purchase", online) + _cell("Barter", barter), 2).replace("dm-row c2", "dm-row c2 n")

# 3 ---------------------------------------------------------------- join CTA states
def ctas():
    def c(label, btn, note, extra=""):
        return _cell(label, f'<div class="dm-cta">{btn}{extra}<small>{note}</small></div>')
    p = lambda t, d="": f'<button class="btn p lg block"{d}>{t}</button>'
    s = lambda t, d="": f'<button class="btn s lg block"{d}>{t}</button>'
    body = (c("Open", p("Join campaign"), "You're eligible to join")
            + c("Apply first", p("Apply to join"), "The brand reviews applications before you join")
            + c("Accepted, with a deadline", p("Join by 26 Nov 2026"), "You're accepted. 8 spots left.")
            + c("Applied", s("View your application"), "Applied · waiting for the brand")
            + c("Already in", s("Open your enrollment"), "You have already enrolled in this campaign.")
            + c("Not open yet", p("Opens 28 Nov 2026", " disabled") , "Opens 28 Nov 2026.", s("Notify me"))
            + c("Full", p("Full", " disabled"), "No spots left right now.", f'<button class="btn g lg block">Tell me when a place opens</button>'))
    return _g("Join CTA states", "The server decides which one shows. One button leads each state.", body, 4)

# 4 ---------------------------------------------------------------- spot hold
def hold():
    h = lambda t, cls="": f'<div class="jf-hold2 dm-h2 {cls}">{ics("clock", 16)}<span>Spot held · <b class="num">{t}</b> left</span><button class="jf-add">Add 10 min</button></div>'
    ended = f'<div class="jf-hold2 dm-h2 ended">{ics("clock", 16)}<span>Your hold ended · you can still order if a spot is free</span></div>'
    return _g("Spot hold", "One slim line: time left, one extension. Shows inside the join sheet.",
              _cell("Held", h("9:41")) + _cell("Running low", h("1:48", "low")) + _cell("Ended", ended), 3)

# 5 ---------------------------------------------------------------- receipt
def receipt():
    up = (f'<div class="dm-rc"><div class="dz">{ic("upload", 22)}<b>Upload your receipt or invoice</b><small>PNG, JPG or PDF · the order total and date must show</small></div>'
          f'<button class="btn s block">{ic("camera", 18)}Choose a file</button></div>')
    chk = (f'<div class="dm-rc mid"><div class="file"><i></i><div><b>nykaa-order.pdf</b><small>284 KB</small></div></div>'
           f'<div class="wait"><span class="spin"></span><div><b>Checking your receipt</b><small>This takes about 20 seconds. Keep this open.</small></div></div></div>')
    ok = (f'<div class="dm-rc"><div class="res ok">{ics("success", 22)}<div><b>Your receipt is verified</b><small>Nykaa · ₹1,899 · 20 Nov 2026</small></div></div>'
          f'<button class="btn p block">Join and earn ₹1,339</button></div>')
    bad = (f'<div class="dm-rc"><div class="res bad">{ics("danger", 22)}<div><b>We couldn\'t verify this receipt</b><small>Make sure the store, date and total are visible, then send it again.</small></div></div>'
           f'<button class="btn s block">Send a different receipt</button></div>')
    return _g("Receipt upload and check", "Upload, wait, then pass or fail with a way forward.",
              _cell("Upload", up) + _cell("Checking", chk) + _cell("Passed", ok) + _cell("Failed", bad), 4)

# 6 ---------------------------------------------------------------- apply sheet
def apply_sheet():
    def sheet(ig):
        return (f'<div class="dm-sheet"><div class="grab"></div><div class="hd"><b>Apply to join</b><span class="dm-x">{ic("x", 16)}</span></div>'
                f'<div class="dm-mini"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><small>Lumen Labs · Nykaa</small></div></div>'
                f'<div class="f"><div class="lr"><label>Why you</label><span class="num">86 of 500</span></div>'
                f'<div class="input textarea t-body">I post daily skincare routines for sensitive skin, and I\'d show this on bare skin in daylight.</div></div>'
                f'{ig}'
                f'<div class="f"><div class="lr"><label>Bonus you\'d like</label><span>Optional</span></div>'
                f'<div class="input"><span class="t-body muted">₹</span><span class="t-body num">150</span></div><small>The campaign pays up to ₹200 bonus.</small></div>'
                f'<button class="btn p lg block">Send application</button><small class="c">The brand picks creators by 28 Nov 2026. You\'ll hear back here.</small></div>')
    conn = (f'<div class="f"><div class="lr"><label>Instagram</label></div><div class="dm-ig">{soc("Instagram", 24)}<div><b>@riya.glows</b><small>Connected · 18.4k followers</small></div>{ics("success", 18, "var(--hd-success)")}</div></div>')
    manual = (f'<div class="f"><div class="lr"><label>Instagram</label></div><div class="input">{soc("Instagram", 18)}<span class="t-body muted">@yourhandle</span></div>'
              f'<small><a class="dm-a">Connect Instagram</a> to skip typing it</small></div>')
    conn_alt = (f'<div class="f"><div class="lr"><label>Instagram</label></div><div class="input">{soc("Instagram", 18)}<span class="t-body">@riya.glows</span></div>'
                f'<small>Typed in by hand · <a class="dm-a">Use the connected account</a></small></div>')
    ig_c = conn[:-6] + '<small><a class="dm-a">Add your handle instead</a></small></div>'
    return _g("Apply sheet content", "Four things, in this order. The handle is connected or typed.",
              _cell("Connected Instagram", sheet(ig_c)) + _cell("Handle added by hand", sheet(conn_alt)), 2)

# 7 ---------------------------------------------------------------- task card
def tasks():
    chips = lambda *t: '<div class="dm-chips">' + "".join(f'<span>{x}</span>' for x in t) + '</div>'
    def head(kind, title, state):
        ico = soc("Instagram", 24) if kind == "reel" else plat("nykaa", 24)
        return f'<div class="dm-th">{ico}<div class="tx"><b>{title}</b></div>{state}</div>'
    def shots(n, of=6):
        th = "".join(f'<div class="s"><img src="{PH[k]}" alt=""><i>{ic("x", 10, "currentColor", 3)}</i></div>' for k in ["serum", "bottles", "cream", "set", "mask", "flatlay"][:n])
        add = f'<div class="s add">{ic("plus", 20)}</div>' if n < of else ""
        return f'<div class="dm-shots">{th}{add}</div><small class="dm-cnt num">{n} of {of} screenshots</small>'
    link = lambda v="": f'<div class="f"><label>Link to your reel</label><div class="input">{ic("link", 16)}<span class="t-body {"" if v else "muted"}">{v or "instagram.com/reel/…"}</span></div></div>'
    todo = (f'<div class="dm-task">{head("reel", "Instagram reel", _st("info", "", "To do"))}'
            f'{chips("#ad", "Paid partnership label", "Link", "Screenshots")}{link()}<div class="f"><label>Screenshots</label>{shots(3)}</div></div>')
    sent = (f'<div class="dm-task">{head("rev", "Nykaa review", _st("mute", "check", "Sent"))}{chips("40+ words", "1 screenshot")}'
            f'<div class="dm-done">{ic("link", 16)}<span>nykaa.com/…/reviews/8841</span></div><small class="muted t-small">Sent 21 Nov 2026 · the brand is reviewing it</small></div>')
    fix = (f'<div class="dm-task">{head("reel", "Instagram reel", _st("warn", "alert", "Fix needed"))}'
           f'<div class="dm-note"><b>Note from Lumen Labs</b><p>The #ad label is hidden behind the caption. Show it in the first line and send it again.</p></div>'
           f'{link("instagram.com/reel/C9x7aQ2")}</div>')
    lock = (f'<div class="dm-task lock">{head("reel", "Instagram reel", _st("mute", "lock", "Locked"))}{chips("#ad", "Paid partnership label")}'
            f'<div class="dm-lk">{ics("lock", 16)}<span>Opens when your order arrives.</span></div></div>')
    one = f'<div class="dm-task slim">{_lbl("1 screenshot")}{shots(1)}</div>'
    six = f'<div class="dm-task slim">{_lbl("6 screenshots, the most")}{shots(6)}</div>'
    return (_g("Task card", "Reel and review kinds, requirements as chips, one link and 1 to 6 screenshots.",
               _cell("To do", todo) + _cell("Sent", sent) + _cell("Fix needed", fix) + _cell("Locked (barter)", lock), 4)
            + _g("Screenshots, 1 to 6", "The add tile goes away at six.", _cell("One", one) + _cell("Six", six), 2))

# 8 ---------------------------------------------------------------- submit bar
def submit():
    att = "I confirm these posts are mine, live now, and follow the brief."
    def bar(title, sub, btn, dis=False, att_=True, ready=2):
        d = " disabled" if dis else ""
        a = f'<p class="at">{ics("privacy", 14)}{att}</p>' if att_ else ""
        return (f'<div class="dm-sb"><div class="r"><div><b>{title}</b><small>{sub}</small></div><button class="btn p lg"{d}>{btn}</button></div>{a}</div>')
    return _g("Submit bar", "Counts what is ready, then asks for one confirmation.",
              _cell("Some ready", bar("1 of 2 ready", "Add the review link and a screenshot", "Submit 2 tasks", True, False))
              + _cell("All ready", bar("2 of 2 ready", "Due in 41 days", "Submit 2 tasks"))
              + _cell("After a fix", bar("1 of 1 ready", "The reel with the brand's note", "Resubmit 1 task")), 3)

# 9 ---------------------------------------------------------------- next step header
def nextstep():
    def n(photo, badge, title, sub, ico, cls=""):
        return (f'<div class="dm-ns {cls}"><img src="{PH[photo]}" alt=""><div class="tx">{badge}<b>{title}</b>'
                f'<small>{ics(ico, 14)}{sub}</small></div></div>')
    return _g("Enrollment next-step header", "Your turn, their turn, done. The heading says who acts.",
              _cell("Your turn", n("serum", _st("info", "", "Submit tasks"), "Submit 2 tasks", "Due in 41 days", "clock"))
              + _cell("Their turn", n("serum", _st("mute", "", "In review"), "Glow serum is reviewing your posts", "Usually within 2 days", "clock"))
              + _cell("Done", n("serum", _st("ok", "", "Paid"), "Approved, paying you", "₹1,339 is on its way to your wallet", "success")), 3)

# 10 --------------------------------------------------------------- journey
def journey():
    def j(steps, cur):
        out = ""
        for i, s in enumerate(steps):
            k = "done" if i < cur else ("now" if i == cur else "")
            mark = ics("check", 12) if i < cur else f'<span class="num">{i+1}</span>'
            out += f'<div class="s {k}"><i>{mark}</i><span>{s}</span></div>'
        return f'<div class="dm-jr" style="--n:{len(steps)}">{out}</div>'
    return _g("Enrollment journey", "Online purchase has four stops; barter has five. Where you are is the one cobalt ring.",
              _cell("Online purchase · tasks next", j(["Proof", "Tasks", "Review", "Paid"], 1))
              + _cell("Barter · waiting on the parcel", j(["Join", "Ship", "Tasks", "Review", "Done"], 1)), 2)

# 11 --------------------------------------------------------------- shipment
def shipment():
    def ship(stage, carrier, track, action, status):
        steps = ["Waiting for product", "On the way", "Delivered"]
        tr = "".join(f'<div class="s {"done" if (i < stage or stage == 2) else ("now" if i == stage else "")}"><i></i><span>{s}</span></div>' for i, s in enumerate(steps))
        return (f'<div class="dm-ship"><div class="h"><b>Your product</b>{status}</div><div class="dm-trk">{tr}</div>'
                f'{_kv("Ship to", "Riya Sharma, 14 Park Street, Kolkata 700016", "w")}{_kv("Carrier", carrier)}{_kv("Tracking number", track)}{action}</div>')
    return _g("Shipment card (barter)", "The brand ships; you confirm it arrived. Tasks open on delivery.",
              _cell("Waiting for product", ship(0, "<span class=\"nil\">Not shipped yet</span>", "<span class=\"nil\">Not available yet</span>", "", _st("mute", "clock", "Waiting for product")))
              + _cell("On the way", ship(1, "Delhivery", "4471 2280", '<button class="btn s block">Track shipment</button>', _st("info", "", "On the way")))
              + _cell("Delivered", ship(2, "Delhivery", "4471 2280", '<button class="btn p block">Received</button>', _st("ok", "check", "Delivered"))), 3)

# 12 --------------------------------------------------------------- money block
def money():
    def m(word, wcls, sub):
        return (f'<div class="dm-mb"><div class="h"><b>Your money</b><span class="w {wcls}">{word}</span></div>'
                f'{_kv("You paid", "₹1,899")}{_kv("Cashback <em>60%</em>", "₹1,139")}{_kv("Bonus", "₹200")}'
                f'<div class="tot"><span>You get</span><b class="num">₹1,339</b></div><small>{sub}</small></div>')
    return _g("Money block on an enrollment", "Same four lines; only the state word moves.",
              _cell("Pending", m("Released when the brand approves", "", "Nothing leaves your wallet. You only paid the store."))
              + _cell("Held", m("Held", "", "Approved. It lands after the hold on 24 Nov 2026."))
              + _cell("Paid", m("In your wallet", "ok", "Ready to withdraw.")), 3)

def kit_domain(theme):
    body = cards() + payout() + ctas() + hold() + receipt() + apply_sheet() + tasks() + submit() + nextstep() + journey() + shipment() + money()
    return sec("Campaign & enrollment", "The product's own components: a campaign, what it pays, joining it, doing the tasks and getting paid. Words, numbers and states come from the live app.", body, "dm")
