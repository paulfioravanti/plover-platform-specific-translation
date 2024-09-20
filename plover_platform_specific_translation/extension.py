"""
Plover entry point extension module for Plover Platform Specific Translation

    - https://plover.readthedocs.io/en/latest/plugin-dev/extensions.html
    - https://plover.readthedocs.io/en/latest/plugin-dev/meta.html
"""
from pathlib import Path
from typing import Tuple

from plover.engine import StenoEngine
from plover.formatting import (
    _Action,
    _Context
)
from plover.machine.base import STATE_RUNNING
from plover.oslayer.config import CONFIG_DIR
from plover.registry import registry

from . import (
    config,
    platform,
    translation
)


_CONFIG_FILE: Path = Path(CONFIG_DIR) / config.CONFIG_BASENAME

class PlatformSpecificTranslation:
    """
    Extension class that also registers a meta plugin.
    The meta deals with determining the appropriate outline translation
    based on the current platform.
    """
    _engine: StenoEngine
    _platform: str
    _platform_translations: dict[str, Tuple[str, str]]

    def __init__(self, engine: StenoEngine) -> None:
        self._engine = engine

    def start(self) -> None:
        """
        Sets up the meta plugin, steno engine hooks, and information to cache
        """
        self._platform = platform.parse()
        self._platform_translations = config.load(_CONFIG_FILE)
        registry.register_plugin(
            "meta",
            "PLATFORM",
            self._platform_specific_translation
        )
        self._engine.hook_connect(
            "machine_state_changed",
            self._machine_state_changed
        )

    def stop(self) -> None:
        """
        Tears down the steno engine hooks
        """
        self._engine.hook_disconnect(
            "machine_state_changed",
            self._machine_state_changed
        )

    def _platform_specific_translation(
        self,
        ctx: _Context,
        argument: str
    ) -> _Action:
        """
        Resolves a platform-specific translation and stores it in memory for
        faster execution on subsequent calls.
        """
        if not argument:
            raise ValueError("No platform-specific translations provided")

        platform_translation: str
        platform_translation_type: str
        try:
            platform_translation_type, platform_translation = (
                self._platform_translations[argument]
            )
        except KeyError:
            platform_translation_type, platform_translation = (
                translation.resolve(self._platform, argument)
            )
            self._platform_translations[argument] = (
                (platform_translation_type, platform_translation)
            )
            config.save(_CONFIG_FILE, self._platform_translations)

        action: _Action = ctx.new_action()

        if platform_translation_type == translation.COMBO:
            action.combo = platform_translation
        elif platform_translation_type == translation.COMMAND:
            action.command = platform_translation
        else:
            action.text = platform_translation

        return action

    def _machine_state_changed(
        self,
        _machine_type: str,
        machine_state: str
    ) -> None:
        """
        This hook will be called when when the Plover UI "Reconnect" button is
        pressed. Resetting the `self._platform_translations` dictionary
        allows for changes made to translations to be re-read in.
        """
        if machine_state == STATE_RUNNING:
            self._platform_translations = config.load(_CONFIG_FILE)
