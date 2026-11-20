"""Every Hypedrive mark in one place: one palette, one font, one lockup, one audit."""
import sys, os, re, subprocess
sys.path.insert(0, "/tmp/hdwm")
import versions as V          # v1-v5
import themed as T            # v8-v12 (registers into V.MARKS)
import refined as R           # r1-r5
import packages as PK         # p1-p6 (registers into R.MARKS)
import iso as I               # iso1-iso6
from text2path import text_path

INK_L, INK_D = "#141414", "#ffffff"
FONT, WGHT, CAP, TRACK, SOFT, GAP = "Jakarta", 760, 18.6, -0.008, 0.55, 9.5

def flat(fn):   # (ink, eye) marks
    return lambda dark: fn(INK_D if dark else INK_L, INK_L if dark else "#ffffff")
def isom(fn):   # iso marks take dark
    return lambda dark: fn(dark)

REG = [
    ("v01-stripes",   flat(V.mark_stripes)),
    ("v02-steps",     flat(V.mark_steps)),
    ("v03-monogram",  flat(V.mark_h)),
    ("v04-chevrons",  flat(V.mark_chevrons)),
    ("v05-gauge",     flat(V.mark_gauge)),
    ("v08-marketing", flat(T.m_marketing)),
    ("v09-discount",  flat(T.m_discount)),
    ("v10-product",   flat(T.m_product)),
    ("v11-packages",  flat(T.m_packages)),
    ("v12-vibes",     flat(T.m_vibes)),
    ("r1-tag",        flat(R.r_tag)),
    ("r2-bag",        flat(R.r_bag)),
    ("r3-spark",      flat(R.r_spark)),
    ("r4-megaphone",  flat(R.r_mega)),
    ("r5-box",        flat(R.r_box)),
    ("p1-unbox",      flat(PK.p_unbox)),
    ("p2-stack",      flat(PK.p_stack)),
    ("p3-express",    flat(PK.p_express)),
    ("p4-dieline",    flat(PK.p_dieline)),
    ("p5-rise",       flat(PK.p_rise)),
    ("p6-isotag",     flat(PK.p_isotag)),
    ("iso1-parcel",   isom(I.i_parcel)),
    ("iso2-stack",    isom(I.i_stack)),
    ("iso3-unbox",    isom(I.i_unbox)),
    ("iso4-label",    isom(I.i_label)),
    ("iso5-express",  isom(I.i_express)),
    ("iso6-monogram", isom(I.i_h)),
]

def lockup(mark_fn, dark, text="Hypedrive"):
    ink = INK_D if dark else INK_L
    m, mw = mark_fn(dark)
    d, tw = text_path(text, WGHT, CAP, TRACK, FONT)
    ox = mw + GAP; W = ox + tw + SOFT
    pad = 1.0
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {W+2*pad:.2f} {28+2*pad}" '
            f'width="{(W+2*pad)*10:.0f}" height="{(28+2*pad)*10:.0f}">{m}'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate({ox:.2f} 22.9)" d="{d}"/></svg>')

def mark_only(mark_fn, dark):
    m, mw = mark_fn(dark)
    side = max(mw, 28) * 1.16
    ox = (side - mw) / 2; oy = (side - 28) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side:.2f} {side:.2f}" width="512" height="512">'
            f'<g transform="translate({ox:.2f} {oy:.2f})">{m}</g></svg>')

def wordmark_only(dark):
    ink = INK_D if dark else INK_L
    d, tw = text_path("Hypedrive", WGHT, CAP, TRACK, FONT)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 3 {tw+2:.2f} 26" width="{(tw+2)*10:.0f}" height="260">'
            f'<path fill="{ink}" stroke="{ink}" stroke-width="{SOFT}" stroke-linejoin="round" transform="translate(0 22.9)" d="{d}"/></svg>')

def build(out):
    os.makedirs(out, exist_ok=True)
    files = []
    for name, fn in REG:
        for theme, dark in (("light", False), ("dark", True)):
            for kind, svg in (("lockup", lockup(fn, dark)), ("mark", mark_only(fn, dark))):
                p = os.path.join(out, f"hypedrive-{name}-{kind}-{theme}.svg")
                open(p, "w").write(svg); files.append(p)
    for theme, dark in (("light", False), ("dark", True)):
        p = os.path.join(out, f"hypedrive-wordmark-{theme}.svg"); open(p, "w").write(wordmark_only(dark)); files.append(p)
    return files

if __name__ == "__main__":
    for p in build(sys.argv[1]):
        h = "512" if "-mark-" in p else "600"
        subprocess.run(["rsvg-convert", "-h", h, p, "-o", p[:-4] + ".png"], check=True)
