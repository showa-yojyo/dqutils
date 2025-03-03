"""Test functions defined in dqutils.mapper for LoROM."""

import pytest

from dqutils.snescpu.mapper import LoROM, make_mapper


def test_make_mapper():
    """Test function dqutils.mapper.make_mapper for LoROM."""
    assert make_mapper(name="LoROM") == LoROM


@pytest.mark.parametrize(
    "input,expected",
    (
        (0x000000, 0x008000),
        (0x008000, 0x018000),
        (0x010000, 0x028000),
        (0x018000, 0x038000),
        (0x1F0000, 0x3E8000),
        (0x1F8000, 0x3F8000),
    ),
)
def test_from_rom(input, expected):
    """Test method dqutils.mapper.LoROM.from_rom."""
    assert LoROM.from_rom(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        (0x008000, 0x000000),
        (0x018000, 0x008000),
        (0x028000, 0x010000),
        (0x038000, 0x018000),
        # ...
        (0x3E8000, 0x1F0000),
        (0x3F8000, 0x1F8000),
    ),
)
def test_from_cpu(input, expected):
    """Test method dqutils.mapper.LoROM.from_cpu."""
    assert LoROM.from_cpu(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        (0x008000, 0x008001),
        (0x00FFFF, 0x018000),
    ),
)
def test_increment_address(input, expected):
    """Test method dqutils.mapper.LoROM.increment_address."""
    assert LoROM.increment_address(input) == expected


def test_bank_offset_size():
    """Test property dqutils.mapper.LoROM.bank_offset_size."""
    assert LoROM.bank_offset_size == 0x8000
