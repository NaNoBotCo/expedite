"""Share card, 1200x630: the 1897 Milan holy card on the right, night sky and gold type on the left."""
import os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "..", "docs")
W, H = 1200, 630
SUP = "/System/Library/Fonts/Supplemental/"

img = Image.new("RGB", (W, H), "#150b24")
d = ImageDraw.Draw(img)
for y in range(H):  # night gradient
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(58 - 40 * t), int(22 - 14 * t), int(80 - 60 * t)))
random.seed(19)
for _ in range(260):
    x, y, r = random.random() * W, random.random() * H, random.random() * 1.6 + .3
    a = random.randint(120, 255)
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 240, 210, a))
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
g = ImageDraw.Draw(glow)
g.ellipse([700, -60, 1260, 700], fill=(216, 60, 40, 120))
g.ellipse([780, 40, 1180, 600], fill=(245, 200, 110, 90))
img.paste(glow.filter(ImageFilter.GaussianBlur(90)), (0, 0), glow.filter(ImageFilter.GaussianBlur(90)))

card = Image.open(os.path.join(DOCS, "img", "milan-1897.jpg")).convert("RGB")
ch = 540
card = card.resize((int(card.width * ch / card.height), ch), Image.LANCZOS)
cx, cy = 1165 - card.width, (H - ch) // 2
frame = Image.new("RGB", (card.width + 20, ch + 20), "#b3121f")
ImageDraw.Draw(frame).rectangle([4, 4, card.width + 15, ch + 15], outline="#e6b64a", width=3)
img.paste(frame, (cx - 10, cy - 10))
img.paste(card, (cx, cy))

d = ImageDraw.Draw(img)
gold = (245, 210, 122)
title = ImageFont.truetype(SUP + "Didot.ttc", 150)
thai = ImageFont.truetype(SUP + "Tahoma Bold.ttf", 64)
body = ImageFont.truetype(SUP + "Baskerville.ttc", 38)
small = ImageFont.truetype(SUP + "Baskerville.ttc", 28)
d.ellipse([70, 78, 88, 96], fill="#b3121f", outline=gold, width=2)
d.text((104, 70), "SAINT EXPEDITE", font=small, fill=(236, 220, 190))
d.text((64, 120), "HODIE", font=title, fill=gold)
d.text((70, 300), "วันนี้", font=thai, fill=(255, 236, 200))
d.text((70, 408), "His cross says today.", font=body, fill=(251, 236, 208))
d.text((70, 456), "The crow says tomorrow.", font=body, fill=(251, 236, 208))
d.text((70, 560), "nanobotco.github.io/expedite", font=small, fill=(205, 185, 230))
img.save(os.path.join(DOCS, "card.jpg"), quality=88, optimize=True)
print("card.jpg", img.size)
