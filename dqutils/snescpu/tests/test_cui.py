"""
Tests for dqutils.snescpu.cui.
"""

from unittest import TestCase
from dqutils.snescpu.rom_image import RomImage
from dqutils.snescpu.cui import (create_argparser, create_args)

# pylint: disable=too-many-public-methods
class TestCui(TestCase):
    """Tests for dqutils.snescpu.cui."""

    def setUp(self):
        self.parser = create_argparser()

    def tearDown(self):
        del self.parser
        self.parser = None

    def test_default_settings(self):
        """Test create_argparser for no argument.
        """
        args = self.parser.parse_args([])

        self.assertFalse(args.accumulator_8bit)
        self.assertFalse(args.index_8bit)
        self.assertFalse(args.bank)
        self.assertFalse(args.range)
        self.assertFalse(args.until_return)

    def test_accum_flag(self):
        """Test create_argparser for -a options.
        """
        parser = self.parser

        args = parser.parse_args(['-a'])
        self.assertTrue(args.accumulator_8bit)
        self.assertFalse(args.index_8bit)

    def test_index_flag(self):
        """Test create_argparser for -x options.
        """
        parser = self.parser

        args = parser.parse_args(['-x'])
        self.assertFalse(args.accumulator_8bit)
        self.assertTrue(args.index_8bit)

    def test_bank(self):
        """Test create_argparser for -b option.
        """
        parser = self.parser

        args = parser.parse_args(['--bank', 'C0'])
        self.assertEqual(args.bank, 'C0')

        args = parser.parse_args(['-b', 'C1'])
        self.assertEqual(args.bank, 'C1')

    def test_range(self):
        """Test create_argparser for -r option.
        """
        parser = self.parser

        args = parser.parse_args(['--range', 'C2B09A:C2B0DD'])
        self.assertEqual(args.range, 'C2B09A:C2B0DD')

        args = parser.parse_args(['-r', 'C2B0DD'])
        self.assertEqual(args.range, 'C2B0DD')

    def test_until_return(self):
        """Test create_argparser for -u option.

        Note that when -u and -r options are specified, the end
        of the range of offsets will be simply discarded.
        """

        parser = self.parser

        args = parser.parse_args(['-u',])
        self.assertTrue(args.until_return)

    def test_create_args_default_dq5(self):
        """Test create_args for DQ5 default values."""

        with RomImage('DRAGONQUEST5') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0x008000)
            self.assertEqual(args['last'], -1)

    def test_create_args_default_dq6(self):
        """Test create_args for DQ6 default values."""

        with RomImage('DRAGONQUEST6') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0xC00000)
            self.assertEqual(args['last'], -1)

    def test_create_args_default_dq3(self):
        """Test create_args for DQ3 default values."""

        with RomImage('DRAGONQUEST3') as rom:
            args, _ = create_args(rom, [])

            self.assertEqual(args['flags'], 0)
            self.assertEqual(args['first'], 0xC00000)
            self.assertEqual(args['last'], -1)
