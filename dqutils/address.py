# -*- coding: utf-8 -*-
"""dqutils.address - SNES address conversion functions.
"""

def from_hi(romaddr):
    """Convert from a ROM address to a CPU address for HiROM.

    >>> cpuaddr = from_hi(0x020000)
    >>> print('0x{:06X}'.format(cpuaddr))
    0xC20000
    """
    return 0x00C00000 | (romaddr & 0x003FFFFF)

def from_lo(romaddr):
    """Convert from a ROM address to a CPU address for LoROM.

    >>> cpuaddr = from_lo(0x008000)
    >>> print('0x{:06X}'.format(cpuaddr))
    0x018000
    """
    return ((romaddr & 0x00007FFF)
            | (((romaddr & 0x007F8000) << 1) | 0x00008000))

def conv_hi(cpuaddr):
    """Convert from a CPU address to a ROM address for HiROM.

    To convert from a CPU address to a ROM address, first, remove bit 15.
    Second, moving all bits after it down one.

    >>> romaddr = conv_hi(0xC20000)
    >>> print('0x{:06X}'.format(romaddr))
    0x020000
    """
    return cpuaddr & 0x003FFFFF

def conv_lo(cpuaddr):
    """Convert from a CPU address to a ROM address for LoROM.

    >>> romaddr = conv_lo(0x018000)
    >>> print('0x{:06X}'.format(romaddr))
    0x008000
    """
    return (cpuaddr & 0x007FFF) | ((cpuaddr & 0x007F0000) >> 1)
