# -*- coding: utf-8 -*-
"""dqutils.dq6.string - DQ6-specific string components.
"""

import dqutils.string
from dqutils.dq6.charsmall import CHARMAP
from dqutils.string_generator import StringGeneratorCStyle

CONTEXT = dict(
    title="DRAGONQUEST6",
    mapper='HiROM',
    delimiters=b'\xAC',
    charmap=CHARMAP,
    addr_string=0xFB8703,
    string_id_first=0x0000,
    string_id_last=0x09CA,)

def enum_string(first=None, last=None):
    """A delegating generator.

    See dqutils.string.enum_string for details.

    Args:
      first (optional): The beginning of the range to enumerate strings.
      last (optional): The end of the range to enumerate strings.

    Yields:
      A tuple of (address, shift-bits, character-code).
    """
    yield from dqutils.string.enum_string(
        CONTEXT, StringGeneratorCStyle, first, last)

def print_all():
    """A delegating function.

    See dqutils.string.print_string for details.
    """
    dqutils.string.print_string(CONTEXT, StringGeneratorCStyle)
