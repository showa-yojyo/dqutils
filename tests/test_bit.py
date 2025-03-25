"""Tests for dqutils.bit module."""

import pytest

from dqutils.bit import get_bits, get_int


@pytest.mark.parametrize(
    "data",
    [
        (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06),
        b"\x00\x01\x02\x03\x04\x05\x06",
    ],
)
@pytest.mark.parametrize(
    ("index", "length", "expected"),
    [
        (0, 1, 0x00),
        (1, 1, 0x01),
        (0, 2, 0x0100),
        (6, 2, 0x0006),
        (0, 3, 0x020100),
        (5, 3, 0x000605),
        (6, 3, 0x000006),
    ],
)
def test_get_int(data, index, length, expected):
    """Test function dqutils.bit.get_int."""
    assert get_int(data, index, length) == expected


@pytest.mark.parametrize("seq", [b"", []])
def test_get_int_empty(seq):
    """Test function dqutils.bit.get_int in case of empty value is passed."""
    assert get_int(seq, 6, 3) == 0


@pytest.mark.parametrize(
    ("index", "mask", "expected"),
    [
        (0, 0xFF00, 0x0001),
        (1, 0xFFFF, 0x0201),
        (0, 0x0100, 0x0001),
    ],
)
def test_get_bits(index, mask, expected):
    """Test function dqutils.bit.get_bits."""
    data = tuple(range(0x06))
    assert get_bits(data, index, mask) == expected
