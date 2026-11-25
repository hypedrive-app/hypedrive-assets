"""Creator screens, part 1: Onboarding, Campaigns browse, Enrollments list. Built from kit components (field, input, seg, chip, tabs, row, badge, dm-cc, cv-pick, cv-sh)."""
from uikit2 import *
from kit4 import _cc, _st
BA = "assets/brand"

def _ill(name, theme, size):
    return f'<img class="n1-ill" style="width:{size}px;height:{size}px" src="{BA}/hypedrive-ill-{name}-{theme}.svg" alt="">'

def s_onboarding():
    body = (
        f'<div class="xm1-bar xm1-s">{ic("back", 22)}</div>'
        f'<div class="xm1-s n1-pg">'
        f'<div class="n1-hero">{_ill("gift", "light", 148)}</div>'
        f'<div class="n1-head"><small class="n1-step num">Step 1 of 2</small><h1>Your profile</h1><p>This is how brands will see you.</p></div>'
        f'<div class="n1-form">'
        f'<div class="n1-two"><div class="field"><label>First name</label><div class="input"><span>Riya</span></div></div>'
        f'<div class="field"><label>Last name</label><div class="input"><span>Sharma</span></div></div></div>'
        f'<div class="field"><label>Gender</label><span class="seg n1-seg"><span class="on">Female</span><span>Male</span><span>Other</span></span></div>'
        f'<div class="field"><label>Date of birth</label><div class="input"><span class="num" style="flex:1">14 Mar 1998</span><span class="trail">{ic("calendar", 18)}</span></div></div>'
        f'</div></div>'
        f'<div class="xm1-bar2 n1-bb"><small>Next: Verify your PAN · optional</small><button class="btn p lg block">Continue</button></div>')
    return phone(body, label="Onboarding")

def s_browse():
    pick = (f'<div class="cv-pick n1-pick"><img src="{PH["serum"]}" alt=""><span class="st">{plat("nykaa", 14)}Nykaa · 8 spots left</span>'
            f'<div class="bt"><div><small>Lumen Labs</small><b>Get ₹1,339 back</b><em>Glow serum · 60% back + ₹200 bonus</em></div><span class="j">Join</span></div></div>')
    chip = lambda t: f'<span class="chip">{t}{ic("down", 14)}</span>'
    body = (
        f'<div class="xm1-bar xm1-s n1-bar"><h1 class="n1-title">Campaigns</h1>{ic("search", 22)}</div>'
        f'<div class="xm1-s n1-pg n1-br">'
        f'<div class="tabs"><span class="on">All</span><span>Ending soon</span><span>New</span><span>Saved</span></div>'
        f'<div class="n1-chips">{chip("Platform")}{chip("Store")}{chip("Category")}</div>'
        f'{pick}'
        f'<div class="n1-grid">'
        + _cc("bottles", "nykaa", "Daily cleanser trio", "Lumen Labs", "55% back", "₹100", "3 spots left")
        + _cc("cream", "amazon", "Night cream, 50 g", "Lumen Labs", "50% back", "", "", _st("mute", "check", "Joined"), cls="muted")
        + f'</div></div>{tabbar("Campaigns")}')
    return phone(body, label="Campaigns")

def s_enrollments():
    def row(photo, title, tone, st, meta):
        return (f'<div class="row"><img class="lead" src="{PH[photo]}" alt=""><div class="tx"><b>{title}</b><small>{meta}</small></div>'
                f'<span class="badge {tone}">{st}</span></div>')
    sh = lambda t, n: f'<div class="cv-sh n1-sh"><h2>{t}</h2><span class="num">{n}</span></div>'
    body = (
        f'<div class="xm1-bar xm1-s n1-bar"><h1 class="n1-title">Enrollments</h1></div>'
        f'<div class="xm1-s n1-pg n1-en">'
        + sh("Your turn", 3)
        + row("serum", "Glow serum, 30 ml", "info", "Submit tasks", "Due in 41 days")
        + row("bottles", "Daily cleanser trio", "warning", "Fix tasks", "Due in 6 days")
        + row("flatlay", "Skin routine kit", "info", "Ready to join", "Join by 26 Nov 2026")
        + sh("Their turn", 3)
        + row("set", "Clear skin set", "info", "On the way", "Arrives Mon, 23 Nov")
        + row("cream", "Night cream, 50 g", "neutral", "In review", "₹990 back after approval")
        + sh("Done", 4)
        + row("bottles", "Face wash, 100 ml", "success", "Paid", "12 Nov 2026")
        + f'</div>{tabbar("Enrolled")}')
    return phone(body, label="Enrollments")
