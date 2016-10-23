"""
A simple hexdump.
"""

from argparse import ArgumentParser
from dqutils.release import VERSION
from dqutils.snescpu.mapper import make_mapper
from dqutils.snescpu.rom_image import (RomImage, get_snes_header)

FORMAT_STRING = '{:02X}/{:04X}:\t{}'

def create_argparser():
    """
    Return a command line parser for the application.

    Returns
    -------
    parser : argparse.ArgumentParser
        Storage of the command line parameters.
    """

    parser = ArgumentParser(description='A simple hexdump tool')
    parser.add_argument(
        '--version', action='version', version=VERSION)
    parser.add_argument(
        'start',
        help='the hexadecimal base CPU address from which to dump')
    parser.add_argument(
        'byte_count',
        type=int,
        help='the number of bytes per an object or record')
    parser.add_argument(
        'record_count',
        type=int,
        help='the number of records/objects')
    return parser

def dump(game_title, start, byte_count, record_count):
    """
    Do as hexdump.

    Parameters
    ----------
    game_title : str
        The game title that specifies the target ROM image.
    start : int
        The beginning of data area to be dumped.
    byte_count : int
        The number of bytes per an object to be displayed.
    record_count : int
        The number of objects to be displayed.
    """

    with RomImage(game_title) as rom:
        mapper = make_mapper(header=get_snes_header(rom))
        rom.seek(mapper.from_cpu(start))

        last_cpu_address = start + byte_count * record_count
        last_cpu_address = min(last_cpu_address,
                               (start & 0xFF0000) + 0x010000)

        cpu_address = start
        while cpu_address < last_cpu_address:
            bank = (cpu_address & 0xFF0000) >> 16
            offset = cpu_address & 0x00FFFF
            if offset + byte_count > 0x10000:
                data = rom.read(0x10000 - offset)
                cpu_address += 0x10000 - offset
            else:
                data = rom.read(byte_count)
                cpu_address += byte_count

            print(FORMAT_STRING.format(
                bank, offset, data.hex().upper()))

def main(game_title):
    """The main function.

    Parameters
    ----------
    game_title : str
        A str object for a game title.
    """

    parser = create_argparser()
    args = parser.parse_args()

    start = int(args.start, 16)
    dump(game_title, start, args.byte_count, args.record_count)
