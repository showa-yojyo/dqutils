#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
"""Tests for dqutils.dq3.message
"""
import unittest

class DQ3BattleMessageTestCase(unittest.TestCase):

    def test_load_battle_msg_code(self):
        from dqutils.dq3.message import load_battle_msg_code
        cpuaddr, codes = load_battle_msg_code(0x0141, 0x0142)[0]
        # [BD]しかし なにも おこらなかった！[B1]
        however_nothing_happened = [0xBD, 0x17, 0x11, 0x17, 0x01, 0x20, 0x21, 0x2E, 0x01, 0x10, 0x15, 0x32, 0x20, 0x11, 0x3F, 0x1B, 0x7F, 0xB1, 0xAC]
        self.assertEqual(however_nothing_happened, codes)

        from dqutils.dq3.message import BATTLE_ID_FIRST, BATTLE_ID_LAST
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_FIRST - 1, BATTLE_ID_FIRST)
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_LAST, BATTLE_ID_LAST + 1)
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_LAST, BATTLE_ID_FIRST)

class DQ3MessageTestCase(unittest.TestCase):

    def test_load_msg_code(self):
        from dqutils.dq3.message import load_msg_code
        self._verify_id(load_msg_code)
        rawcodes = load_msg_code(0x0160, 0x0163)
        self.assertEqual(len(rawcodes), 3)

        msgs = ([0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x052E],
                [0x05DA, 0x05DB, 0x0535, 0x0200, 0x05DA, 0x05DB, 0x0535, 0x052E],
                [0x05DA, 0x053A, 0x0535, 0x0200, 0x05DA, 0x053A, 0x0535, 0x0529],)

        for i in range(3):
            # [-1] holds a delimiter character
            self.assertEqual(msgs[i], rawcodes[i][-1][:-1])

    def _verify_id(self, func):
        from dqutils.dq3.message import MSG_ID_FIRST, MSG_ID_LAST
        self.assertRaises(RuntimeError, func, MSG_ID_FIRST - 1, MSG_ID_FIRST)
        self.assertRaises(RuntimeError, func, MSG_ID_LAST, MSG_ID_LAST + 1)
        self.assertRaises(RuntimeError, func, MSG_ID_LAST, MSG_ID_FIRST)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DQ3BattleMessageTestCase))
    suite.addTest(unittest.makeSuite(DQ3MessageTestCase))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
