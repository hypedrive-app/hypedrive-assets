"""Brand desktop, part 2 (agent b2): Review queue + submission, Wallet & funding (+ invoices), Team & settings. Spec: BRAND-SPEC.md."""
from kit2 import shell
from uikit2 import *

PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-68", "women-44", "women-65", "men-12", "men-32", "women-21")}
NAV_ENROLL, NAV_WALLET, NAV_TEAM = "Enrollments", "Wallet", "Team"   # nav labels (re-check desk_b1.py header)

def inr(n):
    s = str(int(n))
    if len(s) <= 3: return "₹" + s
    head, tail = s[:-3], s[-3:]; parts = []
    while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return "₹" + ",".join(parts) + "," + tail

def _btn(kind, label, icon=None, sm=True, extra=""):
    i = ic(icon, 16) if icon else ""
    return f'<button class="btn {kind}{" sm" if sm else ""}"{extra}>{i}{label}</button>'

# ====================================================================== 5 · review queue + one submission
def _seg(on):
    g = "on" if on == "good" else ""; n = "on" if on == "fix" else ""
    return (f'<div class="b2-seg"><span class="{g} good">Looks good</span><span class="{n} fix">Needs a change</span></div>')

def _thumb(src, n=None):
    return f'<img class="b2-shot" src="{src}" alt="">'

def _task(glyph, title, meta, body, verdict, flagged=""):
    return (f'<div class="b2-card b2-task{" flag" if verdict == "fix" else ""}"><div class="b2-th"><span class="x-tile b2-tl">{glyph}</span>'
            f'<div class="b2-tt"><b>{title}</b><small>{meta}</small></div>{_seg(verdict)}</div>{body}{flagged}</div>')

def _link(url):
    return f'<div class="b2-link">{ic("link", 16)}<span>{url}</span><a class="btn g sm">{ic("external", 16)}Open</a></div>'

def d_queue():
    order = ('<div class="b2-card b2-order"><b class="b2-h">Order</b>'
             '<div class="b2-ol"><span>Product</span><b>Glow serum, 30 ml</b></div>'
             '<div class="b2-ol"><span>Store</span><b>' + plat("nykaa", 16) + 'Nykaa</b></div>'
             '<div class="b2-ol"><span>Order value</span><b class="num">₹1,899</b></div>'
             '<div class="b2-ol"><span>Order ID</span><b class="b2-mono">NYK-2611-48213</b></div>'
             '<div class="b2-ol"><span>Order date</span><b>14 Nov 2026</b></div>'
             f'<div class="b2-ol"><span>Order check</span><b class="b2-match">{ics("success", 16)}Matches</b></div></div>')
    rcpt = f'<div class="b2-files"><img class="b2-shot" src="{PH["bottles"]}" alt=""><a class="b2-full">{ic("eye", 16)}Full size</a></div>'
    reel = (_link("instagram.com/reel/C-9xLm2Qa7R") +
            f'<div class="b2-files"><img class="b2-shot" src="{PH["serum"]}" alt=""><img class="b2-shot" src="{PH["flatlay"]}" alt=""><a class="b2-full">{ic("eye", 16)}Full size</a></div>')
    rev = (_link("nykaa.com/glow-serum-30-ml/reviews") +
           f'<div class="b2-files"><img class="b2-shot" src="{PH["cream"]}" alt=""><a class="b2-full">{ic("eye", 16)}Full size</a></div>')
    chips = "".join(f'<span class="b2-chip{" on" if i == 0 else ""}">{t}</span>' for i, t in enumerate(["Under 40 words", "Not about the product", "Screenshot unclear", "Link doesn't open"]))
    flagged = f'<div class="b2-why">{chips}</div>'
    tasks = (_task(ic("receipt", 20), "Order receipt", "Always required · Sent 18 Nov", rcpt, "good")
             + _task(soc("Instagram", 22), "Instagram reel", "Sent 18 Nov · Link and 2 screenshots", reel, "good")
             + _task(plat("nykaa", 22), "Nykaa review", "Sent 18 Nov · At least 40 words", rev, "fix", flagged))
    note = (f'<div class="b2-card b2-note"><b class="b2-h">Your note to Riya</b>'
            '<div class="b2-ta">The review is under 40 words. Please add a few lines on how the serum felt on your skin, then send it again.</div>'
            '<small class="b2-sub">The creator gets until 25 Nov to fix these.</small></div>')
    cost = (f'<div class="b2-card b2-cost"><b class="b2-h">Your cost</b>'
            f'<div class="b2-ln"><span>Order funding</span><span class="num">₹1,139</span></div><div class="b2-ln"><span>Bonus funding</span><span class="num">₹200</span></div>'
            f'<div class="b2-ln"><span>GST (18%)</span><span class="num">₹241</span></div><div class="b2-ln tot"><span>Total</span><b class="num">₹1,580</b></div>'
            f'</div>')
    bar = (f'<div class="b2-bar"><span class="b2-bt">Needs review</span><span class="b2-bn num">1 of 9</span><i class="b2-prog"><i style="width:11%"></i></i><span class="sp"></span>'
           f'{_btn("s", "Back", "back")}{_btn("s", "Next", "chev")}</div>')
    head = (f'<div class="b2-hd"><img class="b2-av" src="{PEOPLE["women-68"]}" alt=""><div class="b2-who"><div class="t-h1 b2-name">Riya Sharma {vhex(20)}</div>'
            f'<p>Waiting 2 days · Trusted · @riya.glows · Kolkata</p></div>'
            f'<div class="b2-camp"><img src="{PH["serum"]}" alt=""><div><b>Glow serum, 30 ml</b><small>Lumen Labs · Joined 14 Nov</small></div></div>{_btn("s", "Details")}</div>')
    band = (f'<div class="b2-band"><div class="b2-money"><b class="num">₹1,580</b><span>stays on hold while the creator fixes.</span></div><span class="sp"></span>'
            f'<button class="btn g">More</button><button class="btn s">Reject</button><button class="btn p">Send back 1 task</button></div>')
    body = f'<div class="b2-body"><div class="b2-tasks">{tasks}</div><div class="b2-side">{order}{note}{cost}</div></div>'
    page = f'<div class="b2-rv">{bar}{head}{body}{band}</div>'
    return shell(NAV_ENROLL, ["Lumen Labs", "Enrollments", "Riya Sharma"], page)

# ====================================================================== 6 · wallet and funding
def _arow(glyph, title, meta, amt, kind=""):
    return (f'<div class="b2-row"><span class="x-tile b2-tl">{glyph}</span><div class="b2-tt"><b>{title}</b><small>{meta}</small></div>'
            f'<b class="b2-amt num {kind}">{amt}</b></div>')

def _inv(week, num, n, total, status):
    gst = round(total * 18 / 118)
    badge = f'<span class="badge {"success" if status == "Paid" else "neutral"}">{status}</span>'
    cls = " void" if status == "Void" else ""
    return (f'<div class="b2-ir{cls}"><div class="b2-tt"><b>{week}</b><small><span class="b2-mono">{num}</span> · {n} enrollments</small></div>'
            f'<div class="b2-iamt"><b class="num">{inr(total)}</b><small class="num">GST {inr(gst)}</small></div>{badge}<a class="btn g sm b2-dl" aria-label="Download">{ic("download", 16)}</a></div>')

def d_wallet():
    """Wallet: one balance, a quiet ledger, invoices and TDS as plain lists. Paid and Credited are the normal case, so only exceptions are marked."""
    head = '<div class="ph"><div class="t"><div class="t-h1">Wallet</div></div></div>'
    bal = ('<div class="bw-bal"><div class="bw-bm"><small>Available</small><b class="num">₹1,84,500</b>'
           '<p><span class="num">₹96,320</span> on hold for creators who joined · each approval is paid from here</p></div>'
           f'<div class="bw-act"><button class="btn s">Withdraw</button><button class="btn p">{ic("plus", 18)}Add money</button></div></div>')
    led = lambda t, d, date, amt, cr=False: (f'<div class="bw-lr"><div class="bw-tx"><b>{t}</b><small>{d}</small></div><span class="bw-d">{date}</span>'
                                             f'<b class="num bw-a{" cr" if cr else ""}">{amt}</b></div>')
    ledger = ('<div class="bw-card"><div class="bw-h"><b>Activity</b><em class="bw-lk">Statements</em></div>'
              + led("Money added", "Razorpay", "19 Nov", "+₹2,00,000", True)
              + led("Enrollment paid", "Ananya Das · Glow serum", "19 Nov", "−₹1,580")
              + led("On hold", "Kabir Singh · Glow serum", "18 Nov", "−₹1,580")
              + led("Hold released", "Tanvi Shah · Clear skin set", "17 Nov", "+₹2,900", True)
              + led("Withdrawal", "HDFC Bank ••6093", "12 Nov", "−₹50,000")
              + led("Refund", "Order cancelled", "10 Nov", "+₹1,580", True)
              + led("Adjustment", "Hypedrive", "9 Nov", "+₹320", True) + '</div>')
    dl = ic("download", 16)
    inv = lambda wk, num, n, amt, void=False: (f'<div class="bw-lr{" void" if void else ""}"><div class="bw-tx"><b>{wk}</b><small>{num} · {n} enrollments{" · Void" if void else ""}</small></div>'
                                              f'<b class="num bw-a">{amt}</b><span class="bw-ic">{dl}</span></div>')
    invoices = ('<div class="bw-card"><div class="bw-h"><b>Invoices</b><span><span class="num">₹18,42,300</span> invoiced in FY 2026-27</span></div>'
                + inv("9 – 15 Nov", "LL/2627/0042", 31, "₹1,41,120") + inv("2 – 8 Nov", "LL/2627/0041", 27, "₹1,22,780")
                + inv("26 Oct – 1 Nov", "LL/2627/0040", 24, "₹1,09,950") + inv("19 – 25 Oct", "LL/2627/0039", 22, "₹98,360", True) + '</div>')
    q = lambda n, d, act="": f'<div class="bw-lr"><div class="bw-tx"><b>{n}</b><small>{d}</small></div>{act}</div>'
    tds = ('<div class="bw-card"><div class="bw-h"><b>TDS certificates</b><span><span class="num">₹23,240</span> credited of <span class="num">₹34,860</span></span></div>'
           + q("Q3 Oct – Dec", "Due by 31 Jan 2027", '<em class="bw-lk">Send certificate</em>')
           + q("Q2 Jul – Sep", "Credited 12 Nov") + q("Q1 Apr – Jun", "Credited 12 Aug") + '</div>')
    page = f'{head}{bal}<div class="bw-grid"><div>{ledger}</div><div class="bw-side">{invoices}{tds}</div></div>'
    return shell(NAV_WALLET, ["Lumen Labs", "Wallet"], page)

# ====================================================================== 7 · team and settings
ROLES = [("Owner", "Everything, and the only one who can hand the brand on."), ("Admin", "Everything: campaigns, money, people and settings."),
         ("Campaign manager", "Runs campaigns and listings, reviews work, answers disputes. Sees the wallet."),
         ("Finance manager", "Runs the wallet, withdrawals, invoices and bank accounts. Sees campaigns."), ("Viewer", "Sees everything, changes nothing.")]

def d_team():
    def mrow(photo, name, you, mail, role, seen, menu=""):
        fixed = role == "Owner"
        ctl = f'<span class="b2-role fixed">{role}</span>' if fixed else f'<span class="b2-role{" open" if menu else ""}">{role}{ic("down", 16)}</span>'
        return (f'<div class="b2-mrow"><img class="b2-av44" src="{PEOPLE[photo]}" alt=""><div class="b2-tt"><b>{name}{"<em>You</em>" if you else ""}</b><small>{mail}</small></div>'
                f'<div class="b2-rc">{ctl}{menu}</div><span class="b2-seen">{seen}</span></div>')
    items = "".join(f'<div class="b2-mi"><div class="b2-mit"><b>{r}</b>{ics("check", 16) if r == "Campaign manager" else ""}</div><small>{d}</small></div>' for r, d in ROLES[1:])
    menu = f'<div class="b2-menu">{items}</div>'
    members = "".join([mrow("women-44", "Neha Kapoor", True, "neha@lumenlabs.in", "Owner", "Active now"),
                       mrow("men-12", "Arjun Mehta", False, "arjun@lumenlabs.in", "Campaign manager", "Active today", menu),
                       mrow("women-65", "Divya Rao", False, "divya@lumenlabs.in", "Finance manager", "Active yesterday"),
                       mrow("men-32", "Sanjay Iyer", False, "sanjay@lumenlabs.in", "Viewer", "Active 3 days ago")])
    link = (f'<div class="b2-card b2-linkc"><span class="x-tile b2-tl">{ic("link", 20)}</span><div class="b2-tt"><b>Invite link</b><small>Anyone with it joins as the role you pick. Invites expire after 7 days.</small></div>'
            f'<span class="b2-role">Viewer{ic("down", 16)}</span><button class="btn s sm">{ic("copy", 16)}Copy invite link</button><button class="btn g sm">Turn off link</button></div>')
    rail_item = lambda i, t, on=False: f'<div class="b2-ri{" on" if on else ""}">{ics(i, 18) if on else ic(i, 18)}{t}</div>'
    rail = ('<div class="b2-rail"><div class="b2-rg">Workspace</div>' + rail_item("settings", "Workspace") + rail_item("users", "Team", True) + rail_item("receipt", "Tax")
            + rail_item("bank", "Bank account") + rail_item("bell", "Notifications") + '<div class="b2-rg">You</div>' + rail_item("user", "Profile") + rail_item("lock", "Security") + '</div>')
    head = (f'<div class="ph"><div class="t"><div class="t-h1">Team</div><p>4 members. Only an owner or admin manages people and settings.</p></div>'
            f'<button class="btn p sm">{ic("plus", 16)}Invite members</button></div>')
    inv = (f'<div class="b2-mrow"><span class="x-tile b2-tl">{ic("mail", 20)}</span><div class="b2-tt"><b>aman@lumenlabs.in</b><small>Sent on WhatsApp · Expires in 7 days</small></div>'
           f'<div class="b2-rc"><span class="b2-role fixed">Campaign manager</span></div><button class="btn s sm">Resend</button><button class="btn s sm">Cancel invite</button></div>')
    sec = lambda t, n, body: f'<div class="b2-sec"><div class="b2-sech"><b>{t}</b><span class="num">{n}</span></div>{body}</div>'
    main = f'<div class="b2-tmain">{head}{sec("Members", 4, "<div class=b2-mlist>" + members + "</div>")}{sec("Invites", 1, "<div class=b2-mlist>" + inv + "</div>")}{link}</div>'
    return shell(NAV_TEAM, ["Lumen Labs", "Team"], f'<div class="b2-split">{rail}{main}</div>')

SCREENS = [("Brand · Review queue", d_queue), ("Brand · Wallet", d_wallet), ("Brand · Team", d_team)]
