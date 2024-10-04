import json
from pathlib import Path
import pytest


@pytest.fixture
def bad_config_path():
    return _path("files/bad_json_data.json")

@pytest.fixture
def non_existent_config_path():
    return _path("files/non_existent.json")

@pytest.fixture
def non_dict_platform_translations_config_path():
    return _path("files/non_dict_platform_translations.json")

@pytest.fixture
def dict_non_list_platform_translations_config_path():
    return _path("files/dict_non_list_platform_translations.json")

@pytest.fixture
def dict_list_non_string_platform_translations_config_path():
    return _path("files/dict_list_non_string_platform_translations.json")

@pytest.fixture
def valid_platform_translations_config_path():
    path = _path("files/valid_platform_translations.json")
    with path.open(encoding="utf-8") as file:
        config_data = json.load(file)
        file.close()

    yield path

    with path.open("w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=2)
        file.close()

def _path(path):
    return (Path(__file__).parent / path).resolve()
