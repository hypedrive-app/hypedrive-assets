"""New creator screens, part 1 (agent 2): Onboarding, Campaigns browse, Enrollments list. Spec: CREATOR-SPEC.md."""
from uikit2 import *

def s_onboarding():
    return phone('<div class="xm1-s"><p style="padding:40px 20px">Onboarding — to build</p></div>', label="Onboarding")

def s_browse():
    return phone(f'<div class="xm1-s"><p style="padding:40px 20px">Campaigns — to build</p></div>{tabbar("Campaigns")}', label="Campaigns")

def s_enrollments():
    return phone(f'<div class="xm1-s"><p style="padding:40px 20px">Enrollments — to build</p></div>{tabbar("Enrolled")}', label="Enrollments")
