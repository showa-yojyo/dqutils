"""Tests for dqutils.dq3.string"""

from dqutils.dq3.string import CONTEXT, enum_string
from dqutils.string import get_text


def test_get_text():
    """Test function dqutils.dq3.get_text."""
    text = get_text(
        b"\x26\x24\x12\x24\xdc\x0e\xac",
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
    assert "ひのきのぼう" in text


def test_enum_string():
    """Test function dqutils.dq3.enum_string."""
    testdata = tuple(enum_string(0x100, 0x110))

    assert testdata[0][0] == 0xFED659
    assert "せいすい" in get_text(
        testdata[0][1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )

    assert testdata[15][0] == 0xFED6CA
    assert "にじのしずく" in get_text(
        testdata[15][1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
