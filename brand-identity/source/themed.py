import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
import versions as V
from versions import rpoly, banded, Ids, BLUE, ORNG, YELL, PAL, MARKS, lockup

def cols3(shape_d, x0, x1, ys=(0, 28), slope=0.45, cuts=None):
    """Fill a shape with three vertical hue columns (blue/orange/yellow), each PostHog-banded."""
    cid = Ids.new("k"); cw = (x1 - x0) / 3
    o = [f'<clipPath id="{cid}"><path d="{shape_d}"/></clipPath><g clip-path="url(#{cid})">']
    for i, pal in enumerate(PAL):
        cx0 = x0 + i*cw
        col = f"M{cx0-0.02:.2f} -5H{cx0+cw+0.02:.2f}V40H{cx0-0.02:.2f}z"
        h = ys[1]-ys[0]
        o.append(banded(col, pal, cx0, cx0+cw, cuts or [ys[0]+h*0.36, ys[0]+h*0.7], slope))
    o.append("</g>")
    return "".join(o)

def m_marketing(ink, eye):
    o = []
    horn = rpoly([(7, 9.5), (25, 1.5), (25, 26.5), (7, 18.5)], [1, 1.5, 1.5, 1])
    o.append(cols3(horn, 7, 25))
    o.append(f'<path fill="{ink}" d="{rpoly([(0,8.5),(8,8.5),(8,19.5),(0,19.5)], 2.4)}"/>')
    o.append(f'<path fill="{ink}" d="{rpoly([(9,18.5),(14,18.5),(15.5,27),(10.5,27)], 1.6)}"/>')
    o.append(f'<path fill="{ink}" d="{rpoly([(24,0),(29,0),(29,28),(24,28)], 2.2)}"/>')
    o.append(f'<circle cx="4" cy="14" r="1.8" fill="{eye}"/>')
    for r, sw in [(5.5, 2.9), (10.5, 2.9)]:
        a = math.radians(40); cx, cy = 29.5, 14
        o.append(f'<path d="M{cx+r*math.cos(a):.2f} {cy-r*math.sin(a):.2f}A{r} {r} 0 0 1 {cx+r*math.cos(a):.2f} {cy+r*math.sin(a):.2f}" fill="none" stroke="{ink}" stroke-width="{sw}" stroke-linecap="round"/>')
    return "".join(o), 29.5 + 10.5 + 1.5

def m_discount(ink, eye):
    o = []
    tag = rpoly([(0, 14), (10, 0.5), (34, 0.5), (34, 27.5), (10, 27.5)], [2.5, 2.5, 4, 4, 2.5])
    o.append(f'<path fill="{ink}" d="{tag}"/>')
    o.append(f'<circle cx="8.6" cy="14" r="2.3" fill="{eye}"/>')
    # % : banded slash + two coloured rings
    sl = rpoly([(16.5, 23.5), (26, 4.5), (29.5, 4.5), (20, 23.5)], 1.6)
    o.append(banded(sl, BLUE, 16, 30, [11, 17], 0.4))
    for cx, cy, pal in [(18.3, 9, ORNG), (28.2, 19, YELL)]:
        gid = Ids.new("g")
        o.append(f'<linearGradient id="{gid}" x1="0" y1="{cy-4}" x2="0" y2="{cy+4}" gradientUnits="userSpaceOnUse"><stop stop-color="{pal[0]}"/><stop offset=".5" stop-color="{pal[1]}"/><stop offset="1" stop-color="{pal[2]}"/></linearGradient>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="none" stroke="url(#{gid})" stroke-width="2.6"/>')
    return "".join(o), 34

def m_product(ink, eye):
    o = []
    o.append(f'<path d="M9.5 11V7.5a5.5 5.5 0 0 1 11 0V11" fill="none" stroke="{ink}" stroke-width="3.2" stroke-linecap="round"/>')
    bag = rpoly([(2.5, 9), (27.5, 9), (30, 28), (0, 28)], [2, 2, 2.6, 2.6])
    o.append(cols3(bag, 0.6, 29.4, ys=(9, 28)))
    o.append(f'<path fill="{ink}" d="{rpoly([(2.5,9),(27.5,9),(27.9,12.5),(2.1,12.5)], [2,2,0.01,0.01])}"/>')
    o.append(f'<circle cx="9.5" cy="10.8" r="1.25" fill="{eye}"/><circle cx="20.5" cy="10.8" r="1.25" fill="{eye}"/>')
    return "".join(o), 30

def m_packages(ink, eye):
    o = []; W = 27; h = W/2; c = W/2
    top = [(c, 0.5), (W, 7), (c, 13.5), (0, 7)]
    left = [(0, 7), (c, 13.5), (c, 27.5), (0, 21)]
    right = [(c, 13.5), (W, 7), (W, 21), (c, 27.5)]
    o.append(banded(rpoly(top, [1.6, 1.6, 0.01, 1.6]), YELL, 0, W, [4.5, 8.5], 0.0))
    o.append(banded(rpoly(left, [1.6, 0.01, 1.6, 1.6]), BLUE, 0, c, [15, 21.5], 0.48))
    o.append(banded(rpoly(right, [0.01, 1.6, 1.6, 1.6]), ORNG, c, W, [13, 19.5], -0.48))
    # black tape across the top and down the front-left
    o.append(f'<path fill="{ink}" d="M{c*0.5-1.7:.2f} {3.75+0.85:.2f}L{c*0.5+1.7:.2f} {3.75-0.85:.2f}L{c*1.5+1.7:.2f} {10.25-0.85:.2f}L{c*1.5-1.7:.2f} {10.25+0.85:.2f}z"/>')
    o.append(f'<path fill="{ink}" d="M{c*1.5-1.7:.2f} {10.25+0.85:.2f}L{c*1.5+1.7:.2f} {10.25-0.85:.2f}L{c*1.5+1.7:.2f} {17.6:.2f}L{c*1.5-1.7:.2f} {19.3:.2f}z"/>')
    o.append(f'<circle cx="{c*0.5+1.6:.2f}" cy="18.6" r="1.8" fill="{eye}" />')
    return "".join(o), W

def m_vibes(ink, eye):
    o = []; bw = 6; gap = 2.4
    hs = [(BLUE, 13), (ORNG, 22), (YELL, 16), (None, 28), (BLUE, 19)]
    hs = [(BLUE, 12), (ORNG, 22), (YELL, 17), (None, 28)]
    for i, (pal, hgt) in enumerate(hs):
        x = i*(bw+gap); y0 = (28-hgt)/2
        d = rpoly([(x, y0), (x+bw, y0), (x+bw, y0+hgt), (x, y0+hgt)], 3)
        if pal: o.append(banded(d, pal, x, x+bw, [y0+hgt*0.38, y0+hgt*0.7], 0.55))
        else:
            o.append(f'<path fill="{ink}" d="{d}"/>'); o.append(f'<circle cx="{x+bw/2}" cy="6.2" r="1.6" fill="{eye}"/>')
    # wave tail
    x = 4*(bw+gap) + 0.6
    o.append(f'<path d="M{x:.2f} 14c2.2 -5 4.4 -5 6.6 0s4.4 5 6.6 0" fill="none" stroke="{ink}" stroke-width="3" stroke-linecap="round"/>')
    return "".join(o), x + 13.2 + 1.5

MARKS.update(marketing=m_marketing, discount=m_discount, product=m_product, packages=m_packages, vibes=m_vibes)
NEW = [("v8-marketing", "marketing"), ("v9-discount", "discount"), ("v10-product", "product"), ("v11-packages", "packages"), ("v12-vibes", "vibes")]
if __name__ == "__main__":
    out = sys.argv[1]
    for name, mk in NEW:
        for theme, ink, eye in [("light", "#151515", "#fff"), ("dark", "#fff", "#151515")]:
            p = os.path.join(out, f"hypedrive-{name}-{theme}.svg")
            open(p, "w").write(lockup(mk, ink, eye))
            subprocess.run(["rsvg-convert", "-h", "560", p, "-o", p[:-4] + ".png"], check=True)
