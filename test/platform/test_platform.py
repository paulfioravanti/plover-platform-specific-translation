import pytest

from plover_platform_specific_translation import platform

def test_windows_mapping(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    assert platform.parse() == "WINDOWS"

def test_mac_mapping(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Darwin")
    assert platform.parse() == "MAC"

def test_linux_mapping(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Linux")
    assert platform.parse() == "LINUX"

# platform.system() supports "Java", but it's ignored in this plugin.
def test_java_mapping(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Java")
    assert platform.parse() == "OTHER"

def test_unknown_mapping(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "")
    assert platform.parse() == "OTHER"
