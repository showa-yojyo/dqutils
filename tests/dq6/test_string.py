"""Tests for dqutils.dq6.string"""

from unittest import TestCase

from dqutils.dq6.string import CONTEXT, enum_string
from dqutils.string import get_text


class DQ6StringTestCase(TestCase):
    """Test functions defined in dqutils.dq6.string."""

    def test_get_text(self):
        """Test function dqutils.dq6.get_text."""

        text = get_text(b"\x2a\x28\x16\x28\xdc\x12\xac", CONTEXT["charmap"], CONTEXT["delimiters"])
        self.assertTrue("ひのきのぼう" in text)

    def test_enum_string(self):
        """Test function dqutils.dq6.enum_string."""

        testdata = tuple(enum_string(0x300, 0x310))

        self.assertEqual(testdata[0][0], 0xFB97DB)
        self.assertTrue("ムドー" in get_text(testdata[0][1], CONTEXT["charmap"], CONTEXT["delimiters"]))

        self.assertEqual(testdata[15][0], 0xFB9835)
        self.assertTrue("デュラン" in get_text(testdata[15][1], CONTEXT["charmap"], CONTEXT["delimiters"]))
