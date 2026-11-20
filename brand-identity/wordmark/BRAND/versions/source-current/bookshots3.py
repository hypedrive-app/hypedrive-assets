# Render chosen UI-kit sections alone in Zen, trim, and save as book images.
import subprocess, os, sys
from PIL import Image, ImageChops
U = os.path.expanduser("~/Downloads/hypedrive-wordmark/BRAND/ui"); Z = os.path.expanduser("~/.local/share/zen/zen")
OUT = "/tmp/hdwm/bookshots3"
os.makedirs(OUT, exist_ok=True)
def shot(png, size, html):
    subprocess.run(["timeout", "90", Z, "--headless", "--no-remote", "--profile", "/tmp/hdwm/zt/prof3", "--screenshot", png, f"--window-size={size}", "file://" + html], capture_output=True)
def _crop(im, pad):
    bgc = im.getpixel((2, im.height - 2)); box = ImageChops.difference(im, Image.new("RGB", im.size, bgc)).getbbox()
    return im.crop((max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, im.width), min(box[3] + pad, im.height))) if box else im
def trim(png):
    im = _crop(Image.open(png).convert("RGB"), 0)   # 1: drop the page backdrop around the sheet
    _crop(im, 40).save(png)                           # 2: drop empty sheet, keep a 40px margin
for theme, src in (("light", "hypedrive-ui-kit.html"), ("dark", "hypedrive-ui-kit-dark.html")):
    html = open(os.path.join(U, src)).read()
    WARM = ":root,[data-theme=light],body{--hd-bg-subtle:#f7f7f8!important;--hd-canvas:#f7f7f8!important} .box:not([data-theme=dark]){background:#f7f7f8!important;border-color:transparent!important;box-shadow:none!important} body,.sheet-w{background:#f7f7f8!important}" if False else ""
    for n in (2, 4, 5, 6, 8):
        tmp = os.path.join(U, f"_sec{n}.html")
        open(tmp, "w").write(html.replace("</head>", f"<style>.sec{{display:none!important}} .sec:nth-of-type({n}){{display:block!important}} .hero{{display:none!important}} .sec>h2,.sec>p{{display:none!important}} {WARM} body,.sheet-w{{padding-top:0!important;margin-top:0!important}}</style></head>", 1))
        png = f"{OUT}/sec{n}-{theme}.png"; shot(png, "1600,3000", tmp); os.remove(tmp); trim(png)
        print(png, Image.open(png).size)
