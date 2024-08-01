import pytest

from plover_platform_specific_translation import translation


# Fixtures

@pytest.fixture
def all_platforms():
    return (
        "WINDOWS:Windows value"
        ":MAC:Mac value"
        ":LINUX:Linux value"
        ":OTHER:Default value"
    )

@pytest.fixture
def some_platforms_with_fallback():
    return "MAC:Mac value:OTHER:Default value"

@pytest.fixture
def some_platforms_without_fallback():
    return "WINDOWS:Windows value:MAC:Mac value"

@pytest.fixture
def fallback_platform_only():
    return "OTHER:Default value"

# Tests

def test_platform_given_in_non_uppercase():
    outline_translation = "Windows:{#CONTROL(C)}"
    platform_translation = translation.resolve("WINDOWS", outline_translation)
    assert platform_translation == "{#CONTROL(C)}"

def test_all_platforms_translation_with_windows(all_platforms):
    assert translation.resolve("WINDOWS", all_platforms) == "Windows value"

def test_all_platforms_translation_with_mac(all_platforms):
    assert translation.resolve("MAC", all_platforms) == "Mac value"

def test_all_platforms_translation_with_linux(all_platforms):
    assert translation.resolve("LINUX", all_platforms) == "Linux value"

def test_all_platforms_translation_with_default(all_platforms):
    assert translation.resolve("OTHER", all_platforms) == "Default value"

def test_some_platforms_translation_with_fallback(some_platforms_with_fallback):
    assert (
        translation.resolve("WINDOWS", some_platforms_with_fallback)
        == "Default value"
    )

def test_some_platforms_translation_without_fallback(
    some_platforms_without_fallback
):
    with pytest.raises(
        ValueError,
        match="No translation provided for platform: LINUX"
    ):
        translation.resolve("LINUX", some_platforms_without_fallback)

def test_only_fallback_platform_translation_given(fallback_platform_only):
    assert (
        translation.resolve("WINDOWS", fallback_platform_only)
        == "Default value"
    )
