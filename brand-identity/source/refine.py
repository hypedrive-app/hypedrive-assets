"""Refinement options: wordmark weight/width, hexagon i-tittle (the parcel's silhouette), stacked lockup, mark radius."""
import sys, os, math, base64, subprocess
sys.path.insert(0, "/tmp/hdwm")
import final as FN
import isofam as F
import optical as OPT
from versions import rpoly

C30 = math.cos(math.radians(30))
DOT = {100: (24, 570, 197, 709), 94: (21, 569, 192, 706)}   # i-dot bbox (font units)

def hexagon(cx, cy, s, r):
    pts = [(cx, cy - s), (cx + C30*s, cy - s/2), (cx + C30*s, cy + s/2), (cx, cy + s), (cx - C30*s, cy + s/2), (cx - C30*s, cy - s/2)]
    return rpoly(pts, r)

def wordmark(wght=700, wdth=100, tittle="round", cap=FN.CAP, spacing=FN.SPACING):
    """Returns (path_d, width). Baseline at y=0. tittle='hex' swaps the i-dot for the parcel silhouette."""
    ax = {"opsz": 96, "wdth": wdth}
    text = "Hypedrıve" if tittle == "hex" else "Hypedrive"
    d, tw, _, pos = OPT.optical_text_path(text, wght, cap, "Bricolage", ax, positions=True, **spacing)
    if tittle == "hex":
        k = cap / 660
        x0, y0, x1, y1 = DOT[wdth]
        gx = [x for n, x, a in pos if n == "dotlessi"][0]
        cx = gx + (x0 + x1)/2*k; cy = -((y0 + y1)/2)*k
        s = 80*k*(wght/700)**0.35          # hex follows weight a little so it matches stroke heft
        d += hexagon(cx, cy - 4*k, s, s*0.16)
    return d, tw

def lockup(theme="light", wght=700, wdth=100, tittle="round", mark_r=None, stacked=False, mono=None):
    ink = mono or F.SOLID[theme]["ink"]
    orig = FN.box
    if mark_r is not None: FN.box = lambda *a, **k: orig(*a, **{**k, "r": mark_r})
    m, mw = FN.mark(theme, FN.MARK_H if not stacked else FN.CAP*2.05, mono=mono)
    FN.box = orig
    d, tw = wordmark(wght, wdth, tittle)
    S = FN.SOFT; pad = FN.CAP*0.5
    if not stacked:
        top = FN.MARK_CY - FN.MARK_H/2; ox = mw + FN.GAP; W = ox + tw + S
        y0 = min(top, FN.BASE - FN.ASC) - pad; y1 = max(top + FN.MARK_H, FN.BASE + FN.DESC) + pad
        body = f'<g transform="translate(0 {top:.3f})">{m}</g><path fill="{ink}" stroke="{ink}" stroke-width="{S}" stroke-linejoin="round" transform="translate({ox:.3f} {FN.BASE})" d="{d}"/>'
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {y0:.2f} {W+2*pad:.2f} {y1-y0:.2f}" width="{(W+2*pad)*10:.0f}" height="{(y1-y0)*10:.0f}">{body}</svg>'
    mh = FN.CAP*2.05; W = max(mw, tw)
    base = mh + FN.CAP*0.62 + FN.ASC
    body = (f'<g transform="translate({(W-mw)/2:.3f} 0)">{m}</g>'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{S}" stroke-linejoin="round" transform="translate({(W-tw)/2:.3f} {base:.3f})" d="{d}"/>')
    H = base + FN.DESC
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad:.2f} {-pad:.2f} {W+2*pad:.2f} {H+2*pad:.2f}" width="{(W+2*pad)*10:.0f}" height="{(H+2*pad)*10:.0f}">{body}</svg>'

def uri(svg): return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()

if __name__ == "__main__":
    cells = []
    def cell(label, svg, bg="#fff", w=520):
        cells.append(f'<figure style="background:{bg}"><img src="{uri(svg)}" style="width:{w}px"><figcaption>{label}</figcaption></figure>')
    cell("A · current (700, round dot)", lockup())
    cell("B · 700 · hex tittle", lockup(tittle="hex"))
    cell("C · 680 · hex tittle", lockup(wght=680, tittle="hex"))
    cell("D · 740 · hex tittle", lockup(wght=740, tittle="hex"))
    cell("E · 700 · wdth 94 · hex", lockup(wdth=94, tittle="hex"))
    cell("F · mark radius 1.7", lockup(tittle="hex", mark_r=1.7))
    cell("G · dark · hex", lockup("dark", tittle="hex"), "#121417")
    cell("H · stacked · hex", lockup(tittle="hex", stacked=True), "#fff", 300)
    cell("I · stacked dark", lockup("dark", tittle="hex", stacked=True), "#121417", 300)
    cell("J · 32px-high test (B)", lockup(tittle="hex"), "#fff", 150)
    cell("K · 32px-high test (A)", lockup(), "#fff", 150)
    html = ("<!doctype html><html><head><meta charset=utf-8><style>body{margin:0;padding:24px;background:#e8e9ec;font-family:sans-serif}"
            ".g{display:grid;grid-template-columns:repeat(3,560px);gap:16px}figure{margin:0;height:230px;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}"
            "figcaption{font:13px sans-serif;color:#888}</style></head><body><div class=g>" + "".join(cells) + "</div></body></html>")
    open(sys.argv[1], "w").write(html)
