"""
# Config

A package dealing with:
    - loading and saving config containing platform-specific outline values
"""
from .actions import (
    load,
    save
)
from .file import CONFIG_BASENAME

__all__ = [
    "CONFIG_BASENAME",
    "load",
    "save"
]
