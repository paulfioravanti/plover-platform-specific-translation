import pytest


@pytest.fixture
def all_platforms_text():
    return (
        "WINDOWS:Windows value"
        ":MAC:Mac value"
        ":LINUX:Linux value"
        ":OTHER:Default value"
    )

@pytest.fixture
def all_platforms_combo():
    return (
        "WINDOWS:#CONTROL(C)"
        ":MAC:#SUPER(C)"
        ":LINUX:#SHIFT(CONTROL(C))"
        ":OTHER:#ALT(CONTROL(C))"
    )

@pytest.fixture
def all_platforms_command():
    return (
        "WINDOWS::COMMAND:SOLO_DICT:-commands.md"
        ":MAC::COMMAND:APPLESCRIPT:/path/to/script.scpt"
        ":LINUX:PLOVER:TOGGLE_DICT:+some_dict.py"
        ":OTHER::COMMAND:TOGGLE_DICT:~some_dict.py"
    )

@pytest.fixture
def some_platforms_with_fallback_text():
    return "MAC:Mac value:OTHER:Default value"

@pytest.fixture
def some_platforms_without_fallback_text():
    return "WINDOWS:Windows value:MAC:Mac value"

@pytest.fixture
def fallback_platform_only_text():
    return "OTHER:Default value"
