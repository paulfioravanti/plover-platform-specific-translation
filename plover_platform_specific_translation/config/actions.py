"""
Module to handle reading in the application JSON config file.
"""
from pathlib import Path

from . import file


def load(config_filepath: Path) -> dict[str, str]:
    """
    Reads in the config JSON file and resolves each platform-specific
    translation.

    Raises an error if the specified config file is not JSON format.
    """
    data = file.load(config_filepath)
    config_platform_translations = (
        data.get("platform_specific_translations", {})
    )

    if not isinstance(config_platform_translations, dict):
        raise ValueError("'platform_specific_translations' must be a dict")

    return config_platform_translations

def save(config_filepath: Path, platform_translations: dict[str, str]) -> None:
    """
    Saves the set of platform-specific translations to the config JSON file.
    """
    data = {"platform_specific_translations": platform_translations}
    file.save(config_filepath, data)
