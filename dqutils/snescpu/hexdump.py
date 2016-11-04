"""
A simple hexdump.
"""

from argparse import ArgumentParser
from ..release import VERSION
from .mapper import make_mapper
from .rom_image import RomImage
from .statemachine import StateMachine
from .states import DumpState

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
        nargs='+',
        help='the numbers of bytes per an object or record')
    parser.add_argument(
        'record_count',
        type=int,
        help='the number of records/objects')
    return parser

def dump(game_title, cmdline=None):
    """
    Print the contents of a ROM, byte-by-byte, in hexadecimal
    format.

    Parameters
    ----------
    game_title : str
        The title of a game, e.g. 'DRAGONQUEST3'.
    cmdline : iterable of str, optional
        The program arguments passed from the terminal window.
    """

    parser = create_argparser()
    args = parser.parse_args(cmdline)

    with RomImage(game_title) as rom:
        fsm = StateMachine(
            [DumpState], 'DumpState', rom)

        first = int(args.start, 16)
        delattr(args, 'start')
        last = first + sum(args.byte_count) * args.record_count
        last = min(last, (first & 0xFF0000) + 0x10000)

        fsm.run(first=first, last=last, **vars(args))
        fsm.unlink()
