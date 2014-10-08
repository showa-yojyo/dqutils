# -*- coding: utf-8 -*-
"""dqutils.dq3.string - DQ3-specific string components.
"""

import dqutils.string
from dqutils.dq3.charsmall import CHARMAP

CONTEXT = dict(
    title="DRAGONQUEST3",
    mapper='HiROM',
    delimiters=b'\xAC',
    charmap=CHARMAP,
    addr_string=0xFECFB7,
    string_id_first=0x0000,
    string_id_last=0x03BE,)

def enum_string(first=None, last=None):
    """A delegating generator.

    See dqutils.string.enum_string for details.

    Args:
      first (optional): The beginning of the range to enumerate strings.
      last (optional): The end of the range to enumerate strings.

    Yields:
      A tuple of (address, shift-bits, character-code).
    """
    yield from dqutils.string.enum_string(CONTEXT, first, last)

def print_all():
    """A transfer function."""
    dqutils.string.print_string(CONTEXT)
