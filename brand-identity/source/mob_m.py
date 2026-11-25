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
        return f'<div class="md-di{" on" if on else ""}">{ics(i, 24) if on else ic(i, 24)}<span>{n}</span></div>'
    return ('<div class="md-dock">' + it("Today", "home") + it("Enrollments", "enrolled") + f'<div class="md-di">{ic("plus", 24)}<span>New</span></div>'
            + it("Deals", "tag") + it("Wallet", "wallet") + '</div>')

def bar(left="", right=""): return f'<div class="md-bar"><span class="l">{left}</span><span class="r">{right}</span></div>'
def sh(t, right=""): return f'<div class="md-sh"><h2>{t}</h2>{f"<span>{right}</span>" if right else ""}</div>'
def row(lead_, title, meta, trail=""): return f'<div class="row">{lead_}<div class="tx"><b>{title}</b><small>{meta}</small></div>{trail}</div>'
def tabs(items, on): return '<div class="tabs">' + "".join(f'<span{" class=on" if n == on else ""}>{n}</span>' for n in items) + '</div>'
def chips(items, on): return '<div class="md-chips">' + "".join(f'<span class="chip{" on" if n == on else ""}">{n}</span>' for n in items) + '</div>'
def lk(t): return f'<em class="lk">{t}</em>'

def sheet(under, title, step="", body="", foot=""):
    return (under + '<div class="scrim"></div><div class="overlay"><div class="sheet md-sheet"><div class="grab"></div>'
            f'<div class="md-sh2"><div>{f"<small>{step}</small>" if step else ""}<h2>{title}</h2></div><span class="md-x">{ic("x", 22)}</span></div>{body}{foot}</div></div>')

# ------------------------------------------------------------------ 1 Today
def _today():
    ink = ('<div class="cv-wal"><small>You can withdraw</small><div class="big"><b class="num">₹3,240</b><span class="wd">Withdraw</span></div>'
           '<p><span class="num">₹2,440</span> to pay back · <span class="num">₹1,236</span> kept in November</p></div>')
    pay = (f'<div class="dm-ns"><img class="md-pf" src="{AV["asha"]}" alt=""><div class="tx"><span class="badge warning">{ics("clock", 13)}Payback due</span>'
           f'<b>Pay Asha ₹1,195</b><small>Glow serum · approved 20 Nov</small></div><button class="btn p block">Mark paid</button></div>')
    return ('<div class="md-pg">' + bar(av("kavya", 32), ic("search", 22) + f'<span class="bell">{ic("bell", 22)}<i></i></span>')
            + '<div class="md-hd"><h1>Morning, Kavya</h1><p>Friday, 20 Nov</p></div>' + ink
            + sh("To do", "See all 3") + pay
            + row(pa("rohan"), "Rohan Das", "Fix tasks · Night cream")
            + row(pa("meera"), "Meera Joshi", "Tasks due 28 Nov · Daily cleanser trio")
            + sh("Live deals", "See all")
            + row(ph("serum"), "Glow serum, 30 ml", "You keep 5% + ₹50 bonus", '<span class="badge warning">8 spots left</span>')
            + '</div>' + dock("Today"))

def s_m_today(): return phone(_today(), label="Mediator · Today")

# ------------------------------------------------------------------ 2 Deals + slice sheet
def _deals_page():
    cc = (f'<div class="dm-cc"><div class="dm-ph"><img src="{PH["serum"]}" alt=""></div><div class="dm-cb">'
          f'<div class="dm-sr"><span class="dm-store">{plat("nykaa", 14)}Nykaa</span><span class="dm-by">₹1,899</span></div>'
          f'<div class="dm-ti">Glow serum, 30 ml</div><div class="dm-pay"><b class="dm-bk num">60% cashback to split</b><span class="dm-bn num">+₹200 bonus to split</span></div>'
          f'<div class="dm-ft"><span class="dm-sp"><b class="num">8 spots left</b></span><button class="btn p sm">Add to store</button></div></div></div>')
    return ('<div class="md-pg"><div class="md-top"><h1>Deals</h1></div>' + tabs(["Campaigns", "My deals"], "Campaigns")
            + f'<div class="search">{ic("search", 20)}<span style="flex:1">Search campaigns</span>{ic("sliders", 20)}</div>'
            + chips(["All", "New", "Saved", "Ending soon"], "All") + cc + '</div>' + dock("Deals"))

def s_m_deals():
    sl = lambda t, pct, val, hint: (f'<div class="md-sl"><div class="t"><b>{t}</b><span class="num">{val}</span></div>'
                                    f'<div class="slider"><i style="inset:0 {100-pct}% 0 0"></i><b style="left:{pct}%"></b></div><small>{hint}</small></div>')
    mb = ('<div class="dm-mb"><div class="h"><b>What you keep</b></div>'
          '<div class="dm-kv"><span>You get from Hypedrive</span><b class="num">₹1,339</b></div>'
          '<div class="dm-kv"><span>Shopper gets</span><b class="num">₹1,195</b></div>'
          '<div class="tot"><span>You keep</span><b class="num">₹144</b></div></div>')
    body = (sl("Cashback you keep", 10.2, "5%", "Shopper gets 55%. Up to 49% of the 60% to split.")
            + sl("Bonus you keep", 25, "₹50", "Shopper gets ₹150. What you leave goes to the shopper.") + mb)
    foot = '<p class="md-note">Shoppers never see what you keep.</p><button class="btn p lg block">Add to store</button>'
    return phone(sheet(_deals_page(), "Set what you keep", "Glow serum, 30 ml", body, foot), label="Mediator · Deals, set what you keep")

# ------------------------------------------------------------------ 3 My deals
def s_m_store():
    card = (f'<div class="dm-cc"><div class="dm-ph v4-strip"><img src="{PH["serum"]}" alt=""><img src="{PH["cream"]}" alt=""><img src="{PH["bottles"]}" alt=""></div>'
            f'<div class="dm-cb"><div class="dm-ti">Kavya\'s store</div><div class="dm-sr">3 deals live</div>'
            f'<div class="v4-link">{ic("link", 18)}<span>orders.hypedrive.app/m/3VQJHP41</span></div>'
            f'<div class="v4-sw"><b>Take new enrollments</b><span class="switch on"></span></div>'
            f'<div class="v4-btns"><button class="btn p">Share store</button><button class="btn s">View public page</button></div></div></div>')
    deal = lambda k, t, m, badge="": row(ph(k), t, m, badge)
    return phone('<div class="md-pg"><div class="md-top"><h1>Deals</h1></div>' + tabs(["Campaigns", "My deals"], "My deals") + card
                 + deal("serum", "Glow serum, 30 ml", "<em class='warn'>8 spots left</em> · You keep 5% + ₹50")
                 + deal("cream", "Night cream, 50 g", "You keep 5%")
                 + deal("bottles", "Daily cleanser trio", "You keep 5% + ₹40 bonus", '<span class="badge neutral">Paused</span>')
                 + '</div>' + dock("Deals"), label="Mediator · My deals")

# ------------------------------------------------------------------ 4 Enroll a shopper (step 2)
def s_m_enroll():
    offered = (f'<div class="row sel">{ph("serum")}<div class="tx"><b>Glow serum, 30 ml</b><small>55% + ₹150 back · You keep ₹144</small></div>'
               f'<span class="tick">{ics("ok", 22)}</span></div>')
    no = lambda k, t, why: f'<div class="row no">{ph(k)}<div class="tx"><b>{t}</b><small>{why}</small></div></div>'
    body = (f'<div class="segs">' + "".join(f'<i class="{"on" if i < 2 else ""}"></i>' for i in range(4)) + '</div>'
            + '<p class="md-note" style="text-align:left">Deals for Sunita Pillai</p>' + offered
            + no("cream", "Night cream, 50 g", "Sunita is already enrolled.")
            + no("set", "Clear skin set", "This campaign takes applications, so you can't enroll a shopper in it."))
    foot = '<button class="btn p lg block">Continue</button>'
    return phone(sheet(_today(), "Pick a deal", "Step 2 of 4", body, foot), label="Mediator · Enroll a shopper")

# ------------------------------------------------------------------ 5 One enrollment with the payback
def s_m_enrollments():
    j = '<div class="dm-jr" style="--n:5">' + "".join(
        f'<div class="s {k}"><i>{ics("check", 12) if k == "done" else f"<span class=num>{n}</span>"}</i><span>{t}</span></div>'
        for n, (t, k) in enumerate([("Enrolled", "done"), ("Tasks", "done"), ("Approved", "done"), ("Payout", "done"), ("Confirm", "now")], 1)) + '</div>'
    hero = (f'<div class="dm-ns"><img class="md-pf" src="{AV["asha"]}" alt=""><div class="tx"><span class="badge warning">{ics("clock", 13)}Payback due</span>'
            f'<b>Asha Verma</b><small>Glow serum · enrolled 12 Nov</small></div></div>')
    po = ('<div class="dm-po dm-po6"><span class="k">Pay back Asha</span><b class="num big">₹1,195</b>'
          '<p class="mix">55% back on <b class="num">₹1,899</b> · you keep <b class="num">₹144</b></p><button class="btn p lg block">Mark paid</button></div>')
    return phone('<div class="md-pg">' + bar(ic("back", 22), ic("more", 22)) + hero + po + sh("Journey") + j
                 + f'<div class="v4-two"><button class="btn s">{ic("phone", 18)}Call</button><button class="btn s">{soc("Whatsapp", 18)}WhatsApp</button></div>'
                 + '</div>' + dock("Enrollments"), label="Mediator · Enrollment, payback")

# ------------------------------------------------------------------ 6 Wallet
def s_m_wallet():
    ink = ('<div class="cv-wal"><small>You can withdraw</small><div class="big"><b class="num">₹3,240</b><span class="wd">Withdraw</span></div>'
           '<p><span class="num">₹2,440</span> held · <span class="num">₹1,236</span> kept in November</p>'
           f'<div class="ft">{bank("hdfc", 18)}<span>Withdraw to kavya@okhdfc</span><em>Change</em></div></div>')
    mrow = lambda k, t, s_, a: (f'<div class="mn-row"><span class="mn-gl">{lead(PH[k])}</span><div class="mn-rt"><b>{t}</b><small>{s_}</small></div><span class="mn-amt num">{a}</span></div>')
    led = ('<div class="mn-card mn-list">' + mrow("serum", "Glow serum, 30 ml", "You keep 5% + ₹50 bonus", "₹720")
           + mrow("cream", "Night cream, 50 g", "You keep 5%", "₹330")
           + mrow("bottles", "Daily cleanser trio", "You keep 5% + ₹40 bonus", "₹186") + '</div>')
    return phone('<div class="md-pg"><div class="md-top"><h1>Wallet</h1>' + ic("settings", 22) + '</div>' + ink
                 + sh("You keep in November", "<b class=num>₹1,236</b>") + led + '</div>' + dock("Wallet"), label="Mediator · Wallet")

# ------------------------------------------------------------------ 7 TrustDrive
def s_m_trust():
    kv = lambda k, v, cls="": f'<div class="dm-kv {cls}"><span>{k}</span><b class="num">{v}</b></div>'
    score = ('<div class="dm-po dm-po6"><div class="v4-score"><div><span class="k">Paid back</span><b class="num big">95%</b>'
             '<p class="mix"><b class="num">38</b> of 40 shoppers · <b class="num">4.8</b> rating</p></div>' + ring(95, 64, 7, "✓") + '</div>'
             + kv("Confirmed", 36) + kv("In progress", 2) + kv("Partly paid", 1) + kv("Disputed", 1) + kv("Complaints", 0, "mute") + '</div>')
    tile = lambda i: f'<span class="x-tile">{ic(i, 20)}</span>'
    return phone('<div class="md-pg"><div class="md-top"><h1>TrustDrive</h1></div>' + tabs(["Overview", "Reviews", "Requests", "Listing"], "Overview")
                 + score + sh("To do", "3")
                 + row(tile("users"), "Takeover request", "<em class='warn'>Answer within 2 days</em>", lk("Review"))
                 + row(tile("star"), "Calm otter reviewed you", "5 stars · 18 Nov", lk("Reply"))
                 + '</div>' + dock(""), label="Mediator · TrustDrive")

MED = [s_m_today, s_m_deals, s_m_store, s_m_enroll, s_m_enrollments, s_m_wallet, s_m_trust]
