"""
Tests for dqutils.mapper module.
"""

import unittest

from dqutils.snescpu.mapper import HiROM, LoROM, make_mapper


# pylint: disable=too-many-public-methods
class HiROMTestCase(unittest.TestCase):
    """Test functions defined in dqutils.mapper."""

    mapper = HiROM

    def test_make_mapper(self):
        """Test function dqutils.mapper.make_mapper for HiROM."""
        self.assertEqual(make_mapper(name="HiROM"), self.mapper)

    def test_from_rom(self):
        """Test method dqutils.mapper.HiROM.from_rom."""

        mapper = self.mapper
        self.assertEqual(mapper.from_rom(0x020000), 0xC20000)

    def test_from_cpu(self):
        """Test method dqutils.mapper.HiROM.from_cpu."""

        mapper = self.mapper

        # SlowROM

        self.assertEqual(mapper.from_cpu(0x408000), 0x008000)
        self.assertEqual(mapper.from_cpu(0x418000), 0x018000)
        self.assertEqual(mapper.from_cpu(0x428000), 0x028000)
        self.assertEqual(mapper.from_cpu(0x438000), 0x038000)
        # ...
        self.assertEqual(mapper.from_cpu(0x7E8000), 0x3E8000)
        self.assertEqual(mapper.from_cpu(0x7F8000), 0x3F8000)

        # FastROM

        self.assertEqual(mapper.from_cpu(0xC08000), 0x008000)
        self.assertEqual(mapper.from_cpu(0xC18000), 0x018000)
        self.assertEqual(mapper.from_cpu(0xC28000), 0x028000)
        self.assertEqual(mapper.from_cpu(0xC38000), 0x038000)
        # ...
        self.assertEqual(mapper.from_cpu(0xFE8000), 0x3E8000)
        self.assertEqual(mapper.from_cpu(0xFF8000), 0x3F8000)

    def test_increment_address(self):
        """Test method dqutils.mapper.HiROM.increment_address."""

        mapper = self.mapper
        self.assertEqual(mapper.increment_address(0xC00000), 0xC00001)
        self.assertEqual(mapper.increment_address(0xC07FFF), 0xC08000)
        self.assertEqual(mapper.increment_address(0xC08000), 0xC08001)
        self.assertEqual(mapper.increment_address(0xC0FFFF), 0xC10000)

    def test_bank_offset_size(self):
        """Test property dqutils.mapper.HiROM.bank_offset_size."""
        self.assertEqual(self.mapper.bank_offset_size, 0x10000)


class LoROMTestCase(unittest.TestCase):
    """Test functions defined in dqutils.mapper."""

    mapper = LoROM

    def test_make_mapper(self):
        """Test function dqutils.mapper.make_mapper for LoROM."""
        self.assertEqual(make_mapper(name="LoROM"), self.mapper)

    def test_from_rom(self):
        """Test method dqutils.mapper.LoROM.from_rom."""

        mapper = self.mapper

        self.assertEqual(mapper.from_rom(0x000000), 0x008000)
        self.assertEqual(mapper.from_rom(0x008000), 0x018000)
        self.assertEqual(mapper.from_rom(0x010000), 0x028000)
        self.assertEqual(mapper.from_rom(0x018000), 0x038000)
        self.assertEqual(mapper.from_rom(0x1F0000), 0x3E8000)
        self.assertEqual(mapper.from_rom(0x1F8000), 0x3F8000)

    def test_from_cpu(self):
        """Test method dqutils.mapper.LoROM.from_cpu."""

        mapper = self.mapper

        self.assertEqual(mapper.from_cpu(0x008000), 0x000000)
        self.assertEqual(mapper.from_cpu(0x018000), 0x008000)
        self.assertEqual(mapper.from_cpu(0x028000), 0x010000)
        self.assertEqual(mapper.from_cpu(0x038000), 0x018000)
        # ...
        self.assertEqual(mapper.from_cpu(0x3E8000), 0x1F0000)
        self.assertEqual(mapper.from_cpu(0x3F8000), 0x1F8000)

    def test_increment_address(self):
        """Test method dqutils.mapper.HiROM.increment_address."""

        mapper = self.mapper
        self.assertEqual(mapper.increment_address(0x008000), 0x008001)
        self.assertEqual(mapper.increment_address(0x00FFFF), 0x018000)

    def test_bank_offset_size(self):
        """Test property dqutils.mapper.HiROM.bank_offset_size."""
        self.assertEqual(self.mapper.bank_offset_size, 0x8000)
