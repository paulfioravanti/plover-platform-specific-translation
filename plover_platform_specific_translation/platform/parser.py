"""
Module to handle parsing a platform.system() value into an operating system
value compatible with a platform-specific translation that can be contained in
an outline.
"""
import platform


_PLATFORM_MAPPINGS: dict[str, str] = {
    "Windows": "WINDOWS",
    "Darwin": "MAC",
    "Linux": "LINUX"
}

def parse() -> str:
    """
    Parse platform.system() value into a known platform mapping.
    """
    return _PLATFORM_MAPPINGS.get(platform.system(), "OTHER")
