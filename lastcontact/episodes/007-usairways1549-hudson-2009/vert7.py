import sys, os, subprocess, json
from PIL import Image, ImageDraw, ImageFont
B = os.path.expanduser('~/.fonts/BarlowC-ExtraBold.ttf'); M = os.path.expanduser('~/.fonts/JBMono-Bold.ttf')
G = (60, 255, 143, 255); W = (238, 242, 244, 255); A = (255, 176, 32, 255)
SRC = 'master.mp4'
def overlay(path, l1, l2, kick, foot):
    im = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = lambda s, fn=B: ImageFont.truetype(fn, s)
    d.text((60, 250), kick, font=f(30, M), fill=G)
    y = 300
    for line, col in ((l1, W), (l2, G)):
        for part in line.split('\n'):
            d.text((60, y), part, font=f(108), fill=col, stroke_width=3, stroke_fill=(0, 0, 0, 255)); y += 112
    d.text((60, 1370), "LAST", font=f(60), fill=W); d.text((185, 1370), "CONTACT", font=f(60), fill=G)
    d.text((60, 1450), foot, font=f(28, M), fill=(200, 210, 218, 255))
    d.text((60, 1500), "NTSB FINAL REPORT · NTSB/AAR-10/03", font=f(22, M), fill=(126, 138, 150, 255))
    im.save(path)
def endcard(path):
    im = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle([60, 1220, 1020, 1330], fill=(7, 11, 16, 230)); d.rectangle([60, 1220, 70, 1330], fill=G)
    d.text((100, 1240), "FULL STORY ON THE CHANNEL", font=ImageFont.truetype(B, 64), fill=W); im.save(path)
def make(name, a, b, l1, l2, kick, foot, trailer=False):
    ov = f'pub/{name}_ov.png'; overlay(ov, l1, l2, kick, foot)
    dur = b - a
    fc = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.28[bg];"
          "[b]scale=1080:608[fg];[bg][fg]overlay=0:720[v];[v][1:v]overlay=0:0[w]")
    ins = ['-ss', str(a), '-t', str(dur), '-i', SRC, '-i', ov]
    if trailer:
        ec = f'pub/{name}_end.png'; endcard(ec); ins += ['-i', ec]
        fc += f";[w][2:v]overlay=0:0:enable='gte(t,{dur - 2.6:.2f})',format=yuv420p[o]"
    else:
        fc += ";[w]format=yuv420p[o]"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *ins, '-filter_complex', fc, '-map', '[o]', '-map', '0:a',
        '-af', 'afade=t=out:st=%f:d=0.5' % (dur - 0.5), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'aac', '-b:a', '128k', '-r', '30', '-movflags', '+faststart', f'pub/{name}.mp4'], check=True)
    print(name, round(dur, 1))
T = {d['id']: d for d in json.load(open('timing.json'))}
def R(a, b, tail=0.45): return T[a]['start'] - 0.15, T[b]['end'] + tail
K = 'US AIRWAYS 1549 · A320 · HUDSON RIVER · 2009'
FT = 'FULL BREAKDOWN ON THE CHANNEL'; GT = 'FOLLOW FOR THE NEXT FILE'
J = [('lc007-short1', *R('o3', 'o5'), '2,818 FEET.', 'BOTH ENGINES.', K, FT, False),
     ('lc007-short2', *R('s1', 's4'), 'COULD IT MAKE', 'LAGUARDIA?', K, FT, True),
     ('lc007-short3', *R('g1', 'g3'), 'THE GEESE', "WEREN'T LOCAL", K, FT, False),
     ('lc007-short4', *R('k1', 'k3'), 'TESTED: 4 LB.', 'HIT: 8 LB.', K, FT, False),
     ('lc007-tt1', *R('o1', 'h1'), 'FLIGHT 1549:', 'THE FIRST\n3 MINUTES', K, GT, False),
     ('lc007-tt2', *R('b1', 'g2'), 'BIRDS.', 'BOTH ENGINES\nROLL BACK', K, GT, False),
     ('lc007-tt3', *R('r2', 'r9'), 'UNABLE.', 'THE RADIO\nCALLS', K, GT, False),
     ('lc007-tt4', *R('k1', 's5'), 'BACK TO', 'A RUNWAY?', K, GT, False),
     ('lc007-tt5', *R('x1', 'x6'), 'THE FINAL', 'SECONDS', K, GT, False),
     ('lc007-tt6', *R('v3', 'y3'), 'EVERYONE OFF', 'IN 24 MINUTES', K, GT, False)]
only = sys.argv[1:]
os.makedirs('pub', exist_ok=True)
for n, a, b, *r in J:
    if only and n not in only: continue
    make(n, a, b, *r)
