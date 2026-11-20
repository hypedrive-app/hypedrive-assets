import json, sys
sys.path.insert(0, "/tmp/hdwm")
from uikit import NMAP, FILL, ic, ics, CSS
cells = "".join(f'<div class=c>{ic(k, 28)}<b>{k}</b><small>{v}</small></div>' for k, v in NMAP.items())
fills = "".join(f'<div class=c>{ics(k, 28)}<b>{k}</b><small>{v}</small></div>' for k, v in FILL.items())
open("/tmp/hdwm/_icons.html", "w").write(f'<html data-theme="light"><head><style>{CSS} body{{background:#fff;padding:20px;font-family:Geist}} .g{{display:grid;grid-template-columns:repeat(10,1fr);gap:8px;margin-bottom:24px}} .c{{display:flex;flex-direction:column;align-items:center;gap:4px;padding:10px 4px;border:1px solid #eee;border-radius:10px;font-size:11px}} .c small{{color:#777;font-size:10px}}</style></head><body><div class=g>{cells}</div><div class=g>{fills}</div></body></html>')
