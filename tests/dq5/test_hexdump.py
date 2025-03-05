"""
Tests for dquils.snescpu.hexdump.
"""

import re

from snescpu.test_hexdump import ADDRESS_PATTERN

from dqutils.snescpu.hexdump import dump

from .. import requires_config
from .conftest import GAME_TITLE


@requires_config
def test_dump(capsys):
    """Test function `dump`."""

    dump(GAME_TITLE, "238000 25 235".split())
    lines = capsys.readouterr().out.split("\n")

    assert lines[0].startswith("23/8000:")
    assert lines[0].endswith("A102")
    assert lines[1].startswith("23/8019:")
    assert lines[1].endswith("A100")

    for line in lines[:-1]:
        assert re.match(ADDRESS_PATTERN + r"\t[0-9A-F]{50}$", line)
    assert lines[-1] == ""
