#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.address module."""

import unittest
from dqutils.address import HiROM
from dqutils.address import LoROM

# pylint: disable=too-many-public-methods
class HiROMTestCase(unittest.TestCase):
    """Test functions defined in dqutils.address."""

    def test_from_rom(self):
        """Test method dqutils.address.HiROM.from_rom."""

        mapper = HiROM()

        # ROMADDR --> CPUADDR HiROM
        self.assertEqual(mapper.from_rom(0x020000), 0xC20000)

    def test_from_cpu(self):
        """Test method dqutils.address.HiROM.from_cpu."""

        mapper = HiROM()

        # ROMADDR <-- CPUADDR HiROM
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

class LoROMTestCase(unittest.TestCase):
    """Test functions defined in dqutils.address."""

    def test_from_rom(self):
        """Test method dqutils.address.LoROM.from_rom."""

        mapper = LoROM()

        # ROMADDR --> CPUADDR LoROM
        self.assertEqual(mapper.from_rom(0x000000), 0x008000)
        self.assertEqual(mapper.from_rom(0x008000), 0x018000)
        self.assertEqual(mapper.from_rom(0x010000), 0x028000)
        self.assertEqual(mapper.from_rom(0x018000), 0x038000)
        self.assertEqual(mapper.from_rom(0x1F0000), 0x3E8000)
        self.assertEqual(mapper.from_rom(0x1F8000), 0x3F8000)

    def test_from_cpu(self):
        """Test method dqutils.address.LoROM.from_cpu."""

        mapper = LoROM()

        # ROMADDR <-- CPUADDR LoROM
        self.assertEqual(mapper.from_cpu(0x008000), 0x000000)
        self.assertEqual(mapper.from_cpu(0x018000), 0x008000)
        self.assertEqual(mapper.from_cpu(0x028000), 0x010000)
        self.assertEqual(mapper.from_cpu(0x038000), 0x018000)
        # ...
        self.assertEqual(mapper.from_cpu(0x3E8000), 0x1F0000)
        self.assertEqual(mapper.from_cpu(0x3F8000), 0x1F8000)

def test_suite():
    """Setup a test suite."""
    suite = unittest.TestSuite()
    suite.addTest(HiROMTestCase())
    suite.addTest(LoROMTestCase())
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
