"""
This module provides command line interface for the disassmbler.
"""

from argparse import ArgumentParser
from ..release import VERSION
from .rom_image import RomImage
from .mapper import make_mapper
from .statemachine import StateMachine

def create_argparser():
    """Return a command line parser for the application.

    Returns
    -------
    parser : argparse.ArgumentParser
        Storage of the command line parameters.
    """

    parser = ArgumentParser(description='A 65816 CPU disassembler')
    parser.add_argument('--version', action='version', version=VERSION)

    # Only optional arguments.
    parser.add_argument(
        '-a', '--accumulator-8bit',
        dest='accumulator_8bit',
        action='store_true',
        help='start in 8-bit accumulator mode (default is 16-bit)')
    parser.add_argument(
        '-x', '--index-8bit',
        dest='index_8bit',
        action='store_true',
        help='start in 8-bit X/Y mode (default is 16-bit)')

    # numbers are hex-only, no prefixes
    parser.add_argument(
        '-b', '--bank',
        dest='bank',
        metavar='BANK',
        help='disassemble bank BANK only')
    parser.add_argument(
        '-r', '--range',
        dest='range',
        metavar='FIRST[:LAST]',
        help='disassemble block [FIRST, LAST)')

    parser.add_argument(
        '-u', '--until-return',
        dest='until_return',
        action='store_true',
        help='exit immediately after processing RTI/RTS/RTL')

    return parser

def create_args(rom, cmdline_args=None):
    """Initialize the arguments of disassember.

    Parameters
    ----------
    rom : mmap.mmap
        A ROM image object.

    cmdline_args : iterable of str, optional
        The program arguments passed from the terminal window.

    Returns
    -------
    context : dict
        A dictionary of parameters for the disassembler state
        machine. This shall contain the following keys:

        - ``flags``: The initial value of the register status bits.
        - ``first``: The beginning of the CPU address from which
          to disassemble.
        - ``last``: The end of the CPU address to which to
          disassemble. If -1 is specified, then disassembling
          continues until the program counter reaches the end of ROM
          image.
        - ``until_return``: True if disassembling will end
          immediately after RTI, RTL, or RTS command is processed.

    mapper : AbstractMapper
        The mapper to the ROM image.
    """

    parser = create_argparser()
    args = parser.parse_args(cmdline_args)

    context = {}
    # properties for DQ6.
    mapper = make_mapper(rom=rom)

    # Initialize register flags, nvmxdizc.
    flags = 0x00
    if args.accumulator_8bit:
        flags |= 0x20
    if args.index_8bit:
        flags |= 0x10

    context['flags'] = flags

    # Set the address space [`first`, `last`) to disassemble,
    # where `first` is used to set `program_counter`.
    if args.bank:
        bank = int(args.bank, base=16)
        first = bank << 0x10
        last = first + mapper.bank_offset_size
    elif args.range:
        rng = args.range.split(':')
        first = int(rng[0], base=16)
        if len(rng) == 2 and rng[1]:
            last = int(rng[1], base=16)
        else:
            last = -1
    else:
        first = mapper.from_rom(0)
        last = -1 # dummy value; dynamically set

    context.update(
        first=first,
        last=last,
        until_return=args.until_return)

    return context, mapper

def main(game_title, state_machine_type=StateMachine):
    """The main function.

    Parameters
    ----------
    game_title : str
        A str object for a game title.
    """

    with RomImage(game_title) as rom:
        args, mapper = create_args(rom)
        fsm = state_machine_type(rom, mapper)
        fsm.run(**args)
