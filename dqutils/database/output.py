# -*- coding: utf-8 -*-
"""dqutils.database.output
"""
from abc import ABCMeta
from abc import abstractmethod
import sys

# pylint: disable=too-few-public-methods
class AbstractOutput(metaclass=ABCMeta):
    """This class imitates class Docutils.io.Output."""

    def __init__(self, destination=None, destination_path=None):
        """Initialize the instance of class AbstractOutput.

        Args:
          destination (unspecified): The destination for output data.
          destination_path (string): A path to the destination if the output
            is a file.
        """

        self.destination = destination
        self.destination_path = destination_path

    def __repr__(self):
        """Returns the official representation of this instance.

        Returns:
          (string): The official string representation.
        """

        return '{class_name}: destination={dest}, path={path}'.format(
            class_name=self.__class__,
            dest=self.destination,
            path=self.destination_path)

    @abstractmethod
    def write(self, data):
        """Write data to the destination."""
        pass

class NullOutput(AbstractOutput):
    """This class imitates class Docutils.io.NullOutput."""

    def write(self, data):
        """Return a null string."""
        return ''

class StringOutput(AbstractOutput):
    """This class imitates class Docutils.io.StringOutput."""

    def write(self, data):
        self.destination = data
        return self.destination

class TextFileOutput(AbstractOutput):
    """This class imitates class Docutils.io.FileOutput."""

    def __init__(self, destination=None, destination_path=None,
                 auto_close=True):
        """Initialize the instance of class TextFileOutput.

        Args:
          destination (unspecified): Either a file-like object or `None`.
          destination_path (string): A path to the destination.

        If both `destination` and `destination_path` are `None`,
        `sys.stdout` will be the destination.
        """

        super().__init__(destination, destination_path)
        self.opened = True
        self.auto_close = auto_close

        if not destination:
            if destination_path:
                self.opened = False
            else:
                self.destination = sys.stdout

        if not destination_path:
            try:
                self.destination_path = self.destination.name
            except AttributeError:
                pass

    def write(self, data):
        """Write data in a file-like object."""

        if not self.opened:
            self._open()

        try:
            self.destination.write(data)
        finally:
            if self.auto_close:
                self._close()

        return data

    def _open(self):
        """Open a file and set it to `self.destination`.

        Returns:
          None
        """
        path = self.destination_path
        self.destination = open(path, mode='w', encoding='utf-8')
        self.opened = True

    def _close(self):
        """Close the file `self.destination`.

        Returns:
          None
        """

        if self.destination not in (sys.stdout, sys.stderr):
            self.destination.close()
            self.opened = False
