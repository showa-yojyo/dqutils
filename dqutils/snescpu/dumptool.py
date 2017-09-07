"""
Example:
$ dumptool.py dqutils.dq3.dumptool 0xC8F323 0x36 10
#$0000\t#$00001F
#$0000\t#$0003E0
...
#$0035\t#$000001
[EOF]
"""

from argparse import ArgumentParser
from csv import (reader, writer, QUOTE_NONE)
import sys
from ..bit import get_bits
from .rom_image import RomImage
from .mapper import make_mapper

def int_wrapper(string):
    """A helper function."""

    if string.startswith('#$'):
        return int(string[2:], base=16)
    elif string.startswith('$'):
        return int(string[1:], base=16)

    return int(string, 0)

def formatter(mask_bits):
    """A helper function."""

    numbits = bin(mask_bits).count("1")
    if numbits > 16:
        return '{:06X}'
    elif numbits > 8:
        return '{:04X}'
    elif numbits < 4:
        return '{:d}'

    return '{:02X}'

COLUMN_OFFSET = 0
COLUMN_MASK_BITS = 1

def dump(title, address, sizeof_object, sizeof_array, source, destination):
    """Dump a sequence of typed objects in ROM image.

    Parameters
    ----------
    title: str
        The title of a game, e.g. 'DRAGONQUEST3'.
    address: int
        The address of the array in ROM space.
    sizeof_object: int
        length of the array, i.e. the number of objects.
    sizeof_array: int
        The size of the structure, class or object.
    source:
        A CSV reader object.
    destination:
        A CSV writer object.
    """

    members = [
        (int_wrapper(row[COLUMN_OFFSET]),
         int_wrapper(row[COLUMN_MASK_BITS]),)
        for row in source]

    fmts = [formatter(i[COLUMN_MASK_BITS]) for i in members]

    with RomImage(title) as rom:
        mapper = make_mapper(rom)
        rom.seek(mapper.from_cpu(address))
        for i in range(sizeof_array):
            chunk = rom.read(sizeof_object)

            output = ['{:04X}'.format(i)]
            output.extend(
                formatter.format(
                get_bits(chunk, member[COLUMN_OFFSET], member[COLUMN_MASK_BITS]))
                for (member, formatter) in zip(members, fmts))

            destination.writerow(output)

def parse_args(args):
    parser = ArgumentParser(description='A dump tool')
    parser.add_argument(
        'address',
        type=int_wrapper,
        help='address of the array in ROM space')
    parser.add_argument(
        'sizeof_object',
        type=int_wrapper,
        help='size of the structure, class or object')
    parser.add_argument(
        'sizeof_array',
        type=int_wrapper,
        help='length of the array (or the number of objects)')
    parser.add_argument(
        '--delimiter',
        default='\t',
        metavar='SEP',
        help='use SEP as fields separator (default to \\t)')
    return parser.parse_args(args)

def run(title, args=sys.argv[1:]):
    arguments = parse_args(args=args or ('--help',))
    delimiter = arguments.delimiter
    dump(
        title,
        arguments.address,
        arguments.sizeof_object,
        arguments.sizeof_array,
        reader(sys.stdin, delimiter=delimiter, quoting=QUOTE_NONE),
        writer(sys.stdout, delimiter=delimiter, quoting=QUOTE_NONE,
               lineterminator='\n'))
    return 0
