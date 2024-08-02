"""
Module to handle reading in the application JSON config file.
"""
from pathlib import Path
from typing import Tuple

from . import file


def load(config_filepath: Path) -> dict[str, Tuple[str, str]]:
    """
    Reads in the config JSON file and resolves each platform-specific
    translation.

    Raises an error if the specified config file is not JSON format.
    """
    data = file.load(config_filepath)

    try:
        config_platform_translations = data["platform_specific_translations"]
    except KeyError:
        return {}

    if not isinstance(config_platform_translations, dict):
        raise ValueError("'platform_specific_translations' must be a dict")

    platform_translations = {
        outline_translation: tuple(resolved_translation)
        for outline_translation, resolved_translation
        in config_platform_translations.items()
    }

    return platform_translations

def save(
    config_filepath: Path,
    platform_translations: dict[str, Tuple[str, str]]
) -> None:
    """
    Saves the set of platform-specific translations to the config JSON file.
    """
    data = {"platform_specific_translations": platform_translations}
    file.save(config_filepath, data)
