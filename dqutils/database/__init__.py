# -*- coding: utf-8 -*-
""" dqutils package - dqutils.database __init__ module
"""

from dqutils.database.table import Table
from dqutils.database.parser import get_struct_info
from dqutils.database.parser import get_member_info
from dqutils.mapper import make_mapper
from dqutils.rom_image import RomImage
from xml.dom.minidom import parse as parse_xml

def process_xml(context, xml_path):
    """Parse an XML file.

    This function is under construction.

    Args:
      context (dict): TBW
      xml_path (string): Path to an XML file.

    Returns:
      None.
    """

    with open(xml_path, 'r', encoding='utf-8') as source:
        dom = parse_xml(source)

        # Handle the <struct> element in the XML tree.
        node = dom.getElementsByTagName('struct')[0]
        cpu_addr, record_size, record_num = get_struct_info(node)
        members = [get_member_info(i)
                   for i in node.getElementsByTagName('member')]
        read_array(
            context,
            members,
            cpu_addr,
            record_size,
            record_num)

def read_array(context, fields, cpu_addr, record_size, record_num):
    """Read ROM image and list the records.

    This function is under construction.

    Args:
      context (dict): TBW
      fields (list): TBW
      cpu_addr (int): The CPU address the data is stored.
      record_size (int): The size of a record in bytes.
      record_num (int): How many records are present in the ROM.

    Returns:
      None.
    """

    # Test preconditions.
    assert "title" in context
    assert "mapper" in context

    mapper = make_mapper(context["mapper"])

    with RomImage(context["title"]) as mem:
        table = Table(
            mem, mapper.from_cpu(cpu_addr), record_size, record_num)
        table.field_list = fields
        table.parse()
