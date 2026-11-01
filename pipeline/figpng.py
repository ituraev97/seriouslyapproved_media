#!/usr/bin/env python3
"""Crop a patent page to a transparent ink PNG (for thumbnails). usage: figpng.py page.png x0 y0 x1 y1 out.png [blank x0,y0,x1,y1 ...]"""
import sys, numpy as np
from PIL import Image
im = Image.open(sys.argv[1]).convert("L")
for b in sys.argv[7:]: im.paste(255, tuple(map(int, b.split(","))))
im = im.crop(tuple(map(int, sys.argv[2:6]))); g = np.array(im).astype(np.float32); a = np.clip((235 - g) / 150, 0, 1)
rgba = np.zeros((*g.shape, 4), np.uint8); rgba[..., :3] = 27; rgba[..., 3] = (a * 255).astype(np.uint8); Image.fromarray(rgba).save(sys.argv[6])
