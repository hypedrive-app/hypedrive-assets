"""Trim the empty page background below a desktop render (keeps a 40px margin)."""
import sys
from PIL import Image
for p in sys.argv[1:]:
    im = Image.open(p).convert("RGB"); w, h = im.size; bg = im.getpixel((5, h - 5)); px = im.load()
    y = h - 1
    while y > 0 and all(px[x, y] == bg for x in range(0, w, 8)): y -= 1
    im.crop((0, 0, w, min(h, y + 41))).save(p)
