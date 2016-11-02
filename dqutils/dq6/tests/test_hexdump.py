"""
Tests for dquils.snescpu.hexdump.
"""
from ...snescpu.hexdump import dump
from ...snescpu.tests.test_hexdump import (AbstractHexDumpTestCase,
                                           ADDRESS_PATTERN)

class HexDumpTestCase(AbstractHexDumpTestCase):
    """Tests for dquils.snescpu.hexdump."""

    game_title = 'DRAGONQUEST6'

    def test_dump_simple(self):
        """Test function `dump`."""

        dump(self.game_title, ['C0FFC0', '16', '4'])
        lines = self.out.getvalue().split('\n')

        self.assertTrue(lines[0].startswith('C0/FFC0:'))
        self.assertTrue(lines[1].startswith('C0/FFD0:'))

        for line in lines[:-1]:
            self.assertRegex(line, ADDRESS_PATTERN)
            self.assertRegex(line, r'\t[0-9A-F]{32}$')
        self.assertEqual(lines[-1], '')

    def test_dump_bank_boundary(self):
        """Test function `dump`."""

        # about to be across the bank boundary
        dump(self.game_title, ['C0FFC0', '12', '6'])
        lines = self.out.getvalue().split('\n')

        self.assertTrue(lines[0].startswith('C0/FFC0:'))
        self.assertTrue(lines[1].startswith('C0/FFCC:'))

        for line in lines[:-2]:
            self.assertRegex(line, ADDRESS_PATTERN)
            self.assertRegex(line, r'\t[0-9A-F]{24}$')

        self.assertRegex(lines[-2], ADDRESS_PATTERN)
        self.assertRegex(lines[-2], r'\t[0-9A-F]{8}$')
        self.assertEqual(lines[-1], '')

    def test_dump_zero_input(self):
        """Test the case where zeros are passed to `dump`."""

        dump(self.game_title, ['C0FFC0', '0', '0'])
        lines = self.out.getvalue().split('\n')
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[-1], '')

        dump(self.game_title, ['C0FFC0', '1', '0'])
        lines = self.out.getvalue().split('\n')
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[-1], '')

        dump(self.game_title, ['C0FFC0', '0', '1'])
        lines = self.out.getvalue().split('\n')
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[-1], '')
