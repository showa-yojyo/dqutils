"""dqutils.address - SNES address conversion functions.
"""
from abc import (ABCMeta, abstractmethod)

class AbstractMapper(metaclass=ABCMeta):
    """The abstract class that represents the SNES ROM layout.

    LoROM and HiROM are mapping of addresses/offsets between an
    SNES cartridge offsets and addresses of runtime memory space.

    See http://romhack.wikia.com/wiki/SNES_ROM_layout for more
    details (Especially, the section "Formulas to convert addresses"
    is useful.)
    """

    bank_offset_size = None
    """The number of bytes in one bank."""

    @staticmethod
    @abstractmethod
    def check_header_mapper_byte(mapper_byte):
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : bytes
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """
        pass

    @staticmethod
    @abstractmethod
    def from_rom(romaddr):
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
        pass

    @staticmethod
    @abstractmethod
    def from_cpu(cpuaddr):
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
        pass

    @staticmethod
    @abstractmethod
    def increment_address(addr):
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
        pass

class HiROM(AbstractMapper):
    """HiROM mapper.

    HiROM maps each ROM bank into the whole (being addresses $0000 to
    $ffff) of each SNES bank, starting with SNES bank $40, and
    starting again with SNES bank $80.
    """

    bank_offset_size = 0x10000

    @staticmethod
    def check_header_mapper_byte(mapper_byte):
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : bytes
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """
        return mapper_byte & 0x01 == 0x01

    @staticmethod
    def from_rom(romaddr):
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
        >>> print('0x{:06X}'.format(cpuaddr))
        0xC20000
        """
        return 0x00C00000 | (romaddr & 0x003FFFFF)

    @staticmethod
    def from_cpu(cpuaddr):
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
        >>> print('0x{:06X}'.format(romaddr))
        0x020000
        """
        return cpuaddr & 0x003FFFFF

    @staticmethod
    def increment_address(addr):
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
    def check_header_mapper_byte(mapper_byte):
        """Return the mapper name.

        Parameters
        ----------
        mapper_byte : bytes
            The 0x15th byte of SNES header of 64 bytes.

        Returns
        -------
        matched : bool
            Determine if this mapper matches the `mapper_byte`.
        """
        return mapper_byte & 0x01 == 0x00

    @staticmethod
    def from_rom(romaddr):
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
        >>> print('0x{:06X}'.format(cpuaddr))
        0x018000
        """
        return ((romaddr & 0x00007FFF)
                | (((romaddr & 0x007F8000) << 1) | 0x00008000))

    @staticmethod
    def from_cpu(cpuaddr):
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
        >>> print('0x{:06X}'.format(romaddr))
        0x008000
        """
        return (cpuaddr & 0x007FFF) | ((cpuaddr & 0x007F0000) >> 1)

    @staticmethod
    def increment_address(addr):
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

def make_mapper(**kwargs):
    """Return a mapper type.

    You may also directly use subclasses of class AbstractMapper.

    Parameters
    ----------
    name : str
        Mapper's name. Either 'HiROM' or 'LoROM' may be specified.
    header : bytes
        0x40 byte header of SNES ROM.

    Returns
    -------
    mapper : AbstractMapper
        The mapper type.

    See also
    --------
    get_snes_header
    """

    # pylint: disable=no-member
    mappers = AbstractMapper.__subclasses__()

    name = kwargs.get('name')
    if name:
        return next(cls for cls in mappers
                    if cls.__name__ == name)

    header = kwargs.get('header')
    if header:
        assert isinstance(header, bytes)
        assert len(header) == 0x40

        # ROM makeup byte.
        mapper_byte = header[0x15]
        return next(cls for cls in mappers
                    if cls.check_header_mapper_byte(mapper_byte))
