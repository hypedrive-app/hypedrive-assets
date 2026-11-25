"""New creator screens, part 1 (agent 2): Onboarding, Campaigns browse, Enrollments list. Spec: CREATOR-SPEC.md."""
from uikit2 import *

def s_onboarding():
    chip = lambda t, on=False: f'<span class="n1-opt{" on" if on else ""}">{t}</span>'
    return phone(
        f'<div class="xm1-s n1-ob">'
        f'<div class="n1-top">{ic("back", 22)}</div>'
        f'<p class="n1-step num">Step 1 of 2</p>'
        f'<h1 class="n1-h">Your profile</h1>'
        f'<div class="n1-form">'
        f'<div class="n1-f"><label>First name</label><div class="n1-in"><span>Riya</span></div></div>'
        f'<div class="n1-f"><label>Last name</label><div class="n1-in"><span>Sharma</span></div></div>'
        f'<div class="n1-f"><label>Gender</label><div class="n1-opts">{chip("Female", True)}{chip("Male")}{chip("Other")}</div></div>'
        f'<div class="n1-f"><label>Date of birth</label><div class="n1-in"><span class="num">14 / 03 / 1998</span>{ic("calendar", 18)}</div></div>'
        f'</div>'
        f'<div class="n1-bar"><p class="n1-nx">Next: Verify your PAN · optional</p><button class="btn p lg block">Continue</button></div>'
        f'</div>', label="Onboarding")

def s_browse():
    def card(photo, store, title, lead, bonus, foot, joined=False):
        return (f'<div class="n1-cc{" dim" if joined else ""}"><div class="n1-ph"><img src="{PH[photo]}" alt=""></div><div class="n1-bd">'
                f'<span class="n1-sr">{plat(store, 14)}{store.title()}</span><b class="n1-t">{title}</b>'
                f'<p class="n1-pay">{lead}</p>'
                f'{f"<span class=n1-bn>+{bonus} bonus</span>" if bonus else ""}'
                f'{f"<span class=n1-ft>{foot}</span>" if foot else ""}'
                f'{"<span class=n1-jn>Joined</span>" if joined else ""}'
                f'</div></div>')
    chip = lambda t, on=False: f'<span class="n1-chip{" on" if on else ""}">{t}</span>'
    flt = lambda t: f'<span class="n1-flt">{t}{ic("down", 16)}</span>'
    return phone(
        f'<div class="xm1-s n1-br">'
        f'<div class="n1-top n1-top2"><h1 class="n1-h2">Campaigns</h1>{ic("search", 22)}</div>'
        f'<div class="n1-chips">{chip("All", True)}{chip("Ending soon")}{chip("New")}{chip("Saved")}</div>'
        f'<div class="n1-flts">{flt("Platform")}{flt("Store")}{flt("Category")}</div>'
        f'<div class="n1-sort"><span class="num">4 campaigns</span><span class="n1-sb">{ic("sort", 16)}Cashback high to low</span></div>'
        f'<div class="n1-grid">'
        + card("serum", "nykaa", "Glow serum, 30 ml", "<span class=num>60% back</span>", "₹200", "8 spots left")
        + card("bottles", "nykaa", "Daily cleanser trio", "<span class=num>55% back</span>", "₹100", "")
        + card("cream", "amazon", "Night cream, 50 g", "<span class=num>50% back</span>", "", "", True)
        + card("set", "nykaa", "Clear skin set", "Free product", "₹500", "Worth ₹2,400")
        + f'</div></div>{tabbar("Campaigns")}', label="Campaigns")

def s_enrollments():
    def row(photo, title, st, meta, cls=""):
        return (f'<div class="n1-row"><img src="{PH[photo]}" alt=""><div class="tx"><b>{title}</b>'
                f'<small class="{cls}">{st}{" · " + meta if meta else ""}</small></div>{ic("chev", 16)}</div>')
    sh = lambda t, n: f'<div class="n1-sh"><h2>{t}</h2><span class="num">{n}</span></div>'
    return phone(
        f'<div class="xm1-s n1-en">'
        f'<div class="n1-top n1-top2"><h1 class="n1-h2">Enrollments</h1></div>'
        f'<div class="n1-list">'
        + sh("Your turn", 3)
        + row("flatlay", "Skin routine kit", "Ready to join", "join by 26 Nov 2026")
        + row("serum", "Glow serum, 30 ml", "Submit tasks", "due in 41 days")
        + row("bottles", "Daily cleanser trio", "Fix tasks", "due in 6 days", "warn")
        + sh("Their turn", 3)
        + row("set", "Clear skin set", "On the way", "Delhivery")
        + row("mask", "Clay mask, 100 g", "Applied", "waiting for the brand")
        + row("cream", "Night cream, 50 g", "In review", "₹990 back after approval")
        + sh("Done", 4)
        + row("bottles", "Face wash, 100 ml", "Paid", "12 Nov 2026")
        + row("sand", "Hair oil, 100 ml", "Not approved", "")
        + row("cream", "Eye cream, 15 g", "Cancelled", "")
        + row("mask", "Lip balm, 10 g", "Expired", "")
        + f'</div></div>{tabbar("Enrolled")}', label="Enrollments")
