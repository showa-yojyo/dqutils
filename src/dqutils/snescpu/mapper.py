"""dqutils.address - SNES address conversion functions."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    import mmap

from dqutils.snescpu.rom_image import get_snes_header


class AbstractMapper(metaclass=ABCMeta):
    """The abstract class that represents the SNES ROM layout.

    LoROM and HiROM are mapping of addresses/offsets between an
    SNES cartridge offsets and addresses of runtime memory space.

    See http://romhack.wikia.com/wiki/SNES_ROM_layout for more
    details (Especially, the section "Formulas to convert addresses"
    is useful.)
    """

    bank_offset_size: int
    """The number of bytes in one bank."""

    @staticmethod
    @abstractmethod
    def check_header_mapper_byte(mapper_byte: int) -> bool:
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : int
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """

    @staticmethod
    @abstractmethod
    def from_rom(romaddr: int) -> int:
        """Convert from a ROM address to a CPU address for HiROM.

        Parameters
        ----------
        romaddr : int
            A ROM address, i.e. offsets in SMC-headerless ROM image.

        Returns
        -------
        cpuaddr : int
            A CPU address.
        """

    @staticmethod
    @abstractmethod
    def from_cpu(cpuaddr: int) -> int:
        """Convert from a CPU address to a ROM address for HiROM.

        Parameters
        ----------
        cpuaddr : int
            A CPU address.

        Returns
        -------
        romaddr : int
            A ROM address.
        """

    @staticmethod
    @abstractmethod
    def increment_address(addr: int) -> int:
        """Increment given CPU address.

        Parameters
        ----------
        addr : int
            A CPU address.

        Returns
        -------
        cpuaddr : int
            A CPU address.
        """


class HiROM(AbstractMapper):
    """HiROM mapper.

    HiROM maps each ROM bank into the whole (being addresses $0000 to
    $ffff) of each SNES bank, starting with SNES bank $40, and
    starting again with SNES bank $80.
    """

    bank_offset_size = 0x10000

    @staticmethod
    def check_header_mapper_byte(mapper_byte: int) -> bool:
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : int
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """
        return mapper_byte & 0x01 == 0x01

    @staticmethod
    def from_rom(romaddr: int) -> int:
        """Convert from a ROM address to a CPU address for HiROM.

        Parameters
        ----------
        romaddr : int
            A ROM address, i.e. offsets in SMC-headerless ROM image.

        Returns
        -------
        cpuaddr : int
            A CPU address.

        Examples
        --------
        >>> mapper = HiROM
        >>> cpuaddr = mapper.from_rom(0x020000)
        >>> print(f"{cpuaddr:#06x}")
        0xc20000
        """
        return 0x00C00000 | (romaddr & 0x003FFFFF)

    @staticmethod
    def from_cpu(cpuaddr: int) -> int:
        """Convert from a CPU address to a ROM address for HiROM.

        To convert from a CPU address to a ROM address, first,
        remove bit 15.
        Second, moving all bits after it down one.

        Parameters
        ----------
        cpuaddr : int
            A CPU address.

        Returns
        -------
        romaddr : int
            A ROM address.

        Examples
        --------
        >>> mapper = HiROM
        >>> romaddr = mapper.from_cpu(0xC20000)
        >>> print(f"{romaddr:#06x}")
        0x020000
        """
        return cpuaddr & 0x003FFFFF

    @staticmethod
    def increment_address(addr: int) -> int:
        """Increment given CPU address.

        Parameters
        ----------
        addr : int
            A CPU address.

        Returns
        -------
        cpuaddr : int
            A CPU address.
        """
        return addr + 1


class LoROM(AbstractMapper):
    """LoROM mapper.

    LoROM maps each ROM bank into the upper half (being addresses
    $8000 to $ffff) of each SNES bank, starting with SNES bank $00,
    and starting again with SNES bank $80.
    """

    bank_offset_size = 0x8000

    @staticmethod
    def check_header_mapper_byte(mapper_byte: int) -> bool:
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : int
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """
        return mapper_byte & 0x01 == 0x00

    @staticmethod
    def from_rom(romaddr: int) -> int:
        """Convert from a ROM address to a CPU address for HiROM.

        Parameters
        ----------
        romaddr : int
            A ROM address, i.e. offsets in headerless ROM image.

        Returns
        -------
        cpuaddr : int
            A CPU address.

        Examples
        --------
        >>> mapper = LoROM
        >>> cpuaddr = mapper.from_rom(0x008000)
        >>> print(f"{cpuaddr:#06X}")
        0x018000
        """
        return (romaddr & 0x00007FFF) | (((romaddr & 0x007F8000) << 1) | 0x00008000)

    @staticmethod
    def from_cpu(cpuaddr: int) -> int:
        """Convert from a CPU address to a ROM address for HiROM.

        Parameters
        ----------
        cpuaddr : int
            A CPU address.

        Returns
        -------
        romaddr : int
            A ROM address.

        Examples
        --------
        >>> mapper = LoROM
        >>> romaddr = mapper.from_cpu(0x018000)
        >>> print(f"{romaddr:#06X}")
        0x008000
        """
        return (cpuaddr & 0x007FFF) | ((cpuaddr & 0x007F0000) >> 1)

    @staticmethod
    def increment_address(addr: int) -> int:
        """Increment given CPU address.

        Parameters
        ----------
        addr : int
            A CPU address.

        Returns
        -------
        cpuaddr : int
            A CPU address.
        """
        addr += 1
        if addr & 0xFFFF == 0:
            # LoROM next bank
            addr = (addr & 0xFF0000) | 0x8000
        return addr


class MapperNotFoundError(Exception):
    def __init__(self: Self) -> None:
        super().__init__("Mapper type not found")


HEADER_LENGTH = 0x40


def make_mapper(rom: mmap.mmap | None = None, name: str | None = None) -> type[AbstractMapper]:
    """Return a mapper type.

    You may also directly use subclasses of class AbstractMapper.

    Parameters
    ----------
    rom : mmap.mmap, default: None
        A ROM image object.
    name : str
        Mapper's name. Either 'HiROM' or 'LoROM' may be specified.

    Returns
    -------
    mapper : type[AbstractMapper]
        The mapper type.

    See also
    --------
    get_snes_header
    """

    assert rom or name

    # pylint: disable=no-member
    mappers = AbstractMapper.__subclasses__()

    if rom:
        header = get_snes_header(rom)
        assert isinstance(header, bytes)
        assert len(header) == HEADER_LENGTH

        # ROM makeup byte.
        mapper_byte = header[0x15]
        return next(cls for cls in mappers if cls.check_header_mapper_byte(mapper_byte))

    if name:
        return next(cls for cls in mappers if cls.__name__ == name)

    raise MapperNotFoundError
