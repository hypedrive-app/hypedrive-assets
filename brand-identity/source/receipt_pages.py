import sys; sys.path.insert(0,'/tmp/hdwm')
import isoill as IL, isofam as F
def img(fn,th,size,pad): return f'<img style="width:{size}px;height:{size}px" src="data:image/svg+xml;utf8,{F.square(fn,th,size,pad).replace(chr(35),"%23").replace(chr(34),chr(39))}">'
for th,bg in (("light","#f4f5f8"),("dark","#0f1115")):
    for sz,pad,cols in ((84,0.1,17),(120,0.1,9),(360,0.16,6)):
        cells="".join(f'<div style="margin:6px;width:{sz}px;text-align:center">{img(fn,th,sz,pad)}</div>' for n,fn in IL.ILLS)
        open(f'/tmp/hdwm/receipt/{th}-{sz}.html','w').write(f'<html><body style="margin:0;background:{bg}"><div style="display:flex;flex-wrap:wrap;width:{cols*(sz+12)}px;padding:6px">{cells}</div></body></html>')
