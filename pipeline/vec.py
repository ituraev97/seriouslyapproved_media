# usage: vec.py page.png x0 y0 x1 y1 out.svg [blank boxes as x0,y0,x1,y1 ...]  -> potrace outlines as SVG paths (each path animatable)
import sys, io, base64, numpy as np, potrace
from PIL import Image, ImageFilter
src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
im = Image.open(src).convert("L")
for b in sys.argv[7:]:
    bx0, by0, bx1, by1 = map(int, b.split(",")); im.paste(255, (bx0, by0, bx1, by1))
im = im.crop((x0, y0, x1, y1))
S = 0.6
im = im.resize((int(im.width * S), int(im.height * S)), Image.LANCZOS).filter(ImageFilter.MedianFilter(3))
bm = potrace.Bitmap(np.array(im) < 150)
plist = bm.trace(turdsize=6, alphamax=1.0, opticurve=True, opttolerance=0.4)
paths = []
for curve in plist:
    d = [f"M{curve.start_point.x:.1f},{curve.start_point.y:.1f}"]
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        else:
            d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
    xs=[p.x for p in [curve.start_point]+[sg.end_point for sg in curve.segments]]; ys=[p.y for p in [curve.start_point]+[sg.end_point for sg in curve.segments]]
    if max(xs)-min(xs) > im.width*0.85 and max(ys)-min(ys) > im.height*0.85: continue   # scan border / page frame
    paths.append("".join(d) + "Z")
# group: outer contours are drawn in order of position (top-left to bottom-right) so the drawing "travels"
g = np.array(im).astype(np.float32); alpha = np.clip((235 - g) / 150, 0, 1)
rgba = np.zeros((*g.shape, 4), np.uint8); rgba[..., :3] = 27; rgba[..., 3] = (alpha * 255).astype(np.uint8)
buf = io.BytesIO(); Image.fromarray(rgba, "RGBA").save(buf, "PNG", optimize=True); uri = base64.b64encode(buf.getvalue()).decode()
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {im.width} {im.height}" data-w="{im.width}" data-h="{im.height}">' + \
      f'<image class="fill" href="data:image/png;base64,{uri}" x="0" y="0" width="{im.width}" height="{im.height}"/><g class="strokes">' + "".join(f'<path d="{p}"/>' for p in paths) + "</g></svg>"
open(out, "w").write(svg); print(out, len(paths), "paths", im.size)
