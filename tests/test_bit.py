"""Tests for dqutils.bit module."""

from dqutils.bit import get_bits, get_int


def test_get_int():
    """Test function dqutils.bit.get_int."""

    targets = (
        (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06),
        b"\x00\x01\x02\x03\x04\x05\x06",
    )

    for data in targets:
        assert get_int(data, 0, 1) == 0x00
        assert get_int(data, 1, 1) == 0x01
        assert get_int(data, 0, 2) == 0x0100
        assert get_int(data, 6, 2) == 0x0006
        assert get_int(data, 0, 3) == 0x020100
        assert get_int(data, 5, 3) == 0x000605
        assert get_int(data, 6, 3) == 0x000006


def test_get_int_empty():
    """Test function dqutils.bit.get_int in case of empty value is passed."""
    assert get_int(b"", 6, 3) == 0
    assert get_int([], 6, 3) == 0


def test_get_bits():
    """Test function dqutils.bit.get_bits."""
    data = tuple(range(0x06))
    assert get_bits(data, 0, 0xFF00) == 0x0001
    assert get_bits(data, 1, 0xFFFF) == 0x0201
    assert get_bits(data, 0, 0x0100) == 0x0001
