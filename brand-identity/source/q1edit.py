import sys
p='/tmp/hdwm/kit_build.py'
s=open(p).read()
pairs=eval(open(sys.argv[1]).read())
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:70])
    s=s.replace(a,b)
open(p,'w').write(s)
print('ok')
