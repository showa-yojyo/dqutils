#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for dqutils.bit module."""

import unittest
from dqutils.bit import getbits
from dqutils.bit import getbytes

# pylint: disable=too-many-public-methods
class BitTestCase(unittest.TestCase):
    """Test functions defined in dqutils.bit."""

    def setUp(self):
        """Setup the test case."""
        self.data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06]

    def test_getbytes(self):
        """Test function dqutils.bit.getbytes."""
        data = self.data
        self.assertEqual(getbytes(data, 0, 1), 0x00)
        self.assertEqual(getbytes(data, 1, 1), 0x01)
        self.assertEqual(getbytes(data, 0, 2), 0x0100)
        self.assertEqual(getbytes(data, 6, 2), 0x0006)
        self.assertEqual(getbytes(data, 0, 3), 0x020100)
        self.assertEqual(getbytes(data, 5, 3), 0x000605)
        self.assertEqual(getbytes(data, 6, 3), 0x000006)

    def test_getbits(self):
        """Test function dqutils.bit.getbits."""
        data = self.data
        self.assertEqual(getbits(data, 0, 0xFF00), 0x0001)
        self.assertEqual(getbits(data, 1, 0xFFFF), 0x0201)
        self.assertEqual(getbits(data, 0, 0x0100), 0x0001)

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(BitTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
