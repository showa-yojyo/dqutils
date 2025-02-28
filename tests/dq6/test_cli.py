"""
Tests for dqutils.dq6.main
"""

import sys

import pytest

from dqutils.dq6 import main

from ..test_cli import PROG_NAME


@pytest.mark.parametrize("args", [(), ("--help",)])
def test_cli(monkeypatch, capture_stdout, args):
    with pytest.raises(SystemExit) as ei, monkeypatch.context():
        monkeypatch.setattr(sys, "argv", [PROG_NAME, *args])
        main()
    assert ei.value.code == 0
    assert "usage" in capture_stdout.getvalue()
