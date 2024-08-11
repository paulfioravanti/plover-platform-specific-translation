"""
Module to resolve the appropriate translation given a set of platform-specific
translations.
"""
import re
from typing import (
    Pattern,
    Tuple
)


COMBO = "combo"
COMMAND = "command"
_TEXT = "text"

_ARGUMENT_DIVIDER: Pattern[str] = re.compile(
    "(?:(?<=MAC)|(?<=WINDOWS)|(?<=LINUX|OTHER)):"
    "|:(?:(?=MAC)|(?=WINDOWS)|(?=LINUX|OTHER))",
    re.IGNORECASE
)
_COMBO_TYPE: Pattern[str] = re.compile(r"#(.*)")
_COMMAND_TYPE: Pattern[str] = re.compile(
    r"(?:PLOVER|:COMMAND):(.*)",
    re.IGNORECASE
)

def resolve(platform: str, outline_translation: str) -> Tuple[str, str]:
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

    if combo_translation := re.match(_COMBO_TYPE, translation):
        return (COMBO, combo_translation.group(1))

    if command_translation := re.match(_COMMAND_TYPE, translation):
        return (COMMAND, command_translation.group(1))

    return (_TEXT, translation)

def _parse_outline_translation(outline_translation: str) -> dict[str, str]:
    it = iter(re.split(_ARGUMENT_DIVIDER, outline_translation))
    return {
        platform.upper(): translation
        for platform, translation
        in zip(it, it)
    }
