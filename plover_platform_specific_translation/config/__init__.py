"""
# Config

A package dealing with:
    - loading and saving config containing platform-specific outline values
"""

__all__ = [
    "CONFIG_BASENAME",
    "load",
    "save"
]

from .loader import (
    load,
    save
)


CONFIG_BASENAME: str = "platform_specific_translation.json"
