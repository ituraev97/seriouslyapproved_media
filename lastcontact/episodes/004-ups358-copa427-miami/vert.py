import sys,os,subprocess
from PIL import Image,ImageDraw,ImageFont
B=os.path.expanduser('~/.fonts/BarlowC-ExtraBold.ttf'); M=os.path.expanduser('~/.fonts/JBMono-Bold.ttf')
G=(60,255,143,255); A=(255,176,32,255); W=(238,242,244,255)
SRC='master.mp4'
def overlay(path,l1,l2,kick,foot):
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=lambda s,fn=B:ImageFont.truetype(fn,s)
    d.text((60,250),kick,font=f(30,M),fill=G)
    y=300
    for line,col in ((l1,W),(l2,G)):
        for part in line.split('\n'):
            d.text((60,y),part,font=f(104),fill=col,stroke_width=3,stroke_fill=(0,0,0,255)); y+=108
    d.text((60,1370),"LAST",font=f(60),fill=W); d.text((185,1370),"CONTACT",font=f(60),fill=G)
    d.text((60,1450),foot,font=f(28,M),fill=(200,210,218,255))
    d.text((60,1500),"FAA / NTSB STATEMENTS · NO CAUSE DETERMINED",font=f(22,M),fill=(126,138,150,255))
    im.save(path)
def make(name,a,b,l1,l2,kick,foot):
    ov=f'pub/{name}_ov.png'; overlay(ov,l1,l2,kick,foot)
    fc=("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.28[bg];"
        "[b]scale=1080:608[fg];[bg][fg]overlay=0:720[v];[v][1:v]overlay=0:0,format=yuv420p[o]")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(a),'-t',str(b-a),'-i',SRC,'-i',ov,'-filter_complex',fc,'-map','[o]','-map','0:a',
        '-af','afade=t=out:st=%f:d=0.5'%(b-a-0.5),'-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','128k','-r','30','-movflags','+faststart',f'pub/{name}.mp4'],check=True)
    print(name, round(b-a,1))
import json; T={d['id']:d for d in json.load(open('timing.json'))}
def R(a,b): return T[a]['start']-0.15, T[b]['end']+0.45
K='MIAMI INTL · NOV 14, 2026'
FT='FULL BREAKDOWN ON THE CHANNEL'; GT='FOLLOW FOR THE NEXT FILE'
J=[('lc004-short1',*R('o2','o5'),'COPA WINGLET,','UPS NOSE:\nPER THE NTSB',K,FT),
   ('lc004-short2',*R('d2','d4'),'WHY THE NTSB','IS\nINVESTIGATING',K,FT),
   ('lc004-short3',*R('t3','t5'),'"GIVE WAY":','WHAT IT\nMEANS',K,FT),
   ('lc004-short4',*R('w6','w8'),'WINGTIP COLLISIONS:','THE NTSB\nIN 2012','BACKGROUND · NOT A FINDING',FT),
   ('lc004-short5',*R('x2','x4'),'THE SEQUENCE,','PER THE\nFAA + NTSB',K,FT),
   ('lc004-short6',*R('q2','q7'),'MIAMI COLLISION:','THE OPEN\nQUESTIONS',K,FT),
   ('lc004-tt1',*R('o1','o8'),'TWO JETS.','ONE\nINTERSECTION.',K,GT),
   ('lc004-tt2',*R('s2','s7'),'THE STATEMENTS,','WORD BY\nWORD',K,GT),
   ('lc004-tt3',*R('t1','t7'),'"GIVE WAY"','+ THE TAXI\nRULES',K,GT),
   ('lc004-tt4',*R('a1','a6'),'MIAMI INTL','+ ASDE-X',K,GT),
   ('lc004-tt5',*R('w2','w8'),'12 WINGTIP','ACCIDENTS\nIN TAXI','NTSB LETTER, 2012 · BACKGROUND',GT),
   ('lc004-tt6',*R('q1','n4'),"WHAT WE STILL","DON'T KNOW",K,GT)]
only=sys.argv[1:]
for n,a,b,*r in J:
    if only and n not in only: continue
    make(n,a,b,*r)
