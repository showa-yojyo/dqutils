#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
"""dqutils.dq6.message module

This module implements decoding methods for DQ6 message
systems.  The original implementation is of course by
65816 code.  Here is by Python code, via C/C++ code I made
before.

As to DQ6, decoding logic is almost the same way as DQ5.
It seems that only the difference between the two is structures
of Huffman trees
"""

from __future__ import with_statement
from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.bit import readbytes
from dqutils.parser import getbits, getbytes

from dqutils.dq6 import open_rom
import mmap

__DEBUG__ = False

def _is_delimiter(code):
    """Local function"""
    return code == 0xAC or code == 0xAE

#
# Battle message
#

# where message data of battle scene are stored
LOCATION_MSG_BATTLE = ROMADDR(0xF6DEBD)

def _seek_location(fin, id):
    """Local function"""

    fin.seek(LOCATION_MSG_BATTLE)
    ncount = 0
    while ncount < id:
        code = ord(fin.read(1)[0])
        if _is_delimiter(code):
            ncount += 1

    return CPUADDR(fin.tell())


# Constants for use in the loading methods arguments:
BATTLE_ID_FIRST = 0x0000
BATTLE_ID_LAST  = 0x025B

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

    # data to be returned; a list of (cpuaddr, codeseq) pairs
    data = []
    with open_rom() as fin:
        # create memory-mapped file from fin
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)
        cpuaddr = _seek_location(mem, idfirst)

        for i in xrange(idfirst, idlast):
            # Huffman codewords of a message
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code = ord(mem.read(1)[0])
                codeseq.append(code)

            data.append((cpuaddr, codeseq))
            # now update cpuaddr
            cpuaddr = CPUADDR(mem.tell())
        mem.close()
    return data


def make_text_battle(codeseq):
    """Return a legible string.

    make_text_battle(codeseq) -> str,

    where codeseq is the list of codes that is obtained by
    using load_battle_msg_code method and str is text representation.
    """
    
    from dqutils.dq6.charsmall import charmap
    return u''.join([charmap.get(c, u'[%02X]' % c) for c in codeseq])


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
    for id, pair in enumerate(data):
        # remove delimiter code (AC and AE)
        codeseq = pair[1]
        codeseq.pop()
        print u'%04X:%06X:%s' % (id, pair[0], make_text(codeseq))
    et = time.clock()
    print et - st, 'sec'

#
# Conversation, dialog, system messages
#

_LOC_GROUP = ROMADDR(0xC15BB5)
_LOC_SHIFT = ROMADDR(0xC02BCC)
_LOC_DATA  = 0xF7175B
_SHIFTBIT_ARRAY = None

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
    global _SHIFTBIT_ARRAY
    if _SHIFTBIT_ARRAY is None:
        fin.seek(_LOC_SHIFT)
        _SHIFTBIT_ARRAY = readbytes(fin, 8)
    shift = _SHIFTBIT_ARRAY[buffer1[0] & 0x07]

    cpuaddr = (getbytes(buffer1, 0, 3) >> 3) + _LOC_DATA

    # msgid % 7 の値によりループ回数が違う
    for count in xrange(count):
        code = 0
        while not _is_delimiter(code):
            # この関数は重いので注意
            code, cpuaddr, shift = _decode(cpuaddr, shift, fin)

    return cpuaddr, shift


MSG_ID_FIRST = 0x0000
MSG_ID_LAST  = 0x1B2D

def _verify_msg_id(first, last):
    """Local function"""

    if first < MSG_ID_FIRST:
        raise RuntimeError, 'out of range:'
    if MSG_ID_LAST < last:
        raise RuntimeError, 'out of range:'
    if first > last:
        raise RuntimeError, 'invalid range:'


def load_msg_code(idfirst = MSG_ID_FIRST, idlast = MSG_ID_LAST):
    """Return a list of pairs (cpuaddr, codeseq).

    load_msg_code(idfirst, idlast) -> a list of (cpuaddr, codeseq).
    """

    _verify_msg_id(idfirst, idlast)

    # data to be returned
    data = []
    with open_rom() as fin:
        # create memory-mapped file from fin
        mem = mmap.mmap(fin.fileno(), 0, access = mmap.ACCESS_READ)

        # Obtain the first data location
        cpuaddr, shift = _get_cpuaddr(idfirst, mem)

        if __DEBUG__:
            print "*" * 40

        for i in xrange(idfirst, idlast):
            cpuaddr0, shift0 = cpuaddr, shift
            codeseq = []
            code = 0
            while not _is_delimiter(code):
                code, cpuaddr, shift = _decode(cpuaddr, shift, mem)
                codeseq.append(code)
            data.append((cpuaddr0, shift0, codeseq))
        # close mmap object
        mem.close()
    return data


def make_text(codeseq):
    """Return a legible string.

    make_text(codeseq) -> str,

    where codeseq is the list of codes that is obtained by
    using load_msg_code method and str is text representation.
    """
    from dqutils.dq6.charlarge import charmap
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


_LOC_BIT_OFF = ROMADDR(0xC167BE)
_LOC_BIT_ON  = ROMADDR(0xC1700E)
_ROOT = 0x084E
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
        # ファイルからバイト列を抽出
        fin.seek(_LOC_BIT_OFF)
        HUFFMAN_OFF = readbytes(fin, _ROOT + 2)

    if HUFFMAN_ON is None:
        # 上の if ブロックと統合できるように見えるだろうが
        # 別の都合により、そうしていないだけだ
        fin.seek(_LOC_BIT_ON)
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
        fin.seek(ROMADDR(cpuaddr))
        buffer = readbytes(fin, 2)
        value = getbytes(buffer, 0, 2) & shift

        if __DEBUG__:
            print '%02X' % shift,
            if value:
                print 1,
            else:
                print 0,

        shift >>= 1
        if shift == 0:
            shift = 0x0080
            cpuaddr += 1

        if value:
            value = getbytes(HUFFMAN_ON, node, 2)
        else:
            value = getbytes(HUFFMAN_OFF, node, 2)

        if value & 0x8000 == 0:
            if __DEBUG__:
                print '%04X\n' % value

            return value, cpuaddr, shift

        node = value & 0x7FFF
        # endwhile

if __name__ == '__main__':
    #print_all_battle()
    print_all()
    pass
