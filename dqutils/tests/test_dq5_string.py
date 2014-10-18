#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for dqutils.dq5.string
"""

import unittest
from dqutils.dq5.string import enum_string
from dqutils.dq5.string import CONTEXT_PROTOTYPE
from dqutils.dq5.string import CONTEXT_GROUP
from dqutils.dq5.charsmall import CHARMAP
from dqutils.dq5.charsmall import process_dakuten
from dqutils.string import get_text

# pylint: disable=too-many-public-methods
class DQ5StringTestCase(unittest.TestCase):
    """Test functions defined in dqutils.dq5.string."""

    hinokinobou = b'\x2A\x28\x16\x28\x84\x2D\x12'

    def test_enum_string(self):
        """Test function dqutils.dq5.enum_string."""

        context = CONTEXT_GROUP[5]

        addr, code_seq = tuple(enum_string(context, 0, 1))[0]
        self.assertEqual(addr, 0x23CE0E)
        self.assertEqual(code_seq, self.hinokinobou)

    def test_make_text(self):
        """Test function dqutils.dq5.charmapsmall.process_dakuten."""

        context = CONTEXT_GROUP[5]
        charmap = context["charmap"]

        text = process_dakuten(get_text(self.hinokinobou, charmap, None))
        self.assertEqual(text, 'ひのきのぼう')

def test_suite():
    """Setup a test suite."""
    return unittest.makeSuite(DQ5StringTestCase)

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
