"""
Tests for dquils.snescpu.hexdump.
"""

import re

from snescpu.test_hexdump import ADDRESS_PATTERN

from dqutils.snescpu.hexdump import dump

GAME_TITLE = "DRAGONQUEST5"


def test_dump(capture_stdout):
    """Test function `dump`."""

    dump(GAME_TITLE, "238000 25 235".split())
    lines = capture_stdout.getvalue().split("\n")

    assert lines[0].startswith("23/8000:")
    assert lines[0].endswith("A102")
    assert lines[1].startswith("23/8019:")
    assert lines[1].endswith("A100")

    for line in lines[:-1]:
        assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{50}$", line)
    assert lines[-1] == ""
