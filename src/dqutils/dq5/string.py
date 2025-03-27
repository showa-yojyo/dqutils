"""Module dqutils.dq5.string -- a string loader for DQ5.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

# ruff: noqa: T201
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Final

from dqutils import INVALID_ID
from dqutils.string import get_text
from dqutils.string_generator import StringGeneratorPascalStyle

if TYPE_CHECKING:
    from dqutils.string_generator import StrGenContext, StringInfo
from dqutils.dq5.charsmall import CHARMAP, process_dakuten

CONTEXT_GROUP: Final = (
    # Partners (human beings).
    {"address": 0x23C5CE, "id_first": 0, "id_last": 8},
    # Classes.
    {"address": 0x23C5F9, "id_first": 0, "id_last": 17},
    # Distinction (male/female/others!).
    {"address": 0x23C690, "id_first": 0, "id_last": 3},
    # Spells and skills.
    {"address": 0x228000, "id_first": 0, "id_last": 171},
    # Monsters.
    {"address": 0x23C69C, "id_first": 0, "id_last": 236},
    # Items.
    {"address": 0x23CE0E, "id_first": 0, "id_last": 216},
    # Strategies.
    {"address": 0x23D5B5, "id_first": 0, "id_last": 6},
    # Unknown 1.
    {"address": 0x308000, "id_first": 0, "id_last": 0},
    # Unknown 2.
    {"address": 0x23D6A1, "id_first": 0, "id_last": 0},
    # Ditto.
    {"address": 0x23D6A1, "id_first": 0, "id_last": 0},
    # Partners (monsters).
    {"address": 0x23C242, "id_first": 0, "id_last": 168},
    # Destination list.
    {"address": 0x23D5F3, "id_first": 0, "id_last": 23},
)
"""the string table located at $21955B."""


def enum_string(
    context: StrGenContext,
    first: int = INVALID_ID,
    last: int = INVALID_ID,
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
    yield from StringGeneratorPascalStyle(
        "DRAGONQUEST5",
        context["address"],
        first,
        last,
    )


def print_all() -> None:
    """Print all of the string data to sys.stdout."""

    for groupid, context in enumerate(CONTEXT_GROUP):
        print(f"Group #{groupid:d}")
        for i, entry in enumerate(
            StringGeneratorPascalStyle(
                "DRAGONQUEST5",
                context["address"],
                context["id_first"],
                context["id_last"],
            )
        ):
            address, code_seq = entry
            text = process_dakuten(get_text(code_seq, CHARMAP, None))
            print(f"{i:04X}:{address:06X}:{text}")
