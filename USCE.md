# Themes for USCE

Themes and skins control the appearance of UltraStar Community Edition.
The karaoke game lives in [USCE](https://github.com/UltraStar-CE/USCE).
Read [README.md](README.md) for theme structure, installation, and inherited
compatibility notes. This fork initially preserves the upstream assets.

This repository derives from
[UltraStar Deluxe Themes](https://github.com/UltraStar-Deluxe/Themes).
Preserve theme creator names, asset attribution, and all existing notices.
Before publishing new bundles, record the source and license or permission for
each included theme, image, font, video, and other asset. A repository-wide
license has not been established by this setup PR; do not infer one from the
game's license.

Record each asset in a `PROVENANCE.md` file in its theme directory, with a
relative asset path, creator, original source URL, license identifier or permission
reference, and changes made. Include applicable LICENSE/NOTICE files alongside
the theme. Unknown permissions must remain explicit and block redistribution
until established.

For changes, include the game commit you tested, affected screens, screenshots,
and provenance for new assets. Existing upstream notes warn that themes beyond
Modern and Deluxe require newer theme support. Verify compatibility against
the actual USCE game build before claiming a theme works.

The community's
[governance](https://github.com/UltraStar-CE/USCE/blob/HEAD/GOVERNANCE.md),
[contribution process](https://github.com/UltraStar-CE/USCE/blob/HEAD/CONTRIBUTING.md),
and [conduct policy](https://github.com/UltraStar-CE/USCE/blob/HEAD/CODE_OF_CONDUCT.md)
are being established in [the foundation PR](https://github.com/UltraStar-CE/USCE/pull/1).
During the recorded solo bootstrap phase, the sole maintainer may merge after
passing CI and addressing review findings. Once a second human developer joins,
require one independent approval; once there are more than four active developers,
require two. The governance defines the active roster. Maintainers use PRs too.
No automatic merges.

The USCE upstream tracker follows UltraStar-Deluxe/Themes:main. Record source
commits and compatibility adjustments in human-reviewed adaptation PRs. The
initial automation inventories changes; asset and theme adaptations remain
maintainer-led work.
