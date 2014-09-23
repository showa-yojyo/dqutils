#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq3.string
"""

import unittest
from dqutils.dq3.string import load_code
from dqutils.dq3.string import load_string
from dqutils.dq3.string import ID_FIRST
from dqutils.dq3.string import ID_LAST

# pylint: disable=too-many-public-methods
class DQ3StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq3.string."""

    def test_load_code(self):
        """Test function dqutils.dq3.load_code."""

        self._range_check(load_code)

        hinokinobou = [0x26, 0x24, 0x12, 0x24, 0xDC, 0x0E, 0xAC]
        loc, codes = load_code(0x0047)
        self.assertEqual(loc, 0xFED0D5)
        self.assertEqual(codes, hinokinobou)

    def test_load_string(self):
        """Test function dqutils.dq3.load_string."""

        self._range_check(load_string)

        hinokinobou = 'ひのきのぼう'
        text = load_string(0x0047)
        self.assertTrue(hinokinobou in text)

    def _range_check(self, func):
        """Helper method."""
        self.assertRaises(IndexError, func, ID_FIRST - 1)
        self.assertRaises(IndexError, func, ID_LAST)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ3StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
