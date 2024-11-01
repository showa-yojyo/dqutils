"""dqutils.dq6.message module"""

from __future__ import annotations

from array import array
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Final

from ..message import (
    enum_battle as _enum_battle,
    enum_scenario as _enum_scenario,
    print_battle as _print_battle,
    print_scenario as _print_scenario,
)
from ..message_generator import MessageGeneratorW
from .charsmall import CHARMAP as CHARMAP_SMALL
from .charlarge import CHARMAP as CHARMAP_LARGE

if TYPE_CHECKING:
    from ..string_generator import StringInfo
    from ..message_generator import IteratorT

CONTEXT_MESSAGE_BATTLE: Final[dict] = dict(
    title="DRAGONQUEST6",
    delimiters=b"\xac\xae",
    charmap=CHARMAP_SMALL,
    message_id_first=0x0000,
    message_id_last=0x025B,
    addr_message=0xF6DEBD,
    decoding_read_size=2,
)

CONTEXT_MESSAGE_SCENARIO: Final[dict] = dict(
    title="DRAGONQUEST6",
    delimiters=array(
        "H",
        (
            0x00AC,
            0x00AE,
        ),
    ),
    charmap=CHARMAP_LARGE,
    message_id_first=0x0000,
    message_id_last=0x1B2D,
    addr_group=0xC15BB5,
    addr_shiftbit_array=0xC02BCC,
    addr_message=0xF7175B,
    addr_huffman_off=0xC167BE,
    addr_huffman_on=0xC1700E,
    huffman_root=0x084E,
    decoding_read_size=2,
)


def enum_battle(first: int | None = None, last: int | None = None) -> Iterator[StringInfo]:
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
    _print_battle(CONTEXT_MESSAGE_BATTLE)


def enum_scenario(first: int | None = None, last: int | None = None) -> IteratorT:
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
