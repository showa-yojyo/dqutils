#!/usr/bin/env python
"""dumptool.py: TBW

Usage:
dumptool.py ROM_ADDRESS SIZEOF_ARRAY SIZEOF_OBJECT <STDIN>

Example:
$ dumptool.py dqutils.dq3.dumptool 0xC8F323 0x36 10
#$0000\t#$00001F
#$0000\t#$0003E0
...
#$0035\t#$000001
[EOF]

Note that TAB characters are used as CSV delimiter.
"""

import csv
import sys
from dqutils.bit import get_bits
from dqutils.snescpu.rom_image import RomImage
from dqutils.snescpu.mapper import make_mapper

def convert_to_number(text):
    """TODO: docstring"""

    if text.startswith('#$') or text.startswith('0x'):
        return int(text[2:], base=16)

    return int(text)

def format_column(attr):
    """TODO: docstring"""

    if attr > 0xFFFF:
        return '{:06X}'.format(attr)
    elif attr > 0xFF:
        return '{:04X}'.format(attr)
    elif attr > 9:
        return '{:02X}'.format(attr)

    return '{:d}'.format(attr)

COLUMN_OFFSET = 0
COLUMN_MASK_BITS = 1

# TODO: Reduce the number of parameters.
def dump_objects(title, address, sizeof_array, sizeof_object, reader, writer):
    """TODO: docstring
    """

    members = [(convert_to_number(row[COLUMN_OFFSET]),
                convert_to_number(row[COLUMN_MASK_BITS]),)
               for row in reader]

    with RomImage(title) as rom:
        mapper = make_mapper(rom)
        rom.seek(mapper.from_cpu(address))
        for i in range(sizeof_array):
            # ID
            output = ['{:04X}'.format(i)]

            # Raw data
            output.extend(format_column(
                get_bits(rom.read(sizeof_object), j[COLUMN_OFFSET],
                         j[COLUMN_MASK_BITS])) for j in members)

            writer.writerow(output)

def main(title):
    """The main function."""

    # TODO: Use argparse.ArgumentParser.
    address = convert_to_number(sys.argv[1])
    sizeof_object = convert_to_number(sys.argv[2])
    sizeof_array = convert_to_number(sys.argv[3])

    # TODO: CSV delimiter should be variable.
    reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_NONE)
    writer = csv.writer(sys.stdout, delimiter='\t', quoting=csv.QUOTE_NONE)
    dump_objects(title, address, sizeof_array, sizeof_object, reader, writer)

if __name__ == "__main__":
    main('DRAGONQUEST3')
