# Artwork and license records

See [theme credits](CREDITS.md) for the original theme designers and source
projects. This is a collection with different terms for individual works. Keep
the applicable copyright and license notices with each copy of a theme,
including archives and bundles that ship only a subset of the collection.

## Recorded terms

| Scope | Source and accompanying files |
| --- | --- |
| Clarity theme definition, skin and original Clarity textures | [Clarity's source note](Clarity/PROVENANCE.md) and [copy of the pinned USCE license text](Clarity/LICENSE). Modern assets used through inheritance have their own source notices. |
| Karaoke theme definition and original generated layout artwork | [Pinned Karaoke source and artwork generator](https://github.com/3Ryuusei3/USDX/tree/82668398840dc06d1c30ba82ab13090385ff14c0/tools/theme-karaoke), [credits](Karaoke/CREDITS.txt) and [GPL license text](Karaoke/LICENSE). Bundled fonts retain their own licenses. |
| Karaoke and Midnight Inter fonts | [Inter](https://github.com/rsms/inter), SIL OFL 1.1. The font files report build `4.001;git-9221beed3`. Notices are installed with [Karaoke](Karaoke/fonts/Inter/LICENSE.txt) and [Midnight](Midnight/fonts/Inter/LICENSE.txt). |
| Karaoke JetBrains Mono fonts | [JetBrains Mono 2.304](https://github.com/JetBrains/JetBrainsMono/tree/v2.304), SIL OFL 1.1. [Bundled OFL text and copyright](Karaoke/fonts/JetBrainsMono/OFL.txt). |
| Midnight Liberation Sans fonts | [Liberation Sans 2.1.4](https://github.com/liberationfonts/liberation-fonts/tree/2.1.4), SIL OFL 1.1. [Bundled OFL text and copyright](Midnight/fonts/LiberationSans/LICENSE.txt). |
| Modern and standalone Neon rating icons | Modern and standalone Neon ship identical PNGs. See [asset-level attribution, conversion and license links](Modern/ASSET-NOTICES.md). Other themes' rating files have different blobs and need their own source verification. |

## USCE adaptations

USCE is a fork of UltraStar Deluxe. We would have liked to keep the
UltraStar Deluxe name, but using it for both projects would cause confusion,
especially where they share themes and layouts. USCE uses its own name and
logo so players can tell which version they are running and report
USCE-specific bugs to the USCE tracker.

- Modern and Deluxe menu and loading artwork was adapted in
  [63af239](https://github.com/UltraStar-CE/Themes/commit/63af239) and
  [5cd309f](https://github.com/UltraStar-CE/Themes/commit/5cd309f). Themes
  [#42](https://github.com/UltraStar-CE/Themes/pull/42) replaced edited
  backgrounds with independently produced artwork, with [sources and build
  instructions](.github/artwork-source/README.md). See the
  [Modern branding record](Modern/USCE-BRANDING.md) for the wordmark source.
- Themes [#41](https://github.com/UltraStar-CE/Themes/pull/41) removed
  `Modern/[main]songCover.png`, the Candy fallback badge, and the related
  skin mappings. Current bundles use the rendered title tiles from
  USCE [#465](https://github.com/UltraStar-CE/USCE/pull/465).
- [Midnight's credits](Midnight/CREDITS.txt) distinguish the source design
  from the procedural textures in this collection. Its skin inherits Modern.
- [Halloween's source note](Halloween/README.md) identifies its generated
  background and avatars. Its inherited Modern assets use the Modern notices.

## Evidence still needed

| Scope | Current evidence and follow-up |
| --- | --- |
| Verdure Drippin and Springtime media | Their skin headers credit dreamscene.org and describe the videos as free for private or non-commercial use with all rights reserved. Find the original terms or explicit permission covering redistribution and the edited derivatives. The eight `[bg-video]*.avi` files and the static stills `[bg]drippin.jpg` and `[bg]springtime.jpg` need review together. |
| WorldParty Argon and Neon | The creator credit is recorded. Argon skin headers credit some icons to Iconfinder under a generic Creative Commons reference. Identify the original listing, creator, exact license and icon files. Verify the sources and terms for the four bundled WorldParty video backgrounds independently. |
| Candy, Deluxe and standalone Neon background videos | The theme sources establish the theme credits. Original video authorship and terms remain unverified for Candy's `[bg-main]clouds.AVI` and `[bg-main]options.AVI`, Deluxe's `[bg-video]_ocean.avi` and `[bg-video]ribbon.mov`, and Neon's `[bg-main]smoke.mp4` and `[bg-main]smoke_neon_sign.mp4`. |
| Remaining inherited graphics | Where individual files lack a traceable source or permission, preserve the existing credits and obtain asset-specific evidence or source a replacement. The general Tango comments in some skin INIs and the theme creator field alone do not identify the licensing of every graphic. |

For new or modified artwork, record the affected path, creator, original source,
license identifier and text or permission reference, and what changed. Include
required notices in the theme folder so a separately distributed skin or theme
can carry them. A screenshot review, a creator credit and a public source URL
each document different things from redistribution permission.
