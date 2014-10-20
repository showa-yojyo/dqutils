# -*- coding: utf-8 -*-
""" dqutils.rom_image module - TBW
"""

import mmap
from dqutils.config import get_config
from dqutils.mapper import HiROM
from dqutils.mapper import LoROM

# pylint: disable=too-few-public-methods
class RomImage(object):
    """TBW"""

    def __init__(self, title):
        self.title = title
        self.fin = None
        self.image = None

    def __enter__(self):
        rompath = get_config().get('ROM', self.title)
        fin = open(rompath, 'rb')
        image = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        self.fin, self.image = fin, image

        return self.image

    def __exit__(self, exc_type, exc_value, traceback):
        if self.image:
            self.image.close()
        if self.fin:
            self.fin.close()

def get_snes_header(mem):
    """Return the SNES header of 64 bytes.

    Args:
      mem (mmap): A ROM image.

    Returns:
      (bytes): The SNES header of the ROM image.
    """

    try:
        bkp = mem.tell()
        for i in (0x7fc0, 0xffc0):
            mem.seek(i)
            buffer = mem.read(64)

            chksum1 = int.from_bytes(buffer[0x1C:0x1E], 'little')
            chksum2 = int.from_bytes(buffer[0x1E:0x20], 'little')
            if chksum1 ^ chksum2 == 0xFFFF:
                return buffer
        else:
            return None
    finally:
        mem.seek(bkp)

def make_mapper(mem):
    """Return the mapper instance from a ROM header.

    Args:
      mem (mmap): A ROM image.

    Returns:
      (AbstractMapper): The mapper instance.
    """
    header = get_snes_header(mem)
    if header:
        if header[0x15] & 0x01 == 0x01:
            return HiROM()
        elif header[0x15] & 0x01 == 0x00:
            return LoROM()
