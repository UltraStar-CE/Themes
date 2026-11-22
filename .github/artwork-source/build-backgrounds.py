"""Build the themed menu and loading backgrounds from original USCE artwork."""

from io import BytesIO
from math import exp
from pathlib import Path
from random import Random
import argparse
import hashlib

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".github" / "artwork-source"
MENU_SIZE = (800, 600)
WIDE_SIZE = (1672, 941)
SEASONS = ("fall", "summer", "winter")


def blue_background(size):
    """Draw a radial blue glow with slight dithering before quantization."""
    width, height = size
    noise = Random(7623)
    pixels = []
    for y in range(height):
        for x in range(width):
            dx, dy = (x / width - 0.48) * 2, (y / height - 0.42) * 2
            light = exp(-2.4 * (dx * dx + dy * dy))
            dither = noise.uniform(-0.65, 0.65)
            pixels.append(tuple(round(dark + light * (bright - dark) + dither)
                                for dark, bright in ((8, 64), (29, 136), (74, 187))))
    result = Image.new("RGB", size)
    result.putdata(pixels)
    return result


def dark_surface_wordmark(source):
    """Keep the canonical star and render its dark text in white."""
    logo = Image.open(BytesIO(source)).convert("RGBA")
    alpha = logo.getchannel("A")
    box = alpha.point(lambda value: 255 if value > 64 else 0).getbbox()
    text = (855, 0, logo.width, logo.height)
    white_text = Image.new("RGBA", (text[2] - text[0], text[3]), "white")
    white_text.putalpha(alpha.crop(text))
    logo.paste(white_text, text[:2])
    return logo.crop(box)


def modern_wordmark(source):
    """Use a monochrome star and short USCE wordmark for Modern."""
    logo = Image.open(BytesIO(source)).convert("RGBA")
    alpha = logo.getchannel("A")
    star = Image.new("RGBA", (855, logo.height))
    points = [(503, 52), (604, 280), (827, 295), (652, 448),
              (715, 677), (503, 545), (289, 677), (353, 448),
              (174, 295), (402, 280)]
    draw = ImageDraw.Draw(star)
    draw.polygon(points, fill=(205, 219, 235, 255))
    draw.rounded_rectangle((436, 264, 567, 464), radius=65, fill=(32, 65, 105, 255))
    draw.rounded_rectangle((486, 436, 519, 518), radius=16, fill=(32, 65, 105, 255))
    for y in (318, 358, 398):
        draw.rounded_rectangle((465, y, 539, y + 12), radius=6,
                               fill=(205, 219, 235, 255))

    wordmark = Image.new("RGBA", logo.size)
    wordmark.paste(star)
    letters_box = (855, 0, logo.width, 565)
    letters_alpha = alpha.crop(letters_box)
    letters = Image.new("RGBA", letters_alpha.size, "white")
    letters.putalpha(letters_alpha)
    wordmark.paste(letters, letters_box[:2])
    return wordmark.crop(wordmark.getbbox())


def branded(background, wordmark, *, loading=False, top_margin=0.027):
    output = background.copy()
    width, height = output.size
    logo_width = round(width * (0.44 if loading else 0.14))
    logo_height = round(logo_width * wordmark.height / wordmark.width)
    logo = wordmark.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
    if loading:
        position = ((width - logo_width) // 2, (height - logo_height) // 2)
    else:
        position = (width - logo_width - round(width * 0.026), round(height * top_margin))
    output.paste(logo.convert("RGB"), position, logo.getchannel("A"))
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logo", type=Path, help="USCE branding/usce-logo-horizontal.png")
    args = parser.parse_args()
    logo = args.logo.read_bytes()
    if hashlib.sha256(logo).hexdigest() != "daf828018bdb36058091cef2edcc4ca1e123bdee2d950302d2d48ac9b08d9375":
        parser.error("The wordmark must match the source listed in the branding notice.")
    wordmark = dark_surface_wordmark(logo)
    modern = modern_wordmark(logo)

    backgrounds = {"blue": blue_background(MENU_SIZE)}
    for season in SEASONS:
        with Image.open(SOURCE / f"{season}.png") as image:
            backgrounds[season] = ImageOps.fit(image.convert("RGB"), MENU_SIZE,
                                                Image.Resampling.LANCZOS)

    for theme in ("Modern", "Deluxe"):
        for season, background in backgrounds.items():
            path = ROOT / theme / f"[bg-main]{season}.jpg"
            branded(background, modern if theme == "Modern" else wordmark,
                    top_margin=0.05 if theme == "Modern" else 0.027).save(
                        path, quality=93, optimize=True)

    for theme, season in (("Modern", "blue"), ("Modern", "winter"),
                          ("Deluxe", "fall"), ("Deluxe", "summer")):
        path = ROOT / theme / f"[bg-load]{season}.png"
        branded(backgrounds[season], modern if theme == "Modern" else wordmark, loading=True).save(path, optimize=True)

    path = ROOT / "Modern" / "[bg-song]blue-wide.png"
    branded(blue_background(WIDE_SIZE), modern, top_margin=0.05).save(path, optimize=True)


if __name__ == "__main__":
    main()
