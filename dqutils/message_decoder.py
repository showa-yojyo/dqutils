# -*- coding: utf-8 -*-

"""dqutils.MessageDecoder module

This module provides decoding methods for both DQ3 and DQ6 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.
"""

from array import array
from dqutils.address import from_hi as CPUADDR
from dqutils.address import conv_hi as ROMADDR
from dqutils.bit import get_int

class MessageDecoder(object):
    """TBW"""

    # pylint: disable=too-many-instance-attributes
    def __init__(self, **kwargs):
        """Constructor."""

        self.delimiters = kwargs["delimiters"]
        self.message_id_first = kwargs["message_id_first"]
        self.message_id_last = kwargs["message_id_last"]

        self.addr_group = kwargs["addr_group"]
        self.addr_shiftbit_array = kwargs["addr_shiftbit_array"]
        self.addr_message = kwargs["addr_message"]
        self.addr_huffman_off = kwargs["addr_huffman_off"]
        self.addr_huffman_on = kwargs["addr_huffman_on"]
        self.huffman_root = kwargs["huffman_root"]

        self.shiftbit_array = None
        self.huffman_off = None
        self.huffman_on = None

    def assert_valid(self):
        """Test if this instance is valid."""
        assert isinstance(self.delimiters, array) and self.delimiters.typecode == 'H'
        assert 0 < self.addr_group
        assert 0 < self.addr_shiftbit_array
        assert len(self.shiftbit_array) == 8
        assert 0 < self.addr_message
        assert 0 <= self.message_id_first < self.message_id_last
        assert 0 < self.addr_huffman_off
        assert 0 < self.addr_huffman_on
        assert 0 < self.huffman_root
        assert len(self.huffman_off) == self.huffman_root + 2
        assert len(self.huffman_on) == self.huffman_root + 2

    def setup(self, mem):
        """TBW"""

        self.setup_huffman_tree(mem)
        self.setup_shiftbit_array(mem)

        self.assert_valid()

    def setup_huffman_tree(self, mem):
        """Initialize the Huffman trees."""

        # Test preconditions.
        assert self.huffman_root
        assert self.addr_huffman_off
        assert self.addr_huffman_on

        if not self.huffman_off:
            mem.seek(ROMADDR(self.addr_huffman_off))
            self.huffman_off = mem.read(self.huffman_root + 2)

        if not self.huffman_on:
            mem.seek(ROMADDR(self.addr_huffman_on))
            self.huffman_on = mem.read(self.huffman_root + 2)

        # Test postconditions.
        assert len(self.huffman_off) == self.huffman_root + 2
        assert len(self.huffman_on) == self.huffman_root + 2

    def setup_shiftbit_array(self, mem):
        """Initialize the shiftbit array."""

        assert self.addr_shiftbit_array

        mem.seek(ROMADDR(self.addr_shiftbit_array))
        self.shiftbit_array = mem.read(8)

        assert len(self.shiftbit_array) == 8

    def locate_message(self, mem, message_id):
        """Return the location where the messege data is stored."""

        # メッセージ ID から取得できるデータは二つ:
        # 1. 0007h = AEh を検出する回数
        #          = $C1B01C shift 配列 (1byte * 8) のインデックス
        # 2. FFF8h = $C15331 構造体 (3byte) のインデックス
        #            $FCC258 からのオフセット

        count = message_id & 0x0007
        group = message_id >> 3
        group += (group << 1)

        mem.seek(ROMADDR(self.addr_group) + group)
        buffer1 = mem.read(3)

        # In fact, the array in RHS is
        # {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80}.
        shift = self.shiftbit_array[buffer1[0] & 0x07]

        addr = (get_int(buffer1, 0, 3) >> 3) + ROMADDR(self.addr_message)

        delims = self.delimiters

        # The loop counter depends on msgid % 7.
        for _ in range(count):
            code = b'\xFFFF' # dummy value
            while not code in delims:
                addr, shift, code = self.decode(mem, addr, shift)

        return addr, shift

    def decode(self, mem, addr, shift):
        """Decoding algorithm of Huffman coding."""

        # Test preconditions
        assert addr & 0xFF000000 == 0
        assert shift & 0xFFFFFF00 == 0

        huffman_on, huffman_off = self.huffman_on, self.huffman_off
        node = self.huffman_root

        while True:
            mem.seek(ROMADDR(addr))
            buffer = mem.read(2)
            value = int.from_bytes(buffer, byteorder='little') & shift

            shift >>= 1
            if shift == 0:
                shift = 0x0080
                addr += 1

            if value:
                value = get_int(huffman_on, node, 2)
            else:
                value = get_int(huffman_off, node, 2)

            if value & 0x8000 == 0:
                return addr, shift, value

            node = value & 0x7FFF

    def enumerate(self, mem, first=None, last=None):
        """Generate a tuple of (address, shift bits, code)."""

        if not first:
            first = self.message_id_first
        if not last:
            last = self.message_id_last
        assert first < last

        # Yield the first data location.
        addr_cur, shift_cur = self.locate_message(mem, first)

        delims = self.delimiters
        assert isinstance(delims, array) and delims.typecode == 'H'

        for _ in range(first, last):
            addr, shift = addr_cur, shift_cur

            # Array of unsigned short values.
            code_seq = array('H')
            code = b'\xFFFF' # dummy value
            while not code in delims:
                addr_cur, shift_cur, code = self.decode(
                    mem, addr_cur, shift_cur)
                code_seq.append(code)

            yield CPUADDR(addr), shift, code_seq
