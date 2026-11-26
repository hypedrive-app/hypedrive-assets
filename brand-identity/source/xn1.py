# Layer for scr_n1.py and the shared kit-component scope for screens (n1-/n2- pages).
# Kit components are written for the kit sections (.sec.dm / .mn-sec). Here the same rules are re-scoped to a screen
# container (.phone .dm / .phone .mn-sec) so screens use the real components instead of look-alikes.
import re as _re
from xr3 import XR3 as _R3
from xr4 import XR4 as _R4
from xt3 import XT3 as _T3

def _harvest(*layers):
    out = []
    for css in layers:
        css = _re.sub(r"/\*.*?\*/", "", css, flags=_re.S)
        for m in _re.finditer(r"([^{}@]+)\{([^{}]*)\}", css):
            sels = [s.strip() for s in m.group(1).split(",")]
            keep = [s.replace(".sec.dm", ".phone .dm").replace(".mn-sec", ".phone .mn-sec") for s in sels if ".sec.dm" in s or ".mn-sec" in s]
            if keep: out.append(", ".join(keep) + " {" + m.group(2) + "}")
    return "\n".join(out)

XN1 = _harvest(_R3, _R4, _T3) + """
.phone .scr:has(.n1-pg) { background: var(--hd-canvas); }
.phone .n1-pg { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 4px 16px 0; background: var(--hd-canvas); }
.phone .n1-pg > * { flex: none; }
.phone .n1-bar { justify-content: space-between; height: 48px; }
.phone .n1-title { font-family: var(--font-brand); font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 0; color: var(--hd-fg); }
.phone .n1-ill { display: block; object-fit: contain; }
/* onboarding */
.phone .n1-hero { display: flex; justify-content: center; padding-top: 4px; }
.phone .n1-head { padding: 0 4px; }
.phone .n1-step { display: block; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n1-head h1 { font-family: var(--font-brand); font-size: 30px; line-height: 34px; font-weight: 700; letter-spacing: -0.025em; font-variation-settings: 'opsz' 96; margin: 2px 0 0; }
.phone .n1-head p { margin: 4px 0 0; font-size: 15px; line-height: 22px; color: var(--hd-fg-muted); }
.phone .n1-form { display: flex; flex-direction: column; gap: 16px; padding-top: 8px; }
.phone .n1-two { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.phone .n1-seg { display: flex; }
.phone .n1-seg > span { flex: 1; justify-content: center; }
.phone .n1-bb { flex-direction: column; align-items: stretch; gap: 10px; padding: 12px 16px 12px; }
.phone .n1-bb small { text-align: center; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.phone .n1-bb .btn { height: 48px; flex: none; }
.phone .n1-grid .dm-by { display: none; }
/* browse */
.phone .n1-br { gap: 14px; padding-top: 0; }
.phone .n1-br .tabs { margin: 0 -16px; padding: 0 20px; }
.phone .n1-chips { display: flex; gap: 8px; }
.phone .n1-chips .chip { gap: 2px; }
.phone .n1-pick { margin: 0; height: 196px; }
.phone .n1-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.phone .n1-grid .dm-cc { min-width: 0; }
/* enrollments */
.phone .n1-en { gap: 10px; padding-top: 0; }
.phone .n1-sh { padding: 0 4px; margin: 8px 0 -2px; }
.phone .n1-en .row { flex: none; }
"""
XN1 += """
.phone .n1-chips .chip { background: var(--hd-surface); border: 1px solid var(--hd-edge); box-shadow: none; }
"""
XN1 += """
.phone .n1-seg { background: transparent; box-shadow: none; padding: 0; gap: 8px; }
.phone .n1-seg > span { background: var(--hd-surface); border: 1px solid var(--hd-edge); box-shadow: none; border-radius: 12px; height: 44px; align-items: center; color: var(--hd-fg-muted); }
.phone .n1-seg > span.on { background: var(--hd-accent-subtle, #e8efff); border-color: var(--hd-accent, #2f5bea); color: var(--hd-accent, #2f5bea); }
"""
XN1 += """
.phone .n1-chips .chip { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; box-shadow: none !important; }
"""
