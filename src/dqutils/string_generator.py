"""This module provides helper classes for the string module."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, cast

from dqutils.snescpu.mapper import AbstractMapper, make_mapper
from dqutils.snescpu.rom_image import RomImage

if TYPE_CHECKING:
    import mmap
    from collections.abc import Iterator, Mapping
    from typing import Any

    type StringInfo = tuple[int, bytes | bytearray]
    type ContextT = Mapping[str, Any]


# pylint: disable=too-few-public-methods
class AbstractStringGenerator(metaclass=ABCMeta):
    """The base class of StringGenerator subclasses."""

    def __init__(
        self,
        context: ContextT,
        first: int | None = None,
        last: int | None = None,
    ) -> None:
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

        if first is None:
            first = context.get("string_id_first", context.get("message_id_first"))
        if last is None:
            last = context.get("string_id_last", context.get("message_id_last"))

        self.title: str = context["title"]
        self.first: int = cast(int, first)
        self.last: int = cast(int, last)
        self.addr: int = context.get("addr_string", context.get("addr_message"))
        self.delims: bytes | None = context.get("delimiters")
        self.mapper: type[AbstractMapper]
        self.assert_valid()

    def __iter__(self) -> Iterator[StringInfo]:
        self.assert_valid()

        if self.first >= self.last:
            return

        with RomImage(self.title) as mem:
            self.mapper = make_mapper(rom=mem)
            addr = self.addr
            mem.seek(self.mapper.from_cpu(addr))
            yield from self._do_iterate(mem, addr)

    def assert_valid(self) -> None:
        """Test if this instance is valid."""
        if not self.title:
            msg = "title is not set"
            raise ValueError(msg)
        # assert self.first and self.last and 0 <= self.first <= self.last
        if self.addr < 0:
            msg = f"addr {self.addr} must be non-negative value"
            raise ValueError(msg)
        if self.delims and not isinstance(self.delims, bytes):
            msg = f"{self.delims} not supported as delimiters"
            raise TypeError(msg)

    @abstractmethod
    def _do_iterate(self, mem: mmap.mmap, addr: int) -> Iterator[StringInfo]:
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
    """Return generator iterators for Pascal-style (size-included) strings information."""

    def _do_iterate(self, mem: mmap.mmap, addr: int) -> Iterator[StringInfo]:
        first, last = self.first, self.last
        for i in range(last):
            if (size := mem.read(1)[0]) and first <= i:
                yield (addr, mem.read(size))
            addr += size + 1


class StringGeneratorCStyle(AbstractStringGenerator):
    """Return generator iterators for C-style (null-terminated) strings information."""

    def _do_iterate(self, mem: mmap.mmap, addr: int) -> Iterator[StringInfo]:
        first, last = self.first, self.last
        delims = self.delims
        from_rom_addr = self.mapper.from_rom
        for i in range(last):
            code_seq = bytearray()
            addr = from_rom_addr(mem.tell())

            # do-while loop
            code = mem.read_byte()
            code_seq.append(code)
            while code not in delims:
                code = mem.read_byte()
                code_seq.append(code)

            if first <= i:
                # assert code_seq[-1] in delims
                yield (addr, code_seq)
