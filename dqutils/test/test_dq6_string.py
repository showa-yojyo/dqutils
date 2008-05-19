#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
"""Tests for dqutils.dq6.string
"""

import unittest

class DQ6StringTestCase(unittest.TestCase):

    def test_load_code(self):
        from dqutils.dq6.string import load_code
        self._range_check(load_code)

        hinokinobou = [0x2a, 0x28, 0x16, 0x28, 0xdc, 0x12, 0xAC]
        loc, codes = load_code(0x0814)
        self.assertEqual(codes, hinokinobou)

        loc, codes = load_code(0x09A6)
        self.assertEqual(codes, [0xAC])

    def test_load_string(self):
        from dqutils.dq6.string import load_string
        self._range_check(load_string)

        hinokinobou = u'ひのきのぼう'
        text = load_string(0x0814)
        self.assert_(hinokinobou in text)

    def _range_check(self, func):
        from dqutils.dq6.string import ID_FIRST, ID_LAST
        self.assertRaises(RuntimeError, func, ID_FIRST - 1)
        self.assertRaises(RuntimeError, func, ID_LAST)


def test_suite():
    return unittest.makeSuite(DQ6StringTestCase)


if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
