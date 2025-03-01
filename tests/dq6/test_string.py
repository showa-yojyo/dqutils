"""Tests for dqutils.dq6.string"""

from dqutils.dq6.string import CONTEXT, enum_string
from dqutils.string import get_text


def test_get_text():
    """Test function dqutils.dq6.get_text."""
    text = get_text(
        b"\x2a\x28\x16\x28\xdc\x12\xac",
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
    assert "ひのきのぼう" in text


def test_enum_string():
    """Test function dqutils.dq6.enum_string."""
    testdata = tuple(enum_string(0x300, 0x310))

    assert testdata[0][0] == 0xFB97DB
    assert "ムドー" in get_text(
        testdata[0][1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )

    assert testdata[15][0] == 0xFB9835
    assert "デュラン" in get_text(
        testdata[15][1],
        CONTEXT["charmap"],
        CONTEXT["delimiters"],
    )
