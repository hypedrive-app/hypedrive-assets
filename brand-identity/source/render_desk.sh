#!/bin/bash
# Render one built desktop page: render_desk.sh <n 1-7> <profile> [out.png]
U=~/Downloads/hypedrive-wordmark/BRAND/ui; P=/tmp/hdwm/zt/$2; mkdir -p $P; out=${3:-$P/d$1.png}
timeout 120 ~/.local/share/zen/zen --headless --no-remote --profile $P --screenshot "$out" --window-size=1520,1000 "file://$U/hypedrive-desktop-$1.html" >/dev/null 2>&1; echo "$out"
