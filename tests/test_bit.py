"""Tests for dqutils.bit module."""

import unittest
from dqutils.bit import get_bits, get_int


# pylint: disable=too-many-public-methods
class BitTestCase(unittest.TestCase):
    """Test functions defined in dqutils.bit."""

    def test_get_int(self):
        """Test function dqutils.bit.get_int."""

        targets = (
            (0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06),
            b"\x00\x01\x02\x03\x04\x05\x06",
        )

        for data in targets:
            self.assertEqual(get_int(data, 0, 1), 0x00)
            self.assertEqual(get_int(data, 1, 1), 0x01)
            self.assertEqual(get_int(data, 0, 2), 0x0100)
            self.assertEqual(get_int(data, 6, 2), 0x0006)
            self.assertEqual(get_int(data, 0, 3), 0x020100)
            self.assertEqual(get_int(data, 5, 3), 0x000605)
            self.assertEqual(get_int(data, 6, 3), 0x000006)

    def test_get_int_empty(self):
        """Test function dqutils.bit.get_int in case of empty value is
        passed.
        """
        self.assertEqual(get_int(b"", 6, 3), 0)
        self.assertEqual(get_int([], 6, 3), 0)

    def test_get_bits(self):
        """Test function dqutils.bit.get_bits."""
        data = [i for i in range(0x06)]
        self.assertEqual(get_bits(data, 0, 0xFF00), 0x0001)
        self.assertEqual(get_bits(data, 1, 0xFFFF), 0x0201)
        self.assertEqual(get_bits(data, 0, 0x0100), 0x0001)
