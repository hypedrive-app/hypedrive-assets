cd /tmp/hdwm; venv/bin/python -I kit_build.py > build_pb2.log 2>&1 || { tail -5 build_pb2.log; exit 1; }
for s in "Empty states & tables:empty" "Charts:charts" "Shell & sidebar:shell" "More components:more" "Interaction:inter"; do n=${s%%:*}; k=${s##*:}; for t in light dark; do venv/bin/python -I iso_pb2.py "$n" $t /tmp/hdwm/pb2out/$1_${k}_$t.png 1600; done; done
