"""New creator screens, part 2 (agent 3): Enrollment detail, Withdraw, Settings, Barter enrollment. Spec: CREATOR-SPEC.md."""
from uikit2 import *

def _bar(title="", right=""):
    t = f'<b class="n2-bt">{title}</b>' if title else '<span class="n2-bt"></span>'
    return f'<div class="xm1-bar xm1-s n2-bar">{ic("back", 22)}{t}{right}</div>'

def _thumb(photo, size=56):
    return f'<img class="n2-th" style="width:{size}px;height:{size}px" src="{PH[photo]}" alt="">'

def _kv(k, v, cls=""):
    return f'<div class="n2-kv {cls}"><span>{k}</span><b class="num">{v}</b></div>'

def s_enrollment_detail(state="turn"):
    """One enrollment page, two states: your turn (Glow serum, submit tasks) and their turn (Night cream, in review)."""
    review = state == "review"
    steps = ["Joined", "Bought", "Tasks", "In review", "Paid"]
    cur = 3 if review else 2
    jr = ""
    for i, s in enumerate(steps):
        k = "done" if i < cur else ("now" if i == cur else "")
        mark = ics("check", 12) if i < cur else ""
        jr += f'<div class="n2-js {k}"><i>{mark}</i><span>{s}</span></div>'
    task = lambda ico, t, d, st: (f'<div class="n2-row"><span class="x-tile n2-ti">{ico}</span><div class="tx"><b>{t}</b><small>{d}</small></div><span class="n2-st">{st}</span></div>')
    if review:
        prod = ("cream", "Night cream, 50 g", "amazon", "Amazon")
        nxt = '<small>Their turn</small><h1>In review</h1><p>Lumen Labs checks your 2 tasks · usually within 2 days</p>'
        st, money = "Sent", (_kv("You paid", "₹1,980") + _kv("Cashback <em>50%</em>", "₹990") + '<div class="n2-tot"><span>You get back</span><b class="num">₹990</b></div>')
        foot = ""
    else:
        prod = ("serum", "Glow serum, 30 ml", "nykaa", "Nykaa")
        nxt = '<small>Your turn</small><h1>Submit 2 tasks</h1><p>Due in 41 days</p>'
        st, money = "To do", (_kv("You paid", "₹1,899") + _kv("Cashback <em>60%</em>", "₹1,139") + _kv("Bonus", "₹200") + '<div class="n2-tot"><span>You get back</span><b class="num">₹1,339</b></div>')
        foot = '<div class="n2-bb"><div class="e"><b class="num">0 of 2 ready</b><small>Add each link and screenshots</small></div><button class="btn p" disabled>Submit 2 tasks</button></div>'
    body = (
        _bar() +
        f'<div class="xm1-s n2">'
        f'<div class="n2-prod">{_thumb(prod[0], 48)}<div class="tx"><b>{prod[1]}</b><small>Lumen Labs · {plat(prod[2], 14)}{prod[3]}</small></div></div>'
        f'<div class="n2-card n2-next">{nxt}<div class="n2-jr">{jr}</div></div>'
        + task(soc("Instagram", 22), "Instagram reel", "Link, screenshots · #ad, Paid partnership", st)
        + (task(plat("amazon", 22), "Amazon review", "Link, screenshot · 40+ words", st) if review else task(plat("nykaa", 22), "Nykaa review", "Link, screenshot · 40+ words", st))
        + f'<h2 class="n2-h">What you get back</h2>'
        f'<div class="n2-card n2-money">{money}</div>'
        f'</div>{foot}')
    return phone(body, label="Enrollment · in review" if review else "Enrollment detail", sbar_color=None)

def s_withdraw():
    keys = "".join(f'<span class="num">{k}</span>' for k in "123456789") + '<span class="num">.</span><span class="num">0</span><span>' + ic("back", 22) + '</span>'
    body = (
        _bar("Withdraw") +
        f'<div class="xm1-s n2 n2-wd">'
        f'<div class="n2-amt"><small>Amount</small><b class="num">₹4,000</b><p><span class="num">₹6,820</span> available · minimum <span class="num">₹100</span></p></div>'
        f'<div class="n2-row n2-acct">{bank("hdfc", 24, True)}<div class="tx"><b>HDFC ••6093</b><small>Bank account</small></div><button class="btn s sm">Change</button></div>'
        f'<div class="n2-card n2-sum">{_kv("Fee", "₹0")}{_kv("Arrives", "Usually within minutes")}<div class="n2-tot"><span>You receive</span><b class="num">₹4,000</b></div></div>'
        f'<div class="n2-keys">{keys}</div>'
        f'</div>'
        f'<div class="n2-bb"><button class="btn p">Withdraw ₹4,000</button></div>')
    return phone(body, label="Withdraw")

def s_settings(theme="light"):
    row = lambda ico, t, d, cls="": f'<div class="n2-row"><span class="x-tile n2-ti">{ic(ico, 20)}</span><div class="tx"><b>{t}</b><small class="{cls}">{d}</small></div></div>'
    body = (
        _bar() +
        f'<div class="xm1-s n2">'
        f'<h1 class="n2-title">Settings</h1>'
        f'<h2 class="n2-h">Profile</h2>'
        + row("user", "Personal info", "Riya Sharma · @riya.glows")
        + row("privacy", "Verification (PAN)", "Not verified · needed to withdraw", "")
        + f'<h2 class="n2-h">Money</h2>'
        + row("bank", "Payout methods", "HDFC ••6093")
        + row("pin", "Addresses", "1 saved · Kolkata")
        + f'<h2 class="n2-h">Security</h2>'
        + row("lock", "Sign-in & security", "Phone number and sign-in")
        + row("phone", "Devices", "This phone and 1 more")
        + f'</div>')
    return phone(body, theme=theme, label="Settings · dark" if theme == "dark" else "Settings")

def s_barter():
    def stop(k, t, d="", extra=""):
        mark = ics("check", 12) if k == "done" else ""
        dd = f'<small>{d}</small>' if d else ""
        return f'<div class="n2-vs {k}"><i>{mark}</i><div class="tx"><b>{t}</b>{dd}{extra}</div></div>'
    tl = (stop("done", "Address", "Riya Sharma, 14 Park Street, Kolkata 700016")
          + stop("now", "Shipped", "Delhivery · tracking number 4471 2280")
          + stop("", "Delivered", "Tap Received when it arrives")
          + stop("", "Tasks", "Opens when your order arrives.")
          + stop("", "Bonus paid", "+₹500 after the brand approves"))
    body = (
        _bar() +
        f'<div class="xm1-s n2">'
        f'<div class="n2-prod">{_thumb("set", 48)}<div class="tx"><b>Clear skin set</b><small>Lumen Labs · Barter</small></div></div>'
        f'<div class="n2-card n2-next"><small>Their turn</small><h1>On the way to you</h1></div>'
        f'<div class="n2-card n2-offer"><div><small>You get</small><b>Free product</b></div><div class="r"><small>Worth</small><b class="num">₹2,400</b></div><div class="r"><small>Bonus</small><b class="num">+₹500</b></div></div>'
        f'<h2 class="n2-h">Your journey</h2><div class="n2-card n2-vj">{tl}</div>'
        f'</div>'
        f'<div class="n2-bb"><button class="btn p">Track shipment</button></div>')
    return phone(body, label="Barter enrollment")
