"""Test functions defined in dqutils.mapper for LoROM."""

from dqutils.snescpu.mapper import LoROM, make_mapper


def test_make_mapper():
    """Test function dqutils.mapper.make_mapper for LoROM."""
    assert make_mapper(name="LoROM") == LoROM


def test_from_rom():
    """Test method dqutils.mapper.LoROM.from_rom."""
    assert LoROM.from_rom(0x000000) == 0x008000
    assert LoROM.from_rom(0x008000) == 0x018000
    assert LoROM.from_rom(0x010000) == 0x028000
    assert LoROM.from_rom(0x018000) == 0x038000
    assert LoROM.from_rom(0x1F0000) == 0x3E8000
    assert LoROM.from_rom(0x1F8000) == 0x3F8000


def test_from_cpu():
    """Test method dqutils.mapper.LoROM.from_cpu."""
    assert LoROM.from_cpu(0x008000) == 0x000000
    assert LoROM.from_cpu(0x018000) == 0x008000
    assert LoROM.from_cpu(0x028000) == 0x010000
    assert LoROM.from_cpu(0x038000) == 0x018000
    # ...
    assert LoROM.from_cpu(0x3E8000) == 0x1F0000
    assert LoROM.from_cpu(0x3F8000) == 0x1F8000


def test_increment_address():
    """Test method dqutils.mapper.HiROM.increment_address."""
    assert LoROM.increment_address(0x008000) == 0x008001
    assert LoROM.increment_address(0x00FFFF) == 0x018000


def test_bank_offset_size():
    """Test property dqutils.mapper.HiROM.bank_offset_size."""
    assert LoROM.bank_offset_size == 0x8000
