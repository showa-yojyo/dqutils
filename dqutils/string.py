# -*- coding: utf-8 -*-
""" dqutils.string - DQ common string components.

This module defines common functions that access string data.

A string is an array of characters rendered in windows with the small
font.

This module provides a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.romimage import RomImage

def print_charmap(charmap):
    """Print the symbol table.

    It is much faster to open this file in the text editor.

    Args:
      charmap: The character dictionary.

    Returns:
      None.
    """
    assert isinstance(charmap, dict)

    for i in charmap.items():
        print('{0:04X}:{1}'.format(i[0], i[1]))

def get_text(code_seq, charmap, delim=None):
    """Return a text representation of a string.

    Args:
      code_seq: A string (instance of bytearray).
      charmap: The character dictionary.
      delim: The code of the delimiter character.

    Returns:
      string: e.g. "ひのきのぼう"
    """
    assert isinstance(code_seq, bytes) or isinstance(code_seq, bytearray)
    assert isinstance(charmap, dict)
    assert delim is None or isinstance(delim, bytes)

    if delim and code_seq.endswith(delim):
        code_seq = code_seq[0:-1]

    return ''.join(charmap.get(c, '{:02X}'.format(c)) for c in code_seq)

def get_hex(code_seq):
    """Return a hex representation of a string.

    This function does not remove the delimiter code.

    Args:
      code_seq: A string (instance of bytearray).

    Returns:
      string: e.g. "26 24 12 24 DC 0E AC"
    """

    assert isinstance(code_seq, bytes) or isinstance(code_seq, bytearray)
    return ' '.join('{:02X}'.format(c) for c in code_seq)

def enum_string(mem, first, last, base_addr, delim):
    """Generate string data in a range of indices.

    String data that indices in [`first`, `last`) will be generated.

    Args:
      mem: The ROM image.
      first: The first index of the indices range you want.
      last: The last index + 1 of the indices range you want.
      base_addr: The CPU address of the 0-th string data.
      delim: The code of the delimiter character, i.e. 0xAC.

    Yields:
      int: The next CPU address of data in the range of 0 to `last` - 1.
      bytearray: The next bytes of data in the range of 0 to `last` - 1.
    """

    assert first < last
    assert isinstance(delim, bytes)

    mem.seek(ROMADDR(base_addr))

    for i in range(0, last):
        addr = CPUADDR(mem.tell())
        addr_next = CPUADDR(mem.find(delim, mem.tell()))
        code_seq = mem.read(addr_next - addr + 1)

        if first <= i:
            assert code_seq.endswith(delim)
            yield (addr, code_seq)

def get_string(mem, index, base_addr, delim):
    """Return the address and code sequence of given index.

    Args:
      mem: The ROM image.
      index: The index of the string data you want.
      base_addr: The CPU address of the 0-th string data.
      delim: The code of the delimiter character, i.e. 0xAC.

    Returns:
      int: The CPU address of data in the range of 0 to `last_index` - 1.
      bytearray: The bytes of data in the range of 0 to `last_index` - 1.
    """

    assert isinstance(delim, bytes)
    return next(enum_string(mem, index, index + 1, base_addr, delim))

def print_string(context, first=None, last=None):
    """Print string data to sys.stdout.

    String data that indices in [`first`, `last`) will be output.

    Args:
      context: TBW
      first: The first index of the range you want.
      last: The last index + 1 of the range you want.

    Returns:
      None.
    """

    # Test preconditions.
    assert "STRING_INDEX_FIRST" in context or first is not None
    assert "STRING_INDEX_LAST" in context or last is not None

    if not first:
        first = context["STRING_INDEX_FIRST"]
    if not last:
        last = context["STRING_INDEX_LAST"]
    assert first < last

    assert "STRING_DELIMITER" in context
    assert "STRING_CHARMAP" in context
    assert "STRING_ADDRESS" in context
    base_addr = context["STRING_ADDRESS"]

    delim = context["STRING_DELIMITER"]
    assert isinstance(delim, bytes)

    charmap = context["STRING_CHARMAP"]
    assert isinstance(charmap, dict)

    with RomImage(context["TITLE"]) as mem:
        data = enumerate(enum_string(mem, first, last, base_addr, delim))
        for i, item in data:
            if charmap:
                text = get_text(item[1], charmap, delim)
            else:
                text = get_hex(item[1])

            print("{index:04X}:{address:06X}:{data}".format(
                index=i,
                address=item[0],
                data=text))
