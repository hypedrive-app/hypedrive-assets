import sys; sys.path.insert(0,'/tmp/hdwm')
import isoill as IL, isofam as F
names=sys.argv[2:]; out=sys.argv[1]
d=dict(IL.ILLS)
def img(fn,th,size,pad=0.16): return f'<img style="width:{size}px" src="data:image/svg+xml;utf8,{F.square(fn,th,size,pad).replace(chr(35),"%23").replace(chr(34),chr(39))}">'
h=""
for th,bg in (("light","#f4f5f8"),("dark","#0f1115")):
    h+=f'<div style="display:flex;gap:10px;background:{bg};padding:8px;margin:4px">'+"".join(img(d[n],th,int(__import__("os").environ.get("BIG","420"))) for n in ["parcel"]+names)+'</div>'
    h+=f'<div style="display:flex;gap:10px;background:{bg};padding:8px;margin:4px;align-items:center">'+"".join(img(d[n],th,84,0.1) for n in ["parcel"]+names)+"".join(img(d[n],th,120,0.1) for n in ["parcel"]+names)+'</div>'
open('/tmp/hdwm/_dev.html','w').write(f'<html><body style="margin:0;background:#fff">{h}</body></html>')
