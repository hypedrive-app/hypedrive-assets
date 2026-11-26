"""Creator screens, part 1: Onboarding, Campaigns browse, Enrollments list. Built from kit components (field, input, seg, chip, tabs, row, badge, dm-cc, cv-pick, cv-sh)."""
from uikit2 import *
from kit4 import _cc, _st
from scr_v5 import s_onboarding, s_browse, s_enrollments  # v5: white pages (2026-11-26)
BA = "assets/brand"

def _ill(name, theme, size):
    return f'<img class="n1-ill" style="width:{size}px;height:{size}px" src="{BA}/hypedrive-ill-{name}-{theme}.svg" alt="">'

