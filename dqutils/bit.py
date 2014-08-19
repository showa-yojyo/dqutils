#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""dqutils.bit module
"""

def getbits(bytes, index, mask):
    """Obtain masked bits in a byte sequence.

    Obtain masked bits in a byte sequence.
    """
    value = getbytes(bytes, index, 3) & mask

    while mask & 1 == 0:
        value >>= 1
        mask >>= 1

    return value

def getbytes(bytes, index, nbyte):
    """Obtain bytes as an integer in a byte sequence.

    Obtain bytes as an integer in a byte sequence.

    >>> data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06]
    >>> getbytes(data, 0, 1) == 0x00
    True
    >>> getbytes(data, 1, 1) == 0x01
    True
    >>> getbytes(data, 0, 2) == 0x0100
    True
    >>> getbytes(data, 6, 2) == 0x0006
    True
    >>> getbytes(data, 0, 3) == 0x020100
    True
    >>> getbytes(data, 5, 3) == 0x000605
    True
    >>> getbytes(data, 6, 3) == 0x000006
    True
    """
    if nbyte == 0:
        return 0

    value = bytes[index]

    # simple case
    if nbyte == 1:
        return value

    # general case

    indexfirst = index + 1
    indexlast = min(index + nbyte, len(bytes))
    shiftbit = 8

    while indexfirst < indexlast:
        value += (bytes[indexfirst] << shiftbit)
        indexfirst += 1
        shiftbit += 8

    return value

def readbytes(fin, nbyte):
    """Read nbyte byte from fin as binaries rather characters."""
    return [i for i in fin.read(nbyte)]

def _test():
    import doctest, bit
    return doctest.testmod(bit)

if __name__ == '__main__':
    _test()
