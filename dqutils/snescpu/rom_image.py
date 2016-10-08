"""This module provides features dealing with SNES ROM images.
"""

import mmap
from dqutils.config import get_config

# pylint: disable=too-few-public-methods
class RomImage(object):
    """This class manages the file handler of given SNES ROM image."""

    def __init__(self, title):
        """Create an object of RomImage.

        Parameters
        ----------
        title : str
            The title of SNES ROM to read.

        Examples
        --------
        >>> with RomImage('DRAGONQUEST3') as rom:
        ...     header = get_snes_header(rom)
        ...

        See Also
        --------
        get_config, get_snes_header
        """

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
    """Return the 64 bytes of cartridge information a.k.a. SNES
    header.

    Parameters
    ----------
    mem : mmap.mmap
        A memory-mapped file object associated with an SNES ROM.

    Returns
    -------
    buffer : bytes
        The 64 bytes that contains cartridge information of the
        ROM.
    """

    assert not mem.closed

    bkp = mem.tell()
    try:
        # Detect which ROM type it is.
        # For LoROM, SNES header is located in [$7FC0, $8000),
        # while for HiROM, in [$FFC0, $10000).
        for i in (0x7fc0, 0xffc0):
            mem.seek(i)
            buffer = mem.read(64)

            # [$xFDC, $xFDE): checksum complement (inverse).
            # [$xFDE, $xFE0): checksum bytes.
            chksum1 = int.from_bytes(buffer[0x1C:0x1E], 'little')
            chksum2 = int.from_bytes(buffer[0x1E:0x20], 'little')
            if chksum1 | chksum2 == 0xFFFF:
                return buffer
        return None
    finally:
        mem.seek(bkp)
