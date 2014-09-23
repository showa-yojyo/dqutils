#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""dqutils.dq6.message module

This module provides decoding methods for DQ6 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.

As to DQ6, decoding algorithm is almost the same as DQ5.
The difference between two is just structures of Huffman trees.
"""

from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.bit import readbytes
from dqutils.bit import getbytes
from dqutils.dq6 import open_rom
import mmap

def _is_delimiter(code):
    """Local function"""
    return code == 0xAC or code == 0xAE

#
# Battle message
#

# Address where message data of battle scenes are stored.
LOCATION_MSG_BATTLE = ROMADDR(0xF6DEBD)

def _seek_location(fin, index):
    """Local function"""

    fin.seek(LOCATION_MSG_BATTLE)
    ncount = 0
    while ncount < index:
        code = fin.read(1)[0]
        if _is_delimiter(code):
            ncount += 1

    return CPUADDR(fin.tell())

# Constants for use in the loading methods arguments:
BATTLE_ID_FIRST = 0x0000
BATTLE_ID_LAST = 0x025B

def _verify_input(first, last):
    """Local function"""

    if first < BATTLE_ID_FIRST:
        raise IndexError('out of range:')
    if BATTLE_ID_LAST < last:
        raise IndexError('out of range:')
    if first > last:
        raise IndexError('invalid range:')

def load_battle_msg_code(idfirst=BATTLE_ID_FIRST, idlast=BATTLE_ID_LAST):
    """Help me!"""

    _verify_input(idfirst, idlast)

    # Data to be returned; a list of (cpuaddr, codeseq) pairs.
    data = []
    with open_rom() as fin:
        # Create a memory-mapped file from fin.
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
        cpuaddr = _seek_location(mem, idfirst)

        for _ in range(idfirst, idlast):
            # Huffman codewords of a message
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code = mem.read(1)[0]
                codeseq.append(code)

            data.append((cpuaddr, codeseq))
            # Now update cpuaddr.
            cpuaddr = CPUADDR(mem.tell())
        mem.close()
    return data

def make_text_battle(codeseq):
    """Return a legible string.

    make_text_battle(codeseq) -> str,

    where codeseq is the list of codes that are obtained by
    using load_battle_msg_code method, and str is a text representation.
    """

    from dqutils.dq6.charsmall import CHARMAP
    return ''.join([CHARMAP.get(c, '{:02X}'.format(c)) for c in codeseq])

def load_battle_msg(index):
    """Return a legible string.
    """

    return make_text_battle(load_battle_msg_code(index, index + 1)[0][1])

def print_all_battle():
    """Demonstration method by the author, for the author."""

    data = load_battle_msg_code()
    for i, pair in enumerate(data):
        # Remove delimiter codes (AC and AE).
        codeseq = pair[1]
        codeseq.pop()
        print('{0:04X}:{1:06X}:{2}'.format(i, pair[0], make_text(codeseq)))

#
# Conversation, dialog, system messages
#

_LOC_GROUP = ROMADDR(0xC15BB5)
_LOC_SHIFT = ROMADDR(0xC02BCC)
_LOC_DATA = 0xF7175B

def _get_cpuaddr(msgid, fin):
    """Return the location where the messege data is stored.

    _get_cpuaddr(msgid, fin) -> cpuaddr, shift
        msgid: ID of a message data
        fin: ROM image
        cpuaddr: Location by ROM address
        shift: bit for shift operation
    """

    count = msgid & 0x0007
    group = msgid >> 3
    group += (group << 1)

    fin.seek(_LOC_GROUP + group)
    buffer1 = readbytes(fin, 3)

    # from shiftbit array
    # {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80}
    if not getattr(_get_cpuaddr, "SHIFTBIT_ARRAY", None):
        fin.seek(_LOC_SHIFT)
        _get_cpuaddr.SHIFTBIT_ARRAY = readbytes(fin, 8)

    shift = _get_cpuaddr.SHIFTBIT_ARRAY[buffer1[0] & 0x07]

    cpuaddr = (getbytes(buffer1, 0, 3) >> 3) + _LOC_DATA

    # The loop counter depends on msgid % 7.
    for count in range(count):
        code = 0
        while not _is_delimiter(code):
            # この関数は重いので注意
            code, cpuaddr, shift = _decode(cpuaddr, shift, fin)

    return cpuaddr, shift

MSG_ID_FIRST = 0x0000
MSG_ID_LAST = 0x1B2D

def _verify_msg_id(first, last):
    """Local function"""

    if first < MSG_ID_FIRST:
        raise IndexError('out of range:')
    if MSG_ID_LAST < last:
        raise IndexError('out of range:')
    if first > last:
        raise IndexError('invalid range:')

def load_msg_code(idfirst=MSG_ID_FIRST, idlast=MSG_ID_LAST):
    """Return a list of pairs (cpuaddr, codeseq).

    load_msg_code(idfirst, idlast) -> a list of (cpuaddr, codeseq).
    """

    _verify_msg_id(idfirst, idlast)

    # Data to be returned.
    data = []
    with open_rom() as fin:
        # Create a memory-mapped file from fin.
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        # Obtain the first data location.
        cpuaddr, shift = _get_cpuaddr(idfirst, mem)

        for _ in range(idfirst, idlast):
            cpuaddr0, shift0 = cpuaddr, shift
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code, cpuaddr, shift = _decode(cpuaddr, shift, mem)
                codeseq.append(code)
            data.append((cpuaddr0, shift0, codeseq))
        # Close mmap object.
        mem.close()
    return data

def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of codes that are obtained by
    using load_msg_code method, and str is a text representation.
    """
    from dqutils.dq6.charlarge import CHARMAP
    return ''.join([CHARMAP.get(c, '{:02X}'.format(c)) for c in codeseq])

def load_msg(index):
    """Return a legible string.

    load_msg(index) <==> make_text(load_msg_code(index, index + 1)[0][1])
    """

    return make_text(load_msg_code(index, index + 1)[0][-1])

def print_all():
    """Demonstration method by the author, for the author."""

    data = load_msg_code()
    for i, tup in enumerate(data):
        # Remove delimiter code (AC and AE).
        codeseq = tup[-1]
        shift = tup[1]
        codeseq.pop()
        print('{0:04X}:{1:06X}:{2:02X}:{3}'.format(
            i, tup[0], shift, make_text(codeseq)))

_LOC_BIT_OFF = ROMADDR(0xC167BE)
_LOC_BIT_ON = ROMADDR(0xC1700E)
_ROOT = 0x084E

def _init_tree(fin):
    """(Local function) Initialize Huffman tree data."""

    if not getattr(_init_tree, "HUFFMAN_OFF", None):
        # ファイルからバイト列を抽出
        fin.seek(_LOC_BIT_OFF)
        _init_tree.HUFFMAN_OFF = readbytes(fin, _ROOT + 2)

    if not getattr(_init_tree, "HUFFMAN_ON", None):
        fin.seek(_LOC_BIT_ON)
        _init_tree.HUFFMAN_ON = readbytes(fin, _ROOT + 2)

    assert len(_init_tree.HUFFMAN_ON) == _ROOT + 2
    assert len(_init_tree.HUFFMAN_OFF) == _ROOT + 2
    return _init_tree.HUFFMAN_ON, _init_tree.HUFFMAN_OFF

def _decode(cpuaddr, shift, fin, dump_shift_bit=False):
    """Decoding algorithm of Huffman coding."""

    assert cpuaddr & 0xFF000000 == 0
    assert shift & 0xFFFFFF00 == 0

    huffman_on, huffman_off = _init_tree(fin)

    node = _ROOT
    while True:
        fin.seek(ROMADDR(cpuaddr))
        buffer = readbytes(fin, 2)
        value = getbytes(buffer, 0, 2) & shift

        if dump_shift_bit:
            print('{:02X}'.format(shift), end='')
            if value:
                print(1, end='')
            else:
                print(0, end='')

        shift >>= 1
        if shift == 0:
            shift = 0x0080
            cpuaddr += 1

        if value:
            value = getbytes(huffman_on, node, 2)
        else:
            value = getbytes(huffman_off, node, 2)

        if value & 0x8000 == 0:
            if dump_shift_bit:
                print('{:04X}'.format(value))

            return value, cpuaddr, shift

        node = value & 0x7FFF
        # endwhile

if __name__ == '__main__':
    print_all()
