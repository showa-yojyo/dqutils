#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Module dqutils.dq5.string -- a string loader for DQ5.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_lo as CPUADDR
from dqutils.address import conv_lo as ROMADDR
from dqutils.bit import readbytes
from dqutils.dq5 import open_rom
import mmap

# the string table map at $21955B
GROUPS = (
    (0x23C5CE, 8), # 仲間の名前
    (0x23C5F9, 17), # 職業名
    (0x23C690, 3), # 性別
    (0x228000, 171), # じゅもん・とくぎの名前
    (0x23C69C, 236), # モンスター名
    (0x23CE0E, 216), # アイテム名
    (0x23D5B5, 6), # さくせん名
    (0x308000, 0), # 不明 1
    (0x23D6A1, 0), # 不明 2
    (0x23D6A1, 0), # 同上
    (0x23C242, 168), # 仲間モンスターの名前
    (0x23D5F3, 23), # ルーラ行き先
)

# Constants for use in the loading methods arguments:
GROUP_FIRST = 0
GROUP_LAST = len(GROUPS)

def load_code(group):
    """Obtain all raw codes of a section of string table.
    """

    if group < GROUP_FIRST or group >= GROUP_LAST:
        raise IndexError('invalid group: ' + repr(group))

    # Data to be returned.
    data = []

    with open_rom() as fin:
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
        cpuaddr = GROUPS[group][0]
        mem.seek(ROMADDR(cpuaddr))

        ncount = GROUPS[group][1]
        for _ in range(ncount):
            nchar = mem.read(1)[0]
            if nchar:
                loc = CPUADDR(mem.tell())
                codes = readbytes(mem, nchar)
                data.append((loc, codes))
        mem.close()
    return data

def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of raw codes that are obtained by
    using load_code method, and str is a text representation.
    """
    from dqutils.dq5.charsmall import CHARMAP
    from dqutils.dq5.charsmall import process_dakuten
    return process_dakuten(
        ''.join([CHARMAP.get(c, '{:02X}'.format(c)) for c in codeseq]))

# Demonstration method (by the author, for the author).

def print_all():
    """Print all of the strings in DQ5 to sys.stdout."""

    for group in range(GROUP_FIRST, GROUP_LAST):
        print('Group #{0:d} ({1:06X})'.format(group, GROUPS[group][0]))
        pairs = load_code(group) # A list of (location, codeseq) pairs.
        for i, pair in enumerate(pairs):
            # Print id, location, and legible text.
            print('{0:04X}:{1:06X}:{2}'.format(i, pair[0], make_text(pair[1])))

if __name__ == '__main__':
    print_all()
