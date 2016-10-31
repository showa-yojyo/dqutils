"""
Tests for dquils.snescpu.hexdump.
"""

from io import StringIO
from os import devnull
from unittest import TestCase
from unittest.mock import patch
from ...snescpu.hexdump import dump

ADDRESS_PATTERN = r'^[0-9A-F]{2}/[0-9A-F]{4}:'

class TestCaseHexDump(TestCase):
    """Tests for dquils.snescpu.hexdump."""

    game_title = 'DRAGONQUEST3'

    def test_dump(self):
        """Test function `dump`."""

        with patch('sys.stdout', StringIO()) as out:
            dump(self.game_title, ['C808DA', '12', '1389'])
            lines = out.getvalue().split('\n')

            self.assertTrue(lines[0].startswith('C8/08DA:'))
            self.assertTrue(lines[1].startswith('C8/08E6:'))

            for line in lines[:-1]:
                self.assertRegex(line, ADDRESS_PATTERN)
                self.assertRegex(line, r'\t[0-9A-F]{24}$')
            self.assertEqual(lines[-1], '')
