"""
Tests for dquils.snescpu.hexdump.
"""

from io import StringIO
from os import devnull
from unittest import TestCase
from unittest.mock import patch
from dqutils.snescpu.hexdump import dump

ADDRESS_PATTERN = r'^[0-9A-F]{2}/[0-9A-F]{4}:'

class TestCaseHexDump(TestCase):
    """Tests for dquils.snescpu.hexdump."""

    game_title = 'DRAGONQUEST6'

    def test_dump(self):
        """Test function `dump`."""

        with patch('sys.stdout', StringIO()) as out:
            dump(self.game_title, 0xC0FFC0, 16, 4)
            lines = out.getvalue().split('\n')

            self.assertTrue(lines[0].startswith('C0/FFC0:'))
            self.assertTrue(lines[1].startswith('C0/FFD0:'))

            for line in lines[:-1]:
                self.assertRegex(line, ADDRESS_PATTERN)
                self.assertRegex(line, r'\t[0-9A-F]{32}$')
            self.assertEqual(lines[-1], '')

        # about to be across the bank boundary
        with patch('sys.stdout', StringIO()) as out:
            dump(self.game_title, 0xC0FFC0, 12, 6)
            lines = out.getvalue().split('\n')

            self.assertTrue(lines[0].startswith('C0/FFC0:'))
            self.assertTrue(lines[1].startswith('C0/FFCC:'))

            for line in lines[:-2]:
                self.assertRegex(line, ADDRESS_PATTERN)
                self.assertRegex(line, r'\t[0-9A-F]{24}$')

            self.assertRegex(lines[-2], ADDRESS_PATTERN)
            self.assertRegex(lines[-2], r'\t[0-9A-F]{8}$')
            self.assertEqual(lines[-1], '')
