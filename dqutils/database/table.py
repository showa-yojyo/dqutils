# -*- coding: utf-8 -*-
"""dqutils.database.table (prototype)
"""
from dqutils.database.format import CSVFormatter

class Table(object):
    """Under construction."""

    # pylint: disable=too-many-arguments
    def __init__(self,
                 rom=None,
                 romaddr=0,
                 reclen=0,
                 recnum=0,
                 formatter=None):
        self.field_list = []
        self.rom = rom
        self.romaddr = romaddr
        self.reclen = reclen
        self.recnum = recnum
        if formatter is None:
            formatter = CSVFormatter()
        self.formatter = formatter

    def add_field(self, name, **kwargs):
        """Add a member or field to this table.

        Args:
          name (string): The name of the member or field.
          **kwargs: Arbitrary keyword arguments.

        Returns:
          None.
        """
        self.field_list.append(make_field(name, **kwargs))

    def parse(self):
        """Under construction.

        Returns:
          None.
        """

        if self.rom is None or self.reclen == 0:
            return

        saved_ptr = self.rom.tell()
        try:
            # Locate the address of the array on ROM image.
            self.rom.seek(self.romaddr)

            # Setup table header information.
            self.do_make_header()

            for _ in range(self.recnum):
                # Obtain a byte sequence.
                byte_string = self.rom.read(self.reclen)
                self.do_write_record(
                    [field.process(byte_string) for field in self.field_list])
        finally:
            self.rom.seek(saved_ptr)

    def do_make_header(self):
        """Output the header to stdout.

        Returns:
          None.
        """

        self.formatter.make_header(
            [field.title() for field in self.field_list])

    def do_write_record(self, value_list):
        """Ouput one record to stdout.

        Args:
          value_list (list): A list of members or fields.

        Returns:
          None.
        """

        self.formatter.write_record(value_list)
