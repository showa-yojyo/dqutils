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
    """A transfer generator."""
    for i in dqutils.string.enum_string(CONTEXT, first, last):
        yield i

def print_all():
    """A transfer function."""
    dqutils.string.print_string(CONTEXT)
