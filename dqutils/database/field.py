# -*- coding: utf-8 -*-
"""dqutils.database.field (prototype)
"""
from abc import ABCMeta
from abc import abstractmethod
from dqutils.bit import get_bits
from dqutils.bit import get_int

class AbstractField(metaclass=ABCMeta):
    """This class represents a member or field in a data structure.

    Attributes:
      name (string): TBW
      offset (int): TBW
      mask (int): TBW
      type (string): TBW
      format (string): TBW
    """

    def __init__(self, name, **kwargs):
        """The constructor.

        Args:
          name (string): The name of the member or field.
          **kwargs: Arbitrary keyword arguments.
        """

        self.name = name
        self.type = kwargs['type']
        self.offset = kwargs['offset']
        self.mask = kwargs.get('mask')
        self.format = kwargs.get('format', self._do_get_format())

    def __str__(self):
        return '{0:%02X} {1} {2}'.format(self.offset, self.type, self.name)

    @abstractmethod
    def _do_get_format(self):
        """Return the format string."""
        pass

    @abstractmethod
    def _do_get_value(self, byte_string):
        """Return the value passed to the format.

        Args:
          byte_string (bytes): An instance of class bytes.

        Returns:
          TBW
        """
        pass

    def process(self, byte_string):
        """Process bytes and return a text.

        Args:
          byte_string (bytes): An instance of class bytes.

        Returns:
          (string): A formatted value.
        """
        return self.format % self._do_get_value(byte_string)

    def title(self):
        """Return the name of this member or field.

        Returns:
          (string): The name of this instance.
        """
        return self.name

class BitField(AbstractField):
    """This class represents a bit-field member data."""

    def _do_get_format(self):
        self.format = '%X'

    def _do_get_value(self, byte_string):
        return get_bits(byte_string, self.offset, self.mask)

class ByteField(AbstractField):
    """This class represents a byte member data."""

    def _do_get_format(self):
        self.format = '%02X'

    def _do_get_value(self, byte_string):
        return get_int(byte_string, self.offset, 1)

class WordField(AbstractField):
    """This class represents a 2-byte member data."""

    def _do_get_format(self):
        self.format = '%04X'

    def _do_get_value(self, byte_string):
        return get_int(byte_string, self.offset, 2)

class LongField(AbstractField):
    """This class represents a 3-byte member data."""

    def _do_get_format(self):
        self.format = '%06X'

    def _do_get_value(self, byte_string):
        return get_int(byte_string, self.offset, 3)

class BadFieldType(TypeError):
    """An exception type for an unknown field."""

    def __init__(self, bad_type):
        super().__init__()
        self.bad_type = bad_type

    def __str__(self):
        return "no such field type: {0}".format(self.bad_type)

def make_field(name, field_type, **kwargs):
    """Factory method"""

    if field_type in ('bit', 'bits'):
        return BitField(name, **kwargs)
    elif field_type in ('byte', '1byte'):
        return ByteField(name, **kwargs)
    elif field_type in ('word', '2byte'):
        return WordField(name, **kwargs)
    elif field_type in ('long', '3byte'):
        return LongField(name, **kwargs)
    else:
        raise BadFieldType(field_type)
