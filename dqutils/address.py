# -*- coding: utf-8 -*-
"""dqutils SNES addressing module
"""

def from_hi(romaddr, fast=True):
    """Convert from ROM image to CPU address for HiROM.

    Transform a ROM image address to SNES CPU address for HiROM.

    >>> cpuaddr = from_hi(0x020000, True)
    >>> print('0x{:06X}'.format(cpuaddr))
    0xC20000
    >>> cpuaddr = from_hi(0x020000, False)
    >>> print('0x{:06X}'.format(cpuaddr))
    0x420000
    """
    cpuaddr = romaddr & 0x003FFFFF
    if fast:
        return cpuaddr | 0x00C00000
    else:
        return cpuaddr | 0x00400000

def from_lo(romaddr, fast=False):
    """Convert from ROM image to CPU address for LoROM.

    Transform a ROM image address to SNES CPU address for LoROM.

    >>> cpuaddr = from_lo(0x008000, True)
    >>> print('0x{:06X}'.format(cpuaddr))
    0x818000
    >>> cpuaddr = from_lo(0x008000, False)
    >>> print('0x{:06X}'.format(cpuaddr))
    0x018000
    """
    cpuaddr = ((romaddr & 0x00007FFF)
               | (((romaddr & 0x007F8000) << 1) | 0x00008000))
    if fast:
        return cpuaddr | 0x00800000
    return cpuaddr

def conv_hi(cpuaddr):
    """Convert from CPU address to ROM address for HiROM.

    Transform an SNES CPU address to ROM image address for HiROM.

    >>> romaddr = conv_hi(0xC20000)
    >>> print('0x{:06X}'.format(romaddr))
    0x020000
    """
    return cpuaddr & 0x003FFFFF

def conv_lo(cpuaddr):
    """Convert from CPU address to ROM address for LoROM.

    Transform an SNES CPU address to ROM image address for LoROM.

    >>> romaddr = conv_lo(0x018000)
    >>> print('0x{:06X}'.format(romaddr))
    0x008000
    """
    return (cpuaddr & 0x007FFF) | ((cpuaddr & 0x00FF0000) >> 1)

def _test():
    """Test all of the examples in docstrings in this module."""
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    _test()
