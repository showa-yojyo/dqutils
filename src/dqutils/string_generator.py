"""This module provides helper classes for the string module.
"""

from abc import (ABCMeta, abstractmethod)
from .snescpu.mapper import make_mapper
from .snescpu.rom_image import RomImage

# pylint: disable=too-few-public-methods
class AbstractStringGenerator(metaclass=ABCMeta):
    """The base class of StringGenerator subclasses."""

    def __init__(self, context, first=None, last=None):
        """Create an object of class AbstractStringGenerator.

        Parameters
        ----------
        context : dict
            This shall have the following keys:

            - ``title``: the game title.
            - ``addr_string`` or ``addr_message``: the address that
              string or message data are stored.
            - ``delimiters``: delimeter characters, in type bytes.

            and the following keys are optional:

            - ``string_id_first`` or ``message_id_first``:
              this value is referred when `first` is not specified.
            - ``string_id_last`` or ``message_id_last``:
              this value is referred when `last` is not specified.

        first : int, optional
            The first index of the range of indices you want.
        last : int, optional
            The last index + 1 of the range of indices you want.
        """

        assert "title" in context
        title = context["title"]

        if not first:
            first = context.get("string_id_first",
                                context.get("message_id_first"))
        if not last:
            last = context.get("string_id_last",
                               context.get("message_id_last"))
        assert 0 <= first <= last

        addr = context.get("addr_string", context.get("addr_message"))
        assert addr

        delims = context.get("delimiters")
        assert delims is None or isinstance(delims, bytes)

        self.title = title
        self.first = first
        self.last = last
        self.addr = addr
        self.delims = delims
        self.mapper = None
        self.assert_valid()

    def __iter__(self):
        self.assert_valid()

        if self.first == self.last:
            raise StopIteration

        with RomImage(self.title) as mem:
            self.mapper = make_mapper(rom=mem)
            addr = self.addr
            mem.seek(self.mapper.from_cpu(addr))
            yield from self._do_iterate(mem, addr)

    def assert_valid(self):
        """Test if this instance is valid."""
        assert self.title
        assert 0 <= self.first <= self.last
        assert self.addr >= 0
        assert self.delims is None or isinstance(self.delims, bytes)

    @abstractmethod
    def _do_iterate(self, mem, addr):
        """Iterate pairs of string information.

        Parameters
        ----------
        mem : mmap
            The ROM image.
        addr : int
            An offset value in which a character string locates.

        Yields
        ------
        addr : int
            An offset value of the ROM address space.
        code_seq : bytearray
            A sequence of characters locating in `addr`.
        """
        raise StopIteration

class StringGeneratorPascalStyle(AbstractStringGenerator):
    """Return generator iterators for Pascal-style (size-included)
    strings information.
    """

    def _do_iterate(self, mem, addr):
        first, last = self.first, self.last
        for i in range(0, last):
            size = mem.read(1)[0]
            if size and first <= i:
                yield (addr, mem.read(size))
            addr += size + 1

class StringGeneratorCStyle(AbstractStringGenerator):
    """Return generator iterators for C-style (null-terminated)
    strings information.
    """

    def _do_iterate(self, mem, addr):
        first, last = self.first, self.last
        delims = self.delims
        from_rom_addr = self.mapper.from_rom
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
