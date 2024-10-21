"""dqutils.dq6.string - DQ6-specific string components.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Iterator

from ..string import (enum_string as _enum_string,
                      print_string as _print_string)
from ..string_generator import StringGeneratorCStyle
from .charsmall import CHARMAP

if TYPE_CHECKING:
    from ..string_generator import StringInfo

CONTEXT = dict(
    title="DRAGONQUEST6",
    delimiters=b'\xAC',
    charmap=CHARMAP,
    addr_string=0xFB8703,
    string_id_first=0x0000,
    string_id_last=0x09CA,)

def enum_string(
        first: int | None=None,
        last: int | None=None
        ) -> Iterator[StringInfo]:
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

def print_string(
        first: int | None=None,
        last: int | None=None
        ) -> None:
    """Print string data to sys.stdout.

    String data those indices in [`first`, `last`) will be used.

    Parameters
    ----------
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.
    """
    _print_string(CONTEXT, StringGeneratorCStyle, first, last)

def print_all() -> None:
    """Print all of the string data to sys.stdout."""
    print_string()
