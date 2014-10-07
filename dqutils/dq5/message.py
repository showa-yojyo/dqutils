# -*- coding: utf-8 -*-

"""dqutils.dq5.message module

This module provides decoding methods for DQ5 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.

These decoding functions are based on classical Huffman's algorithm.

Special thanks to Mr. kobun_c.
"""

from dqutils.bit import getbits
from dqutils.bit import get_int
from dqutils.dq5.charsmall import CHARMAP as CHARMAP_SMALL
from dqutils.dq5.charsmall import process_dakuten
from dqutils.dq5.charlarge import CHARMAP as CHARMAP_LARGE
import dqutils.message
from dqutils.message import MessageDecoder
from dqutils.string import get_text
from array import array

CONTEXT_MESSAGE_BATTLE = dict(
    title="DRAGONQUEST5",
    mapper='LoROM',
    delimiters=array('H', (0x00E7, 0x00EF, 0x00FE)),
    charmap=CHARMAP_SMALL,
    message_id_first=0x0000,
    message_id_last=0x01A3,
    addr_group=0x24AECD,
    addr_shiftbit_array=0x249E8C,
    addr_message=0x000000,
    addr_huffman_off=0x249D18,
    addr_huffman_on=0x249C2E,
    huffman_root=0x00E8,
    decoding_mask=0x00FF,
    decoding_read_size=1)

CONTEXT_MESSAGE_SCENARIO = dict(
    title="DRAGONQUEST5",
    mapper='LoROM',
    delimiters=array('H', (0x1001, 0x1010, 0x1018)),
    charmap=CHARMAP_LARGE,
    message_id_first=0x0000,
    message_id_last=0x0C7E,
    addr_group=0x24AF1E,
    addr_shiftbit_array=0x249E8C,
    addr_message=0x000000,
    addr_huffman_off=0x249472,
    addr_huffman_on=0x248CB6,
    huffman_root=0x07BA,
    decoding_mask=0x1FFF,
    decoding_read_size=2)

def enum_battle(first=None, last=None):
    """A transfer generator."""
    for i in dqutils.message.enum_scenario(
        CONTEXT_MESSAGE_BATTLE, first, last, MessageDecoderV):
        yield i

def print_all_battle():
    """Print message data to sys.stdout."""

    context = CONTEXT_MESSAGE_BATTLE

    first = context["message_id_first"]
    last = context["message_id_last"]
    assert first < last

    charmap = context["charmap"]
    assert charmap is None or isinstance(charmap, dict)

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, array)

    for i, item in enumerate(enum_battle(first, last)):
        address, shift, code_seq = item
        text = process_dakuten(get_text(code_seq, charmap, delims))
        print("{index:04X}:{address:06X}:{shift:02X}:{message}".format(
            index=i,
            address=address,
            shift=shift,
            message=text))

def enum_scenario(first=None, last=None):
    """A transfer generator."""
    for i in dqutils.message.enum_scenario(
        CONTEXT_MESSAGE_SCENARIO, first, last, MessageDecoderV):
        yield i

def print_all_scenario():
    """Print message data to sys.stdout."""

    context = CONTEXT_MESSAGE_SCENARIO

    first = context["message_id_first"]
    last = context["message_id_last"]
    assert first < last

    charmap = context["charmap"]
    assert charmap is None or isinstance(charmap, dict)

    delims = context["delimiters"]
    assert delims is None or isinstance(delims, array)

    for i, item in enumerate(enum_scenario(first, last)):
        address, shift, code_seq = item
        text = get_text(code_seq, charmap, delims)
        print("{index:04X}:{address:06X}:{shift:02X}:{message}".format(
            index=i,
            address=address,
            shift=shift,
            message=text))

class MessageDecoderV(MessageDecoder):
    """TBW"""

    def _select_message_group(self, message_id):
        """TBW"""
        count = message_id & 0x000F
        group = message_id // 16 * 3
        return count, group

    def _next_location(self, addr, shift):
        """TBW"""
        shift <<= 1
        if shift > 0x80:
            shift = 0x01
            addr += 1
            if addr & 0xFFFF == 0:
                # LoROM next bank
                addr = (addr & 0xFF0000) | 0x8000
        return addr, shift

    def _next_node(self, node):
        """TBW"""
        node &= 0x1FFF
        node <<= 1
        return node

    def _is_leaf_node(self, node):
        """TBW"""
        return node & 0x8000
