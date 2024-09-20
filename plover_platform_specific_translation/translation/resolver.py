"""
Module to resolve the appropriate translation given a set of platform-specific
translations.
"""
import re
from typing import (
    Any,
    Iterator,
    Optional,
    Match,
    Pattern,
    Tuple,
    Union
)


COMBO: str = "combo"
COMMAND: str = "command"
_TEXT: str = "text"

# Ignore any colons in commands contained in outline translations.
_ARGUMENT_DIVIDER: Pattern[str] = re.compile(
    """
    (?:(?<=MAC)|(?<=WINDOWS)|(?<=LINUX|OTHER)): # Colon after platform name
    |:(?:(?=MAC)|(?=WINDOWS)|(?=LINUX|OTHER))   # OR colon before platform name
    """,
    re.IGNORECASE | re.VERBOSE
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
    platform_translations: dict[str, str] = (
        _parse_outline_translation(outline_translation)
    )

    translation: str
    try:
        translation = platform_translations[platform]
    except KeyError:
        try:
            translation = platform_translations["OTHER"]
        except KeyError as exc:
            raise ValueError(
                f"No translation provided for platform: {platform}"
            ) from exc

    return _resolve_type_for_translation(translation)

def _parse_outline_translation(outline_translation: str) -> dict[str, str]:
    it: Iterator[Union[str, Any]] = iter(
        re.split(_ARGUMENT_DIVIDER, outline_translation)
    )

    # REF: https://stackoverflow.com/a/5389547/567863
    return {
        platform.upper(): translation
        for platform, translation
        in zip(it, it)
    }

def _resolve_type_for_translation(translation: str) -> Tuple[str, str]:
    combo_translation: Optional[Match[str]]
    if combo_translation := re.match(_COMBO_TYPE, translation):
        return (COMBO, combo_translation.group(1))

    command_translation: Optional[Match[str]]
    if command_translation := re.match(_COMMAND_TYPE, translation):
        return (COMMAND, command_translation.group(1))

    return (_TEXT, translation)
