"""This module provides functions for low-level bit/byte
manipulation.
"""

from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def get_bits(byte_seq: bytes | bytearray | Iterable[int], index: int, mask: int) -> int:
    """Obtain specified bits as an integer value from a sequence of
    bytes.

    The bit length of the value shall not be greater than 24.

    Parameters
    ----------
    byte_seq : iterable of bytes
        A byte sequence.
    index : int
        The index from which to obtain bits.
    mask : int
        The bit mask.

    Returns
    -------
    value : int
        The integer that extracted bit string represents (in little endian).

    See Also
    --------
    get_int
    """

    value = get_int(byte_seq, index, 3) & mask

    while mask & 1 == 0:
        value >>= 1
        mask >>= 1

    return value


def get_int(byte_seq: bytes | bytearray | Iterable[int], index: int, length: int) -> int:
    """Obtain the integer value from a subsequence in a sequence of
    bytes.

    Parameters
    ----------
    byte_seq : bytes, bytearray, or iterable of integers.
        The source sequence.
    index : int
        The index from which to obtain byte items.
    length : int
        The size of byte items to obtain from `byte_seq`.

    Returns
    -------
    value : int
        The integer represented by `byte_seq[index:index + length]`
        (in little endian).

    Examples
    --------
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

    return int.from_bytes(islice(byte_seq, index, index + length), "little")
