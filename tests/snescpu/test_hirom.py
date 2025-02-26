"""Test functions defined in dqutils.mapper for HiROM."""

from dqutils.snescpu.mapper import HiROM, make_mapper


def test_make_mapper():
    """Test function dqutils.mapper.make_mapper for HiROM."""
    assert make_mapper(name="HiROM") == HiROM


def test_from_rom():
    """Test method dqutils.mapper.HiROM.from_rom."""
    assert HiROM.from_rom(0x020000) == 0xC20000


def test_from_cpu():
    """Test method dqutils.mapper.HiROM.from_cpu."""
    # SlowROM
    assert HiROM.from_cpu(0x408000) == 0x008000
    assert HiROM.from_cpu(0x418000) == 0x018000
    assert HiROM.from_cpu(0x428000) == 0x028000
    assert HiROM.from_cpu(0x438000) == 0x038000
    # ...
    assert HiROM.from_cpu(0x7E8000) == 0x3E8000
    assert HiROM.from_cpu(0x7F8000) == 0x3F8000

    # FastROM
    assert HiROM.from_cpu(0xC08000) == 0x008000
    assert HiROM.from_cpu(0xC18000) == 0x018000
    assert HiROM.from_cpu(0xC28000) == 0x028000
    assert HiROM.from_cpu(0xC38000) == 0x038000
    # ...
    assert HiROM.from_cpu(0xFE8000) == 0x3E8000
    assert HiROM.from_cpu(0xFF8000) == 0x3F8000


def test_increment_address():
    """Test method dqutils.mapper.HiROM.increment_address."""
    assert HiROM.increment_address(0xC00000) == 0xC00001
    assert HiROM.increment_address(0xC07FFF) == 0xC08000
    assert HiROM.increment_address(0xC08000) == 0xC08001
    assert HiROM.increment_address(0xC0FFFF) == 0xC10000


def test_bank_offset_size():
    """Test property dqutils.mapper.HiROM.bank_offset_size."""
    assert HiROM.bank_offset_size == 0x10000
