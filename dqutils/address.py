# -*- coding: utf-8 -*-
"""dqutils.address - SNES address conversion functions.
"""
from abc import ABCMeta
from abc import abstractmethod

class AbstractMapper(metaclass=ABCMeta):
    """The abstract class that represents the SNES ROM layout.

    LoROM or HiROM is used to map between ROM offsets and SNES addresses.

    See http://romhack.wikia.com/wiki/SNES_ROM_layout for more details
    (Especially, the section "Formulas to convert addresses" is useful.)
    """

    @abstractmethod
    def from_rom(self, romaddr):
        """Convert from a ROM address to a CPU address for HiROM.

        Args:
          romaddr (int): A ROM address, i.e. offsets in headerless ROM image.

        Returns:
          (int) CPU address.
        """
        pass

    @abstractmethod
    def from_cpu(self, cpuaddr):
        """Convert from a CPU address to a ROM address for HiROM.

        Args:
          cpuaddr (int): A CPU address.

        Returns:
          (int) ROM address.
        """
        pass

class HiROM(AbstractMapper):
    """HiROM mapper.

    HiROM maps each ROM bank into the whole (being addresses $0000 to
    $ffff) of each SNES bank, starting with SNES bank $40, and starting again
    with SNES bank $80.
    """

    def from_rom(self, romaddr):
        """Convert from a ROM address to a CPU address for HiROM.

        Args:
          romaddr (int): A ROM address, i.e. offsets in headerless ROM image.

        Returns:
          (int) CPU address.

        Examples:
          >>> mapper = HiROM()
          >>> cpuaddr = mapper.from_rom(0x020000)
          >>> print('0x{:06X}'.format(cpuaddr))
          0xC20000
        """
        return 0x00C00000 | (romaddr & 0x003FFFFF)

    def from_cpu(self, cpuaddr):
        """Convert from a CPU address to a ROM address for HiROM.

        To convert from a CPU address to a ROM address, first, remove bit 15.
        Second, moving all bits after it down one.

        Args:
          cpuaddr (int): A CPU address.

        Returns:
          (int) ROM address.

        Examples:
          >>> mapper = HiROM()
          >>> romaddr = mapper.from_cpu(0xC20000)
          >>> print('0x{:06X}'.format(romaddr))
          0x020000
        """
        return cpuaddr & 0x003FFFFF

class LoROM(AbstractMapper):
    """LoROM mapper.

    LoROM maps each ROM bank into the upper half (being addresses $8000 to $ffff)
    of each SNES bank, starting with SNES bank $00, and starting again with SNES
    bank $80.
    """

    def from_rom(self, romaddr):
        """Convert from a ROM address to a CPU address for HiROM.

        Args:
          romaddr (int): A ROM address, i.e. offsets in headerless ROM image.

        Returns:
          (int) CPU address.

        Examples:
          >>> mapper = LoROM()
          >>> cpuaddr = mapper.from_rom(0x008000)
          >>> print('0x{:06X}'.format(cpuaddr))
          0x018000
        """
        return ((romaddr & 0x00007FFF)
            | (((romaddr & 0x007F8000) << 1) | 0x00008000))

    def from_cpu(self, cpuaddr):
        """Convert from a CPU address to a ROM address for HiROM.

        Args:
          cpuaddr (int): A CPU address.

        Returns:
          (int) ROM address.

        Examples:
          >>> mapper = LoROM()
          >>> romaddr = mapper.from_cpu(0x018000)
          >>> print('0x{:06X}'.format(romaddr))
          0x008000
        """
        return (cpuaddr & 0x007FFF) | ((cpuaddr & 0x007F0000) >> 1)

def make_mapper(name):
    """Return the mapper instance from its class name.

    Args:
      name (string): 'HiROM' or 'LoROM'.

    Returns:
      (AbstractMapper): The mapper instance.
    """

    if name == 'HiROM':
        return HiROM()
    elif name == 'LoROM':
        return LoROM()
