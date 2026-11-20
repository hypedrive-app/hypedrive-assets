#!/bin/bash
# dx.sh N OUT [H]
U=~/Downloads/hypedrive-wordmark/BRAND/ui
timeout 90 ~/.local/share/zen/zen --headless --no-remote --profile /tmp/pq2 --screenshot $2 --window-size=1520,${3:-2200} file://$U/hypedrive-desktop-$1.html >/dev/null 2>&1
