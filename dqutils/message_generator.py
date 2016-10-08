"""
This module provides decoding methods for both DQ3 and DQ6 message
systems.

The original implementation is written in the 65816 Processor codes.
Here are in Python version, which is based on C/C++ implementation
I wrote a long ago.
"""

from abc import (ABCMeta, abstractmethod)
from array import array
from dqutils.bit import (get_bits, get_int)
from dqutils.snescpu.mapper import make_mapper
from dqutils.snescpu.rom_image import (RomImage, get_snes_header)

class AbstractMessageGenerator(metaclass=ABCMeta):
    """The base class of MessageGenerator subclasses."""

    # pylint: disable=too-many-instance-attributes
    def __init__(self, context, first=None, last=None):
        """Create an object of class AbstractMessageGenerator.

        Parameters
        ----------
        context : dict
            This shall have the following keys:

            - ``title``: the game title.
            - ``delimiters``: delimeter characters, in type bytes.
            - ``addr_group``: the address of information on message
              grouping information.
            - ``addr_shiftbit_array``: the address of information
              on shift bits corresponding the message grouping.
            - ``addr_message``: the address that message data are
            stored.
            - ``addr_huffman_off``: the address of the OFF branch.
            - ``addr_huffman_on``: the address of the ON branch.
            - ``huffman_root ``: the value of the root.

            and the following keys are optional:

            - ``message_id_first``: this value is referred when
              `first` is not specified.
            - ``message_id_last``: this value is referred when
              `last` is not specified.
            - ``decoding_read_size``: the size of an encoded code.
            - ``decoding_mask``: the mask for an decoded code.

        first : int, optional
            The first index of the range of indices you want.
        last : int, optional
            The last index + 1 of the range of indices you want.
        """

        self.title = context["title"]
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

        self.mapper = None

    def assert_valid(self):
        """Test if this instance is valid."""
        assert self.title
        assert self.mapper
        assert isinstance(self.delimiters, array)
        assert self.delimiters.typecode == 'H'
        assert self.addr_group >= 0
        assert self.addr_shiftbit_array >= 0
        assert len(self.shiftbit_array) == 8
        assert self.addr_message >= 0
        assert 0 <= self.first < self.last
        assert self.addr_huffman_off >= 0
        assert self.addr_huffman_on >= 0
        assert self.huffman_root > 0
        assert len(self.huffman_off) == self.huffman_root + 2
        assert len(self.huffman_on) == self.huffman_root + 2

    def setup(self, mem):
        """Setup this instance.

        Parameters
        ----------
        mem : mmap.mmap
            The input stream of ROM.
        """

        self.mapper = make_mapper(header=get_snes_header(mem))

        self._setup_huffman_tree(mem)
        self._setup_shiftbit_array(mem)

        self.assert_valid()

    def _setup_huffman_tree(self, mem):
        """Initialize the Huffman trees.

        Parameters
        ----------
        mem : mmap.mmap
            The input stream of ROM.
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

        Parameters
        ----------
        mem : mmap.mmap
            The input stream of ROM.
        """

        assert self.addr_shiftbit_array

        mem.seek(self.mapper.from_cpu(self.addr_shiftbit_array))
        self.shiftbit_array = mem.read(8)

        assert len(self.shiftbit_array) == 8

    def locate_message(self, mem, message_id):
        """Return the location where the messege data is stored.

        Parameters
        ----------
        mem : mmap.mmap
            The input stream of ROM.
        message_id : int
            An ID of a message data.

        Returns
        -------
        addr : int
            The address of the message data.
        shift : int
            The shift from `addr`.
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

        Parameters
        ----------
        mem : mmap.mmap
            The input stream of ROM.
        addr : int
            The initial address from which to read the variable
            length-bit string.
        shift : int
            The initial shift bit of the address.

        Returns
        -------
        addr : int
            the location of the next message data.
        shift : int
            The shift from `addr`.
        value : int
            A decoded character code.
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
        """Return a generator iterator."""

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
        """Return detailed location information of message data.

        Parameters
        ----------
        message_id : int
            An ID of a message data.

        Returns
        --------
        count : int
            The number how many message data are stored before the
            message.
        group : int
            The ID of grouping.
        """
        pass

    @abstractmethod
    def _do_is_leaf_node(self, node):
        """Determine if `node` is a leaf node.

        Parameters
        ----------
        node : int
            A two-byte value.

        Returns
        --------
        is_leaf : bool
            True if `node` is a leaf, False otherwise.
        """
        pass

    @abstractmethod
    def _do_next_location(self, addr, shift):
        """Return the next address to read data encoded.

        Parameters
        ----------
        addr : int
            The current address in CPU space.
        shift : int
            An one-byte value for mask.

        Returns
        --------
        addr : int
            The next address.
        shift : int
            The shift from `addr`.
        """
        pass

    @abstractmethod
    def _do_next_node(self, node):
        """Return the next node to traverse in the Huffman tree.

        Parameters
        ----------
        node : int
            The current node, a two-byte value.

        Returns
        --------
        node : int
            The next node, a two-byte value.
        """
        pass

class MessageGeneratorW(AbstractMessageGenerator):
    """This class is for DQ3 and DQ6."""

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
    """This class is for DQ5."""

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
