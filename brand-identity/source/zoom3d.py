import sys; sys.path.insert(0,'/tmp/hdwm')
import isoill as IL, isofam as F
name,th,size,ox,oy=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
fn=dict(IL.ILLS)[name]
svg=F.square(fn,th,size,0.1).replace(chr(35),"%23").replace(chr(34),chr(39))
bg="#f4f5f8" if th=="light" else "#0f1115"
open('/tmp/hdwm/_zoom.html','w').write(f'<html><body style="margin:0;background:{bg};overflow:hidden"><img style="position:absolute;left:{-ox}px;top:{-oy}px;width:{size}px" src="data:image/svg+xml;utf8,{svg}"></body></html>')
