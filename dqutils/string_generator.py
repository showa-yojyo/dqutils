# -*- coding: utf-8 -*-
""" dqutils.string_generator - DQ common string components.

This module defines common functions that access string data.

A string is an array of characters rendered in windows with the small
font.

This module provides a few functions capable to load strings in the forms of
raw bytes.
"""

from dqutils.address import make_mapper
from dqutils.rom_image import RomImage
from abc import ABCMeta
from abc import abstractmethod

# pylint: disable=too-few-public-methods
class AbstractStringGenerator(metaclass=ABCMeta):
    """TBW"""

    def __init__(self, context, first=None, last=None):
        """Constructor"""

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
        self.mapper = make_mapper(context["mapper"])

        self.assert_valid()

    def __iter__(self):
        """TBW"""
        self.assert_valid()

        if self.first == self.last:
            raise StopIteration

        with RomImage(self.title) as mem:
            addr = self.addr
            mem.seek(self.mapper.from_cpu(addr))
            yield from self._do_iterate(mem, addr)

    def assert_valid(self):
        """Test if this instance is valid."""
        assert self.title
        assert 0 <= self.first < self.last
        assert 0 <= self.addr
        assert self.delims is None or isinstance(self.delims, bytes)
        assert self.mapper

    @abstractmethod
    def _do_iterate(self, mem, addr):
        """TBW"""
        raise StopIteration

class StringGeneratorPascalStyle(AbstractStringGenerator):
    """For DQ5"""

    def _do_iterate(self, mem, addr):
        """TBW"""

        first, last = self.first, self.last
        for i in range(0, last):
            size = mem.read(1)[0]
            if size and first <= i:
                yield (addr, mem.read(size))
            addr += size + 1

class StringGeneratorCStyle(AbstractStringGenerator):
    """For DQ3 and DQ6"""

    def _do_iterate(self, mem, addr):
        """TBW"""

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
