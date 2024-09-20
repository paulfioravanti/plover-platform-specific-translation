"""
Transformer

Module to handle transforming information from the application JSON config file
into a form the application can work with.
"""
from typing import (
    Any,
    Tuple
)

def transform_inbound(data: dict[str, Any]) -> dict[str, Tuple[str, str]]:
    """
    Transform inbound config data, providing defaults values where not provided.
    """
    config_platform_translations = (
        data.get("platform_specific_translations", {})
    )

    # Check that `config_platform_translations` is a dict[str, list[str]]
    if (
        isinstance(config_platform_translations, dict)
        and all(
            isinstance(outline_translation, str)
            and isinstance(resolved_translation, list)
            and all(isinstance(item, str) for item in resolved_translation)
            for outline_translation, resolved_translation
            in config_platform_translations.items()
        )
    ):
        # Transform the dict[str, list[str]] to a dict[str, Tuple[str, str]]
        return {
            outline_translation: tuple(resolved_translation)
            for outline_translation, resolved_translation
            in config_platform_translations.items()
        }

    raise ValueError(
        "'platform_specific_translations' must be a dict containing "
        "lists of strings."
    )

def transform_outbound(
    platform_translations: dict[str, Tuple[str, str]]
) -> dict[str, dict[str, Tuple[str, str]]]:
    """
    Transform platform translations into outbound config data.
    """
    return {
        "platform_specific_translations": platform_translations
    }
