# -*- coding: utf-8 -*-
"""dqutils.database.reader -- (prototype)
"""
from dqutils.database.table import Table
from abc import ABCMeta
from abc import abstractmethod

class AbstractReader(metaclass=ABCMeta):
    """This class imitates class Docutils.readers.Reader."""

    def __init__(self, parser=None):
        """Initialize the instance of class AbstractReader.

        Args:
          parser (unspecified): The underlying parser instance.
        """

        self.parser = parser
        self.source = None
        self.input = None
        self.document = None

    def read(self, source, parser):
        """TBW"""

        self.source = source
        if not self.parser:
            self.parser = parser

        self.input = self.source.read()
        return self.parse()

    def parse(self):
        """Parse `self.input` into X.

        Returns:
          (unspecified): Unspecified.
        """

        self.document = doc = self._do_new_document()
        self.parser.parse(self.input, doc)
        return doc

    @abstractmethod
    def _do_new_document(self):
        """TBW"""
        pass

class NullReader(AbstractReader):
    """TBW"""

    def _do_new_document(self):
        pass

class TableReader(AbstractReader):
    """TBW"""

    def _do_new_document(self):
        return Table()
