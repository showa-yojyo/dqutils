"""
Tests for dquils.snescpu.hexdump
"""

import re

from snescpu.test_hexdump import ADDRESS_PATTERN

from dqutils.snescpu.hexdump import dump

from .conftest import GAME_TITLE


def test_dump(capture_stdout):
    """Test function `dump`."""
    dump(GAME_TITLE, ["C808DA", "12", "1389"])
    lines = capture_stdout.getvalue().split("\n")

    assert lines[0].startswith("C8/08DA:")
    assert lines[1].startswith("C8/08E6:")

    for line in lines[:-1]:
        assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{24}$", line)
    assert lines[-1] == ""
