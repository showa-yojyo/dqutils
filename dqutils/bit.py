# -*- coding: utf-8 -*-
"""dqutils.bit module -- bits and bytes manipulation.
"""
from itertools import islice

def get_bits(byte_seq, index, mask):
    """Obtain specific bits in bytes.

    Args:
      byte_seq (iterable of bytes): A byte sequence.
      index (int): The index from which to obtain bits.
      mask (int): The bit mask.

    Returns:
      int: The integer that extracted bit string represents
        (in little endian).
    """
    value = get_int(byte_seq, index, 3) & mask

    while mask & 1 == 0:
        value >>= 1
        mask >>= 1

    return value

def get_int(byte_seq, index, length):
    """Obtain the integer from a subsequence in the given sequence.

    Args:
      byte_seq: An instance of class bytes, bytearray, or iterable of ints.
      index: The index from which to obtain byte items.
      length: The size of byte items to obtain from `byte_seq`.

    Returns:
      int: The integer represented by `byte_seq[index:index + length]`
        (in little endian).

    Examples:
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
    """

    return int.from_bytes(
        islice(byte_seq, index, index + length), 'little')
