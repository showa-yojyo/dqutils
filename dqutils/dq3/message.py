# -*- coding: utf-8 -*-

"""dqutils.dq3.message module"""

from dqutils.dq3.charsmall import CHARMAP as CHARMAP_SMALL
from dqutils.dq3.charlarge import CHARMAP as CHARMAP_LARGE
import dqutils.message
from array import array

CONTEXT_MESSAGE_BATTLE = dict(
    title="DRAGONQUEST3",
    delimiters=b'\xAC\xAE',
    charmap=CHARMAP_SMALL,
    message_id_first=0x0000,
    message_id_last=0x0177,
    addr_message=0xFC9F22,)

CONTEXT_MESSAGE_SCENARIO = dict(
    title="DRAGONQUEST3",
    delimiters=array('H', (0x00AC, 0x00AE,)),
    charmap=CHARMAP_LARGE,
    message_id_first=0x0000,
    message_id_last=0x0FCF,
    addr_group=0xC15331,
    addr_shiftbit_array=0xC1B01C,
    addr_message=0xFCC258,
    addr_huffman_off=0xC159D3,
    addr_huffman_on=0xC161A7,
    huffman_root=0x07D2,)

def enum_battle(first=None, last=None):
    """A transfer generator."""
    for i in dqutils.message.enum_battle(
        CONTEXT_MESSAGE_BATTLE, first, last):
        yield i

def print_all_battle():
    """A transfer function."""
    print_string(CONTEXT_MESSAGE_BATTLE)

def enum_scenario(first=None, last=None):
    """A transfer generator."""
    for i in dqutils.message.enum_scenario(
        CONTEXT_MESSAGE_SCENARIO, first, last):
        yield i

def print_all_scenario():
    """A transfer function."""
    dqutils.message.print_scenario(CONTEXT_MESSAGE_SCENARIO)
