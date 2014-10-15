# -*- coding: utf-8 -*-
"""dqutils.database.table (prototype)
"""

class Table(object):
    """Under construction."""

    def __init__(self,
                 cpu_addr,
                 record_size,
                 record_num,
                 columns):
        self.cpu_addr = cpu_addr
        self.columns = columns
        self.record_size = record_size
        self.record_num = record_num

        self.rows = None

    def parse(self, mem, mapper):
        """Under construction.

        Args:
          mem (mmap): The ROM image.
          mapper (AbstractMapper): The mapper instance.

        Returns:
          None.
        """

        saved_ptr = mem.tell()
        try:
            # Locate the address of the array on ROM image.
            mem.seek(mapper.from_cpu(self.cpu_addr))

            self.rows = []

            # Obtain each byte sequence.
            for _ in range(self.record_num):
                byte_string = mem.read(self.record_size)
                self.rows.append(
                    [i.process(byte_string) for i in self.columns])

            assert len(self.rows) == self.record_num
        finally:
            mem.seek(saved_ptr)
