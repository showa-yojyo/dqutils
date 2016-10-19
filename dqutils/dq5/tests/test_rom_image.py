"""
Tests for dqutils.snescpu.rom_image.
"""

from unittest import TestCase
from dqutils.snescpu.rom_image import (RomImage, get_snes_header)

class RomImageTestCase(TestCase):
    """Test functions defined in dqutils.snescpu.rom_image."""

    def test_get_snes_header(self):
        """Test function dqutils.snescpu.rom_image.get_snes_header
        for DQ5.
        """

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
