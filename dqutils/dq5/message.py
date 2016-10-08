"""
This module provides decoding methods for DQ5 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.

These decoding functions are based on classical Huffman's algorithm.

Special thanks to Mr. kobun_c.
"""

from array import array
from dqutils.bit import get_int
from dqutils.message import enum_scenario as _enum_scenario
from dqutils.message_generator import MessageGeneratorV
from dqutils.string import get_text
from .charsmall import (CHARMAP as CHARMAP_SMALL,
                        process_dakuten)
from .charlarge import CHARMAP as CHARMAP_LARGE

CONTEXT_MESSAGE_BATTLE = dict(
    title="DRAGONQUEST5",
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
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.

    Yields
    ------
    addr : int
        An offset value of the ROM address space.
    code_seq : bytearray
        A sequence of characters locating in `addr`.
    """
    yield from _enum_scenario(
        CONTEXT_MESSAGE_BATTLE, MessageGeneratorV, first, last)

def print_all_battle():
    """Print all message data of battle mode to sys.stdout."""

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
    """Return generator iterators of message data by specifying
    their indices.

    Message data those indices in [`first`, `last`) will be returned.

    Parameters
    ----------
    first : int, optional
        The first index of the range of indices you want.
    last : int, optional
        The last index + 1 of the range of indices you want.

    Yields
    ------
    addr : int
        The address of the message data.
    shift_bits : int
        The shift from `addr`.
    code_seq : bytearray
        A sequence of characters locating in `addr`.
    """
    yield from _enum_scenario(
        CONTEXT_MESSAGE_SCENARIO, MessageGeneratorV, first, last)

def print_all_scenario():
    """Print all message data of conversation mode to sys.stdout."""

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
