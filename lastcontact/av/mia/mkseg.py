import json,sys; sys.path.insert(0,'/home/claude/av/mia'); from script import LINES
tm=json.load(open('/home/claude/av/mia/timing.json')); V={l[0]:l[4] for l in LINES}
for d in tm: d['vis']=list(V[d['id']])
json.dump(tm,open('/home/claude/av/mweb/timing.json','w'),indent=0)
segs=[];cur=None
for d in tm:
    key=json.dumps(d['vis'][:2] if d['vis'][0] in('3d','card') else d['vis'])
    if cur and cur['key']==key: cur['ids'].append(d['id'])
    else:
        cur={'key':key,'vis':d['vis'],'ids':[d['id']],'start':d['start'] if segs else 0.0}; segs.append(cur)
total=tm[-1]['end']+2.0
for i,s in enumerate(segs): s['end']=segs[i+1]['start'] if i+1<len(segs) else total
json.dump(segs,open('/home/claude/av/mia/segs.json','w'),indent=0)
for s in segs: print(round(s['start'],1),round(s['end']-s['start'],1),s['vis'][:2],s['ids'][0])
