"""
Module to resolve the appropriate translation given a set of platform-specific
translations.
"""
_ARGUMENT_DIVIDER = ":"

def resolve(platform: str, outline_translation: str) -> str:
    """
    Resolves a single translation from a set of platform-specific translations.
    """
    platform_translations = _parse_outline_translation(outline_translation)

    try:
        translation = platform_translations[platform]
    except KeyError:
        try:
            translation = platform_translations["OTHER"]
        except KeyError as exc:
            raise ValueError(
                f"No translation provided for platform: {platform}"
            ) from exc

    return translation

def _parse_outline_translation(outline_translation: str) -> dict[str, str]:
    it = iter(outline_translation.split(_ARGUMENT_DIVIDER))
    return {
        platform.upper(): translation
        for platform, translation
        in zip(it, it)
    }
