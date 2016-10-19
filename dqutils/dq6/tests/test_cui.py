"""
Tests for dqutils.snescpu.cui.
"""

from unittest import TestCase
from dqutils.snescpu.rom_image import RomImage
from dqutils.snescpu.cui import create_args

class TestCui(TestCase):
    """Tests dqutils.snescpu.cui for DQ6."""

    def test_create_args_default(self):
        """Test create_args for DQ6 default values."""

        with RomImage('DRAGONQUEST6') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0xC00000)
            self.assertEqual(args['last'], -1)
            self.assertFalse(args['until_return'])
