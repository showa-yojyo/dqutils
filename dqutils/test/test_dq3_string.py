#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq3.string"""

import unittest
import mmap
from dqutils.dq3 import open_rom
from dqutils.dq3.string import enum_string
from dqutils.dq3.string import get_text

# pylint: disable=too-many-public-methods
class DQ3StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq3.string."""

    def test_get_text(self):
        """Test function dqutils.dq3.get_text."""

        text = get_text(bytearray(b"\x26\x24\x12\x24\xDC\x0E\xAC"))
        self.assertTrue('ひのきのぼう' in text)

    def test_enum_string(self):
        """Test function dqutils.dq3.enum_string."""
        with open_rom() as fin:
            with mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ) as mem:
                testdata = tuple(enum_string(mem, 0x100, 0x110))

                self.assertEqual(testdata[0][0], 0xFED659)
                self.assertTrue('せいすい' in get_text(testdata[0][1]))

                self.assertEqual(testdata[15][0], 0xFED6CA)
                self.assertTrue('にじのしずく' in get_text(testdata[15][1]))

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ3StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
