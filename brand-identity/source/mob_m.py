"""Mediator phone screens (agent md). Spec: MEDIATOR-SPEC.md. Classes prefixed md-."""
from uikit2 import *

AV = {"kavya": f"{STOCK}/people/women-21.jpg", "asha": f"{STOCK}/people/women-65.jpg", "rohan": f"{STOCK}/people/men-12.jpg",
      "meera": f"{STOCK}/people/women-44.jpg", "sunita": f"{STOCK}/people/women-68.jpg"}
def av(k, s=40): return f'<img class="md-av s{s}" src="{AV[k]}" alt="">'
def th(k, s=48): return f'<img class="md-th s{s}" src="{PH[k]}" alt="">'

def dock(active):
    """The real mediator dock: Today, Enrollments, New, Deals, Wallet. New is a plain tab (no disc), like the creator tab bar."""
    def it(n, i):
        on = n == active
        return f'<div class="md-di{" on" if on else ""}">{ics(i, 24) if on else ic(i, 24)}<span>{n}</span></div>'
    new = f'<div class="md-di">{ic("plus", 24)}<span>New</span></div>'
    return ('<div class="md-dock">' + it("Today", "home") + it("Enrollments", "enrolled") + new + it("Deals", "tag") + it("Wallet", "wallet") + '</div>')

def bar(left="", right=""):
    return f'<div class="md-bar"><span class="l">{left}</span><span class="r">{right}</span></div>'

def sh(t, right=""):
    k = " k" if right and not str(right).isdigit() else ""
    return f'<div class="md-sh"><h2>{t}</h2>{f"<span class=\'{k.strip()}\'>{right}</span>" if right else ""}</div>'

def row(lead, title, meta, trail=""):
    return f'<div class="md-row">{lead}<div class="tx"><b>{title}</b><small>{meta}</small></div>{trail}</div>'

def tabs(items, on):
    return '<div class="md-tabs">' + "".join(f'<span class="{"on" if n == on else ""}">{n}</span>' for n in items) + '</div>'

def chips(items, on):
    return '<div class="md-chips">' + "".join(f'<span class="md-chip{" on" if n == on else ""}">{n}<i class="num">{c}</i></span>' for n, c in items) + '</div>'

def sheet(under, title, step="", body="", foot=""):
    return (under + '<div class="scrim"></div><div class="overlay"><div class="sheet md-sheet"><div class="grab"></div>'
            f'<div class="md-sh2"><div>{f"<small>{step}</small>" if step else ""}<h2>{title}</h2></div><span class="md-x">{ic("x", 22)}</span></div>{body}{foot}</div></div>')

# ------------------------------------------------------------------ 1 Today
def _today():
    pay = row(av("asha"), "Asha Verma", "<em class='warn'>Pay back ₹1,195</em>", '<button class="btn s sm">Mark paid</button>')
    return (f'<div class="md-pg">'
            + bar(av("kavya", 32), ic("search", 22) + f'<span class="bell">{ic("bell", 22)}<i></i></span>')
            + '<div class="md-hd"><h1>Morning, Kavya</h1><p>Friday, 20 Nov</p></div>'
            + '<div class="hm-wal"><small>You can withdraw</small><b class="num">₹3,240</b>'
              '<p><span class="num">₹2,440</span> to pay back · <span class="num">₹1,236</span> kept in November</p></div>'
            + sh("To do", "4") + pay
            + row(av("rohan"), "Rohan Das", "Fix tasks · Night cream")
            + row(av("meera"), "Meera Joshi", "Tasks due 28 Nov · Daily cleanser trio")
            + sh("Live deals", "See all")
            + row(th("serum"), "Glow serum, 30 ml", "8 spots left · you keep 5% + ₹50 bonus")
            + row(th("cream"), "Night cream, 50 g", "You keep 5%")
            + '</div>' + dock("Today"))

def s_m_today(): return phone(_today(), label="Mediator · Today")

# ------------------------------------------------------------------ 2 Deals + slice sheet
def _deals_page():
    card = lambda photo, store, title, line, bonus, foot, btn: (
        f'<div class="md-cc"><div class="top">{th(photo, 64)}<div class="tx"><span class="sr">{plat(store, 14)}{store.title()}</span><b>{title}</b>'
        f'<small>{line}</small><small>{bonus}</small></div></div><div class="ft"><span class="warn">{foot}</span>{btn}</div></div>')
    return (f'<div class="md-pg md-dl"><div class="md-top"><h1>Deals</h1></div>' + tabs(["Campaigns", "My deals"], "Campaigns")
            + f'<div class="md-search">{ic("search", 20)}<span>Search campaigns</span>{ic("sliders", 20)}</div>'
            + chips([("All", 4), ("New", 1), ("Saved", 2), ("Ending soon", 1)], "All")
            + card("serum", "nykaa", "Glow serum, 30 ml", "₹1,899 · 60% cashback to split", "₹200 bonus to split", "8 spots left", '<button class="btn p sm">Add to store</button>')
            + '</div>' + dock("Deals"))

def s_m_deals():
    sl = lambda t, val, pct, hint, split: (
        f'<div class="md-sl"><div class="t"><b>{t}</b><span class="num">{split}</span></div><div class="rail"><i style="width:{pct}%"></i><s style="left:{pct}%"></s></div>'
        f'<small>{hint}</small></div>')
    fig = lambda k, v: f'<div><small>{k}</small><b class="num">{v}</b></div>'
    body = (sl("Cashback you keep", "5%", 10.2, "Of the 60% to split, up to 49%", "You 5%, shopper 55%")
            + sl("Bonus you keep", "₹50", 25, "Of the ₹200 bonus, none to all. What you leave goes to the shopper.", "You ₹50, shopper ₹150")
            + '<p class="md-drag">Drag to set your share</p>'
            + '<div class="md-fig">' + fig("You get", "₹1,339") + fig("Shopper gets", "₹1,195") + fig("You keep", "₹144") + '</div>'
            + '<p class="md-note">Shoppers never see what you keep.</p>')
    foot = '<button class="btn p lg block">Add to store</button>'
    return phone(sheet(_deals_page(), "Set what you keep", "Glow serum, 30 ml", body, foot), label="Mediator · Deals, set what you keep")

# ------------------------------------------------------------------ 3 My deals
def s_m_store():
    deal = lambda photo, title, state, keep, cls="": (
        f'<div class="md-row md-deal">{th(photo, 56)}<div class="tx"><b>{title}</b>'
        f'<small>{state}</small><small>{keep}</small></div></div>')
    link = (f'<div class="md-store"><div class="lkr"><div class="tx"><b>Kavya\'s store</b><small>orders.hypedrive.app/m/3VQJHP41</small></div><button class="btn s sm">{ic("share", 16)}Share</button></div>'
            f'<div class="swr"><div class="tx"><b>Take new enrollments</b><small>Enrollments already made carry on. Switch on to take new ones.</small></div><span class="md-switch on"><i></i></span></div></div>')
    return phone('<div class="md-pg"><div class="md-top"><h1>Deals</h1></div>' + tabs(["Campaigns", "My deals"], "My deals") + link
                 + chips([("All", 3), ("Live", 2), ("Paused", 1), ("Full", 0)], "All")
                 + deal("serum", "Glow serum, 30 ml", "<em class='warn'>8 spots left</em> · Shopper 55% back", "You keep 5% + ₹50 bonus")
                 + deal("cream", "Night cream, 50 g", "Shopper 45% back", "You keep 5%")
                 + deal("bottles", "Daily cleanser trio", "<em>Paused</em> · Shopper 50% + ₹60 back", "You keep 5% + ₹40 bonus")
                 + '</div>' + dock("Deals"), label="Mediator · My deals")

# ------------------------------------------------------------------ 4 Enroll a shopper (step 2)
def s_m_enroll():
    offered = (f'<div class="md-opt on">{th("serum", 48)}<div class="tx"><b>Glow serum, 30 ml</b><small>Get 55% + ₹150 back</small><small>You keep ₹144</small></div></div>')
    no = lambda photo, t, why: f'<div class="md-opt no">{th(photo, 40)}<div class="tx"><b>{t}</b><small>{why}</small></div></div>'
    body = ('<p class="md-for">Deals for Sunita Pillai</p>' + offered
            + '<p class="md-cant">Can\'t enroll</p>'
            + no("cream", "Night cream, 50 g", "Sunita is already enrolled.")
            + no("set", "Clear skin set", "This campaign takes applications, so you can't enroll a shopper in it."))
    foot = '<button class="btn p lg block">Continue</button>'
    return phone(sheet(_today(), "Pick a deal", "Step 2 of 4", body, foot), label="Mediator · Enroll a shopper")

# ------------------------------------------------------------------ 5 One enrollment with the payback
def s_m_enrollments():
    done = lambda t, d: f'<li class="done">{ics("ok", 18)}<div><b>{t}</b></div><span>{d}</span></li>'
    return phone('<div class="md-pg">' + bar(ic("back", 22), ic("more", 22))
                 + f'<div class="md-hd md-hd2">{th("serum", 56)}<div><h1>Glow serum, 30 ml</h1><p>{plat("nykaa", 14)}Nykaa · Enrolled 12 Nov</p></div></div>'
                 + '<div class="md-pay"><h2>Pay back. Asha is owed <span class="num">₹1,195</span>.</h2>'
                 '<p>55% back on ₹1,899. Hypedrive paid you ₹1,339 and you keep ₹144.</p><button class="btn p block">Mark paid</button></div>'
                 + f'<div class="md-row md-who">{av("asha")}<div class="tx"><b>Asha Verma</b><small>Your shopper</small></div>'
                 f'<span class="md-ib">{ic("phone", 18)}</span><span class="md-ib">{soc("Whatsapp", 18)}</span></div>'
                 + '<ul class="md-jr">' + done("Enrolled", "12 Nov") + done("Tasks sent", "14 Nov") + done("Approved", "20 Nov") + done("Payout landed", "₹1,339")
                 + '<li class="now"><span class="ring"></span><div><b>Asha confirms</b><small>Did you get it? Yes · Got less · Not yet</small></div></li></ul>'
                 + '</div>' + dock("Enrollments"), label="Mediator · Enrollment, payback")

# ------------------------------------------------------------------ 6 Wallet
def s_m_wallet():
    deal = lambda photo, t, v: f'<div class="md-erow">{th(photo, 32)}<b>{t}</b><span class="num">{v}</span></div>'
    return phone('<div class="md-pg">' + f'<div class="md-top"><h1>Wallet</h1>{ic("settings", 22)}</div>'
                 + '<div class="md-bal"><small>You can withdraw</small><b class="num">₹3,240</b><p><span><span class="num">₹2,440</span> held</span><em>Held money, see why</em></p>'
                 '<button class="btn p block">Withdraw</button></div>'
                 + f'<div class="md-row md-pa">{bank("hdfc", 22, True)}<div class="tx"><b>kavya@okhdfc</b><small>UPI · withdrawals go here</small></div><em class="md-lk">Change</em></div>'
                 + '<div class="hm-wal md-earn2"><small>You keep in November</small><b class="num">₹1,236</b>'
                   '<p>9 enrollments · <span class="num">₹2,850</span> in October</p></div>'
                 + sh("By deal in November")
                 + deal("serum", "Glow serum", "₹720") + deal("cream", "Night cream", "₹330") + deal("bottles", "Daily cleanser trio", "₹186")
                 + '</div>' + dock("Wallet"), label="Mediator · Wallet")

# ------------------------------------------------------------------ 7 TrustDrive
def s_m_trust():
    stat = lambda k, v, sub="": f'<div><b class="num">{v}</b><small>{k}</small></div>'
    stars = ics("star", 14) * 5
    rev = lambda name, date: (f'<div class="md-row md-rv"><div class="tx"><b>{name}{vhex(14)}</b><small><span class="st">{stars}</span>{date} · <em class="warn">Needs reply</em></small></div>'
                              f'<button class="btn s sm">Reply</button></div>')
    take = (f'<div class="md-row"><span class="x-tile md-tl">{ic("users", 20)}</span><div class="tx"><b>Takeover request</b><small><em class="warn">2 days left</em></small></div></div>')
    return phone('<div class="md-pg"><div class="md-top"><h1>TrustDrive</h1></div>' + tabs(["Overview", "Reviews", "Requests", "Listing"], "Overview")
                 + sh("To do", "3") + take + rev("Calm otter", "18 Nov") + rev("Brave finch", "16 Nov")
                 + sh("How shoppers see you")
                 + '<div class="md-stats"><div class="hero"><b class="num">95%</b><small>Paid back</small><span>38 of 40</span></div>'
                   '<div class="hero"><b class="num">4.8</b><small>Rating</small><span>31 reviews</span></div></div>'
                 + '<div class="md-stats2">' + stat("Confirmed", 36) + stat("In progress", 2) + stat("Partly paid", 1) + stat("Disputed", 1) + stat("Complaints", 0) + '</div>'
                 + '</div>' + dock(""), label="Mediator · TrustDrive")

MED = [s_m_today, s_m_deals, s_m_store, s_m_enroll, s_m_enrollments, s_m_wallet, s_m_trust]
