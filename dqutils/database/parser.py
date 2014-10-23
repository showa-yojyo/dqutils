# -*- coding: utf-8 -*-
"""dqutils.database.parser - TBW
"""
from dqutils.database.field import make_field
from dqutils.rom_image import RomImage
from dqutils.rom_image import get_snes_header
from dqutils.mapper import make_mapper
from abc import ABCMeta
from abc import abstractmethod

# pylint: disable=too-few-public-methods
class AbstractParser(metaclass=ABCMeta):
    """Under construction."""

    def __init__(self):
        self.input_bytes = None
        self.table = None

    def parse(self, input_bytes, table):
        """Parse `input_bytes` into `table`.

        Args:
          input_bytes (bytes): TBW
          table (Table): TBW

        Returns:
          None
        """
        self._begin_parse(input_bytes, table)
        self._do_parse(input_bytes, table)
        self._end_parse()

    def _begin_parse(self, input_bytes, table):
        """Initial parse setup.

        Args:
          input_bytes (bytes): TBW
          table (Table): TBW

        Returns:
          None
        """
        self.input_bytes = input_bytes
        self.table = table

    @abstractmethod
    def _do_parse(self, input_bytes, table):
        """Override to parse `input_bytes` into data `table`.

        Args:
          input_bytes (bytes): TBW
          table (Table): TBW

        Returns:
          None
        """
        pass

    def _end_parse(self):
        """Finalize parse details.

        Returns:
          None
        """
        pass

class NullParser(AbstractParser):
    """TBW"""

    def _do_parse(self, input_bytes, table):
        pass

class XmlParser(AbstractParser):
    """Under construction."""

    def _do_parse(self, dom, table):
        # Handle the <struct> element in the XML tree.
        node = dom.getElementsByTagName('struct')[0]
        cpu_addr, record_size, record_num = XmlParser.get_struct_info(node)
        members = [XmlParser.get_member_info(i)
                   for i in node.getElementsByTagName('member')]

        title = dom.getElementsByTagName('rom')[0].getAttribute('name')

        # Read ROM image and list the records.
        with RomImage(title) as mem:
            mapper = make_mapper(header=get_snes_header(mem))

            # Locate the address of the array on ROM image.
            mem.seek(mapper.from_cpu(cpu_addr))

            # Obtain each byte sequence.
            rows = []
            for _ in range(record_num):
                byte_string = mem.read(record_size)
                rows.append(
                    [i.process(byte_string) for i in members])

        table.cpu_addr = cpu_addr
        table.record_size = record_size
        table.columns = members
        table.rows = rows

        assert len(rows) == record_num

    @staticmethod
    def get_struct_info(node):
        """Returns the information in order to retrieve data from ROM.

        Args:
          node (xmlnode): The `<struct>` node in the XML file.

        Returns:
          A tuple of (cpu address, record size, record count).
        """

        cpu_addr = 0
        if node.hasAttribute('cpuaddress'):
            cpu_addr = get_int(node.getAttribute('cpuaddress'))

        record_size = 0
        if node.hasAttribute('size'):
            record_size = get_int(node.getAttribute('size'))

        record_num = 0
        if node.hasAttribute('number'):
            record_num = get_int(node.getAttribute('number'))

        return cpu_addr, record_size, record_num

    @staticmethod
    def get_member_info(node):
        """Returns information of a member or field from a member element.

        A `member` element must have three attributes: `name`, `offset`,
        and `type`. Other attributes such as `mask` or `format' are optional.

        Args:
          node: A `<member>` DOM element.

        Returns:
          (AbstractField): An instance which has information of the member or
            field.
        """

        attrs = {}

        attr_name = node.getAttribute('name')
        attr_type = node.getAttribute('type')
        attrs['offset'] = get_int(node.getAttribute('offset'))

        attr_mask = get_int(node.getAttribute('mask'))
        if attr_mask:
            attrs['mask'] = attr_mask

        attr_format = node.getAttribute('format')
        if format:
            attrs['format'] = attr_format

        # pylint: disable=star-args
        return make_field(attr_name, attr_type, **attrs)

def get_int(text):
    """Cast a text value to a numeric value.

    Args:
      text (string): A text which represents an decimal or hexadecimal
        integer.

    Returns:
      An integer.
    """

    if not text:
        return 0

    if text.startswith('0x'):
        return int(text, 16)
    else:
        return int(text, 10)
