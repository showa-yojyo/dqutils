#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.address module."""

import unittest

class AddressingTestCase(unittest.TestCase):

    def test_IFH(self):
        # ROMADDR --> CPUADDR HiROM
        from dqutils.address import from_hi as IFH
        self.assertEqual(IFH(0x020000, fast = True),  0xC20000)
        self.assertEqual(IFH(0x020000, fast = False), 0x420000)

    def test_ISL(self):
        # ROMADDR --> CPUADDR LoROM
        from dqutils.address import from_lo as ISL
        self.assertEqual(ISL(0x000000, fast = False),  0x008000)
        self.assertEqual(ISL(0x008000, fast = False),  0x018000)
        self.assertEqual(ISL(0x010000, fast = False),  0x028000)
        self.assertEqual(ISL(0x018000, fast = False),  0x038000)
        self.assertEqual(ISL(0x1F0000, fast = False),  0x3E8000)
        self.assertEqual(ISL(0x1F8000, fast = False),  0x3F8000)

    def test_OFH(self):
        # ROMADDR <-- CPUADDR HiROM
        from dqutils.address import conv_hi as HiROM

        # SlowROM

        self.assertEqual(HiROM(0x408000), 0x008000)
        self.assertEqual(HiROM(0x418000), 0x018000)
        self.assertEqual(HiROM(0x428000), 0x028000)
        self.assertEqual(HiROM(0x438000), 0x038000)
        # ...
        self.assertEqual(HiROM(0x7E8000), 0x3E8000)
        self.assertEqual(HiROM(0x7F8000), 0x3F8000)

        # FastROM

        self.assertEqual(HiROM(0xC08000), 0x008000)
        self.assertEqual(HiROM(0xC18000), 0x018000)
        self.assertEqual(HiROM(0xC28000), 0x028000)
        self.assertEqual(HiROM(0xC38000), 0x038000)
        # ...
        self.assertEqual(HiROM(0xFE8000), 0x3E8000)
        self.assertEqual(HiROM(0xFF8000), 0x3F8000)

    def test_OSL(self):
        from dqutils.address import conv_lo as OSL
        # ROMADDR <-- CPUADDR LoROM
        self.assertEqual(OSL(0x008000), 0x000000)
        self.assertEqual(OSL(0x018000), 0x008000)
        self.assertEqual(OSL(0x028000), 0x010000)
        self.assertEqual(OSL(0x038000), 0x018000)
        # ...
        self.assertEqual(OSL(0x3E8000), 0x1F0000)
        self.assertEqual(OSL(0x3F8000), 0x1F8000)

def test_suite():
    return unittest.makeSuite(AddressingTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
