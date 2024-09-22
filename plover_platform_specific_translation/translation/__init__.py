"""
# Translation

A package dealing with:
    - resolving the correct translation from a platform-specific outline value
"""

__all__ = [
    "COMBO",
    "COMMAND",
    "resolve"
]

from .resolver import (
    COMBO,
    COMMAND,
    resolve
)
