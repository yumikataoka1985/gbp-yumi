#!/usr/bin/env python3
"""Render do reel depoimento Cristina (estilo Lousa Viva, modo depoimento)."""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

B = sys.argv[1]            # pasta dos brutos
OUT = sys.argv[2]          # pasta de saida
os.makedirs(OUT, exist_ok=True)
FPS = 30
W, H = 1080, 960
GOLD = (232, 181, 74); RED = (229, 72, 77); WHITE = (255, 255, 255); DARK = (16, 22, 22)
FD = "/usr/share/fonts/opentype/inter/"
def F(w, s): return ImageFont.truetype(FD + {"x": "Inter-ExtraBold.otf", "k": "Inter-Black.otf", "b": "Inter-Bold.otf", "m": "Inter-Medium.otf"}[w], s)

# ---------------------------------------------------------------- segmentos
# src, a, b, rosto, zoom, cena
SEGS = [
    ("C0139", 316.55, 319.10, "bottom", 1.00, "A"),
    ("C0004", 2.15, 2.78, "bottom", 1.12, "B"),
    ("C0004", 3.98, 5.05, "bottom", 1.00, "B"),
    ("C0004", 5.15, 7.70, "top", 1.00, "C1"),
    ("C0004", 8.38, 10.30, "top", 1.12, "C1"),
    ("C0004", 13.12, 14.62, "top", 1.00, "C2"),
    ("C0004", 15.50, 19.50, "top", 1.12, "C2"),
    ("C0139", 302.12, 304.80, "bottom", 1.00, "D"),
    ("C0139", 304.86, 307.70, "bottom", 1.12, "D"),
    ("C0139", 308.20, 313.80, "top", 1.00, "E"),
    ("C0139", 313.80, 316.18, "top", 1.12, "E"),
    ("C0139", 320.56, 324.95, "bottom", 1.00, "F1"),
    ("C0139", 325.05, 328.52, "bottom", 1.12, "F2"),
    ("C0139", 338.62, 343.98, "top", 1.00, "G"),
    ("C0139", 349.10, 356.00, "bottom", 1.00, "H"),
    ("C0139", 719.58, 722.00, "top", 1.00, "I"),
    ("C0139", 316.55, 317.72, "bottom", 1.12, "A2"),
]
starts = []; t = 0.0
for s in SEGS:
    starts.append(t); t += s[2] - s[1]
TOTAL = t
def out_t(i, src_t): return starts[i] + (src_t - SEGS[i][1])
def seg_at(tt):
    for i in range(len(SEGS) - 1, -1, -1):
        if tt >= starts[i]: return i
    return 0

# ---------------------------------------------------------------- elementos
def rr(d, box, r, fill, outline=None, width=0): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)
def text_w(font, txt): return font.getbbox(txt)[2] - font.getbbox(txt)[0]

def icon_check(size, color=GOLD):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, size - 1, size - 1), fill=color)
    w = max(6, size // 9)
    d.line([(size * .27, size * .52), (size * .44, size * .69), (size * .75, size * .33)], fill=DARK, width=w, joint="curve")
    return im
def icon_x(size, color=RED):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, size - 1, size - 1), fill=color)
    w = max(6, size // 9); a, b = size * .32, size * .68
    d.line([(a, a), (b, b)], fill=WHITE, width=w); d.line([(a, b), (b, a)], fill=WHITE, width=w)
    return im
def icon_star(size, color=GOLD):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, size - 1, size - 1), fill=color)
    c = size / 2; pts = []
    for k in range(10):
        r = size * (.33 if k % 2 == 0 else .14); ang = -math.pi / 2 + k * math.pi / 5
        pts.append((c + r * math.cos(ang), c + r * math.sin(ang)))
    d.polygon(pts, fill=DARK); return im
def icon_box(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (4, 4, size - 5, size - 5), 14, None, (255, 255, 255, 200), 6); return im

def card(txt, icon=None, fs=54, color=WHITE, minw=0):
    f = F("x", fs); tw = text_w(f, txt); ic = 78
    w = max(minw, tw + 80 + (ic + 26 if icon else 0)); h = 128
    im = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (10, 16, w + 10, h + 16), 40, (0, 0, 0, 90))
    rr(d, (10, 10, w + 10, h + 10), 40, (12, 30, 30, 225), (255, 255, 255, 70), 3)
    x = 50
    if icon:
        icim = {"ok": icon_check, "bad": icon_x, "star": icon_star, "box": icon_box}[icon](ic)
        im.alpha_composite(icim, (x - 4, 10 + (h - ic) // 2)); x += ic + 22
    d.text((x, 10 + h / 2), txt, font=f, fill=color, anchor="lm")
    return im
def pill(txt, gold=True, fs=48):
    f = F("k", fs); tw = text_w(f, txt); w, h = tw + 80, int(fs * 1.9)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if gold: rr(d, (0, 0, w - 1, h - 1), h // 2, GOLD); d.text((w / 2, h / 2), txt, font=f, fill=DARK, anchor="mm")
    else:
        rr(d, (0, 0, w - 1, h - 1), h // 2, (255, 255, 255, 34), (255, 255, 255, 90), 2)
        d.text((w / 2, h / 2), txt, font=f, fill=WHITE, anchor="mm")
    return im
def stamp(txt, color):
    f = F("k", 104); tw = text_w(f, txt); w, h = tw + 80, 160
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (6, 6, w - 7, h - 7), 22, None, color, 10)
    d.text((w / 2, h / 2 + 4), txt, font=f, fill=color, anchor="mm")
    return im.rotate(-7, expand=True, resample=Image.BICUBIC)
def polaroid(photo, name):
    pw = 360; im = Image.new("RGBA", (pw + 40, pw + 130), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (0, 0, pw + 39, pw + 129), 10, (250, 247, 240))
    im.paste(photo.resize((pw, pw)), (20, 20))
    d.text(((pw + 40) / 2, pw + 75), name, font=F("k", 52), fill=DARK, anchor="mm")
    return im.rotate(4, expand=True, resample=Image.BICUBIC)
def body_fig(highlight=False):
    w, h = 300, 520; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = (255, 255, 255, 210); lw = 26
    d.ellipse((110, 10, 190, 90), fill=c)
    d.line([(150, 110), (150, 300)], fill=c, width=lw + 14)
    d.line([(150, 130), (70, 260)], fill=c, width=lw); d.line([(150, 130), (230, 260)], fill=c, width=lw)
    d.line([(150, 295), (100, 500)], fill=c, width=lw); d.line([(150, 295), (200, 500)], fill=c, width=lw)
    if highlight:  # lado direito dela = esquerda de quem olha
        g = Image.new("RGBA", (w, h), (0, 0, 0, 0)); gd = ImageDraw.Draw(g)
        gd.line([(150, 130), (70, 260)], fill=RED + (255,), width=lw + 6)
        gd.line([(140, 120), (140, 300)], fill=RED + (255,), width=18)
        gd.line([(150, 295), (100, 500)], fill=RED + (255,), width=lw + 6)
        glow = g.filter(ImageFilter.GaussianBlur(14)); im.alpha_composite(glow); im.alpha_composite(g)
    return im
def calendar_base():
    cols, rows, s, gap = 7, 2, 96, 14
    w = cols * s + (cols - 1) * gap; h = rows * s + (rows - 1) * gap + 70
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.text((0, 20), "DIAS TENTANDO", font=F("k", 40), fill=(255, 255, 255, 200), anchor="lm")
    for r in range(rows):
        for c in range(cols):
            x = c * (s + gap); y = 70 + r * (s + gap)
            rr(d, (x, y, x + s, y + s), 18, (12, 30, 30, 225), (255, 255, 255, 70), 3)
    return im, s, gap
def cell_pos(idx, s=96, gap=14, ox=0, oy=0):
    r, c = divmod(idx, 7); return ox + c * (s + gap) + s / 2, oy + 70 + r * (s + gap) + s / 2
def xmark(size=64):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line([(8, 8), (size - 8, size - 8)], fill=RED, width=12); d.line([(8, size - 8), (size - 8, 8)], fill=RED, width=12)
    return im
def gold_ring(size=120):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((5, 5, size - 6, size - 6), outline=GOLD, width=10); return im
def people_icon():
    w, h = 300, 130; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for k, x in enumerate((50, 150, 250)):
        col = GOLD if k == 1 else (255, 255, 255, 220)
        d.ellipse((x - 26, 6, x + 26, 58), fill=col); d.pieslice((x - 48, 66, x + 48, 162), 180, 360, fill=col)
    return im
def arrow_down():
    im = Image.new("RGBA", (80, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line([(40, 0), (40, 70)], fill=GOLD, width=14); d.polygon([(10, 62), (70, 62), (40, 108)], fill=GOLD); return im
def profile_card(avatar):
    w, h = 820, 330; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (0, 0, w - 1, h - 1), 44, (12, 30, 30, 235), (255, 255, 255, 80), 3)
    av = avatar.resize((190, 190)); m = Image.new("L", (190, 190), 0); ImageDraw.Draw(m).ellipse((0, 0, 189, 189), fill=255)
    im.paste(av, (40, 40), m); d.ellipse((36, 36, 234, 234), outline=GOLD, width=6)
    d.text((270, 95), "@yumikataoka", font=F("k", 52), fill=WHITE, anchor="lm")
    d.text((270, 160), "Thai Massage · Formação", font=F("m", 36), fill=(255, 255, 255, 200), anchor="lm")
    d.text((270, 210), "para terapeutas", font=F("m", 36), fill=(255, 255, 255, 200), anchor="lm")
    return im
def button(txt):
    f = F("k", 50); w = text_w(f, txt) + 110; h = 112
    im = Image.new("RGBA", (w, h + 10), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, (0, 10, w - 1, h + 9), 30, (120, 85, 20)); rr(d, (0, 0, w - 1, h - 1), 30, GOLD)
    d.text((w / 2, h / 2), txt, font=f, fill=DARK, anchor="mm"); return im
def pointer():
    im = Image.new("RGBA", (110, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(10, 10), (95, 50), (58, 60), (78, 100), (62, 106), (44, 68), (14, 92)], fill=WHITE, outline=DARK)
    return im

# fotos para polaroide e avatar
def grab(src, ts, box):
    p = f"{OUT}/grab_{src}_{ts}.png"
    if not os.path.exists(p):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(ts), "-i", f"{B}/{src}.MP4", "-frames:v", "1", p], check=True)
    return Image.open(p).convert("RGB").crop(box)
cris_photo = grab("C0004", 2.4, (2150, 280, 3350, 1480))
yumi_photo = Image.open('/tmp/claude-0/-home-user-gbp-yumi/db5fc9d1-fbee-574a-b915-3b517045ddce/scratchpad/fotos/avatar.png').convert('RGB')

# ---------------------------------------------------------------- cenas
# (cena, seg_idx, src_t, elemento_img, cx, cy, anim, som)
EV = []
def ev(scene, i, st, img, cx, cy, anim="pop", snd="pop"): EV.append(dict(scene=scene, t=out_t(i, st), img=img, cx=cx, cy=cy, anim=anim, snd=snd))
CX = 470
for sc, i, base in (("A", 0, 316.55), ("A2", 16, 316.55)):
    ev(sc, i, base, pill("Workshop de Thai Massage", gold=False, fs=34), CX, 170, "slide", "whoosh")
    ev(sc, i, base + 0.05, stamp("DEPOIS", GOLD), CX, 330, "stamp", "stamp")
    if sc == "A":
        ev(sc, i, 317.68, card("COM DOR", "bad", minw=430), CX, 520, "slide", "whoosh")
        ev(sc, i, 318.60, card("SEM DOR", "ok", color=GOLD, minw=430), CX, 670, "pop", "ding")
ev("B", 1, 2.15, polaroid(cris_photo, "Cristina"), 290, 440, "slide", "whoosh")
ev("B", 2, 4.22, pill("MASSOTERAPEUTA", fs=40), 770, 380, "pop", "pop")
ev("B", 2, 4.60, pill("aluna do workshop", gold=False, fs=34), 770, 500, "slide", "whoosh")
ev("C1", 3, 5.15, stamp("ANTES", RED), CX, 250, "stamp", "stamp")
ev("C1", 3, 5.98, pill("Qual a expectativa?", gold=False, fs=40), CX, 440, "slide", "whoosh")
ev("C1", 4, 9.12, card("GRANDES EXPECTATIVAS", "star"), CX, 610, "pop", "ding")
ev("C2", 5, 13.12, stamp("ANTES", RED), 760, 190, "stamp", "stamp")
ev("C2", 5, 13.94, pill("Quero aprender", gold=False, fs=40), 330, 190, "slide", "whoosh")
ev("C2", 6, 16.02, card("Várias coisas", "box", minw=560), CX, 360, "slide", "pop")
ev("C2", 6, 17.94, card("Mobilidade", "box", minw=560), CX, 510, "slide", "pop")
ev("C2", 6, 18.90, card("Alívio de dor", "box", color=GOLD, minw=560), CX, 660, "slide", "pop")
ev("D", 7, 302.12, stamp("DEPOIS", GOLD), 720, 210, "stamp", "stamp")
ev("D", 7, 303.80, pill("EM ÊXTASE"), 720, 390, "pop", "pop")
ev("D", 8, 304.86, body_fig(False), 250, 480, "slide", "whoosh")
ev("D", 8, 306.08, body_fig(True), 250, 480, "fade", "pop")
ev("D", 8, 306.30, card("encurtamento", "bad", fs=46), 720, 540, "pop", "whoosh")
ev("D", 8, 307.02, pill("lado direito", gold=False, fs=40), 720, 680, "slide", "pop")
cal, cs, cg = calendar_base(); cal_ox, cal_oy = 540 - cal.width / 2, 120
ev("E", 9, 308.20, cal, 540, cal_oy + cal.height / 2, "slide", "whoosh")
for k, st in enumerate((308.8, 309.3, 309.8, 310.3, 310.8, 311.3, 311.9, 312.5, 313.1)):
    x, y = cell_pos(k, cs, cg, cal_ox, cal_oy); ev("E", 9, st, xmark(), x, y, "pop", "tick")
ev("E", 9, 310.74, pill("várias alternativas", gold=False, fs=40), 540, 545, "slide", "whoosh")
x, y = cell_pos(9, cs, cg, cal_ox, cal_oy)
ev("E", 10, 314.08, gold_ring(), x, y, "pop", "pop")
ev("E", 10, 314.20, pill("HOJE", fs=34), x, y + 95, "pop", "pop")
ev("E", 10, 315.64, card("SEM DOR", "ok", fs=64, color=GOLD, minw=520), 540, 660, "pop", "ding")
# F1: barra de expectativa (desenho dinamico) + pilula
ev("F1", 11, 324.32, pill("SUPER ACIMA", fs=56), 470, 220, "pop", "ding")
ev("F2", 12, 325.05, pill("Vim buscar", gold=False, fs=40), CX, 200, "slide", "whoosh")
ev("F2", 12, 325.30, card("Alívio da dor", "box", color=GOLD, minw=600), CX, 380, "slide", "pop")
ev("F2", 12, 327.60, icon_check(78), CX - 225, 380, "pop", "ding")
ev("G", 13, 339.88, pill("MENTE EM SILÊNCIO"), 470, 500, "pop", "pop")
ev("G", 13, 341.62, card("recebendo", "ok", fs=46, minw=380), 280, 660, "slide", "ding")
ev("G", 13, 342.62, card("fazendo", "ok", fs=46, minw=380), 690, 660, "slide", "ding")
ev("H", 14, 350.54, pill("APROFUNDAR"), CX, 170, "pop", "pop")
ev("H", 14, 352.32, card("experiência", "ok", fs=46, minw=460), CX, 300, "slide", "whoosh")
ev("H", 14, 354.28, card("conhecimento", "ok", fs=46, minw=460), CX, 430, "slide", "whoosh")
ev("H", 14, 354.90, arrow_down(), CX, 545, "slide", "pop")
ev("H", 14, 355.08, people_icon(), CX, 650, "pop", "ding")
ev("H", 14, 355.30, pill("minhas clientes", gold=False, fs=38), CX, 765, "slide", "pop")
ev("I", 15, 719.58, profile_card(yumi_photo), 500, 270, "slide", "whoosh")
ev("I", 15, 720.08, button("PRÓXIMA TURMA"), 500, 520, "pop", "click")
ev("I", 15, 720.50, pointer(), 760, 580, "slide", "click")
ev("I", 15, 721.30, pill("link na bio", gold=False, fs=40), 500, 690, "slide", "pop")
SC_START = {}
for i, s in enumerate(SEGS):
    SC_START.setdefault(s[5], starts[i])

# ---------------------------------------------------------------- fundo
bg = Image.new("RGB", (W, H)); bd = ImageDraw.Draw(bg)
for y in range(H):
    k = y / H; c1, c2 = (14, 60, 58), (5, 30, 32)
    bd.line([(0, y), (W, y)], fill=tuple(int(c1[j] * (1 - k) + c2[j] * k) for j in range(3)))
vig = Image.new("L", (W, H), 0); ImageDraw.Draw(vig).ellipse((-300, -200, W + 300, H + 200), fill=255)
vig = vig.filter(ImageFilter.GaussianBlur(120))
bg = Image.composite(bg, Image.new("RGB", (W, H), (3, 18, 20)), vig).convert("RGBA")
dots = Image.new("RGBA", (W + 48, H + 48), (0, 0, 0, 0)); dd = ImageDraw.Draw(dots)
for yy in range(0, H + 48, 48):
    for xx in range(0, W + 48, 48): dd.ellipse((xx - 2, yy - 2, xx + 2, yy + 2), fill=(255, 255, 255, 26))

def ease_back(p):
    c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2
def place(frame, e, tt):
    p = (tt - e["t"]) / 0.28
    if p < 0: return
    p = min(1, p); img = e["img"]; a = 1.0; dy = 0; sc = 1.0
    if e["anim"] == "pop": sc = 0.55 + 0.45 * ease_back(p); a = min(1, p * 2.5)
    elif e["anim"] == "slide": dy = (1 - (1 - (1 - p) ** 3)) * 70; a = min(1, p * 2)
    elif e["anim"] == "stamp": sc = 1.9 - 0.9 * (1 - (1 - p) ** 3); a = min(1, p * 2)
    elif e["anim"] == "fade": a = p
    else: pass
    # respiracao sutil do ultimo elemento
    if sc != 1.0:
        img = img.resize((max(1, int(img.width * sc)), max(1, int(img.height * sc))), Image.BICUBIC)
    if a < 1:
        al = img.getchannel("A").point(lambda v: int(v * a)); img = img.copy(); img.putalpha(al)
    frame.alpha_composite(img, (int(e["cx"] - img.width / 2), int(e["cy"] - img.height / 2 + dy)))

def draw_bar(frame, tt):
    i = 11; t0, t1 = out_t(i, 320.60), out_t(i, 324.30)
    p = max(0, min(1, (tt - t0) / (t1 - t0))); p = 1 - (1 - p) ** 2
    d = ImageDraw.Draw(frame); x0, x1, y0, y1 = 120, 860, 400, 520
    d.text((x0, y0 - 40), "MINHA EXPECTATIVA", font=F("k", 36), fill=WHITE, anchor="ls")
    rr(d, (x0, y0, x1, y1), 40, (12, 30, 30, 225), (255, 255, 255, 70), 3)
    fx = x0 + 8 + (x1 - x0 - 16) * 0.97 * p
    if fx > x0 + 50: rr(d, (x0 + 8, y0 + 8, fx, y1 - 8), 32, GOLD)
    lx = x0 + (x1 - x0) * 0.6
    for yy in range(y0 - 30, y1 + 50, 22): d.line([(lx, yy), (lx, yy + 12)], fill=WHITE, width=5)
    d.text((lx, y1 + 80), "o que eu esperava", font=F("b", 32), fill=(255, 255, 255, 220), anchor="mm")
def draw_mind(frame, tt):
    i = 13; t0 = out_t(i, 338.62); t1 = out_t(i, 341.26)
    calm = max(0, min(1, (tt - t0) / (t1 - t0)))
    d = ImageDraw.Draw(frame); cx, cy = 470, 260
    d.ellipse((cx - 80, cy - 80, cx + 80, cy + 80), fill=(255, 255, 255, 230))
    for k in range(1, 5):
        amp = (1 - calm) * 22; r = 80 + k * 38
        pts = []
        for j in range(73):
            ang = j / 72 * 2 * math.pi
            rr_ = r + amp * math.sin(ang * (5 + k) + tt * 9 + k)
            pts.append((cx + rr_ * math.cos(ang), cy + rr_ * math.sin(ang)))
        col = GOLD if calm >= 1 else (255, 255, 255)
        d.line(pts, fill=col + (int(150 - k * 25),), width=5)

def lousa(tt):
    i = seg_at(tt); sc = SEGS[i][5]
    off = int(tt * 10) % 48
    fr = bg.copy(); fr.alpha_composite(dots.crop((off, off, off + W, off + H)))
    if sc == "F1": draw_bar(fr, tt)
    if sc == "G": draw_mind(fr, tt)
    for e in EV:
        if e["scene"] == sc and e["t"] <= tt + 1e-6: place(fr, e, tt)
    return fr.convert("RGB")

def render_lousa():
    p = f"{OUT}/lousa.mp4"
    n = int(round(TOTAL * FPS))
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                           "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", p], stdin=subprocess.PIPE)
    for k in range(n): ff.stdin.write(lousa(k / FPS).tobytes())
    ff.stdin.close(); ff.wait()

# ---------------------------------------------------------------- rosto (video + audio)
def crop_for(src, z):
    if src == "C0004": cx, w = 2200, 2430
    else: cx, w = 2080, 2000
    w = int(w / z); h = int(w / 1.125); x = int(cx - w / 2); y = int((2160 - h) * (0.35 if src == "C0004" else 0.0))
    return f"crop={w}:{h}:{x}:{y},scale={W}:{H}:flags=lanczos,setsar=1,fps={FPS}"
def render_face():
    parts = []
    for i, (src, a, b, pos, z, sc) in enumerate(SEGS):
        p = f"{OUT}/seg{i:02d}.mp4"; d = b - a
        if not os.path.exists(p):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", f"{B}/{src}.MP4", "-t", f"{d:.3f}",
                            "-vf", crop_for(src, z) + ",eq=contrast=1.06:saturation=1.08:brightness=0.01",
                            "-af", f"afade=t=in:d=0.03,afade=t=out:st={d-0.04:.3f}:d=0.04,aresample=48000",
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", "-ac", "1", p.replace(".mp4", ".mov")], check=True)
            os.rename(p.replace(".mp4", ".mov"), p)
        parts.append(p)
    lst = f"{OUT}/concat.txt"; open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "copy", "-c:a", "pcm_s16le", f"{OUT}/face.mov"], check=True)

# ---------------------------------------------------------------- legendas
KEY = {"dor", "dor.", "sem", "êxtase", "encurtamento", "alongamento", "acima", "alívio", "mobilidade", "expectativas",
       "expectativa", "silenciar", "mente", "clientes", "aprofundar", "massoterapeuta", "cristina", "convite", "próximos",
       "grupos", "thai", "massage", "hoje", "direito", "dias", "alternativas"}
def ass_time(x):
    cs = int(round(x * 100)); return f"{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}"
def build_ass():
    words = {}
    for src in ("C0004", "C0139"):
        r = json.load(open(f"{B}/{src}.json"))
        words[src] = [w for s in r["segments"] for w in s.get("words", [])]
    fix = {"Tô": "TÔ", "tô": "TÔ"}
    ev_ = []
    for i, (src, a, b, pos, z, sc) in enumerate(SEGS):
        ws = [w for w in words[src] if w["start"] >= a - 0.05 and w["start"] < b - 0.05]
        chunk = []
        def flush():
            if not chunk: return
            t0 = out_t(i, max(a, chunk[0]["start"])); t1 = out_t(i, min(b, chunk[-1]["end"] + 0.12))
            parts = []
            for w in chunk:
                raw = w["word"].strip(); base = raw.strip(",.?!…").lower()
                txt = raw.strip(",.…").upper().replace("?", "?")
                if base in KEY: parts.append("{\\c&H4AB5E8&}" + txt + "{\\c&HFFFFFF&}")
                else: parts.append(txt)
            ev_.append([t0, t1, " ".join(parts)]); chunk.clear()
        for w in ws:
            chunk.append(w); raw = w["word"].strip()
            if len(chunk) >= 3 or raw[-1:] in ",.?!" or len("".join(x["word"] for x in chunk)) > 16: flush()
        flush()
    ev_.sort()
    for k in range(len(ev_) - 1):  # sem buracos curtos, sem sobreposicao
        if ev_[k + 1][0] - ev_[k][1] < 0.25: ev_[k][1] = ev_[k + 1][0]
        ev_[k][1] = min(ev_[k][1], ev_[k + 1][0])
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Leg,Inter ExtraBold,82,&H00FFFFFF,&H00FFFFFF,&H80000000,&H96000000,0,0,0,0,100,100,0,0,1,5,4,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Leg,,0,0,0,,{{\\pos(540,960)\\fscx88\\fscy88\\t(0,90,\\fscx100\\fscy100)}}{t}" for s, e, t in ev_]
    open(f"{OUT}/legendas.ass", "w").write(hdr + "\n".join(lines) + "\n")
    open(f"{OUT}/legendas.txt", "w").write("\n".join(f"{s:6.2f}-{e:6.2f} {t}" for s, e, t in ev_))

# ---------------------------------------------------------------- sons
def sfx_files():
    sr = 48000
    gens = {
        "whoosh": "anoisesrc=d=0.35:c=pink:a=0.6,bandpass=f=1800:w=1500,afade=t=in:d=0.15,afade=t=out:st=0.15:d=0.2",
        "pop": "sine=f=520:d=0.09,volume=0.9,afade=t=out:st=0.02:d=0.07",
        "ding": "sine=f=1568:d=0.5,afade=t=out:st=0.02:d=0.48,volume=0.5",
        "tick": "sine=f=2400:d=0.03,afade=t=out:d=0.03,volume=0.7",
        "click": "anoisesrc=d=0.03:c=white:a=0.8,highpass=f=2500,afade=t=out:d=0.03",
        "stamp": "sine=f=90:d=0.22,afade=t=out:st=0.02:d=0.2,volume=1.2",
    }
    for k, g in gens.items():
        p = f"{OUT}/sfx_{k}.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", g, "-ar", str(sr), "-ac", "1", p], check=True)
def sfx_events():
    out = [(e["t"], e["snd"]) for e in EV]
    for i in range(1, len(SEGS)):  # whoosh nas inversoes
        if SEGS[i][3] != SEGS[i - 1][3]: out.append((starts[i], "whoosh"))
    return sorted(out)

def compose():
    evs = sfx_events()
    swap = "+".join(f"between(t,{starts[i]:.3f},{starts[i] + SEGS[i][2] - SEGS[i][1] - 0.0001:.3f})" for i in range(len(SEGS)) if SEGS[i][3] == "top")
    inputs = ["-i", f"{OUT}/face.mov", "-i", f"{OUT}/lousa.mp4"]
    names = sorted({s for _, s in evs})
    for n in names: inputs += ["-i", f"{OUT}/sfx_{n}.wav"]
    fc = [f"color=c=black:s=1080x1920:r={FPS}:d={TOTAL:.3f}[bg]",
          f"[bg][0:v]overlay=x=0:y='if({swap},0,960)':eval=frame[v1]",
          f"[v1][1:v]overlay=x=0:y='if({swap},960,0)':eval=frame[v2]",
          f"[v2]ass={OUT}/legendas.ass[vout]",
          "[0:a]highpass=f=80,afftdn=nf=-25,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,equalizer=f=180:t=q:w=1:g=2,loudnorm=I=-14:TP=-1.5:LRA=7[voz]"]
    mix = ["[voz]"]
    for k, (t_, n) in enumerate(evs):
        idx = 2 + names.index(n); ms = int(t_ * 1000)
        fc.append(f"[{idx}:a]adelay={ms}|{ms},volume=0.22[s{k}]"); mix.append(f"[s{k}]")
    # separa as entradas de sfx reaproveitadas
    used = {}
    for k, (t_, n) in enumerate(evs):
        used.setdefault(n, []).append(k)
    split = []
    for n, ks in used.items():
        idx = 2 + names.index(n)
        split.append(f"[{idx}:a]asplit={len(ks)}" + "".join(f"[r{k}]" for k in ks))
    fc = [l for l in fc if not l.startswith("[") or ":a]adelay" not in l]
    fc += split
    for k, (t_, n) in enumerate(evs):
        ms = int(t_ * 1000); fc.append(f"[r{k}]adelay={ms}|{ms},volume=0.22[s{k}]")
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")
    open(f"{OUT}/fc.txt", "w").write(";\n".join(fc))
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex_script", f"{OUT}/fc.txt", "-map", "[vout]", "-map", "[aout]",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-t", f"{TOTAL:.3f}", f"{OUT}/reel-depoimento-cristina.mp4"], check=True)

if __name__ == "__main__":
    step = sys.argv[3] if len(sys.argv) > 3 else "all"
    print("duracao", round(TOTAL, 2))
    if step in ("all", "preview"):
        for tt in (1.5, 4.0, 8, 13, 17, 22, 27, 33, 37, 43, 47.5, 50.5):
            if tt < TOTAL: lousa(tt).save(f"{OUT}/prev_{tt:05.1f}.png")
    if step == "preview": sys.exit()
    build_ass(); sfx_files(); render_face(); render_lousa(); compose(); print("ok")
