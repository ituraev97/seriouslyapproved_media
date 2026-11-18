import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
B = os.path.expanduser('~/.fonts/BarlowC-ExtraBold.ttf'); M = os.path.expanduser('~/.fonts/JBMono-Bold.ttf')
G = (60, 255, 143); A = (255, 176, 32); W = (238, 242, 244); R = (255, 46, 46); N = (7, 11, 16)
f = lambda s, fn=B: ImageFont.truetype(fn, s)
def base(bg, dark=0.55, crop=None):
    im = Image.open(bg).convert('RGB')
    if crop: im = im.crop(crop)
    im = im.resize((1280, 720), Image.LANCZOS)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    ov = Image.new('RGBA', (1280, 720), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for x in range(760):  # left gradient for text
        a = int(255 * dark * (1 - x / 760) ** 1.2); d.line([(x, 0), (x, 720)], fill=(7, 11, 16, a))
    return Image.alpha_composite(im.convert('RGBA'), ov)
def txt(d, xy, s, size, col, fn=B, stroke=4):
    d.text(xy, s, font=f(size, fn), fill=col, stroke_width=stroke, stroke_fill=(0, 0, 0))
def brand(d):
    d.text((44, 650), "LAST", font=f(40), fill=W); d.text((128, 650), "CONTACT", font=f(40), fill=G)
def circle(d, c, r):
    for k in range(7): d.ellipse([c[0] - r - k, c[1] - r - k, c[0] + r + k, c[1] + r + k], outline=R)

# A — contact close-up
im = base('thumb_bgA.jpg', 0.8, (0, 135, 1440, 945)); d = ImageDraw.Draw(im)
txt(d, (44, 40), "MIAMI · NOV 14 · NTSB", 34, A, M, 2)
txt(d, (40, 90), "WINGTIP", 190, W); txt(d, (40, 270), "vs NOSE", 190, G)
brand(d); im.convert('RGB').save('thumbA.jpg', quality=92)

# B — two jets from above
im = base('thumb_bgB.jpg', 0.7); d = ImageDraw.Draw(im)
txt(d, (44, 40), "UPS 767 · COPA 737 · MIAMI", 34, A, M, 2)
txt(d, (40, 92), "TWO JETS.", 170, W); txt(d, (40, 255), "ONE", 170, G); txt(d, (40, 418), "INTERSECTION.", 120, G)
brand(d); im.convert('RGB').save('thumbB.jpg', quality=92)

# C — "give way"
im = base('thumb_bgC.jpg', 0.85); d = ImageDraw.Draw(im)
txt(d, (44, 40), "WHAT THE FAA SAID", 38, A, M, 2)
txt(d, (34, 100), "“GIVE", 220, W); txt(d, (34, 310), "WAY”", 220, G)
txt(d, (44, 560), "UPS 358 · COPA 427 · MIAMI", 34, W, M, 2)
brand(d); im.convert('RGB').save('thumbC.jpg', quality=92)
print('ok')
