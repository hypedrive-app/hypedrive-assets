import sys, os, math, subprocess
sys.path.insert(0, "/tmp/hdwm")
import refined as R
from refined import rpoly, banded, Ids, BLUE, ORNG, YELL, PAL, clipwrap, grad, striped, G

def full(): return "M-10 -10H90V40H-10z"

def rot_bar(cx, cy, w, l, ang, pal):
    """Rounded bar standing on (cx,cy), length l upwards, rotated ang degrees."""
    d = rpoly([(cx-w/2, cy), (cx-w/2, cy-l), (cx+w/2, cy-l), (cx+w/2, cy)], w/2-0.01)
    inner = banded(full(), pal, cx-w, cx+w, [cy-l+l*0.33, cy-l+l*0.62], 0.25)
    cid = Ids.new("b")
    return f'<g transform="rotate({ang} {cx} {cy})"><clipPath id="{cid}"><path d="{d}"/></clipPath><g clip-path="url(#{cid})">{inner}</g></g>'

def p_unbox(ink, eye):
    """Open parcel with hype bursting out."""
    o = [rot_bar(15, 17, 5.4, 15.5, -27, BLUE), rot_bar(15, 17, 5.4, 16.5, 27, YELL), rot_bar(15, 17, 5.4, 16.8, 0, ORNG)]
    o.append(f'<path fill="{ink}" d="{rpoly([(4,14.6),(13.2,14.6),(10,10.2),(0.6,10.2)], 1.1)}"/>')
    o.append(f'<path fill="{ink}" d="{rpoly([(16.8,14.6),(26,14.6),(29.4,10.2),(20,10.2)], 1.1)}"/>')
    o.append(f'<path fill="{ink}" d="{rpoly([(4,15.8),(26,15.8),(26,28),(4,28)], [0.8,0.8,2.6,2.6])}"/>')
    o.append(f'<circle cx="15" cy="21.9" r="2" fill="{eye}"/>')
    return "".join(o), 30

def box(x0, y0, x1, y1, pal):
    d = rpoly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], 2)
    inner = banded(full(), pal, x0, x1, [y0+(y1-y0)*0.42, y0+(y1-y0)*0.75], 0.32)
    m = (x0+x1)/2
    inner += f'<path fill="#fff" fill-opacity=".4" d="M{m-1.3:.2f} {y0-1}H{m+1.3:.2f}V{y0+(y1-y0)*0.45:.2f}H{m-1.3:.2f}z"/>'
    return clipwrap(d, inner)

def p_stack(ink, eye):
    """Pyramid of parcels — orders piling up."""
    o = [box(0, 18.4, 13.6, 28, BLUE), box(15.1, 18.4, 28.7, 28, ORNG), box(6.3, 7.8, 22.4, 16.9, YELL)]
    o.append(f'<path fill="{ink}" d="{rpoly([(10.4,0),(18.3,0),(18.3,6.3),(10.4,6.3)], 1.8)}"/>')
    o.append(f'<circle cx="14.35" cy="3.15" r="1.5" fill="{eye}"/>')
    return "".join(o), 28.7

def p_express(ink, eye):
    """Parcel in motion with speed trails."""
    o = []
    for (y, x0, pal) in [(4.2, 4, BLUE), (11.8, 0, ORNG), (19.4, 6, YELL)]:
        gid, g = grad(pal, x0, 0, 22, 0)
        o.append(g + f'<path fill="url(#{gid})" d="{rpoly([(x0,y),(22,y),(22,y+4.4),(x0,y+4.4)], 2.2)}"/>')
    bx = 17
    o.append(f'<path fill="{ink}" d="{rpoly([(bx,1.5),(bx+24,1.5),(bx+24,26.5),(bx,26.5)], 3)}"/>')
    o.append(f'<path fill="{eye}" d="M{bx+10.3} 1.5H{bx+13.7}V12H{bx+10.3}z"/>')
    o.append(f'<path fill="{eye}" d="{rpoly([(bx+15.5,18.5),(bx+21,18.5),(bx+21,22.8),(bx+15.5,22.8)], 0.9)}"/>')
    return "".join(o), bx + 24

def p_dieline(ink, eye):
    """Unfolded box net (dieline)."""
    o = []; s = 8.6; g = 1.15; y = (28 - s) / 2
    xs = [i*(s+g) for i in range(4)]
    for x, pal in zip(xs, [BLUE, None, YELL, ORNG]):
        d = rpoly([(x, y), (x+s, y), (x+s, y+s), (x, y+s)], 1.6)
        if pal: o.append(clipwrap(d, banded(full(), pal, x, x+s, [y+3.4, y+6.2], 0.4)))
        else: o.append(f'<path fill="{ink}" d="{d}"/><circle cx="{x+s/2:.2f}" cy="{y+s/2:.2f}" r="1.6" fill="{eye}"/>')
    x = xs[1]
    top = rpoly([(x, y-g), (x+1.4, 1.2), (x+s-1.4, 1.2), (x+s, y-g)], [0.6, 1.6, 1.6, 0.6])
    bot = rpoly([(x, y+s+g), (x+s, y+s+g), (x+s-1.4, 26.8), (x+1.4, 26.8)], [0.6, 0.6, 1.6, 1.6])
    o.append(clipwrap(top, banded(full(), ORNG, x, x+s, [4.6, 7.4], 0.4)))
    o.append(clipwrap(bot, banded(full(), BLUE, x, x+s, [22.2, 25], 0.4)))
    return "".join(o), xs[3] + s

def p_rise(ink, eye):
    """Box whose lid is an up-arrow — sales going up."""
    o = []
    body = rpoly([(1, 13), (29, 13), (29, 28), (1, 28)], [0.8, 0.8, 2.6, 2.6])
    o.append(striped(body, [1, 10.6, 19.6, 99], 0, [BLUE, ORNG, YELL], ink, 0.4))
    o.append(f'<path d="M3.2 10.4L15 2.4L26.8 10.4" fill="none" stroke="{ink}" stroke-width="4.4" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(o), 30

def p_isotag(ink, eye):
    """Isometric parcel with a hanging price tag."""
    o = []; W = 26; c = W/2
    top = [(c, 0.6), (W, 7), (c, 13.4), (0, 7)]
    left = [(0, 7), (c, 13.4), (c, 27.4), (0, 21)]
    right = [(c, 13.4), (W, 7), (W, 21), (c, 27.4)]
    o.append(clipwrap(rpoly(left, [1.6, 0.01, 1.6, 1.6]), banded(full(), BLUE, 0, c, [15.5, 21.5], 0.49)))
    o.append(clipwrap(rpoly(top, [1.6, 1.6, 0.01, 1.6]), banded(full(), YELL, 0, W, [5.2, 8.8], 0.0)))
    o.append(clipwrap(rpoly(right, [0.01, 1.6, 1.6, 1.6]), banded(full(), ORNG, c, W, [14, 20], -0.49)))
    tx, ty = W + 2.5, 11
    o.append(f'<path d="M{W-2.8} 12.6Q{W+0.4} 9 {tx+6} {ty+2.2}" fill="none" stroke="{ink}" stroke-width="1.5" stroke-linecap="round"/>')
    tag = rpoly([(tx+1, ty+1), (tx+11, ty+1), (tx+11, ty+11.5), (tx+6, ty+16), (tx+1, ty+11.5)], [1.6, 1.6, 1.4, 2, 1.4])
    o.append(f'<path fill="{ink}" d="{tag}"/>')
    o.append(f'<circle cx="{tx+6}" cy="{ty+4.4}" r="1.6" fill="{eye}"/>')
    return "".join(o), tx + 11

R.MARKS.update(unbox=p_unbox, stack=p_stack, express=p_express, dieline=p_dieline, rise=p_rise, isotag=p_isotag)
NAMES = ["unbox", "stack", "express", "dieline", "rise", "isotag"]

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    for i, mk in enumerate(NAMES, 1):
        for theme, ink, eye in [("light", "#141414", "#fff"), ("dark", "#fff", "#141414")]:
            p = os.path.join(out, f"hypedrive-p{i}-{mk}-{theme}.svg")
            open(p, "w").write(R.lockup(mk, ink, eye, "jakarta"))
            subprocess.run(["rsvg-convert", "-h", "592", p, "-o", p[:-4] + ".png"], check=True)
            m, mw = R.MARKS[mk](ink, eye)
            q = os.path.join(out, f"hypedrive-p{i}-{mk}-mark-{theme}.svg")
            open(q, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 {mw+4:.2f} 32" width="{(mw+4)*16:.0f}" height="512">{m}</svg>')
            subprocess.run(["rsvg-convert", "-h", "512", q, "-o", q[:-4] + ".png"], check=True)
