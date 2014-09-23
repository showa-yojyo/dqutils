#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""dqutils.dq5.message module

This module provides decoding methods for DQ6 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.

The decoding algorithm is based on classical Huffman's method.

Special thanks to Mr. kobun_c.
"""

from dqutils.address import conv_lo as ROMADDR
from dqutils.bit import readbytes
from dqutils.bit import getbits
from dqutils.bit import getbytes
from dqutils.dq5 import open_rom
import mmap

#
# Conversation, dialog, system messages
#

def _is_delimiter(code):
    """Local function"""
    return code == 0x1001 or code == 0x1010 or code == 0x1018

_LOC_GROUP = ROMADDR(0x24AF1E)

def _get_cpuaddr(msgid, fin):
    """Local function dq5 $248BAF"""

    group = msgid // 16 * 3
    fin.seek(_LOC_GROUP + group)
    buffer1 = readbytes(fin, 3)

    # inline subroutine $248xxx here
    cpuaddr = getbits(buffer1, 0, 0xFFFFF8)
    shift = getbits(buffer1, 0, 0x000007)

    count = msgid & 0x000F
    for count in range(count):
        code = 0
        while not _is_delimiter(code):
            code, cpuaddr, shift = _decode(cpuaddr, shift, fin)

    return cpuaddr, shift

_LOC_MASK = 0x249E8C

def _init_maskbit_array(fin):
    """(Local function)"""

    if not getattr(_init_maskbit_array, "SHIFTBIT_ARRAY", None):
        fin.seek(ROMADDR(_LOC_MASK))
        _init_maskbit_array.SHIFTBIT_ARRAY = readbytes(fin, 8)

    return _init_maskbit_array.SHIFTBIT_ARRAY

# Constants for use in the loading methods arguments:
MSG_ID_FIRST = 0x0000
MSG_ID_LAST = 0x0C7E

def _verify_msg_id(first, last):
    """Local function"""

    if first < MSG_ID_FIRST:
        raise IndexError('out of range:')
    if MSG_ID_LAST < last:
        raise IndexError('out of range:')
    if first > last:
        raise IndexError('invalid range:')

def load_msg_code(idfirst=MSG_ID_FIRST, idlast=MSG_ID_LAST):
    """Return a list of tuples (cpuaddr, shift, codeseq).

    load_msg_code(idfirst, idlast) -> [(cpuaddr, shift, codeseq)]
    """

    _verify_msg_id(idfirst, idlast)

    # Data to be returned, a list of (cpuaddr, codeseq) pairs.
    data = []
    with open_rom() as fin:
        # Create a memory-mapped file from fin.
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        shiftbit_array = _init_maskbit_array(mem)

        # Obtain the first data location.
        cpuaddr, shift = _get_cpuaddr(idfirst, mem)
        for _ in range(idfirst, idlast):
            cpuaddr0, shift0 = cpuaddr, shiftbit_array[shift]
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code, cpuaddr, shift = _decode(cpuaddr, shift, mem)
                codeseq.append(code)

            data.append((cpuaddr0, shift0, codeseq))
        mem.close()
    return data

def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of codes that are obtained by
    using load_msg_code method, and str is a text representation.
    """

    from dqutils.dq5.charlarge import CHARMAP
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
        # remove delimiter code (AC and AE)
        codeseq = tup[-1]
        shift = tup[1]
        codeseq.pop()
        print('{0:04X}:{1:06X}:{2:02X}:{3}'.format(
            i, tup[0], shift, make_text(codeseq)))

# emulate subroutine $249E02

_LOC_BIT_ON = ROMADDR(0x248CB6)
_LOC_BIT_OFF = ROMADDR(0x249472)
_ROOT = 0x07BA

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

    shiftbit_array = _init_maskbit_array(fin)
    huffman_on, huffman_off = _init_tree(fin)

    node = _ROOT
    while True:
        fin.seek(ROMADDR(cpuaddr))   # cpuaddr <- [$F0]
        buffer = readbytes(fin, 2)
        value = getbytes(buffer, 0, 2) & shiftbit_array[shift]

        if dump_shift_bit:
            print('{0:02X}={1:02X}'.format(
                getbytes(buffer, 0, 1), shiftbit_array[shift]), end='')
            if value:
                print(1, end='')
            else:
                print(0, end='')

        if value:
            value = getbytes(huffman_on, node, 2)
        else:
            value = getbytes(huffman_off, node, 2)

        shift += 1
        if shift >= 8:
            shift = 0
            cpuaddr += 1
            if cpuaddr & 0xFFFF == 0:
                # LoROM nextbank
                cpuaddr = (cpuaddr & 0xFF0000) | 0x8000

        if value & 0x8000:
            break

        value &= 0x1FFF
        node = value << 1
        # endwhile

    value &= 0x1FFF

    if dump_shift_bit:
        print(':{:04X}'.format(value))

    return value, cpuaddr, shift

#
# Battle message
#

def _is_delimiter_battle(code):
    """Local function"""

    return code == 0x00FE or code == 0x00E7 or code == 0x00EF

LOCATION_MSG_BATTLE = ROMADDR(0x24AECD)

def _seek_location_battle(msgid, fin):
    """Local function dq5 $248C39"""

    group = msgid // 16 * 3
    fin.seek(LOCATION_MSG_BATTLE + group)
    buffer1 = readbytes(fin, 3)

    # inline subroutine $248C8D here
    cpuaddr = getbits(buffer1, 0, 0xFFFFF8)
    shift = getbits(buffer1, 0, 0x000007)

    count = msgid & 0x000F
    while count:
        code, cpuaddr, shift = _decode_battle(cpuaddr, shift, fin)
        if _is_delimiter_battle(code):
            count -= 1

    return cpuaddr, shift

# emulate subroutine $249E47

_LOC_BIT_ON_B = 0x249C2E
_LOC_BIT_OFF_B = 0x249D18
_ROOT_B = 0x00E8

def _init_tree_battle(fin):
    """(Local function) Initialize Huffman tree data."""

    if not getattr(_init_tree_battle, "HUFFMAN_OFF", None):
        fin.seek(ROMADDR(_LOC_BIT_OFF_B))
        _init_tree_battle.HUFFMAN_OFF = readbytes(fin, _ROOT_B + 2)

    if not getattr(_init_tree_battle, "HUFFMAN_ON", None):
        fin.seek(ROMADDR(_LOC_BIT_ON_B))
        _init_tree_battle.HUFFMAN_ON = readbytes(fin, _ROOT_B + 2)

    assert len(_init_tree_battle.HUFFMAN_ON) == _ROOT_B + 2
    assert len(_init_tree_battle.HUFFMAN_OFF) == _ROOT_B + 2
    return _init_tree_battle.HUFFMAN_ON, _init_tree_battle.HUFFMAN_OFF

def _decode_battle(cpuaddr, shift, fin, dump_shift_bit=False):
    """Huffman routine"""

    assert cpuaddr & 0xFF000000 == 0
    assert shift & 0xFFFFFF00 == 0

    shiftbit_array = _init_maskbit_array(fin)
    huffman_on, huffman_off = _init_tree_battle(fin)

    node = _ROOT_B
    while True:
        fin.seek(ROMADDR(cpuaddr))   # cpuaddr <- [$F0]
        buffer = readbytes(fin, 1)
        value = getbytes(buffer, 0, 1) & shiftbit_array[shift]

        if dump_shift_bit:
            print('{0:02X}={1:02X}'.format(
                getbytes(buffer, 0, 1), shiftbit_array[shift]), end='')
            if value:
                print(1, end='')
            else:
                print(0, end='')

        if value:
            value = getbytes(huffman_on, node, 2)
        else:
            value = getbytes(huffman_off, node, 2)

        shift += 1
        if shift >= 8:
            shift = 0
            cpuaddr += 1
            if cpuaddr & 0xFFFF == 0:
                # LoROM nextbank
                cpuaddr = (cpuaddr & 0xFF0000) | 0x8000

        if value & 0x8000:
            break

        value &= 0x1FFF
        node = value << 1
        # endwhile

    value &= 0xFF
    if dump_shift_bit:
        print(':{:02X}'.format(value))

    return value, cpuaddr, shift

BATTLE_ID_FIRST = 0
BATTLE_ID_LAST = 0x01A3

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

    # Data to be returned, a list of (cpuaddr, codeseq) pairs.
    data = []
    with open_rom() as fin:
        # Create a memory-mapped file from fin.
        mem = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        shiftbit_array = _init_maskbit_array(mem)

        # Obtain the first data location.
        cpuaddr, shift = _seek_location_battle(idfirst, mem)
        for _ in range(idfirst, idlast):
            cpuaddr0, mask0 = cpuaddr, shiftbit_array[shift]
            codeseq = [] # codewords of a message
            code = 0 # a codeword
            while not _is_delimiter_battle(code):
                code, cpuaddr, shift = _decode_battle(cpuaddr, shift, mem)
                codeseq.append(code)

            data.append((cpuaddr0, mask0, codeseq))
        mem.close()
    return data

def make_text_battle(codeseq):
    """Return a legible string.

    make_text_battle(codeseq) -> str,

    where codeseq is the list of codes that are obtained by
    using load_battle_msg_code method, and str is a text representation.
    """

    from dqutils.dq5.charsmall import CHARMAP
    from dqutils.dq5.charsmall import process_dakuten
    return process_dakuten(
        ''.join([CHARMAP.get(c, '{:02X}'.format(c)) for c in codeseq]))

def load_battle_msg(index):
    """Return a legible string.
    """

    return make_text_battle(load_battle_msg_code(index, index + 1)[0][1])

def print_all_battle():
    """Demonstration method by the author, for the author"""

    data = load_battle_msg_code()
    for i, tup in enumerate(data):
        # Remove delimiter codes (AC and AE).
        codeseq = tup[-1]
        shift = tup[1]
        codeseq.pop()
        print('{0:04X}:{1:06X}:{2:02X}:{3}'.format(
            i, tup[0], shift, make_text_battle(codeseq)))

if __name__ == '__main__':
    print_all()
