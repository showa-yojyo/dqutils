# -*- coding: utf-8 -*-
"""dqutils.database.writer -- (prototype)
"""
from abc import ABCMeta
from abc import abstractmethod
from io import StringIO

# pylint: disable=too-few-public-methods
# pylint: disable=abstract-class-little-used
class AbstractWriter(metaclass=ABCMeta):
    """Abstract class to format and write tabular data.

    Inspired by class Docutils.writers.Writer.

    Under construction.
    """

    def __init__(self):
        """The constructor."""
        self.table = None
        self.destination = None
        self.output = None

    def write(self, table, destination):
        """Under construction.

        Args:
          table (): TBW
          destination (): TBW

        Returns:
          (): TBW
        """
        self.table = table
        self.destination = destination
        self._do_translate()
        return self.destination.write(self.output)

    @abstractmethod
    def _do_translate(self):
        """Translate self.table and output to self.output."""
        pass

class CSVWriter(AbstractWriter):
    """Write tabular data in CSV format.

    Under construction.

    Attributes:
      sep (string): A separator character of CSV. Default to ':'.
    """

    def __init__(self, sep=':'):
        super().__init__()
        self.sep = sep

    def _do_translate(self):
        sep = self.sep
        table = self.table
        buffer = StringIO()

        # Write the table header row.
        print(sep.join((i.title() for i in table.columns)), file=buffer)

        # Write the table body rows.
        for i in table.rows:
            print(sep.join(i), file=buffer)

        self.output = buffer.getvalue()
