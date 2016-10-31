"""
Tests for dquils.snescpu.hexdump.
"""

from io import StringIO
from os import devnull
from unittest import TestCase
from unittest.mock import patch
from ..hexdump import dump

ADDRESS_PATTERN = r'^[0-9A-F]{2}/[0-9A-F]{4}:'

class TestCaseHexDump(TestCase):
    """Tests for dquils.snescpu.hexdump."""

    game_title = 'DRAGONQUEST5'

    def test_dump(self):
        """Test function `dump`."""

        with patch('sys.stdout', StringIO()) as out:
            dump(self.game_title, '238000 25 235'.split())
            lines = out.getvalue().split('\n')

            self.assertTrue(lines[0].startswith('23/8000:'))
            self.assertTrue(lines[0].endswith('A102'))
            self.assertTrue(lines[1].startswith('23/8019:'))
            self.assertTrue(lines[1].endswith('A100'))

            for line in lines[:-1]:
                self.assertRegex(line, ADDRESS_PATTERN)
                self.assertRegex(line, r'\t[0-9A-F]{50}$')
            self.assertEqual(lines[-1], '')
