#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.rom_image"""

import unittest
from dqutils.rom_image import RomImage
from dqutils.rom_image import get_snes_header

# pylint: disable=too-many-public-methods
class RomImageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.rom_image."""

    def test_get_snes_header_for_dq6(self):
        """Test function dqutils.rom_image.get_snes_header."""

        with RomImage('DRAGONQUEST6') as mem:
            header = get_snes_header(mem)

        # [offset]: +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
        # ---------------------------------------------------------
        # 0000FFC0: 44 52 41 47 4F 4E 51 55 45 53 54 36 20 20 20 20
        # 0000FFD0: 20 20 20 20 20 31 02 0C 03 00 33 00 70 A1 8F 5E
        # 0000FFE0: FF FF FF FF AC FF A8 FF A4 FF A0 FF A4 FF A4 FF
        # 0000FFF0: FF FF FF FF A4 FF A4 FF A4 FF A0 FF 98 FF A4 FF

        self.assertEqual(len(header), 64)
        self.assertTrue(header.startswith(b'DRAGONQUEST6'))
        self.assertEqual(header[0x15] & 0x01, 0x01) # HiROM
        self.assertEqual(header[0x17], 0x0C) # $0c => 4 megabytes

    def test_get_snes_header_for_dq3(self):
        """Test function dqutils.rom_image.get_snes_header."""

        with RomImage('DRAGONQUEST3') as mem:
            header = get_snes_header(mem)

        # [offset]: +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
        # ---------------------------------------------------------
        # 0000FFC0: 44 52 41 47 4F 4E 51 55 45 53 54 33 20 20 20 20
        # 0000FFD0: 20 20 20 20 20 31 02 0C 03 00 33 00 8C 8B 73 74
        # 0000FFE0: FF FF FF FF AC FF A8 FF A4 FF A0 FF A4 FF A4 FF
        # 0000FFF0: FF FF FF FF A4 FF A4 FF A4 FF A0 FF 98 FF A4 FF

        self.assertEqual(len(header), 64)
        self.assertTrue(header.startswith(b'DRAGONQUEST3'))
        self.assertEqual(header[0x15] & 0x01, 0x01) # HiROM
        self.assertEqual(header[0x17], 0x0C) # $0c => 4 megabytes

    def test_get_snes_header_for_dq5(self):
        """Test function dqutils.rom_image.get_snes_header."""

        with RomImage('DRAGONQUEST5') as mem:
            header = get_snes_header(mem)

        # [offset]: +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
        # ---------------------------------------------------------
        # 00007FC0: 44 52 41 47 4F 4E 51 55 45 53 54 35 20 20 20 20
        # 00007FD0: 20 20 20 20 20 20 02 0B 03 00 B4 00 06 45 F9 BA
        # 00007FE0: 00 00 00 00 7F 8F 80 8F 7F 8F 5D 88 7F 8F 7F 8F
        # 00007FF0: 00 00 00 00 7F 8F 80 8F 7F 8F 5D 88 39 86 7F 8F

        self.assertEqual(len(header), 64)
        self.assertTrue(header.startswith(b'DRAGONQUEST5'))
        self.assertEqual(header[0x15] & 0x01, 0x00) # LoROM
        self.assertEqual(header[0x17], 0x0B) # 1.5M => 2M

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(RomImageTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
