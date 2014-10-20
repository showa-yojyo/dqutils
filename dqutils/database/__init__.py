# -*- coding: utf-8 -*-
""" dqutils package - dqutils.database __init__ module
"""

from dqutils.database.parser import XmlParser
from dqutils.database.table import Table
from dqutils.database.format import CSVFormatter
from xml.dom.minidom import parse as parse_xml

def process_xml(xml_path):
    """Parse an XML file.

    This function is under construction.

    Args:
      xml_path (string): Path to an XML file.

    Returns:
      None.
    """
    parser = XmlParser()
    table = Table()

    with open(xml_path, 'r', encoding='utf-8') as source:
        parser.parse(parse_xml(source), table)

    # Output the header to stdout.
    formatter = CSVFormatter()
    print(formatter.format_header(table.columns))

    # Ouput one record to stdout.
    for i in table.rows:
        print(formatter.format_record(i))
