"""
Tests for dqutils.snescpu.disasm.
"""

from unittest import TestCase
from dqutils.snescpu.disasm import create_args
from dqutils.snescpu.rom_image import RomImage

class DisasmTestCase(TestCase):
    """Tests dqutils.snescpu.disasm for DQ5."""

    def test_create_args_default(self):
        """Test create_args for DQ5 default values."""

        with RomImage('DRAGONQUEST5') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0x008000)
            self.assertEqual(args['last'], -1)
            self.assertFalse(args['until_return'])
