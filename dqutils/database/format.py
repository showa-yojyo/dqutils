# -*- coding: utf-8 -*-
"""dqutils.database.format -- (prototype)
"""
from abc import ABCMeta
from abc import abstractmethod

class AbstractTableFormatter(metaclass=ABCMeta):
    """Abstract class to format and write tabular data.

    Under construction.
    """

    def __init__(self):
        """The constructor."""
        pass

    @abstractmethod
    def format_header(self, columns):
        """Write the table header row.

        Args:
          columns (list): A list of members or fields.

        Returns:
          (string): TBW
        """
        pass

    @abstractmethod
    def format_record(self, row):
        """Write the table row for record contents.

        Args:
          row (list): A row in the target table.

        Returns:
          (string): TBW
        """
        pass

class CSVFormatter(AbstractTableFormatter):
    """Write tabular data in CSV format.

    Under construction.

    Attributes:
      sep (string): A separator character of CSV. Default to ':'.
    """

    def __init__(self, sep=':'):
        super().__init__()
        self.sep = sep

    def format_header(self, columns):
        return self.sep.join((i.title() for i in columns))

    def format_record(self, row):
        return self.sep.join(row)
