# -*- coding: utf-8 -*-
"""dqutils.database.reader -- (prototype)
"""
from abc import ABCMeta
from abc import abstractmethod
from dqutils.database.table import Table
from xml.dom.minidom import parse as parse_xml

class AbstractReader(metaclass=ABCMeta):
    """Under construction.

    Inspired by class Docutils.readers.Reader.
    """

    def __init__(self, parser=None):
        """TBW"""

        self.parser = parser
        self.source_path = None
        self.input = None
        self.document = None

    def parse(self):
        """TBW"""

        self.document = doc = self._do_new_document()
        self.parser.parse(self.input, doc)
        return doc

    @abstractmethod
    def read(self, source_path, parser):
        """TBW"""
        pass

    @abstractmethod
    def _do_new_document(self):
        """TBW"""
        pass

class NullReader(AbstractReader):
    """TBW"""

    def read(self, source_path, parser):
        pass

    def _do_new_document(self):
        pass

class XmlReader(AbstractReader):
    """TBW"""

    def read(self, source_path, parser):
        """TBW"""

        self.source_path = source_path
        if not self.parser:
            self.parser = parser

        #self.input = self.source.read()
        with open(source_path, 'r', encoding='utf-8') as fin:
            self.input = parse_xml(fin)

        self.parse()
        return self.document

    def _do_new_document(self):
        """TBW"""
        return Table()
