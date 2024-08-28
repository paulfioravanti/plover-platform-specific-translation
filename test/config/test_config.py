import json
from pathlib import Path
import pytest

from plover_platform_specific_translation import config

# Files

@pytest.fixture
def bad_config_path():
    return (Path(__file__).parent / "files/bad_json_data.json").resolve()

@pytest.fixture
def non_existent_config_path():
    return (Path(__file__).parent / "files/non_existent.json").resolve()

@pytest.fixture
def non_dict_platform_translations_config_path():
    return (
        Path(__file__).parent / "files/non_dict_platform_translations.json"
    ).resolve()

@pytest.fixture
def valid_platform_translations_config_path():
    path = (
        Path(__file__).parent / "files/valid_platform_translations.json"
    ).resolve()
    with path.open(encoding="utf-8") as file:
        config_data = json.load(file)
        file.close()

    yield path

    with path.open("w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=2)
        file.close()

# Tests

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
        match="'platform_specific_translations' must be a dict"
    ):
        config.load(non_dict_platform_translations_config_path)

def test_loading_valid_config(valid_platform_translations_config_path):
    config_platform_translations = (
        config.load(valid_platform_translations_config_path)
    )

    assert (
        config_platform_translations[
            "WINDOWS:Hello:MAC:Hi:LINUX:Good day:OTHER:Whassup"
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
