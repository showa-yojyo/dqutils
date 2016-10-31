"""dqutils.database.input -- Define input classes.
"""
from abc import (ABCMeta, abstractmethod)
import sys

# pylint: disable=too-few-public-methods
class AbstractInput(metaclass=ABCMeta):
    """This class imitates class Docutils.io.Input."""

    def __init__(self, source=None, source_path=None):
        """Initialize the instance of class AbstractInput.

        Args:
          source (unspecified): The source of input data.
          source_path (string): A path to the source if the input is
            a file.
        """

        self.source = source
        self.source_path = source_path

    def __repr__(self):
        """Returns the official representation of this instance.

        Returns:
          (string): The official string representation.
        """

        return '{class_name}: source={src}, path={path}'.format(
            class_name=self.__class__,
            src=self.source,
            path=self.source_path)

    @abstractmethod
    def read(self):
        """Read data from the source and return it."""
        pass

class NullInput(AbstractInput):
    """This class imitates class Docutils.io.NullInput."""

    def read(self):
        """Return a null string.

        Returns:
          (string): A empty string.
        """
        return ''

class StringInput(AbstractInput):
    """This class imitates class Docutils.io.StringInput."""

    def read(self):
        """Read data from the source and return it.

        Returns:
          (string): A string from `self.source`.
        """
        return self.source

class TextFileInput(AbstractInput):
    """This class imitates class Docutils.io.FileInput."""

    def __init__(self, source=None, source_path=None,
                 auto_close=True):
        """Initialize the instance of class TextFileInput.

        Args:
          source (unspecified): Either a file-like object or `None`.
          source_path (string): A path to a file, which is opened and
            then read.
          auto_close (bool): Close automatically after read (except when
              `sys.stdin` is the source).

        If both `source` and `source_path` are `None`,
        `sys.stdin` will be the source.
        """

        super().__init__(source, source_path)
        self.auto_close = auto_close

        if not source:
            if source_path:
                self.source = open(source_path, mode='r', encoding='utf-8')
            else:
                self.source = sys.stdin

        if not source_path:
            try:
                self.source_path = self.source.name
            except AttributeError:
                pass

    def read(self):
        """Read data in a file-like object and return it.

        Returns:
          (string): A string from `self.source`.
        """

        try:
            if self.source is sys.stdin:
                data = self.source.buffer.read()
            else:
                data = self.source.read()
        finally:
            if self.auto_close:
                self._close()

        return data

    def _close(self):
        """Close the file `self.source`.

        Returns:
          None
        """

        if self.source is not sys.stdin:
            self.source.close()
