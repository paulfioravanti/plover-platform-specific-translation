"""
Module to handle reading in the application JSON config file.
"""
from pathlib import Path
from typing import (
    Any,
    Tuple
)

from . import (
    file,
    transformer
)


def load(config_filepath: Path) -> dict[str, Tuple[str, str]]:
    """
    Reads in the config JSON file and resolves each platform-specific
    translation.

    Raises an error if the specified config file is not JSON format.
    """
    data: dict[str, Any] = file.load(config_filepath) # extractor function
    return transformer.transform_inbound(data)

def save(
    config_filepath: Path,
    platform_translations: dict[str, Tuple[str, str]]
) -> None:
    """
    Saves the set of platform-specific translations to the config JSON file.
    """
    data: dict[str, dict[str, Tuple[str, str]]] = (
        transformer.transform_outbound(platform_translations)
    )
    file.save(config_filepath, data)
