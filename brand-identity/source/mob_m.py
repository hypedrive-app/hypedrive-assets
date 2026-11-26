"""Mediator phone screens (agent md, v4). Built from kit components: dm- (kit4), mn- (kit5), cv-wal (Ink card), .row/.tabs/.chip/.badge/.btn/.switch/.slider/.notice/.sheet. Spec: MEDIATOR-SPEC.md."""
from uikit2 import *

AV = {"kavya": f"{STOCK}/people/women-21.jpg", "asha": f"{STOCK}/people/women-65.jpg", "rohan": f"{STOCK}/people/men-12.jpg",
      "meera": f"{STOCK}/people/women-44.jpg", "sunita": f"{STOCK}/people/women-68.jpg"}
def av(k, s=40): return f'<img class="md-av s{s}" src="{AV[k]}" alt="">'
def lead(src): return f'<img class="lead" src="{src}" alt="">'
def ph(k): return lead(PH[k])
def pa(k): return lead(AV[k]).replace('class="lead"', 'class="lead" style="border-radius:50%"')


def dock(active):
    def it(n, i):
        on = n == active
        return f'<div class="m6-di{" on" if on else ""}">{ics(i, 24) if on else ic(i, 24)}<span>{n}</span></div>'
    return ('<div class="m6-dock">' + it("Today", "home") + it("Enrollments", "enrolled")
            + f'<div class="m6-di m6-new"><i>{ic("plus", 22, "#fff", 2.4)}</i><span>New</span></div>'
            + it("Deals", "tag") + it("Wallet", "wallet") + '</div>')

def bar(left="", right=""): return f'<div class="xm1-bar xm1-s w5-bar"><span class="l">{left}</span><span class="r">{right}</span></div>'
def page(*parts): return '<div class="xm1-s w5 m6-pg m7">' + "".join(parts) + '</div>'
def h1(t, inbar=False): return f'<h1 class="w5-h1{" w5-inbar" if inbar else ""}">{t}</h1>'
def lead_(t): return f'<p class="w5-lead">{t}</p>'
def sh(t, right=""): return f'<div class="w5-sh"><h2>{t}</h2>{f"<span>{right}</span>" if right else ""}</div>'
def wrow(img, title, meta, trail=None, cls="", round_=False):
    return (f'<div class="w5-row {cls}"><img{" class=m6-pa" if round_ else ""} src="{img}" alt=""><div class="tx"><b>{title}</b><small>{meta}</small></div>'
            + (ic("chev", 16) if trail is None else trail) + '</div>')
def utabs(items, on, icons=None):
    out = ""
    for n in items:
        ico = ""
        if icons:
            name, col = icons[n]
            ico = ics(name, 16, col) if n == on else ic(name, 16, col)
        cnt = ""
        if isinstance(n, tuple): pass
        out += f'<span{" class=on" if n == on else ""}>{ico}{n}</span>'
    return f'<div class="tabs w5-tabs">{out}</div>'
def ftabs(items, on):
    """status filter tabs: (icon, colour, label, count)"""
    out = "".join(f'<span{" class=on" if t == on else ""}>{(ics if t == on else ic)(i, 16, c)}{t} <span class="tc">{k}</span></span>' for i, c, t, k in items)
    return f'<div class="tabs w5-tabs">{out}</div>'
def lk(t): return f'<em class="w5-lk">{t}</em>'

def sheet(under, title, step="", body="", foot=""):
    return (under + '<div class="scrim"></div><div class="overlay"><div class="sheet md-sheet"><div class="grab"></div>'
            f'<div class="md-sh2"><div>{f"<small>{step}</small>" if step else ""}<h2>{title}</h2></div><span class="md-x">{ic("x", 22)}</span></div>{body}{foot}</div></div>')

# ------------------------------------------------------------------ 1 Today
def mcard(label, amount, line, foot):
    """White money card (creator Home structure): label, one hero figure, one muted sentence, a footer row."""
    return (f'<div class="m7-money"><small>{label}</small><b class="num">{amount}</b><p>{line}</p>'
            f'<div class="m7-ft">{foot}</div></div>')
def payto(action):
    return f'{bank("hdfc", 20)}<span>To kavya@okhdfc</span>{action}'

def _today():
    money = mcard("You can withdraw", "₹3,240", "<b class=num>₹2,440</b> is held for paybacks",
                  payto(lk("Withdraw")))
    pay = (f'<div class="w5-row m7-due"><img class="m6-pa" src="{AV["asha"]}" alt=""><div class="tx"><b>Pay Asha ₹1,195</b>'
           f'<small>Glow serum · 20 Nov</small></div><button class="btn p sm">Mark paid</button></div>')
    return (bar(av("kavya", 32), ic("search", 22) + f'<span class="bell">{ic("bell", 22)}<i></i></span>')
            + page('<p class="m7-date">Friday, 20 Nov</p>', h1("Hi, Kavya"), money,
                   sh("Needs you", "3"), pay,
                   wrow(AV["rohan"], "Rohan Das", "<span class='warn'>Fix tasks</span> · Night cream", round_=True),
                   wrow(AV["meera"], "Meera Joshi", "Due 28 Nov · Daily cleanser trio", round_=True))
            + dock("Today"))

def s_m_today(): return phone(_today(), label="Mediator · Today")

# ------------------------------------------------------------------ 2 Deals + slice sheet
def _deals_top(on):
    return (bar(h1("Deals", True), ic("search", 22) + ic("sliders", 22)) , utabs(["Campaigns", "My deals"], on))

def _deals_page():
    b, t = _deals_top("Campaigns")
    rows = (wrow(PH["serum"], "Glow serum, 30 ml", "60% + ₹200 to split · <span class='warn'>8 spots left</span>")
            + wrow(PH["cream"], "Night cream, 50 g", "₹1,980 · 50% to split")
            + wrow(PH["bottles"], "Daily cleanser trio", "55% + ₹100 to split"))
    return b + page(t, rows) + dock("Deals")

def s_m_deals():
    sl = lambda t, pct, val, hint: (f'<div class="md-sl"><div class="t"><b>{t}</b><span class="num">{val}</span></div>'
                                    f'<div class="slider"><i style="inset:0 {100-pct}% 0 0"></i><b style="left:{pct}%"></b></div><small>{hint}</small></div>')
    mb = ('<div class="w5-sum m6-sumsheet"><small>You keep</small><b class="num">₹144</b><dl>'
          '<dt>You get from Hypedrive</dt><dd>₹1,339</dd><dt>Shopper gets</dt><dd>₹1,195</dd></dl></div>')
    body = (sl("Cashback you keep", 10.2, "5%", "Shopper gets 55%. Up to 49% of the 60% to split.")
            + sl("Bonus you keep", 25, "₹50", "Shopper gets ₹150. What you leave goes to the shopper.") + mb)
    foot = '<p class="md-note">Shoppers never see what you keep.</p><button class="btn p lg block">Add to store</button>'
    return phone(sheet(_deals_page(), "Set what you keep", "Glow serum, 30 ml", body, foot), label="Mediator · Deals, set what you keep")

# ------------------------------------------------------------------ 3 My deals
def s_m_store():
    b, t = _deals_top("My deals")
    store = (f'<div class="m7-store"><div class="m6-sl"><span class="x-tile w5-ti">{ics("link", 20, "var(--hd-accent)")}</span><div class="tx"><b>Kavya\'s store</b>'
             '<small>orders.hypedrive.app/m/3VQJHP41</small></div><button class="btn s sm">Share</button></div>'
             '<div class="m6-sw"><span>Take new enrollments</span><span class="switch on"></span></div></div>')
    return phone(b + page(t, store, sh("In your store", "3"),
                 wrow(PH["serum"], "Glow serum, 30 ml", "You keep 5% + ₹50 · <span class='warn'>8 spots left</span>"),
                 wrow(PH["cream"], "Night cream, 50 g", "You keep 5%"),
                 wrow(PH["bottles"], "Daily cleanser trio", "Paused · you keep 5% + ₹40", cls="m7-mute"))
                 + dock("Deals"), label="Mediator · My deals")

# ------------------------------------------------------------------ 4 Enroll a shopper (step 2)
def s_m_enroll():
    offered = wrow(PH["serum"], "Glow serum, 30 ml", "55% + ₹150 back · You keep ₹144", ics("ok", 22), "m6-sel")
    no = lambda k, t, why: wrow(PH[k], t, why, " ", "m6-no")
    body = ('<div class="segs">' + "".join(f'<i class="{"on" if i < 2 else ""}"></i>' for i in range(4)) + '</div>'
            + '<p class="m6-for">Deals for Sunita Pillai</p>' + offered
            + no("cream", "Night cream, 50 g", "Sunita is already enrolled.")
            + no("set", "Clear skin set", "Takes applications, so you can't enroll a shopper."))
    foot = '<button class="btn p lg block">Continue</button>'
    return phone(sheet(_today(), "Pick a deal", "Step 2 of 4", body, foot), label="Mediator · Enroll a shopper")

# ------------------------------------------------------------------ 5 One enrollment with the payback
def s_m_enrollments():
    contact = f'<span class="m6-ct">{ic("phone", 20)}{soc("Whatsapp", 20)}</span>'
    prod = (f'<div class="w5-prod"><img class="m6-pa" src="{AV["asha"]}" alt=""><div><b>Asha Verma</b><small>Glow serum · enrolled 12 Nov</small></div>{contact}</div>')
    steps = ('<div class="w5-steps">' + "".join(
        f'<div class="w5-st {k}"><i>{ics("check", 12, "#fff") if k == "done" else ""}</i><span>{t}</span></div>'
        for t, k in [("Joined", "done"), ("Tasks", "done"), ("Approved", "done"), ("Paid out", "done"), ("Payback", "now")]) + '</div>')
    sm = mcard("Asha is owed", "₹1,195", "55% back on her ₹1,899 order. Hypedrive paid you <b class=num>₹1,339</b>, you keep <b class=num>₹144</b>.",
               '<span class="m7-hint">Send by UPI or bank, then mark it paid</span><button class="btn p sm">Mark paid</button>')
    return phone(bar(ic("back", 22), ic("more", 22))
                 + page(prod, h1("Pay Asha back"), lead_("Asha confirms once she gets it."), steps, sm, sh("Her order"),
                        wrow(PH["serum"], "Glow serum, 30 ml", f'{plat("nykaa", 13)} Nykaa · ordered 13 Nov · ₹1,899', ""))
                 + dock("Enrollments"), label="Mediator · Enrollment, payback")

# ------------------------------------------------------------------ 6 Wallet
def s_m_wallet():
    money = mcard("You can withdraw", "₹3,240", "<b class=num>₹2,440</b> is held for paybacks",
                  payto('<button class="btn p sm">Withdraw</button>'))
    r = lambda k, t, m, a: wrow(PH[k], t, m, f'<b class="num m6-amt">{a}</b>')
    return phone(bar(h1("Wallet", True), ic("settings", 22))
                 + page(money, sh("Kept in November", "₹1,236"),
                        r("serum", "Glow serum, 30 ml", "5% + ₹50 bonus · 9 shoppers", "₹720"),
                        r("cream", "Night cream, 50 g", "5% · 4 shoppers", "₹330"),
                        r("bottles", "Daily cleanser trio", "5% + ₹40 bonus · 2 shoppers", "₹186"))
                 + dock("Wallet"), label="Mediator · Wallet")

# ------------------------------------------------------------------ 7 TrustDrive
def s_m_trust():
    tile = lambda i, c: f'<span class="x-tile w5-ti">{ics(i, 20, c)}</span>'
    trow = lambda i, c, t, m, a: f'<div class="w5-row w5-task">{tile(i, c)}<div class="tx"><b>{t}</b><small>{m}</small></div>{lk(a)}</div>'
    seg = [("Confirmed", 36, "var(--hd-success)"), ("In progress", 2, "var(--hd-accent)"), ("Partly paid", 1, "var(--hd-tone-marigold)"), ("Disputed", 1, "var(--hd-danger)")]
    barh = "".join(f'<i style="flex:{n};background:{c}"></i>' for _, n, c in seg)
    leg = "".join(f'<span><i style="background:{c}"></i>{t} <b class="num">{n}</b></span>' for t, n, c in seg)
    score = (f'<div class="m7-money m7-score"><small>Paid back on time</small><b class="num">95%</b>'
             f'<p><b class=num>38</b> of 40 shoppers · {ics("star", 14, "var(--hd-tone-marigold)")}<b class=num>4.8</b> from 31 reviews</p>'
             f'<div class="m7-bar">{barh}</div><div class="m7-leg">{leg}</div></div>')
    return phone(bar(h1("TrustDrive", True))
                 + page(utabs(["Overview", "Reviews", "Requests", "Listing"], "Overview"), score, sh("Needs you", "3"),
                        trow("users", "var(--hd-accent)", "Takeover request", "<span class='warn'>Answer in 2 days</span>", "Review"),
                        trow("star", "var(--hd-tone-marigold)", "Calm otter", "Rated you 5 stars · 18 Nov", "Reply"),
                        trow("star", "var(--hd-tone-marigold)", "Swift heron", "Rated you 4 stars · 15 Nov", "Reply"))
                 + dock(""), label="Mediator · TrustDrive")

MED = [s_m_today, s_m_deals, s_m_store, s_m_enroll, s_m_enrollments, s_m_wallet, s_m_trust]
