# -*- coding: utf-8 -*-
""" dqutils package - dqutils.database __init__ module
"""
import sys
from dqutils.database.reader import XmlReader
from dqutils.database.parser import XmlParser
from dqutils.database.format import CSVFormatter

def process_xml(xml_path):
    """Parse an XML file.

    This function is under construction.

    Args:
      xml_path (string): Path to an XML file.

    Returns:
      None.
    """

    reader = XmlReader()
    table = reader.read(xml_path, XmlParser())

    formatter = CSVFormatter()
    formatter.write(table, sys.stdout)

