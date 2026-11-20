import sys
from PIL import Image
p=sys.argv[1]; im=Image.open(p).convert("RGB")
W,H=im.size
px=im.load()
def uniform(y):
    c=px[0,y]
    return all(px[x,y]==c for x in range(0,W,7))
y=H-1
while y>0 and uniform(y): y-=1
im=im.crop((0,0,W,min(y+24,H)))
im.save(p)
n=0
for y0 in range(0,im.height,900):
    im.crop((0,y0,W,min(y0+900,im.height))).save(p.replace(".png",f"_t{n}.png")); n+=1
print(p,im.size,n)
