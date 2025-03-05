"""Tests for dqutils.config"""

import os
from pathlib import Path

import pytest

from dqutils.config import ConfigNotFoundError, confdir_home

from . import requires_config


# @pytest.mark.skipif(get_config() is None, reason="No configuration provided")
@requires_config
def test_confdir_home():
    actual = confdir_home()
    assert actual.is_dir()
    assert actual.as_posix().endswith("dqutils")


@pytest.mark.xfail(raises=ConfigNotFoundError)
def test_confdir_home_error(monkeypatch):
    with monkeypatch.context():
        monkeypatch.setattr(os.environ, "get", lambda _: "")
        monkeypatch.setattr(Path, "home", lambda: Path("/dev/null"))
        confdir_home()
