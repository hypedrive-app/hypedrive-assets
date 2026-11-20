import sys; sys.path.insert(0, "/tmp/hdwm")
from uikit import NMAP, FILL, ic, ics, CSS
cells = "".join(f'<div class=c><div class=p>{ic(k, 26)}{ics(k, 26) if k in FILL else ""}</div><b>{k}</b></div>' for k in NMAP)
open("/tmp/hdwm/_icons2.html", "w").write(f'<html data-theme="light"><head><style>{CSS} body{{background:#fff;padding:20px;font-family:Geist}} .g{{display:grid;grid-template-columns:repeat(10,1fr);gap:8px}} .c{{display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px 4px;border:1px solid #eee;border-radius:10px;font-size:11px}} .p{{display:flex;gap:10px}}</style></head><body><div class=g>{cells}</div></body></html>')
