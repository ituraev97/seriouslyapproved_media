#!/usr/bin/env python3
"""Build episode video from segs.json. usage: build.py [browser|ffmpeg|concat|all]"""
import asyncio, json, os, subprocess, sys, time, math, functools, http.server, threading
from PIL import Image, ImageDraw, ImageFont, ImageFilter
EP = '/home/claude/av/mia'; WEB = '/home/claude/av/mweb'; OUT = f'{EP}/segs'; os.makedirs(OUT, exist_ok=True)
FPS = 30
SEGS = json.load(open(f'{EP}/segs.json'))
X264 = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS)]
FONT = os.path.expanduser('~/.fonts/JBMono-Bold.ttf')

def nframes(s): return round(s['end'] * FPS) - round(s['start'] * FPS)

def label_png(text, path):
    f = ImageFont.truetype(FONT, 24); W = int(f.getlength(text)) + 44
    im = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x, y = 56, 990
    d.rectangle([x, y, x + W, y + 46], fill=(7, 11, 16, 215)); d.rectangle([x, y, x + 5, y + 46], fill=(60, 255, 143, 255))
    d.text((x + 22, y + 9), text, font=f, fill=(238, 242, 244, 255)); im.save(path)

def build_clip(i, s):
    _, f, st, lab = s['vis']; n = nframes(s); out = f'{OUT}/{i:03d}.mp4'
    if os.path.exists(out): return
    lp = f'{OUT}/lab{i:03d}.png'; label_png(lab, lp)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(st), '-i', f'{EP}/{f}', '-i', lp, '-filter_complex',
                    f'[0:v]fps={FPS},scale=1920:1080,setsar=1,format=yuv420p[v];[v][1:v]overlay=0:0,fade=t=in:st=0:d=0.25', '-frames:v', str(n), '-an'] + X264 + [out], check=True)

def build_photo(i, s):
    _, f, lab = s['vis']; n = nframes(s); out = f'{OUT}/{i:03d}.mp4'
    if os.path.exists(out): return
    src = Image.open(f'{EP}/{f}').convert('RGB')
    if src.height > src.width * 1.2: src = src.rotate(90, expand=True)   # FDR plot is printed sideways
    W, H = 3840, 2160
    bg = src.copy(); r = max(W / bg.width, H / bg.height); bg = bg.resize((int(bg.width * r) + 2, int(bg.height * r) + 2)).crop((0, 0, W, H))
    bg = bg.filter(ImageFilter.GaussianBlur(40)); bg = Image.blend(bg, Image.new('RGB', (W, H), (7, 11, 16)), 0.6)
    r = min(3520 / src.width, 1880 / src.height); fg = src.resize((int(src.width * r), int(src.height * r)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2 - 40)); still = f'{OUT}/still{i:03d}.png'; bg.save(still)
    lp = f'{OUT}/lab{i:03d}.png'; label_png(lab, lp)
    z = f"1+0.05*on/{n}"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', still, '-i', lp, '-filter_complex',
                    f"[0:v]zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps={FPS},format=yuv420p[v];[v][1:v]overlay=0:0,fade=t=in:st=0:d=0.25",
                    '-frames:v', str(n)] + X264 + [out], check=True)

async def browser():
    from playwright.async_api import async_playwright
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8767), functools.partial(Q, directory=WEB)); threading.Thread(target=srv.serve_forever, daemon=True).start()
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        pg.on('pageerror', lambda e: print('ERR:', e, flush=True))
        await pg.goto('http://127.0.0.1:8767/index.html'); await pg.wait_for_function('window.READY===true', timeout=180000)
        await pg.evaluate('document.fonts.ready')
        t0 = time.time()
        for i, s in enumerate(SEGS):
            kind = s['vis'][0]
            if kind not in ('3d', 'card'): continue
            out = f'{OUT}/{i:03d}.mp4'
            if os.path.exists(out): continue
            n = nframes(s); fr = FPS if kind == '3d' else 15
            m = math.ceil(n * fr / FPS)
            tmp = out + '.tmp.mp4'
            vf = ['-vf', f'fps={FPS}'] if fr != FPS else []
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fr), '-c:v', 'mjpeg', '-i', '-'] + vf + ['-frames:v', str(n)] + X264 + [tmp], stdin=subprocess.PIPE)
            for k in range(m):
                t = s['start'] + k / fr
                await pg.evaluate(f'renderAt({t})')
                ff.stdin.write(await pg.screenshot(type='jpeg', quality=92))
            ff.stdin.close(); ff.wait(); os.rename(tmp, out)
            print(f'seg {i} {kind} {s["vis"][1]} {n}f done {round(time.time() - t0)}s', flush=True)
        await b.close()

def concat():
    lst = f'{EP}/concat.txt'
    with open(lst, 'w') as f:
        for i, s in enumerate(SEGS): f.write(f"file '{OUT}/{i:03d}.mp4'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{EP}/video_raw.mp4'], check=True)

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('ffmpeg', 'all'):
        for i, s in enumerate(SEGS):
            if s['vis'][0] == 'clip': build_clip(i, s)
            elif s['vis'][0] == 'photo': build_photo(i, s)
        print('ffmpeg segs done', flush=True)
    if what in ('browser', 'all'): asyncio.run(browser())
    if what in ('concat', 'all'): concat(); print('concat done')
