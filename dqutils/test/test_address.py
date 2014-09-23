#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.address module."""

import unittest

# pylint: disable=too-many-public-methods
class AddressingTestCase(unittest.TestCase):
    """Test functions defined in dqutils.address."""

    def test_from_hi(self):
        """Test function dqutils.address.from_hi."""

        # ROMADDR --> CPUADDR HiROM
        from dqutils.address import from_hi
        self.assertEqual(from_hi(0x020000, fast=True), 0xC20000)
        self.assertEqual(from_hi(0x020000, fast=False), 0x420000)

    def test_from_lo(self):
        """Test function dqutils.address.from_lo."""

        # ROMADDR --> CPUADDR LoROM
        from dqutils.address import from_lo
        self.assertEqual(from_lo(0x000000, fast=False), 0x008000)
        self.assertEqual(from_lo(0x008000, fast=False), 0x018000)
        self.assertEqual(from_lo(0x010000, fast=False), 0x028000)
        self.assertEqual(from_lo(0x018000, fast=False), 0x038000)
        self.assertEqual(from_lo(0x1F0000, fast=False), 0x3E8000)
        self.assertEqual(from_lo(0x1F8000, fast=False), 0x3F8000)

    def test_conv_hi(self):
        """Test function dqutils.address.conv_hi."""

        # ROMADDR <-- CPUADDR HiROM
        from dqutils.address import conv_hi

        # SlowROM

        self.assertEqual(conv_hi(0x408000), 0x008000)
        self.assertEqual(conv_hi(0x418000), 0x018000)
        self.assertEqual(conv_hi(0x428000), 0x028000)
        self.assertEqual(conv_hi(0x438000), 0x038000)
        # ...
        self.assertEqual(conv_hi(0x7E8000), 0x3E8000)
        self.assertEqual(conv_hi(0x7F8000), 0x3F8000)

        # FastROM

        self.assertEqual(conv_hi(0xC08000), 0x008000)
        self.assertEqual(conv_hi(0xC18000), 0x018000)
        self.assertEqual(conv_hi(0xC28000), 0x028000)
        self.assertEqual(conv_hi(0xC38000), 0x038000)
        # ...
        self.assertEqual(conv_hi(0xFE8000), 0x3E8000)
        self.assertEqual(conv_hi(0xFF8000), 0x3F8000)

    def test_conv_lo(self):
        """Test function dqutils.address.conv_lo."""

        from dqutils.address import conv_lo
        # ROMADDR <-- CPUADDR LoROM
        self.assertEqual(conv_lo(0x008000), 0x000000)
        self.assertEqual(conv_lo(0x018000), 0x008000)
        self.assertEqual(conv_lo(0x028000), 0x010000)
        self.assertEqual(conv_lo(0x038000), 0x018000)
        # ...
        self.assertEqual(conv_lo(0x3E8000), 0x1F0000)
        self.assertEqual(conv_lo(0x3F8000), 0x1F8000)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(AddressingTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
