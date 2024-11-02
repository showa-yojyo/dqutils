"""
This module defines common functions that access string data.

A string is an array of characters that is rendered in several
windows with the smaller font.

This module provides functions capable to load strings either in
forms of raw bytes or human-readable texts.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from array import array
    from collections.abc import Iterator, Mapping
    from typing import Any

    type CodeSeq = bytes | bytearray | array

    from dqutils.string_generator import AbstractStringGenerator, StringInfo


def get_text(code_seq: CodeSeq, charmap: Mapping[int, str], delims: CodeSeq | None = None) -> str:
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
    context: Mapping[str, Any],
    generator_t: type[AbstractStringGenerator],
    first: int | None = None,
    last: int | None = None,
) -> Iterator[StringInfo]:
    """Return generator iterators of string data by specifying
    their indices.

    String data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``addr_string`` or ``addr_message``: the address that
        string data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``string_id_first`` or ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``string_id_last`` or ``message_id_last``:
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
    context: Mapping[str, Any],
    generator_t: type[AbstractStringGenerator],
    first: int | None = None,
    last: int | None = None,
) -> None:
    """Print string data to sys.stdout.

    String data those indices in [`first`, `last`) will be used.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``charmap``: a dict object for character mapping.
      - ``addr_string`` or ``addr_message``: the address that
        string data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``string_id_first`` or ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``string_id_last`` or ``message_id_last``:
        this value is referred when `last` is not specified.

    generator_t : `~AbstractStringGenerator`
        The type of string generator. See the module
        dqutils.string_generator for details.
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.
    """

    delim = cast(bytes, context["delimiters"])
    charmap = cast(dict[int, str], context["charmap"])
    start = 0 if first is None else int(first)
    for i, item in enumerate(generator_t(context, start, last), start):
        text = get_text(item[1], charmap, delim) if charmap else get_hex(item[1])
        print(f"{i:04X}:{item[0]:06X}:{text}")
