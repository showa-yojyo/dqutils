"""
This module defines common functions that access string data.

A string is an array of characters that is rendered in several
windows with the smaller font.

This module provides functions capable to load strings either in
forms of raw bytes or human-readable texts.
"""

from __future__ import annotations

from array import array
from typing import TYPE_CHECKING

from dqutils import INVALID_ID

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

    from dqutils.string_generator import AbstractStringGenerator, StrGenContext, StringInfo

type CodeSeq = bytes | bytearray | array[int]


def get_text(
    code_seq: CodeSeq,
    charmap: Mapping[int, str],
    delims: CodeSeq | None = None,
) -> str:
    """Return a text representation of a string.

    Parameters
    ----------
    code_seq : str
        A string (instance of bytearray).
    charmap : dict
        The character dictionary.
    delims : iterable of str, optional
        The code of the delimiter characters.

    Returns
    -------
    text : str
        A human-readble text, e.g. "ひのきのぼう".
    """

    if delims and code_seq[-1] in delims:
        code_seq = code_seq[0:-1]

    return "".join(charmap.get(c, f"[{c:02X}]") for c in code_seq)


def get_hex(code_seq: CodeSeq) -> str:
    """Return a hex representation of a string.

    This function does not remove the delimiter code.

    Parameters
    ----------
    code_seq : bytearray
        A sequence of character codes.

    Returns
    -------
    dump : str
        E.g. "26 24 12 24 DC 0E AC".
    """
    return " ".join(f"{c:02X}" for c in code_seq)


def enum_string(
    context: StrGenContext,
    generator_t: type[AbstractStringGenerator],
    first: int = INVALID_ID,
    last: int = INVALID_ID,
) -> Iterator[StringInfo]:
    """Return generator iterators of string data by specifying
    their indices.

    String data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``address``: the address that string/data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``id_first``:
        this value is referred when `first` is not specified.
      - ``id_last``:
        this value is referred when `last` is not specified.

    generator_t : `~AbstractStringGenerator`
        The type of string generator. See the module
        dqutils.string_generator for details.
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

    yield from generator_t(context, first, last)


def print_string(
    context: StrGenContext,
    generator_t: type[AbstractStringGenerator],
    charmap: Mapping[int, str],
    first: int = INVALID_ID,
    last: int = INVALID_ID,
) -> None:
    """Print string data to sys.stdout.

    String data those indices in [`first`, `last`) will be used.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``address``: the address that string/data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``id_first``:
        this value is referred when `first` is not specified.
      - ``id_last``:
        this value is referred when `last` is not specified.

    generator_t : `~AbstractStringGenerator`
        The type of string generator. See the module
        dqutils.string_generator for details.
    charmap :
        a dict object for character mapping.
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.
    """

    delim = context["delimiters"]
    if first == INVALID_ID:
        first = 0
    for i, item in enumerate(generator_t(context, first, last), first):
        text = get_text(item[1], charmap, delim) if charmap else get_hex(item[1])
        print(f"{i:04X}:{item[0]:06X}:{text}")  # noqa: T201
