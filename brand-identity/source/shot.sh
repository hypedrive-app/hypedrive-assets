#!/bin/bash
# usage: shot.sh name  -> renders _ills.html and screenshot _ills3d_<name>.png
cd /tmp/hdwm && venv/bin/python -I isoill.py && mkdir -p zt/prof6 && ~/.local/share/zen/zen --headless --no-remote --profile /tmp/hdwm/zt/prof6 --screenshot /tmp/hdwm/_ills3d_$1.png --window-size=1500,2300 file:///tmp/hdwm/_ills.html >/dev/null 2>&1
ls -la /tmp/hdwm/_ills3d_$1.png
