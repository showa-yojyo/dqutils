#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq5.message
"""
import unittest

# TODO: test dakuten

class DQ5MessageTestCase(unittest.TestCase):

    def test_load_msg_code(self):
        from dqutils.dq5.message import load_msg_code
        cpuaddr, shift, codeseq = load_msg_code(0x0B95, 0x0B96)[0]

        # :0B95:わーい わーい！[1001]
        wai = [0x031B, 0x0360, 0x0398, 0x0000, 0x031B, 0x0360, 0x0398, 0x035A, 0x1001]
        self.assertEqual(wai, codeseq)

        from dqutils.dq5.message import MSG_ID_FIRST, MSG_ID_LAST
        self.assertRaises(RuntimeError, load_msg_code, MSG_ID_FIRST - 1, MSG_ID_FIRST)
        self.assertRaises(RuntimeError, load_msg_code, MSG_ID_LAST, MSG_ID_LAST + 1)
        self.assertRaises(RuntimeError, load_msg_code, MSG_ID_LAST, MSG_ID_FIRST)

class DQ5BattleMessageTestCase(unittest.TestCase):

    def test_load_battle_msg_code(self):
        from dqutils.dq5.message import load_battle_msg_code
        cpuaddr, shift, codeseq = load_battle_msg_code(0x007B, 0x007C)[0]

        # しかし なにも おこらなかった！[FE]
        however_nothing_happened = [0x1B, 0x15, 0x1B, 0x01, 0x24, 0x25, 0x32, 0x01, 0x14, 0x19, 0x36, 0x24, 0x15, 0x3E, 0x1F, 0x7A, 0xFE]
        self.assertEqual(however_nothing_happened, codeseq)

        from dqutils.dq5.message import BATTLE_ID_FIRST, BATTLE_ID_LAST
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_FIRST - 1, BATTLE_ID_FIRST)
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_LAST, BATTLE_ID_LAST + 1)
        self.assertRaises(RuntimeError, load_battle_msg_code, BATTLE_ID_LAST, BATTLE_ID_FIRST)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DQ5BattleMessageTestCase))
    suite.addTest(unittest.makeSuite(DQ5MessageTestCase))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
