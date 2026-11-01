#!/usr/bin/env python3
"""Find figure boxes on a patent drawing page (ink blobs merged by dilation). usage: figboxes.py page.png [dilate=45] [out_preview.jpg]
Prints one box per line: idx x0 y0 x1 y1 (page pixels), skipping the header band; writes a numbered preview."""
import sys, numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd
im = Image.open(sys.argv[1]).convert("L"); a = np.array(im) < 140
H, W = a.shape; a[: int(H * 0.085)] = False          # header: "U.S. Patent  date  Sheet x of y  number"
r = int(sys.argv[2]) if len(sys.argv) > 2 else 45
d = nd.binary_dilation(a[::3, ::3], iterations=max(1, r // 3)); lab, n = nd.label(d)
boxes = []
for k, sl in enumerate(nd.find_objects(lab), 1):
    y0, y1 = sl[0].start * 3, sl[0].stop * 3; x0, x1 = sl[1].start * 3, sl[1].stop * 3
    if (x1 - x0) * (y1 - y0) > 0.012 * W * H: boxes.append((x0, y0, min(W, x1), min(H, y1)))
boxes.sort(key=lambda b: (b[1] // 300, b[0]))
pv = im.convert("RGB"); dr = ImageDraw.Draw(pv)
for i, (x0, y0, x1, y1) in enumerate(boxes):
    print(i, x0, y0, x1, y1); dr.rectangle([x0, y0, x1, y1], outline=(255, 0, 0), width=8); dr.text((x0 + 10, y0 + 10), str(i), fill=(255, 0, 0))
if len(sys.argv) > 3: pv.resize((W // 4, H // 4)).save(sys.argv[3])
