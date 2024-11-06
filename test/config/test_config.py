import pytest

from plover_platform_specific_translation import config


def test_loading_bad_config(bad_config_path):
    with pytest.raises(
        ValueError,
        match="Unable to decode file contents as JSON"
    ):
        config.load(bad_config_path)

def test_loading_non_existent_config(non_existent_config_path):
    loaded_config = config.load(non_existent_config_path)
    assert loaded_config == {}

def test_loading_config_with_non_dict_platform_translations(
    non_dict_platform_translations_config_path
):
    with pytest.raises(
        ValueError,
        match=(
            "'platform_specific_translations' must be a dict containing "
            "lists of strings."
        )
    ):
        config.load(non_dict_platform_translations_config_path)

def test_loading_config_with_dict_non_list_platform_translations(
    dict_non_list_platform_translations_config_path
):
    with pytest.raises(
        ValueError,
        match=(
            "'platform_specific_translations' must be a dict containing "
            "lists of strings."
        )
    ):
        config.load(dict_non_list_platform_translations_config_path)

def test_loading_config_with_dict_list_non_string_platform_translations(
    dict_list_non_string_platform_translations_config_path
):
    with pytest.raises(
        ValueError,
        match=(
            "'platform_specific_translations' must be a dict containing "
            "lists of strings."
        )
    ):
        config.load(dict_list_non_string_platform_translations_config_path)

def test_loading_valid_config(valid_platform_translations_config_path):
    config_platform_translations = (
        config.load(valid_platform_translations_config_path)
    )

    assert (
        config_platform_translations[
            "WINDOWS:Hello,MAC:Hi,LINUX:Good day,OTHER:Whassup"
        ]
        == ("text", "Hi")
    )

def test_saving_config(valid_platform_translations_config_path):
    platform_translations = {"foo": ("text", "bar")}
    config.save(
        valid_platform_translations_config_path,
        platform_translations
    )
    config_platform_translations = (
        config.load(valid_platform_translations_config_path)
    )

    assert config_platform_translations == platform_translations
