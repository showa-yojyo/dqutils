# -*- coding: utf-8 -*-

"""Module dqutils.dq5.string -- a string loader for DQ5.

A string is an array of characters that are rendered in windows with the small
font.

This module has a few functions capable to load strings in the forms of
raw bytes and legible texts.
"""

from dqutils.address import from_hi
from dqutils.address import from_lo
from dqutils.address import conv_hi
from dqutils.address import conv_lo
from dqutils.rom_image import RomImage
from dqutils.string import get_text
from dqutils.dq5.charsmall import CHARMAP
from dqutils.dq5.charsmall import process_dakuten

# the string table map at $21955B
CONTEXT_GROUP = [
    # 仲間の名前
    dict(addr_string=0x23C5CE, string_id_first=0, string_id_last=8),
    # 職業名
    dict(addr_string=0x23C5F9, string_id_first=0, string_id_last=17),
    # 性別
    dict(addr_string=0x23C690, string_id_first=0, string_id_last=3),
    # じゅもん・とくぎの名前
    dict(addr_string=0x228000, string_id_first=0, string_id_last=171),
    # モンスター名
    dict(addr_string=0x23C69C, string_id_first=0, string_id_last=236),
    # アイテム名
    dict(addr_string=0x23CE0E, string_id_first=0, string_id_last=216),
    # さくせん名
    dict(addr_string=0x23D5B5, string_id_first=0, string_id_last=6),
    # 不明 1
    dict(addr_string=0x308000, string_id_first=0, string_id_last=0),
    # 不明 2
    dict(addr_string=0x23D6A1, string_id_first=0, string_id_last=0),
    # 同上
    dict(addr_string=0x23D6A1, string_id_first=0, string_id_last=0),
    # 仲間モンスターの名前
    dict(addr_string=0x23C242, string_id_first=0, string_id_last=168),
    # ルーラ行き先
    dict(addr_string=0x23D5F3, string_id_first=0, string_id_last=23),
    ]

CONTEXT_PROTOTYPE = dict(
    title="DRAGONQUEST5",
    mapper='LoROM',
    charmap=CHARMAP,)

for group in CONTEXT_GROUP:
    group.update(CONTEXT_PROTOTYPE)

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

    if not first:
        first = context["string_id_first"]
    if not last:
        last = context["string_id_last"]
    if first == last:
        raise StopIteration

    mapper = context["mapper"]
    if mapper == 'HiROM':
        from_rom_addr = from_hi
        from_cpu_addr = conv_hi
    elif mapper == 'LoROM':
        from_rom_addr = from_lo
        from_cpu_addr = conv_lo

    addr = context["addr_string"]

    with RomImage(context["title"]) as mem:
        mem.seek(from_cpu_addr(addr))
        for _ in range(0, last):
            size = mem.read(1)[0]
            if size:
                yield (addr, mem.read(size))
            addr += size + 1

def print_all():
    """Print all of the strings in DQ5 to sys.stdout."""

    for i, context in enumerate(CONTEXT_GROUP):
        print('Group #{0:d}'.format(i))

        charmap = context["charmap"]
        assert charmap is None or isinstance(charmap, dict)

        for j, item in enumerate(enum_string(context)):
            text = process_dakuten(get_text(item[1], charmap, None))
            print('{index:04X}:{address:06X}:{data}'.format(
                index=j,
                address=item[0],
                data=text))
