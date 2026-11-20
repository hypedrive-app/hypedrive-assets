import sys
INK = "#111"
S = 4.25; R = 1.24; GAP = 2.4
BASE = 22.9; XH = 9.3; CAP = 4.0; DESC = 28.0
CY = 16.05; RO = 7.0; RIX = 3.2; RIY = 3.6

def rect(x, y0, y1, w=S, r=R):
    return f'<rect x="{x:.2f}" y="{y0:.2f}" width="{w:.2f}" height="{y1-y0:.2f}" rx="{r}"/>'

def ring(cx, cy=CY, ro=RO, rix=RIX, riy=RIY):
    return (f'<path fill-rule="evenodd" d="M{cx-ro:.2f} {cy:.2f}a{ro} {ro} 0 1 0 {2*ro} 0a{ro} {ro} 0 1 0 {-2*ro} 0z'
            f'M{cx-rix:.2f} {cy:.2f}a{rix} {riy} 0 1 0 {2*rix} 0a{rix} {riy} 0 1 0 {-2*rix} 0z"/>')

def stroke(d, w=3.9, cap="round"):
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="{cap}" stroke-linejoin="round"/>'


import math
def e_glyph(x, cid):
    ecx = x + RO; cy0 = 17.0; a = math.radians(48); L = 20
    wedge = f"M{ecx:.2f} {cy0}L{ecx+L:.2f} {cy0}L{ecx+L*math.cos(a):.2f} {cy0+L*math.sin(a):.2f}z"
    big = f"M{x-2:.2f} -2H{x+2*RO+2:.2f}V32H{x-2:.2f}z"
    out = [f'<clipPath id="{cid}"><path clip-rule="evenodd" d="{big}{wedge}"/></clipPath>',
           f'<g clip-path="url(#{cid})">{ring(ecx)}</g>',
           f'<rect x="{x+1:.2f}" y="14.6" width="{2*RO-1:.2f}" height="2.4" rx="0.5"/>']
    return out

def word(ox):
    g = []; x = ox
    # H
    g += [rect(x, CAP, BASE), rect(x+11, CAP, BASE), f'<rect x="{x+2:.2f}" y="11.6" width="11" height="3.6"/>']
    x += 15.25 + GAP
    # y : u-shape + descender hook
    w = 14.25; cx = x + w/2; ro = w/2; cyb = 23.1 - ro; rix = ro - S + 0.2; riy = 3.4
    g += [rect(x, XH, cyb+2), rect(x+w-S, XH, 24.5)]
    g.append(f'<path fill-rule="evenodd" d="M{x:.2f} {cyb:.2f}a{ro} {ro} 0 0 0 {w:.2f} 0z M{cx-rix:.2f} {cyb:.2f}a{rix} {riy} 0 0 0 {2*rix:.2f} 0z"/>')
    sx = x + w - S/2
    g.append(stroke(f"M{sx:.2f} 21V22.5a3.5 3.5 0 0 1 -3.5 3.5H{cx-1.2:.2f}", w=4.0))
    x += w + GAP
    # p
    g += [rect(x, XH, DESC), ring(x + RO + 0.1)]
    x += 2*RO + 0.1 + GAP
    # e
    g += e_glyph(x, 'ecut')
    x += 2*RO + GAP
    # d
    g += [ring(x + RO), rect(x + 2*RO - S, CAP, BASE)]
    x += 2*RO + GAP
    # r
    g.append(rect(x, XH, BASE))
    g.append(stroke(f"M{x+S/2:.2f} 17.2V15.6a5.0 5.0 0 0 1 5.0 -5.0H{x+S/2+6.6:.2f}", w=3.9))
    x += S + 6.6 + GAP - 0.4
    # i
    g += [rect(x, XH, BASE), rect(x, CAP, 7.75)]
    x += S + GAP - 0.6
    # v
    vw = 13.4
    g.append(f'<clipPath id="vcut"><rect x="{x-2:.2f}" y="{XH:.2f}" width="{vw+4:.2f}" height="20"/></clipPath>')
    g.append(f'<g clip-path="url(#vcut)">' + stroke(f"M{x+2.0:.2f} 6L{x+vw/2:.2f} 20.9L{x+vw-2.0:.2f} 6", w=4.4, cap="butt") + '</g>')
    x += vw + GAP - 0.8
    # e
    g += e_glyph(x, 'ecut2')
    x += 2*RO
    return "\n".join(g), x

# ---- mark: three forward-leaning speed stripes + black "drive" nose with a headlight
PAL = [("#3f80ff","#0255ff","#0041c6"), ("#ff651e","#ef3c00","#c42c00"), ("#ffd849","#ffb700","#ff9500")]
def mark():
    out = []; defs = []
    lean = 6.0; sw = 7.6; gap = 2.0; inset = 1.25
    for i,(c1,c2,c3) in enumerate(PAL):
        x0 = i*(sw+gap)
        poly = f"M{x0+inset:.2f} {28-inset}L{x0+sw-inset:.2f} {28-inset}L{x0+sw+lean-inset:.2f} {inset}L{x0+lean+inset:.2f} {inset}z"
        defs.append(f'<clipPath id="s{i}"><path d="{poly}" stroke="#000" stroke-width="{2*inset}" stroke-linejoin="round"/></clipPath>')
        # three tonal bands split by lines perpendicular to the lean
        b = []
        for k,(c,y) in enumerate([(c1,0),(c2,9.6),(c3,19.2)]):
            b.append(f'<path fill="{c}" d="M{x0-4:.2f} {y-2+ (0 if k==0 else 0):.2f}L{x0+sw+lean+4:.2f} {y+1.2:.2f}V40H{x0-4:.2f}z"/>')
        out.append(f'<g clip-path="url(#s{i})">' + "".join(b) + '</g>')
    x0 = 3*(sw+gap)
    ni = 2.2
    tipx = x0 + lean + 19.5
    nose = f"M{x0+ni+0.4:.2f} {28-ni}L{x0+lean+ni+0.4:.2f} {ni}L{tipx-ni:.2f} 14z"
    out.append(f'<path fill="{INK}" stroke="{INK}" stroke-width="{2*ni}" stroke-linejoin="round" d="{nose}"/>')
    out.append(f'<circle cx="{x0+lean/2+6.6:.2f}" cy="14" r="2.05" fill="#fff"/>')
    mw = tipx
    return "\n".join(defs), "\n".join(out), mw

def build(ink="#111", with_mark=True):
    global INK; INK = ink
    d, m, mw = mark()
    ox = mw + 10.5 if with_mark else 0
    w, wx = word(ox)
    W = wx + 0.5
    body = (m if with_mark else "")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} 28" width="{W*1:.0f}" height="28"><defs>{d}</defs>{body}<g fill="{ink}">{w}</g></svg>'

if __name__ == "__main__":
    out = sys.argv[1]
    import os
    open(os.path.join(out,"hypedrive-wordmark.svg"),"w").write(build("#111"))
    open(os.path.join(out,"hypedrive-wordmark-dark.svg"),"w").write(build("#fff").replace('fill="#fff"/>','fill="#111"/>',1) if False else build("#fff"))
