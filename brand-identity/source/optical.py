"""Optical letter-spacing: measure the real white space between each glyph pair
(row by row through the x-height band) and nudge kerning so every pair holds the same visual gap."""
import io, subprocess
import numpy as np
from PIL import Image
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb
import text2path as T

SCALE = 0.25      # px per font unit for measurement

def glyph_profiles(gs, name, upm, top, bottom, rows):
    """Left/right ink edge per row (font units, relative to glyph origin) in [bottom, top]."""
    pen = SVGPathPen(gs); tp = TransformPen(pen, (SCALE, 0, 0, -SCALE, 0.5*upm*SCALE, top*SCALE)); gs[name].draw(tp)
    w = int(2.0*upm*SCALE); h = int((top-bottom)*SCALE)+1
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"><path d="{pen.getCommands()}" fill="#000"/></svg>'
    png = subprocess.run(["rsvg-convert"], input=svg.encode(), capture_output=True, check=True).stdout
    a = np.array(Image.open(io.BytesIO(png)).convert("RGBA"))[..., 3]
    L, R = [], []
    for y in np.linspace(0, h-1, rows).astype(int):
        xs = np.nonzero(a[y] > 100)[0]
        if len(xs): L.append(xs[0]/SCALE - 0.5*upm); R.append(xs[-1]/SCALE - 0.5*upm)
        else: L.append(None); R.append(None)
    return L, R

def optical_text_path(text, wght, cap_px, name, axes=None, strength=0.75, extra=0.0, cap_gap=None, positions=False):
    tt, data = T.font(name, wght, axes)
    upm = tt["head"].unitsPerEm; cap = tt["OS/2"].sCapHeight; xh = tt["OS/2"].sxHeight
    k = cap_px / cap
    face = hb.Face(data); f = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(f, buf, {"kern": True, "liga": False})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    names = [order[i.codepoint] for i in buf.glyph_infos]; adv = [p.x_advance for p in buf.glyph_positions]
    rows = 24
    prof = {n: glyph_profiles(gs, n, upm, xh, 0, rows) for n in set(names)}
    limit = 0.20*upm                       # deep notches (open v, y bowls) count only up to this
    gaps = []
    for i in range(len(names)-1):
        R = prof[names[i]][1]; L = prof[names[i+1]][0]
        g = [min(adv[i] - r + l, limit) for r, l in zip(R, L) if r is not None and l is not None]
        gaps.append(float(np.mean(g)) if g else limit)
    target = (cap_gap if cap_gap is not None else float(np.median(gaps))) + extra*upm
    deltas = [(target - g)*strength for g in gaps] + [0]
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    x = 0; pos = []
    for n, a, dlt in zip(names, adv, deltas):
        gs[n].draw(TransformPen(pen, (k, 0, 0, -k, x*k, 0)))
        pos.append((n, x*k, a*k))
        x += a + dlt
    report = list(zip([a+b for a, b in zip(names, names[1:])], [round(g) for g in gaps], [round(d) for d in deltas]))
    if positions: return pen.getCommands(), (x - deltas[-1])*k, report, pos
    return pen.getCommands(), (x - deltas[-1])*k, report
