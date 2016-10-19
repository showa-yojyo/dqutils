# -*- coding: utf-8 -*-
"""Tests for dqutils.dq5.message"""

from array import array
from unittest import TestCase
from dqutils.dq5.message import (enum_battle, enum_scenario)

class DQ5MessageTestCase(TestCase):
    """Test functions defined in dqutils.dq5.message."""

    def test_enum_battle(self):
        """Test function dqutils.dq5.enum_battle."""

        cpu_addr, _, code_seq = tuple(enum_battle(0x007B, 0x007C))[0]

        # しかし なにも おこらなかった！[FE]
        however_nothing_happened = array('H', (
            0x1B, 0x15, 0x1B, 0x01,
            0x24, 0x25, 0x32, 0x01,
            0x14, 0x19, 0x36, 0x24, 0x15, 0x3E, 0x1F, 0x7A, 0xFE))

        self.assertEqual(cpu_addr, 0x078647)
        self.assertEqual(however_nothing_happened, code_seq)

    def test_enum_scenario(self):
        """Test function dqutils.dq5.enum_scenario."""

        cpu_addr, _, code_seq = tuple(enum_scenario(0x0B95, 0x0B96))[0]

        # 0B95:0BCCD8:02:わーい わーい！
        wai = array('H', (
            0x031B, 0x0360, 0x0398, 0x0000,
            0x031B, 0x0360, 0x0398, 0x035A, 0x1001))

        self.assertEqual(cpu_addr, 0x0BCCD8)
        self.assertEqual(wai, code_seq)
