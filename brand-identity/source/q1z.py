import sys
from PIL import Image
# usage: q1z.py src out [x0 y0 x1 y1]  -> 2x crop
src,out=sys.argv[1:3]; im=Image.open(src).convert('RGB')
box=tuple(map(int,sys.argv[3:7])) if len(sys.argv)>6 else (30,30,420,880)
c=im.crop(box); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(out)
