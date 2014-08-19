#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq3.string
"""

import unittest

class DQ3StringTestCase(unittest.TestCase):

    def test_load_code(self):
        from dqutils.dq3.string import load_code
        self._range_check(load_code)

        hinokinobou = [0x26, 0x24, 0x12, 0x24, 0xDC, 0x0E, 0xAC]
        loc, codes = load_code(0x0047)
        self.assertEqual(codes, hinokinobou)

    def test_load_string(self):
        from dqutils.dq3.string import load_string
        self._range_check(load_string)

        hinokinobou = 'ひのきのぼう'
        text = load_string(0x0047)
        self.assertTrue(hinokinobou in text)

    def _range_check(self, func):
        from dqutils.dq3.string import ID_FIRST, ID_LAST
        self.assertRaises(IndexError, func, ID_FIRST - 1)
        self.assertRaises(IndexError, func, ID_LAST)

def test_suite():
    return unittest.makeSuite(DQ3StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
