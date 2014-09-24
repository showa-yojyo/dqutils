# -*- coding: utf-8 -*-
"""dqutils.dq6.string - DQ6-specific string components.
"""

import dqutils.string
from dqutils.dq6 import open_rom
from dqutils.dq6.charsmall import CHARMAP

# Constant variables.

# Delimeter character code.
DELIMITER_CODE = b'\xac'

# Location at where string data are stored.
STRING_BASE_ADDRESS = 0xFB8703

# Range of the valid indices. [first, last) form.
STRING_INDEX_FIRST = 0x0000
STRING_INDEX_LAST = 0x09CA

def get_text(code_seq, delim=None):
    """A transfer function."""
    return dqutils.string.get_text(code_seq, CHARMAP, delim)

def enum_string(mem, first, last):
    """A transfer function."""
    return dqutils.string.enum_string(
        mem, first, last, STRING_BASE_ADDRESS, DELIMITER_CODE)

def print_all():
    """A transfer function."""
    dqutils.string.print_string(
        open_rom,
        first=STRING_INDEX_FIRST,
        last=STRING_INDEX_LAST,
        base_addr=STRING_BASE_ADDRESS,
        charmap=CHARMAP,
        delim=DELIMITER_CODE)
