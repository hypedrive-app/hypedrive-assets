"""Concept: creator Home, designed at discretion (owner 2026-11-26). In the kit since 2026-11-26."""
from uikit2 import *
BA = "assets/brand"

def home():
    act = lambda ph, tag, small, big, cls, pct, prog, btn, bcls="": (
        f'<div class="cv-act"><div class="ph"><img src="{PH[ph]}" alt=""><span class="tag">{tag}</span></div><div class="bd">'
        f'<small>{small}</small><b class="{cls}">{big}</b><div class="pr"><i><u style="width:{pct}%"></u></i><span>{prog}</span></div>'
        f'<button class="go {bcls}">{btn}</button></div></div>')
    body = (
        f'<div class="xm1-bar xm1-s"><img class="av" src="{STOCK}/people/women-68.jpg" alt="Riya Sharma">{ic("search")}<span class="bell">{ic("bell")}<i></i></span></div>'
        f'<div class="xm1-s cv">'
        f'<div class="cv-hi"><div><small>Friday, 20 Nov</small><h1>Hi, Riya</h1></div></div>'
        f'<div class="cv-wal"><small>Available</small><div class="big"><b class="num">₹6,820</b><span class="wd">Withdraw</span></div>'
        f'<p><span class="num">₹1,339</span> on hold · <span class="num">₹990</span> pending approval</p>'
        f'<div class="ft">{ics("privacy", 16, "#a0c6ff")}<span>Verify your PAN to withdraw</span><em>Verify</em></div></div>'
        f'<div class="cv-sh"><h2>Your turn</h2><span>2</span></div>'
        f'<div class="cv-rail">'
        + act("serum", f'{plat("nykaa", 14)}Glow serum', "Due in 41 days", "Submit 2 tasks", "", 8, "0 of 2 sent", "Start")
        + act("bottles", f'{plat("nykaa", 14)}Daily cleanser trio', "Due in 6 days", "Fix 1 task", "warn", 50, "1 of 2 approved", "See what to fix", "s")
        + f'</div>'
        f'<div class="cv-sh"><h2>On the way</h2></div>'
        f'<div class="cv-ship"><img class="il" src="{BA}/hypedrive-ill-tracking-light.svg" alt=""><div class="tx"><b>Clear skin set</b>'
        f'<small>Delhivery · arrives Mon, 23 Nov</small><div class="cv-steps"><i class="on"></i><i class="on"></i><i></i><i></i><i></i></div></div></div>'
        f'<div class="cv-sh"><h2>In review</h2></div>'
        f'<div class="cv-row"><img src="{PH["cream"]}" alt=""><div class="tx"><b>Night cream, 50 g</b><small>Usually within 2 days</small></div><span class="amt num">₹990</span></div>'
        f'<div class="cv-sh"><h2>Picked for you</h2><em>See all</em></div>'
        f'<div class="cv-pick"><img src="{PH["flatlay"]}" alt=""><span class="st">{plat("nykaa", 14)}Nykaa · 6 spots left</span>'
        f'<div class="bt"><div><small>Lumen Labs</small><b>Get ₹780 back</b><em>Rose toner · 50% back + ₹150 bonus</em></div><span class="j">Join</span></div></div>'
        f'</div>{tabbar("Home")}')
    return phone(body, label="Home")

