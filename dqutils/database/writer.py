"""dqutils.database.writer -- Define writer classes.
"""
from abc import (ABCMeta, abstractmethod)
from io import StringIO

# pylint: disable=too-few-public-methods
# pylint: disable=abstract-class-little-used
class AbstractWriter(metaclass=ABCMeta):
    """This class imitates class Docutils.writers.Writer."""

    def __init__(self):
        """Initialize the instance of class AbstractWriter."""

        self.document = None
        self.destination = None
        self.output = None

    def write(self, document, destination):
        """Write a model data into the given destination.

        Args:
          documentument (object): An unspecified data.
          destination (AbstractOutput): ???

        Returns:
          (string): An unspecified data.
        """
        self.document = document
        self.destination = destination
        self._do_translate()
        return self.destination.write(self.output)

    @abstractmethod
    def _do_translate(self):
        """Translate self.document and output to self.output."""
        pass

class CSVWriter(AbstractWriter):
    """Write tabular data in CSV format.

    Attributes:
      sep (string): A separator character of CSV. Default to ':'.
    """

    def __init__(self, sep=':'):
        """Initialize the instance of class AbstractWriter.

        Args:
          sep (string): A separator character of CSV. Default to ':'.
        """

        super().__init__()
        self.sep = sep

    def _do_translate(self):
        sep = self.sep
        document = self.document
        buffer = StringIO()

        # Write the table header row.
        print(sep.join((i.title() for i in document.columns)), file=buffer)

        # Write the table body rows.
        for i in document.rows:
            print(sep.join(i), file=buffer)

        self.output = buffer.getvalue()
