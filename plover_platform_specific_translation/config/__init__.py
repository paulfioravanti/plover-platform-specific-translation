"""
# Config

A package dealing with:
    - loading and saving config containing platform-specific outline values
"""
from .loader import (
    load,
    save
)


__all__ = [
    "CONFIG_BASENAME",
    "load",
    "save"
]

CONFIG_BASENAME: str = "platform_specific_translation.json"
