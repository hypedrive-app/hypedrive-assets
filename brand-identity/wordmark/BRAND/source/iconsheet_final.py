"""Icon sheet: every Nucleo UI Outline 18 icon beside its exact Fill 18 twin, light + dark, one grid.
Usage: python -I iconsheet_final.py OUT.html   (layout and labels only; glyphs come untouched from nucleo_outline/fill.json)"""
import sys; sys.path.insert(0, "/tmp/hdwm")
from uikit import NMAP, FILL, NO, NF, CSS
out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/hdwm/_icons_final.html"
missing = [k for k, v in NMAP.items() if v + "Outline18" not in NO or v + "Fill18" not in NF]
assert not missing, missing
def o(k, s): return f'<svg width="{s}" height="{s}" viewBox="0 0 18 18" stroke-width="1.5" aria-hidden="true">{NO[NMAP[k] + "Outline18"]}</svg>'
def f(k, s): return f'<svg width="{s}" height="{s}" viewBox="0 0 18 18" fill="currentColor" aria-hidden="true">{NF[NMAP[k] + "Fill18"]}</svg>'
def card(k):
    return (f'<div class=c><div class=big><span class=s>{o(k, 28)}</span><span class=s>{f(k, 28)}</span></div>'
            f'<div class=sm><span class=s>{o(k, 18)}</span><span class=s>{f(k, 18)}</span></div>'
            f'<b>{k}</b><small>{NMAP[k]}</small></div>')
cells = "".join(card(k) for k in NMAP)
def sheet(theme):
    return (f'<section data-theme="{theme}"><header><h1>Nucleo UI 18</h1><p>Outline and Fill, exact twins · {len(NMAP)} icons · 28 px above, 18 px below · stroke-only glyphs (chevrons, plus, check, x, arrows, search, minus, link, more) have no heavier solid, so the twin is the same shape</p>'
            f'<div class=key><span>Outline · idle</span><span>Fill · active</span></div></header><div class=g>{cells}</div></section>')
css = """
body{margin:0;font-family:Geist,sans-serif;display:flex}
section{padding:28px;width:1260px;--bg:#fff;--card:#fff;--line:#e4e5ea;--fg:#14161c;--mut:#6b6f7b;--sub:#f4f5f8}
section[data-theme=dark]{--bg:#0f1115;--card:#171a21;--line:#272b35;--fg:#f2f3f6;--mut:#9a9fac;--sub:#1e222b}
section{background:var(--bg);color:var(--fg)}
header{display:flex;align-items:baseline;gap:16px;margin-bottom:20px}
h1{font:650 22px 'Bricolage Grotesque';margin:0}
header p{margin:0;font-size:13px;color:var(--mut);flex:1}
.key{display:flex;gap:16px;font-size:12px;color:var(--mut)}
.g{display:grid;grid-template-columns:repeat(8,1fr);gap:10px}
.c{display:flex;flex-direction:column;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 6px 10px}
.big,.sm{display:grid;grid-template-columns:1fr 1fr;width:100%;justify-items:center}
.sm{margin-top:10px;padding-top:10px;border-top:1px solid var(--line);color:var(--fg)}
.big{color:var(--fg)}
.s{display:flex;align-items:center;justify-content:center;height:28px}
.sm .s{height:18px}
.c b{margin-top:10px;font-size:12px;font-weight:560}
.c small{font-size:10.5px;color:var(--mut);margin-top:1px}
svg{display:block}
"""
open(out, "w").write(f'<html><head><meta charset=utf-8><style>{CSS.split("@font-face")[0]}@font-face{CSS.split("@font-face",1)[1].split("{TOK}")[0] if False else ""}</style></head></html>') if False else None
import re
fonts = "".join(re.findall(r"@font-face \{.*?\}\n", CSS, re.S))
open(out, "w").write(f'<html><head><meta charset=utf-8><style>{fonts}{css}</style></head><body>{sheet("light")}{sheet("dark")}</body></html>')
print("ok", len(NMAP))
