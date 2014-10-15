# -*- coding: utf-8 -*-
""" dqutils package - dqutils.database __init__ module
"""

from dqutils.database.parser import get_struct_info
from dqutils.database.parser import get_member_info
from dqutils.database.table import Table
from dqutils.database.format import CSVFormatter
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

    # Test preconditions.
    assert "title" in context
    assert "mapper" in context

    with open(xml_path, 'r', encoding='utf-8') as source:
        dom = parse_xml(source)

        # Handle the <struct> element in the XML tree.
        node = dom.getElementsByTagName('struct')[0]
        cpu_addr, record_size, record_num = get_struct_info(node)
        members = [get_member_info(i)
                   for i in node.getElementsByTagName('member')]

    # Read ROM image and list the records.
    table = Table(cpu_addr, record_size, record_num, members)
    with RomImage(context["title"]) as mem:
        table.parse(mem, make_mapper(context["mapper"]))

    # Output the header to stdout.
    formatter = CSVFormatter()
    print(formatter.format_header(members))

    # Ouput one record to stdout.
    for i in table.rows:
        print(formatter.format_record(i))
