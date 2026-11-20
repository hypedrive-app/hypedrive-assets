import sys
from PIL import Image, ImageDraw
b,a,out=sys.argv[1:4]
box=tuple(map(int,sys.argv[4:8])) if len(sys.argv)>7 else None
B=Image.open(b).convert("RGB"); A=Image.open(a).convert("RGB")
if box: B=B.crop(box); A=A.crop(box)
W=max(B.width,A.width); 
im=Image.new("RGB",(W,B.height+A.height+40),(255,0,255))
im.paste(B,(0,0)); im.paste(A,(0,B.height+40)); im.save(out)
