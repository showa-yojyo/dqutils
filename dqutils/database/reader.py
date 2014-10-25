# -*- coding: utf-8 -*-
"""dqutils.database.reader -- Define reader classes.
"""
from dqutils.database.table import Table
from abc import ABCMeta
from abc import abstractmethod

class AbstractReader(metaclass=ABCMeta):
    """This class imitates class Docutils.readers.Reader."""

    def __init__(self, parser=None):
        """Initialize the instance of class AbstractReader.

        Args:
          parser (AbstractParser): The underlying parser instance.
        """

        self.parser = parser
        self.source = None
        self.input = None
        self.document = None

    def read(self, source, parser):
        """Read contents of source and parse them.

        Args:
          source: A file-like object.
          parser (AbstractParser): The underlying parser instance.

        Returns:
          (object): An unspecified data.
        """

        self.source = source
        if not self.parser:
            self.parser = parser

        self.input = self.source.read()
        return self.parse()

    def parse(self):
        """Parse `self.input` into a model.

        Returns:
          (object): An unspecified data.
        """

        self.document = doc = self._do_new_document()
        self.parser.parse(self.input, doc)
        return doc

    @abstractmethod
    def _do_new_document(self):
        """Create and return a new empty model.

        Returns:
          (object): An unspecified data.
        """
        pass

class NullReader(AbstractReader):
    """This class is a null reader."""

    def _do_new_document(self):
        """Return a something empty.

        Returns:
          (object): ???
        """
        return ''

class TableReader(AbstractReader):
    """This class reads for table models."""

    def _do_new_document(self):
        """Create and return a new empty table model.

        Returns:
          (Table): An empty table model.
        """
        return Table()
