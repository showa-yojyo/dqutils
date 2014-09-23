#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq6.string
"""

import unittest
from dqutils.dq6.string import load_code
from dqutils.dq6.string import load_string
from dqutils.dq6.string import ID_FIRST
from dqutils.dq6.string import ID_LAST

# pylint: disable=too-many-public-methods
class DQ6StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq6.string."""

    def test_load_code(self):
        """Test function dqutils.dq6.load_code."""

        self._range_check(load_code)

        hinokinobou = [0x2a, 0x28, 0x16, 0x28, 0xdc, 0x12, 0xAC]
        loc, codes = load_code(0x0814)
        self.assertEqual(loc, 0xFBBD23)
        self.assertEqual(codes, hinokinobou)

        loc, codes = load_code(0x09A6)
        self.assertEqual(loc, 0xFBC749)
        self.assertEqual(codes, [0xAC])

    def test_load_string(self):
        """Test function dqutils.dq6.load_string."""

        self._range_check(load_string)

        hinokinobou = 'ひのきのぼう'
        text = load_string(0x0814)
        self.assertTrue(hinokinobou in text)

    def _range_check(self, func):
        """Helper method."""
        self.assertRaises(IndexError, func, ID_FIRST - 1)
        self.assertRaises(IndexError, func, ID_LAST)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ6StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
