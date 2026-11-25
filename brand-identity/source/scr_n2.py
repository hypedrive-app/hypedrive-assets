"""New creator screens, part 2 (agent 3): Enrollment detail, Withdraw, Settings, Barter enrollment. Spec: CREATOR-SPEC.md."""
from uikit2 import *

def s_enrollment_detail():
    return phone('<div class="xm1-s"><p style="padding:40px 20px">Enrollment detail — to build</p></div>', label="Enrollment detail")

def s_withdraw():
    return phone('<div class="xm1-s"><p style="padding:40px 20px">Withdraw — to build</p></div>', label="Withdraw")

def s_settings():
    return phone('<div class="xm1-s"><p style="padding:40px 20px">Settings — to build</p></div>', label="Settings")

def s_barter():
    return phone('<div class="xm1-s"><p style="padding:40px 20px">Barter enrollment — to build</p></div>', label="Barter enrollment")
