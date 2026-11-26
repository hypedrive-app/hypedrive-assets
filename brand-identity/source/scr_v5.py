"""Creator screens, v5 (lead, 2026-11-26): white pages, inline headers and progress, imagery first,
cards only for list items (owner rule: data lists are separate rounded cards). Researched against
order-detail and deals screens from Amazon, eBay, TikTok Shop, IKEA and PayPal (Mobbin)."""
from uikit2 import *
from kit4 import _cc, _st

BA = "assets/brand"


def _top(left="", right=""):
    return f'<div class="xm1-bar xm1-s w5-bar"><span class="l">{left}</span><span class="r">{right}</span></div>'


def _steps(labels, cur):
    out = ""
    for i, t in enumerate(labels):
        k = "done" if i < cur else ("now" if i == cur else "")
        dot = ics("check", 12, "#fff") if i < cur else ""
        out += f'<div class="w5-st {k}"><i>{dot}</i><span>{t}</span></div>'
    return f'<div class="w5-steps">{out}</div>'


# ------------------------------------------------------------------ onboarding
def s_onboarding():
    field = lambda label, val, extra="": f'<label class="w5-f"><span>{label}</span><div class="w5-in">{val}{extra}</div></label>'
    body = (
        _top(ic("back", 22), '<span class="w5-prog"><i class="on"></i><i></i></span>')
        + '<div class="xm1-s w5 w5-ob">'
        '<h1 class="w5-h1">Tell brands about you</h1>'
        '<p class="w5-lead">Brands see your name when you join their campaigns.</p>'
        '<div class="w5-two">' + field("First name", "Riya") + field("Last name", "Sharma") + '</div>'
        '<p class="w5-hint">Use the name on your PAN, so payouts match it.</p>'
        '<div class="w5-f"><span>Gender</span><div class="w5-seg"><span class="on">Female</span><span>Male</span><span>Other</span></div></div>'
        + field("Date of birth", "14 Mar 1998", f'<i class="w5-ic">{ic("calendar", 18)}</i>')
        + '</div>'
        '<div class="w5-bb"><p>Next: verify your PAN · optional</p><button class="btn p lg block">Continue</button></div>')
    return phone(body, label="Onboarding")


# ------------------------------------------------------------------ browse
def s_browse():
    tile = lambda ph, store, name, back, bonus, state, cls="": (
        f'<div class="w5-tile {cls}"><div class="w5-tp"><img src="{PH[ph]}" alt=""></div>'
        f'<span class="w5-sr">{plat(store, 13)}{store.title()}</span><b class="w5-tn">{name}</b>'
        f'<span class="w5-back">{back}{f"<em>+{bonus}</em>" if bonus else ""}</span>{state}</div>')
    tabs = [("grid", "var(--hd-accent)", "All", "8"), ("clock", "var(--hd-tone-marigold)", "Ending soon", "2"),
            ("spark", "var(--hd-info)", "New", "3"), ("heart", "var(--hd-tone-vermilion)", "Saved", "1")]
    chips = "".join(f'<span{" class=on" if i == 0 else ""}>{ics(n, 16, c)}{t} <span class="tc">{k}</span></span>' for i, (n, c, t, k) in enumerate(tabs))
    body = (
        _top('<h1 class="w5-h1 w5-inbar">Campaigns</h1>', ic("sliders", 22) + ic("search", 22))
        + '<div class="xm1-s w5 w5-br">'
        f'<div class="tabs w5-tabs">{chips}</div>'
        f'<div class="w5-feat"><img src="{PH["flatlay"]}" alt=""><span class="w5-tag">{plat("nykaa", 13)}6 spots left</span>'
        '<div class="w5-ft"><small>Rose toner · Lumen Labs</small><b>Get ₹780 back</b><span>50% back + ₹150 bonus</span></div></div>'
        '<div class="w5-sh"><h2>Open for you</h2></div>'
        '<div class="w5-grid">'
        + tile("sand", "nykaa", "Skin routine kit", "40% back", "₹150 bonus", '<span class="w5-state ok">Ready to join</span>')
        + tile("mask", "nykaa", "Clay mask, 100 g", "45% back", "", '<span class="w5-state">Applied</span>')
        + '</div></div>' + tabbar("Campaigns"))
    return phone(body, label="Campaigns")


# ------------------------------------------------------------------ enrollments
def s_enrollments():
    row = lambda ph, name, meta, cls="": (f'<div class="w5-row"><img src="{PH[ph]}" alt=""><div class="tx"><b>{name}</b>'
                                         f'<small class="{cls}">{meta}</small></div>{ic("chev", 16)}</div>')
    sh = lambda t, n: f'<div class="w5-sh"><h2>{t}</h2><span>{n}</span></div>'
    body = (
        _top('<h1 class="w5-h1 w5-inbar">Enrollments</h1>')
        + '<div class="xm1-s w5 w5-en">'
        + sh("Your turn", 3)
        + row("serum", "Glow serum, 30 ml", "Submit 2 tasks · due in 41 days")
        + row("bottles", "Daily cleanser trio", "Fix 1 task · due in 6 days", "warn")
        + row("sand", "Skin routine kit", "Ready to join · by 26 Nov")
        + sh("Their turn", 3)
        + row("set", "Clear skin set", "On the way · arrives Mon, 23 Nov")
        + row("cream", "Night cream, 50 g", "In review · ₹990 back")
        + row("mask", "Clay mask, 100 g", "Applied · waiting for the brand")
        + '</div>' + tabbar("Enrolled"))
    return phone(body, label="Enrollments")


# ------------------------------------------------------------------ enrollment detail (two states)
def s_enrollment_detail(state="turn"):
    review = state == "review"
    if review:
        prod = ("cream", "Night cream, 50 g", "amazon", "Amazon")
        title, sub, cur = "In review", "Lumen Labs checks your tasks, usually in 2 days", 3
        tasks = [(soc("Instagram", 22), "Instagram reel", "Sent 18 Nov", ""), (plat("amazon", 22), "Amazon review", "Sent 18 Nov", "")]
        money = ("₹990", [("Order on Amazon", "₹1,980", ""), ("Cashback, 50%", "₹990", "in")], "Paid to your wallet when Lumen Labs approves")
        foot = ""
    else:
        prod = ("serum", "Glow serum, 30 ml", "nykaa", "Nykaa")
        title, sub, cur = "Submit 2 tasks", "Due in 41 days · post, then add the links here", 2
        tasks = [(soc("Instagram", 22), "Instagram reel", "Link + screenshots · #ad", "Start"),
                 (plat("nykaa", 22), "Nykaa review", "Link + screenshot · 40+ words", "Start")]
        money = ("₹1,339", [("Order on Nykaa", "₹1,899", ""), ("Cashback, 60%", "₹1,139", "in"), ("Bonus", "₹200", "in")], "Paid to your wallet when Lumen Labs approves")
        foot = '<div class="w5-bb"><button class="btn p lg block">Start the Instagram reel</button></div>'
    task = lambda lead, t, m, act: (f'<div class="w5-row w5-task"><span class="x-tile w5-ti">{lead}</span><div class="tx"><b>{t}</b><small>{m}</small></div>'
                                    + (ic("chev", 16) if act else ics("check", 18, "var(--hd-success-strong)")) + '</div>')
    body = (
        _top(ic("back", 22), ic("more", 22))
        + '<div class="xm1-s w5 w5-dt">'
        f'<div class="w5-prod"><img src="{PH[prod[0]]}" alt=""><div><b>{prod[1]}</b><small>Lumen Labs · {plat(prod[2], 13)}{prod[3]}</small></div></div>'
        f'<h1 class="w5-h1">{title}</h1><p class="w5-lead">{sub}</p>'
        + _steps(["Joined", "Bought", "Tasks", "Review", "Paid"], cur)
        + f'<div class="w5-sh"><h2>Tasks</h2><span>{"2 of 2 sent" if review else "0 of 2 sent"}</span></div>'
        + "".join(task(*t) for t in tasks)
        + f'<div class="w5-sum"><small>You get back</small><b class="num">{money[0]}</b><dl>'
        + "".join(f'<dt>{k}</dt><dd class="{c}">{v}</dd>' for k, v, c in money[1])
        + f'</dl><p>{money[2]}</p></div>'
        + f'</div>{foot}')
    return phone(body, label="Enrollment · in review" if review else "Enrollment detail")
