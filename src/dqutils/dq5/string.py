"""Module dqutils.dq5.string -- a string loader for DQ5.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from ..string import (enum_string as _enum_string,
                      get_text)
from ..string_generator import StringGeneratorPascalStyle
from .charsmall import (CHARMAP, process_dakuten)

CONTEXT_GROUP = [
    # Partners (human beings).
    dict(addr_string=0x23C5CE, string_id_first=0, string_id_last=8),
    # Classes.
    dict(addr_string=0x23C5F9, string_id_first=0, string_id_last=17),
    # Distinction (male/female/others!).
    dict(addr_string=0x23C690, string_id_first=0, string_id_last=3),
    # Spells and skills.
    dict(addr_string=0x228000, string_id_first=0, string_id_last=171),
    # Monsters.
    dict(addr_string=0x23C69C, string_id_first=0, string_id_last=236),
    # Items.
    dict(addr_string=0x23CE0E, string_id_first=0, string_id_last=216),
    # Strategies.
    dict(addr_string=0x23D5B5, string_id_first=0, string_id_last=6),
    # Unknown 1.
    dict(addr_string=0x308000, string_id_first=0, string_id_last=0),
    # Unknown 2.
    dict(addr_string=0x23D6A1, string_id_first=0, string_id_last=0),
    # Ditto.
    dict(addr_string=0x23D6A1, string_id_first=0, string_id_last=0),
    # Partners (monsters).
    dict(addr_string=0x23C242, string_id_first=0, string_id_last=168),
    # Destination list.
    dict(addr_string=0x23D5F3, string_id_first=0, string_id_last=23),
    ]
"""the string table located at $21955B."""

CONTEXT_PROTOTYPE = dict(
    title="DRAGONQUEST5",
    charmap=CHARMAP,)

for group in CONTEXT_GROUP:
    group.update(CONTEXT_PROTOTYPE)

def enum_string(context, first=None, last=None):
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
        context, StringGeneratorPascalStyle, first, last)

def print_all():
    """Print all of the string data to sys.stdout."""

    for i, context in enumerate(CONTEXT_GROUP):
        print('Group #{0:d}'.format(i))

        charmap = context["charmap"]
        assert charmap is None or isinstance(charmap, dict)

        for j, item in enumerate(StringGeneratorPascalStyle(context)):
            text = process_dakuten(get_text(item[1], charmap, None))
            print('{index:04X}:{address:06X}:{data}'.format(
                index=j,
                address=item[0],
                data=text))
