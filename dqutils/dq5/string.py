# -*- coding: utf-8 -*-

"""Module dqutils.dq5.string -- a string loader for DQ5.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_hi
from dqutils.address import from_lo
from dqutils.address import conv_hi
from dqutils.address import conv_lo
from dqutils.rom_image import RomImage
from dqutils.string import get_text
from dqutils.dq5.charsmall import CHARMAP
from dqutils.dq5.charsmall import process_dakuten
from dqutils.string_generator import StringGeneratorPascalStyle
import dqutils.string

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
    mapper='LoROM',
    charmap=CHARMAP,)

for group in CONTEXT_GROUP:
    group.update(CONTEXT_PROTOTYPE)

def enum_string(context, first=None, last=None):
    """A delegating generator.

    See dqutils.string.enum_string for details.

    Args:
      context: The information of the string table to enumerate.
      first (optional): The beginning of the range to enumerate strings.
      last (optional): The end of the range to enumerate strings.

    Yields:
      A tuple of (address, shift-bits, character-code).
    """
    yield from dqutils.string.enum_string(
        context, StringGeneratorPascalStyle, first, last)

def print_all():
    """Print all of the strings in DQ5 to sys.stdout."""

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
