import sys,glob
from PIL import Image
# usage: q1mont.py out n1 n2 ...  (side by side 2x-ish crops of screens dir)
out=sys.argv[1]; ns=sys.argv[2:]
ims=[]
for n in ns:
    f=glob.glob(f'/home/shivam-gupta/Downloads/hypedrive-wordmark/BRAND/ui/screens/{int(n):02d}-*.png')[0]
    ims.append(Image.open(f).convert('RGB').crop((30,30,420,880)))
m=Image.new('RGB',(390*len(ims),850),'white')
for i,im in enumerate(ims): m.paste(im,(i*390,0))
m.save(out)
