""" dqutils package - dqutils.database __init__ module
"""
from .reader import TableReader
from .parser import XmlParser
from .writer import CSVWriter
from .input import TextFileInput
from .output import TextFileOutput

def process_xml(xml_path):
    """Parse an XML file.

    This function is under construction.

    Args:
      xml_path (string): Path to an XML file.

    Returns:
      None.
    """

    reader = TableReader()
    parser = XmlParser()
    writer = CSVWriter()
    source = TextFileInput(source_path=xml_path)
    destination = TextFileOutput() # destination=sys.stdout

    table = reader.read(source, parser)

    #   self.apply_transforms()

    writer.write(table, destination)

    #   self.writer.assemble_parts()
