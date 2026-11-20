import sys,re,subprocess,os
U=os.path.expanduser('~/Downloads/hypedrive-wordmark/BRAND/ui')
name,theme,out,w=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 1600
src=open(f'{U}/hypedrive-ui-kit{"-dark" if theme=="dark" else ""}.html').read()
def f(m):
    return m.group(0) if f'<h2>{name}</h2>' in m.group(0)[:200] else ''
html=re.sub(r'<section class="sec[^"]*">.*?</section>',f,src,flags=re.S)
html=html.replace('</head>','<style>.hero{display:none!important}</style></head>',1)
tmp=f'{U}/_pb2_tmp.html'
open(tmp,'w').write(html)
subprocess.run([os.path.expanduser('~/.local/share/zen/zen'),'--headless','--no-remote','--profile','/tmp/hdwm/zt/pb2','--screenshot',out,f'--window-size={w},1400',f'file://{tmp}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=120)
os.remove(tmp)
