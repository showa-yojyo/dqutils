# -*- coding: utf-8 -*-
"""dqutils.dq6.string - DQ6-specific string components.
"""

import dqutils.string
from dqutils.dq6.charsmall import CHARMAP

CONTEXT = dict(
    title="DRAGONQUEST6",
    delimiter=b'\xAC',
    charmap=CHARMAP,
    addr_string=0xFB8703,
    string_id_first=0x0000,
    string_id_last=0x09CA,)

def enum_string(first=None, last=None):
    """A transfer generator."""
    for i in dqutils.string.enum_string(CONTEXT, first, last):
        yield i

def print_all():
    """A transfer function."""
    dqutils.string.print_string(CONTEXT)
