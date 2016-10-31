"""Tests for dqutils.database.field module."""
import unittest
from ..field import (make_field,
                     BitField,
                     ByteField,
                     WordField,
                     LongField,
                     BadFieldType)

# pylint: disable=too-many-public-methods
class FieldTestCase(unittest.TestCase):
    """Test classes and functions defined in dqutils.database.field."""

    def setUp(self):
        """Prepare the test fixture."""

        self.params = dict(offset=0x12, mask=0xFFF8, format='%d')

    def test_make_field_for_bitfield(self):
        """Test function dqutils.database.field.make_field."""

        for i in ('bit', 'bits'):
            self.assertIsInstance(
                make_field('X', i, **self.params), BitField)

    def test_make_field_for_bytefield(self):
        """Test function dqutils.database.field.make_field."""

        for i in ('byte', 'bytes', '1byte'):
            self.assertIsInstance(
                make_field('X', i, **self.params), ByteField)

    def test_make_field_for_wordfield(self):
        """Test function dqutils.database.field.make_field."""

        for i in ('word', '2byte'):
            self.assertIsInstance(
                make_field('X', i, **self.params), WordField)

    def test_make_field_for_longfield(self):
        """Test function dqutils.database.field.make_field."""

        for i in ('long', 'address', '3byte'):
            self.assertIsInstance(
                make_field('X', i, **self.params), LongField)

    def test_make_field_exception(self):
        """Test that BadFieldType is raised."""

        self.assertRaises(
            BadFieldType, make_field, 'X', 'dummy', kwargs=self.params)
