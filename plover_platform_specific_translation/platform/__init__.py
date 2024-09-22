"""
# Platform

A package dealing with:
    - Determining the current platform Plover is running in
    - Returning a value back that will match valid operating system values that
      can be contained in a platform-specific translation
"""

__all__ = [
    "parse"
]

from .parser import parse
