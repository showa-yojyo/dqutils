# -*- coding: utf-8 -*-
"""dqutils.dq3.string - DQ3-specific string components.
"""

import dqutils.string
from dqutils.dq3.charsmall import CHARMAP as CHARMAP_SMALL

# pylint: disable=too-few-public-methods
class Context(object):
    """TBW"""

    def __init__(self):
        self.entries = dict(
            TITLE="DRAGONQUEST3",

            # Delimeter character code.
            STRING_DELIMITER=b'\xAC',
            STRING_CHARMAP=CHARMAP_SMALL,

            # Location at where string data are stored.
            STRING_ADDRESS=0xFECFB7,

            # Range of the valid indices. [first, last) form.
            STRING_INDEX_FIRST=0x0000,
            STRING_INDEX_LAST=0x03BE,)

    def __contains__(self, key):
        return key in self.entries

    def __getitem__(self, key):
        return self.entries[key]

CONTEXT = Context()

def get_text(code_seq, delim=None):
    """A transfer function."""
    return dqutils.string.get_text(
        code_seq, CONTEXT["STRING_CHARMAP"], delim)

def enum_string(mem, first, last):
    """A transfer function."""
    return dqutils.string.enum_string(
        mem, first, last,
        CONTEXT["STRING_ADDRESS"],
        CONTEXT["STRING_DELIMITER"])

def print_all():
    """A transfer function."""
    dqutils.string.print_string(CONTEXT)
