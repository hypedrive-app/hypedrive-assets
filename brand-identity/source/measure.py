import sys, subprocess, io
sys.path.insert(0, '/tmp/hdwm')
import isoill as I, isofam as F
import numpy as np
from PIL import Image
res = {}
for name, fn in I.ILLS:
    svg = F.square(fn, 'light', 512, 0.14)
    png = subprocess.run(['rsvg-convert', '-w', '512', '-h', '512'], input=svg.encode(), capture_output=True).stdout
    a = np.array(Image.open(io.BytesIO(png)).convert('RGBA'))[:, :, 3] > 40
    ys, xs = np.where(a)
    A = a.mean(); bw, bh = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
    cy, cx = ys.mean() / 512, xs.mean() / 512
    res[name] = A
    print(f"{name:9s} area {A:.3f}  bbox {bw}x{bh} fill-of-bbox {a.sum()/(bw*bh):.2f}  centroid ({cx:.2f},{cy:.2f})")
