# -*- coding: utf-8 -*-
""" dqutils.string - DQ common string components.

This module defines common functions that access string data.

A string is an array of characters rendered in windows with the small
font.

This module provides a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_hi
from dqutils.address import from_lo
from dqutils.address import conv_hi
from dqutils.address import conv_lo
from dqutils.rom_image import RomImage
from array import array

def get_text(code_seq, charmap, delims=None):
    """Return a text representation of a string.

    Args:
      code_seq: A string (instance of bytearray).
      charmap: The character dictionary.
      delims: The code of the delimiter character(s).

    Returns:
      string: e.g. "ひのきのぼう"
    """
    assert any(
        isinstance(code_seq, i) for i in (bytes, bytearray, array))
    assert isinstance(charmap, dict)
    assert delims is None or any(
        isinstance(code_seq, i) for i in (bytes, bytearray, array))

    if delims and code_seq[-1] in delims:
        code_seq = code_seq[0:-1]

    return ''.join(charmap.get(c, '[{0:02X}]'.format(c)) for c in code_seq)

def get_hex(code_seq):
    """Return a hex representation of a string.

    This function does not remove the delimiter code.

    Args:
      code_seq: A string (instance of bytearray).

    Returns:
      string: e.g. "26 24 12 24 DC 0E AC"
    """

    assert any(
        isinstance(code_seq, i) for i in (bytes, bytearray, array))
    return ' '.join('{:02X}'.format(c) for c in code_seq)

def enum_string(context, first=None, last=None):
    """Generate string data in a range of indices.

    String data that indices in [`first`, `last`) will be generated.

    Args:
      context: TBW
      first: The first index of the indices range you want.
      last: The last index + 1 of the indices range you want.

    Yields:
      int: The next CPU address of data in the range of 0 to `last` - 1.
      bytearray: The next bytes of data in the range of 0 to `last` - 1.
    """

    # Test preconditions.
    assert "title" in context

    if not first:
        first = context.get("string_id_first", context.get("message_id_first"))
    if not last:
        last = context.get("string_id_last", context.get("message_id_last"))
    assert first < last

    addr = context.get("addr_string", context.get("addr_message"))
    assert addr

    delims = context.get("delimiters")
    assert delims is None or isinstance(delims, bytes)

    mapper = context["mapper"]
    if mapper == 'HiROM':
        from_rom_addr = from_hi
        from_cpu_addr = conv_hi
    elif mapper == 'LoROM':
        from_rom_addr = from_lo
        from_cpu_addr = conv_lo

    with RomImage(context["title"]) as mem:
        mem.seek(from_cpu_addr(addr))

        for i in range(0, last):
            code_seq = bytearray()
            addr = from_rom_addr(mem.tell())
            code = b'\xFFFF' # dummy value
            while code not in delims:
                code = mem.read_byte()
                code_seq.append(code)

            if first <= i:
                assert code_seq[-1] in delims
                yield (addr, code_seq)

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
    delim = context["delimiters"]
    assert isinstance(delim, bytes)

    charmap = context["charmap"]
    assert isinstance(charmap, dict)

    for i, item in enumerate(enum_string(context, first, last)):
        if charmap:
            text = get_text(item[1], charmap, delim)
        else:
            text = get_hex(item[1])

        print("{index:04X}:{address:06X}:{data}".format(
            index=i,
            address=item[0],
            data=text))
