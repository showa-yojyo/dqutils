
"""Tests for dqutils.dq3.message"""

from array import array
from unittest import TestCase
from ..message import (enum_battle, enum_scenario)

class DQ3MessageTestCase(TestCase):
    """Test functions defined in dqutils.dq3.message."""

    def test_enum_battle(self):
        """Test function dqutils.dq3.enum_battle."""

        cpuaddr, code_seq = next(enum_battle(0x0141, 0x0142))

        # [BD]しかし なにも おこらなかった！[B1]
        however_nothing_happened =\
            b'\xBD\x17\x11\x17\x01'\
            b'\x20\x21\x2E\x01'\
            b'\x10\x15\x32\x20\x11\x3F\x1B\x7F\xB1\xAC'

        self.assertEqual(cpuaddr, 0xFCBD36)
        self.assertEqual(however_nothing_happened, code_seq)

    def test_enum_scenario(self):
        """Test function dqutils.dq3.enum_scenario."""

        # 0160:FCD9D7:08:ぐがー ぐがー！
        # 0161:FCD9E0:80:ぐごー ぐごー！
        # 0162:FCD9E9:20:ぐがー ぐがー。
        addrs = (0xFCD9D7, 0xFCD9E0, 0xFCD9E9)

        # pylint: disable=line-too-long
        codes = (
            array('H', [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x052E]),
            array('H', [0x05DA, 0x05DB, 0x0535, 0x0200, 0x05DA, 0x05DB, 0x0535, 0x052E]),
            array('H', [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x0529]),)

        for result, addr, code in zip(enum_scenario(0x0160, 0x0163), addrs, codes):
            self.assertEqual(result[0], addr)
            # [-1] is one of the delimiter characters.
            self.assertEqual(result[-1][:-1], code)
