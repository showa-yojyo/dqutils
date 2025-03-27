"""dqutils.dq6.message module"""

from __future__ import annotations

from array import array
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Final

from dqutils import INVALID_ID
from dqutils.dq6.charlarge import CHARMAP as CHARMAP_LARGE
from dqutils.dq6.charsmall import CHARMAP as CHARMAP_SMALL
from dqutils.message import enum_battle as _enum_battle
from dqutils.message import enum_scenario as _enum_scenario
from dqutils.message import print_battle as _print_battle
from dqutils.message import print_scenario as _print_scenario
from dqutils.message_generator import MessageGeneratorW

if TYPE_CHECKING:
    from dqutils.message_generator import IteratorT, MsgGenContext
    from dqutils.string_generator import StrGenContext, StringInfo

CONTEXT_MESSAGE_BATTLE: Final[StrGenContext] = {
    "title": "DRAGONQUEST6",
    "delimiters": b"\xac\xae",
    "id_first": 0x0000,
    "id_last": 0x025B,
    "address": 0xF6DEBD,
}

CONTEXT_MESSAGE_SCENARIO: Final[MsgGenContext] = {
    "title": "DRAGONQUEST6",
    "delimiters": array(
        "H",
        (
            0x00AC,
            0x00AE,
        ),
    ),
    "charmap": CHARMAP_LARGE,
    "decoding_mask": 0xFFFF,
    "id_first": 0x0000,
    "id_last": 0x1B2D,
    "addr_group": 0xC15BB5,
    "addr_shiftbit_array": 0xC02BCC,
    "address": 0xF7175B,
    "addr_huffman_off": 0xC167BE,
    "addr_huffman_on": 0xC1700E,
    "huffman_root": 0x084E,
    "decoding_read_size": 2,
}


def enum_battle(
    first: int = INVALID_ID,
    last: int = INVALID_ID,
) -> Iterator[StringInfo]:
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
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
    yield from _enum_battle(CONTEXT_MESSAGE_BATTLE, first, last)


def print_all_battle() -> None:
    """Print all message data of battle mode to sys.stdout."""
    _print_battle(CONTEXT_MESSAGE_BATTLE, CHARMAP_SMALL)


def enum_scenario(
    first: int = INVALID_ID,
    last: int = INVALID_ID,
) -> IteratorT:
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
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
    yield from _enum_scenario(CONTEXT_MESSAGE_SCENARIO, MessageGeneratorW, first, last)


def print_all_scenario() -> None:
    """Print all message data of conversation mode to sys.stdout."""
    _print_scenario(CONTEXT_MESSAGE_SCENARIO, MessageGeneratorW)
