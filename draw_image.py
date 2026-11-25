#!/usr/bin/env python3
"""Draw the 25 Nov 2026 world-news summary image (1024x1024 PNG).

A dense one-page newspaper, written from scratch for this entry:
masthead, three big illustrated stories, a UTC timeline of the morning
as reported, a world map with numbered pins, a numbers column, and a
numbered list of stories 4-35. 35 stories in all, 6 continents + space.
Run: python3 draw_image.py
Writes: entry.png next to this file.
Uses only Pillow + DejaVu fonts available on this machine.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

PAPER = (250, 246, 236)
INK = (24, 28, 38)
NAVY = (16, 34, 60)
GOLD = (255, 214, 130)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
GREY = (90, 96, 108)
WHITE = (255, 255, 255)
BODY = (52, 58, 70)
RULE = (210, 204, 190)
SEA = (206, 224, 236)
LAND = (168, 196, 172)
LANDB = (140, 175, 150)
SKY = (18, 30, 58)


def font(name, size):
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/" + name, size)


F_MAST = font("DejaVuSans-Bold.ttf", 46)
F_DATE = font("DejaVuSans-Bold.ttf", 20)
F_COUNT = font("DejaVuSans-Bold.ttf", 22)
F_KICK = font("DejaVuSans-Bold.ttf", 15)
F_HEAD = font("DejaVuSans-Bold.ttf", 20)
F_BODY = font("DejaVuSans.ttf", 14)
F_SEC = font("DejaVuSans-Bold.ttf", 16)
F_TIME = font("DejaVuSans-Bold.ttf", 13)
F_TLAB = font("DejaVuSans.ttf", 12)
F_NUM = font("DejaVuSans-Bold.ttf", 18)
F_NUMS = font("DejaVuSans-Bold.ttf", 14)
F_NLAB = font("DejaVuSans.ttf", 11)
F_NLABS = font("DejaVuSans.ttf", 10)
F_LIST = font("DejaVuSans.ttf", 13)
F_LISTB = font("DejaVuSans-Bold.ttf", 13)
F_LEG = font("DejaVuSans.ttf", 11)
F_FOOT = font("DejaVuSans.ttf", 13)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def tw(s, f):
    return d.textlength(s, font=f)


def wrap(text, f, max_w, max_lines=2):
    """Greedy word wrap, at most max_lines; last line gets an ellipsis."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = (cur + " " + word).strip()
        if tw(trial, f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
            if len(lines) == max_lines:
                break
    if len(lines) < max_lines and cur:
        lines.append(cur)
    elif lines and len(lines) == max_lines:
        last = lines[-1]
        while last and tw(last + " ...", f) > max_w:
            last = last.rsplit(" ", 1)[0] if " " in last else ""
        lines[-1] = (last + " ...").strip()
    return lines


# ------------------------------------------------------------------ masthead
d.rectangle([0, 0, W, 100], fill=NAVY)
d.rectangle([0, 100, W, 106], fill=RED)
d.text((16, 10), "THE WORLD TODAY", font=F_MAST, fill=WHITE)
d.text((16, 66), "WEDNESDAY 25 NOVEMBER 2026", font=F_DATE, fill=GOLD)
d.text((1008, 66), "35 STORIES", font=F_COUNT, fill=WHITE, anchor="ra")
d.text((1008, 22), "6 CONTINENTS + SPACE", font=F_DATE, fill=GOLD, anchor="ra")

# ------------------------------------------------------------------ big stories
# (kicker, headline, body, accent, picture)
BIG = [
    ("SPACE  •  CHINA",
     "Pakistan's first astronaut reaches Tiangong",
     "Launched 00:18 UTC, docked 03:56 UTC. "
     "Zeeshan Ali: first Pakistani in orbit.",
     TEAL, "rocket"),
    ("ENERGY  •  HORMUZ",
     "Six tankers hit by mines in the Strait",
     "Tehran says six tankers hit mines in 24h; claim "
     "unconfirmed. The US blockade holds.",
     RED, "tanker"),
    ("TRADE  •  WASHINGTON",
     "US set to unveil new tariffs",
     "Section 301 findings on 16 partners due; "
     "Asian stocks slid on the news.",
     (16, 100, 140), "tariff"),
]


def picture(x, y, w, h, kind, color):
    """A simple scene drawn in the box (x, y, w, h)."""
    if kind == "rocket":
        d.rectangle([x, y, x + w, y + h], fill=SKY)
        for sx, sy in ((18, 12), (60, 26), (120, 10), (180, 30), (250, 14),
                       (290, 40), (90, 48), (220, 55)):
            d.ellipse([x + sx, y + sy, x + sx + 4, y + sy + 4], fill=WHITE)
        d.ellipse([x + 190, y + h - 30, x + w - 4, y + h + 6],
                  fill=(52, 90, 140))
        d.ellipse([x + 205, y + h - 20, x + w - 18, y + h + 2],
                  fill=(90, 140, 90))
        cx = x + w // 2 - 30
        d.polygon([(cx + 22, y + 8), (cx + 38, y + 34), (cx + 6, y + 34)],
                  fill=RED)
        d.rectangle([cx + 6, y + 34, cx + 38, y + 66], fill=WHITE)
        d.rectangle([cx + 14, y + 44, cx + 30, y + 56], fill=TEAL)
        d.polygon([(cx + 6, y + 58), (cx - 6, y + 76), (cx + 6, y + 68)],
                  fill=RED)
        d.polygon([(cx + 38, y + 58), (cx + 50, y + 76), (cx + 38, y + 68)],
                  fill=RED)
        d.polygon([(cx + 16, y + 66), (cx + 28, y + 66), (cx + 22, y + 84)],
                  fill=GOLD)
    elif kind == "tanker":
        d.rectangle([x, y, x + w, y + h], fill=(178, 214, 232))
        d.rectangle([x, y + 52, x + w, y + h], fill=(28, 78, 122))
        d.polygon([(x + 30, y + 52), (x + w - 30, y + 52), (x + w - 55, y + 78),
                   (x + 55, y + 78)], fill=(60, 60, 66))
        d.rectangle([x + 150, y + 28, x + 195, y + 52], fill=WHITE)
        d.rectangle([x + 165, y + 16, x + 180, y + 28], fill=WHITE)
        for mx, my in ((60, 66), (120, 60), (250, 64)):
            d.ellipse([x + mx - 5, y + my - 5, x + mx + 5, y + my + 5],
                      fill=(30, 30, 30))
            d.line([x + mx - 8, y + my, x + mx + 8, y + my], fill=(30, 30, 30),
                   width=2)
            d.line([x + mx, y + my - 8, x + mx, y + my + 8], fill=(30, 30, 30),
                   width=2)
        d.ellipse([x + 225, y + 8, x + 255, y + 38], outline=(255, 120, 40),
                  width=3)
        d.line([x + 225, y + 23, x + 255, y + 23], fill=(255, 120, 40), width=3)
    else:  # tariff: falling bars with a down arrow
        d.rectangle([x, y, x + w, y + h], fill=(238, 234, 224))
        base = y + h - 12
        for i, bh in enumerate((34, 52, 44, 66, 48)):
            bx = x + 24 + i * 52
            col = RED if i >= 3 else (16, 100, 140)
            d.rectangle([bx, base - bh, bx + 34, base], fill=col)
        d.line([x + 20, y + 12, x + 150, y + 34, x + 260, y + 62],
               fill=RED, width=5)
        d.polygon([(x + 260, y + 62), (x + 236, y + 58), (x + 256, y + 80)],
                  fill=RED)
        # "301" sits in the free top-right corner, clear of the trend line
        # (which crosses the top-left) and clear of the tallest bar below.
        d.text((x + w - 12, y + 4), "301", font=F_KICK, fill=RED,
               anchor="ra")


for i, (kicker, head, body, color, kind) in enumerate(BIG):
    x = 16 + i * 334
    y = 112
    w = 324
    d.rounded_rectangle([x, y, x + w, y + 206], radius=10, fill=WHITE,
                        outline=RULE, width=2)
    picture(x + 8, y + 8, w - 16, 86, kind, color)
    d.text((x + 12, y + 102), kicker, font=F_KICK, fill=color)
    hy = y + 122
    for line in wrap(head, F_HEAD, w - 24):
        d.text((x + 12, hy), line, font=F_HEAD, fill=INK)
        hy += 24
    by = hy + 4
    for line in wrap(body, F_BODY, w - 24, max_lines=2):
        d.text((x + 12, by), line, font=F_BODY, fill=BODY)
        by += 17

# ------------------------------------------------------------------ timeline
d.text((16, 328), "THE DAY AS REPORTED  —  BBC WORLD, UTC", font=F_SEC, fill=NAVY)
d.line([16, 404, 1008, 404], fill=RULE, width=2)
# (time, line 1, line 2) — labels kept short on purpose: dots sit 151 px
# apart, so every line must stay well under that; the widest line here is
# "Nvidia questions" at ~100 px, leaving ~50 px of air on each side.
TL = [
    ("00:18", "Shenzhou-24", "lifts off"),
    ("00:56", "Russia: 500k", "war dead"),
    ("01:40", "Markle indicted", "in the US"),
    ("02:59", "Huawei guilty", "of trade theft"),
    ("03:44", "US AG dodges", "Nvidia questions"),
    ("04:49", "Abrego leaves", "US for Spain"),
    ("07:04", "Real Madrid", "5-1 PSV"),
]
d.line([60, 378, 968, 378], fill=NAVY, width=3)
for i, (t, l1, l2) in enumerate(TL):
    cx = 60 + i * 151
    # Clamp the label centre so the widest line never runs off the page:
    # half-width + 6 px margin from each edge.
    half = max(tw(l1, F_TLAB), tw(l2, F_TLAB)) / 2
    cx = max(half + 6, min(cx, 1018 - half))
    d.ellipse([60 + i * 151 - 8, 370, 60 + i * 151 + 8, 386], fill=RED,
              outline=WHITE, width=2)
    d.text((60 + i * 151, 348), t, font=F_TIME, fill=RED, anchor="ma")
    d.text((cx, 392), l1, font=F_TLAB, fill=INK, anchor="ma")
    d.text((cx, 408), l2, font=F_TLAB, fill=GREY, anchor="ma")

# ------------------------------------------------------------------ map + numbers
d.rounded_rectangle([16, 428, 664, 550], radius=10, fill=WHITE,
                    outline=RULE, width=2)
d.text((28, 436), "WHERE IT HAPPENED", font=F_SEC, fill=NAVY)
d.rectangle([28, 460, 652, 518], fill=SEA)
# rough continents (panel-local coords, scaled to fit the sea box)
OX, OY = 28, 460
SX, SY = 0.98, 0.48  # map box is 624 x 58, continent sketch is 570 x 112
LANDS = [
    [(32, 12), (122, 0), (162, 17), (142, 47), (92, 62), (42, 52), (17, 32)],
    [(122, 67), (157, 64), (167, 87), (147, 112), (127, 92)],
    [(272, 7), (312, 0), (327, 22), (302, 37), (272, 27)],
    [(272, 42), (322, 40), (337, 72), (312, 102), (282, 87), (267, 62)],
    [(332, 2), (452, -3), (532, 12), (562, 37), (512, 62), (442, 67),
     (372, 52), (337, 27)],
    [(492, 87), (542, 84), (552, 100), (512, 107), (487, 97)],
]
for poly in LANDS:
    pts = [(OX + px * SX, OY + py * SY) for px, py in poly]
    d.polygon(pts, fill=LAND, outline=LANDB)
PINS = [
    (1, 492, 22),   # Jiuquan
    (2, 380, 42),   # Hormuz
    (3, 350, 58),   # Riyadh (moved apart from Hormuz so pins don't overlap)
    (4, 327, 40),   # Gaza
    (5, 307, 17),   # Kyiv
    (6, 67, 27),    # Washington
    (7, 512, 77),   # Bogor
    (8, 302, 77),   # Ituri
]
for n, px, py in PINS:
    cx, cy = OX + px * SX, OY + py * SY
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=RED, outline=WHITE,
              width=2)
    d.text((cx, cy), str(n), font=F_TLAB, fill=WHITE, anchor="mm")
d.text((28, 522),
       "1 Jiuquan   2 Hormuz   3 Riyadh   4 Gaza   5 Kyiv   6 Washington",
       font=F_LEG, fill=BODY)
d.text((28, 536), "7 Bogor   8 Ituri, DR Congo",
       font=F_LEG, fill=BODY)

d.rounded_rectangle([676, 428, 1008, 550], radius=10, fill=NAVY)
d.text((692, 436), "THE DAY IN NUMBERS", font=F_SEC, fill=GOLD)
NUMS = [
    ("500,000", "Russian war deaths (own figures)"),
    ("74,746", "Gaza death toll"),
    ("30", "miners trapped in Bogor"),
    ("11", "hurt in the Riyadh tower strike"),
    ("5-1", "Real top UCL group, 15 pts"),
    ("~$91", "Brent crude a barrel"),
]
# 6 rows in ~92 px of panel: 15 px steps with a 14 pt number fit cleanly;
# the old 18 pt numbers on 14 px steps overlapped each other.
ny = 458
for big, lab in NUMS:
    d.text((692, ny), big, font=F_NUMS, fill=WHITE)
    d.text((772, ny + 3), lab, font=F_NLABS, fill=(210, 220, 235))
    ny += 15

# ------------------------------------------------------------------ story list 4-35
d.text((16, 556), "THE REST OF THE DAY  —  STORIES 4–35", font=F_SEC, fill=NAVY)
d.line([16, 578, 1008, 578], fill=NAVY, width=2)
REST = [
    "Putin vows revenge for Ukraine refinery strikes",
    "Kyiv claims Baltic cargo-ship drone strike",
    "Ukraine: sea drones sank Russian corvette off Libya",
    "Magyar meets Zelensky, first Hungary PM visit since 2015",
    "Norway pledges at least $7bn to Ukraine in 2027",
    "Russian strike on Zaporizhzhia flats: 2 dead, 40+ hurt",
    "Gaza: Israeli strike kills Hamas security chief",
    "Gaza death toll reaches 74,746; 9 killed in a day",
    "Houthis hit Riyadh PIF tower; 11 people injured",
    "Houthis threaten Jeddah, Saudi Red Sea ports",
    "Saudi-led coalition orders civilians out of Hodeidah",
    "WHO pulls staff from DR Congo hospital in Ebola zone",
    "DR Congo plane missing; rebels claim shoot-down",
    "Sahel rebels turn cheap FPV drones on Mali army",
    "China probes Politburo member Chen Jining",
    "Russia sends home Chinese suspect in $2.3bn case",
    "Australia inflation 3.8%; rate pressure grows",
    "Asia stocks slide: Seoul -5.3%, Taipei -5.1%",
    "Bitcoin $59,258; ether $1,661 as crypto slips",
    "US core PCE data due before Thanksgiving",
    "Nvidia shares fall ~7% as Huang returns as CEO",
    "COP31 fallout: focus shifts to COP32 in Addis Ababa",
    "Myanmar tops world landmine toll: 1,891 hurt in 2025",
    "30 miners trapped in flooded Bogor gold mine",
    "Cikande candy-factory fire toll rises to 26",
    "Real Madrid 5-1 PSV; Arsenal 1-1 Dortmund",
    "Senegal reinstated as 2025 Africa Cup winners",
    "Sarkozy and Carla Bruni ordered to face trial",
    "Eisenkot seals first coalition pact in Israel",
    "Solomon Islands swaps China pact for Australia",
    "NATO chief vows defence vs space threat",
    "Trump pardons turkeys Freedom and Feathers",
]
assert len(REST) == 32, len(REST)
for j, item in enumerate(REST):
    col = j // 16
    row = j % 16
    x = 16 + col * 504
    y = 588 + row * 23
    num = 4 + j
    d.text((x, y), str(num) + ".", font=F_LISTB, fill=RED)
    d.text((x + 30, y), item, font=F_LIST, fill=INK)

# ------------------------------------------------------------------ footer
d.rectangle([0, 956, W, H], fill=NAVY)
d.text((16, 962),
       "DATE CHECK: COP31 ended 22 Nov, only its 25 Nov fallout counts here. "
       "Miley Cyrus married 21 Nov, not today.",
       font=F_FOOT, fill=GOLD)
d.text((16, 984),
       "UCL scores are Tue night, first reported Wed 25 Nov UTC. "
       "Sources: Reuters, BBC, Xinhua, UEFA, Carbon Brief, Al Jazeera.",
       font=F_FOOT, fill=WHITE)
d.text((16, 1006),
       "Drawn for make.fun  •  entry by @dinishkawaii  •  Wednesday 25 November 2026",
       font=F_FOOT, fill=(180, 195, 215))

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT)
