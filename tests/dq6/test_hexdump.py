"""
Tests for dquils.snescpu.hexdump.
"""

import re

import pytest
from snescpu.test_hexdump import ADDRESS_PATTERN

from dqutils.snescpu.hexdump import dump

from .. import requires_config
from .conftest import GAME_TITLE

pytestmark = requires_config


def test_dump_simple(capsys):
    """Test function `dump`."""
    dump(GAME_TITLE, ["C0FFC0", "16", "4"])
    lines = capsys.readouterr().out.split("\n")

    assert lines[0].startswith("C0/FFC0:")
    assert lines[1].startswith("C0/FFD0:")

    for line in lines[:-1]:
        assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{32}$", line)
    assert lines[-1] == ""


def test_dump_bank_boundary(capsys):
    """Test function `dump`."""
    # about to be across the bank boundary
    dump(GAME_TITLE, ["C0FFC0", "12", "6"])
    lines = capsys.readouterr().out.split("\n")

    assert lines[0].startswith("C0/FFC0:")
    assert lines[1].startswith("C0/FFCC:")

    for line in lines[:-2]:
        assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{24}$", line)

    assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{8}$", lines[-2])
    assert lines[-1] == ""


@pytest.mark.parametrize(
    "dump_args",
    (
        ("C0FFC0", "0", "0"),
        ("C0FFC0", "1", "0"),
        ("C0FFC0", "0", "1"),
    ),
)
def test_dump_zero_input(capsys, dump_args):
    """Test the case where zeros are passed to `dump`."""
    dump(GAME_TITLE, dump_args)
    lines = capsys.readouterr().out.split("\n")
    assert len(lines) == 1
    assert lines[-1] == ""


def test_dump_nonuniform(capsys):
    """Test nonuniform hexdump."""

    dump(GAME_TITLE, "C316DD 1 2 3 2 1".split())
    # fmt: off
    expected = (
        "C3/16DD:\t00\n"
        "C3/16DE:\t2000\n"
        "C3/16E0:\tB4387E\n"
        "C3/16E3:\t1600\n"
        ""
    )
    # fmt: on
    assert capsys.readouterr().out == expected
