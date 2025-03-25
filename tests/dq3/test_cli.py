"""
Tests for dqutils.dq3.main
"""

import sys

import pytest

from dqutils.dq3 import main

from ..test_cli import PROG_NAME


@pytest.mark.parametrize("args", [(), ("--help",)])
def test_cli(monkeypatch, capsys, args):
    with monkeypatch.context():
        monkeypatch.setattr(sys, "argv", [PROG_NAME, *args])
        with pytest.raises(SystemExit) as ei:
            main()
        assert ei.value.code == 0
        assert "usage" in capsys.readouterr().out
