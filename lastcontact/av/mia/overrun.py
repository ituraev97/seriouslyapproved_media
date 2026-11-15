import sys, json, hashlib, os, subprocess, soundfile as sf
sys.path.insert(0,'/home/claude/av/mia'); from script import LINES
L=sys.argv[1]; D=f'dub/{L}'
import types,re
src=open('dub_build.py').read(); ns={'np':__import__('numpy'),'SR':24000}
exec(src[src.index('def squeeze'):src.index('def synth')],ns); B=types.SimpleNamespace(**ns)
T={d['id']:d for d in json.load(open('timing.json'))}
VL=903.44
txt=[l.rstrip('\n') for l in open(f'{D}/script.txt') if l.strip()]
for i,(lid,*_) in enumerate(LINES):
    k=hashlib.md5(f'{L}|{txt[i]}|1.000'.encode()).hexdigest()[:12]
    f=f'{D}/cache/{k}.wav'
    if not os.path.exists(f): print(i+1,lid,'NOT CACHED'); continue
    import importlib.util
    a,sr=sf.read(f,dtype='float32'); dur=len(B.trim(a))/sr
    nxt=T[LINES[i+1][0]]['start'] if i+1<len(LINES) else VL-0.5
    slot=nxt-T[lid]['start']-0.12
    ex=dur/1.2-slot
    if ex>0.3: print(f"{i+1} {lid} excess {ex:.1f}s cut {100*(1-slot*1.2/dur):.0f}% | {txt[i]}")
