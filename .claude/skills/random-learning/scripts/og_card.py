"""Render a per-day Open Graph share card (1200x630 PNG) with Pillow.

Each dated entry gets its own card showing that day's topic titles, so a shared
link previews the actual day rather than a generic site image. Rendering is pure
Pillow + a bundled OFL font (PT Serif), so it is deterministic and works the same
locally and in CI with no system rasterizer. ``build_site`` imports
``render_day_card``; if Pillow is unavailable the build falls back to the static
site card.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MARGIN = 84
PAPER = (250, 247, 241)
INK = (33, 29, 24)
MUTED = (111, 102, 87)
ACCENT = (180, 84, 31)
ACCENT_INK = (143, 63, 21)
GLOW = (246, 216, 191)
SUN = (241, 201, 164)

FONTS_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS_DIR / name), size)


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _draw_dawn(img: Image.Image) -> None:
    """Soft corner glow + a faint sun motif, echoing the favicon."""
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = 1090, -40
    for r, a in ((520, 26), (400, 30), (280, 36), (180, 40)):
        gd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GLOW + (a,))
    img.alpha_composite(glow)
    d = ImageDraw.Draw(img)
    # sun rays + arc (faint), top-right
    sx, sy, R = 1010, 150, 70
    for ang in range(0, 360, 45):
        import math
        a = math.radians(ang)
        d.line((sx + math.cos(a) * (R + 16), sy + math.sin(a) * (R + 16),
                sx + math.cos(a) * (R + 40), sy + math.sin(a) * (R + 40)),
               fill=SUN + (170,), width=5)
    d.arc((sx - R, sy - R, sx + R, sy + R), 180, 360, fill=SUN + (210,), width=6)
    d.line((sx - R - 22, sy, sx + R + 22, sy), fill=SUN + (210,), width=6)


def render_day_card(out_path, date_display: str, topic_titles: list[str], count: int) -> None:
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    _draw_dawn(img)
    d = ImageDraw.Draw(img)

    kicker = _font("PT_Serif-Web-Bold.ttf", 26)
    title_f = _font("PT_Serif-Web-Bold.ttf", 46)
    foot_f = _font("PT_Serif-Web-Bold.ttf", 26)
    foot_r = _font("PT_Serif-Web-Regular.ttf", 24)

    # kicker
    d.text((MARGIN, 70), f"{date_display.upper()}  ·  RANDOM LEARNING",
           font=kicker, fill=ACCENT_INK)

    # topic titles (max 3), each wrapped, with an accent marker
    y = 150
    max_w = W - MARGIN - 200
    for i, title in enumerate(topic_titles[:3]):
        lines = _wrap(d, title, title_f, max_w)[:2]
        d.rectangle((MARGIN, y + 12, MARGIN + 16, y + 28), fill=ACCENT)
        for ln in lines:
            d.text((MARGIN + 38, y), ln, font=title_f, fill=INK)
            y += 58
        y += 26

    # footer
    fy = H - 92
    d.line((MARGIN, fy, MARGIN + 120, fy), fill=ACCENT, width=3)
    d.text((MARGIN, fy + 18),
           f"{count} {'thing' if count == 1 else 'things'} I learned · grounded in the last 30 days",
           font=foot_r, fill=MUTED)
    brand = "rl.fz.ax"
    bw = d.textlength(brand, font=foot_f)
    d.text((W - MARGIN - bw, fy + 16), brand, font=foot_f, fill=INK)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(out_path, "PNG")
