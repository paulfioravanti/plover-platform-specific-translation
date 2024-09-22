import pytest

from plover_platform_specific_translation import translation


def test_all_platforms_text_translation_with_windows(all_platforms_text):
    assert (
        translation.resolve("WINDOWS", all_platforms_text)
        == ("text", "Windows value")
    )

def test_all_platforms_text_translation_with_mac(all_platforms_text):
    assert (
        translation.resolve("MAC", all_platforms_text)
        == ("text", "Mac value")
    )

def test_all_platforms_text_translation_with_linux(all_platforms_text):
    assert (
        translation.resolve("LINUX", all_platforms_text)
        == ("text", "Linux value")
    )

def test_all_platforms_text_translation_with_default(all_platforms_text):
    assert (
        translation.resolve("OTHER", all_platforms_text)
        == ("text", "Default value")
    )

def test_all_platforms_combo_translation_with_windows(all_platforms_combo):
    assert (
        translation.resolve("WINDOWS", all_platforms_combo)
        == ("combo", "CONTROL(C)")
    )

def test_all_platforms_combo_translation_with_mac(all_platforms_combo):
    assert (
        translation.resolve("MAC", all_platforms_combo)
        == ("combo", "SUPER(C)")
    )

def test_all_platforms_combo_translation_with_linux(all_platforms_combo):
    assert (
        translation.resolve("LINUX", all_platforms_combo)
        == ("combo", "SHIFT(CONTROL(C))")
    )

def test_all_platforms_combo_translation_with_default(all_platforms_combo):
    assert (
        translation.resolve("OTHER", all_platforms_combo)
        == ("combo", "ALT(CONTROL(C))")
    )

def test_all_platforms_command_translation_with_windows(all_platforms_command):
    assert (
        translation.resolve("WINDOWS", all_platforms_command)
        == ("command", "SOLO_DICT:-commands.md")
    )

def test_all_platforms_command_translation_with_mac(all_platforms_command):
    assert (
        translation.resolve("MAC", all_platforms_command)
        == ("command", "APPLESCRIPT:/path/to/script.scpt")
    )

def test_all_platforms_command_translation_with_linux(all_platforms_command):
    assert (
        translation.resolve("LINUX", all_platforms_command)
        == ("command", "TOGGLE_DICT:+some_dict.py")
    )

def test_all_platforms_command_translation_with_default(all_platforms_command):
    assert (
        translation.resolve("OTHER", all_platforms_command)
        == ("command", "TOGGLE_DICT:~some_dict.py")
    )

def test_some_platforms_text_translation_with_fallback(
    some_platforms_with_fallback_text
):
    assert (
        translation.resolve("WINDOWS", some_platforms_with_fallback_text)
        == ("text", "Default value")
    )

def test_some_platforms_text_translation_without_fallback(
    some_platforms_without_fallback_text
):
    with pytest.raises(
        ValueError,
        match="No translation provided for platform: LINUX"
    ):
        translation.resolve("LINUX", some_platforms_without_fallback_text)

def test_only_fallback_platform_text_translation_given(
    fallback_platform_only_text
):
    assert (
        translation.resolve("WINDOWS", fallback_platform_only_text)
        == ("text", "Default value")
    )

def test_platform_text_translation_given_in_non_uppercase():
    outline_translation = "Windows:Windows value"
    platform_translation = translation.resolve("WINDOWS", outline_translation)
    assert platform_translation == ("text", "Windows value")
