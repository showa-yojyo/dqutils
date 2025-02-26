"""
Tests for dqutils.snescpu.addressing.
"""

import pytest

from dqutils.snescpu.addressing import ADDRESSING_MODE_TABLE, get_addressing_mode


def test_basic():
    """Test basic behaviors of get_addressing_mode."""

    addrmode = get_addressing_mode("Immediate")
    assert addrmode

    # Intentionally add extra space characters.
    addrmode = get_addressing_mode(" Absolute Long   ")
    assert addrmode


def test_invalid_args():
    """Test get_addressing_mode for invalid arguments."""

    invalid_arg = "XYZ"
    with pytest.raises(KeyError, match=invalid_arg):
        get_addressing_mode(invalid_arg)


def test_properties():
    """Test AbstractAddressingMode for its properties."""

    for mode in ADDRESSING_MODE_TABLE:
        name, syntax, formatter = mode

        addrmode = get_addressing_mode(name)
        assert addrmode is not None
        assert addrmode.name == name.strip()
        assert addrmode.syntax == syntax.strip()

        if formatter:
            assert addrmode.formatter.__name__ == formatter.__name__
        else:
            assert addrmode.formatter is None
            assert addrmode.formatter is None
