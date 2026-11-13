"""Die-cut sticker for loud thumbnails: transparent line-art PNG -> PNG with a solid white silhouette,
thick white border and thin black outline around the whole object (not around every line).
usage: python3 sticker.py in.png out.png [border_px=22]"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd

src, dst = sys.argv[1], sys.argv[2]
border = int(sys.argv[3]) if len(sys.argv) > 3 else 22
im = Image.open(src).convert("RGBA")
# work on a padded canvas so the border never gets clipped
pad = border * 3
W, H = im.size
canvas = Image.new("RGBA", (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0)); canvas.paste(im, (pad, pad), im)
a = np.array(canvas)[:, :, 3] > 40
# silhouette: close gaps between strokes, fill enclosed areas, keep the biggest blobs
sil = nd.binary_closing(a, structure=np.ones((3, 3)), iterations=max(6, min(W, H) // 60))
sil = nd.binary_fill_holes(sil)
lab, n = nd.label(sil)
if n > 1:
    sizes = nd.sum(sil, lab, range(1, n + 1)); keep = [i + 1 for i, s in enumerate(sizes) if s > 0.02 * sizes.max()]
    sil = np.isin(lab, keep)
white = nd.binary_dilation(sil, iterations=border)
outline = nd.binary_dilation(white, iterations=4) & ~white
out = np.zeros(white.shape + (4,), np.uint8)
out[white] = (255, 255, 255, 255)
out[outline] = (13, 13, 13, 255)
base = Image.fromarray(out).filter(ImageFilter.SMOOTH_MORE)
base.alpha_composite(canvas)
bb = base.getbbox(); base.crop(bb).save(dst)
print("sticker", dst, base.crop(bb).size)
