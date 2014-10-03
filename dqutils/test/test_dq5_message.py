#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq5.message
"""

import unittest
from dqutils.dq5.message import load_msg_code
from dqutils.dq5.message import enum_battle
from dqutils.dq5.message import MSG_ID_FIRST
from dqutils.dq5.message import MSG_ID_LAST
from array import array

# TODO: test dakuten

# pylint: disable=too-many-public-methods
class DQ5MessageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq5.message."""

    def test_load_msg_code(self):
        """Test function dqutils.dq5.load_msg_code."""

        cpuaddr, shift, codeseq = load_msg_code(0x0B95, 0x0B96)[0]

        # :0B95:わーい わーい！[1001]
        wai = [
            0x031B, 0x0360, 0x0398, 0x0000,
            0x031B, 0x0360, 0x0398, 0x035A, 0x1001]
        self.assertEqual(wai, codeseq)

    def test_load_msg_code_exceptions(self):
        """Test function dqutils.dq5.load_msg_code."""

        self.assertRaises(
            IndexError, load_msg_code, MSG_ID_FIRST - 1, MSG_ID_FIRST)
        self.assertRaises(
            IndexError, load_msg_code, MSG_ID_LAST, MSG_ID_LAST + 1)
        self.assertRaises(
            IndexError, load_msg_code, MSG_ID_LAST, MSG_ID_FIRST)

    def test_enum_battle(self):
        """Test function dqutils.dq5.enum_battle."""

        cpu_addr, shift, code_seq = tuple(enum_battle(0x007B, 0x007C))[0]

        # しかし なにも おこらなかった！[FE]
        however_nothing_happened = array('H',
            (0x1B, 0x15, 0x1B, 0x01,
             0x24, 0x25, 0x32, 0x01,
             0x14, 0x19, 0x36, 0x24, 0x15, 0x3E, 0x1F, 0x7A, 0xFE))

        self.assertEqual(cpu_addr, 0x078647)
        self.assertEqual(however_nothing_happened, code_seq)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ5MessageTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
