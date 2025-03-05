"""
Tests for dqutils.snescpu.addressing.
"""

import pytest

from dqutils.snescpu.addressing import ADDRESSING_MODE_TABLE, get_addressing_mode


@pytest.mark.parametrize("name", (["Immediate", " Absolute Long   "]))
def test_basic(name):
    """Test basic behaviors of get_addressing_mode."""

    assert get_addressing_mode(name)


@pytest.mark.parametrize("name", ("XYZ"))
def test_invalid_args(name):
    """Test get_addressing_mode for invalid arguments."""

    with pytest.raises(KeyError, match=name):
        get_addressing_mode(name)


@pytest.mark.parametrize("mode", ADDRESSING_MODE_TABLE)
def test_properties(mode):
    """Test AbstractAddressingMode for its properties."""

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
