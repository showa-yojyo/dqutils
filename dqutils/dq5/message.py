#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
"""dqutils.dq5.message module

This module implements decoding methods for DQ5 message
systems.  The original implementation is of course by
65816 code.  Here is by Python code, via C/C++ code I made
before.

The decoding logic is based on classical Huffman's method
(Thanks to Mr. kobun_c).
"""

from __future__ import with_statement
from dqutils.address import conv_lo as ROMADDR
from dqutils.bit import readbytes
from dqutils.parser import getbits, getbytes

from dqutils.dq5 import open_rom
import mmap

__DEBUG_MODE__ = False

#
# Conversation, dialog, system messages
#

def _is_delimiter(code):
    """Local function"""

    return code == 0x1001 or code == 0x1010 or code == 0x1018

_LOC_GROUP = ROMADDR(0x24AF1E)

def _get_cpuaddr(msgid, fin):
    """Local function dq5 $248BAF"""

    group = msgid / 16 * 3
    fin.seek(_LOC_GROUP + group)
    buffer1 = readbytes(fin, 3)

    # inline subroutine $248xxx here
    cpuaddr = getbits(buffer1, 0, 0xFFFFF8)
    shift = getbits(buffer1, 0, 0x000007)

    count = msgid & 0x000F
    for count in xrange(count):
        code = 0
        while not _is_delimiter(code):
            code, cpuaddr, shift = _decode(cpuaddr, shift, fin)

    return cpuaddr, shift


_LOC_MASK = 0x249E8C
_SHIFTBIT_ARRAY = None

def _init_maskbit_array(fin):
    """(Local function)"""

    global _SHIFTBIT_ARRAY
    if _SHIFTBIT_ARRAY is None:
        fin.seek(ROMADDR(_LOC_MASK))
        _SHIFTBIT_ARRAY = readbytes(fin, 8)


# Constants for use in the loading methods arguments:
MSG_ID_FIRST = 0x0000
MSG_ID_LAST  = 0x0C7E

def _verify_msg_id(first, last):
    """Local function"""

    if first < MSG_ID_FIRST:
        raise RuntimeError, 'out of range:'
    if MSG_ID_LAST < last:
        raise RuntimeError, 'out of range:'
    if first > last:
        raise RuntimeError, 'invalid range:'


def load_msg_code(idfirst = MSG_ID_FIRST, idlast = MSG_ID_LAST):
    """Return a list of tuples (cpuaddr, shift, codeseq).

    load_msg_code(idfirst, idlast) -> [(cpuaddr, shift, codeseq)]
    """
    _verify_msg_id(idfirst, idlast)

    # data to be returned, a list of (cpuaddr, codeseq) pairs
    data = []
    with open_rom() as fin:
        # create memory-mapped file from fin
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)

        _init_maskbit_array(mem)
        # Obtain the first data location
        cpuaddr, shift = _get_cpuaddr(idfirst, mem)
        for i in xrange(idfirst, idlast):
            cpuaddr0, shift0 = cpuaddr, _SHIFTBIT_ARRAY[shift]
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code, cpuaddr, shift = _decode(cpuaddr, shift, mem)
                codeseq.append(code)

            if __DEBUG_MODE__:
                print '=' * 40

            data.append((cpuaddr0, shift0, codeseq))
        mem.close()
    return data


def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of codes that is obtained by
    using load_msg_code method and str is text representation.
    """
    from dqutils.dq5.charlarge import charmap
    return u''.join([charmap.get(c, u'[%02X]' % c) for c in codeseq])


def load_msg(id):
    """Return a legible string.

    load_msg(id) <==> make_text(load_msg_code(id, id + 1)[0][1])
    """

    return make_text(load_msg_code(id, id + 1)[0][-1])


def print_all():
    """Demonstration method by the author, for the author"""
    import time
    st = time.clock()
    data = load_msg_code()
    et = time.clock()

    for id, tup in enumerate(data):
        # remove delimiter code (AC and AE)
        codeseq = tup[-1]
        shift = tup[1]
        codeseq.pop()
        print u'%04X:%06X:%02X:%s' % (id, tup[0], shift, make_text(codeseq))
    print et - st, 'sec'

# emulate subroutine $249E02

_LOC_BIT_ON  = 0x248CB6
_LOC_BIT_OFF = 0x249472
_ROOT        = 0x07BA

HUFFMAN_OFF = None
HUFFMAN_ON  = None

def _init_tree(fin):
    """(Local function) Initialize Huffman tree data."""

    # C/C++ の感覚だと、当スコープ？からでもこれらの名前を見つけて
    # 当然だと思ってしまいがちだが、この global 宣言を欠くと
    # if 文のある行で UnboundLocalError を生ずる
    global HUFFMAN_OFF
    global HUFFMAN_ON

    if HUFFMAN_OFF is None:
        fin.seek(ROMADDR(_LOC_BIT_OFF))
        HUFFMAN_OFF = readbytes(fin, _ROOT + 2)

    if HUFFMAN_ON is None:
        fin.seek(ROMADDR(_LOC_BIT_ON))
        HUFFMAN_ON = readbytes(fin, _ROOT + 2)

    assert len(HUFFMAN_ON) == _ROOT + 2
    assert len(HUFFMAN_OFF) == _ROOT + 2


def _decode(cpuaddr, shift, fin):
    """Decoding algorithm of Huffman coding."""
    assert cpuaddr & 0xFF000000 == 0
    assert shift & 0xFFFFFF00 == 0

    _init_tree(fin)

    node = _ROOT
    while True:
        fin.seek(ROMADDR(cpuaddr))   # cpuaddr <- [$F0]
        buffer = readbytes(fin, 2)
        value = getbytes(buffer, 0, 2) & _SHIFTBIT_ARRAY[shift]

        if __DEBUG_MODE__:
            print '%02X=%02X' % (getbytes(buffer, 0, 1), _SHIFTBIT_ARRAY[shift]),
            if value:
                print 1,
            else:
                print 0,

        if value:
            value = getbytes(HUFFMAN_ON, node, 2)
        else:
            value = getbytes(HUFFMAN_OFF, node, 2)

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

    if __DEBUG_MODE__:
        print ':%04X' % value

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

    group = msgid / 16 * 3
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

_LOC_BIT_ON_B  = 0x249C2E
_LOC_BIT_OFF_B = 0x249D18
_ROOT_B        = 0x00E8

HUFFMAN_OFF_B = None
HUFFMAN_ON_B  = None

def _init_tree_battle(fin):
    """(Local function) Initialize Huffman tree data."""

    global HUFFMAN_OFF_B
    global HUFFMAN_ON_B

    if HUFFMAN_OFF_B is None:
        fin.seek(ROMADDR(_LOC_BIT_OFF_B))
        HUFFMAN_OFF_B = readbytes(fin, _ROOT_B + 2)

    if HUFFMAN_ON_B is None:
        fin.seek(ROMADDR(_LOC_BIT_ON_B))
        HUFFMAN_ON_B = readbytes(fin, _ROOT_B + 2)

    assert len(HUFFMAN_ON_B) == _ROOT_B + 2
    assert len(HUFFMAN_OFF_B) == _ROOT_B + 2

def _decode_battle(cpuaddr, shift, fin):
    """Huffman routine"""
    assert cpuaddr & 0xFF000000 == 0
    assert shift & 0xFFFFFF00 == 0

    _init_tree_battle(fin)

    node = _ROOT_B
    while True:
        fin.seek(ROMADDR(cpuaddr))   # cpuaddr <- [$F0]
        buffer = readbytes(fin, 1)
        value = getbytes(buffer, 0, 1) & _SHIFTBIT_ARRAY[shift]

        if __DEBUG_MODE__:
            print '%02X=%02X' % (getbytes(buffer, 0, 1), _SHIFTBIT_ARRAY[shift]),
            if value:
                print 1,
            else:
                print 0,

        if value:
            value = getbytes(HUFFMAN_ON_B, node, 2)
        else:
            value = getbytes(HUFFMAN_OFF_B, node, 2)

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
    if __DEBUG_MODE__:
        print ':%02X' % value

    return value, cpuaddr, shift


BATTLE_ID_FIRST = 0
BATTLE_ID_LAST  = 0x01A3

def _verify_input(first, last):
    """Local function"""

    if first < BATTLE_ID_FIRST:
        raise RuntimeError, 'out of range:'
    if BATTLE_ID_LAST < last:
        raise RuntimeError, 'out of range:'
    if first > last:
        raise RuntimeError, 'invalid range:'


def load_battle_msg_code(
    idfirst = BATTLE_ID_FIRST,
    idlast  = BATTLE_ID_LAST):
    """Help me!"""
    _verify_input(idfirst, idlast)

    # data to be returned, a list of (cpuaddr, codeseq) pairs
    data = []
    with open_rom() as fin:
        # create memory-mapped file from fin
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)

        _init_maskbit_array(mem)
        # Obtain the first data location
        cpuaddr, shift = _seek_location_battle(idfirst, mem)
        for i in xrange(idfirst, idlast):
            cpuaddr0, mask0 = cpuaddr, _SHIFTBIT_ARRAY[shift]
            codeseq = []  # codewords of a message
            code = 0    # a codeword
            while not _is_delimiter_battle(code):
                code, cpuaddr, shift = _decode_battle(cpuaddr, shift, mem)
                codeseq.append(code)
            if __DEBUG_MODE__:
                print '=' * 40

            data.append((cpuaddr0, mask0, codeseq))
        mem.close()
    return data


def make_text_battle(codeseq):
    """Return a legible string.

    make_text_battle(codeseq) -> str,

    where codeseq is the list of codes that is obtained by
    using load_battle_msg_code method and str is text representation.
    """

    from dqutils.dq5.charsmall import charmap, process_dakuten
    return process_dakuten(u''.join([charmap.get(c, u'[%02X]' % c) for c in codeseq]))


def load_battle_msg(id):
    """Return a legible string.

    load_battle_msg(id) <==> make_text_battle(load_battle_msg_code(id, id + 1)[0][1])
    """

    return make_text_battle(load_battle_msg_code(id, id + 1)[0][1])


def print_all_battle():
    """Demonstration method by the author, for the author"""
    import time
    st = time.clock()
    data = load_battle_msg_code()
    et = time.clock()
    for id, tup in enumerate(data):
        # remove delimiter code (AC and AE)
        codeseq = tup[-1]
        mask = tup[1]
        codeseq.pop()
        print u'%04X:%06X:%02X:%s' % (id, tup[0], mask, make_text_battle(codeseq))
    print et - st, 'sec'


if __name__ == '__main__':
    #print_all_battle()
    print_all()
    pass
