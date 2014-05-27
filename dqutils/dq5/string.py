#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

"""Module dqutils.dq6.string -- a string loader for DQ6.

A string is an array of characters that are rendered with the small font.

This module has a few of functions capable to load strings in the form of
both raw bytes or texts legible to human.
"""

from __future__ import with_statement
from dqutils.address import from_lo as CPUADDR
from dqutils.address import conv_lo as ROMADDR
from dqutils.bit import readbytes
from dqutils.dq5 import open_rom
import mmap

# the string table map at $21955B
GROUPS = (
    (0x23C5CE,   8),  # 仲間の名前
    (0x23C5F9,  17),  # 職業名
    (0x23C690,   3),  # 性別
    (0x228000, 171),  # じゅもん・とくぎの名前
    (0x23C69C, 236),  # モンスター名
    (0x23CE0E, 216),  # アイテム名
    (0x23D5B5,   6),  # さくせん名
    (0x308000,   0),  # 不明 1
    (0x23D6A1,   0),  # 不明 2
    (0x23D6A1,   0),  # 同上
    (0x23C242, 168),  # 仲間モンスターの名前
    (0x23D5F3,  23),  # ルーラ行き先
)

# Constants for use in the loading methods arguments:
GROUP_FIRST = 0
GROUP_LAST  = len(GROUPS)


def load_code(group):
    """Obtain all raw codes of a section of string table

    """
    if group < GROUP_FIRST or group >= GROUP_LAST:
        raise RuntimeError, 'invalid group: ' + repr(group)

    # data to be returned
    data = []

    with open_rom() as fin:
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)
        cpuaddr = GROUPS[group][0]
        mem.seek(ROMADDR(cpuaddr))

        ncount = GROUPS[group][1]
        for i in xrange(ncount):
            nchar = ord(mem.read(1)[0])
            if nchar:
                loc = CPUADDR(mem.tell())
                codes = readbytes(mem, nchar)
                data.append((loc, codes))
        mem.close()
    return data


def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of raw codes that is obtained by
    using load_code method and str is text representation.
    """
    from dqutils.dq5.charsmall import charmap, process_dakuten
    return process_dakuten(u''.join([charmap.get(c, u'[%02X]' % c) for c in codeseq]))


# Demonstration method (by the author, for the author)

def print_all():
    """Print all of the strings in DQ5 to sys.stdout."""

    for group in xrange(GROUP_FIRST, GROUP_LAST):
        print u'Group #%d (%06X)' % (group, GROUPS[group][0])
        pairs = load_code(group) # a list of (location, codeseq) pairs
        for i, pair in enumerate(pairs):
            # print id, location, and legible text
            print u'%04X:%06X:%s' % (i, pair[0], make_text(pair[1]))
        print  # a blank line

if __name__ == '__main__':
    print_all()
