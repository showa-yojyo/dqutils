"""This module provides features dealing with SNES ROM images."""

from __future__ import annotations

import mmap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import TracebackType
    from typing import BinaryIO, Self

from dqutils.config import get_config, ConfigNotFoundError


# pylint: disable=too-few-public-methods
class RomImage:
    """This class manages the file handler of given SNES ROM image."""

    def __init__(self: Self, title: str) -> None:
        """Create an object of RomImage.

        Parameters
        ----------
        title : str
            The title of SNES ROM to read.

        Examples
        --------
        >>> with RomImage("DRAGONQUEST3") as rom:
        ...     header = get_snes_header(rom)

        See Also
        --------
        get_config, get_snes_header
        """

        self.title = title
        self.fin: BinaryIO
        self.image: mmap.mmap

    def __enter__(self: Self) -> mmap.mmap:
        conf = get_config()
        if not conf:
            raise ConfigNotFoundError

        fin = open(conf.get("ROM", self.title), "rb")  # noqa: SIM115
        image = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

        self.fin, self.image = fin, image
        return self.image

    def __exit__(
        self: Self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self.image:
            self.image.close()
        if self.fin:
            self.fin.close()


class RomHeaderNotFoundError(Exception):
    def __init__(self: Self) -> None:
        super().__init__("ROM header not found")


def get_snes_header(mem: mmap.mmap) -> bytes:
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
        for i in (0x7FC0, 0xFFC0):
            mem.seek(i)
            buffer = mem.read(64)

            # [$xFDC, $xFDE): checksum complement (inverse).
            # [$xFDE, $xFE0): checksum bytes.
            chksum1 = int.from_bytes(buffer[0x1C:0x1E], "little")
            chksum2 = int.from_bytes(buffer[0x1E:0x20], "little")
            if chksum1 ^ chksum2 == 0xFFFF:  # noqa: PLR2004
                return buffer
        raise RomHeaderNotFoundError
    finally:
        mem.seek(bkp)
