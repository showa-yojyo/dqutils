"""Test functions defined in dqutils.mapper for HiROM."""

import pytest

from dqutils.snescpu.mapper import HiROM, make_mapper


def test_make_mapper():
    """Test function dqutils.mapper.make_mapper for HiROM."""
    assert make_mapper(name="HiROM") == HiROM


def test_from_rom():
    """Test method dqutils.mapper.HiROM.from_rom."""
    assert HiROM.from_rom(0x020000) == 0xC20000


@pytest.mark.parametrize(
    "input,expected",
    (
        # SlowROM
        (0x408000, 0x008000),
        (0x418000, 0x018000),
        (0x428000, 0x028000),
        (0x438000, 0x038000),
        # ...
        (0x7E8000, 0x3E8000),
        (0x7F8000, 0x3F8000),
        # FastROM
        (0xC08000, 0x008000),
        (0xC18000, 0x018000),
        (0xC28000, 0x028000),
        (0xC38000, 0x038000),
        # ...
        (0xFE8000, 0x3E8000),
        (0xFF8000, 0x3F8000),
    ),
)
def test_from_cpu(input, expected):
    """Test method dqutils.mapper.HiROM.from_cpu."""
    assert HiROM.from_cpu(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        (0xC00000, 0xC00001),
        (0xC07FFF, 0xC08000),
        (0xC08000, 0xC08001),
        (0xC0FFFF, 0xC10000),
    ),
)
def test_increment_address(input, expected):
    """Test method dqutils.mapper.HiROM.increment_address."""
    assert HiROM.increment_address(input) == expected


def test_bank_offset_size():
    """Test property dqutils.mapper.HiROM.bank_offset_size."""
    assert HiROM.bank_offset_size == 0x10000
