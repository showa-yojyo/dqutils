"""
Tests for dquils.snescpu.hexdump.
"""

from os import devnull
from unittest import TestCase
from unittest.mock import patch
from ..hexdump import create_argparser

class TestCaseHexDump(TestCase):
    """Tests for dquils.snescpu.hexdump."""

    def test_create_argparser(self):
        """Test function `create_argparser`."""

        parser = create_argparser()

        # invalid arguments
        with patch('sys.stderr', open(devnull, 'w')):
            self.assertRaises(SystemExit, parser.parse_args)
            self.assertRaises(SystemExit, parser.parse_args,
                              ['C0FF70'])
            self.assertRaises(SystemExit, parser.parse_args,
                              ['C0FF70', '16'])

        # a normal case
        args = parser.parse_args(['C0FF70', '16', '4'])
        self.assertEqual(args.start, 'C0FF70')
        self.assertEqual(args.byte_count, 16)
        self.assertEqual(args.record_count, 4)
