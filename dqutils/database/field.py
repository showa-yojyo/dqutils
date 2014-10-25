# -*- coding: utf-8 -*-
"""dqutils.database.field -- Define field classes.
"""
from abc import ABCMeta
from abc import abstractmethod
from dqutils.bit import get_bits
from dqutils.bit import get_int

class AbstractField(metaclass=ABCMeta):
    """This class represents a member data or field in a data structure.

    Attributes:
      name (string): The name of this member data or field.
      offset (int): The offset from the base alignment (in bytes).
      mask (int): A mask value for a bit field.
      format (string): A `sprintf` style formatting string.
    """

    def __init__(self, name, **kwargs):
        """The constructor.

        Args:
          name (string): The name of the member data or field.
          **kwargs: Arbitrary keyword arguments.
        """

        self.name = name
        self.offset = kwargs['offset']
        self.mask = kwargs.get('mask')
        self.format = kwargs.get('format', self._do_get_format())

    def __str__(self):
        return '{0:02X} {1}'.format(self.offset, self.name)

    @classmethod
    @abstractmethod
    def field_type(cls):
        """Return the type name of field."""
        pass

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
          (object): A numeric value.
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

    @classmethod
    def field_type(cls):
        """Return the type name of field."""
        return 'bits'

    def _do_get_format(self):
        self.format = '%X'

    def _do_get_value(self, byte_string):
        return get_bits(byte_string, self.offset, self.mask)

class ByteField(AbstractField):
    """This class represents a byte member data."""

    @classmethod
    def field_type(cls):
        """Return the type name of field."""
        return '1byte'

    def _do_get_format(self):
        self.format = '%02X'

    def _do_get_value(self, byte_string):
        return get_int(byte_string, self.offset, 1)

class WordField(AbstractField):
    """This class represents a 2-byte member data."""

    @classmethod
    def field_type(cls):
        """Return the type name of field."""
        return '2byte'

    def _do_get_format(self):
        self.format = '%04X'

    def _do_get_value(self, byte_string):
        return get_int(byte_string, self.offset, 2)

class LongField(AbstractField):
    """This class represents a 3-byte member data."""

    @classmethod
    def field_type(cls):
        """Return the type name of field."""
        return '3byte'

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

_field_aliases = {
    'bit': 'bits',
    'byte': '1byte',
    'bytes': '1byte',
    'word': '2byte',
    'long': '3byte',
    'address': '3byte'}

def make_field(name, field_type, **kwargs):
    """Make an instance of field class.

    Args:
      name (string): The name of this member data or field.
      field_type (string): The type name of field.
      **kwargs: Keyword arguments passed to the constructor of field class.

    Returns:
      (AbstractField): A field instance.

    Examples:
      >>> params = dict(offset=0x12, mask=0xFFF8, format='%d')
      >>> gold = make_field('Gold', 'bits', **params)
      >>> isinstance(gold, BitField)
      True
    """

    field_type = field_type.lower()
    if field_type in _field_aliases:
        field_type = _field_aliases[field_type]

    for cls in AbstractField.__subclasses__():
        if cls.field_type() == field_type:
            return cls(name, **kwargs)

    raise BadFieldType(field_type)
