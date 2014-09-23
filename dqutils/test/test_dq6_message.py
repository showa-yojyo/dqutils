#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq6.message
"""

import unittest
from dqutils.dq6.message import load_battle_msg_code
from dqutils.dq6.message import BATTLE_ID_FIRST
from dqutils.dq6.message import BATTLE_ID_LAST
from dqutils.dq6.message import load_msg_code
from dqutils.dq6.message import MSG_ID_FIRST
from dqutils.dq6.message import MSG_ID_LAST

# pylint: disable=too-many-public-methods
class DQ6BattleMessageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq6.message."""

    def test_load_battle_msg_code(self):
        """Test function dqutils.dq3.load_battle_msg_code."""

        cpuaddr, codes = load_battle_msg_code(0x0140, 0x0141)[0]

        # [BD]しかし なにも おこらなかった！[B1]
        however_nothing_happened = [
            0xBD, 0x1B, 0x15, 0x1B, 0x01,
            0x24, 0x25, 0x32, 0x01,
            0x14, 0x19, 0x36, 0x24, 0x15, 0x3E, 0x1F, 0x7A, 0xB1,
            0xAC]
        self.assertEqual(however_nothing_happened, codes)

    # pylint: disable=invalid-name
    def test_load_battle_msg_code_exceptions(self):
        """Test function dqutils.dq3.load_battle_msg_code."""

        self.assertRaises(
            IndexError, load_battle_msg_code,
            BATTLE_ID_FIRST - 1, BATTLE_ID_FIRST)
        self.assertRaises(
            IndexError, load_battle_msg_code,
            BATTLE_ID_LAST, BATTLE_ID_LAST + 1)
        self.assertRaises(
            IndexError, load_battle_msg_code,
            BATTLE_ID_LAST, BATTLE_ID_FIRST)

# pylint: disable=too-many-public-methods
class DQ6MessageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq6.message."""

    # :0x0023:にゃーん。:
    # :0x0024:にゃ～ん。:
    # :0x0025:にゃん にゃん にゃん！:

    def test_load_msg_code(self):
        """Test function dqutils.dq6.load_msg_code."""

        self._verify_id(load_msg_code)

        rawcodes = load_msg_code(0x0023, 0x0026)
        self.assertEqual(len(rawcodes), 3)

        msgs = ([0x0629, 0x0621, 0x0558, 0x04F7, 0x054C],
                [0x0629, 0x0621, 0x0559, 0x04F7, 0x054C],
                [0x0629, 0x0621, 0x04F7, 0x0200,
                 0x0629, 0x0621, 0x04F7, 0x0200,
                 0x0629, 0x0621, 0x04F7, 0x0551],)

        for i in range(3):
            # [-1] holds a delimiter character
            self.assertEqual(msgs[i], rawcodes[i][-1][:-1])

    def _verify_id(self, func):
        """Helper method."""

        self.assertRaises(IndexError, func, MSG_ID_FIRST - 1, MSG_ID_FIRST)
        self.assertRaises(IndexError, func, MSG_ID_LAST, MSG_ID_LAST + 1)
        self.assertRaises(IndexError, func, MSG_ID_LAST, MSG_ID_FIRST)

def test_suite():
    """Setup a test suite."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DQ6BattleMessageTestCase))
    suite.addTest(unittest.makeSuite(DQ6MessageTestCase))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
