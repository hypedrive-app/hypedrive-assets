import json
NS=json.load(open('/tmp/hdwm/nucleo_sharp.json')); NF=json.load(open('/tmp/hdwm/nucleo_fill.json'))
G={'creators':['People','People2','People3','Users2','UsersStar','UserHeart'],'home':['House','House2','House5','House6','House8','House9'],
'overview':['HouseDashboard','HouseDashboard2','Gauge','Gauge2','GridLayout','SquareLayoutGrid4'],'box':['Box2','Box3','BoxCart','BagShopping','Gift'],
'grid':['Grid','Grid2','Grid2x2','GridLayout','RectLayoutGrid4'],'payouts':['MoneyTransfer','HandHoldingCoin','MoneyBill','CreditCard','WalletCoin','BankingOnline'],
'campaign':['Bullseye','Rocket','Gift','Tag','Ticket'],'reports':['ChartColumn','ChartColumnTrendUp','ChartLine','ChartBarTrendUp','ChartArea','ChartPie2'],
'pause/live/draft':['MediaPause','HalfDottedCirclePause','Bolt','CirclePlay','MediaPlay','Pen','FilePen','Pencil']}
def s(n): return f'<svg width=28 height=28 viewBox="0 0 24 24">{NS[n]}</svg>'
def f(n): return f'<svg width=28 height=28 viewBox="0 0 18 18" fill="currentColor">{NF[n+"Fill18"]}</svg>' if n+'Fill18' in NF else '<i>—</i>'
rows="".join(f'<h4>{g}</h4><div class=r>'+"".join(f'<div class=c><div>{s(n)}{f(n)}</div><small>{n}</small></div>' for n in ns if n in NS)+'</div>' for g,ns in G.items())
open('/tmp/hdwm/_cand.html','w').write(f'<html><body style="font-family:sans-serif;padding:16px;background:#fff;color:#121417"><style>.r{{display:flex;gap:8px}} .c{{border:1px solid #eee;border-radius:10px;padding:8px;text-align:center;width:130px}} .c div{{display:flex;gap:14px;justify-content:center}} small{{font-size:11px;color:#666}} h4{{margin:10px 0 4px}}</style>{rows}</body></html>')
