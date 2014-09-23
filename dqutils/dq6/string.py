#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Module dqutils.dq6.string -- a string loader for DQ6.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.dq6 import open_rom
import mmap

# 0xAC is the only delimiter code.
def _is_delimiter(code):
    """Local function"""
    return code == 0xAC

# Location at where string data are stored.
_LOCSTR = ROMADDR(0xFB8703)

def _seekloc(fin, index):
    """Local function"""

    fin.seek(_LOCSTR)
    ncount = 0
    while ncount < index:
        code = fin.read(1)[0]
        if _is_delimiter(code):
            ncount += 1

    return CPUADDR(fin.tell())

# Constants for the loading method arguments:
ID_FIRST = 0x0000
ID_LAST = 0x09CA

def load_code(index):
    """Return a string as an array of raw codes.

    load_code(index) -> (loc, codeseq),

    where loc is the CPU address (mapped to HiROM) at where the bytes
    locate and codeseq is the list of raw codes ends with the delimiter
    code 0xAC.

    index MUST in xrange(ID_FIRST, ID_LAST).
    """

    if index < ID_FIRST or ID_LAST <= index:
        raise IndexError('out of range')

    loc = 0
    with open_rom() as fin:
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
        loc = _seekloc(mem, index)

        codeseq = []
        code = 0
        while not _is_delimiter(code):
            code = mem.read(1)[0]
            codeseq.append(code)
        mem.close()
    return loc, codeseq

def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of raw codes that are obtained by
    using load_code method, and str is a text representation.
    """

    from dqutils.dq6.charsmall import CHARMAP
    return ''.join([CHARMAP.get(c, '{:02X}'.format(c)) for c in codeseq])

def load_string(index):
    """Return a legible string.
    """
    return make_text(load_code(index)[1])

# Demonstration method (by the author, for the author)

def print_all():
    """Print all of the strings in DQ6 to sys.stdout."""

    for i in range(ID_FIRST, ID_LAST):
        loc, codeseq = load_code(i)
        codeseq.pop()  # remove delimiter code (AC)
        text = make_text(codeseq)
        print('{0:04X}:{1:06X}:{2}'.format(i, loc, text))

if __name__ == '__main__':
    print_all()
