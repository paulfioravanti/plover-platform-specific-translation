import json
from pathlib import Path
import pytest


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
def dict_non_list_platform_translations_config_path():
    return (
        Path(__file__).parent / "files/dict_non_list_platform_translations.json"
    ).resolve()

@pytest.fixture
def dict_list_non_string_platform_translations_config_path():
    return (
        Path(__file__).parent
        / "files/dict_list_non_string_platform_translations.json"
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
