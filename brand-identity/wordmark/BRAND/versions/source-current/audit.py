"""Automated checks for every generated SVG/PNG.
1 XML parses            2 every url(#id) resolves, ids unique
3 renders               4 nothing touches the canvas edge (no clipping)
5 all four colours present (blue, orange, yellow + ink) in the rendered mark pixels
6 mark is visible at 16px (enough non-transparent pixels)"""
import sys, os, re, glob, subprocess, io, colorsys
from xml.etree import ElementTree as ET
import numpy as np
from PIL import Image

def hue_family(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    if s < 0.25 or l < 0.12 or l > 0.92: return "ink"
    h *= 360
    if 200 <= h <= 235: return "blue"
    if 5 <= h <= 30: return "orange"
    if 35 <= h <= 55: return "yellow"
    return "other"

def render(path, h):
    png = subprocess.run(["rsvg-convert", "-h", str(h), path], capture_output=True, check=True).stdout
    return np.array(Image.open(io.BytesIO(png)).convert("RGBA"))

def check(path):
    issues = []
    txt = open(path).read()
    try: ET.fromstring(txt)
    except ET.ParseError as e: return [f"XML: {e}"]
    ids = re.findall(r'\bid="([^"]+)"', txt)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: issues.append(f"duplicate ids {sorted(dup)[:4]}")
    missing = set(re.findall(r'url\(#([^)]+)\)', txt)) - set(ids)
    if missing: issues.append(f"unresolved refs {sorted(missing)[:4]}")
    try: a = render(path, 400)
    except subprocess.CalledProcessError as e: return issues + ["render failed"]
    al = a[..., 3]
    edge = max(al[0].max(), al[-1].max(), al[:, 0].max(), al[:, -1].max())
    if edge > 8 and not any(k in path for k in ('app-icon', 'splash', 'pattern', 'print', 'social', 'screens')): issues.append(f"clipped at canvas edge (alpha {edge})")
    name = os.path.basename(path)
    if "-mark-" in name:
        px = a[al > 200][:, :3]
        fam = {}
        for r, g, b in px[:: max(1, len(px)//6000)]:
            f = hue_family(int(r), int(g), int(b)); fam[f] = fam.get(f, 0) + 1
        tot = sum(fam.values())
        need = ["blue", "orange", "yellow"] + (["ink"] if "light" in name else [])
        for f in need:
            if fam.get(f, 0) / tot < 0.015: issues.append(f"colour missing/too small: {f} ({fam.get(f,0)/tot:.1%})")
        if "dark" in name:   # light ink parts on dark: must have near-white pixels
            w = ((px.min(axis=1) > 200)).mean()
            if w < 0.015: issues.append(f"no light ink part on dark ({w:.1%})")
        s = render(path, 16)[..., 3]
        if (s > 128).sum() < 40: issues.append(f"too faint at 16px ({(s>128).sum()} px)")
    return issues

if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(sys.argv[1], "*.svg")))
    bad = 0
    for f in files:
        iss = check(f)
        if iss:
            bad += 1; print(os.path.basename(f), "->", "; ".join(iss))
    print(f"\n{len(files)} files checked, {bad} with issues")
