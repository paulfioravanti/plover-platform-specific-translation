"""
Module to handle reading and writing to JSON
"""
import json
from pathlib import Path
from typing import Any


def load(filepath: Path) -> dict[str, Any]:
    """
    Reads in data from a JSON file

    Raises an error if the specified config file is not JSON format.
    """
    data: dict[str, Any]
    try:
        with filepath.open(encoding="utf-8") as file:
            data = json.load(file)
            file.close()
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError as exc:
        raise ValueError("Unable to decode file contents as JSON") from exc

    return data

def save(filepath: Path, data: dict[str, Any]) -> None:
    """
    Saves a dictionary to a JSON file.
    """
    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.close()
