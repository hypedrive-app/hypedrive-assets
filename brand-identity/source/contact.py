import glob
from PIL import Image
fs=sorted(glob.glob('/tmp/hdwm/spec_ba/before/a-*.png'))
ims=[Image.open(f) for f in fs]; w,h=ims[0].size
cols=6
for k in range(0,len(ims),24):
    ch=ims[k:k+24]; rows=(len(ch)+cols-1)//cols
    S=Image.new('RGB',(cols*w,rows*h),'white')
    for i,im in enumerate(ch): S.paste(im,((i%cols)*w,(i//cols)*h))
    S.save(f'/tmp/hdwm/spec_ba/contact{k//24}.png')
print(w,h)
