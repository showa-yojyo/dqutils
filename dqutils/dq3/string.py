"""dqutils.dq3.string - DQ3-specific string components.
"""

from ..string import (enum_string as _enum_string,
                            print_string as _print_string)
from ..string_generator import StringGeneratorCStyle
from .charsmall import CHARMAP

CONTEXT = dict(
    title="DRAGONQUEST3",
    delimiters=b'\xAC',
    charmap=CHARMAP,
    addr_string=0xFECFB7,
    string_id_first=0x0000,
    string_id_last=0x03BE,)

def enum_string(first=None, last=None):
    """Return generator iterators of string data by specifying
    their indices.

    String data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.

    Yields
    ------
    i : int
        The next CPU address of data in the range of 0 to `last` - 1.
    b : bytearray
        The next bytes of data in the range of 0 to `last` - 1.
    """
    yield from _enum_string(
        CONTEXT, StringGeneratorCStyle, first, last)

def print_all():
    """Print all of the string data to sys.stdout."""
    _print_string(CONTEXT, StringGeneratorCStyle)
