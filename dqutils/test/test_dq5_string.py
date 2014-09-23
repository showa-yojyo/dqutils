#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq5.string
"""

import unittest
from dqutils.dq5.string import load_code
from dqutils.dq5.string import make_text
from dqutils.dq5.string import GROUPS
from dqutils.dq5.string import GROUP_FIRST
from dqutils.dq5.string import GROUP_LAST

# pylint: disable=too-many-public-methods
class DQ5StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq5.string."""

    hinokinobou = [0x2A, 0x28, 0x16, 0x28, 0x84, 0x2D, 0x12]

    def test_load_code(self):
        """Test function dqutils.dq5.load_code."""

        self._range_check(load_code)

        loc, code = load_code(5)[0]
        self.assertEqual(loc, 0x23CE0F)
        self.assertEqual(code, self.hinokinobou)

    def test_make_text(self):
        """Test function dqutils.dq5.make_text."""

        text = make_text(self.hinokinobou)
        self.assertEqual(text, 'ひのきのぼう')

    def _range_check(self, func):
        """Helper method."""

        for group in range(GROUP_FIRST, GROUP_LAST):
            data = func(group)
            self.assertEqual(len(data), GROUPS[group][1])

        self.assertRaises(IndexError, func, GROUP_FIRST - 1)
        self.assertRaises(IndexError, func, GROUP_LAST)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ5StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
