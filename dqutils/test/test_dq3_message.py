#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq3.message
"""

import unittest
from dqutils.romimage import RomImage
from dqutils.dq3.message import CONTEXT_MESSAGE_BATTLE
from dqutils.dq3.message import enum_battle_message
from dqutils.dq3.message import load_msg_code
from dqutils.dq3.message import MSG_ID_FIRST
from dqutils.dq3.message import MSG_ID_LAST

# pylint: disable=too-many-public-methods
class DQ3BattleMessageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq3.message."""

    def test_enum_battle_message(self):
        """Test function dqutils.dq3.enum_battle_message."""

        with RomImage(CONTEXT_MESSAGE_BATTLE["TITLE"]) as mem:
            cpuaddr, codes = tuple(enum_battle_message(mem, 0x0141, 0x0142))[0]

            # [BD]しかし なにも おこらなかった！[B1]
            however_nothing_happened =\
                b'\xBD\x17\x11\x17\x01' +\
                b'\x20\x21\x2E\x01' +\
                b'\x10\x15\x32\x20\x11\x3F\x1B\x7F\xB1\xAC'

            self.assertEqual(however_nothing_happened, codes)

# pylint: disable=too-many-public-methods
class DQ3MessageTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq3.message."""

    def test_load_msg_code(self):
        """Test function dqutils.dq3.load_msg_code."""

        self._verify_id(load_msg_code)
        rawcodes = load_msg_code(0x0160, 0x0163)
        self.assertEqual(len(rawcodes), 3)

        msgs = (
            [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x052E],
            [0x05DA, 0x05DB, 0x0535, 0x0200, 0x05DA, 0x05DB, 0x0535, 0x052E],
            [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x0529],)

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
    suite.addTest(unittest.makeSuite(DQ3BattleMessageTestCase))
    suite.addTest(unittest.makeSuite(DQ3MessageTestCase))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
