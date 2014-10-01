# -*- coding: utf-8 -*-
"""dqutils.bit module -- bits and bytes manipulation.
"""

def getbits(byte_seq, index, mask):
    """Obtain masked bits in a byte sequence.

    Obtain masked bits in a byte sequence.
    """
    value = get_int(byte_seq, index, 3) & mask

    while mask & 1 == 0:
        value >>= 1
        mask >>= 1

    return value

def get_int(byte_seq, index, length):
    """Obtain the integer from a subsequence in the given sequence.

    >>> data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06]
    >>> get_int(data, 0, 1) == 0x00
    True
    >>> get_int(data, 1, 1) == 0x01
    True
    >>> get_int(data, 0, 2) == 0x0100
    True
    >>> get_int(data, 6, 2) == 0x0006
    True
    >>> get_int(data, 0, 3) == 0x020100
    True
    >>> get_int(data, 5, 3) == 0x000605
    True
    >>> get_int(data, 6, 3) == 0x000006
    True

    Args:
      byte_seq: An instance of class bytes, bytearray, or iterable of ints.
      index: The index from which to obtain byte items.
      length: The size of byte items to obtain from `byte_seq`.

    Returns:
      int: The integer represented by `byte_seq[index:index + length]`.
    """

    return int.from_bytes(byte_seq[index:index + length], 'little')

def readbytes(fin, length):
    """Read `length` byte from fin as binaries rather characters."""
    return [i for i in fin.read(length)]
