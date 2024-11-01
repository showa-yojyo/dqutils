"""
Tests for dquils.snescpu.hexdump.
"""

from dqutils.snescpu.hexdump import dump
from ..snescpu.test_hexdump import AbstractHexDumpTestCase, ADDRESS_PATTERN


class HexDumpTestCase(AbstractHexDumpTestCase):
    """Tests for dquils.snescpu.hexdump."""

    game_title = "DRAGONQUEST3"

    def test_dump(self):
        """Test function `dump`."""

        dump(self.game_title, ["C808DA", "12", "1389"])
        lines = self.out.getvalue().split("\n")

        self.assertTrue(lines[0].startswith("C8/08DA:"))
        self.assertTrue(lines[1].startswith("C8/08E6:"))

        for line in lines[:-1]:
            self.assertRegex(line, ADDRESS_PATTERN)
            self.assertRegex(line, r"\t[0-9A-F]{24}$")
        self.assertEqual(lines[-1], "")
