#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$

"""Module dqutils.dq3.string -- a string loader for DQ3.

A string is an array of characters that are rendered with the small font.

This module has a few of functions capable to load strings in the form of
both raw bytes or texts legible to human.
"""

from __future__ import with_statement
from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.dq3 import open_rom
import mmap

# 0xAC is the only delimiter code.
def _is_delimiter(code):
    return code == 0xAC


# Location at where string data are stored
_LOCSTR = ROMADDR(0xFECFB7)


def _seekloc(fin, id):
    """Local method"""

    fin.seek(_LOCSTR)
    ncount = 0
    while ncount < id:
        code = ord(fin.read(1)[0])
        if _is_delimiter(code):
            ncount += 1

    return CPUADDR(fin.tell())


# Constants for use in the loading methods arguments:
ID_FIRST = 0x0000
ID_LAST  = 0x03BE

def load_code(id):
    """Return a string as an array of raw codes.

    load_code(id) -> (loc, codeseq),

    where loc is the CPU address (mapped to HiROM) at where the bytes
    locate and codeseq is the list of raw codes ends with the delimiter
    code 0xAC.

    id MUST in xrange(ID_FIRST, ID_LAST).
    """

    if id < ID_FIRST or ID_LAST <= id:
        raise RuntimeError, 'out of range'

    loc = 0
    with open_rom() as fin:
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)
        loc = _seekloc(mem, id)

        codeseq = []
        code = 0
        while not _is_delimiter(code):
            code = ord(mem.read(1)[0])
            codeseq.append(code)
        mem.close()
    return loc, codeseq


def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of raw codes that is obtained by
    using load_code method and str is text representation.
    """

    from dqutils.dq3.charsmall import charmap
    return u''.join([charmap.get(c, u'[%02X]' % c) for c in codeseq])


def load_string(id):
    """Return a legible string.

    load_string(id) <==> make_text(load_code(id)[1])
    """
    return make_text(load_code(id)[1])


# Demonstration method (by the author, for the author)

def print_all():
    """Print all of the strings in DQ3 to sys.stdout."""

    for id in xrange(ID_FIRST, ID_LAST):
        loc, codeseq = load_code(id)
        codeseq.pop()  # remove delimiter code (AC)
        text = make_text(codeseq)
        print u'%04X:%06X:%s' % (id, loc, text)


if __name__ == '__main__':
    print_all()
