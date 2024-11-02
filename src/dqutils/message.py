"""
This module provides functions that access message data.

There are two kinds of message data in each SNES DRAGONQUEST
programs. They are message data that are used in battle mode and
conversational data. Both are displayed in the message window in the
screen. Battle messages are rendered with the smaller font, while
conversational messages are rendered with the larger font.

For all of the programs, conversational message data are compressed.
"""

from __future__ import annotations

from array import array
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping
    from typing import Any

from dqutils.string import get_hex, get_text
from dqutils.string_generator import StringGeneratorCStyle

if TYPE_CHECKING:
    from dqutils.message_generator import AbstractMessageGenerator, IteratorT
    from dqutils.string_generator import StringInfo


def enum_battle(context: Mapping[str, Any], first: int | None = None, last: int | None = None) -> Iterator[StringInfo]:
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``addr_message``: the address that message data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``message_id_last``:
        this value is referred when `last` is not specified.

    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.

    Yields
    ------
    addr : int
        An offset value of the ROM address space.
    code_seq : bytearray
        A sequence of characters locating in `addr`.
    """
    yield from StringGeneratorCStyle(context, first, last)


def print_battle(context: Mapping[str, Any], first: int | None = None, last: int | None = None) -> None:
    """Print message data to sys.stdout.

    Message data those indices in [`first`, `last`) will be used.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``charmap``: a dict object for character mapping.
      - ``addr_message``: the address that message data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``message_id_last``:
        this value is referred when `last` is not specified.

    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.
    """

    charmap = cast(dict, context["charmap"])
    delims = cast(bytes, context["delimiters"])
    for i, item in enumerate(enum_battle(context, first, last)):
        text = get_text(item[1], charmap, delims) if charmap else get_hex(item[1])
        print(f"{i:04X}:{item[0]:06X}:{text}")


def enum_scenario(
    context: Mapping[str, Any],
    generator_t: type[AbstractMessageGenerator],
    first: int | None = None,
    last: int | None = None,
) -> IteratorT:
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``addr_message``: the address that message data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``message_id_last``:
        this value is referred when `last` is not specified.

    generator_t : `~AbstractMessageGenerator`
        The type of message generator. See the module
        dqutils.message_generator for details.
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.

    Yields
    ------
    addr : int
        The address of the message data.
    shift_bits : int
        The shift from `addr`.
    code_seq : bytearray
        A sequence of characters locating in `addr`.
    """
    yield from generator_t(context, first, last)


def print_scenario(
    context: Mapping[str, Any],
    generator_t: type[AbstractMessageGenerator],
    first: int | None = None,
    last: int | None = None,
) -> None:
    """Print message data to sys.stdout.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    context : dict
      This shall have the following keys:

      - ``title``: the game title.
      - ``addr_message``: the address that message data are stored.
      - ``delimiters``: delimeter characters, in type bytes.

      and the following keys are optional:

      - ``message_id_first``:
        this value is referred when `first` is not specified.
      - ``message_id_last``:
        this value is referred when `last` is not specified.

    generator_t : `~AbstractMessageGenerator`
        The type of message generator. See the module
        dqutils.message_generator for details.
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.
    """

    charmap = cast(dict, context["charmap"])
    delims = cast(array, context["delimiters"])
    for i, item in enumerate(enum_scenario(context, generator_t, first, last)):
        address, shift, code_seq = item
        text = get_text(code_seq, charmap, delims)
        print(f"{i:04X}:{address:06X}:{shift:02X}:{text}")
