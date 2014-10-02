# -*- coding: utf-8 -*-

"""dqutils.dq6.message module"""

from dqutils.dq6.charsmall import CHARMAP as CHARMAP_SMALL
from dqutils.dq6.charlarge import CHARMAP as CHARMAP_LARGE
import dqutils.message
from array import array

CONTEXT_MESSAGE_BATTLE = dict(
    title="DRAGONQUEST6",
    mapper='HiROM',
    delimiters=b'\xAC\xAE',
    charmap=CHARMAP_SMALL,
    message_id_first=0x0000,
    message_id_last=0x025B,
    addr_message=0xF6DEBD,)

CONTEXT_MESSAGE_SCENARIO = dict(
    title="DRAGONQUEST6",
    mapper='HiROM',
    delimiters=array('H', (0x00AC, 0x00AE,)),
    charmap=CHARMAP_LARGE,
    message_id_first=0x0000,
    message_id_last=0x1B2D,
    addr_group=0xC15BB5,
    addr_shiftbit_array=0xC02BCC,
    addr_message=0xF7175B,
    addr_huffman_off=0xC167BE,
    addr_huffman_on=0xC1700E,
    huffman_root=0x084E,)

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
