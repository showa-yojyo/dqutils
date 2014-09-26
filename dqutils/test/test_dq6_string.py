#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq6.string"""

import unittest
from dqutils.romimage import RomImage
from dqutils.dq6.string import CONTEXT
from dqutils.dq6.string import enum_string
from dqutils.dq6.string import get_text

# pylint: disable=too-many-public-methods
class DQ6StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq6.string."""

    def test_get_text(self):
        """Test function dqutils.dq6.get_text."""

        text = get_text(b"\x2A\x28\x16\x28\xDC\x12\xAC")
        self.assertTrue('ひのきのぼう' in text)

    def test_enum_string(self):
        """Test function dqutils.dq6.enum_string."""

        with RomImage(CONTEXT["TITLE"]) as mem:
            testdata = tuple(enum_string(mem, 0x300, 0x310))

            self.assertEqual(testdata[0][0], 0xFB97DB)
            self.assertTrue('ムドー' in get_text(testdata[0][1]))

            self.assertEqual(testdata[15][0], 0xFB9835)
            self.assertTrue('デュラン' in get_text(testdata[15][1]))

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ6StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
