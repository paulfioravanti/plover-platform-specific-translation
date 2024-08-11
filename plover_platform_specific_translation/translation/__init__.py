"""
# Translation

A package dealing with:
    - resolving the correct translation from a platform-specific outline value
"""
from .resolver import (
    COMBO,
    COMMAND,
    resolve
)

__all__ = [
    "COMBO",
    "COMMAND",
    "resolve"
]
