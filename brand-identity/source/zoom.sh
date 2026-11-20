# usage: zoom.sh name theme px
cd /tmp/hdwm && venv/bin/python -I -c "
import sys; sys.path.insert(0,'/tmp/hdwm')
import isoill as I, isofam as F
fn=dict(I.ILLS)['$1']
open('/tmp/hdwm/_z.html','w').write('<body style=\"margin:0;background:'+('#f4f5f8' if '$2'=='light' else '#0f1115')+'\">'+F.square(fn,'$2',$3,0.08))
" && ~/.local/share/zen/zen --headless --no-remote --profile /tmp/hdwm/zt/prof2 --screenshot /tmp/hdwm/_z_$1.png --window-size=$3,$3 file:///tmp/hdwm/_z.html >/dev/null 2>&1
