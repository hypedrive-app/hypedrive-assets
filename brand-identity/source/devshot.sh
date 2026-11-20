#!/bin/bash
# devshot.sh out.png names...
out=$1; shift
cd /tmp/hdwm && venv/bin/python -I dev.py x "$@" && ~/.local/share/zen/zen --headless --no-remote --profile /tmp/hdwm/zt/prof6 --screenshot /tmp/hdwm/$out --window-size=${W:-1000},${H:-1000} file:///tmp/hdwm/_dev.html >/dev/null 2>&1; ls -la /tmp/hdwm/$out
