#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""Tests for dqutils.dq5.string
"""

import unittest

from dqutils.dq5.string import GROUPS, GROUP_FIRST, GROUP_LAST

class DQ5StringTestCase(unittest.TestCase):

    hinokinobou = [0x2A, 0x28, 0x16, 0x28, 0x84, 0x2D, 0x12]

    def test_load_code(self):
        from dqutils.dq5.string import load_code
        self._range_check(load_code)

        loc, code = load_code(5)[0]
        self.assertEqual(code, self.hinokinobou)

    def test_make_text(self):
        from dqutils.dq5.string import make_text
        text = make_text(self.hinokinobou)
        self.assertEqual(text, u'ひのきのぼう')

    def _range_check(self, func):
        for group in xrange(GROUP_FIRST, GROUP_LAST):
            data = func(group)
            self.assertEqual(len(data), GROUPS[group][1])

        self.assertRaises(RuntimeError, func, GROUP_FIRST - 1)
        self.assertRaises(RuntimeError, func, GROUP_LAST)


def test_suite():
    return unittest.makeSuite(DQ5StringTestCase)


if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
