PEOPLE = {k: f"{STOCK}/people/{k}.jpg" for k in ("women-21", "women-44", "women-65", "men-12", "men-32")}
def avs(ps, size=30): return '<span class="x-avs">' + "".join(f'<img src="{PEOPLE[p]}" alt="" style="width:{size}px;height:{size}px">' for p in ps) + '</span>'
def meta(*items): return '<div class="x-meta">' + "".join(f'<div>{ic(i, 18)}<b class="num">{v}</b> {k}</div>' for i, v, k in items) + '</div>'

def s_welcome():
    return phone(f'<div class="body" style="justify-content:flex-end;padding-bottom:10px;gap:18px;background:{I["950"]}"><img src="{LOGO["dark"]}" style="height:28px;align-self:flex-start;margin-top:6px">'
                 f'<div style="flex:1;display:flex;align-items:center;justify-content:center"><img src="{ILL[("content","dark")]}" style="width:250px"></div>'
                 f'<div class="x-head" style="color:#fff;font-size:44px;line-height:46px">Products in.<br><span style="color:{C["300"]}">Hype out.</span></div>'
                 f'<p class="t-body" style="color:var(--hd-track-strong);margin:0;font-size:16px;line-height:24px">Try new products free, tell your people, and get paid for honest reviews.</p>'
                 f'<div class="stack" style="gap:6px"><button class="btn p lg block">Get started</button><button class="btn g block" style="color:{C["300"]}">I already have an account</button></div></div>', "dark", "Welcome", "#fff")

def s_otp():
    return phone(f'<div class="topbar">{ic("back")}</div><div class="body" style="gap:18px"><div><div class="x-page">Enter the code</div><p class="t-body muted" style="margin:6px 0 0;font-size:16px">Sent to <b class="num" style="color:var(--hd-fg)">+91 98•••• 4821</b></p></div>'
                 f'<div class="x-otp num"><span>4</span><span>8</span><span>2</span><span class="on"></span><span></span><span></span></div>'
                 f'<span class="t-small muted">Resend in <b class="num" style="color:var(--hd-fg)">0:24</b></span>'
                 f'<div class="x-tip"><b>Private</b>We never share your number with brands.</div><div style="flex:1"></div><button class="btn p lg block dis">Verify</button></div>'
                 f'<div class="keypad">' + "".join(f'<span class="{"blank" if not a else ""}"><b>{a}</b><small>{b}</small></span>' for a, b in [('1', ''), ('2', 'ABC'), ('3', 'DEF'), ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'), ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ'), ('', ''), ('0', ''), ('⌫', '')]) + '</div>', label="Verify phone")

def s_home():
    return phone(f'<div class="topbar" style="height:60px"><div class="x-who"><img src="{PEOPLE["women-21"]}" alt=""><div><b>Riya Sharma {vhex(15)}</b><small>Creator · Kolkata</small></div></div><span class="ttl"></span>{ic("search")}<span style="position:relative">{ic("bell")}<span class="dot" style="position:absolute;top:0;right:1px;background:var(--hd-tone-vermilion)"></span></span></div>'
                 f'<div class="body" style="gap:14px;padding-top:8px"><div class="x-head">Hi Riya, <span>3 drops picked for you.</span></div>'
                 f'<div class="tabs"><span class="on">{ics("foryou", 16, "var(--hd-accent)")}For you <span class="cnt-b">3</span></span><span>{ic("trend", 16, "var(--hd-tone-vermilion)")}Trending</span><span>{ic("heart", 16, "var(--hd-tone-mint)")}Saved</span></div>'
                 f'<div class="x-stack"><div class="x-hero" style="margin-top:0"><img src="{PH["serum_hero"]}" alt=""><div class="sh"></div>'
                 f'<div class="top"><span class="x-pill">{ic("clock", 14)}Ends Fri</span><span class="x-pill">{avs(("women-44", "men-12", "women-65"), 20)}36 left</span></div>'
                 f'<div class="bt"><div class="t"><b>Glow serum, 30 ml</b><small>Lumen Labs · you earn ₹ 1,240</small></div><span class="x-go">{ic("arrow", 22)}</span></div></div></div>'
                 + meta(("rupee", "8,460", "this month"), ("star", "4.9", "rating")) +
                 f'<div class="row"><img class="lead" src="{PH["scooter"]}"><div class="tx"><b>Kick scooter</b><small>Out for delivery · today</small></div><span class="badge info">On the way</span></div>'
                 f'</div>{tabbar("Home")}', label="Home")

def s_detail():
    return phone(f'<div class="x-photo"><img src="{PH["serum_hero"]}" alt=""><div class="tb"><span class="x-disc">{ic("back", 22)}</span><span class="x-disc">{ic("share", 20)}</span></div></div>'
                 f'<div class="x-sheet"><div><div class="x-title">Glow serum, 30 ml</div><div class="flexw" style="margin-top:6px;font-size:15px;color:var(--hd-fg-muted)">by Lumen Labs · also on {plat("nykaa", 18)}{plat("amazon", 18)}</div></div>'
                 f'<div class="x-chips"><span class="x-chip">Skincare</span><span class="x-chip">Vitamin C</span><span class="x-chip">Vegan</span></div>'
                 + meta(("rupee", "1,240", "you earn"), ("gift", "1,899", "worth"), ("clock", "7", "days")) +
                 f'<p class="t-body muted" style="margin:0;font-size:16px;line-height:24px">A light vitamin C serum. Use it for two weeks, then tell your people how it went. <b style="color:var(--hd-link);font-weight:600">More</b></p>'
                 f'<div class="x-row">{avs(("women-44", "men-12", "women-65", "men-32"))}<span style="font-size:14px;color:var(--hd-fg-muted)"><b class="num" style="color:var(--hd-fg)">84</b> creators trying it · 36 slots left</span></div></div>'
                 f'<div class="x-cta" style="background:var(--hd-canvas)"><button class="btn s icon sq" aria-label="Save">{ic("heart", 22)}</button><button class="btn p lg">Apply for this drop</button></div>', label="Drop details")

def s_apply():
    under = f'<div class="x-photo"><img src="{PH["serum_hero"]}" alt=""></div><div class="x-sheet"><div class="x-title">Glow serum, 30 ml</div></div>'
    return phone(under + f'<div class="scrim"></div><div class="overlay"><div class="sheet" style="padding-bottom:40px"><div class="grab"></div><div class="x-page" style="font-size:26px;line-height:30px">Where will you post?</div><p class="t-body muted" style="margin:6px 0 16px">Pick one now. You can add more later.</p>'
                 f'<div class="stack"><div class="row sel"><span class="radio on"></span>{soc("Instagram", 26)}<div class="tx"><b>Instagram</b><small>@riya.glows · 18.4k followers</small></div></div>'
                 f'<div class="row"><span class="radio"></span>{soc("Youtube", 26)}<div class="tx"><b>YouTube</b><small>Riya Sharma · 6.1k subscribers</small></div></div>'
                 f'<div class="row"><span class="check on">{ic("check", 16, "#fff", 3)}</span><div class="tx"><b>Ship to home</b><small>14 Park Street, Kolkata 700016</small></div><span class="t-small" style="color:var(--hd-link);font-weight:600">Edit</span></div>'
                 f'<button class="btn p lg block" style="margin-top:6px">Send application</button><span class="t-small subtle" style="text-align:center">Brands usually reply within a day</span></div></div></div>', label="Apply (sheet)")

def s_track():
    st = [("done", "Approved", "Nov 12, 4:10 pm"), ("done", "Shipped", "Nov 13 · Delhivery 4471 2280"), ("now", "Out for delivery", "With Ravi · +91 90•••• 1102"), ("", "Delivered", "Unbox on camera if you can"), ("", "Review due", "Nov 21")]
    tl = "".join(f'<div class="s {k}"><div class="k"><i>{ic("check", 13, "#fff", 3) if k == "done" else ""}</i>{"<em></em>" if n < len(st) - 1 else ""}</div><div><b>{t}</b><small>{d}</small></div></div>' for n, (k, t, d) in enumerate(st))
    return phone(f'<div class="topbar">{ic("back")}<span class="ttl"></span>{ic("more")}</div><div class="body" style="gap:16px">'
                 f'<div class="x-row" style="gap:16px"><img src="{PH["scooter"]}" style="width:96px;height:96px"><div><div class="x-page" style="font-size:28px;line-height:31px">Arrives by 7 pm</div><span class="t-body muted">Kick scooter · out for delivery</span></div></div>'
                 f'<div class="tape"><i style="width:75%"></i></div>'
                 f'<div class="x-tl">{tl}</div>'
                 f'<div class="x-tip"><b>Tip</b>A 15-second unboxing clip gets 3× more saves.</div></div>{tabbar("Drops")}', label="Parcel tracking")

def s_review():
    th = "".join(f'<div style="width:96px;height:96px;position:relative"><img src="{PH[i]}" style="width:96px;height:96px"><span style="position:absolute;top:-6px;right:-6px;width:24px;height:24px;border-radius:50%;background:{I["900"]};display:flex;align-items:center;justify-content:center">{ic("x", 12, "#fff", 3)}</span></div>' for i in ("serum", "bottles"))
    return phone(f'<div class="topbar">{ic("x")}<span class="ttl"></span><span class="t-small" style="color:var(--hd-fg-subtle);font-weight:600">Draft saved</span></div><div class="body" style="gap:16px">'
                 f'<div><div class="x-page">Your review</div><span class="t-body muted">Glow serum, 30 ml · due in 3 days</span></div>'
                 f'<div class="field"><label>How was it?</label><div class="stars">' + "".join(ic("star", 38, "var(--hd-tone-marigold)", 1.5, "var(--hd-tone-marigold)") for _ in range(4)) + ic("star", 38, "var(--hd-track-strong)", 1.5) + '</div></div>'
                 f'<div class="field"><label>Photos and video</label><div class="flexw" style="gap:10px">{th}<div class="drop" style="width:96px;height:96px;padding:0;justify-content:center">{ic("plus", 24)}</div></div></div>'
                 f'<div class="field"><label>Post link</label><div class="input foc">{ic("link", 18)}<span class="t-body">instagram.com/p/C9x…</span></div><span class="help">Make sure the post is public</span></div>'
                 f'<div class="field"><label>A few words</label><div class="input textarea t-body">Used it every night for two weeks. Light, no smell, and my skin feels calmer.</div></div></div>'
                 f'<div class="cta"><button class="btn s lg">Preview</button><button class="btn p lg" style="flex:1">Submit review</button></div>', label="Submit review")

def s_wallet():
    tx = [("trolley", "Kitchen trolley", "Nov 18 · review approved", "+ ₹ 640", "success"), ("bank", "Payout to HDFC ••4821", "Nov 15 · sent", "− ₹ 2,000", None), ("chair", "Ergo office chair", "Nov 11 · review approved", "+ ₹ 480", "success")]
    def lead(i): return f'<span class="x-tile cobalt">{ic("bank", 22)}</span>' if i == "bank" else f'<img class="lead" src="{PH[i]}" style="width:44px;height:44px">'
    rows = "".join(f'<div class="row">{lead(i)}<div class="tx"><b>{t}</b><small>{d}</small></div><b class="num" style="color:{"var(--hd-success)" if k else "var(--hd-fg)"}">{a}</b></div>' for i, t, d, a, k in tx)
    return phone(f'<div class="topbar"><span class="ttl"></span>{ic("clock")}{ic("settings")}</div><div class="body" style="gap:14px;padding-top:0">'
                 f'<div class="x-page">Wallet</div>'
                 f'<div class="x-money"><small>Available</small><div class="v num"><span>₹</span>6,820</div><small>₹ 640 held until 1 review is approved</small>'
                 f'<div class="flexw" style="margin-top:14px;gap:8px"><button class="btn w" style="flex:1">Withdraw</button><button class="btn t">Details</button></div></div>'
                 + meta(("rupee", "8,460", "this month"), ("check", "14", "reviews paid")) +
                 f'<div class="flexw" style="justify-content:space-between"><b class="t-h3">Activity</b><button class="btn link">See all</button></div><div class="stack">{rows}</div></div>{tabbar("Wallet")}', label="Wallet")

def s_success():
    return phone(f'<div class="topbar"><span class="ttl"></span>{ic("x")}</div><div class="body" style="align-items:center;text-align:center;justify-content:center;gap:14px">'
                 f'<img src="{ILL[("approved","light")]}" style="width:220px">'
                 f'<div class="x-head" style="font-size:38px;line-height:41px">Review approved.<br><span>Nice work.</span></div>'
                 f'<p class="t-body muted" style="margin:0;max-width:290px;font-size:16px;line-height:24px">Lumen Labs loved it. <b class="num" style="color:var(--hd-fg)">₹ 1,240</b> is on its way and lands by Friday.</p></div>'
                 f'<div class="cta" style="border:0;flex-direction:column;background:transparent"><button class="btn p lg block">Find your next drop</button><button class="btn g block">Share your review</button></div>', label="Success")

def s_notifs():
    groups = [("Today", [("box", "cobalt", "New drop for you", "Glow serum is looking for skincare creators", "2m", True), ("fast", "mint", "Out for delivery", "Kick scooter arrives by 7 pm", "1h", True)]),
              ("This week", [("bank", "mint", "Payout sent", "₹ 2,000 to HDFC ••4821", "Mon", False), ("clock", "marigold", "Review due in 3 days", "Glow serum · Nov 21", "Sun", False), ("linkbroken", "vermilion", "Link not public", "Make your post public so we can verify it", "Sat", False)])]
    body = ""
    for g, items in groups:
        body += f'<span class="t-small muted" style="margin-top:6px;font-weight:600">{g}</span><div class="stack" style="gap:8px">'
        for i, c, t, d, w, unread in items:
            body += (f'<div class="row" style="align-items:flex-start"><span class="x-tile {c}">{ic(i, 22)}</span>'
                     f'<div class="tx"><b>{t}</b><small>{d}</small></div><div class="end" style="display:flex;flex-direction:column;align-items:flex-end;gap:8px"><span class="t-cap subtle">{w}</span>{"<span class=dot></span>" if unread else ""}</div></div>')
        body += '</div>'
    return phone(f'<div class="topbar">{ic("back")}<span class="ttl"></span><button class="btn link">Mark all read</button></div><div class="body" style="gap:10px;padding-top:0"><div class="x-page">Notifications</div>{body}</div>', label="Notifications")

def s_profile():
    def gi(icon, label, tail): return f'<div class="gi">{ic(icon, 20)}<b>{label}</b>{tail}</div>'
    chev = f'<span class="chevr">{ic("chev", 18)}</span>'
    account = (gi("user", "Personal details", chev) + gi("link", "Linked accounts", soc("Instagram", 18, "currentColor") + soc("Youtube", 18, "currentColor") + chev) +
               gi("bank", "Payout method", f'<span class="meta">HDFC ••4821</span>{chev}'))
    prefs = gi("bell", "Notifications", '<span class="switch on"></span>') + gi("privacy", "Privacy", chev) + gi("help", "Help and support", chev)
    return phone(f'<div class="topbar"><span class="ttl"></span>{ic("settings")}</div><div class="body" style="gap:14px;padding-top:0">'
                 f'<div class="x-row" style="gap:16px"><img class="x-ava" src="{PEOPLE["women-21"]}" alt=""><div style="flex:1"><div class="x-page" style="font-size:28px;line-height:32px;display:flex;align-items:center;gap:6px">Riya Sharma {vhex(20)}</div><span class="t-body muted">@riya.glows · Kolkata</span></div></div>'
                 + meta(("check", "52", "reviews"), ("star", "4.9", "rating"), ("eye", "18.4k", "reach")) +
                 f'<div class="ghead">Account</div><div class="group">{account}</div><div class="ghead">Preferences</div><div class="group">{prefs}</div>'
                 f'<button class="btn s block" style="color:var(--hd-danger-strong)">Log out</button></div>{tabbar("You")}', "dark", "Profile · dark", "#fff")

def s_empty():
    pop = ["Sunscreen", "Lip balm", "Protein bar", "Earbuds", "Desk lamp"]
    sim = [("serum", "Glow serum, 30 ml", "Lumen Labs", "+ ₹ 1,240"), ("set", "Clear skin set", "Daybreak", "+ ₹ 980"), ("bottles", "Daily cleanser trio", "Lumen Labs", "+ ₹ 640")]
    rows = "".join(f'<div class="row"><img class="lead" src="{PH[i]}" style="width:44px;height:44px"><div class="tx"><b>{t}</b><small>{b}</small></div><b class="num" style="color:var(--hd-success)">{r}</b></div>' for i, t, b, r in sim)
    return phone(f'<div class="searchbar"><div class="search foc">{ic("search", 18)}<span class="q">matcha whisk</span><span class="clr">{ic("x", 11, sw=3)}</span></div><button class="btn link" style="text-decoration:none">Cancel</button></div>'
                 f'<div class="body" style="gap:16px"><div class="x-row" style="gap:16px;align-items:center"><img src="{ILL[("search","light")]}" style="width:104px"><div><div class="x-page" style="font-size:24px;line-height:28px">Nothing for “matcha whisk” yet</div><button class="btn p sm" style="margin-top:10px">{ic("bell", 16)}Alert me</button></div></div>'
                 f'<div class="stack" style="gap:8px"><b class="t-h3">Popular right now</b><div class="chiprow">' + "".join(f'<span class="chip">{ic("trend", 14, "var(--hd-tone-vermilion)")}{p}</span>' for p in pop) + '</div></div>'
                 f'<div class="stack" style="gap:8px"><div class="flexw" style="justify-content:space-between"><b class="t-h3">Similar drops</b><button class="btn link">See all</button></div>{rows}</div></div>{tabbar("Drops")}', label="Empty search")

