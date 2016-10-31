"""
Tests for dqutils.snescpu.addressing.
"""

from unittest import TestCase
from ..addressing import (ADDRESSING_MODE_TABLE,
                          get_addressing_mode)

# pylint: disable=too-many-public-methods
class TestAddressing(TestCase):
    """Tests for dqutils.snescpu.addressing."""

    def test_basic(self):
        """Test basic behaviors of get_addressing_mode."""

        addrmode = get_addressing_mode('Immediate')
        self.assertTrue(addrmode)

        # Intentionally add extra space characters.
        addrmode = get_addressing_mode(' Absolute Long   ')
        self.assertTrue(addrmode)

    def test_invalid_args(self):
        """Test get_addressing_mode for invalid arguments."""

        self.assertRaises(KeyError, get_addressing_mode, 'XYZ')

    def test_properties(self):
        """Test AbstractAddressingMode for its properties."""

        for mode in ADDRESSING_MODE_TABLE:
            name, syntax, formatter = mode

            addrmode = get_addressing_mode(name)
            self.assertIsNotNone(addrmode)
            self.assertEqual(addrmode.name, name.strip())
            self.assertEqual(addrmode.syntax, syntax.strip())

            if formatter:
                self.assertEqual(addrmode.formatter.__name__,
                                 formatter.__func__.__name__)
            else:
                self.assertIsNone(addrmode.formatter)
