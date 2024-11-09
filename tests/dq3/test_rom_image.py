"""
Tests for dqutils.snescpu.rom_image.
"""

from unittest import TestCase

from dqutils.snescpu.rom_image import RomImage, get_snes_header


class RomImageTestCase(TestCase):
    """Test functions defined in dqutils.snescpu.rom_image."""

    def test_get_snes_header(self):
        """Test function dqutils.snescpu.rom_image.get_snes_header.
        for DQ3.
        """

        with RomImage("DRAGONQUEST3") as mem:
            header = get_snes_header(mem)

        # [offset]: +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
        # ---------------------------------------------------------
        # 0000FFC0: 44 52 41 47 4F 4E 51 55 45 53 54 33 20 20 20 20
        # 0000FFD0: 20 20 20 20 20 31 02 0C 03 00 33 00 8C 8B 73 74
        # 0000FFE0: FF FF FF FF AC FF A8 FF A4 FF A0 FF A4 FF A4 FF
        # 0000FFF0: FF FF FF FF A4 FF A4 FF A4 FF A0 FF 98 FF A4 FF

        self.assertEqual(len(header), 64)
        self.assertTrue(header.startswith(b"DRAGONQUEST3"))
        self.assertEqual(header[0x1C] ^ header[0x1E], 0xFF)
        self.assertEqual(header[0x1D] ^ header[0x1F], 0xFF)
        self.assertEqual(header[0x15] & 0x01, 0x01)  # HiROM
        self.assertEqual(header[0x17], 0x0C)  # $0c => 4 megabytes
