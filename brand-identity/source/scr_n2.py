"""Creator screens, part 2: Enrollment detail, Withdraw, Settings, Barter. Built from kit components (dm-ns, dm-jr, dm-ship, dm-task, dm-sb, cv-wal Ink card, eb-empty2, row, badge)."""
from uikit2 import *
from kit4 import _st, _kv
BA = "assets/brand"

def _bar(title="", right=""):
    t = f'<b class="n2-bt">{title}</b>' if title else '<span class="n2-bt"></span>'
    return f'<div class="xm1-bar xm1-s n2-bar">{ic("back", 22)}{t}{right}</div>'

def _row(lead, t, d, end=""):
    return f'<div class="row">{lead}<div class="tx"><b>{t}</b><small>{d}</small></div>{end}</div>'

def s_enrollment_detail(state="turn"):
    """Your turn (Glow serum, submit tasks) and their turn (Night cream, in review)."""
    review = state == "review"
    steps = ["Proof", "Tasks", "Review", "Paid"]
    cur = 2 if review else 1
    jr = "".join(f'<div class="s {"done" if i < cur else ("now" if i == cur else "")}"><i>{ics("check", 12) if i < cur else f"<span class=num>{i+1}</span>"}</i><span>{s}</span></div>' for i, s in enumerate(steps))
    tile = lambda g: f'<span class="x-tile">{g}</span>'
    if review:
        ns = (f'<div class="dm-ns"><img src="{PH["cream"]}" alt=""><div class="tx">{_st("mute", "", "In review")}<b>Lumen Labs is reviewing your posts</b>'
              f'<small>{ics("clock", 14)}Usually within 2 days</small></div></div>')
        t1 = _row(tile(soc("Instagram", 22)), "Instagram reel", "Sent 21 Nov 2026", '<span class="badge neutral">Sent</span>')
        t2 = _row(tile(plat("amazon", 22)), "Amazon review", "Sent 21 Nov 2026", '<span class="badge neutral">Sent</span>')
        ink = (f'<div class="cv-wal n2-ink"><small>You get back</small><div class="big"><b class="num">₹990</b></div>'
               f'<p>50% cashback</p>'
               f'<div class="ft">{ics("clock", 16, "#a0c6ff")}<span>You paid <span class="num">₹1,980</span> · released on approval</span></div></div>')
        foot = ""
    else:
        ns = (f'<div class="dm-ns"><img src="{PH["serum"]}" alt=""><div class="tx">{_st("info", "", "Submit tasks")}<b>Submit 2 tasks</b>'
              f'<small>{ics("clock", 14)}Due in 41 days</small></div></div>')
        t1 = _row(tile(soc("Instagram", 22)), "Instagram reel", "Link, screenshots · #ad label", '<span class="badge info">To do</span>')
        t2 = _row(tile(plat("nykaa", 22)), "Nykaa review", "Link, screenshot · 40+ words", '<span class="badge info">To do</span>')
        ink = (f'<div class="cv-wal n2-ink"><small>You get back</small><div class="big"><b class="num">₹1,339</b></div>'
               f'<p><span class="num">₹1,139</span> cashback + <span class="num">₹200</span> bonus</p>'
               f'<div class="ft">{ics("clock", 16, "#a0c6ff")}<span>You paid <span class="num">₹1,899</span> · released on approval</span></div></div>')
        foot = ('<div class="n2-sbw"><div class="dm-sb"><div class="r"><div><b>0 of 2 ready</b><small>Add each link first</small></div>'
                '<button class="btn p lg" disabled>Submit 2 tasks</button></div></div></div>')
    body = (
        _bar() +
        f'<div class="xm1-s n2 dm">{ns}<div class="dm-jr" style="--n:4">{jr}</div>'
        f'<div class="n2-sh"><h2>Tasks</h2></div>{t1}{t2}{ink}</div>{foot}')
    return phone(body, label="Enrollment · in review" if review else "Enrollment detail")

def s_withdraw():
    """Honest state: PAN is not verified, so the page is the blocker, with no keypad. The verified flow (amount, account, review) lives in the kit's Money section."""
    body = (
        _bar("Withdraw") +
        f'<div class="xm1-s n2 n2-wd">'
        f'<div class="card eb-empty2"><img src="{BA}/hypedrive-ill-payout-light.svg" alt=""><b class="e2t">Verify your PAN to withdraw</b>'
        f'<p class="e2p">It takes a minute and is needed once. Your <span class="num">₹6,820</span> stays safe until you do.</p>'
        f'<button class="btn p e2b">Verify PAN</button></div>'
        + _row(f'<span class="x-tile">{ic("rupee", 20)}</span>', "Available", "₹1,339 on hold", '<b class="num n2-v">₹6,820</b>')
        + _row(bank("hdfc", 24, True), "HDFC ••6093", "Fee ₹0 · usually within minutes", '<a class="n2-lk">Change</a>')
        + f'</div>')
    return phone(body, label="Withdraw")

def s_settings(theme="light"):
    dark = theme == "dark"
    row = lambda ico, t, d, cls="": f'<div class="row n2-sr">{ic(ico, 20)}<div class="tx"><b>{t}</b><small class="{cls}">{d}</small></div>{ic("chev", 16)}</div>'
    grp = lambda h, *rows: f'<div class="n2-list">' + "".join(rows) + '</div>'
    body = (
        _bar() +
        f'<div class="xm1-s n2">'
        f'<h1 class="n2-title">Settings</h1>'
        f'<div class="row n2-me"><img class="lead xt1-ava" src="{STOCK}/people/women-68.jpg" alt="Riya Sharma"><div class="tx"><b>Riya Sharma</b><small>@riya.glows · Kolkata</small></div></div>'
        + grp("Account",
              row("user", "Personal info", "Name, date of birth"),
              row("privacy", "Verification (PAN)", "Not verified", "warn"),
              row("bank", "Payout methods", "HDFC ••6093"),
              row("pin", "Addresses", "1 saved · Kolkata"))
        + grp("Security",
              row("lock", "Sign-in & security", "Phone number and sign-in"),
              row("phone", "Devices", "This phone and 1 more"))
        + grp("Preferences",
              row("bell", "Notifications", "Push and email"),
              row("sliders", "Appearance", "Dark" if dark else "Light"))
        + f'</div>')
    return phone(body, theme=theme, label="Settings · dark" if dark else "Settings")

def s_barter():
    steps = ["Waiting for product", "On the way", "Delivered"]
    trk = "".join(f'<div class="s {"done" if i < 1 else ("now" if i == 1 else "")}"><i></i><span>{s}</span></div>' for i, s in enumerate(steps))
    ship = (f'<div class="dm-ship"><div class="h"><b>Your product</b>{_st("info", "", "On the way")}</div><div class="dm-trk">{trk}</div>'
            f'{_kv("Ship to", "14 Park Street, Kolkata 700016", "w")}{_kv("Carrier", "Delhivery")}{_kv("Tracking number", "4471 2280")}'
            f'<button class="btn s block">Track shipment</button></div>')
    lock = (f'<div class="dm-task lock slim"><div class="dm-th">{soc("Instagram", 24)}<div class="tx"><b>Instagram reel</b></div>{_st("mute", "lock", "Locked")}</div>'
            f'<div class="dm-lk">{ics("lock", 16)}<span>Opens when your order arrives.</span></div></div>')
    body = (
        _bar() +
        f'<div class="xm1-s n2 dm">'
        + _row(f'<img class="lead" src="{PH["set"]}" alt="">', "Clear skin set", "Worth ₹2,400 · +₹500 bonus")
        + f'<div class="n2-moment"><img src="{BA}/hypedrive-ill-tracking-light.svg" alt=""><h1>Arriving Mon, 23 Nov</h1><p>Delhivery is bringing your Clear skin set</p></div>'
        + ship + lock + '</div>')
    return phone(body, label="Barter enrollment")
