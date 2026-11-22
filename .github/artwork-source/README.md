# Background source and build recipe

Fall, Summer, and Winter were generated for USCE on 2026-11-22 with OpenAI
image generation. No inherited theme image was supplied as input. The
unbranded source PNGs are in this directory. Blue is drawn from numerical
color stops and a radial light falloff in the build script.

The three seasonal prompts used this shared direction: "Create a new original
background image for a karaoke game menu, landscape 4:3 if supported.
Atmospheric photographic texture, [palette]. The scene is [scene]. Maintain a
darkened, low-detail central region and edges for white menus and text. No
letters, text, logo, people, frame, icons, central subject, or UI elements.
Soft vignette, fine film texture, a polished understated game background.
Invent all imagery; no reference or recreation of any existing image."

| Season | Palette | Scene |
| --- | --- | --- |
| Fall | late autumn copper, burnt orange, muted gold, earth-green | softly defocused autumn woodland, with gold and copper leaves and warmly lit drooping branches kept at the edges |
| Summer | warm rose, coral, wine and subtle green | softly defocused summer garden flowers and warm, hazy foliage kept near the edges |
| Winter | slate blue, silver, midnight navy and icy teal | softly defocused winter frost on delicate glass and branch tips kept near the edges |

The wordmark comes from [USCE branding](https://github.com/UltraStar-CE/USCE/blob/a2072d52bfc5d7a006e14d10bcc94ab1bc8b1008/branding/usce-logo-horizontal.png).
The composition keeps the star and microphone, renders the dark letters in
white for use on dark backgrounds, and moves the wordmark to the center on
loading screens. Modern draws a continuous monochrome star and uses the short USCE wordmark
without the subtitle. Deluxe uses the full wordmark. The script verifies the
branding source checksum.

Run `python .github/artwork-source/build-backgrounds.py PATH_TO_USCE_LOGO` with
Python and Pillow. It preserves the existing 800x600 and 1672x941 asset sizes.
