#!/usr/bin/env python3
"""Regenerate all raster assets from the source SVGs in logos/.
Requires: cairosvg, pillow  (pip install cairosvg pillow)
Run:      python3 build.py
"""
import cairosvg
from PIL import Image

def png(src, out, w=None, h=None):
    cairosvg.svg2png(url=src, write_to=out, output_width=w, output_height=h)

# Favicons / PWA icons (from the dark app tile)
for s in [16, 32, 48, 64, 180, 192, 256, 384, 512, 1024]:
    png("logos/app-icon-dark.svg", f"favicons/icon-{s}.png", w=s, h=s)
png("logos/app-icon-dark.svg", "favicons/apple-touch-icon.png", w=180, h=180)
png("logos/app-icon-maskable.svg", "favicons/icon-maskable.png", w=512, h=512)
Image.open("favicons/icon-16.png").save(
    "favicons/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)]
)
import shutil; shutil.copy("logos/app-icon-dark.svg", "favicons/favicon.svg")

# Email wordmarks (light + dark), 1x + 2x
png("logos/wordmark.svg", "email/wordmark.png", w=600)
png("logos/wordmark.svg", "email/wordmark@2x.png", w=1200)
png("logos/wordmark-dark.svg", "email/wordmark-dark.png", w=600)
png("logos/wordmark-dark.svg", "email/wordmark-dark@2x.png", w=1200)
png("logos/icon.svg", "email/icon.png", w=128)
png("logos/icon.svg", "email/icon@2x.png", w=256)

# OG cards
for f in ["og", "og-creator", "og-brand"]:
    png(f"og/{f}.svg", f"og/{f}.png", w=1200, h=630)

print("assets rebuilt")
