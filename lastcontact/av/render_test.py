import asyncio,sys,subprocess,time,os
from playwright.async_api import async_playwright
FPS=30
async def main():
    mode=sys.argv[1]  # 'stills' or 'video'
    import http.server,threading,functools
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self,*a):pass
    srv=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Q,directory='/home/claude/av/web')); threading.Thread(target=srv.serve_forever,daemon=True).start()
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        pg.on('console',lambda m:print('JS:',m.text)); pg.on('pageerror',lambda e:print('ERR:',e))
        await pg.goto('http://127.0.0.1:8765/index.html'); await pg.wait_for_function('window.READY===true',timeout=120000)
        await pg.evaluate('document.fonts.ready')
        dur=await pg.evaluate('window.DUR')
        if mode=='stills':
            ts=[float(x) for x in sys.argv[2].split(',')]
            os.makedirs(os.environ.get('SD','/home/claude/av/stills'),exist_ok=True)
            for t in ts:
                await pg.evaluate(f'renderAt({t})'); await pg.screenshot(path=os.environ.get('SD','/home/claude/av/stills')+f'/s_{t:07.2f}.jpg',type='jpeg',quality=80)
        else:
            out=sys.argv[2]; a=float(sys.argv[3]) if len(sys.argv)>3 else 0; e=float(sys.argv[4]) if len(sys.argv)>4 else dur
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
            n=int((e-a)*FPS); t0=time.time()
            for i in range(n):
                t=a+i/FPS
                await pg.evaluate(f'renderAt({t})')
                ff.stdin.write(await pg.screenshot(type='jpeg',quality=93))
                if i%300==0: print(i,n,round(time.time()-t0),flush=True)
            ff.stdin.close(); ff.wait()
        await b.close()
asyncio.run(main())
