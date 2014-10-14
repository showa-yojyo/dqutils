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
    def make_header(self, title_list):
        """Write the table header row.

        Args:
          title_list (list): A list of names of members or fields.

        Returns:
          None.
        """
        pass

    @abstractmethod
    def write_record(self, value_list):
        """Write the table row for record contents.

        Args:
          value_list (list): A list of values of members or fields.

        Returns:
          None.
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

    def make_header(self, title_list):
        print(self.sep.join(title_list))

    def write_record(self, value_list):
        print(self.sep.join(value_list))
