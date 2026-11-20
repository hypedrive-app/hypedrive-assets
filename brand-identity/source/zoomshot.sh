#!/bin/bash
# zoomshot.sh out.png name theme size ox oy
cd /tmp/hdwm && venv/bin/python -I zoom3d.py $2 $3 $4 $5 $6 && ~/.local/share/zen/zen --headless --no-remote --profile /tmp/hdwm/zt/prof6 --screenshot /tmp/hdwm/$1 --window-size=900,700 file:///tmp/hdwm/_zoom.html >/dev/null 2>&1
