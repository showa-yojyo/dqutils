# -*- coding: utf-8 -*-
"""dqutils.message_generator module

This module provides decoding methods for both DQ3 and DQ6 message systems.
The original implementation is of course written in 65816 code.
Here are in Python version, which is based on C/C++ code version I wrote
before.
"""

from abc import ABCMeta
from abc import abstractmethod
from array import array
from dqutils.mapper import make_mapper
from dqutils.bit import get_bits
from dqutils.bit import get_int
from dqutils.rom_image import RomImage

class AbstractMessageGenerator(metaclass=ABCMeta):
    """TBW"""

    # pylint: disable=too-many-instance-attributes
    def __init__(self, context, first=None, last=None):
        """Constructor."""

        self.title = context["title"]
        self.mapper = make_mapper(context["mapper"])
        self.delimiters = context["delimiters"]

        if not first:
            first = context["message_id_first"]
        if not last:
            last = context["message_id_last"]
        self.first = first
        self.last = last

        self.addr_group = context["addr_group"]
        self.addr_shiftbit_array = context["addr_shiftbit_array"]
        self.addr_message = context["addr_message"]
        self.addr_huffman_off = context["addr_huffman_off"]
        self.addr_huffman_on = context["addr_huffman_on"]
        self.huffman_root = context["huffman_root"]

        self.shiftbit_array = None
        self.huffman_off = None
        self.huffman_on = None

        self.decoding_read_size = context.get("decoding_read_size", 2)
        self.decoding_mask = context.get("decoding_mask", 0xFFFF)

    def assert_valid(self):
        """Test if this instance is valid."""
        assert self.title
        assert self.mapper
        assert isinstance(self.delimiters, array)
        assert self.delimiters.typecode == 'H'
        assert 0 <= self.addr_group
        assert 0 <= self.addr_shiftbit_array
        assert len(self.shiftbit_array) == 8
        assert 0 <= self.addr_message
        assert 0 <= self.first < self.last
        assert 0 <= self.addr_huffman_off
        assert 0 <= self.addr_huffman_on
        assert 0 < self.huffman_root
        assert len(self.huffman_off) == self.huffman_root + 2
        assert len(self.huffman_on) == self.huffman_root + 2

    def setup(self, mem):
        """Setup this instance.

        Args:
          mem (mmap): The input stream of ROM.
        """

        self._setup_huffman_tree(mem)
        self._setup_shiftbit_array(mem)

        self.assert_valid()

    def _setup_huffman_tree(self, mem):
        """Initialize the Huffman trees.

        Args:
          mem (mmap): The input stream of ROM.

        Returns:
          None.
        """

        # Test preconditions.
        assert self.huffman_root
        assert self.addr_huffman_off
        assert self.addr_huffman_on

        if not self.huffman_off:
            mem.seek(self.mapper.from_cpu(self.addr_huffman_off))
            self.huffman_off = mem.read(self.huffman_root + 2)

        if not self.huffman_on:
            mem.seek(self.mapper.from_cpu(self.addr_huffman_on))
            self.huffman_on = mem.read(self.huffman_root + 2)

        # Test postconditions.
        assert len(self.huffman_off) == self.huffman_root + 2
        assert len(self.huffman_on) == self.huffman_root + 2

    def _setup_shiftbit_array(self, mem):
        """Initialize the shiftbit array.

        Args:
          mem (mmap): The input stream of ROM.

        Returns:
          None.
        """

        assert self.addr_shiftbit_array

        mem.seek(self.mapper.from_cpu(self.addr_shiftbit_array))
        self.shiftbit_array = mem.read(8)

        assert len(self.shiftbit_array) == 8

    def locate_message(self, mem, message_id):
        """Return the location where the messege data is stored.

        Args:
          mem (mmap): The input stream of ROM.
          message_id: An ID.

        Returns:
          TBW
        """

        count, group = self._do_select_message_group(message_id)

        mem.seek(self.mapper.from_cpu(self.addr_group) + group)
        buffer1 = mem.read(3)

        # In fact, the array in RHS is
        # {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80}.
        shift = self.shiftbit_array[buffer1[0] & 0x07]
        addr = get_bits(buffer1, 0, 0xFFFFF8) + self.addr_message
        delims = self.delimiters

        # The loop counter depends on message id & 0x0007.
        for _ in range(count):
            code = b'\xFFFF' # dummy value
            while not code in delims:
                addr, shift, code = self.decode(mem, addr, shift)

        return addr, shift

    def decode(self, mem, addr, shift):
        """Decoding algorithm of Huffman coding.

        Decode a Huffman-encoded bit string and return a decoded character.

        Args:
          mem (mmap): The ROM image.
          addr (int): The initial address to read the variable length-bit
            string.
          shift (int): The initial shift bit of the address.

        Returns:
          An instance of tuple (addr, shift, value), where `addr` and
          `shift` is the next location to read, and `value` is the
          character code decoded from the Huffman tree.
        """

        # Test preconditions
        assert addr & 0xFF000000 == 0
        assert shift & 0xFFFFFF00 == 0

        huffman_on, huffman_off = self.huffman_on, self.huffman_off
        node = self.huffman_root
        from_cpu_addr = self.mapper.from_cpu
        read_size = self.decoding_read_size

        # Traverse the Huffman tree downward beginning at the root node.
        while True:
            # The message is a variable length-bit string.
            # We take successive bits from the initial `addr`.
            mem.seek(from_cpu_addr(addr))

            bit = get_int(mem.read(read_size), 0, read_size) & shift
            addr, shift = self._do_next_location(addr, shift)

            if bit:
                node = get_int(huffman_on, node, 2)
            else:
                node = get_int(huffman_off, node, 2)

            if self._do_is_leaf_node(node):
                break

            node = self._do_next_node(node)

        return addr, shift, node & self.decoding_mask

    def __iter__(self):
        """Generate message data.

        Yields:
          A tuple of (address, shift-bits, character-code).
        """
        with RomImage(self.title) as mem:
            self.setup(mem)

            first = self.first
            last = self.last
            assert 0 <= first <= last
            if self.first == self.last:
                raise StopIteration

            # Locate the first data location.
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

                yield addr, shift, code_seq

    @abstractmethod
    def _do_select_message_group(self, message_id):
        """TBW

        Args:
          message_id (int): A message ID.

        Returns:
          A tuple (int, int), where:
            int: count TBW
            int: group TBW
        """
        pass

    @abstractmethod
    def _do_is_leaf_node(self, node):
        """Determine if `node` is a leaf node.

        Args:
          node (int): 2-byte value.

        Returns:
          bool: True if `node` is a leaf, False otherwise.
        """
        pass

    @abstractmethod
    def _do_next_location(self, addr, shift):
        """Returns the next address to read data encoded.

        Args:
          addr (int): The current CPU address.
          shift (int): An 1-byte value for mask.

        Returns:
          (tuple of int): The next address and shift-bit.
        """
        pass

    @abstractmethod
    def _do_next_node(self, node):
        """Returns the next node to traverse in the Huffman tree.

        Args:
          node (int): The current node, represented by 2-byte value.

        Returns:
          (int): The next node, represented by 2-byte value.
        """
        pass

class MessageGeneratorW(AbstractMessageGenerator):
    """For DQ3 and DQ6."""

    def _do_select_message_group(self, message_id):
        # The message ID gives the folowing information:
        # 1. 0007h bits: the number of AEh occurrences,
        #    e.g., in DQ3, the index of the array $C1B01C (1byte * 8)
        # 2. FFF8h bits: in DQ3, the index of the array $C15331 (3byte * N),
        #    which contains offset values from address $FCC258.
        count = message_id & 0x0007
        group = message_id >> 3
        group += (group << 1)
        return count, group

    def _do_is_leaf_node(self, node):
        return node & 0x8000 == 0

    def _do_next_location(self, addr, shift):
        shift >>= 1
        if shift == 0:
            shift = 0x80
            addr = self.mapper.increment_address(addr)
        return addr, shift

    def _do_next_node(self, value):
        return value & 0x7FFF

class MessageGeneratorV(AbstractMessageGenerator):
    """For DQ5."""

    def _do_select_message_group(self, message_id):
        count = message_id & 0x000F
        group = message_id // 16 * 3
        return count, group

    def _do_is_leaf_node(self, node):
        return node & 0x8000

    def _do_next_location(self, addr, shift):
        shift <<= 1
        if shift > 0x80:
            shift = 0x01
            addr = self.mapper.increment_address(addr)
        return addr, shift

    def _do_next_node(self, node):
        node &= 0x1FFF
        node <<= 1
        return node
